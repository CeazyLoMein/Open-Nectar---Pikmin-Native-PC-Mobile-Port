#include "nectar_net/pikmin_replication.h"
#include "nectar_net/byte_io.h"
#include <cmath>
#include <cstring>

namespace nectar::net {
namespace {
bool within(float f, float bound) { return std::isfinite(f) && std::fabs(f) <= bound; }
bool player(std::uint8_t p) { return p < 2 || p == 255; }
std::uint32_t bits(float f) { std::uint32_t n = 0; std::memcpy(&n, &f, sizeof(n)); return n; }
float number(std::uint32_t n) { float f = 0; std::memcpy(&f, &n, sizeof(f)); return f; }
}
bool validPikminState(const PikminState& s)
{
    return within(s.position.x, kMaxWorldCoordinate) && within(s.position.y, kMaxWorldCoordinate)
        && within(s.position.z, kMaxWorldCoordinate) && within(s.velocity.x, kMaxSpeed)
        && within(s.velocity.y, kMaxSpeed) && within(s.velocity.z, kMaxSpeed)
        && within(s.faceDirection, 1000.0f) && within(s.health, 1000000.0f) && s.health >= 0
        && player(s.owner) && player(s.leader) && s.color < 5 && s.maturity < 3 && s.action < 256
        && s.upperAnimation < 1024 && s.lowerAnimation < 1024
        && within(s.upperFrame, 1000000.0f) && s.upperFrame >= 0
        && within(s.lowerFrame, 1000000.0f) && s.lowerFrame >= 0;
}
std::vector<std::uint8_t> encodePikminState(const PikminState& s)
{
    if (!validPikminState(s)) return {};
    ByteWriter w(kPikminStateBytes);
    for (const float f : {s.position.x, s.position.y, s.position.z, s.velocity.x, s.velocity.y,
                          s.velocity.z, s.faceDirection, s.health}) w.writeU32(bits(f));
    w.writeU8(s.owner); w.writeU8(s.leader); w.writeU8(s.color); w.writeU8(s.maturity); w.writeU16(s.action);
    w.writeU16(s.upperAnimation); w.writeU16(s.lowerAnimation);
    w.writeU32(bits(s.upperFrame)); w.writeU32(bits(s.lowerFrame));
    return w.ok() ? w.bytes() : std::vector<std::uint8_t>{};
}
bool decodePikminState(const std::uint8_t* data, std::size_t size, PikminState& state)
{
    if (!data || size != kPikminStateBytes) return false;
    ByteReader r(data, size);
    float f[8];
    for (float& value : f) { std::uint32_t n = 0; if (!r.readU32(n)) return false; value = number(n); }
    PikminState decoded;
    decoded.position = {f[0], f[1], f[2]}; decoded.velocity = {f[3], f[4], f[5]};
    decoded.faceDirection = f[6]; decoded.health = f[7];
    if (!r.readU8(decoded.owner) || !r.readU8(decoded.leader) || !r.readU8(decoded.color)
        || !r.readU8(decoded.maturity) || !r.readU16(decoded.action)
        || !r.readU16(decoded.upperAnimation) || !r.readU16(decoded.lowerAnimation)) return false;
    std::uint32_t upper = 0, lower = 0;
    if (!r.readU32(upper) || !r.readU32(lower)) return false;
    decoded.upperFrame = number(upper); decoded.lowerFrame = number(lower);
    if (!validPikminState(decoded)) return false;
    state = decoded;
    return true;
}
EntityRecord pikminRecord(std::uint64_t value, const PikminState& state)
{
    NetEntityId id;
    if (!NetEntityId::unpack(value, id) || id.kind != EntityKind::Pikmin) return {};
    auto data = encodePikminState(state);
    if (data.empty()) return {};
    return {value, kPikminSchema, std::move(data)};
}
} // namespace nectar::net
