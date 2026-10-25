#pragma once
#include "nectar_net/world.h"
#include <cstdint>
#include <map>

namespace nectar::net {

// Host simulation-thread registry. Object keys are LOCAL addresses/tokens only:
// never serialize them. Call retireLocal before pool reuse/heap reset. A fresh
// counter is assigned even when the next lifetime has the exact same address.
class HostEntityRegistry {
public:
    static constexpr std::uint8_t kUnowned = 255;
    struct Limits { std::size_t live = 512; std::uint32_t issuedPerScene = 65536; };
    struct Entry { std::uint64_t id = 0; std::uint8_t owner = kUnowned; };
    HostEntityRegistry() : HostEntityRegistry(Limits{}) {}
    explicit HostEntityRegistry(Limits limits) : mLimits(limits) {}
    // Epochs cannot repeat or wrap within this registry/session. Invalid calls
    // leave current bindings intact. A new session needs a fresh transport ID.
    bool beginScene(std::uint32_t epoch);
    void endScene();
    std::uint64_t observe(EntityKind kind, std::uintptr_t localKey, std::uint8_t initialOwner = kUnowned);
    std::uint64_t retireLocal(std::uintptr_t localKey);
    std::uint64_t idForLocal(std::uintptr_t localKey, EntityKind expectedKind) const;
    std::uintptr_t localForId(std::uint64_t id, EntityKind expectedKind) const;
    bool setOwner(std::uint64_t id, std::uint8_t owner);
    std::uint8_t owner(std::uint64_t id) const;
    bool active() const { return mActive; }
    std::uint16_t epoch() const { return static_cast<std::uint16_t>(mEpoch); }
    std::size_t size() const { return mLocal.size(); }
private:
    Limits mLimits;
    bool mActive = false;
    std::uint32_t mEpoch = 0, mIssued = 0;
    std::map<std::uintptr_t, Entry> mLocal;
    std::map<std::uint64_t, std::uintptr_t> mIds;
};
} // namespace nectar::net
