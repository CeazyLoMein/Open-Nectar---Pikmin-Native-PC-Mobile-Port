#pragma once
// Minimal legacy-engine hooks. All compile away without the prototype option.
#if defined(PIKI_PC_PORT) && defined(NECTAR_COOP_WORLD) && NECTAR_COOP_WORLD
void pc_coop_world_forget(const void* actor);
void pc_coop_world_end_scene();
// Game thread only. Ordinary play advances normally; an explicitly admitted
// guest NEVER simulates, even after its bindings become invalid. An admitted
// host starts held until the session driver grants advancement after readiness.
bool pc_coop_world_may_advance();
bool pc_coop_world_has_guest();
class Graphics;
// True means a dedicated guest population owns this draw, including an empty
// or invalidated population. Never fall back to drawing stale local actors.
bool pc_coop_world_draw_guest_pikmin(Graphics&);
#else
inline void pc_coop_world_forget(const void*) {}
inline void pc_coop_world_end_scene() {}
inline bool pc_coop_world_may_advance() { return true; }
inline bool pc_coop_world_has_guest() { return false; }
class Graphics;
inline bool pc_coop_world_draw_guest_pikmin(Graphics&) { return false; }
#endif
