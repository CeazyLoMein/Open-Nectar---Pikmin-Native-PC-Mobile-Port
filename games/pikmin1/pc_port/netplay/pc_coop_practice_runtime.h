#pragma once
#include "netplay/pc_coop_practice_bridge.h"
#include <cstdint>
class GameCoreSection;
struct PADStatus;
#if defined(NECTAR_COOP_WORLD) && NECTAR_COOP_WORLD
void pc_coop_practice_note_title(bool available);
bool pc_coop_practice_block_title();
void pc_coop_practice_tick_begin();
void pc_coop_practice_tick_end();
void pc_coop_practice_loaded(GameCoreSection& core);
bool pc_coop_practice_select_stage();
bool pc_coop_practice_guest_effects_running();
void pc_coop_practice_filter_pad(PADStatus* pads);
bool pc_coop_practice_control_yaw(int player, float* sine, float* cosine);
bool pc_coop_practice_remote_input(int player);
std::uint8_t pc_coop_practice_ext(int player);
std::int16_t pc_coop_practice_cursor_rotate(int player);
bool pc_coop_practice_cursor_delta(int player,float* x,float* y);
float pc_coop_practice_remote_speed(int player);
int pc_coop_practice_local_player();
bool pc_coop_practice_hud(int player,int& formation,int& total,int& nextType);

#else
inline void pc_coop_practice_note_title(bool) {}
inline bool pc_coop_practice_block_title() { return false; }
inline void pc_coop_practice_tick_begin() {}
inline void pc_coop_practice_tick_end() {}
inline void pc_coop_practice_loaded(GameCoreSection&) {}
inline bool pc_coop_practice_select_stage() { return false; }
inline bool pc_coop_practice_guest_effects_running() { return false; }
inline void pc_coop_practice_filter_pad(PADStatus*) {}
inline bool pc_coop_practice_control_yaw(int,float*,float*) { return false; }
inline bool pc_coop_practice_remote_input(int) { return false; }
inline std::uint8_t pc_coop_practice_ext(int) { return 0; }
inline std::int16_t pc_coop_practice_cursor_rotate(int) { return 0; }
inline bool pc_coop_practice_cursor_delta(int,float*,float*) { return false; }
inline float pc_coop_practice_remote_speed(int) { return 1.0f; }
inline int pc_coop_practice_local_player() { return 0; }
inline bool pc_coop_practice_hud(int,int&,int&,int&) { return false; }
#endif
