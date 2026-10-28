#include "nectar_net/onion_authority.h"
#include <cstdio>
#include <limits>

namespace {
using namespace nectar::net;
using A = OnionAuthority;
int failures = 0;
void check(bool ok, const char* message) { if (!ok) { std::printf("FAIL: %s\n", message); ++failures; } }
std::uint64_t id(std::uint32_t counter, std::uint16_t epoch = 1, EntityKind kind = EntityKind::Pikmin)
{ return NetEntityId{epoch, kind, 0, counter}.pack(); }
A::Command command(std::uint8_t player, std::uint64_t sequence, A::Operation operation,
                   std::uint32_t first, std::uint32_t count, std::uint8_t color = 0)
{
    A::Command c; c.sceneEpoch = 1; c.player = player; c.sequence = sequence; c.operation = operation; c.color = color;
    for (std::uint32_t n = 0; n < count; ++n) c.entities.push_back(id(first + n));
    return c;
}
void sharedStock()
{
    A a(1, 3, {200, 50, 10, 0, 0}, {30, 30});
    auto raye = command(1, 1, A::Operation::Withdraw, 1, 20);
    check(a.apply(1, raye).status == A::Status::Applied && a.stored(0) == 180, "Raye withdraws 20 from shared 200");
    auto host = command(0, 1, A::Operation::Withdraw, 21, 30);
    check(a.apply(0, host).status == A::Status::Applied && a.stored(0) == 150, "host sees 180, withdraws own 30");
    check(a.fieldCount(0) == 30 && a.fieldCount(1) == 20, "independent per-player allowances");
    check(a.apply(1, command(1, 2, A::Operation::Withdraw, 51, 10)).status == A::Status::Applied,
          "Raye can reach her own 30 while host already has 30");
    check(a.apply(0, command(0, 2, A::Operation::Withdraw, 61, 1)).status == A::Status::PlayerLimit,
          "workers/idle/following stay counted, cannot bypass allowance");
    const auto revision = a.revision();
    auto reply = a.apply(1, command(1, 3, A::Operation::Store, 1, 20));
    check(reply.status == A::Status::Applied && a.stored(0) == 160 && a.fieldCount(1) == 10, "store returns exact owned Pikmin");
    check(a.apply(1, command(1, 3, A::Operation::Store, 1, 20)).revision == reply.revision
          && a.apply(1, command(1, 3, A::Operation::Store, 1, 20)).replayed
          && !reply.replayed && a.revision() == revision + 1 && a.stored(0) == 160, "lost acknowledgement/retry never stores twice");
}
void validation()
{
    A a(1, 3, {2, 0, 0, 0, 0}, {30, 30});
    auto c = command(0, 1, A::Operation::Withdraw, 1, 2);
    auto forged = c; forged.player = 1;
    check(a.apply(0, forged).status == A::Status::WrongPlayer, "packet cannot impersonate partner");
    auto wrongScene = c; wrongScene.sceneEpoch = 2;
    check(a.apply(0, wrongScene).status == A::Status::InvalidSession, "old scene command refused");
    auto skipped = c; skipped.sequence = 2;
    check(a.apply(0, skipped).status == A::Status::OutOfOrder && a.stored(0) == 2, "reordered command requires resend");
    auto dup = c; dup.entities[1] = dup.entities[0];
    check(a.apply(0, dup).status == A::Status::InvalidEntity && a.stored(0) == 2 && a.field().empty(), "duplicate IDs fail atomically");
    check(a.apply(0, c).status == A::Status::ReusedSequence, "same sequence cannot be rewritten");
    c.sequence = 2;
    check(a.apply(0, c).status == A::Status::Applied, "fresh command withdraws once");
    check(a.apply(0, c).status == A::Status::Applied && a.apply(0, c).replayed && a.stored(0) == 0, "duplicate withdrawal is idempotent");
    auto stolen = command(1, 1, A::Operation::Store, 1, 2);
    check(a.apply(1, stolen).status == A::Status::InvalidEntity && a.fieldCount(0) == 2, "partner cannot return another squad");
    auto mixed = command(0, 3, A::Operation::Store, 1, 2); mixed.entities[1] = id(999);
    check(a.apply(0, mixed).status == A::Status::InvalidEntity && a.fieldCount(0) == 2, "partially invalid return changes nothing");
    check(a.retire(id(1)) && !a.retire(id(1)) && a.fieldCount(0) == 1 && a.stored(0) == 0, "death releases allowance, not stock");
    auto oldEntity = command(1, 2, A::Operation::Withdraw, 5, 1); oldEntity.entities[0] = id(5, 2);
    check(a.apply(1, oldEntity).status == A::Status::InvalidEntity, "wrong-scene entity refused");
    oldEntity.sequence = 3; oldEntity.entities[0] = id(5, 1, EntityKind::Enemy);
    check(a.apply(1, oldEntity).status == A::Status::InvalidEntity, "non-Pikmin ID refused");
    check(a.apply(0, c).status == A::Status::OutOfOrder, "older-than-cache request cannot replay");
    check(a.apply(1, stolen).status == A::Status::OutOfOrder, "stale return cannot replay");
    auto zero = command(1, 0, A::Operation::Withdraw, 100, 1);
    check(a.apply(1, zero).status == A::Status::OutOfOrder, "zero sequence refused");
    auto huge = command(1, 4, A::Operation::Withdraw, 100, 1001);
    check(a.apply(1, huge).status == A::Status::InvalidCommand, "oversized request bounded");
    auto insufficient = command(1, 4, A::Operation::Withdraw, 100, 1);
    check(a.apply(1, insufficient).status == A::Status::InsufficientStock, "empty Onion refused");
    check(!A(0, 3, {10, 0, 0, 0, 0}, {30, 30}).valid(), "zero scene epoch cannot create campaign authority");
    check(!A(1, 3, {0, 0, 0, 1, 0}, {30, 30}).valid(), "P1 cannot initialize inaccessible color stock");
    check(!A(1, 3, {}, {0, 30}).valid(), "invalid allowance refused");
    A overflow(1, 3, {std::numeric_limits<std::uint32_t>::max(), 0, 0, 0, 0}, {30, 30});
    check(overflow.apply(0, command(0, 1, A::Operation::Withdraw, 1, 1)).status == A::Status::Applied,
          "large valid stock withdraws without overflow");
    check(overflow.apply(0, command(0, 2, A::Operation::Store, 1, 1)).status == A::Status::Applied
          && overflow.stored(0) == std::numeric_limits<std::uint32_t>::max(), "return preserves maximum balance");
}
void soak()
{
    A a(1, 5, {200, 200, 200, 200, 200}, {30, 30});
    std::uint32_t counter = 1;
    std::uint64_t seq[2] = {0, 0};
    for (int round = 0; round < 10000; ++round) {
        const auto p = static_cast<std::uint8_t>(round % 2);
        const auto color = static_cast<std::uint8_t>(round % 5);
        const auto n = static_cast<std::uint32_t>(1 + round % 30);
        auto c = command(p, ++seq[p], A::Operation::Withdraw, counter, n, color);
        check(a.apply(p, c).status == A::Status::Applied, "soak withdraw");
        check(a.apply(p, c).status == A::Status::Applied, "soak retry");
        c.sequence = ++seq[p]; c.operation = A::Operation::Store;
        check(a.apply(p, c).status == A::Status::Applied, "soak store");
        check(a.apply(p, c).status == A::Status::Applied, "soak store retry");
        counter += n;
        check(a.field().empty() && a.fieldCount(0) == 0 && a.fieldCount(1) == 0 && a.stored(color) == 200,
              "stock and ownership conserved through 40000 command deliveries");
    }
}
}
int main()
{
    sharedStock(); validation(); soak();
    if (!failures) std::puts("PASS host Onion authority: shared stock, independent quotas, atomic commands, retry safety, 10000 cycles");
    return failures ? 1 : 0;
}
