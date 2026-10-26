#include "nectar_net/coop_connection.h"

namespace nectar::net {
CoopConnection::~CoopConnection() { close(); }
bool CoopConnection::accepted(GatedTransport* link, GatedTransport::Role role) {
    if (!link || link->role() != role || link->state() != TransportState::Connected ||
        link->joinState() != JoinState::Authenticated) return false;
    const auto* identity = link->compatibility();
    if (!identity || identity->state() != CompatibilityState::Compatible ||
        !(identity->peer().capabilities & kCoopSessionCapability)) return false;
    bool build = false, content = false;
    for (auto b : identity->peer().build) build |= b != 0;
    for (auto b : identity->peer().content) content |= b != 0;
    return build && content;
}
GatedTransport* CoopConnection::link() const {
    return mHost ? mHost->transport() : mGuest ? mGuest->transport() : nullptr;
}
bool CoopConnection::bufferBeforeHandoff(TransportEvent&& event) {
    if (mHost || mGuest || mSession || event.type != TransportEventType::Message ||
        event.delivery != Delivery::ReliableOrdered || mPending.size() >= 64 ||
        event.payload.size() > 64*1024 - mPendingBytes) return false;
    Message checked;
    if (decodeMessage(event.payload.data(),event.payload.size(),checked,kActorMaxPacketBytes)!=DecodeError::None)
        return false;
    mPendingBytes += event.payload.size();
    event.peerAddress.clear();event.detail.clear();
    mPending.push_back(std::move(event));
    return true;
}
bool CoopConnection::adoptHost(std::unique_ptr<HostRoom>& room) {
    if (mHost || mGuest || mSession || !room || !accepted(room->transport(), GatedTransport::Role::Host))
        return false;
    mHost = std::move(room);
    return true;
}
bool CoopConnection::adoptGuest(std::unique_ptr<GuestJoin>& join) {
    if (mHost || mGuest || mSession || !join || !accepted(join->transport(), GatedTransport::Role::Guest))
        return false;
    mGuest = std::move(join);
    return true;
}
bool CoopConnection::connected() const {
    return accepted(link(), mHost ? GatedTransport::Role::Host : GatedTransport::Role::Guest);
}
bool CoopConnection::role(CoopRole& output) const {
    if (!mHost && !mGuest) return false;
    output = mHost ? CoopRole::Host : CoopRole::Guest;
    return true;
}
bool CoopConnection::stats(TransportStats& output) const {
    return connected() && link()->stats(output);
}
bool CoopConnection::pollBeforeSession(TransportEvent& event) {
    if (mSession || !link()) return false;
    if (!mPending.empty()) {
        mPendingBytes -= mPending.front().payload.size();
        event = std::move(mPending.front());mPending.pop_front();return true;
    }
    return link()->poll(event);
}
bool CoopConnection::sendBeforeSession(const std::vector<std::uint8_t>& payload) {
    return !mSession && connected() && !payload.empty() && payload.size() <= kActorMaxPacketBytes &&
           link()->send(Delivery::ReliableOrdered, payload.data(), payload.size());
}
bool CoopConnection::beginSession(std::uint64_t id, std::uint16_t epoch,
                                  std::uint64_t baseline, std::uint64_t now) {
    if (mSession || !id || !epoch || !baseline || !connected() ||
        (id == mLastSession && epoch <= mLastEpoch)) return false;
    auto session = std::make_unique<CoopSession>(*link(), mHost ? CoopRole::Host : CoopRole::Guest);
    // Even a failed first status send retires its issued context. Never let a
    // retry interpret a delayed partial start as a new scene with the same ID.
    mLastSession = id; mLastEpoch = epoch;
    if (!session->begin(id, epoch, baseline, now)) return false;
    session->mBuffered = std::move(mPending);
    mPending.clear();
    mPendingBytes = 0;
    mSession = std::move(session);
    return true;
}
void CoopConnection::endSession() {
    if (mSession) mSession->end();
    mSession.reset();
}
bool CoopConnection::maintain(std::uint64_t now, std::uint64_t unixSeconds, RoomStatus& updated) {
    return mHost && mHost->maintain(now, unixSeconds, updated);
}
void CoopConnection::close() {
    endSession(); // Session borrows GatedTransport; never reverse this order.
    if (mGuest) mGuest->cancel();
    if (mHost) mHost->close();
    mGuest.reset(); mHost.reset();
    mPending.clear();mPendingBytes=0;
}
} // namespace nectar::net
