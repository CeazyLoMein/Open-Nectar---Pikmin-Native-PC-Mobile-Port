#pragma once
#include "netplay/pc_coop_world_hooks.h"
#include "nectar_net/world.h"
#include "nectar_net/actor_frame.h"
#include <cstdint>
#include <vector>

// Read-only host capture prototype. Main simulation thread, BETWEEN ticks only.
// No input, actor spawning, save writing, network sockets or mode activation UI.
// Caller owns the session ID/scene barrier; session IDs must never be reused.
bool pc_coop_world_begin_host(std::uint64_t sessionId, std::uint32_t sceneEpoch);
bool pc_coop_world_active();
// Complete current captain/Pikmin record list for a future keyframe. Failed
// capture leaves output intact; do NOT transmit old output when false is returned.
// Does not yet include jobs' targets, enemies, items, Onions or campaign state.
bool pc_coop_world_capture(std::vector<nectar::net::EntityRecord>& output);
std::uint64_t pc_coop_world_actor_id(const void* actor, nectar::net::EntityKind kind);
bool pc_coop_world_set_owner(std::uint64_t pikminId, std::uint8_t owner);

// Capture and packetize one complete frame, without enabling any networking.
// Failure leaves output intact; never send it when false. Caller supplies a
// strictly increasing frame number and authoritative simulation tick.
bool pc_coop_world_capture_packets(std::uint64_t frame, std::uint64_t tick,
    std::size_t maxPacketBytes, std::vector<std::vector<std::uint8_t>>& packets);
