#include "nectar_net/practice_bootstrap.h"
#include <limits>
namespace nectar::net {
bool PracticeBootstrap::begin(CoopRole expected, std::uint64_t now) {
    CoopRole role;
    if (mPhase != PracticeLoadPhase::Closed || !mOwner.connected() || mOwner.session() ||
        !mOwner.role(role) || role != expected || now > std::numeric_limits<std::uint64_t>::max()-60000)
        return false;
    mRole = role; mNow = mStarted = now;
    return true;
}
bool PracticeBootstrap::beginHost(std::uint64_t id, std::uint64_t seed, std::uint64_t now) {
    if (!id || !begin(CoopRole::Host, now)) return false;
    mId = id; mScene = mHost.prepare(mAllowedScene, seed, now);
    mPhase = PracticeLoadPhase::Loading;
    return send(MessageType::ScenePrepare, encodeScenePrepare(mScene));
}
bool PracticeBootstrap::beginGuest(std::uint64_t now) {
    if (!begin(CoopRole::Guest, now)) return false;
    mPhase = PracticeLoadPhase::WaitingForHost;
    return true;
}
bool PracticeBootstrap::send(MessageType type, const std::vector<std::uint8_t>& payload) {
    if (!mId || mSent == std::numeric_limits<std::uint32_t>::max()) {
        mPhase = PracticeLoadPhase::Failed;return false;
    }
    Message m;m.header.type=type;m.header.sessionId=mId;m.header.sceneEpoch=mScene.epoch;
    m.header.sequence=mSent+1;m.payload=payload;
    std::vector<std::uint8_t> bytes;
    if (payload.empty() || !encodeMessage(m,bytes) || !mOwner.sendBeforeSession(bytes)) {
        mPhase = PracticeLoadPhase::Failed;return false;
    }
    ++mSent;return true;
}
bool PracticeBootstrap::startHostSession() {
    if (!mLocalLoaded || mHost.state()!=BarrierState::Ready) return true; // wait, never continue alone
    const auto start=mHost.start(1);
    if (!send(MessageType::SceneStart,encodeSceneStart(start)) ||
        !mOwner.beginSession(mId,static_cast<std::uint16_t>(mScene.epoch),1,mNow)) {
        mPhase=PracticeLoadPhase::Failed;return false;
    }
    mPhase=PracticeLoadPhase::SessionLoading;return true;
}
bool PracticeBootstrap::worldLoaded(std::uint32_t actual, std::uint64_t now) {
    if (mPhase!=PracticeLoadPhase::Loading || actual!=mAllowedScene || actual!=mScene.sceneId) return false;
    if (!mOwner.connected() || now<mNow || now<mStarted || now-mStarted>=60000) {
        mPhase=PracticeLoadPhase::Failed;return false;
    }
    mNow=now;
    if (mLocalLoaded) return true;
    if (mRole==CoopRole::Guest) {
        SceneReady ready;
        if (!mGuest.loaded(ready) || !send(MessageType::SceneReady,encodeSceneReady(ready))) return false;
    }
    mLocalLoaded=true;
    return mRole==CoopRole::Guest || startHostSession();
}
void PracticeBootstrap::receive(const TransportEvent& event,std::uint64_t now) {
    if(event.type==TransportEventType::Disconnected || event.type==TransportEventType::Error) {
        mPhase=PracticeLoadPhase::Failed;return;
    }
    if(event.type!=TransportEventType::Message || event.delivery!=Delivery::ReliableOrdered) return;
    Message m;
    if(decodeMessage(event.payload.data(),event.payload.size(),m,kActorMaxPacketBytes)!=DecodeError::None ||
       !m.header.sequence || m.header.sequence<=mReceived || !m.header.sessionId) return;
    bool accepted=false;
    if(mRole==CoopRole::Guest && mPhase==PracticeLoadPhase::WaitingForHost &&
       m.header.type==MessageType::ScenePrepare) {
        ScenePrepare proposed;
        if(decodeScenePrepare(m.payload.data(),m.payload.size(),proposed) && proposed.epoch &&
           proposed.epoch<=65535 && proposed.epoch==m.header.sceneEpoch &&
           proposed.sceneId==mAllowedScene && mGuest.onPrepare(proposed)) {
            mId=m.header.sessionId;mScene=proposed;mPhase=PracticeLoadPhase::Loading;accepted=true;
        }
    } else if(m.header.sessionId==mId && m.header.sceneEpoch==mScene.epoch) {
        if(mRole==CoopRole::Host && mPhase==PracticeLoadPhase::Loading && m.header.type==MessageType::SceneReady) {
            SceneReady ready;
            if(decodeSceneReady(m.payload.data(),m.payload.size(),ready) && mHost.onReady(ready)) {
                accepted=true;startHostSession();
            }
        } else if(mRole==CoopRole::Guest && mPhase==PracticeLoadPhase::Loading &&
                  mLocalLoaded && m.header.type==MessageType::SceneStart) {
            SceneStart start;
            if(decodeSceneStart(m.payload.data(),m.payload.size(),start) && start.startTick==1 &&
               mGuest.onStart(start)) {
                if(mOwner.beginSession(mId,static_cast<std::uint16_t>(mScene.epoch),1,now)) {
                    mPhase=PracticeLoadPhase::SessionLoading;accepted=true;
                } else mPhase=PracticeLoadPhase::Failed;
            }
        }
    }
    if(accepted)mReceived=m.header.sequence; // rejected high sequences never poison legitimate start
}
void PracticeBootstrap::pump(std::uint64_t now) {
    if(mPhase==PracticeLoadPhase::Closed || mPhase==PracticeLoadPhase::Failed ||
       mPhase==PracticeLoadPhase::SessionLoading) return;
    if(!mOwner.connected() || now<mNow || now<mStarted || now-mStarted>=60000) {
        mPhase=PracticeLoadPhase::Failed;return;
    }
    mNow=now;
    TransportEvent event;
    for(int count=0;count<64 && mOwner.pollBeforeSession(event);++count) {
        receive(event,now);
        if(mPhase==PracticeLoadPhase::Failed || mPhase==PracticeLoadPhase::SessionLoading) break;
    }
}
} // namespace nectar::net
