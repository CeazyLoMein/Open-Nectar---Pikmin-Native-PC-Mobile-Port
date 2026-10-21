#pragma once
#include "pikmin1_ios_profile.h"
namespace nectar_ios {
// Apply only to a fresh, isolated test config. An existing test config remains
// byte-for-byte unchanged, so chosen graphics/mods and later test settings survive.
inline ProfileResult apply_pikmin1_solo_test_profile(const std::string& original) {
    if (!original.empty()) return {original, false};
    auto profile = apply_pikmin1_enhanced_profile(original);
    profile.text += "# Disposable P1 Solo Test defaults\n"
                    "unlockZones = 1\nallOnions = 1\nfpsMode = 1\niosPerformanceHud = 1\n";
    profile.changed = true;
    return profile;
}
}
