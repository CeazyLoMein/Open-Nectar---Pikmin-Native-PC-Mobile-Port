#pragma once
#if NECTAR_P1_SOLO_TEST
// Same tutorial flags as the normal skip path. The synthetic test file already
// owns the engine: leaving these unset plays the engine movie for OTHER parts.
// Also repair old Build33 test cards on stage entry, without resetting progress.
template<class State>
inline bool pc_solo_test_repair_tutorial(State& state) {
    if (state.isTutorial() || !state.hasUfoParts(UFOID_MainEngine)) return false;
    const int flags[] = { DEMOFLAG_DiscoverRedOnyon, DEMOFLAG_ApproachSeed,
        DEMOFLAG_PluckRedPikmin, DEMOFLAG_NoPikminTimeout, DEMOFLAG_CameraInfo,
        DEMOFLAG_Unk9, DEMOFLAG_CollectFirstPellet, DEMOFLAG_ApproachEngine,
        DEMOFLAG_CollectEngine, DEMOFLAG_StartBoxPush, DEMOFLAG_FinishBoxPush,
        DEMOFLAG_Pluck15thPikmin };
    bool changed = false;
    for (int flag : flags) {
        if (!state.mDemoFlags.isFlag(flag)) {
            state.mDemoFlags.setFlagOnly(flag);
            changed = true;
        }
    }
    return changed;
}
#endif
