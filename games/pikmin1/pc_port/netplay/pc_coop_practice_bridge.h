#pragma once
// UIKit-safe C++ boundary: no game/Dolphin/BOOL headers. All calls run on the
// owning game/UI thread. UI callbacks only queue intent; engine mutates at ticks.
#include <cstddef>
#include <memory>
namespace nectar { namespace net { class CoopConnection; } }
#if defined(NECTAR_COOP_WORLD) && NECTAR_COOP_WORLD
bool pc_coop_practice_can_enter();
bool pc_coop_practice_adopt(std::unique_ptr<nectar::net::CoopConnection>& owner);
bool pc_coop_practice_active();
bool pc_coop_practice_can_ready();
bool pc_coop_practice_ready();
void pc_coop_practice_pause();
void pc_coop_practice_leave();
void pc_coop_practice_background(bool away);
void pc_coop_practice_status(char* output, std::size_t capacity);

#else
inline bool pc_coop_practice_can_enter() { return false; }
inline bool pc_coop_practice_active() { return false; }
#endif
