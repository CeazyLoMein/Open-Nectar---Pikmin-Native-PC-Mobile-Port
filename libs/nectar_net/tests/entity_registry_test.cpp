#include "nectar_net/entity_registry.h"
#include <cstdio>
using namespace nectar::net;
int bad = 0;
void check(bool ok, const char* what) { if (!ok) { std::printf("FAIL %s\n", what); ++bad; } }
int main()
{
    HostEntityRegistry r;
    check(!r.observe(EntityKind::Pikmin, 1), "inactive cannot allocate");
    check(!r.beginScene(0) && r.beginScene(1), "valid scene starts");
    const auto a = r.observe(EntityKind::Pikmin, 0x1000, 0);
    const auto b = r.observe(EntityKind::Captain, 0x2000, 1);
    check(a && b && a != b && r.size() == 2, "distinct valid identities");
    check(r.observe(EntityKind::Pikmin, 0x1000, 1) == a && r.owner(a) == 0, "repeat observation retains identity and ownership");
    check(!r.observe(EntityKind::Enemy, 0x1000), "kind alias refused");
    check(!r.localForId(a, EntityKind::Captain) && r.localForId(a, EntityKind::Pikmin) == 0x1000, "typed resolution");
    check(!r.beginScene(1) && !r.beginScene(0) && !r.beginScene(65536) && r.size() == 2, "stale/wrapped epochs preserve bindings");
    check(r.retireLocal(0x1000) == a && !r.localForId(a, EntityKind::Pikmin), "retire removes reverse resolution");
    const auto replacement = r.observe(EntityKind::Pikmin, 0x1000, 1);
    check(replacement && replacement != a && !r.localForId(a, EntityKind::Pikmin), "pooled address reuse never revives stale ID");
    check(r.setOwner(replacement, 0) && r.owner(replacement) == 0 && !r.setOwner(replacement, 2), "host ownership validation");
    check(!r.setOwner(a, 1) && !r.observe(EntityKind::Pikmin, 0) && !r.observe(EntityKind::Other, 9, 2), "unknown/null/invalid owner refused");
    r.endScene(); check(!r.size() && !r.localForId(b, EntityKind::Captain) && !r.beginScene(1), "end clears bindings but keeps epoch guard");
    check(r.beginScene(2), "next scene starts");
    const auto next = r.observe(EntityKind::Pikmin, 0x1000);
    check(next != a && next != replacement, "new scene cannot alias previous IDs");
    HostEntityRegistry capped({1, 2}); check(capped.beginScene(1), "bounded registry");
    const auto first = capped.observe(EntityKind::Pikmin, 1);
    check(first && !capped.observe(EntityKind::Pikmin, 2), "live capacity enforced");
    capped.retireLocal(1);check(capped.observe(EntityKind::Pikmin, 2) != 0, "new lifetime uses next ID");
    capped.retireLocal(2);check(!capped.observe(EntityKind::Pikmin, 1), "issued budget refuses reuse/wrap");
    HostEntityRegistry soak;
    check(soak.beginScene(1), "soak scene");
    std::uint64_t previous = 0;
    for (int i = 0; i < 20000; ++i) {
        const auto id = soak.observe(EntityKind::Pikmin, 42, static_cast<std::uint8_t>(i % 2));
        check(id && id != previous && !soak.localForId(previous, EntityKind::Pikmin), "20000 pooled lifetimes reject previous identity");
        previous = soak.retireLocal(42);
    }
    if (!bad) std::puts("PASS host registry: typed IDs, ownership, scene lifetime, bounds and20000 recycled actors");
    return bad ? 1 : 0;
}
