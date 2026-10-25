#include "netplay/pc_coop_world.h"
#include "nectar_net/entity_registry.h"
#include "nectar_net/pikmin_replication.h"
#include "Navi.h"
#include "NaviMgr.h"
#include "Piki.h"
#include "PikiMgr.h"
#include <memory>

namespace {
namespace net = nectar::net;
struct CaptureState { net::HostEntityRegistry registry; std::uint64_t session=0, lastFrame=0, lastTick=0; };
// No allocation or manager traversal until explicitly begun by a future session.
std::unique_ptr<CaptureState> state;
struct GuestState {
    std::uint64_t session = 0, lastFrame = 0, lastTick = 0, ids[2] = {};
    std::uint16_t epoch = 0;
    Navi* captains[2] = {};
    bool invalidated = false;
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
bool pc_coop_world_apply_guest_captains(std::uint64_t sessionId, std::uint32_t epoch,
                                       const net::ActorFrame& frame)
{
    if (!guest || guest->invalidated || sessionId != guest->session || epoch != guest->epoch ||
        !frame.frame || frame.frame <= guest->lastFrame || frame.tick < guest->lastTick ||
        frame.captains.size() != 2) return false;
    Navi* local[2] = {};
    if (!findCaptains(local) || local[0] != guest->captains[0] || local[1] != guest->captains[1]) return false;
    const net::CaptainState* incoming[2] = {};
    std::uint64_t ids[2] = {};
    for (const auto& entry : frame.captains) {
        net::NetEntityId id;
        const auto& value = entry.second;
        if (!net::NetEntityId::unpack(entry.first, id) || id.sceneEpoch != guest->epoch ||
            id.kind != net::EntityKind::Captain || value.player > 1 || incoming[value.player]) return false;
        // Validate even if a caller bypassed ActorFrameReceiver. Round-trip the
        // actual bounded captain schema; no untrusted NaN enters camera maths.
        auto bytes = net::encodeCaptainState(value);
        net::CaptainState checked;
        if (!net::decodeCaptainState(bytes.data(), bytes.size(), checked) ||
            (guest->ids[value.player] && guest->ids[value.player] != entry.first)) return false;
        incoming[value.player] = &value;
        ids[value.player] = entry.first;
    }
    if (!incoming[0] || !incoming[1]) return false;
    // No engine writes until every actor/identity/value above is validated.
    for (int player = 0; player < 2; ++player) {
        Navi* n = local[player]; const auto& value = *incoming[player];
        n->mSRT.t.x = value.position.x; n->mSRT.t.y = value.position.y; n->mSRT.t.z = value.position.z;
        n->mLastPosition = n->mSRT.t;
        n->mVelocity.x = value.velocity.x; n->mVelocity.y = value.velocity.y; n->mVelocity.z = value.velocity.z;
        n->mFaceDirection = value.faceDirection;
        n->mSRT.r.y = value.faceDirection;
        guest->ids[player] = ids[player];
    }
    guest->lastFrame = frame.frame; guest->lastTick = frame.tick;
    return true;
}
bool pc_coop_world_begin_host(std::uint64_t sessionId, std::uint32_t epoch)
{
    if (state || guest || sessionId == 0 || !naviMgr || !pikiMgr || (sessionId == lastSession && epoch <= lastEpoch)) return false;
    auto pending = std::make_unique<CaptureState>();
    if (!pending->registry.beginScene(epoch)) return false;
    pending->session=sessionId;
    state = std::move(pending); lastSession = sessionId; lastEpoch = epoch;
    return true;
}
void pc_coop_world_end_scene() { state.reset(); guest.reset(); }
void pc_coop_world_forget(const void* actor)
{
    if (state && actor) state->registry.retireLocal(key(actor));
    if (guest && actor && (actor == guest->captains[0] || actor == guest->captains[1]))
        guest->invalidated = true; // same address after pool reuse is NOT same lifetime
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
        const auto id = state->registry.observe(net::EntityKind::Pikmin, key(p), s.leader);
        if (!id) return false;
        s.owner = state->registry.owner(id); // workers/idle keep allowance ownership
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
