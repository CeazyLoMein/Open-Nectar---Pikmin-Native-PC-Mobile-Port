#include "netplay/pc_coop_world.h"
#include "nectar_net/entity_registry.h"
#include "nectar_net/pikmin_replication.h"
#include "Navi.h"
#include "NaviMgr.h"
#include "Piki.h"
#include "PikiMgr.h"
#include "teki.h"
#include "Graphics.h"
#include "Material.h"
#include <cmath>
#include <memory>
#include <set>
#include <algorithm>
#include <functional>

namespace {
namespace net = nectar::net;
struct CaptureState {
    net::HostEntityRegistry registry;
    std::uint64_t session = 0, lastFrame = 0, lastTick = 0;
    bool running = false, practiceOwners = false;
};
// No allocation or manager traversal until explicitly begun by a future session.
std::unique_ptr<CaptureState> state;
bool emergencyHold=false;
struct GuestPikmin {
    Piki* local = nullptr;
    std::uint16_t color = 0;
    net::PikminState applied;
};
struct VisualPikmin { std::size_t slot = 0; net::PikminState applied; };
struct GuestState {
    std::uint64_t session = 0, lastFrame = 0, lastTick = 0, ids[2] = {};
    std::uint16_t epoch = 0;
    Navi* captains[2] = {};
    net::CaptainState captainStates[2];
    bool invalidated = false, pikminBound = false, havePikminFrame = false;
    std::map<std::uint64_t, GuestPikmin> pikmin;
    Teki* enemy=nullptr;
    std::uint64_t enemyId=0;
    bool enemyRetired=false,enemyVisible=false;
    net::EnemyState enemyState;
    std::vector<Piki*> orderedPikmin, liveScratch;
    PikiMgr* visualManager = nullptr;
    std::vector<ViewPiki*> visualSlots;
    std::map<std::uint64_t, VisualPikmin> visuals;
};
std::unique_ptr<GuestState> guest;
void clearGuestEnemyTargets() {
    if(!guest || !guest->enemy || !naviMgr)return;
    Iterator navis(naviMgr);CI_LOOP(navis) {
        auto* n=static_cast<Navi*>(*navis);
        if(n && n->mPcLockTarget==guest->enemy)n->mPcLockTarget=nullptr;
    }
}

AnimInfo* enemyAnimation(Teki* enemy,unsigned index) {
    if(!enemy || !enemy->mTekiShape || !enemy->mTekiShape->mAnimMgr || index>=1024)return nullptr;
    auto* a=static_cast<AnimInfo*>(enemy->mTekiShape->mAnimMgr->mAnimList.mChild);
    for(unsigned i=0;a && i<index;++i)a=static_cast<AnimInfo*>(a->mNext);
    return a && a->mData && a->mData->mTotalFrameCount>0 ? a : nullptr;
}
bool validateEnemy(const net::ActorFrame& frame) {
    if(!guest || frame.enemies.size()>1)return false;
    if(frame.enemies.empty())return true;
    const auto& e=*frame.enemies.begin();net::NetEntityId id;
    if(!guest->enemy || guest->enemyRetired || !net::NetEntityId::unpack(e.first,id) || id.sceneEpoch!=guest->epoch
       || id.kind!=net::EntityKind::Enemy || (guest->enemyId && guest->enemyId!=e.first)
       || !net::validEnemyState(e.second) || e.second.type!=guest->enemy->mTekiType)return false;
    auto* a=enemyAnimation(guest->enemy,e.second.animation);
    return a && e.second.animationFrame<=a->mData->mTotalFrameCount;
}
void applyEnemy(const net::ActorFrame& frame,bool presentation=false) {
    if(frame.enemies.empty()) {
        if(guest->enemyId)guest->enemyRetired=true;
        guest->enemyVisible=false;
        if(guest->enemy)guest->enemy->clearTekiOption(TEKIOPT_Visible|TEKIOPT_LifeGaugeVisible);
        return;
    }
    const auto& e=*frame.enemies.begin();auto* local=guest->enemy;const auto& s=e.second;
    guest->enemyId=e.first;if(!presentation)guest->enemyState=s;guest->enemyVisible=s.visible!=0;
    local->mSRT.t.set(s.position.x,s.position.y,s.position.z);local->mLastPosition=local->mSRT.t;
    local->mSRT.s.set(s.scale.x,s.scale.y,s.scale.z);local->mFaceDirection=s.faceDirection;local->_3A4=s.tilt;local->mHealth=s.health;
    local->mLifeGauge.updValue(s.health,s.maxHealth);
    pc_coop_world_prepare_enemy_gauge(local->mLifeGauge,s.health,s.maxHealth);
    if(s.visible)local->setTekiOption(TEKIOPT_Visible|TEKIOPT_LifeGaugeVisible);
    else local->clearTekiOption(TEKIOPT_Visible|TEKIOPT_LifeGaugeVisible);
    auto* a=local->mTekiAnimator;a->mListener=nullptr;a->mCurrentKeyIndex=-1;a->mPlayState=ANIMSTATE_Inactive;a->mMotionIdx=-1;
    a->mCurrentAnimID=s.animation;a->mAnimInfo=enemyAnimation(local,s.animation);
    a->mAnimationCounter=std::min(s.animationFrame,float(a->mAnimInfo->mData->mTotalFrameCount-1));
}
bool findCaptains(Navi* (&found)[2]) {
    if (!naviMgr) return false;
    Iterator it(naviMgr);
    CI_LOOP(it) {
        Navi* n = static_cast<Navi*>(*it);
        if (!n || n->mNaviID < 0 || n->mNaviID > 1 || found[n->mNaviID] || !n->isAlive()) return false;
        found[n->mNaviID] = n;
    }
    return found[0] && found[1];
}
std::uint64_t lastSession = 0;
std::uint32_t lastEpoch = 0;
std::uintptr_t key(const void* actor) { return reinterpret_cast<std::uintptr_t>(actor); }
std::uint8_t leader(Navi* associated, Navi* const (&captains)[2])
{
    for (std::uint8_t p = 0; p < 2; ++p) if (associated && associated == captains[p]) return p;
    return net::HostEntityRegistry::kUnowned;
}
}

bool pc_coop_world_active() { return state != nullptr || guest != nullptr; }
bool pc_coop_world_has_guest() { return guest != nullptr; }
bool pc_coop_world_may_advance() { return !emergencyHold && !guest && (!state || state->running); }
void pc_coop_world_stop() { emergencyHold=true;if(state)state->running=false; }
bool pc_coop_world_set_host_running(std::uint64_t sessionId, std::uint32_t epoch, bool running)
{
    if (!state || state->session != sessionId || state->registry.epoch() != epoch) return false;
    if (running) {
        Navi* captains[2] = {};
        if (!findCaptains(captains)) { state->running = false; return false; }
    }
    state->running = running;
    return true;
}
bool pc_coop_world_guest_active() { return guest && !guest->invalidated; }
bool pc_coop_world_begin_guest(std::uint64_t sessionId, std::uint32_t epoch)
{
    if (state || guest || !sessionId || !epoch || epoch > 65535 ||
        (sessionId == lastSession && epoch <= lastEpoch)) return false;
    auto pending = std::make_unique<GuestState>();
    if (!findCaptains(pending->captains)) return false;
    pending->session = sessionId;
    pending->epoch = static_cast<std::uint16_t>(epoch);
    guest = std::move(pending);
    lastSession = sessionId; lastEpoch = epoch;
    return true;
}
namespace {
struct CaptainApply {
    Navi* local[2] = {};
    const net::CaptainState* incoming[2] = {};
    std::uint64_t ids[2] = {};
};
bool prepareCaptains(std::uint64_t sessionId, std::uint32_t epoch,
                     const net::ActorFrame& frame, CaptainApply& pending)
{
    if (!guest || guest->invalidated || sessionId != guest->session || epoch != guest->epoch ||
        !frame.frame || frame.frame <= guest->lastFrame || frame.tick < guest->lastTick ||
        frame.captains.size() != 2) return false;
    if (!findCaptains(pending.local) || pending.local[0] != guest->captains[0] ||
        pending.local[1] != guest->captains[1]) return false;
    for (const auto& entry : frame.captains) {
        net::NetEntityId id;
        const auto& value = entry.second;
        if (!net::NetEntityId::unpack(entry.first, id) || id.sceneEpoch != guest->epoch ||
            id.kind != net::EntityKind::Captain || value.player > 1 || pending.incoming[value.player]) return false;
        auto bytes = net::encodeCaptainState(value);
        net::CaptainState checked;
        if (!net::decodeCaptainState(bytes.data(), bytes.size(), checked) ||
            !pending.local[value.player]->pcCoopVisualValidate(value) ||
            (value.lockedEnemy && (!guest->enemy || frame.enemies.size()!=1)) ||
            (guest->ids[value.player] && guest->ids[value.player] != entry.first)) return false;
        pending.incoming[value.player] = &value;
        pending.ids[value.player] = entry.first;
    }
    return pending.incoming[0] && pending.incoming[1];
}
void commitCaptains(const CaptainApply& pending, const net::ActorFrame& frame)
{
    for (int player = 0; player < 2; ++player) {
        Navi* n = pending.local[player]; const auto& value = *pending.incoming[player];
        n->mSRT.t.x = value.position.x; n->mSRT.t.y = value.position.y; n->mSRT.t.z = value.position.z;
        n->mLastPosition = n->mSRT.t;
        n->mVelocity.x = value.velocity.x; n->mVelocity.y = value.velocity.y; n->mVelocity.z = value.velocity.z;
        n->mFaceDirection = value.faceDirection;
        n->mSRT.r.y = value.faceDirection;
        n->pcCoopVisualApply(value);
        n->mPcLockTarget=value.lockedEnemy ? guest->enemy : nullptr;
        guest->ids[player] = pending.ids[player];
        guest->captainStates[player] = value;
    }
    guest->lastFrame = frame.frame; guest->lastTick = frame.tick;
}
bool livePikmin(std::vector<Piki*>& live)
{
    if (!pikiMgr) return false;
    constexpr std::size_t maximum = net::ActorFrameLimits{}.maxRecords - 2;
    // Reused scratch storage: no per-Pikmin tree allocation on every frame.
    live.clear();
    if (live.capacity() < maximum) live.reserve(maximum);
    Iterator it(pikiMgr);
    CI_LOOP(it) {
        Piki* p = static_cast<Piki*>(*it);
        if (!p) return false;
        if (!p->isAlive()) continue;
        if (p->mColor >= 3 || live.size() >= maximum) return false;
        live.push_back(p);
    }
    std::sort(live.begin(), live.end(), std::less<Piki*>{});
    return std::adjacent_find(live.begin(), live.end()) == live.end();
}
}

bool pc_coop_world_apply_guest_captains(std::uint64_t sessionId, std::uint32_t epoch,
                                       const net::ActorFrame& frame)
{
    CaptainApply pending;
    if (!frame.enemies.empty() || (guest && (guest->pikminBound || guest->visualManager)) || !prepareCaptains(sessionId, epoch, frame, pending)) return false;
    commitCaptains(pending, frame);
    return true;
}

bool pc_coop_world_bind_guest_pikmin(std::uint64_t sessionId, std::uint32_t epoch,
    const std::vector<PcCoopGuestPikminBinding>& bindings)
{
    if (!guest || guest->invalidated || guest->pikminBound || guest->visualManager || sessionId != guest->session ||
        epoch != guest->epoch || bindings.size() > net::ActorFrameLimits{}.maxRecords - 2) return false;
    Navi* captains[2] = {};
    if (!findCaptains(captains) || captains[0] != guest->captains[0] || captains[1] != guest->captains[1]) return false;
    std::vector<Piki*> live;
    if (!livePikmin(live) || live.size() != bindings.size()) return false;
    std::set<Piki*> remaining(live.begin(), live.end());
    std::map<std::uint64_t, GuestPikmin> pending;
    for (const auto& binding : bindings) {
        net::NetEntityId id;
        if (!net::NetEntityId::unpack(binding.id, id) || id.sceneEpoch != guest->epoch ||
            id.kind != net::EntityKind::Pikmin || !binding.local || !remaining.erase(binding.local) ||
            pending.count(binding.id)) return false;
        GuestPikmin value; value.local = binding.local; value.color = binding.local->mColor;
        pending.emplace(binding.id, value);
    }
    if (!remaining.empty()) return false;
    guest->liveScratch.reserve(net::ActorFrameLimits{}.maxRecords - 2);
    guest->orderedPikmin.swap(live);
    guest->pikmin.swap(pending);
    guest->pikminBound = true;
    return true;
}

bool pc_coop_world_apply_guest_actors(std::uint64_t sessionId, std::uint32_t epoch,
    const net::ActorFrame& frame)
{
    CaptainApply captains;
    if (!guest || !guest->pikminBound || !frame.enemies.empty() || frame.pikmin.size() != guest->pikmin.size() ||
        !prepareCaptains(sessionId, epoch, frame, captains)) return false;
    if (!livePikmin(guest->liveScratch) || guest->liveScratch != guest->orderedPikmin) return false;
    // Prepare ALL allocations/value validation before any engine write. Bound
    // pool lifetimes are invalidated by the existing forget hooks before reuse.
    for (const auto& entry : frame.pikmin) {
        const auto found = guest->pikmin.find(entry.first);
        if (found == guest->pikmin.end()) return false;
        const auto& binding = found->second; const auto& value = entry.second;
        if (binding.local->mColor != binding.color ||
            value.color != binding.color || value.color >= 3 || !net::validPikminState(value)) return false;
    }
    // Plain field assignments only from here: no spawning, killing, callbacks,
    // action changes, pathfinding or fallible allocations halfway through apply.
    for (const auto& entry : frame.pikmin) {
        auto& binding = guest->pikmin.find(entry.first)->second;
        Piki* p = binding.local; const auto& value = entry.second;
        p->mSRT.t.x = value.position.x; p->mSRT.t.y = value.position.y; p->mSRT.t.z = value.position.z;
        p->mLastPosition = p->mSRT.t;
        p->mVelocity.x = value.velocity.x; p->mVelocity.y = value.velocity.y; p->mVelocity.z = value.velocity.z;
        p->mFaceDirection = value.faceDirection; p->mSRT.r.y = value.faceDirection;
        p->mHealth = value.health; p->mHappa = value.maturity;
        p->mNavi = value.leader < 2 ? captains.local[value.leader] : nullptr;
        binding.applied = value; // owner/action remain metadata, not guest AI commands
    }
    commitCaptains(captains, frame);
    guest->havePikminFrame = true;
    return true;
}

bool pc_coop_world_prepare_guest_visuals(std::uint64_t sessionId, std::uint32_t epoch)
{
    if (!guest || guest->invalidated || guest->pikminBound || guest->visualManager
        || sessionId != guest->session || epoch != guest->epoch || !pikiMgr) return false;
    Navi* captains[2] = {};
    if (!findCaptains(captains) || captains[0] != guest->captains[0] || captains[1] != guest->captains[1]) return false;
    std::vector<ViewPiki*> slots;
    if (!pikiMgr->pcCoopVisualSlots(slots)) return false;
    guest->visualSlots.swap(slots);
    guest->visualManager = pikiMgr;
    return true;
}

bool pc_coop_world_apply_guest_visuals(std::uint64_t sessionId, std::uint32_t epoch, const net::ActorFrame& frame)
{
    CaptainApply captains;
    if (!guest || !guest->visualManager || guest->visualManager != pikiMgr
        || !prepareCaptains(sessionId, epoch, frame, captains)
        || frame.pikmin.size() > guest->visualSlots.size()
        || !pikiMgr->pcCoopVisualSlotsValid(guest->visualSlots)) return false;
    if(!validateEnemy(frame))return false;
    // Allocate and validate the ENTIRE replacement before touching any model.
    std::map<std::uint64_t, VisualPikmin> pending;
    std::vector<bool> used(guest->visualSlots.size(), false);
    for (const auto& entry : frame.pikmin) {
        net::NetEntityId id;
        if (!net::NetEntityId::unpack(entry.first, id) || id.sceneEpoch != epoch
            || id.kind != net::EntityKind::Pikmin || !net::validPikminState(entry.second) || entry.second.color >= 3) return false;
        const auto old = guest->visuals.find(entry.first);
        if (old != guest->visuals.end()) {
            if (old->second.slot >= used.size() || used[old->second.slot]) return false;
            used[old->second.slot] = true;
            pending.emplace(entry.first, VisualPikmin{old->second.slot, entry.second});
        }
    }
    std::size_t free = 0;
    for (const auto& entry : frame.pikmin) {
        if (pending.count(entry.first)) continue;
        while (free < used.size() && used[free]) ++free;
        if (free == used.size()) return false;
        used[free] = true;
        pending.emplace(entry.first, VisualPikmin{free, entry.second});
    }
    for (const auto& entry : pending)
        if (!guest->visualSlots[entry.second.slot]->pcCoopVisualValidate(entry.second.applied)) return false;
    for (const auto& entry : pending)
        guest->visualSlots[entry.second.slot]->pcCoopVisualApply(entry.second.applied);
    applyEnemy(frame);
    guest->visuals.swap(pending); // absent actors disappear without gameplay death
    commitCaptains(captains, frame);
    guest->havePikminFrame = true;
    return true;
}

bool pc_coop_world_present_guest(const net::ActorFrame& frame)
{
    if (!guest || guest->invalidated || !guest->visualManager || !guest->havePikminFrame
        || frame.frame!=guest->lastFrame || frame.tick!=guest->lastTick
        || frame.captains.size()!=2 || frame.pikmin.size()!=guest->visuals.size()
        || guest->visualManager!=pikiMgr || !pikiMgr->pcCoopVisualSlotsValid(guest->visualSlots)) return false;
    Navi* captains[2]={};
    if (!findCaptains(captains) || captains[0]!=guest->captains[0] || captains[1]!=guest->captains[1]) return false;
    for (int player=0;player<2;++player) {
        auto it=frame.captains.find(guest->ids[player]);
        if (it==frame.captains.end() || it->second.player!=player
            || it->second.upperAnimation!=guest->captainStates[player].upperAnimation
            || it->second.lowerAnimation!=guest->captainStates[player].lowerAnimation
            || !captains[player]->pcCoopVisualValidate(it->second)) return false;
    }
    for (const auto& entry:guest->visuals) {
        auto it=frame.pikmin.find(entry.first);
        if (it==frame.pikmin.end()
            || it->second.upperAnimation!=entry.second.applied.upperAnimation
            || it->second.lowerAnimation!=entry.second.applied.lowerAnimation
            || !guest->visualSlots[entry.second.slot]->pcCoopVisualValidate(it->second)) return false;
    }
    if(!validateEnemy(frame) || frame.enemies.size()!=((guest->enemyId && !guest->enemyRetired) ? 1u : 0u))return false;
    if(!frame.enemies.empty()) {
        const auto& e=frame.enemies.begin()->second;const auto& accepted=guest->enemyState;
        if(e.animation!=accepted.animation || e.health!=accepted.health || e.maxHealth!=accepted.maxHealth || e.visible!=accepted.visible)return false;
    }
    for (int player=0;player<2;++player) {
        auto* n=captains[player];auto value=guest->captainStates[player];
        const auto& pose=frame.captains.at(guest->ids[player]);
        value.position=pose.position;value.velocity=pose.velocity;value.faceDirection=pose.faceDirection;
        value.upperFrame=pose.upperFrame;value.lowerFrame=pose.lowerFrame;value.cursor=pose.cursor;value.whistleRadius=pose.whistleRadius;
        n->mSRT.t.x=value.position.x;n->mSRT.t.y=value.position.y;n->mSRT.t.z=value.position.z;
        n->mLastPosition=n->mSRT.t;
        n->mVelocity.x=value.velocity.x;n->mVelocity.y=value.velocity.y;n->mVelocity.z=value.velocity.z;
        n->mFaceDirection=value.faceDirection;n->mSRT.r.y=value.faceDirection;n->pcCoopVisualApply(value);
        n->mPcLockTarget=value.lockedEnemy ? guest->enemy : nullptr;
    }
    for (const auto& entry:guest->visuals) {
        auto value=entry.second.applied;
        const auto& pose=frame.pikmin.at(entry.first);
        value.position=pose.position;value.velocity=pose.velocity;value.faceDirection=pose.faceDirection;
        value.upperFrame=pose.upperFrame;value.lowerFrame=pose.lowerFrame;
        guest->visualSlots[entry.second.slot]->pcCoopVisualApply(value);
    }
    applyEnemy(frame,true);
    return true;
}

bool pc_coop_world_guest_idle_count(int& count) {
    if(!guest || guest->invalidated || !guest->havePikminFrame || !guest->visualManager)return false;
    int idle=0;for(const auto& entry:guest->visuals) {
        const auto& p=entry.second.applied;
        if(p.health>0 && p.action==PikiMode::FreeMode)++idle;
    }
    count=idle;return true;
}
void pc_coop_world_prepare_enemy_gauge(LifeGauge& gauge,float health,float maximum) {
    if(!state && !guest)return;
    if(!std::isfinite(health)||!std::isfinite(maximum)||maximum<=0)return;
    gauge.mDisplayState=LifeGauge::STATE_Display;gauge.mFadeTransitionValue=1;
    gauge.mCurrentDisplayHealthRatio=gauge.mTargetHealthRatio=std::clamp(health/maximum,0.0f,1.0f);
    gauge.mVisibleHoldTimer=5;gauge.mSnapToTargetHealth=true;
}
bool pc_coop_world_bind_guest_encounter(Teki* enemy) {
    if(!guest || guest->enemy || !enemy || enemy->mTekiType!=net::kPracticeEnemyType || !enemy->mTekiAnimator || !enemy->mTekiShape)return false;
    guest->enemy=enemy;return true;
}
bool pc_coop_world_draw_guest_enemies(Graphics& gfx) {
    if(!guest)return false;
    if(guest->invalidated || !guest->enemyVisible || !guest->enemy || !gfx.mCamera)return true;
    auto* e=guest->enemy;
    if(!gfx.mCamera->isPointVisible(e->mSRT.t,e->getBoundingSphereRadius()))return true;
    // The guest samples only host poses; no strategy draw, collision/platform,
    // AI, hit events, particle spawning, death jobs or animation callbacks.
    Matrix4f world,view;Quat rotation(0,0,0,1);
    rotation.rotate(Vector3f(0,1,0),e->mFaceDirection);
    NVector3f axis;rotation.genVectorZ(axis);rotation.rotate(axis,e->_3A4);
    world.makeVQS(e->mSRT.t,rotation,e->mSRT.s);gfx.mCamera->mLookAtMtx.multiplyTo(world,view);
    gfx.useMatrix(Matrix4f::ident,0);e->mTekiAnimator->updateContext();
    e->mTekiShape->mShape->updateAnim(gfx,view,nullptr,nullptr);
    e->mAnimatedMaterials.animate(nullptr);
    e->mTekiShape->mShape->drawshape(gfx,*gfx.mCamera,&e->mAnimatedMaterials);
    return true;
}
bool pc_coop_world_draw_guest_enemy_gauges(Graphics& gfx) {
    if(!guest)return false;
    if(guest->invalidated || !guest->enemyVisible || !guest->enemy || !gfx.mCamera)return true;
    auto* e=guest->enemy;
    if(!gfx.mCamera->isPointVisible(e->mSRT.t,e->getBoundingSphereRadius()))return true;
    // Collision centres are not advanced by the replica, so use the received
    // world position rather than the original spawn-time collision geometry.
    e->mLifeGauge.mPosition.input(e->mSRT.t);
    e->mLifeGauge.mOffset.y=e->getParameterF(TPF_LifeGaugeOffset);
    e->mLifeGauge.mScale=5000.0f/gfx.mCamera->mNear;
    e->mLifeGauge.refresh(gfx);return true;
}
bool pc_coop_world_draw_guest_pikmin(Graphics& gfx)
{
    if (!guest || !guest->visualManager) return false;
    if (guest->invalidated || guest->visualManager != pikiMgr
        || !pikiMgr->pcCoopVisualSlotsValid(guest->visualSlots)) return true;
    for (const auto& entry : guest->visuals)
        guest->visualSlots[entry.second.slot]->pcCoopVisualDraw(gfx);
    return true;
}

bool pc_coop_world_guest_pikmin_state(std::uint64_t id, net::PikminState& output)
{
    if (!guest || guest->invalidated || !guest->havePikminFrame) return false;
    if (guest->visualManager) {
        const auto visual = guest->visuals.find(id);
        if (visual == guest->visuals.end()) return false;
        output = visual->second.applied; return true;
    }
    const auto found = guest->pikmin.find(id);
    if (found == guest->pikmin.end()) return false;
    output = found->second.applied;
    return true;
}

bool pc_coop_world_begin_host(std::uint64_t sessionId, std::uint32_t epoch, bool practiceOwners)
{
    if (state || guest || sessionId == 0 || !naviMgr || !pikiMgr || (sessionId == lastSession && epoch <= lastEpoch)) return false;
    auto pending = std::make_unique<CaptureState>();
    if (!pending->registry.beginScene(epoch)) return false;
    pending->session=sessionId;pending->practiceOwners=practiceOwners;
    state = std::move(pending); lastSession = sessionId; lastEpoch = epoch;
    return true;
}
void pc_coop_world_end_scene() { clearGuestEnemyTargets();emergencyHold=false;state.reset(); guest.reset(); }
void pc_coop_world_forget(const void* actor)
{
    if (state && actor) state->registry.retireLocal(key(actor));
    if (guest && actor && (actor == guest->captains[0] || actor == guest->captains[1]))
        guest->invalidated = true; // same address after pool reuse is NOT same lifetime
    if (guest && actor && actor==guest->enemy) { clearGuestEnemyTargets();guest->invalidated=true; }
    if (guest && actor) for (const auto* slot : guest->visualSlots)
        if (slot == actor) { guest->invalidated = true; break; }
    if (guest && actor) for (const auto& binding : guest->pikmin) {
        if (binding.second.local == actor) { guest->invalidated = true; break; }
    }
}
std::uint64_t pc_coop_world_actor_id(const void* actor, net::EntityKind kind)
{
    return state ? state->registry.idForLocal(key(actor), kind) : 0;
}
bool pc_coop_world_set_owner(std::uint64_t id, std::uint8_t owner)
{
    return state && state->registry.localForId(id, net::EntityKind::Pikmin) && state->registry.setOwner(id, owner);
}

bool pc_coop_world_capture(std::vector<net::EntityRecord>& output)
{
    if (!state || !naviMgr || !pikiMgr) return false;
    std::vector<net::EntityRecord> records;
    Navi* captains[2] = {nullptr, nullptr};
    Iterator navis(naviMgr);
    CI_LOOP(navis) {
        Navi* n = static_cast<Navi*>(*navis);
        if (!n || n->mNaviID < 0 || n->mNaviID > 1 || captains[n->mNaviID]) return false;
        const auto player = static_cast<std::uint8_t>(n->mNaviID);
        captains[player] = n;
        net::CaptainState s;
        s.position = {n->mSRT.t.x, n->mSRT.t.y, n->mSRT.t.z};
        s.velocity = {n->mVelocity.x, n->mVelocity.y, n->mVelocity.z};
        s.faceDirection = n->mFaceDirection; s.player = player;
        s.cursor = {n->mCursorWorldPos.x,n->mCursorWorldPos.y,n->mCursorWorldPos.z};
        s.health=n->mHealth;s.cursorVisible=n->mIsCursorVisible ? 1 : 0;
        n->pcCoopWhistleCapture(s);
        s.lockedEnemy=state->registry.idForLocal(key(n->mPcLockTarget),net::EntityKind::Enemy)!=0;
        const auto& upper=n->mNaviAnimMgr.getUpperAnimator();
        const auto& lower=n->mNaviAnimMgr.getLowerAnimator();
        if (upper.mCurrentAnimID<0 || upper.mCurrentAnimID>=1024 || lower.mCurrentAnimID<0 || lower.mCurrentAnimID>=1024) return false;
        s.upperAnimation=static_cast<std::uint16_t>(upper.mCurrentAnimID);
        s.lowerAnimation=static_cast<std::uint16_t>(lower.mCurrentAnimID);
        s.upperFrame=upper.mAnimationCounter;s.lowerFrame=lower.mAnimationCounter;
        auto record = net::captainRecord(state->registry.epoch(), s);
        net::CaptainState validated;
        if (!net::decodeCaptainState(record.data.data(), record.data.size(), validated)) return false;
        record.id = state->registry.observe(net::EntityKind::Captain, key(n), player);
        if (!record.id) return false;
        records.push_back(std::move(record));
    }
    if (!captains[0]) return false;
    Iterator pikis(pikiMgr);
    CI_LOOP(pikis) {
        Piki* p = static_cast<Piki*>(*pikis);
        if (!p) return false;
        if (!p->isAlive()) { pc_coop_world_forget(p); continue; }
        if (p->mColor >= 3 || p->mHappa < 0 || p->mHappa > 2) return false;
        net::PikminState s;
        s.position = {p->mSRT.t.x, p->mSRT.t.y, p->mSRT.t.z};
        s.velocity = {p->mVelocity.x, p->mVelocity.y, p->mVelocity.z};
        s.faceDirection = p->mFaceDirection; s.health = p->mHealth;
        s.leader = leader(p->mNavi, captains);
        s.color = static_cast<std::uint8_t>(p->mColor);
        s.maturity = static_cast<std::uint8_t>(p->mHappa); s.action = p->mMode;
        const auto& upper = p->mPikiAnimMgr.getUpperAnimator();
        const auto& lower = p->mPikiAnimMgr.getLowerAnimator();
        if (upper.mCurrentAnimID < 0 || upper.mCurrentAnimID >= 1024 || lower.mCurrentAnimID < 0 || lower.mCurrentAnimID >= 1024) return false;
        s.upperAnimation = static_cast<std::uint16_t>(upper.mCurrentAnimID);
        s.lowerAnimation = static_cast<std::uint16_t>(lower.mCurrentAnimID);
        s.upperFrame = upper.mAnimationCounter; s.lowerFrame = lower.mAnimationCounter;
        if (state->practiceOwners && (p->mPlayerId < 0 || p->mPlayerId > 1)) return false;
        const auto initialOwner=state->practiceOwners ? static_cast<std::uint8_t>(p->mPlayerId) : s.leader;
        const auto id = state->registry.observe(net::EntityKind::Pikmin, key(p), initialOwner);
        if (!id) return false;
        s.owner = state->registry.owner(id);
        if (state->practiceOwners && s.owner != initialOwner) return false; // workers/idle keep allowance ownership
        auto record = net::pikminRecord(id, s);
        if (!record.id) return false;
        records.push_back(std::move(record));
    }
    if(tekiMgr) {
        Iterator enemies(tekiMgr);CI_LOOP(enemies) {
            auto* e=static_cast<Teki*>(*enemies);
            if(!e || e->mTekiType!=net::kPracticeEnemyType || !e->mTekiAnimator)return false;
            auto* a=e->mTekiAnimator;
            net::EnemyState s;s.position={e->mSRT.t.x,e->mSRT.t.y,e->mSRT.t.z};
            s.velocity={e->mVelocity.x,e->mVelocity.y,e->mVelocity.z};s.scale={e->mSRT.s.x,e->mSRT.s.y,e->mSRT.s.z};
            s.faceDirection=e->mFaceDirection;s.health=std::max(0.0f,e->mHealth);s.maxHealth=e->getMaxLife();s.tilt=e->_3A4;
            if(a->mCurrentAnimID<0 || a->mCurrentAnimID>=1024)return false;
            s.animation=static_cast<std::uint16_t>(a->mCurrentAnimID);s.animationFrame=a->mAnimationCounter;
            s.visible=e->mDeadState==0 && e->getTekiOption(TEKIOPT_ShapeVisible);
            const auto id=state->registry.observe(net::EntityKind::Enemy,key(e));
            auto record=net::enemyRecord(id,s);if(!record.id)return false;
            records.push_back(std::move(record));
        }
    }
    output.swap(records);
    return true;
}

bool pc_coop_world_capture_packets(std::uint64_t frame, std::uint64_t tick,
    std::size_t budget, std::vector<std::vector<std::uint8_t>>& packets)
{
    if (!state || frame <= state->lastFrame || tick < state->lastTick) return false;
    std::vector<net::EntityRecord> records;
    if (!pc_coop_world_capture(records) || !net::packActorFrame(state->session, state->registry.epoch(),
            frame, tick, records, budget, {}, packets)) return false;
    state->lastFrame=frame;state->lastTick=tick;
    return true;
}
