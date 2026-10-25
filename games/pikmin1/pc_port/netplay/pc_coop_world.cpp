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
std::uint64_t lastSession = 0;
std::uint32_t lastEpoch = 0;
std::uintptr_t key(const void* actor) { return reinterpret_cast<std::uintptr_t>(actor); }
std::uint8_t leader(Navi* associated, Navi* const (&captains)[2])
{
    for (std::uint8_t p = 0; p < 2; ++p) if (associated && associated == captains[p]) return p;
    return net::HostEntityRegistry::kUnowned;
}
}

bool pc_coop_world_active() { return state != nullptr; }
bool pc_coop_world_begin_host(std::uint64_t sessionId, std::uint32_t epoch)
{
    if (state || sessionId == 0 || !naviMgr || !pikiMgr || (sessionId == lastSession && epoch <= lastEpoch)) return false;
    auto pending = std::make_unique<CaptureState>();
    if (!pending->registry.beginScene(epoch)) return false;
    pending->session=sessionId;
    state = std::move(pending); lastSession = sessionId; lastEpoch = epoch;
    return true;
}
void pc_coop_world_end_scene() { state.reset(); }
void pc_coop_world_forget(const void* actor)
{
    if (state && actor) state->registry.retireLocal(key(actor));
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
