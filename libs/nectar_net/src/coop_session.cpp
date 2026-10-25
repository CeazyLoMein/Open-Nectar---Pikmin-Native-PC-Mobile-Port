#include "nectar_net/coop_session.h"
#include "nectar_net/byte_io.h"
#include "nectar_net/limits.h"
#include <cmath>
#include <cstring>
#include <limits>

namespace nectar::net {
namespace {
constexpr std::uint8_t kHeartbeat = 0, kLoaded = 1, kReady = 2, kBlocks = 3, kAllBlocks = 7;
bool anyBytes(const std::array<std::uint8_t, 32> &a) {
    for (auto b : a)
        if (b)
            return true;
    return false;
}
bool pointValid(const Vec3 &p) {
    for (float x : {p.x, p.y, p.z})
        if (!std::isfinite(x) || std::fabs(x) > kMaxWorldCoordinate)
            return false;
    return true;
}
std::vector<std::uint8_t> markerBytes(std::uint8_t player, MarkerKind kind, const Vec3 &p) {
    ByteWriter w(14);
    w.writeU8(player);
    w.writeU8(static_cast<std::uint8_t>(kind));
    for (float v : {p.x, p.y, p.z}) {
        std::uint32_t bits;
        std::memcpy(&bits, &v, 4);
        w.writeU32(bits);
    }
    return w.bytes();
}
bool readMarker(const std::vector<std::uint8_t> &b, std::uint8_t &player, MarkerKind &kind, Vec3 &p) {
    if (b.size() != 14)
        return false;
    ByteReader r(b);
    std::uint8_t k = 0;
    if (!r.readU8(player) || !r.readU8(k) || player > 1 || k > 3)
        return false;
    float v[3];
    for (float &x : v) {
        std::uint32_t bits;
        if (!r.readU32(bits))
            return false;
        std::memcpy(&x, &bits, 4);
    }
    p = {v[0], v[1], v[2]};
    kind = static_cast<MarkerKind>(k);
    return pointValid(p);
}
} // namespace
void requireCoopSessionCapability(CompatibilityInfo &info) {
    info.capabilities |= kCoopSessionCapability;
    info.requiredCapabilities |= kCoopSessionCapability;
}
bool CoopSession::linked() const {
    const auto *c = mLink.compatibility();
    return mLink.role() ==
               (mRole == CoopRole::Host ? GatedTransport::Role::Host : GatedTransport::Role::Guest) &&
           mLink.state() == TransportState::Connected && mLink.joinState() == JoinState::Authenticated && c &&
           c->state() == CompatibilityState::Compatible &&
           (c->peer().capabilities & kCoopSessionCapability) != 0 && anyBytes(c->peer().build) &&
           anyBytes(c->peer().content);
}
bool CoopSession::begin(std::uint64_t session, std::uint16_t epoch, std::uint64_t baseline,
                        std::uint64_t now) {
    if (mActive || !session || !epoch || !baseline || !linked() ||
        (session == mLastSession && epoch <= mLastEpoch))
        return false;
    end();
    if (!mActors.begin(session, epoch))
        return false;
    mSession = session;
    mEpoch = epoch;
    mRequiredFrame = baseline;
    mLastHeard = mLastHeartbeat = now;
    mActive = true;
    mLastSession = session;
    mLastEpoch = epoch;
    if (mRole == CoopRole::Host && !publishView()) {
        lost();
        return false;
    }
    return true;
}
void CoopSession::end() {
    mActive = false;
    mLost = false;
    mSession = 0;
    mEpoch = 0;
    mRequiredFrame = mLastPublished = mLastPublishedTick = mLastActorAt = 0;
    mSent = mReceived = 0;
    mLocalLoaded = mLocalReady = mHaveView = false;
    mLocalBlocks = 0;
    mView = CoopView{};
    mActors.end();
    mMarkers = {};
    mLastMarker = {};
    mMarked = {};
}
void CoopSession::lost() {
    mLost = true;
    mLocalReady = false;
}
bool CoopSession::send(MessageType type, const std::vector<std::uint8_t> &payload) {
    if (!mActive || mLost)
        return false;
    if (!linked() || mSent == std::numeric_limits<std::uint32_t>::max()) {
        lost();
        return false;
    }
    Message msg;
    msg.header.type = type;
    msg.header.sessionId = mSession;
    msg.header.sceneEpoch = mEpoch;
    msg.header.sequence = mSent + 1;
    msg.payload = payload;
    std::vector<std::uint8_t> bytes;
    if (!encodeMessage(msg, bytes) || !mLink.send(Delivery::ReliableOrdered, bytes.data(), bytes.size())) {
        lost();
        return false;
    }
    ++mSent;
    return true;
}
bool CoopSession::control(std::uint8_t op, std::uint8_t value, std::uint64_t frame) {
    ByteWriter w(10);
    w.writeU8(op);
    w.writeU8(value);
    w.writeU64(frame);
    return send(MessageType::CoopControl, w.bytes());
}
bool CoopSession::publishView() {
    ByteWriter w(12);
    w.writeU64(mView.revision);
    w.writeU8(static_cast<std::uint8_t>((mView.loaded[0] ? 1 : 0) | (mView.loaded[1] ? 2 : 0)));
    w.writeU8(static_cast<std::uint8_t>((mView.ready[0] ? 1 : 0) | (mView.ready[1] ? 2 : 0)));
    w.writeU8(mView.blockers[0]);
    w.writeU8(mView.blockers[1]);
    mHaveView = true;
    return send(MessageType::CoopStatus, w.bytes());
}
bool CoopSession::publishActors(const std::vector<std::vector<std::uint8_t>> &packets, std::uint64_t now) {
    if (mRole != CoopRole::Host || !mActive || mLost || packets.empty() || packets.size() > 512)
        return false;
    if (mLastPublished && (now < mLastActorAt || now - mLastActorAt < kActorPeriodMs))
        return false;
    TransportStats stats;
    if (mLink.stats(stats) && stats.pendingReliableBytes >= kReliableBacklogLimit)
        return false;
    ActorFrameReceiver check;
    if (!check.begin(mSession, mEpoch))
        return false;
    std::size_t commits = 0;
    for (const auto &p : packets) {
        const auto result = check.receive(p.data(), p.size(), 0);
        if (result == ActorFrameReceiver::Result::Rejected || result == ActorFrameReceiver::Result::Ignored)
            return false;
        commits += result == ActorFrameReceiver::Result::Committed ? 1U : 0U;
    }
    if (commits != 1 || check.assembling() || check.current().frame < mRequiredFrame ||
        check.current().frame <= mLastPublished || check.current().tick < mLastPublishedTick)
        return false;
    for (const auto &p : packets)
        if (!send(MessageType::WorldSnapshot, p))
            return false;
    mLastPublished = check.current().frame;
    mLastPublishedTick = check.current().tick;
    mLastActorAt = now;
    return true;
}
bool CoopSession::confirmWorldLoaded() {
    if (!mActive || mLost)
        return false;
    const auto frame = mRole == CoopRole::Host ? mLastPublished : mActors.current().frame;
    if (frame < mRequiredFrame)
        return false;
    if (mLocalLoaded)
        return true;
    if (mRole == CoopRole::Host) {
        mLocalLoaded = true;
        mView.loaded[0] = true;
        ++mView.revision;
        return publishView();
    }
    if (!control(kLoaded, 1, frame))
        return false;
    mLocalLoaded = true;
    return true;
}
bool CoopSession::setReady(bool ready) {
    if (!mActive || mLost ||
        (ready && (!mLocalLoaded || (mLocalBlocks & static_cast<std::uint8_t>(CoopBlock::Background)))))
        return false;
    if (mLocalReady == ready)
        return true;
    if (mRole == CoopRole::Host) {
        mLocalReady = ready;
        mView.ready[0] = ready;
        ++mView.revision;
        return publishView();
    }
    if (!control(kReady, ready ? 1 : 0))
        return false;
    mLocalReady = ready;
    return true;
}
bool CoopSession::setBlocked(CoopBlock reason, bool blocked) {
    const auto bit = static_cast<std::uint8_t>(reason);
    if (!mActive || mLost || (bit != 1 && bit != 2 && bit != 4))
        return false;
    const auto wanted = static_cast<std::uint8_t>(blocked ? mLocalBlocks | bit : mLocalBlocks & ~bit);
    if (wanted == mLocalBlocks)
        return true;
    // Freeze local commands immediately, even while the pause request travels.
    mLocalBlocks = wanted;
    if (wanted & 4)
        mLocalReady = false;
    if (mRole == CoopRole::Host) {
        mView.blockers[0] = wanted;
        if (wanted & 4)
            mView.ready[0] = false;
        ++mView.revision;
        return publishView();
    }
    return control(kBlocks, wanted);
}
bool CoopSession::placeMarker(MarkerKind kind, const Vec3 &point, std::uint64_t now) {
    const auto player = localPlayer();
    if (!mActive || mLost || !mLocalLoaded || !pointValid(point) || static_cast<std::uint8_t>(kind) > 3 ||
        (mMarked[player] && (now < mLastMarker[player] || now - mLastMarker[player] < kMarkerCooldownMs)))
        return false;
    if (!send(MessageType::CoopMarker, markerBytes(player, kind, point)))
        return false;
    mMarkers[player] = {point, kind, now + kMarkerMs, true};
    mLastMarker[player] = now;
    mMarked[player] = true;
    return true;
}
CoopMarker CoopSession::marker(std::uint8_t player, std::uint64_t now) const {
    if (player > 1)
        return {};
    auto m = mMarkers[player];
    m.visible = mActive && !mLost && m.visible && now < m.expiresAtMs;
    return m;
}
CoopPhase CoopSession::phase() const {
    if (!mActive)
        return CoopPhase::Closed;
    if (mLost || !linked())
        return CoopPhase::WaitingForPartner;
    if (!mHaveView || !mView.loaded[0] || !mView.loaded[1])
        return CoopPhase::Loading;
    if (mLocalBlocks || mView.blockers[0] || mView.blockers[1])
        return CoopPhase::Paused;
    if (!mLocalReady || !mView.ready[0] || !mView.ready[1])
        return CoopPhase::WaitingForReady;
    return CoopPhase::Running;
}
bool CoopSession::hostShouldAdvanceWorld() const {
    return mRole == CoopRole::Host && phase() == CoopPhase::Running;
}
bool CoopSession::canIssueCommands() const { return phase() == CoopPhase::Running; }
void CoopSession::receive(const TransportEvent &event, std::uint64_t now) {
    if (event.type == TransportEventType::Disconnected || event.type == TransportEventType::Error) {
        lost();
        return;
    }
    if (event.type != TransportEventType::Message || event.delivery != Delivery::ReliableOrdered)
        return;
    Message msg;
    if (decodeMessage(event.payload.data(), event.payload.size(), msg, kActorMaxPacketBytes) !=
        DecodeError::None)
        return;
    if (msg.header.sessionId != mSession || msg.header.sceneEpoch != mEpoch || !msg.header.sequence ||
        msg.header.sequence <= mReceived)
        return;
    bool accepted = false;
    if (mRole == CoopRole::Host && msg.header.type == MessageType::CoopControl && msg.payload.size() == 10) {
        const auto before = mView;
        ByteReader r(msg.payload);
        std::uint8_t op = 0, value = 0;
        std::uint64_t frame = 0;
        r.readU8(op);
        r.readU8(value);
        r.readU64(frame);
        if (op == kHeartbeat && value == 0 && frame == 0)
            accepted = true;
        else if (op == kLoaded && value == 1 && frame >= mRequiredFrame && frame <= mLastPublished) {
            mView.loaded[1] = true;
            accepted = true;
        } else if (op == kReady && value <= 1 && frame == 0 &&
                   (!value || (mView.loaded[1] && !(mView.blockers[1] & 4)))) {
            mView.ready[1] = value != 0;
            accepted = true;
        } else if (op == kBlocks && (value & ~kAllBlocks) == 0 && frame == 0) {
            mView.blockers[1] = value;
            if (value & 4)
                mView.ready[1] = false;
            accepted = true;
        }
        if (accepted && (before.loaded != mView.loaded || before.ready != mView.ready ||
                         before.blockers != mView.blockers)) {
            ++mView.revision;
            publishView();
        }
    } else if (mRole == CoopRole::Guest && msg.header.type == MessageType::CoopStatus &&
               msg.payload.size() == 12) {
        ByteReader r(msg.payload);
        CoopView v;
        std::uint8_t loaded = 0, ready = 0;
        r.readU64(v.revision);
        r.readU8(loaded);
        r.readU8(ready);
        r.readU8(v.blockers[0]);
        r.readU8(v.blockers[1]);
        if ((loaded & ~3) == 0 && (ready & ~loaded) == 0 && (v.blockers[0] & ~kAllBlocks) == 0 &&
            (v.blockers[1] & ~kAllBlocks) == 0 && v.revision >= mView.revision) {
            for (std::size_t i = 0; i < 2; ++i) {
                v.loaded[i] = (loaded & (1U << i)) != 0;
                v.ready[i] = (ready & (1U << i)) != 0;
            }
            mView = v;
            mHaveView = true;
            accepted = true;
        }
    } else if (mRole == CoopRole::Guest && msg.header.type == MessageType::WorldSnapshot) {
        const auto result = mActors.receive(msg.payload.data(), msg.payload.size(), now);
        accepted =
            result == ActorFrameReceiver::Result::Buffered || result == ActorFrameReceiver::Result::Committed;
    } else if (msg.header.type == MessageType::CoopMarker) {
        std::uint8_t player = 0;
        MarkerKind kind;
        Vec3 point;
        if (readMarker(msg.payload, player, kind, point) && (mRole == CoopRole::Guest || player == 1) &&
            (!mMarked[player] ||
             (now >= mLastMarker[player] && now - mLastMarker[player] >= kMarkerCooldownMs))) {
            if (mRole == CoopRole::Host && !mView.loaded[1])
                return;
            mMarkers[player] = {point, kind, now + kMarkerMs, true};
            mLastMarker[player] = now;
            mMarked[player] = true;
            accepted = true;
            if (mRole == CoopRole::Host)
                send(MessageType::CoopMarker, msg.payload);
        }
    }
    if (accepted) {
        mReceived = msg.header.sequence;
        mLastHeard = now;
    }
}
void CoopSession::pump(std::uint64_t now) {
    if (!mActive || mLost)
        return;
    if (!linked() || now < mLastHeard || now - mLastHeard >= kPeerTimeoutMs) {
        lost();
        return;
    }
    TransportEvent event;
    for (std::size_t i = 0; i < 64 && mLink.poll(event); ++i) {
        receive(event, now);
        if (mLost)
            return;
    }
    mActors.expire(now);
    if (now < mLastHeard || now - mLastHeard >= kPeerTimeoutMs) {
        lost();
        return;
    }
    if (now < mLastHeartbeat || now - mLastHeartbeat >= kHeartbeatMs) {
        if (mRole == CoopRole::Host)
            publishView();
        else
            control(kHeartbeat);
        mLastHeartbeat = now;
    }
}
} // namespace nectar::net
