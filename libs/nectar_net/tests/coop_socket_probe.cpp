// Real encrypted loopback UDP, authentication, compatibility and session flow.
// No game assets, save files, router mapping or synthetic transport involved.
#include "nectar_net/coop_session.h"
#include "nectar_net/gns_transport.h"
#include "nectar_net/secure_random.h"
#include "nectar_net/room.h"
#include <chrono>
#include <cstdio>
#include <memory>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <cstdlib>

using namespace nectar::net;
namespace {
// A stuck constructor/poll/destructor must produce a FAIL, not an endless CI hang.
// Test process only: never built into the game's room UI.
class ProbeDeadline {
    std::mutex mutex;
    std::condition_variable wake;
    bool done = false;
    std::thread worker;
public:
    ProbeDeadline() : worker([this] {
        std::unique_lock<std::mutex> lock(mutex);
        if (!wake.wait_for(lock, std::chrono::seconds(60), [this] { return done; })) {
            std::fputs("FAIL native probe deadline reached; inspect the last completed stage\n", stderr);
            std::fflush(stderr);
            std::_Exit(124);
        }
    }) {}
    ~ProbeDeadline() {
        { std::lock_guard<std::mutex> lock(mutex); done = true; }
        wake.notify_one();
        worker.join();
    }
};
std::uint64_t nowMs() {
    return static_cast<std::uint64_t>(std::chrono::duration_cast<std::chrono::milliseconds>(
        std::chrono::steady_clock::now().time_since_epoch()).count());
}
template<class Pump, class Done> bool until(Pump pump, Done done, std::uint64_t wait = 5000) {
    const auto end = nowMs() + wait;
    do {
        pump();
        if (done()) return true;
        std::this_thread::sleep_for(std::chrono::milliseconds(2));
    } while (nowMs() < end);
    return false;
}
bool require(bool ok, const char* label) {
    std::printf("%s %s\n", ok ? "PASS" : "FAIL", label);
    std::fflush(stdout);
    return ok;
}
CompatibilityInfo identity() {
    // Explicit probe fixture identity, never used for actual game/content checks.
    CompatibilityInfo info;
    info.game = static_cast<std::uint8_t>(GameId::Pikmin1);
    info.region = 1;
    info.build.fill(42);
    info.content.fill(73);
    requireCoopSessionCapability(info);
    return info;
}
}
int main() {
    std::setvbuf(stdout, nullptr, _IONBF, 0);
    std::puts("NECTAR_COOP_SOCKET_PROBE_STARTED");
    ProbeDeadline deadline;
    JoinCredentials secret;
    if (!require(secureRandomBytes(secret.sessionNonce.data(), secret.sessionNonce.size()) &&
                 secureRandomBytes(secret.joinSecret.data(), secret.joinSecret.size()),
                 "OS random source; private credentials never printed")) return 1;
    std::puts("STAGE encrypted transport creation");
    GatedTransport host(std::make_unique<GnsTransport>(), GatedTransport::Role::Host, secret);
    host.requireCompatibility(identity());
    Endpoint address{"127.0.0.1", 0};
    // Several loopback-only ports avoid one occupied CI port causing a false failure.
    bool listening = false;
    for (std::uint16_t port = 39920; port < 39930 && !listening; ++port) {
        address.port = port;
        listening = host.listen(address);
    }
    if (!require(listening, "real UDP listener opens on loopback only")) return 1;
    // A socket connection alone does not authorize a partner.
    auto wrong = secret;
    wrong.joinSecret[0] ^= 1;
    {
        GatedTransport intruder(std::make_unique<GnsTransport>(), GatedTransport::Role::Guest, wrong);
        intruder.requireCompatibility(identity());
        if (!require(intruder.connect(address), "wrong-secret attempt starts")) return 1;
        if (!require(until([&] {
            TransportEvent e;
            while (host.poll(e)) {}
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
            while (intruder.poll(e)) {}
        }, [&] { return intruder.lastJoinError() == JoinError::Refused; }),
            "wrong join secret rejected over real encrypted UDP")) return 1;
    }
    GatedTransport guest(std::make_unique<GnsTransport>(), GatedTransport::Role::Guest, secret);
    guest.requireCompatibility(identity());
    if (!require(guest.connect(address), "matching partner connection starts")) return 1;
    if (!require(until([&] {
        TransportEvent e;
        while (host.poll(e)) {}
        while (guest.poll(e)) {}
    }, [&] { return host.state() == TransportState::Connected && guest.state() == TransportState::Connected; }),
        "join secret and build/content compatibility accepted")) return 1;
    CoopSession h(host, CoopRole::Host), g(guest, CoopRole::Guest);
    if (!require(h.begin(100, 1, 1, nowMs()) && g.begin(100, 1, 1, nowMs()),
                 "accepted scene starts held for loading")) return 1;
    auto pump = [&] { h.pump(nowMs()); g.pump(nowMs()); };
    CaptainState a, b;
    b.player = 1;
    std::vector<EntityRecord> records{captainRecord(1, a), captainRecord(1, b)};
    for (std::uint32_t i = 0; i < 60; ++i) {
        PikminState p;
        p.owner = p.leader = static_cast<std::uint8_t>(i % 2);
        p.position.x = static_cast<float>(i);
        records.push_back(pikminRecord(NetEntityId{1, EntityKind::Pikmin, 0, i + 10}.pack(), p));
    }
    std::vector<std::vector<std::uint8_t>> packets;
    if (!require(packActorFrame(100, 1, 1, 1, records, 1000, {}, packets) &&
                 h.publishActors(packets, nowMs()), "complete 60-Pikmin frame sent through real socket")) return 1;
    if (!require(until(pump, [&] { return g.actors().frame == 1; }) &&
                 g.actors().pikmin.size() == 60 && g.actors().captains.size() == 2,
                 "receiver atomically reconstructs both captains and all 60 Pikmin")) return 1;
    // This fixture has no other world systems; real engine must attest ALL systems.
    if (!require(h.confirmWorldLoaded() && g.confirmWorldLoaded() && h.setReady(true) && g.setReady(true),
                 "both deliberately ready after fixture baseline loads")) return 1;
    if (!require(until(pump, [&] { return h.hostShouldAdvanceWorld() && g.canIssueCommands(); }),
                 "host alone owns simulation; ready partner may issue commands")) return 1;
    if (!require(g.setBlocked(CoopBlock::Settings, true) &&
                 until(pump, [&] { return h.phase() == CoopPhase::Paused; }),
                 "partner settings pauses official world")) return 1;
    if (!require(g.setBlocked(CoopBlock::Settings, false) &&
                 until(pump, [&] { return h.phase() == CoopPhase::Running; }),
                 "closing settings clears only that pause")) return 1;
    if (!require(g.placeMarker(MarkerKind::Help, {17, 2, 39}, nowMs()) &&
                 until(pump, [&] { return h.marker(1, nowMs()).visible; }) &&
                 h.marker(1, nowMs()).position.x == 17,
                 "typed partner marker crosses the encrypted connection")) return 1;
    if (!require(g.setBlocked(CoopBlock::Background, true) &&
                 until(pump, [&] { return h.phase() == CoopPhase::Paused && !h.view().ready[1]; }),
                 "phone interruption pauses and removes partner readiness")) return 1;
    if (!require(g.setBlocked(CoopBlock::Background, false) &&
                 until(pump, [&] { return h.phase() == CoopPhase::WaitingForReady; }) &&
                 g.setReady(true) && until(pump, [&] { return h.hostShouldAdvanceWorld(); }),
                 "foreground needs explicit partner readiness")) return 1;
    TransportStats stats;
    if (!require(host.stats(stats) && stats.rttMs >= 0, "real connection exposes measured RTT")) return 1;
    guest.disconnectPeer(false);
    if (!require(until(pump, [&] { return h.phase() == CoopPhase::WaitingForPartner; }) &&
                 !h.hostShouldAdvanceWorld() && g.actors().pikmin.size() == 60,
                 "disconnect freezes official world and retains last complete replica")) return 1;
    h.end(); g.end(); guest.close(); host.close();
    RoomConfig config;
    config.compatibility = identity();
    config.automaticPortMapping = false;
    config.includeLanEndpoint = false;
    config.localPort = static_cast<std::uint16_t>(address.port + 20);
    config.listenAddress = "127.0.0.1";
    DirectEndpoint loopback;
    loopback.address = {127, 0, 0, 1};
    loopback.port = config.localPort;
    config.manualEndpoints.push_back(loopback);
    std::puts("STAGE private room creation");
    HostRoom room(defaultTransportFactory(), PublisherBackends{});
    RoomStatus status;
    constexpr std::uint64_t unixNow = 1790000000;
    if (!require(room.open(config, unixNow, status) == RoomError::None && !status.code.empty(),
                 "private one-code room opens without router mapping")) return 1;
    ConnectionCode decoded;
    if (!require(decodeConnectionCode(status.code,decoded)==ConnectionCodeError::None &&
                 decoded.endpoints.size()==1 && decoded.endpoints[0].family==DirectEndpoint::Family::Ipv4 &&
                 decoded.endpoints[0].address==loopback.address && decoded.endpoints[0].port==loopback.port,
                 "probe room publishes only its explicit loopback endpoint")) return 1;
    auto settleJoin = [&](GuestJoin& join) {
        JoinProgress progress = JoinProgress::Connecting;
        const bool settled = until([&] {
            TransportEvent event;
            while (room.transport()->poll(event)) {}
            // Deliberately let reliable verdict and peer-close arrive together.
            // A loaded phone/simulator need not poll every two milliseconds.
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
            bool has = false;
            progress = join.poll(nowMs(), event, has);
        }, [&] {
            return progress == JoinProgress::Connected || progress == JoinProgress::Failed;
        }, GuestJoin::kAttemptTimeoutMs + 1000);
        std::printf("JOIN verdict: settled=%d progress=%d failure=%s mismatch=%s attempts=%zu rejected=%u\n",
            static_cast<int>(settled),static_cast<int>(progress),joinFailureString(join.failure()),
            compatibilityFieldString(join.incompatibility()),join.attemptedEndpoints(),room.transport()->rejectedPeers());
        return settled;
    };
    const CompatibilityField fields[] = {CompatibilityField::Content,CompatibilityField::Build,
        CompatibilityField::Region,CompatibilityField::Game,CompatibilityField::Capabilities};
    for (const auto field : fields) {
        GuestJoin mismatch;
        auto different = identity();
        switch (field) {
        case CompatibilityField::Content: different.content[0] ^= 1; break;
        case CompatibilityField::Build: different.build[0] ^= 1; break;
        case CompatibilityField::Region: different.region = 2; break;
        case CompatibilityField::Game: different.game = static_cast<std::uint8_t>(GameId::Pikmin2); break;
        case CompatibilityField::Capabilities: different.capabilities = 0; break;
        case CompatibilityField::None: return 1;
        }
        std::printf("STAGE private room mismatch %s\n",compatibilityFieldString(field));
        if (!require(mismatch.start(status.code,different,1,unixNow,nowMs())==JoinFailure::None &&
                     settleJoin(mismatch) && mismatch.failure()==JoinFailure::Incompatible &&
                     mismatch.incompatibility()==field && mismatch.host()!=nullptr &&
                     mismatch.attemptedEndpoints()==1 && room.transport()->state()==TransportState::Listening,
                     "delayed guest receives exact incompatibility; host remains available")) return 1;
    }
    if (!require(room.transport()->bannedOrigins()==0,"version/content differences never ban the partner")) return 1;
    {
        GuestJoin partner;
        if (!require(partner.start(status.code, identity(), 1, unixNow, nowMs()) == JoinFailure::None &&
                     settleJoin(partner) && partner.transport()->state() == TransportState::Connected,
                     "matching partner joins using the private room code")) return 1;
        partner.cancel();
    }
    {
        GuestJoin rejoin;
        if (!require(rejoin.start(status.code,identity(),1,unixNow,nowMs())==JoinFailure::None &&
                     settleJoin(rejoin) && rejoin.transport()->state()==TransportState::Connected,
                     "matching partner rejoins after leaving the same room")) return 1;
        rejoin.cancel();
    }
    room.close();
    std::puts("STAGE private room closed; leaving native probe");
    std::puts("NECTAR_COOP_SOCKET_PROBE_PASS");
    return 0;
}
