#pragma once
#include "nectar_net/actor_frame.h"
#include "nectar_net/coop_audio.h"
#include "nectar_net/gated_transport.h"
#include "nectar_net/protocol.h"
#include "nectar_net/input.h"
#include <array>
#include <deque>

namespace nectar::net {
constexpr std::uint32_t kCoopSessionCapability = 0x00010000;
// Add to actual source/content identity BEFORE the room compatibility handshake.
void requireCoopSessionCapability(CompatibilityInfo &info);
enum class CoopRole { Host, Guest };
enum class CoopPhase { Closed, Loading, WaitingForReady, Running, Paused, WaitingForPartner };
enum class CoopBlock : std::uint8_t { Manual = 1, Settings = 2, Background = 4 };
enum class MarkerKind : std::uint8_t { Here = 0, Danger = 1, Help = 2, Carry = 3 };
struct CoopMarker {
    Vec3 position;
    MarkerKind kind = MarkerKind::Here;
    std::uint64_t expiresAtMs = 0;
    bool visible = false;
};
struct CoopView {
    std::uint64_t revision = 0;
    std::array<bool, 2> loaded{}, ready{};
    std::array<std::uint8_t, 2> blockers{};
};
// Two-player session over an ALREADY authenticated + build/content-compatible
// GatedTransport. No socket creation, game actor mutation, disk saves or UI.
// The link must outlive this object: end before Room::close/GuestJoin::cancel.
// One owning thread. Adapter must call pump while paused as well as running.
// Integrate with actual engine readiness/pause/input/camera only in prototype.
class CoopSession {
  public:
    static constexpr std::uint64_t kHeartbeatMs = 500, kPeerTimeoutMs = 3000, kMarkerMs = 8000,
                                   kMarkerCooldownMs = 1000, kActorPeriodMs = 50;
    static constexpr std::int32_t kReliableBacklogLimit = 64 * 1024;
    CoopSession(GatedTransport &link, CoopRole role) : mLink(link), mRole(role) {}
    // Context accepted by scene barrier; never read it from incoming packets.
    // Rejoining requires new authenticated link + higher epoch + new full load
    // and both ready checks. No automatic continuation or world reconstruction.
    bool begin(std::uint64_t session, std::uint16_t epoch, std::uint64_t requiredActorFrame,
               std::uint64_t nowMs);
    void end();                     // clears protocol state, never closes the owning room or saves
    void pump(std::uint64_t nowMs); // bounded64 events; no unbounded catch-up
    // At most20 complete visual updates/second; defer whole updates when queued.
    bool publishActors(const std::vector<std::vector<std::uint8_t>> &packets, std::uint64_t nowMs);
    // Engine callback must attest ALL required world state is loaded, not just
    // these actor positions. Guest also requires an assembled baseline frame.
    bool confirmWorldLoaded();
    // Trusted game policy, before loading is confirmed. Retained across pause resets.
    bool configureInputContinuousMask(std::uint8_t mask);
    // Guest submits host-tick-addressed inputs only while both are ready.
    // Each bundle is tied to the exact host readiness/pause revision. Frames
    // queued before any pause cannot move a captain after it resumes.
    // The engine adapter supplies target HOST ticks, never render/phone ticks.
    bool publishInput(const std::vector<NetInputFrame>& newestFirst, std::uint64_t nowMs);
    // Host simulation thread, once per increasing host tick. On gaps briefly
    // hold continuous movement; then neutralize. Never repeats one-shot edges.
    // Not a position-write API: guest never selects its captain/player slot.
    bool consumeGuestInput(std::uint64_t hostTick, NetInputFrame& input, InputHealth& health,
                           std::uint64_t nowMs = 0);
    std::uint32_t inputHoldTicks() const { return mGuestInput.policy().holdTicks; }
    // Host-only, bounded, authenticated presentation events. No guest simulation.
    bool publishAudio(const std::vector<AudioCue>& cues, std::uint64_t nowMs);
    std::vector<AudioCue> takeAudio(std::uint64_t nowMs);
    bool setReady(bool ready);
    bool setBlocked(CoopBlock reason, bool blocked);
    bool placeMarker(MarkerKind kind, const Vec3 &point, std::uint64_t nowMs);
    CoopPhase phase() const;
    bool hostShouldAdvanceWorld() const;
    bool canIssueCommands() const;
    // Diagnostic acknowledgement of buffered input, NOT a simulation clock or
    // proof it was applied. Clears at every pause/readiness revision.
    std::uint64_t receivedGuestInputTick() const { return mReceivedInputTick; }
    const CoopView &view() const { return mView; }
    const ActorFrame &actors() const { return mActors.current(); }
    CoopMarker marker(std::uint8_t player, std::uint64_t nowMs) const;

  private:
    friend class CoopConnection; // exclusive already-authenticated handoff queue
    std::deque<TransportEvent> mBuffered;
    bool linked() const;
    bool send(MessageType type, const std::vector<std::uint8_t> &payload);
    bool control(std::uint8_t op, std::uint8_t value = 0, std::uint64_t frame = 0);
    bool publishView();
    void receive(const TransportEvent &event, std::uint64_t nowMs);
    void lost();
    std::uint8_t localPlayer() const { return mRole == CoopRole::Host ? 0 : 1; }
    GatedTransport &mLink;
    CoopRole mRole;
    std::uint64_t mSession = 0, mLastSession = 0, mRequiredFrame = 0, mLastPublished = 0, mLastHeard = 0,
                  mLastHeartbeat = 0, mLastActorAt = 0, mLastPublishedTick = 0;
    std::uint16_t mEpoch = 0, mLastEpoch = 0;
    std::uint32_t mSent = 0, mReceived = 0;
    bool mActive = false, mLost = false, mLocalLoaded = false, mLocalReady = false, mHaveView = false;
    std::uint8_t mLocalBlocks = 0;
    InputPolicy mInputPolicy;
    InputReceiver mGuestInput;
    std::uint64_t mInputRevision = 0, mLastInputAt = 0, mLastInputTarget = 0, mLastInputTick = 0;
    std::uint64_t mReceivedInputTick = 0;
    bool mInputSent = false, mInputConsumed = false;
    std::uint64_t mHoldClockTick=0,mHoldClockAt=0;
    bool mHaveHoldClock=false;
    void resetInput();
    struct PendingAudio { AudioCue cue; std::uint64_t at=0, frame=0; };
    std::deque<PendingAudio> mAudio;
    std::uint64_t mLastAudioAt=0;
    bool mAudioSent=false;
    CoopView mView;
    ActorFrameReceiver mActors;
    std::array<CoopMarker, 2> mMarkers{};
    std::array<std::uint64_t, 2> mLastMarker{};
    std::array<bool, 2> mMarked{};
};
} // namespace nectar::net
