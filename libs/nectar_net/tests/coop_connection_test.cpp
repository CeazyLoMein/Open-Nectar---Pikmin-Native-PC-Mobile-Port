#include "nectar_net/coop_connection.h"
#include "nectar_net/practice_bootstrap.h"
#include "nectar_net/sim_network.h"
#include <cstdio>
#include <functional>
#include <memory>
using namespace nectar::net;
namespace {
int failures = 0;
void check(bool ok,const char* why) { if (!ok) { std::printf("FAIL %s\n",why);++failures; } }
struct Watched final : ITransport {
    std::unique_ptr<ITransport> inner;
    CoopConnection& owner;
    bool& badOrder;
    bool* blockSend = nullptr;
    Watched(std::unique_ptr<ITransport> p, CoopConnection& c, bool& bad, bool* block=nullptr)
        : inner(std::move(p)), owner(c), badOrder(bad), blockSend(block) {}
    bool listen(const Endpoint& e) override { return inner->listen(e); }
    bool connect(const Endpoint& e) override { return inner->connect(e); }
    bool send(Delivery d,const std::uint8_t* p,std::size_t n) override {return !(blockSend && *blockSend) && inner->send(d,p,n);}
    bool poll(TransportEvent& e) override {return inner->poll(e);}
    void disconnectPeer(bool flush) override { if(owner.session()) badOrder=true;inner->disconnectPeer(flush); }
    void close() override { if(owner.session()) badOrder=true;inner->close(); }
    TransportState state() const override {return inner->state();}
    bool stats(TransportStats& out) const override {return inner->stats(out);}
};
CompatibilityInfo identity(bool capability=true,bool known=true) {
    CompatibilityInfo info;info.game=1;info.region=1;
    if(known){info.build.fill(21);info.content.fill(51);}
    if(capability)requireCoopSessionCapability(info);
    return info;
}
PublisherBackends offlineBackends() {
    PublisherBackends b;
    b.listAddresses=[] {return LocalAddresses{};};
    b.randomBytes=[](std::uint8_t* out,std::size_t n) {
        for(std::size_t i=0;i<n;++i)out[i]=static_cast<std::uint8_t>(i+8);return true;
    };
    return b;
}
struct Pair {
    SimulatedNetwork net{20261025};
    bool badOrder=false, failHostSend=false;
    CoopConnection h,g; // outlive rooms and watched transports
    std::unique_ptr<HostRoom> host;
    std::unique_ptr<GuestJoin> guest;
    RoomStatus status;
    std::uint64_t now=0;
    Pair(bool capability=true,bool known=true,bool mismatch=false) {
        host=std::make_unique<HostRoom>([this] {
            return std::make_unique<Watched>(net.createHost(),h,badOrder,&failHostSend);
        },offlineBackends());
        guest=std::make_unique<GuestJoin>([this] {
            return std::make_unique<Watched>(net.createGuest(),g,badOrder);
        });
        RoomConfig config;config.compatibility=identity(capability,known);config.localPort=45000;
        config.automaticPortMapping=false;config.includeLanEndpoint=false;
        DirectEndpoint ep;ep.address={127,0,0,1};ep.port=45000;config.manualEndpoints={ep};
        check(host->open(config,1790000000,status)==RoomError::None,"room opens with injected offline discovery");
        check(!h.adoptHost(host)&&host,"listening host cannot transfer before authentication");
        auto info=identity(capability,known);if(mismatch)info.content[0]^=1;
        check(guest->start(status.code,info,1,1790000000,now)==JoinFailure::None,"guest connection starts");
        check(!g.adoptGuest(guest)&&guest,"connecting guest cannot transfer before compatibility");
        for(;now<1000;now+=5) {
            net.advance(now);TransportEvent e;
            while(host->transport()->poll(e)){}
            bool has=false;guest->poll(now,e,has);
            if(host->transport()->state()==TransportState::Connected && guest->transport() &&
               guest->transport()->state()==TransportState::Connected)break;
        }
    }
    void advance(std::uint64_t ms=100) {
        const auto end=now+ms;
        for(;now<end;now+=5) {net.advance(now);if(h.session())h.session()->pump(now);if(g.session())g.session()->pump(now);}
    }
    ~Pair(){g.close();h.close();check(!badOrder,"session is destroyed BEFORE owning transport closes");}
};
}
int main() {
    {
        Pair p(false);check(!p.h.adoptHost(p.host)&&p.host&&!p.g.adoptGuest(p.guest)&&p.guest,
                           "connection-only peer lacks required gameplay session capability");
    }
    {
        Pair p(true,false);check(!p.h.adoptHost(p.host)&&p.host&&!p.g.adoptGuest(p.guest)&&p.guest,
                                "unknown source/content identity never enters gameplay owner");
    }
    {
        Pair p(true,true,true);check(!p.h.adoptHost(p.host)&&p.host&&!p.g.adoptGuest(p.guest)&&p.guest,
                                    "incompatible peer cannot hand off either room");
    }
    {
        Pair p;check(p.h.adoptHost(p.host)&&p.g.adoptGuest(p.guest),"failed-start fixture adopts accepted rooms");
        p.failHostSend=true;
        check(!p.h.beginSession(123,1,1,p.now)&&!p.h.session()&&p.h.connected(),"failed initial status send retains room but not partial session");
        p.failHostSend=false;
        check(!p.h.beginSession(123,1,1,p.now),"failed issued scene context is retired against delayed start replay");
        check(p.h.beginSession(123,2,1,p.now),"retry uses a higher scene epoch");
    }
    {
        Pair p;
        const std::vector<std::uint8_t> queued{9,8,7,6};
        check(p.guest->transport()->send(Delivery::ReliableOrdered,queued.data(),queued.size()),"application bytes queued before transfer");
        check(p.h.adoptHost(p.host)&&!p.host&&p.g.adoptGuest(p.guest)&&!p.guest,
              "accepted handoff MOVES ownership, original UI owners become empty");
        CoopRole role=CoopRole::Guest;
        check(p.h.role(role)&&role==CoopRole::Host&&p.g.role(role)&&role==CoopRole::Guest,"host/guest identity retained after move");
        check(p.h.connected()&&p.g.connected(),"handoff keeps same live authenticated connection");
        bool found=false;
        for(int i=0;i<100&&!found;++i) {
            p.net.advance(++p.now);TransportEvent e;
            while(p.h.pollBeforeSession(e))if(e.type==TransportEventType::Message&&e.payload==queued)found=true;
        }
        check(found,"unread message survives ownership transfer without UI consuming it");
        auto extra=std::make_unique<HostRoom>();
        check(!p.h.adoptHost(extra)&&extra,"occupied game owner cannot silently replace its room");
        check(!p.g.sendBeforeSession({})&&!p.g.sendBeforeSession(std::vector<std::uint8_t>(1201)),"bootstrap send has explicit size bounds");
        check(!p.h.beginSession(0,1,1,p.now)&&!p.h.session()&&p.h.connected(),"failed start keeps accepted room available");
        check(p.h.beginSession(100,1,1,p.now)&&p.g.beginSession(100,1,1,p.now),"same accepted scene begins under retained owner");
        TransportEvent unchanged;unchanged.detail="unchanged";
        check(!p.h.pollBeforeSession(unchanged)&&unchanged.detail=="unchanged"&&!p.g.sendBeforeSession(queued),
              "bootstrap poll/send cannot compete with CoopSession after start");
        CaptainState a,b;b.player=1;
        std::vector<std::vector<std::uint8_t>> packets;
        check(packActorFrame(100,1,1,1,{captainRecord(1,a),captainRecord(1,b)},1000,{},packets)&&
              p.h.session()->publishActors(packets,p.now),"actual session frame crosses retained link");
        p.advance();
        check(p.g.session()->actors().captains.size()==2,"retained guest receives complete captain frame");
        check(p.h.session()->confirmWorldLoaded()&&p.g.session()->confirmWorldLoaded()&&
              p.h.session()->setReady(true)&&p.g.session()->setReady(true),"explicit fixture world loading and readiness");
        p.advance();
        NetInputFrame input;input.tick=4;input.stickY=75;
        check(p.g.session()->publishInput({input},p.now),"guest inputs use retained session");p.advance();
        NetInputFrame applied;InputHealth health;
        check(p.h.session()->consumeGuestInput(4,applied,health)&&health==InputHealth::Live&&applied.stickY==75,
              "host applies guest controls after UI room has relinquished ownership");
        p.h.endSession();p.g.endSession();
        check(p.h.connected()&&p.g.connected()&&!p.h.session()&&!p.g.session(),"end session does not destroy retained room");
        check(!p.h.beginSession(100,1,1,p.now)&&!p.g.beginSession(100,1,1,p.now),"end/restart cannot replay retired scene context");
        check(p.h.beginSession(100,2,1,p.now)&&p.g.beginSession(100,2,1,p.now),"higher accepted epoch begins fresh held scene");
        check(p.g.session()->actors().captains.empty()&&!p.g.session()->confirmWorldLoaded(),"previous scene baseline does not imply loaded new world");
        check(!p.h.prepareHostRejoin(),"a live or loading session cannot be silently replaced");
        p.g.close();p.advance();
        check(!p.g.session()&&!p.g.connected()&&p.h.session()->phase()==CoopPhase::WaitingForPartner,
              "guest close safely stops session and freezes retained host");
        check(!p.g.prepareHostRejoin(),"guest cannot take ownership of host listener");
        check(p.h.prepareHostRejoin()&&!p.h.session()&&!p.h.connected(),
              "lost host session retires before resetting peer, retaining its listener");
        check(!p.h.prepareHostRejoin(),"duplicate rejoin setup cannot reset a new peer");
        auto mismatch=std::make_unique<GuestJoin>([&p]{return p.net.createGuest();});
        auto wrong=identity();wrong.content[0]^=1;
        check(mismatch->start(p.status.code,wrong,1,1790000000,p.now)==JoinFailure::None,
              "incompatible guest starts a fresh handshake");
        JoinProgress mismatchProgress=JoinProgress::Connecting;
        for(int i=0;i<400 && mismatchProgress!=JoinProgress::Failed;++i) {
            p.now+=5;p.net.advance(p.now);p.h.pollHostRejoin();
            TransportEvent e;bool has=false;mismatchProgress=mismatch->poll(p.now,e,has);
        }
        std::printf("REJOIN mismatch progress=%d failure=%d hostConnected=%d hostSession=%d\n",int(mismatchProgress),int(mismatch->failure()),int(p.h.connected()),int(p.h.session()!=nullptr));
        check(mismatchProgress==JoinProgress::Failed &&
              (mismatch->failure()==JoinFailure::Incompatible || mismatch->failure()==JoinFailure::Unreachable) &&
              !p.h.connected() && !p.h.session(),
              "incompatible rejoin is rejected without opening a session or destroying host room");
        mismatch->cancel();
        auto rejoin=std::make_unique<GuestJoin>([&p]{return p.net.createGuest();});
        check(rejoin->start(p.status.code,identity(),1,1790000000,p.now)==JoinFailure::None,
              "partner can reuse the same private room code");
        for(int i=0;i<400;++i) {
            p.now+=5;p.net.advance(p.now);p.h.pollHostRejoin();
            TransportEvent e;bool has=false;rejoin->poll(p.now,e,has);
            if(p.h.connected() && rejoin->transport() && rejoin->transport()->state()==TransportState::Connected)break;
        }
        check(p.h.connected()&&p.g.adoptGuest(rejoin),"same host accepts a freshly authenticated compatible partner");
        check(!p.h.beginSession(100,2,1,p.now),"retired session identity cannot be replayed after reconnect");
        check(p.h.beginSession(101,1,1,p.now)&&p.g.beginSession(101,1,1,p.now),
              "new session is created only after fresh authentication");
        check(!p.h.session()->hostShouldAdvanceWorld()&&!p.g.session()->confirmWorldLoaded(),
              "reconnection cannot resume without a fresh baseline and readiness");
        p.h.close();p.h.close();
        check(!p.h.session()&&!p.h.connected()&&!p.h.role(role),"close is idempotent and clears owned identity");
    }

    {
        Pair p;check(p.h.adoptHost(p.host)&&p.g.adoptGuest(p.guest),"bootstrap owns compatible retained rooms");
        PracticeBootstrap hs(p.h), gs(p.g);
        check(!hs.beginGuest(p.now)&&!gs.beginHost(400,42,p.now)&&!hs.beginHost(0,42,p.now),"bootstrap rejects wrong role and zero context");
        check(gs.beginGuest(p.now),"guest waits for host proposal");
        ScenePrepare wrong;wrong.epoch=1;wrong.sceneId=99;
        Message bad;bad.header.type=MessageType::ScenePrepare;bad.header.sequence=999999;bad.header.sessionId=400;
        bad.header.sceneEpoch=1;bad.payload=encodeScenePrepare(wrong);std::vector<std::uint8_t> bytes;
        check(encodeMessage(bad,bytes)&&p.h.sendBeforeSession(bytes),"bad-area high-sequence proposal injected");
        auto step=[&] {p.now+=5;p.net.advance(p.now);hs.pump(p.now);gs.pump(p.now);};
        for(int i=0;i<10;++i)step();
        check(gs.phase()==PracticeLoadPhase::WaitingForHost&&!p.g.session(),"unapproved area cannot choose guest level or poison sequence");
        check(hs.beginHost(400,42,p.now),"host proposes local-policy familiar test area");
        for(int i=0;i<20&&gs.phase()!=PracticeLoadPhase::Loading;++i)step();
        check(gs.phase()==PracticeLoadPhase::Loading&&gs.sessionId()==400&&gs.scene().sceneId==0&&gs.scene().seed==42,
              "guest adopts exact authenticated session, area, epoch and seed");
        check(!gs.worldLoaded(99,p.now)&&!p.g.session(),"wrong actual loaded area cannot acknowledge");
        SceneStart premature;premature.epoch=1;premature.startTick=1;
        bad.header.type=MessageType::SceneStart;bad.payload=encodeSceneStart(premature);bytes.clear();
        check(encodeMessage(bad,bytes)&&p.h.sendBeforeSession(bytes),"premature high-sequence start injected");
        for(int i=0;i<10;++i)step();
        check(!p.g.session()&&gs.phase()==PracticeLoadPhase::Loading,"start before actual guest load is ignored without sequence poisoning");
        check(gs.worldLoaded(0,p.now),"guest engine attests actual area load");
        for(int i=0;i<20;++i)step();
        check(!p.h.session()&&!p.g.session(),"guest load alone does not start either world");
        check(hs.worldLoaded(0,p.now),"host also attests area load");
        for(int i=0;i<20&&gs.phase()!=PracticeLoadPhase::SessionLoading;++i)step();
        check(hs.phase()==PracticeLoadPhase::SessionLoading&&gs.phase()==PracticeLoadPhase::SessionLoading&&
              p.h.session()&&p.g.session(),"both loaded hands one poll owner to same accepted CoopSession");
        check(!p.h.session()->hostShouldAdvanceWorld()&&!p.g.session()->canIssueCommands()&&
              !p.g.session()->confirmWorldLoaded(),"scene handshake alone cannot claim full actors/world ready or enable gameplay");
    }
    {
        Pair p;check(p.h.adoptHost(p.host)&&p.g.adoptGuest(p.guest),"timeout fixture adopts rooms");
        PracticeBootstrap hs(p.h),gs(p.g);check(hs.beginHost(500,0,p.now)&&gs.beginGuest(p.now),"load timeout starts held");
        for(int i=0;i<20;++i){p.now+=5;p.net.advance(p.now);hs.pump(p.now);gs.pump(p.now);}
        check(hs.worldLoaded(0,p.now),"host loaded but partner still loading");
        p.now+=60000;hs.pump(p.now);gs.pump(p.now);
        check(hs.phase()==PracticeLoadPhase::Failed&&gs.phase()==PracticeLoadPhase::Failed&&
              !p.h.session()&&!p.g.session(),"load timeout fails closed, never silently continues campaign alone");
    }
    {
        Pair p;check(p.h.adoptHost(p.host)&&p.g.adoptGuest(p.guest),"failed start-send fixture adopts rooms");
        PracticeBootstrap hs(p.h),gs(p.g);check(hs.beginHost(600,0,p.now)&&gs.beginGuest(p.now),"failed start-send bootstrap begins");
        for(int i=0;i<20;++i){p.now+=5;p.net.advance(p.now);hs.pump(p.now);gs.pump(p.now);}
        check(hs.worldLoaded(0,p.now),"host ready while waiting for guest engine load");
        p.failHostSend=true;check(gs.worldLoaded(0,p.now),"guest sends ready before host send failure");
        for(int i=0;i<20;++i){p.now+=5;p.net.advance(p.now);hs.pump(p.now);gs.pump(p.now);}
        check(hs.phase()==PracticeLoadPhase::Failed&&!p.h.session()&&!p.g.session(),"failed start announcement cannot leave partially running session");
    }


    {
        CoopConnection pending;
        Message m;m.header.type=MessageType::ScenePrepare;m.header.sessionId=900;m.header.sceneEpoch=1;m.header.sequence=1;
        m.payload=encodeScenePrepare({1,0,42});TransportEvent e;e.type=TransportEventType::Message;
        check(encodeMessage(m,e.payload),"bounded pending fixture encodes");
        for(int i=0;i<64;++i){auto copy=e;check(pending.bufferBeforeHandoff(std::move(copy)),"bounded pending event accepted");}
        const auto original=e.payload;
        check(!pending.bufferBeforeHandoff(std::move(e))&&e.payload==original,"full handoff queue refuses without consuming input");
        pending.close();
        check(pending.bufferBeforeHandoff(std::move(e)),"close clears old pending data and capacity");
        TransportEvent malformed;malformed.type=TransportEventType::Message;malformed.payload={1,2,3};
        check(!pending.bufferBeforeHandoff(std::move(malformed))&&malformed.payload.size()==3,"malformed app bytes refused without mutation");
    }
    {
        Pair p;check(p.h.adoptHost(p.host)&&p.h.beginSession(901,1,1,p.now),"host begins fixture before guest UI hands off");
        CaptainState a,b;b.player=1;std::vector<std::vector<std::uint8_t>> packets;
        check(packActorFrame(901,1,1,1,{captainRecord(1,a),captainRecord(1,b)},1000,{},packets)&&
              p.h.session()->publishActors(packets,p.now)&&p.h.session()->confirmWorldLoaded()&&p.h.session()->setReady(true),
              "host queues baseline and ready view while guest is still native UI owner");
        int remembered=0;
        for(int i=0;i<30;++i){p.now+=5;p.net.advance(p.now);TransportEvent e;bool has=false;
            do{has=false;p.guest->poll(p.now,e,has);
                if(has&&e.type==TransportEventType::Message){check(p.g.bufferBeforeHandoff(std::move(e)),"native-style pending session message buffered");++remembered;}
            }while(has);
        }
        check(remembered>=3&&p.g.adoptGuest(p.guest)&&p.g.beginSession(901,1,1,p.now),"guest transfers already-received messages with live owner");
        p.advance();
        check(p.g.session()->actors().captains.size()==2&&p.g.session()->view().loaded[0]&&p.g.session()->view().ready[0],
              "CoopSession replays pending baseline/status before reading later socket messages");
        TransportEvent invalid;invalid.type=TransportEventType::Message;
        check(!p.g.bufferBeforeHandoff(std::move(invalid)),"retired UI cannot append to gameplay queue");
    }

    if(!failures)std::puts("PASS exclusive room handoff: gates, queued bytes, single poll owner, actual session input, retired epoch and shutdown order");
    return failures?1:0;
}
