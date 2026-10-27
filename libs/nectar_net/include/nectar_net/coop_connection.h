#pragma once
#include "nectar_net/coop_session.h"
#include "nectar_net/room.h"
#include <memory>

namespace nectar::net {
// Exclusive room/link ownership after UI -> game handoff. All methods on ONE
// owning thread; transfer at a safe boundary with old polling stopped. Neither
// adoption nor session startup loads a level, creates actors or writes a save.
// Failed adoption leaves BOTH caller's room and this connection unchanged.
class CoopConnection {
  public:
    CoopConnection() = default;
    ~CoopConnection();
    CoopConnection(const CoopConnection&) = delete;
    CoopConnection& operator=(const CoopConnection&) = delete;
    // UI may already have received authenticated application bytes while the
    // other phone left its screen first. Preserve them IN MEMORY, max64/64KiB.
    // Only before adoption; invalid/full queues leave the input event intact.
    bool bufferBeforeHandoff(TransportEvent&& event);
    bool adoptHost(std::unique_ptr<HostRoom>& room);
    bool adoptGuest(std::unique_ptr<GuestJoin>& join);
    bool connected() const;
    bool role(CoopRole& output) const;
    bool stats(TransportStats& output) const;
    // Explicit scene/bootstrap negotiator is the sole event consumer before
    // beginSession. These refuse access once CoopSession owns event dispatch.
    bool pollBeforeSession(TransportEvent& event);
    bool sendBeforeSession(const std::vector<std::uint8_t>& payload);
    bool beginSession(std::uint64_t sessionId, std::uint16_t epoch,
                      std::uint64_t baselineFrame, std::uint64_t nowMs);
    // Borrowed until endSession/close/destruction. Caller pumps it while
    // loading/paused as well as running; do not poll HostRoom/GuestJoin too.
    CoopSession* session() { return mSession.get(); }
    void endSession();
    // Trusted host driver only, after its actual world has already been held.
    // Retires the lost session and keeps the room listener/code. A fresh peer
    // must authenticate and load a new baseline; never resumes gameplay alone.
    bool prepareHostRejoin(bool worldHeld);
    // Pump only while waiting; stops immediately on authentication to avoid
    // consuming messages belonging to the next bootstrap.
    bool pollHostRejoin();
    // Keep host's mapping lease alive without polling/consuming session events.
    bool maintain(std::uint64_t nowMs, std::uint64_t nowUnixSeconds, RoomStatus& updated);
    // End borrowed session FIRST, then close/wipe its owning room/link.
    void close();
  private:
    GatedTransport* link() const;
    static bool accepted(GatedTransport* link, GatedTransport::Role role);
    std::unique_ptr<HostRoom> mHost;
    std::unique_ptr<GuestJoin> mGuest;
    std::unique_ptr<CoopSession> mSession;
    std::deque<TransportEvent> mPending;
    std::size_t mPendingBytes = 0;
    bool mWaitingForRejoin = false;
    std::uint64_t mLastSession = 0;
    std::uint16_t mLastEpoch = 0;
};
} // namespace nectar::net
