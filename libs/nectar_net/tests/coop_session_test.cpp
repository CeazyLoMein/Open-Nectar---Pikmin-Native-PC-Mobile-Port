#include "nectar_net/byte_io.h"
#include "nectar_net/coop_session.h"
#include "nectar_net/sim_network.h"
#include <cstdio>
#include <limits>
#include <memory>

using namespace nectar::net;
namespace {
struct MeteredTransport final : ITransport {
    std::unique_ptr<ITransport> inner;
    int pending = 0;
    std::size_t sends = 0;
    explicit MeteredTransport(std::unique_ptr<ITransport> p) : inner(std::move(p)) {}
    bool listen(const Endpoint &e) override { return inner->listen(e); }
    bool connect(const Endpoint &e) override { return inner->connect(e); }
    bool send(Delivery d, const std::uint8_t *p, std::size_t n) override {
        ++sends;
        return inner->send(d, p, n);
    }
    bool poll(TransportEvent &e) override { return inner->poll(e); }
    void disconnectPeer(bool f) override { inner->disconnectPeer(f); }
    void close() override { inner->close(); }
    TransportState state() const override { return inner->state(); }
    bool stats(TransportStats &s) const override {
        const bool ok = inner->stats(s);
        s.pendingReliableBytes = pending;
        return ok;
    }
};
int failures = 0;
void check(bool ok, const char *why) {
    if (!ok) {
        std::printf("FAIL %s\n", why);
        ++failures;
    }
}
JoinCredentials credentials() {
    JoinCredentials c;
    for (std::size_t i = 0; i < 16; ++i) {
        c.sessionNonce[i] = static_cast<std::uint8_t>(i + 1);
        c.joinSecret[i] = static_cast<std::uint8_t>(i + 81);
    }
    return c;
}
struct Pair {
    SimulatedNetwork net{20261024};
    std::uint64_t now = 0;
    MeteredTransport *meter = nullptr;
    MeteredTransport *guestMeter = nullptr;
    std::unique_ptr<ITransport> hostEnd() {
        auto p = std::make_unique<MeteredTransport>(net.createHost());
        meter = p.get();
        return p;
    }
    std::unique_ptr<ITransport> guestEnd() {
        auto p = std::make_unique<MeteredTransport>(net.createGuest());
        guestMeter = p.get();
        return p;
    }
    GatedTransport h, g;
    CoopSession host, guest;
    Pair(bool capability = true, bool identities = true, bool mismatch = false)
        : h(hostEnd(), GatedTransport::Role::Host, credentials(), [this] { return now; }),
          g(guestEnd(), GatedTransport::Role::Guest, credentials(), [this] { return now; }),
          host(h, CoopRole::Host), guest(g, CoopRole::Guest) {
        LinkConditions c;
        c.latencyMs = 20;
        c.jitterMs = 10;
        c.lossPerMille = 100;
        c.duplicatePerMille = 100;
        net.setHostToGuest(c);
        net.setGuestToHost(c);
        CompatibilityInfo info;
        info.game = static_cast<std::uint8_t>(GameId::Pikmin1);
        info.region = 1;
        if (identities) {
            info.build.fill(11);
            info.content.fill(22);
        }
        if (capability)
            requireCoopSessionCapability(info);
        h.requireCompatibility(info);
        if (mismatch)
            info.content[0] ^= 1;
        g.requireCompatibility(info);
        check(h.listen({"", 1}) && g.connect({"", 1}), "in-memory transport opens");
        check(!host.begin(100, 1, 1, now), "session cannot start before authentication/compatibility");
        for (; now < 1000; now += 5) {
            net.advance(now);
            TransportEvent e;
            while (h.poll(e)) {
            }
            while (g.poll(e)) {
            }
            if (h.state() == TransportState::Connected && g.state() == TransportState::Connected)
                break;
        }
    }
    void settle(std::uint64_t duration = 200) {
        const auto end = now + duration;
        for (; now < end; now += 5) {
            net.advance(now);
            host.pump(now);
            guest.pump(now);
        }
    }
    std::vector<std::vector<std::uint8_t>> frame(std::uint16_t epoch, std::uint64_t number = 1) {
        CaptainState a, b;
        b.player = 1;
        std::vector<EntityRecord> r = {captainRecord(epoch, a), captainRecord(epoch, b)};
        for (std::uint32_t i = 0; i < 60; ++i) {
            PikminState p;
            p.owner = static_cast<std::uint8_t>(i % 2);
            p.leader = p.owner;
            p.position.x = static_cast<float>(i);
            r.push_back(pikminRecord(NetEntityId{epoch, EntityKind::Pikmin, 0, i + 10}.pack(), p));
        }
        std::vector<std::vector<std::uint8_t>> packets;
        check(packActorFrame(100, epoch, number, number, r, 1000, {}, packets), "fixture frame packs");
        return packets;
    }
    void begin(std::uint16_t epoch = 1) {
        check(host.begin(100, epoch, 1, now) && guest.begin(100, epoch, 1, now),
              "matching accepted session and scene begin");
    }
    void load(std::uint16_t epoch = 1) {
        check(host.publishActors(frame(epoch), now),
              "host publishes complete actual actor schema through gated transport");
        check(!guest.confirmWorldLoaded(), "guest cannot load before complete actor baseline");
        check(host.confirmWorldLoaded(), "host world adapter loaded");
        settle();
        check(guest.actors().pikmin.size() == 60, "all60 owned Pikmin crossed authenticated transport");
        check(guest.confirmWorldLoaded(), "guest adapter confirms world after complete baseline");
        settle();
    }
    void ready() {
        check(host.setReady(true) && guest.setReady(true), "both explicit ready requests");
        settle();
        check(host.phase() == CoopPhase::Running && guest.phase() == CoopPhase::Running,
              "both ready and loaded allows session");
    }
    void inject(MessageType type, std::vector<std::uint8_t> payload, std::uint32_t seq,
                std::uint16_t epoch = 1) {
        Message m;
        m.header.type = type;
        m.header.sessionId = 100;
        m.header.sceneEpoch = epoch;
        m.header.sequence = seq;
        m.payload = std::move(payload);
        std::vector<std::uint8_t> b;
        check(encodeMessage(m, b) && g.send(Delivery::ReliableOrdered, b.data(), b.size()),
              "authenticated malformed/forged request fixture sent");
    }
};
std::vector<std::uint8_t> ctrl(std::uint8_t op, std::uint8_t value, std::uint64_t frame = 0) {
    ByteWriter w(10);
    w.writeU8(op);
    w.writeU8(value);
    w.writeU64(frame);
    return w.bytes();
}
std::vector<std::uint8_t> mark(std::uint8_t player) {
    ByteWriter w(14);
    w.writeU8(player);
    w.writeU8(0);
    w.writeU32(0);
    w.writeU32(0);
    w.writeU32(0);
    return w.bytes();
}
} // namespace
int main() {
    {
        Pair p(false);
        check(!p.host.begin(100, 1, 1, p.now), "old builds without session capability cannot enter");
    }
    {
        Pair p(true, false);
        check(!p.host.begin(100, 1, 1, p.now), "unknown all-zero build/content identity refused");
    }
    {
        Pair p(true, true, true);
        check(!p.host.begin(100, 1, 1, p.now) && !p.guest.begin(100, 1, 1, p.now),
              "mismatched gameplay content cannot begin");
    }
    Pair p;
    CoopSession wrongRole(p.g, CoopRole::Host);
    check(!wrongRole.begin(100, 1, 1, p.now), "guest transport cannot be used as host authority");
    p.begin();
    check(p.host.phase() == CoopPhase::Loading && !p.host.hostShouldAdvanceWorld(),
          "world held during loading");
    check(!p.host.setReady(true) && !p.guest.setReady(true), "cannot ready before world baseline");
    p.load();
    check(p.host.phase() == CoopPhase::WaitingForReady && p.guest.phase() == CoopPhase::WaitingForReady,
          "loading never auto-starts play");
    check(!p.guest.publishActors(p.frame(1), p.now), "guest cannot publish authoritative actor frames");
    check(!p.host.publishActors(p.frame(1), p.now), "same authoritative frame cannot be republished as new");
    p.ready();
    const auto repeated = p.net.sent();
    for (int i = 0; i < 100; ++i) {
        check(p.host.confirmWorldLoaded() && p.guest.confirmWorldLoaded(), "repeat loaded is idempotent");
        check(p.host.setReady(true) && p.guest.setReady(true), "repeat ready is idempotent");
        check(p.host.setBlocked(CoopBlock::Settings, false) && p.guest.setBlocked(CoopBlock::Settings, false),
              "repeat blocker is idempotent");
    }
    check(p.net.sent() == repeated, "repeated UI state cannot flood either connection");
    p.meter->pending = CoopSession::kReliableBacklogLimit;
    const auto sends = p.meter->sends;
    check(!p.host.publishActors(p.frame(1, 2), p.now) && p.meter->sends == sends,
          "queued connection defers WHOLE actor update without partial sends");
    p.meter->pending = 0;
    check(p.host.publishActors(p.frame(1, 2), p.now), "actor transfer resumes when network catches up");
    check(!p.host.publishActors(p.frame(1, 3), p.now),
          "visual render FPS cannot flood actor network updates");
    p.settle();
    check(p.guest.actors().frame == 2 && p.host.publishActors(p.frame(1, 3), p.now),
          "network cadence independent of renderer and next full update allowed");
    p.settle();
    check(p.host.hostShouldAdvanceWorld() && !p.guest.hostShouldAdvanceWorld() && p.guest.canIssueCommands(),
          "only host advances official world; guest issues commands");
    check(p.guest.setBlocked(CoopBlock::Settings, true) && !p.guest.canIssueCommands(),
          "guest menu blocks its own commands immediately");
    p.settle();
    check(p.host.phase() == CoopPhase::Paused && !p.host.hostShouldAdvanceWorld(),
          "guest settings pause official world");
    check(p.host.setBlocked(CoopBlock::Manual, true), "host manual pause");
    p.settle();
    check(p.guest.setBlocked(CoopBlock::Settings, false), "guest leaves settings");
    p.settle();
    check(p.host.phase() == CoopPhase::Paused, "guest cannot clear host pause");
    check(p.host.setBlocked(CoopBlock::Manual, false), "host resumes its own pause");
    p.settle();
    check(p.host.phase() == CoopPhase::Running, "resume after all pause reasons clear");
    check(p.guest.setBlocked(CoopBlock::Background, true), "phone interruption reported");
    p.settle();
    check(p.host.phase() == CoopPhase::Paused && !p.host.view().ready[1],
          "backgrounding pauses world and removes guest readiness");
    check(!p.guest.setReady(true), "backgrounded phone cannot re-ready");
    check(p.guest.setBlocked(CoopBlock::Background, false), "guest foreground");
    p.settle();
    check(p.host.phase() == CoopPhase::WaitingForReady && !p.guest.canIssueCommands(),
          "foregrounding never auto-resumes combat");
    check(p.guest.setReady(true), "guest deliberately resumes");
    p.settle();
    check(p.host.phase() == CoopPhase::Running, "both present and ready again");
    const auto revision = p.host.view().revision;
    check(p.guest.placeMarker(MarkerKind::Help, {50, 2, 30}, p.now), "guest teammate help marker");
    check(!p.guest.placeMarker(MarkerKind::Danger, {1, 2, 3}, p.now), "local marker flood limited");
    p.settle();
    check(p.host.marker(1, p.now).visible && p.host.marker(1, p.now).kind == MarkerKind::Help &&
              p.host.marker(1, p.now).position.x == 50,
          "partner sees typed world-space mark");
    check(p.host.view().revision == revision && p.host.hostShouldAdvanceWorld(),
          "marker has no pause/ownership/AI side effects");
    check(p.host.placeMarker(MarkerKind::Carry, {5, 6, 7}, p.now), "host carry/help coordinate marker");
    p.settle();
    check(p.guest.marker(0, p.now).visible && p.guest.marker(0, p.now).position.z == 7,
          "guest receives host marker");
    check(!p.host.marker(0, p.now + CoopSession::kMarkerMs).visible, "marker expires without retained queue");
    check(
        !p.guest.placeMarker(MarkerKind::Help, {std::numeric_limits<float>::infinity(), 0, 0}, p.now + 1001),
        "nonfinite marker refused");
    p.inject(MessageType::CoopMarker, mark(0), 1000000);
    p.inject(MessageType::CoopControl, ctrl(2, 2), 1000001);
    p.inject(MessageType::CoopControl, ctrl(3, 255), 1000002);
    p.inject(MessageType::CoopControl, ctrl(1, 1, 999999), 1000003);
    p.inject(MessageType::CoopControl, ctrl(2, 0), 1000004, 2);
    p.settle();
    check(p.host.phase() == CoopPhase::Running && p.host.marker(0, p.now).visible,
          "spoofed player, bad blockers/ready/frame and stale scene cannot change authority");
    // An old or unrecognized request must not advance the accepted sequence.
    check(p.guest.setReady(false), "legitimate request after rejected forged sequence");
    p.settle();
    check(p.host.phase() == CoopPhase::WaitingForReady,
          "invalid high sequence cannot poison normal control stream");
    check(p.guest.setReady(true), "legitimate re-ready");
    p.settle();
    p.inject(MessageType::CoopControl, ctrl(2, 0), 1);
    p.settle();
    check(p.host.phase() == CoopPhase::Running, "replayed old ready request ignored");
    // Stop pumping guest (phone suspended): host must not keep the day running.
    const auto stop = p.now;
    for (; p.now < stop + 3100; p.now += 5) {
        p.net.advance(p.now);
        p.host.pump(p.now);
    }
    check(p.host.phase() == CoopPhase::WaitingForPartner && !p.host.hostShouldAdvanceWorld(),
          "missing peer heartbeat freezes host world");
    p.guest.pump(p.now);
    check(p.guest.phase() == CoopPhase::WaitingForPartner && !p.guest.canIssueCommands(),
          "stale queued status cannot revive suspended guest");
    check(p.guest.actors().pikmin.size() == 60, "disconnect retains last complete visual replica");
    check(!p.guest.setReady(true) && !p.host.setReady(true),
          "lost peer cannot silently resume with ready command");
    p.host.end();
    p.guest.end();
    check(!p.host.begin(100, 1, 1, p.now) && !p.guest.begin(100, 1, 1, p.now),
          "same accepted scene cannot replay after end");
    // Re-authenticate the underlying connection; a fresh accepted epoch still
    // requires a NEW baseline and two explicit ready checks.
    p.h.close();
    p.g.close();
    {
        TransportEvent e;
        while (p.h.poll(e)) {
        }
        while (p.g.poll(e)) {
        }
    } // drain events belonging to the OLD closed connection
    p.h.listen({"", 1});
    p.g.connect({"", 1});
    for (auto end = p.now + 1000; p.now < end; p.now += 5) {
        p.net.advance(p.now);
        TransportEvent e;
        while (p.h.poll(e)) {
        }
        while (p.g.poll(e)) {
        }
        if (p.h.state() == TransportState::Connected && p.g.state() == TransportState::Connected)
            break;
    }
    p.begin(2);
    check(p.guest.phase() == CoopPhase::Loading && !p.guest.confirmWorldLoaded(),
          "rejoin cannot use previous scene baseline");
    p.load(2);
    p.ready();
    check(p.host.phase() == CoopPhase::Running,
          "re-authentication + new scene + baseline + readiness restores session");
    p.h.disconnectPeer(false);
    p.settle(10);
    check(p.host.phase() == CoopPhase::WaitingForPartner && !p.guest.canIssueCommands(),
          "explicit link close blocks play immediately");
    p.host.end();
    p.guest.end();
    check(p.guest.phase() == CoopPhase::Closed && p.guest.actors().pikmin.empty(),
          "leave clears protocol replicas, not game saves");

    {
        Pair q;
        NetInputFrame input; input.tick=3; input.stickX=90; input.held=1; input.flags=1;
        InputHealth health;
        NetInputFrame applied;
        q.begin();
        check(!q.guest.publishInput({input},q.now),"no guest commands before baseline/ready");
        check(!q.host.consumeGuestInput(1,applied,health)&&health==InputHealth::Neutral,
              "loading world cannot consume remote movement");
        q.load();q.ready();
        check(!q.host.publishInput({input},q.now),"host cannot impersonate guest input sender");
        check(!q.guest.consumeGuestInput(3,applied,health),"guest cannot consume authoritative input");
        auto invalid=input;invalid.stickX=-128;
        check(!q.guest.publishInput({invalid},q.now),"out-of-range stick rejected before send");
        invalid=input;invalid.tick=50000;
        check(!q.guest.publishInput({invalid},q.now),"future timestamp cannot fill host input buffer");
        auto older=input;older.tick=1;
        check(!q.guest.publishInput({input,older},q.now),"noncontiguous redundant bundle refused");
        q.guestMeter->pending=CoopSession::kReliableBacklogLimit;
        const auto guestSends=q.guestMeter->sends;
        check(!q.guest.publishInput({input},q.now) && q.guestMeter->sends==guestSends,
              "congested guest queues no movement and does not advance send state");
        q.guestMeter->pending=0;
        check(q.guest.publishInput({input},q.now),"guest publishes one target HOST tick after congestion clears");
        auto next=input;next.tick=4;
        check(!q.guest.publishInput({next},q.now),"120FPS renderer cannot flood input sends");
        q.settle();
        check(q.host.consumeGuestInput(3,applied,health)&&health==InputHealth::Live&&
              applied.stickX==90&&(applied.pressed&1)&&applied.flags==1,
              "authenticated impaired link delivers guest movement/one-shot to host only");
        check(!q.host.consumeGuestInput(3,applied,health)&&health==InputHealth::Neutral,
              "same host tick cannot apply input twice");
        check(q.host.consumeGuestInput(4,applied,health)&&health==InputHealth::Repeated&&
              applied.stickX==90&&!applied.pressed&&!applied.flags,
              "gap briefly holds movement without repeating action press");
        check(q.host.consumeGuestInput(10,applied,health)&&health==InputHealth::Neutral&&
              applied.stickX==0&&(applied.released&1),"expired guest input releases held buttons");
        check(q.host.consumeGuestInput(11,applied,health)&&applied.released==0,
              "missing partner release is not repeated");
        // Queue movement for a later host tick, then pause/resume before it is used.
        input.tick=14;check(q.guest.publishInput({input},q.now),"queue movement before pause");
        q.settle();
        const auto oldRevision=q.host.view().revision;
        check(q.host.setBlocked(CoopBlock::Manual,true),"pause clears pending input generation");
        q.settle();
        check(!q.host.consumeGuestInput(12,applied,health)&&applied.stickX==0,
              "paused host returns neutral and does not consume tick");
        check(!q.guest.publishInput({input},q.now),"paused guest cannot publish commands");
        check(q.host.setBlocked(CoopBlock::Manual,false),"resume changes control revision");q.settle();
        check(q.host.consumeGuestInput(14,applied,health)&&health==InputHealth::Neutral&&applied.stickX==0,
              "pre-pause queued movement never leaks into resumed host world");
        ByteWriter oldInput(8+128);oldInput.writeU64(oldRevision);
        input.tick=16;auto payload=encodeInputBundle({input});oldInput.writeBytes(payload.data(),payload.size());
        q.inject(MessageType::InputBundle,oldInput.bytes(),999999);q.settle();
        check(q.host.consumeGuestInput(16,applied,health)&&health==InputHealth::Neutral,
              "old-revision delayed input rejected without sequence poisoning");
        input.tick=18;check(q.guest.publishInput({input},q.now),"new revision accepts fresh guest controls");
        q.settle();
        check(q.host.consumeGuestInput(18,applied,health)&&health==InputHealth::Live&&applied.stickX==90,
              "legitimate stream still works after rejected high-sequence replay");
        check(q.host.consumeGuestInput(1000000000,applied,health)&&health==InputHealth::Neutral,
              "large trusted host-tick jump discards history in bounded time");
        check(!q.host.consumeGuestInput(std::numeric_limits<std::uint64_t>::max(),applied,health),
              "tick wraparound refused before buffering math");
        q.h.disconnectPeer(false);q.settle(10);
        check(!q.host.consumeGuestInput(1000000001,applied,health)&&applied.stickX==0&&
              !q.guest.publishInput({input},q.now),"disconnect stops all movement commands");
    }

    {
        Pair delayed; delayed.begin(); delayed.load(); delayed.ready();
        LinkConditions loss; loss.lossPerMille=1000; loss.reliableLossDelayMs=200;
        delayed.net.setHostToGuest(loss);
        check(delayed.host.setBlocked(CoopBlock::Manual,true), "host pause queued under simulated reliable delay");
        delayed.net.setHostToGuest({});
        NetInputFrame command; command.tick=3; command.stickX=75; command.held=1;
        check(delayed.guest.publishInput({command},delayed.now), "guest can briefly send before delayed pause arrives");
        delayed.settle(100);
        InputHealth health;NetInputFrame applied;
        check(!delayed.host.hostShouldAdvanceWorld() &&
              !delayed.host.consumeGuestInput(3,applied,health) && applied.stickX==0,
              "host stays frozen despite guest input before delayed pause arrives");
        delayed.settle(200);
        check(!delayed.guest.canIssueCommands(), "guest learns pause after ordered delay clears");
        check(delayed.host.setBlocked(CoopBlock::Manual,false), "host can resume after delayed pause");
        delayed.settle();
        check(delayed.host.consumeGuestInput(3,applied,health) && applied.stickX==0,
              "input generated before delayed pause cannot leak into resumed world");
    }

    if (!failures)
        std::puts("PASS co-op session over real join/compatibility gate:19-stage "
                  "ready/pause/background/rejoin lifecycle, whole squad transfer, safe authority, typed "
                  "bounded teammate pings and network interruption");
    return failures ? 1 : 0;
}
