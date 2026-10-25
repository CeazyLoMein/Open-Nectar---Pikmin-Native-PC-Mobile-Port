#pragma once
#include "nectar_net/pikmin_replication.h"
#include <map>

namespace nectar::net {
// Prototype captain/Pikmin visual state ONLY: not AI, a campaign save or a
// complete world snapshot. Transport must authenticate the host before receive.
// Sessions/epochs come from that session's accepted scene barrier, never a packet.
struct ActorFrameLimits {
    std::size_t maxFrameBytes = 128 * 1024;
    std::size_t maxRecords = 512;
    std::size_t maxFragments = 512;
    std::uint64_t timeoutMs = 2000;
};
constexpr std::size_t kActorFragmentHeaderBytes = 48;
constexpr std::size_t kActorMaxPacketBytes = 1200; // payload; outer transport needs its own budget
struct ActorFrame {
    std::uint64_t frame = 0, tick = 0;
    std::map<std::uint64_t, CaptainState> captains;
    std::map<std::uint64_t, PikminState> pikmin;
};
// All-or-nothing: rejects oversized/invalid captures; never drops actors to fit.
// Returned vectors own their bytes (no borrowed actor/record buffers).
bool packActorFrame(std::uint64_t session, std::uint16_t epoch, std::uint64_t frame,
                    std::uint64_t tick, const std::vector<EntityRecord>& records,
                    std::size_t maxPacketBytes, const ActorFrameLimits& limits,
                    std::vector<std::vector<std::uint8_t>>& packets);

class ActorFrameReceiver {
public:
    enum class Result { Ignored, Buffered, Committed, Rejected };
    explicit ActorFrameReceiver(ActorFrameLimits limits = {}) : mLimits(limits) {}
    // New authenticated session/accepted scene: atomically discard old context.
    // Session IDs must not be reused. Caller enforces increasing scene epochs.
    bool begin(std::uint64_t session, std::uint16_t epoch);
    void end();
    Result receive(const std::uint8_t* data, std::size_t size, std::uint64_t nowMs);
    void expire(std::uint64_t nowMs); // deadline doesn't slide on retries
    const ActorFrame& current() const { return mCurrent; }
    bool hasFrame() const { return mCurrent.frame != 0; }
    bool assembling() const { return mPending.frame != 0; }
private:
    struct Pending {
        std::uint64_t frame=0, tick=0, checksum=0, started=0;
        std::uint32_t bytes=0;
        std::uint16_t parts=0;
        std::size_t received=0;
        std::vector<std::uint8_t> body, seen;
    };
    ActorFrameLimits mLimits;
    std::uint64_t mSession=0, mSeenFrame=0;
    std::uint16_t mEpoch=0;
    ActorFrame mCurrent;
    Pending mPending;
};
} // namespace nectar::net
