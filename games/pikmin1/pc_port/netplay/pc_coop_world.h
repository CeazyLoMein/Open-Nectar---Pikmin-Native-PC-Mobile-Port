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
// Guest visual bridge only. Must be explicitly entered AFTER an accepted scene
// loads TWO local presentation captains. Caller suppresses guest simulation.
// No scene boot, spawning, inputs, Piki/jobs, camera selection or saving here.
bool pc_coop_world_begin_guest(std::uint64_t sessionId, std::uint32_t sceneEpoch);
bool pc_coop_world_guest_active();
// Apply both captain transforms atomically, between ticks, from the current
// authenticated session's fully assembled frame. Session ID is trusted context
// supplied by the adapter (ActorFrame itself intentionally carries no session).
// Fails without changing either captain on stale epoch/frame, duplicate player,
// missing/recycled local actor, invalid values or changed bound host actor IDs.
bool pc_coop_world_apply_guest_captains(std::uint64_t sessionId, std::uint32_t sceneEpoch,
                                       const nectar::net::ActorFrame& frame);
// Explicit engine-created visual bindings. IDs come from an authenticated
// accepted baseline; LOCAL pointers never come from the network or ordering.
// Bind once after this scene loads. Every live local Pikmin must be included.
// This fixed-cohort step does not spawn/kill actors or reconstruct AI/jobs.
class Piki;
struct PcCoopGuestPikminBinding { std::uint64_t id; Piki* local; };
bool pc_coop_world_bind_guest_pikmin(std::uint64_t sessionId, std::uint32_t sceneEpoch,
    const std::vector<PcCoopGuestPikminBinding>& bindings);
// Atomic captain+Pikmin transform/health/maturity/leader apply. Reject the
// ENTIRE frame if population/identity/lifetime/type/values don't match.
// Caller must suppress autonomous guest simulation. Color conversion, births,
// deaths, animation and enemy/item/Onion/job adapters remain separate work.
// Never mix captain-only apply after a cohort has been bound.
bool pc_coop_world_apply_guest_actors(std::uint64_t sessionId, std::uint32_t sceneEpoch,
    const nectar::net::ActorFrame& frame);
// Last applied host ownership/action metadata; does NOT change guest AI/FSM.
bool pc_coop_world_guest_pikmin_state(std::uint64_t id, nectar::net::PikminState& output);

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
