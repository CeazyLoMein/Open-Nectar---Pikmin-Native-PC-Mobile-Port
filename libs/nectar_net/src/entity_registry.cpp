#include "nectar_net/entity_registry.h"

namespace nectar::net {
bool HostEntityRegistry::beginScene(std::uint32_t epoch)
{
    if (epoch == 0 || epoch > 65535 || epoch <= mEpoch || mLimits.live == 0 || mLimits.live > 4096
        || mLimits.issuedPerScene == 0 || mLimits.issuedPerScene > 1000000) return false;
    mLocal.clear(); mIds.clear(); mIssued = 0; mEpoch = epoch; mActive = true;
    return true;
}
void HostEntityRegistry::endScene() { mActive = false; mLocal.clear(); mIds.clear(); }

std::uint64_t HostEntityRegistry::observe(EntityKind kind, std::uintptr_t key, std::uint8_t initialOwner)
{
    if (!mActive || key == 0 || !isKnownEntityKind(static_cast<std::uint8_t>(kind))
        || (initialOwner > 1 && initialOwner != kUnowned)) return 0;
    const auto found = mLocal.find(key);
    if (found != mLocal.end()) return idForLocal(key, kind); // ownership is not inferred anew each tick
    if (mLocal.size() >= mLimits.live || mIssued >= mLimits.issuedPerScene) return 0;
    const auto id = NetEntityId{epoch(), kind, 0, mIssued + 1}.pack();
    // Allocate the reverse entry first and roll it back on allocation failure.
    const auto reverse = mIds.emplace(id, key);
    try { mLocal.emplace(key, Entry{id, initialOwner}); }
    catch (...) { mIds.erase(reverse.first); throw; }
    ++mIssued;
    return id;
}
std::uint64_t HostEntityRegistry::retireLocal(std::uintptr_t key)
{
    const auto it = mLocal.find(key);
    if (it == mLocal.end()) return 0;
    const auto id = it->second.id;
    mIds.erase(id); mLocal.erase(it);
    return id;
}
std::uint64_t HostEntityRegistry::idForLocal(std::uintptr_t key, EntityKind kind) const
{
    const auto it = mLocal.find(key);
    if (it == mLocal.end()) return 0;
    NetEntityId id;
    return NetEntityId::unpack(it->second.id, id) && id.kind == kind ? it->second.id : 0;
}
std::uintptr_t HostEntityRegistry::localForId(std::uint64_t value, EntityKind kind) const
{
    NetEntityId id;
    if (!mActive || !NetEntityId::unpack(value, id) || id.sceneEpoch != epoch() || id.kind != kind) return 0;
    const auto it = mIds.find(value);
    return it == mIds.end() ? 0 : it->second;
}
bool HostEntityRegistry::setOwner(std::uint64_t value, std::uint8_t player)
{
    if (player > 1 && player != kUnowned) return false;
    const auto it = mIds.find(value);
    if (it == mIds.end()) return false;
    mLocal.at(it->second).owner = player;
    return true;
}
std::uint8_t HostEntityRegistry::owner(std::uint64_t value) const
{
    const auto it = mIds.find(value);
    return it == mIds.end() ? kUnowned : mLocal.at(it->second).owner;
}
} // namespace nectar::net
