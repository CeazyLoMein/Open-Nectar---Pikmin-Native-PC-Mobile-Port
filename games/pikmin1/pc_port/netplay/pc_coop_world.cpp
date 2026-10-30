#include "netplay/pc_coop_world.h"
#include "nectar_net/entity_registry.h"
#include "nectar_net/pikmin_replication.h"
#include "Navi.h"
#include "NaviMgr.h"
#include "Piki.h"
#include "PikiMgr.h"
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
    std::vector<Piki*> orderedPikmin, liveScratch;
    PikiMgr* visualManager = nullptr;
    std::vector<ViewPiki*> visualSlots;
    std::map<std::uint64_t, VisualPikmin> visuals;
};
std::unique_ptr<GuestState> guest;
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
    if ((guest && (guest->pikminBound || guest->visualManager)) || !prepareCaptains(sessionId, epoch, frame, pending)) return false;
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
    if (!guest || !guest->pikminBound || frame.pikmin.size() != guest->pikmin.size() ||
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
    for (int player=0;player<2;++player) {
        auto* n=captains[player];auto value=guest->captainStates[player];
        const auto& pose=frame.captains.at(guest->ids[player]);
        value.position=pose.position;value.velocity=pose.velocity;value.faceDirection=pose.faceDirection;
        value.upperFrame=pose.upperFrame;value.lowerFrame=pose.lowerFrame;value.cursor=pose.cursor;value.whistleRadius=pose.whistleRadius;
        n->mSRT.t.x=value.position.x;n->mSRT.t.y=value.position.y;n->mSRT.t.z=value.position.z;
        n->mLastPosition=n->mSRT.t;
        n->mVelocity.x=value.velocity.x;n->mVelocity.y=value.velocity.y;n->mVelocity.z=value.velocity.z;
        n->mFaceDirection=value.faceDirection;n->mSRT.r.y=value.faceDirection;n->pcCoopVisualApply(value);
    }
    for (const auto& entry:guest->visuals) {
        auto value=entry.second.applied;
        const auto& pose=frame.pikmin.at(entry.first);
        value.position=pose.position;value.velocity=pose.velocity;value.faceDirection=pose.faceDirection;
        value.upperFrame=pose.upperFrame;value.lowerFrame=pose.lowerFrame;
        guest->visualSlots[entry.second.slot]->pcCoopVisualApply(value);
    }
    return true;
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
void pc_coop_world_end_scene() { emergencyHold=false;state.reset(); guest.reset(); }
void pc_coop_world_forget(const void* actor)
{
    if (state && actor) state->registry.retireLocal(key(actor));
    if (guest && actor && (actor == guest->captains[0] || actor == guest->captains[1]))
        guest->invalidated = true; // same address after pool reuse is NOT same lifetime
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
