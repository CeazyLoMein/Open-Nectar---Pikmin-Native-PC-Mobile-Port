#pragma once
#include "nectar_net/actor_frame.h"
#include "nectar_net/byte_io.h"
#include <cmath>
#include <cstring>

namespace nectar::net
{
// Presentation cues only. Opaque emitter tokens are never addresses or asset paths.
enum class AudioKind : std::uint8_t
{
    Reset,
    SpatialPlay,
    SpatialStop,
    SpatialMove,
    SpatialRelease,
    PlayerPlay,
    PlayerStop,
    SystemPlay,
    SystemStop,
    Formation,
    Footstep
};
struct AudioCue
{
    AudioKind kind = AudioKind::Reset;
    std::uint32_t emitter = 0;
    std::uint16_t sound = 0;
    std::uint8_t type = 0, player = 255;
    bool loop = false;
    Vec3 position;
    std::int8_t x = 0, y = 0;
};
constexpr std::size_t kAudioBatchCues = 24, kAudioQueueCues = 256, kAudioCueBytes = 24;
inline bool validAudioCue(const AudioCue &c)
{
    if (static_cast<unsigned>(c.kind) > static_cast<unsigned>(AudioKind::Footstep) ||
        (c.player > 1 && c.player != 255) || c.x == -128 || c.y == -128)
        return false;
    for (float v : {c.position.x, c.position.y, c.position.z})
        if (!std::isfinite(v) || std::fabs(v) > kMaxWorldCoordinate)
            return false;
    const bool spatial = c.kind >= AudioKind::SpatialPlay && c.kind <= AudioKind::SpatialRelease;
    if (spatial)
        return c.emitter && c.type >= 1 && c.type <= 8 && c.sound <= 511 && c.player == 255 && !c.x && !c.y;
    if (c.emitter || c.type || c.position.x || c.position.y || c.position.z)
        return false;
    if (c.kind == AudioKind::PlayerPlay || c.kind == AudioKind::PlayerStop)
        return (c.sound <= 255 || (c.sound >= 0x8000 && c.sound <= 0x80ff)) && !c.x && !c.y && !c.loop;
    if (c.kind == AudioKind::SystemPlay || c.kind == AudioKind::SystemStop || c.kind == AudioKind::Footstep)
        return c.sound <= 255 && !c.x && !c.y && !c.loop;
    if (c.kind == AudioKind::Formation)
        return !c.sound && !c.loop;
    return !c.sound && !c.loop && !c.x && !c.y && c.player == 255;
}
inline std::vector<std::uint8_t> encodeAudio(const std::vector<AudioCue> &cues)
{
    if (cues.empty() || cues.size() > kAudioBatchCues)
        return {};
    ByteWriter w(1 + kAudioBatchCues * kAudioCueBytes);
    w.writeU8(static_cast<std::uint8_t>(cues.size()));
    for (const auto &c : cues)
    {
        if (!validAudioCue(c))
            return {};
        w.writeU8(static_cast<std::uint8_t>(c.kind));
        w.writeU32(c.emitter);
        w.writeU16(c.sound);
        w.writeU8(c.type);
        w.writeU8(c.player);
        w.writeU8(c.loop ? 1 : 0);
        for (float v : {c.position.x, c.position.y, c.position.z})
        {
            std::uint32_t bits;
            std::memcpy(&bits, &v, 4);
            w.writeU32(bits);
        }
        w.writeU8(static_cast<std::uint8_t>(c.x));
        w.writeU8(static_cast<std::uint8_t>(c.y));
    }
    return w.ok() ? w.bytes() : std::vector<std::uint8_t>{};
}
inline bool decodeAudio(const std::uint8_t *bytes, std::size_t size, std::vector<AudioCue> &out)
{
    if (!bytes || size < 1 || size > 1 + kAudioBatchCues * kAudioCueBytes)
        return false;
    ByteReader r(bytes, size);
    std::uint8_t count = 0;
    if (!r.readU8(count) || !count || count > kAudioBatchCues || r.remaining() != count * kAudioCueBytes)
        return false;
    std::vector<AudioCue> decoded;
    decoded.reserve(count);
    for (unsigned i = 0; i < count; ++i)
    {
        AudioCue c;
        std::uint8_t kind = 0, loop = 0, x = 0, y = 0;
        if (!r.readU8(kind) || !r.readU32(c.emitter) || !r.readU16(c.sound) || !r.readU8(c.type) ||
            !r.readU8(c.player) || !r.readU8(loop) || loop > 1)
            return false;
        c.kind = static_cast<AudioKind>(kind);
        c.loop = loop != 0;
        for (float *v : {&c.position.x, &c.position.y, &c.position.z})
        {
            std::uint32_t bits;
            if (!r.readU32(bits))
                return false;
            std::memcpy(v, &bits, 4);
        }
        if (!r.readU8(x) || !r.readU8(y))
            return false;
        c.x = static_cast<std::int8_t>(x);
        c.y = static_cast<std::int8_t>(y);
        if (!validAudioCue(c))
            return false;
        decoded.push_back(c);
    }
    out = std::move(decoded);
    return true;
}
} // namespace nectar::net
