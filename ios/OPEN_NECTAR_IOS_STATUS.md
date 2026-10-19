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

1. Finish and review the Pikmin 1 candidate against both settings render paths and touch mapping.
2. Preserve existing Pikmin 2 correction; run local checks and inspect staged diff for assets/unrelated work.
3. Fetch/recheck remote, commit scoped fixes, and push once with `[ios-build]` on the final commit.
4. Record the exact build commit/run/job IDs; retrieve failures directly and iterate based on compiler evidence.
5. Record build, IPA, installation, and runtime as distinct milestones; ask for a targeted phone test only once an IPA is ready.

## October 19 implementation milestone

- Pikmin 2 correction committed as 5543394e43f8c9b3bc51b75e995aa9b8b3752df1 (includes preserved pre-existing header work).
- Pikmin 1 candidate and journal prepared for the same push; final commit will contain [ios-build]. No new IPA or runtime result yet.
- Working source was checked with git diff --check; no proprietary assets or unrelated files staged.
