#pragma once
#include "nectar_net/replication.h"

namespace nectar::net {
// Initial visual/diagnostic state, NOT an exact-scene save or full AI snapshot.
// owner persists across working/idle states; leader is only the current engine
// association. Job mode is game-specific and doesn't encode its target/FSM yet.
struct PikminState {
    Vec3 position, velocity;
    float faceDirection = 0.0f, health = 0.0f;
    std::uint8_t owner = 255, leader = 255, color = 0, maturity = 0;
    std::uint16_t action = 0;
    // Host-sampled visual pose. Local display never executes animation events.
    std::uint16_t upperAnimation = 0, lowerAnimation = 0;
    float upperFrame = 0.0f, lowerFrame = 0.0f;
};
constexpr std::uint8_t kPikminSchema = 2;
constexpr std::size_t kPikminStateBytes = 50;
bool validPikminState(const PikminState& state);
std::vector<std::uint8_t> encodePikminState(const PikminState& state);
bool decodePikminState(const std::uint8_t* data, std::size_t size, PikminState& state);
// Only known Pikmin IDs may wrap the schema; no local key or pointer is written.
EntityRecord pikminRecord(std::uint64_t id, const PikminState& state);
} // namespace nectar::net
