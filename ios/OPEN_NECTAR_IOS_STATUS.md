# Open Nectar native iOS status

Updated: 2026-10-19, America/New_York. Branch: `ios-experimental`.

## Preservation baseline

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Starting local and fetched remote commit: `ed22a5ea9c362fba953b525d5358384426f23bf2`.
- Initial working tree already contained the three-edit `EnemyMgrBase.h` v1.4 iterator correction. Preserve and attribute it as pre-existing work.
- Pikmin 1 framebuffer correction is present in `games/pikmin1/pc_port/pc_window.cpp` (`pc_window_ios_drawable`, swap binding) and `gl/pc_gfx.cpp` (`pc_gfx_display_framebuffer`). Do not revert it.
- User reports Pikmin 1 title/menu/gameplay/Olimar movement/audio/touch working on iPhone 15 Pro Max, reportedly iOS 27.2. This session has no new hardware evidence.
- No game images, extracted assets, credentials, or signing material belong in Git.

## Verified build baseline

Build #9: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39167424765

- Commit: `ed22a5ea9c362fba953b525d5358384426f23bf2`.
- Pikmin 1 job `117793183742`: success, artifact `12150844781` (`nectar-pikmin1-experimental`).
- Pikmin 2 job `117793184024`: failure, artifact `12150864586` (`nectar-pikmin2-experimental`, compiler log only).
- Full workflow logs and Pikmin 2 compiler artifact retrieved directly from GitHub on October 19.
- Compiler artifact contains exactly one fatal compiler error: `EnemyMgrBase.h:95`, pointer-to-smaller-`int` conversion in `get(void*)`, compiling `plugProjectKandoU/vsTekiMgr.cpp`. No linker stage reached. Prior `vtxAnm.cpp` errors absent.

## Pikmin 1 investigation

- Downloaded Settings Menu Fix v1.4 ZIP exists but was not applied to the baseline.
- F1 settings mobile layout/render mapping/viewport are Android-only. iOS uses a fixed 640x480 desktop canvas.
- Title Options uses a separate fixed-canvas `settings/pc_glass_menu.cpp`; changing F1 gates alone does not address it.
- Settings GX/P2D text renders into the scene framebuffer before `pc_gfx_present`, then is linearly upscaled. Default scene render scale is 2/3.
- SDL UIKit defaults to scale 1 without `SDL_WINDOW_ALLOW_HIGHDPI`; touch icons draw after presentation through the independent overlay.
- Implemented candidate: retina drawable; retain logical-pixel scene workload during normal gameplay; full drawable resolution while F1 or title Advanced settings are open; 400-high mobile canvas and matching inverse touch mapping. Menu frame mode is latched for consistent presentation aspect; saved resolution/aspect settings remain unchanged. Conservative landscape margins are 56 horizontal and 24 bottom virtual units; dynamic UIKit safe-area support remains future work.
- Local verification: 115 C++17 x64 cases compiled/executed from actual changed geometry/sizing functions: four drawable shapes, inverse touch mapping, all five aspect modes, three render scales, both menus, explicit resolution override, close restoration, and mid-frame latch. MSVC emits only isolated harness shadow warnings. This does not compile the full iOS renderer.
- Changed source: pc_window.cpp high-DPI flag; gl/pc_gfx.cpp menu-frame resolution choice; settings/pc_settings.cpp mobile F1 gates/margins; settings/pc_glass_menu.cpp mobile Advanced layout, viewport/scissor, inverse tap/drag mapping. Existing SDL drawable framebuffer correction is retained.
- Hardware clarity/performance/touch validation remains required. Opening menus temporarily allocates a larger scene target and can cost memory/time. Original basic game Options/BLO typography is not redesigned by this patch.
- Existing right-thumb camera gesture is implemented in `touch/pc_touch.cpp`: separate movement and gesture fingers, button exclusion, one-finger rotation and two-finger zoom. Do not add a duplicate camera system before testing settings/behavior.

## Pikmin 2 verification

- Existing `EnemyMgrBase.h` change includes `<cstdint>`, encodes `getEnd()` through `std::intptr_t`, and decodes `get(void*)` through `std::intptr_t` before converting the bounded slot index to `int`.
- Local x64 MSVC C++14 `/W4 /WX` check compiles the actual changed inline methods extracted from the header. Execution passes empty/end handling and valid-slot pointer/index round trips. This is not an AppleClang/iOS build.
- Corrected the same pointer-as-index conversion in `src/plugProjectYamashitaU/enemyMgrBase.cpp::getNext`, including returned slot/end tokens. CMake includes this source through GAME_YAMASHITA_SOURCES. This is a verified source hazard adjacent to the logged header error, not a separately observed Build 9 compiler error.
- Extended x64 C++14 semantic check passes actual extracted getNext code with the -1 start sentinel, empty list, skipped inactive slots, live slots 2/6, and end-of-iteration handling.

## Workflow and authority

- Existing `.github/workflows/ios-native-experimental.yml` builds both matrix games on macOS/Xcode.
- Only commit messages containing `[ios-build]` execute build jobs; documentation commits should omit it.
- User authorizes normal scoped commits/pushes to `ios-experimental`, existing workflow builds, logs, and artifacts. No force pushes, history rewriting, main merges, repository security changes, or stable releases.
- Git authentication verified with a successful dry-run push October 19. Do not store credentials in documentation or scripts.
- User is applying to jobs; only request necessary input. Play an audio alert when user action is needed.

## Exact next actions

1. Read the next build result when the user reports completion; retrieve full failed logs directly and iterate from evidence.
2. User can install the Build 10 Pikmin 1 IPA and test F1/title Advanced clarity, edge taps, scrolling, notch clearance, and restoration of gameplay/audio/touch.
3. After Pikmin 2 compiles/packages, validate its own presentation/input/audio on the phone.
4. Keep build, IPA, installation, and runtime milestones distinct. User requested no idle polling while waiting for GitHub.

## October 19 implementation milestone

- Pikmin 2 correction committed as 5543394e43f8c9b3bc51b75e995aa9b8b3752df1 (includes preserved pre-existing header work).
- Pikmin 1 candidate and journal prepared for the same push; final commit will contain [ios-build]. No new IPA or runtime result yet.
- Working source was checked with git diff --check; no proprietary assets or unrelated files staged.

## Build #10 dispatched

- Run: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39263564026
- Exact build commit: `483815d4b0d4f8b074be5381738f59af3a54b796`.
- Includes Pikmin 2 commit `5543394e43f8c9b3bc51b75e995aa9b8b3752df1` and Pikmin 1/journal commit `483815d4`.
- Push succeeded; initial live status queued on October 19 at approximately 09:50 Eastern.
- Results, IPA contents, installation, and runtime remain pending. Do not label menu appearance fixed yet.

## Pikmin 2 presentation investigation and candidate

- Its own `pc_port/gl/pc_gfx.cpp` still targeted FBO 0 in final present and touch overlay. Its own `pc_port/pc_window.cpp` swapped on iOS without binding UIKit's drawable framebuffer/color renderbuffer.
- Applied a P2-only candidate following inspection of its implementation: `pc_window_ios_drawable` uses SDL SysWM UIKit information; swap binds that FBO/RBO and restores separate prior read/draw/RBO bindings; final presentation and overlay use the SDL display FBO.
- Existing P1 source is unchanged by this follow-up. No P2 Retina, resolution, audio, or settings behavior is changed.
- Local MSVC C++17 host validation passes five states using actual candidate helpers/swap code: valid target, replaced drawable, unavailable WMInfo, wrong subsystem, and null window. Prior distinct bindings restore exactly. This is simulated host validation, not OpenGL execution on iPhone.
- These P2 display changes are not included in Build #10; they await a later commit/build. No runtime black screen has been observed for P2 in this session.
- Audio clarification: P2 uses its own JSystem JAS/JAI software DSP and SDL sink. The top-level PIKMIN_NATIVE_JAUDIO=OFF does not establish missing P2 audio. Hardware audio remains unverified.
- Camera clarification: P1 touch drag is consumed without requiring Free Camera; Free Camera Speed changes the controller stick, not touch sensitivity.

## Build #10 result and next corrections (October 19, ~10:06 Eastern)

- Build #10 is completed: Pikmin 1 job 118097217644 succeeded; Pikmin 2 job 118097217295 failed. Exact source commit remains 483815d4b0d4f8b074be5381738f59af3a54b796.
- P1 artifact 12193380985 contains Nectar-pikmin1-unsigned.ipa (2,550,357 bytes). ZIP integrity passes; Payload/Nectar-pikmin1.app has ARM64 Mach-O executable Nectar-pikmin1 (6,295,688 bytes), bundle org.opennectar.experimental.pikmin1, minimum iOS15.0. SHA256 8138f1f378a04b9597aaee8fa725611a9ddd7d57f9e0f8263fc2e872b17999cc. Not installed/tested in this session.
- P2 artifact 12192161804 contains the failed build log. Full workflow archive is retained as work/build10-logs.zip in the local task workspace.
- Ten compiler errors, one root: VsOtakaraName undeclared in vsGameSection.cpp at lines383 (three),807(two),1084,1120,1313,1347(two). No linker error/stage reached. Previous EnemyMgrBase pointer error is absent.
- Compiler warning trace shows pikmin2-decomp-adapter/VSOtakaraName.h including itself through case-only spelling VsOtakaraName.h on case-insensitive macOS. The include guard then hides the real struct.
- Corrected VSOtakaraName.h to explicitly include ../pikmin2-decomp/include/VsOtakaraName.h. Corrected the identical verified pattern in PikiAi.h to explicitly include ../pikmin2-decomp/include/PikiAI.h. No other basename self-includes were found in the adapter headers.
- Local MSVC C++14 test reproduces the old case-only alias failure on Windows, then the actual corrected VsOtakaraName header compiles under /W4 /WX. PikiAI preprocessing reaches the real _PIKIAI_H guard; it emits existing host/decomp varargs redefinition warnings, not a full source compile result.
- P2 display follow-up is committed as 762eba1b16d24976bf3cfb84f430052756c51e1a. It and the two alias corrections will be pushed together for the next build. P1 source remains exactly the Build10 version.
- User requested conserving usage: after dispatching the next build, stop polling and wait for the user to report completion.
## Build #11 dispatch and stop-wait checkpoint

- Run https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39265932808; initial status queued at October19 10:06 Eastern.
- Exact local/remote source commit 204c06ade5e82bebd528a56e46bfa76b66115fb9, including P2 display commit762eba1b16d24976bf3cfb84f430052756c51e1a. Push succeeded.
- No P1 source change since successful Build10. Build11 compiler/IPA/runtime results are pending.
- This dispatch checkpoint is the only post-push uncommitted journal update. No source edits remain uncommitted.
- STOP idle polling per user request. Resume when user reports the build result; fetch the actual run/job logs and continue from evidence.

## User-facing project folder (October 19, 2026)

The user requests all future test materials in C:\Users\chazz\Documents\Open Nectar.
Put each test IPA in `1 - Install on iPhone`, with a clear game/build filename
and short WHAT TO TEST.txt. Refresh plain-text progress/master-handoff copies
in `2 - Progress and ChatGPT Handoff` after milestones. Use these accessible
paths when asking the user to install/test; do not make them browse generated
Codex directories. Play an audio alert when user action is required.

Nine reviewed Downloads items were moved individually and SHA256-verified.
RVZ images are in `3 - Game Files - Keep Private\Original RVZ Files`.
Verified ISOs, source code, active/earlier sessions, and display backup are
accessible through junctions; originals stay at their existing working paths.
Windows Documents points to OneDrive; its Open Nectar.lnk points to the local
project folder, keeping game data outside OneDrive and the Git repository.

Automatic approval review rejected the initial bulk relocation of the live
repo/active chat workspace. The safer staged plan moved only reviewed Downloads,
kept active directories in place, and added access links. The old bulk script
is disabled; do not rerun it. No build was triggered for organization.

## Build #11 result and nested adapter fix (October 19, ~10:27 Eastern)

- Exact build commit204c06ade5e82bebd528a56e46bfa76b66115fb9. Run39265932808 completed: P1 job118105370021 success; P2 job118105369589 failure.
- Artifacts: P1 12193133375 (unsigned build bundle), P2 12193278343 (failed build log). The user is testing the existing Build10 P1 IPA; no hardware result has been reported. Do not replace that test with a redundant P1 download.
- Complete workflow logs retrieved as work/build11-logs.zip and extracted in work/build11-full. Exactly one fatal compiler error: vsGS_Title.cpp298, Morimura::DispMemberChallengeSelect incomplete. No linker stage reached. Previous VsOtakaraName errors absent.
- The warning trace identifies the same self-include hazard in pikmin2-decomp-adapter/Morimura/challengeSelect2D.h. Its include with a directory component resolves back to itself on a case-insensitive host, hiding the real challengeSelect2d.h definition.
- Previous audit only tested basename includes and missed this nested path. Corrected the adapter to include ../../pikmin2-decomp/include/Morimura/challengeSelect2d.h explicitly.
- Added tests/pikmin2_adapter_includes.py. It models case-insensitive lookup using a case-folded adapter/decomp header inventory, including directory components and normal local-header-first lookup. It detected the original recursive include; after the correction all43 adapter headers pass.
- Existing experimental workflow runs the new fast check only for the pikmin2 matrix job before CMake configuration. P1 source is unchanged. Workflow step reviewed; no local YAML parser package was available, so no YAML-parser pass is claimed.
- Actual corrected header was preprocessed by local MSVC C++14, confirming the real _MORIMURA_CHALLENGESELECT_H guard and complete DispMemberChallengeSelect declaration. Full AppleClang compilation and P2 presentation/runtime remain pending.
- Next: push this fix/test/workflow update together with the accumulated organization documentation. Record the new build ID, refresh the user-facing reports, then stop idle polling. Resume from compiler evidence when the user reports completion. P1 hardware feedback remains pending.
