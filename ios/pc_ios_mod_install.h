#ifndef PC_IOS_MOD_INSTALL_H
#define PC_IOS_MOD_INSTALL_H

// Portable filesystem transaction; no SDL, renderer or configuration access.
// kind: -1 texture ZIP, 0..5 model ZIP (same order as the HD Models menu).
// loadRoot: game's writable Load folder. activeTexturePack: selected folder,
// "*" when every existing pack is indexed, or "" when no texture pack is active.
// Calls must be serialized. The caller must also keep the active selection
// stable until this finishes. Returns imported file count, or zero on failure.
// Existing model siblings are merged, so Bulborb and Dwarf Bulborb coexist.
// Replaced folders remain in Load/.ios-import/<transaction>/previous/.
// Restart is required to apply imports; this never activates a pack.
int pc_ios_mod_install(const char* source, int kind, const char* loadRoot,
                       const char* activeTexturePack, char* message,
                       unsigned long messageSize);

#endif
