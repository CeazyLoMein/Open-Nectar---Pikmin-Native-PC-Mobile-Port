#pragma once
// Minimal legacy-engine hooks. All compile away without the prototype option.
#if defined(PIKI_PC_PORT) && defined(NECTAR_COOP_WORLD) && NECTAR_COOP_WORLD
void pc_coop_world_forget(const void* actor);
void pc_coop_world_end_scene();
#else
inline void pc_coop_world_forget(const void*) {}
inline void pc_coop_world_end_scene() {}
#endif
