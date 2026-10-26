#pragma once
// Where the emulated memory card keeps a channel's files on disk (the
// folder holding "Pikmin dataFile" and its ".meta_" record). Online sessions
// copy the host's card to the guest so both games load the same save.
#include <string>

std::string pc_card_channel_dir(int channel);

#include <mutex>
// Serializes complete card/history I/O against explicit practice admission.
// Recursive because CARDCreate/async wrappers call other CARD entry points.
std::recursive_mutex& pc_card_io_mutex();
// Call only after normal card initialization, at a title/session-start boundary.
// The driver must stop new engine save requests and drain CardUtil BEFORE scene
// teardown: this lock serializes filesystem I/O, not engine-buffer lifetimes.
// Creates a NEW child of an existing absolute scratch directory (OS temp by
// default), refusing overlap with the real save root. No copy/import of saves.
// Process-latched: there is deliberately NO return-to-real-card API. Restart
// the app after the first practice test, so delayed worker jobs cannot cross
// back into real saves. False leaves normal routing intact; never fall back to
// a real card if practice admission fails. Already-active admission is refused.
bool pc_card_begin_coop_practice(const char* scratchDirectory = nullptr);
bool pc_card_coop_practice_active();
