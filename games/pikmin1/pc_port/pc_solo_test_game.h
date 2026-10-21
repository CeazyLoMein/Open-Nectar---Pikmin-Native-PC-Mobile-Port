#pragma once
#if NECTAR_P1_SOLO_TEST
#include "pc_solo_test_log.h"
#include "pc_solo_test_tutorial.h"
// Call ONLY from the fresh-file path, after ordinary new-game initialization.
// Do not call on load, stage entry or day transitions: no inventory refills.
inline void pc_solo_test_prepare_new_campaign(PlayerState& state, PikiInfMgr& bank, int slot) {
    if (state.mTotalParts != UFO_COUNT || !state.mUfoParts) return;
#if NECTAR_P1_SOLO_UPDATE
    // Every update slot uses the familiar-area fixture; no accidental finale.
    const bool finale = false;
#else
    const bool finale = slot == 1;
#endif
    for (int i=0; i<UFO_COUNT; ++i)
        state.mUfoParts[i].mPartVisType = (finale ? i != UFO_SecretSafe : i == UFO_MainEngine)
            ? (finale ? PARTVIS_Visible : PARTVIS_Invisible) : PARTVIS_Uncollected;
    state.mCurrParts = finale ? 29 : 1;
    state.mRequiredUfoPartCount = finale ? 25 : 1;
    state.mShipUpgradeLevel = finale ? 4 : 1;
    state.mShipEffectPartFlag = finale ? 7 : 0;
    state.mIsTutorialMode = false;
    for (int i=0; i<STAGE_COUNT; ++i) state.mStagePartsCollected[i]=0;
    state.mStagePartsCollected[STAGE_Practice] = finale ? 2 : 1;
    if (finale) {
        state.mStagePartsCollected[STAGE_Forest]=8;
        state.mStagePartsCollected[STAGE_Cave]=9;
        state.mStagePartsCollected[STAGE_Yakushima]=10;
    }
    for (int color=0; color<PikiColorCount; ++color) {
        state.setContainer(color);
        state.setBootContainer(color);
        state.setDisplayPikiCount(color);
        for (int leaf=0; leaf<PikiHappaCount; ++leaf)
            bank.mPikiCounts[color][leaf] = leaf == Leaf ? 100 : 0;
    }
    state.mLivingPikiNum=300;
    state.mTotalBornPikiNum=300;
    state.mTotalPluckedPikiCount=300;
    state.mPartsCollectedByDay[0]=state.mCurrParts;
    pc_solo_test_repair_tutorial(state);
    // Setup is explicitly logged, never counted as collected-in-game evidence.
    pc_solo_test::record("preset_new_file_slot_parts", slot, state.mCurrParts, 100, 100);
}
// Unlock in the disposable campaign state, not in the user's settings file.
template<class PlayStateType>
inline void pc_solo_test_unlock_areas(PlayStateType& play) {
#if NECTAR_P1_SOLO_UPDATE
    const int end=STAGE_Last; // finale deferred for this user's test
#else
    const int end=STAGE_COUNT;
#endif
    for(int stage=STAGE_START;stage<end;++stage) play.openStage(stage);
}
#endif
