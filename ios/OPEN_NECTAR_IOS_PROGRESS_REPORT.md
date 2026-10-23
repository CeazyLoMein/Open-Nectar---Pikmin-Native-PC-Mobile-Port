# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-23 13:10 Eastern Daylight Time

**Overall project status:** Build46 FAILED in the shared simulator startup gate while compiling SDL CoreAudio: two undeclared UIScene notification constants, one missing owning header. Both game builds were SKIPPED; simulator launch did not run and no game IPA was produced. Header correction IMPLEMENTED;24 local dependency/metadata/wiring checks PASS. Build47/run39992850789, source2034e139369df84f61fd499d0d085b4e567b1d78, startup job120548733186: dispatched, no result yet. P1 Build44 remains a confirmed phone launch failure; P2 Build45 compiled successfully but remains on installation HOLD. Landscape only; FPS player-controlled including120.

### Pikmin 1

- Current objective: Restore launch before testing adaptive display and120 FPS options; preserve original app/settings/assets/saves.
- What was investigated: Complete Build46 job120542742441 log and artifact12517803044; exactly two compiler errors at SDL_coreaudio.m:494 and504. Traced actual includes through SDL_coreaudio.h: it imports UIApplication.h, which does not declare UISceneDidActivateNotification or UISceneWillEnterForegroundNotification. Audited other scene-notification users: UIKit appdelegate and optional iOS HID already import full UIKit.h.
- Root cause or leading hypothesis: Build46 compile cause CONFIRMED: missing UIScene header in CoreAudio. Separate P1 Build44 phone crash CONFIRMED from3 matching-UUID reports: UIKit traps at ___UIApplicationEvaluateRuntimeIssueForNoSceneLifecycleAdoption_block_invoke before game entry. Shared scene migration addresses that omission but has not yet passed Apple compilation/runtime.
- Files changed: games/pikmin1/third_party/SDL2-android/src/audio/coreaudio/SDL_coreaudio.h adds UIKit/UIScene.h only inside the existing iOS branch and NECTAR_IOS_SCENES/non-tvOS guard. tests/ios_scene_contract_test.py adds owning-header dependency/negative checks and audits other notification imports. Journals updated. No gameplay, framebuffer, DSP, save, navigation, aiming or FPS algorithm changes in this correction.
- Tests and results:24 local scene metadata/dependency/wiring checks PASS, including rejection after removing the new import; Python syntax and git diff formatting PASS. Artifact ZIP digest verified and all entries CRC-tested. Build46 native gate FAIL; runtime NOT RUN; games SKIPPED. Native correction, simulator runtime, fresh game builds/IPAs and phone results PENDING. Windows host checks are not UIKit compilation proof.
- Confirmed working: Earlier P1 user hardware baseline only. Build44 installed but launch FAILED; withdrawn file marked .ipa.DO-NOT-INSTALL and archived. Pre-SDK42 backup retained unchanged, SHA256304ac9abd4c60d96d76eb95902a0716ab743a074b1c69003aad238f7f7efd6a1. No claim that42 following/teleport is hardware-verified.
- Remaining issues: Get shared scene gate and native game build passing, then launch/graphics/touch/background-resume/audio/settings/FPS/display checks. Prior normal-follow pacing, genuine stuck-only teleport (explicitly UNTESTED), idle ship Recall All, rare clam scene and full campaign remain open.

### Pikmin 2

- Current objective: Preserve successful Build45 const-return correction and working installed Build32 while resolving shared startup before an update.
- What was investigated: Build46 dependency blocked P2 too; no new P2 compiler result. Previous45 full native job120429205992, artifact12504090493 and exact IPA verified; its SDK27.1 package lacks scene manifest.
- Root cause or leading hypothesis: P2's earlier JSGGetName override return mismatch was resolved by45. P2 shares SDL2 startup omission proved in P1, so45 installation remains HOLD; a P245 phone crash is inferred risk, not observed runtime evidence.
- Files changed: Shared CoreAudio header correction only; prior P2 ObjectSystem.h and JSTObjectSystem.cpp char const* correction retained. No P2 game/audio DSP edits.
- Tests and results:45/run39958190774/source dd5683cec866d7f96f6fe5dcc2321b2d8426a088 native compile/link/IPA PASS. Held IPA4,157,515bytes SHA256c1cc05b8b0b8265acc6786b9c8b241cd8832e4a3f9125c7aa09d670282f337e1.46 game build SKIPPED; corrected shared native/runtime/new IPA/phone PENDING.
- Confirmed working: User-confirmed installed Build32 audio/gameplay baseline preserved;45 compiler correction only, not new hardware success.
- Remaining issues: Shared gate, new native/IPA, then launch/input/menus/Pikmin-enemy-wind audio/background-resume and full-campaign testing.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; local C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental, verified clean and fetched before edits; local/remote matched f1ef80dccd541967995ae0772e6bd6272aaa632f, no incoming changes.
- Starting commit: f1ef80dccd541967995ae0772e6bd6272aaa632f. Build46 source0f61ee4163ea4b47f668f50ed1f1e3511149b3bd.
- Latest source/local/remote checkpoint: 2034e139369df84f61fd499d0d085b4e567b1d78. A follow-up [skip ci] journal commit may be newer; use git log and origin/ios-experimental for that exact SHA. External checkpoint records final journal SHA after push.
- Commits created: Scoped CoreAudio header/dependency-regression/journal correction; source SHA above if dispatched, otherwise pending commit.
- Changes pushed: Build47/run39992850789, source2034e139369df84f61fd499d0d085b4e567b1d78, startup job120548733186: dispatched, no result yet. One combined run; both game jobs remain gated on actual simulator launch/resume. No bypass or duplicate build.
- Uncommitted changes: Before source commit, only scoped header/test/journals; after dispatch, journal-only until its [skip ci] commit. No assets/private phone reports/credentials staged; final state recorded externally after journal push.
- GitHub Actions run IDs:44=39950748289 P1 native PASS/P2 compile FAIL;45=39958190774 P2 SUCCESS but HOLD.46=39991097065 startup job120542742441 FAIL, downstream build job120545456816 SKIPPED. Build47/run39992850789, source2034e139369df84f61fd499d0d085b4e567b1d78, startup job120548733186: dispatched, no result yet.
- Build results:46 two compile errors/one missing-header cause, no runtime/game build. Correction local24 PASS; Apple compilation/runtime/IPA/phone pending. Earlier20 contract checks missed header ownership; added explicit dependency negative control, retained real native gate.
- Artifacts produced:46 diagnostic artifact12517803044 (ios-scene-build.log only), ZIP SHA2566710fccadf47fccf23b7a6eb76c9d2bd73597f0b3d0a408aa430d42878165602; no game IPA.45 P2 IPA held privately under outputs/Build45-Pikmin2, NOT ready to install. Bad P144 archived; old42 backup retained.

### Next steps

- Next Pikmin 1 task: Inspect corrected shared gate first, then native game/IPA; stage verified original-ID update and test launch FIRST. Do not uninstall/reset/reimport assets.
- Next Pikmin 2 task: Keep installed working version. Do not install45. Use scene-enabled new IPA only after gate/native/package verification, then regression test audio/gameplay.
- GitHub/build task: Build47/run39992850789, source2034e139369df84f61fd499d0d085b4e567b1d78, startup job120548733186: dispatched, no result yet. Stop idle polling once dispatched. On reported completion retrieve gate log and diagnostics first; only after PASS inspect both native jobs/IPAs. Fix real failures rather than disabling the gate.
- Anything requiring my involvement: Nothing on the phone now; it may be closed/disconnected. Report build completion. A separate verified settings/save/assets backup is still needed before erasing/transferring away the old phone; none was created from the recent crash-log connection.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know:46 failed before either game compiled. This is a missing platform header, not a new gameplay/audio symptom. Shared scene source remains unverified natively.44 P1 startup trap confirmed;45 P2 compile PASS/HOLD. Original IDs and player-selected120/landscape retained. No new co-op/autosave/AI changes; existing texture/mod installation and prior features preserved, not reinstalled.
- Important source-file locations: ios/IOS27_SCENE_LIFECYCLE.md diagnosis/design; ios/sdl_scene_support.cmake private SDL2 opt-in; ios/Info.plist.in scene manifest; SDL UIKit appdelegate NectarSDLSceneDelegate/nectarConnectWindowScene and single-entry guards; actual scene-owned window and filtered notifications. SDL_coreaudio.h owns new import. tests/ios_scene_smoke, tests/run_ios_scene_smoke.py; ios/verify_scene_bundle.py checks manifest plus compiled class/selector markers. Workflow scene-startup gates both games.
- Relevant logs: work/build46-scene-full.log, build46-scene-artifact.zip, build46-failure-verification.json; copies in Documents/Open Nectar/2 - Progress and ChatGPT Handoff. Private P144 crash reports under work/p1-build44-launch-20261023-091109 and friendly folder2/P1 Build44 - Private Startup Crash Evidence.45 full successful log and held verification retained. No private evidence in Git.
- Unverified fixes: New owning-header correction has no Apple compile yet. All scene startup/runtime/actual gameplay rendering/audio/display checks remain pending. Probe is asset-free generic SDL window, not the game GLES renderer. Full story/follower teleport/rare scene bugs remain unproven.
- Risks and warnings: Keep44 DO-NOT-INSTALL and45 HOLD. Scene migration changes shared platform startup; possible later compile/runtime issues remain. Simulator evidence cannot establish real phone gameplay or Duo sizing. No complete current game-data backup; do not erase old phone assuming crash reports contain saves/assets. Don't force-push, merge main or alter working installs.
- Exact next actions: Build47/run39992850789, source2034e139369df84f61fd499d0d085b4e567b1d78, startup job120548733186: dispatched, no result yet. When completion reported, retrieve startup artifact/logs, confirm actual simulator launch and background/resume; if successful retrieve both game artifacts and validate original-ID/ARM64/device/unsigned/SDK/icons/scene manifest plus compiled support. Stage only validated IPAs in friendly folder1, then request launch-first phone tests. Stop idle polling while waiting.

**END PROGRESS REPORT**
