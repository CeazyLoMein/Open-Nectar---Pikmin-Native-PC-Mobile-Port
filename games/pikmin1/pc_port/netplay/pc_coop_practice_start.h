#pragma once

struct MemoryCard;
enum class PcCoopPracticeStart { Idle, Draining, Armed, Loading, Failed, RestartRequired };
// Internal game-thread bridge. The room driver must have an accepted peer,
// pump it through loading, and cancel here on disconnect BEFORE admission.
// This does not enable UI, negotiate a scene or claim a complete guest world.
bool pc_coop_practice_request_start(const char* scratchDirectory = nullptr);
PcCoopPracticeStart pc_coop_practice_poll_start();
PcCoopPracticeStart pc_coop_practice_start_state();
bool pc_coop_practice_cancel_start();
bool pc_coop_practice_prepare_setup(MemoryCard& card);
// Once an isolated run has begun or an admitted start is aborted, app restart
// is required. Never show ordinary solo choices using the temporary card.
bool pc_coop_practice_restart_required();
