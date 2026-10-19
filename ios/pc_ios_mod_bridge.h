#ifndef PC_IOS_MOD_BRIDGE_H
#define PC_IOS_MOD_BRIDGE_H
#include <cstddef>

// Called on the game thread. -1 = textures, 0..5 = HD Models menu rows.
// Capture the renderer's actual active texture selection, not a pending setting.
bool pc_ios_mod_import_open(int kind, const char* activeTexturePack);
// Completion is consumed on the game thread; UIKit and workers never touch UI state.
bool pc_ios_mod_import_poll(bool* ok, bool* cancelled, char* message, std::size_t size);

#endif
