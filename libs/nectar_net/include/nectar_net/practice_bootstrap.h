#pragma once
#include "nectar_net/coop_connection.h"
#include "nectar_net/scene.h"

namespace nectar::net {
enum class PracticeLoadPhase { Closed, WaitingForHost, Loading, SessionLoading, Failed };
// Single-use, explicit practice-area agreement on an authenticated retained room.
// It does NOT load the engine or save a campaign. Accepted scene ID comes from
// local build policy, not network filenames. Main owning thread; caller MUST
// keep pumping through loading. No timeout fallback to playing alone.
class PracticeBootstrap {
  public:
    explicit PracticeBootstrap(CoopConnection& owner, std::uint32_t allowedScene = 0)
        : mOwner(owner), mAllowedScene(allowedScene) {}
    bool beginHost(std::uint64_t uniqueSessionId, std::uint64_t seed, std::uint64_t nowMs);
    bool beginGuest(std::uint64_t nowMs);
    void pump(std::uint64_t nowMs);
    // Engine attestation of its actual completed area load; never call this on
    // a UI button alone. Both captains/presentation level must already exist.
    bool worldLoaded(std::uint32_t actualSceneId, std::uint64_t nowMs);
    PracticeLoadPhase phase() const { return mPhase; }
    std::uint64_t sessionId() const { return mId; }
    const ScenePrepare& scene() const { return mScene; }
  private:
    bool begin(CoopRole expected, std::uint64_t nowMs);
    bool send(MessageType type, const std::vector<std::uint8_t>& payload);
    bool startHostSession();
    void receive(const TransportEvent& event, std::uint64_t nowMs);
    CoopConnection& mOwner;
    const std::uint32_t mAllowedScene;
    PracticeLoadPhase mPhase = PracticeLoadPhase::Closed;
    CoopRole mRole = CoopRole::Guest;
    HostSceneBarrier mHost;
    GuestSceneBarrier mGuest;
    ScenePrepare mScene;
    std::uint64_t mId = 0, mStarted = 0, mNow = 0;
    std::uint32_t mSent = 0, mReceived = 0;
    bool mLocalLoaded = false;
};
} // namespace nectar::net
