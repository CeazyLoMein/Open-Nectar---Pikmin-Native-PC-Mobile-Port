#pragma once
#include "nectar_net/replication.h"
namespace nectar::net {
// First encounter adapter deliberately admits only the original Dwarf Bulborb.
// Visual samples are not enemy AI, corpse/carry state or a durable scene save.
constexpr std::uint8_t kPracticeEnemyType = 3;
constexpr std::uint8_t kEnemySchema = 3;
constexpr std::size_t kEnemyStateBytes = 60;
struct EnemyState {
    Vec3 position, velocity, scale{1,1,1};
    float faceDirection=0, health=0, tilt=0, animationFrame=0, maxHealth=1;
    std::uint16_t animation=0;
    std::uint8_t type=kPracticeEnemyType, visible=1;
};
bool validEnemyState(const EnemyState& state);
std::vector<std::uint8_t> encodeEnemyState(const EnemyState& state);
bool decodeEnemyState(const std::uint8_t* data,std::size_t size,EnemyState& state);
EntityRecord enemyRecord(std::uint64_t id,const EnemyState& state);
} // namespace nectar::net
