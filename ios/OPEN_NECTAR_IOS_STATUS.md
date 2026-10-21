CURRENT - 2026-10-21 10:33 EDT: Build36 CANCELLED at user request. Combined crossing/route+Recall All/Pikmin Speed source localPASS63/82/283; combined P1-only standard build pending commit/push. New Apple/IPA/phone pending. Build35 rollback intact, P2 paused. No teleport or phone writes.

CURRENT - 2026-10-21 10:11 EDT: Build35 phone Aim/SoftAssist/charge whistle/save-reload PASS; clam untested, raised crossing stranded followers persist. Separate recall button +Pikmin Speed localPASS82/283, Build36/run39614665805, source472937e505eef2a14d00b0c923620dbaee4bd9cd, observed in_progress. New Apple/IPA/phone pending; no stuck-rescue/teleport implementation; P2 paused.

CURRENT - 2026-10-21 10:10 EDT: Build35 phone Aim/SoftAssist/charge whistle/save-reload PASS; clam untested, raised crossing stranded followers persist. Separate recall button +Pikmin Speed localPASS82/283, P1-only standard build pending commit/push/dispatch. New Apple/IPA/phone pending; no stuck-rescue/teleport implementation; P2 paused.

CURRENT - 2026-10-21 01:43 EDT: P1 Build35/run39548476790 SUCCESS, source01d7e7ed18df04cb0856ae5cab77b6df62101e39. STANDARD original-ID ARM64 device IPA verified/staged in folder1; SHA256 eab4b43ccaeda4de25137e010342592a4e0fc6d2cd328be9b66d365d10e3cc89. Phone installation/runtime pending; P2 unchanged. No new build needed; await normal-save test feedback.

CURRENT - 2026-10-21 01:15 EDT: Build34 FAILED (missing KeyConfig.h), corrected/local checks PASS, source01d7e7ed18df04cb0856ae5cab77b6df62101e39. P1-only STANDARD Build35/run39548476790 in_progress at dispatch. No new IPA/phone result; P2 unchanged. No idle polling.

## Build 34 compiler correction — 2026-10-21 01:14 EDT

- Build 34 / run 39545404613 / source ff57b9ffc71b9fcd87c444630b2454bcbe4e4110 FAILED. Full job 119042338355 log inspected: one compiler error, navi.cpp:1539 undeclared KeyConfig. No new IPA was produced. Installed P1/P2 remain unchanged.
- Cause: new whistle-priority code used the correct existing binding API but navi.cpp lacked its direct KeyConfig.h include. The extracted host fixture supplied that type and missed this integration dependency.
- Correction: add the direct include; generator now rejects source using KeyConfig without that header. Negative control on Build 34 source fails with the expected dependency message.
- Local verification: 60 command/aim/recall/edge scenarios PASS; preset update/separate/standard 58/58/7 PASS; Clang checks PASS; git diff --check PASS. Apple compilation and phone runtime still pending.
- Next build is P1-only STANDARD normal campaign, original app identity, all previous fixes retained; no P2 change, no synthetic campaign, no autosave/network feature enabled. Verified restore backups remain intact. After dispatch, record run/source and stop waiting; user will report completion.

CURRENT - 2026-10-21 00:42 EDT: P1-only normal-campaign Build34/run39545404613 DISPATCHED, sourceff57b9ffc71b9fcd87c444630b2454bcbe4e4110, observedin_progress. Includes baa8af2b upstream RNG correction and locally checked command/aim/recall/edge batch. Apple/IPA/phone results pending. No new autosave/networking feature enabled. Phone may disconnect. No idle polling.

CURRENT - 2026-10-21 00:40 EDT: Build33 phone test/save evidence collected. P1 charge/whistle/cursor, Aim/Soft Assist, recall and bounded ledge fixes implemented/local PASS60+58+58+7+27 checks; P2 shared menus188/198 PASS. Standard P1-only Apple build pending dispatch. Normal saving retained; shared exact-scene snapshot/co-op plan recorded. Upstream1.0.6 audited, isolated RNG fix adopted. Phone released; no phone writes.

CURRENT - 2026-10-20 21:15 EDT: P1-only Build33/run39523034602/source8e813868 SUCCESS. Original-ID solo-update IPA verified/staged; SHA256 c04abe4dad2a9ecfada89ddfa53e24aa40c6a272696df1d6dd45bdc32fd7916b.
Backup intact; exact install/checklist in folder1. Phone install/settings/save/runtime unverified. P2 Build32 positive user feedback. No new build needed; await test results.

CURRENT - 2026-10-20 20:49 EDT: User reports "P2 is working now" after Build32. This is a positive phone runtime/audio retest in the context of the missing Pikmin/enemy sounds. Individual effects, other colors, distance attenuation, caves/area transitions and the full campaign were not separately confirmed. No new phone audio report was retrieved; do not describe every sound as independently verified.
P1-only Build33/run39523034602 remains pending at last observation; no CI polling performed.
P1 rollback backup remains verified; phone may disconnect. Documentation-only update, no build.

CURRENT - 2026-10-20 20:44 EDT: P1-only Build33 dispatched, run39523034602,
source8e8138684fd5e36595a89058d090240217fe66ae, observedin_progress.
Verified rollback backup ready; current-app test update uses preserved settings/
assets and separate test saves, no finale preset. New Apple/IPA/phone tests pending.
User can disconnect. No idle polling; next inspect once user reports completion.

CURRENT - 2026-10-20 20:43 EDT: P1 current-app test update authorized; verified rollback
IPA/settings/layout/save backup completed first. New solo-update source locally
PASS, Apple build pending. Reuses assets/settings, separate test cards, no finale.
P2 unchanged; Build32 audio phone result pending. No phone writes or new install.

CURRENT - 2026-10-20 20:26 EDT: Build32 BOTH PASSED, run39518825366, source1f04dd8f.
P1 Solo Test and P2 IPAs verified/staged in folder1; neither new app phone test confirmed.
Original P1 untouched; finale deferred. Next: P2 audio retest, separate P1 install
and private content preparation over USB, then spoiler-free A/C checks.
No new build needed; see current master handoff and folder1 instructions.

CURRENT - 2026-10-20 20:05 EDT: User requests spoiler-free P1 testing. Final boss/ending
coverage deferred; not a prerequisite for separate co-op prototype. Use A/C and
familiar earlier areas, avoid B/final area. Invincibility optional; skipped death/
hazard behavior remains unverified. Build32 source unchanged; no extra build.

CURRENT - 2026-10-20 20:03 EDT: Combined Build32 DISPATCHED, run39518825366, observedqueued.
Source 1f04dd8f0117b91c0e5cc6e80cd61384943603e9; includes90785c36 P2 mute cleanup.
P1 is the separate solo-test app; P2 retains standard identity. Local checks PASS;
new Apple results/IPAs/phone tests pending. Original P1 untouched. Phone released.
No idle polling: user reports completion. Exact source/run in current handoff.

CURRENT - 2026-10-20 20:01 EDT: P1 solo-test source/presets and P2 opening mute cleanup locally verified.
Original P1 app untouched. New test IPA/phone scenarios pending. P2 Build31 snow
ambience restored; Pikmin/enemy audio still silent. Report retrieved; nearby gains
zero only in those categories. Opening exit cleanup candidate implemented/tested.
Combined P1 test/P2 standard build pending dispatch. See latest master handoff.

CURRENT - 2026-10-20 19:43 EDT: Build31 P2-only PASSED, run39514971137, sourcedc73a848.
Verified IPA staged in folder1. New audio/proximity/report phone test pending.
P1 working app untouched. Separate solo-readiness test approach accepted;
eventual proven co-op is intended for original app. No test IPA/co-op code yet.
See PIKMIN1_SOLO_READINESS_PLAN.md and current master handoff.

CURRENT - 2026-10-20 19:26 EDT: P2-only Build31 DISPATCHED, run39514971137.
Source dc73a84887e60d4e3b7911b1e46ed64ab4a764b9; observed in_progress.
Native JAI parameter stride/report platform defects corrected; local48 parameter,
11 activation and28 routing checks PASS. Apple result/IPA/phone audio pending.
Build30 HUD clearer; audio failed on phone. P1 unchanged. No idle polling.
Phone/game not needed until next successful install/test. See current handoff.

CURRENT - 2026-10-20 19:25 EDT: Build30 phone result: HUD clearer, audio NOT resolved.
Pikmin/enemy/wind missing; ship and inactive captain breathing can ignore distance.
Confirmed native audio parameter union stride defect and report activation defect;
local48 producer/consumer and11 platform report checks PASS. New Apple build pending.
P1 unchanged. Phone had no audio reports; see current handoff/audio audit notes.

CURRENT - 2026-10-20 19:10 EDT: P2 Build30 PASSED, run39509564730, sourcee9a06beb.
New unsigned IPA verified and staged in folder1; phone install/audio/HUD test pending.
P1 untouched. All142 P2 audio assets matched phone originals. User accepted saving
separate P1 online prototype plan; no online implementation started.
See PIKMIN2_AUDIO_AUDIT.md, ONLINE_COOP_DESIGN_NOTES.md and current master handoff.

CURRENT - 2026-10-20 18:39 EDT: P2-only Build30 DISPATCHED, run39509564730.
Source e9a06bebd443e3eb5d8943a5c01c53e186512423; observed in_progress.
All142 phone audio files match originals. Local mixer/HUD/audit checks PASS.
Apple result/new IPA/phone audio and HUD validation pending. P1 unchanged.
No idle polling. See current master handoff and PIKMIN2_AUDIO_AUDIT.md.

CURRENT - 2026-10-20 18:37 EDT: P2 audio/HUD batch locally verified; Apple build not dispatched yet.
Build29 phone gameplay/settings confirmed, but voices/wind/ship-distance issues remain.
All142 phone AudioRes files SHA-256 match originals. HUD toggle resolved by user.
New mixer/HUD corrections and bounded diagnostics require Apple/phone validation.
See PIKMIN2_AUDIO_AUDIT.md and the current progress report below. P1 untouched.

CURRENT - 2026-10-20 14:31 EDT: Build29 P2-only PASSED; verified enhancements IPA ready in folder1.
Source7f7d0783/run39470849443. New phone installation/runtime test pending.
P1 textures confirmed354 replacements/0 failures; P1 unchanged. Future co-op
choices recorded (notes only, implementation still last). Older pending headers historical.

CURRENT - 2026-10-20 14:07 EDT: P1 GPI HD textures CONFIRMED loading on phone:
354 successful replacements,0 failed;455 originals not in pack. No P1 changes needed.
P2 Build29 result still pending at last observation; no idle polling.
Older texture-unconfirmed notes below are superseded by this screenshot.

CURRENT - 2026-10-20 14:00 EDT: Build29 P2-only DISPATCHED, run39470849443.
Source7f7d0783e8b42870a8b6bbb1954199fbe9ffc6bb; observedin_progress.
Build28 FAILED at import API call; corrected, new19-check real API fixture PASS.
Build29 result/link/IPA/phone tests pending; Build27 working baseline. P1 untouched.
No idle polling. Next inspect Build29 when user reports done. Older entries historical.

CURRENT - 2026-10-20 13:59 EDT: Build28 FAILED (2 compiler errors,1 incorrect API call).
Correction and19-check real menu/API regression locally PASS; retry not dispatched yet.
Build27 remains limited positive phone baseline. P1 untouched; texture replacements
not confirmed. New entries supersede older pending-build headers below.

CURRENT - 2026-10-20 13:42 EDT: Build28 P2-only DISPATCHED, run39468391460.
Source386771cabe6366b0788091f4d6d63f9ef6850c67; observed in_progress.
Local checks PASS; new Apple result/IPA/phone tests pending. Build27 user reports
no crashes so far (limited test). P1 app unchanged; GPI activation unverified.
No idle polling; next action inspect Build28 when user reports completion.

CURRENT - 2026-10-20 13:41 EDT: P2 enhancements implemented; local checks PASS.
Apple build/IPA/new-profile phone tests pending. Build27 user reports no crashes
so far (limited test). P1 GPI texture pack installed/listed but inactive in screenshot;
activation unverified. P1 working app untouched; keep60FPS. New entries supersede
older current-status headers; older entries below are historical.

CURRENT - 2026-10-20 09:57 EDT: Build27 P2-only PASSED; verified IPA in folder1.
P2 phone crash/control retest pending. P1 models INSTALLED, runtime pending;
saves/settings unchanged. HD environment textures NOT installed.

CURRENT CONTENT UPDATE - 2026-10-20 09:52 EDT: P1 character bundle INSTALLED;
20 files hash-verified, saves/settings unchanged. P1 model runtime test pending.
HD environment textures NOT installed. P2 Build27 pending at last dispatch.

CURRENT - 2026-10-20 09:38 EDT: Build26 PHONE REGRESSIONS: menu gear/A hidden;
captain-preview/Metal heap crashes. P2-only batch locally checked; Build27/run39432157516 (in_progress at dispatch).
New Apple build and phone results pending. Build24 backup; P1 untouched.

CURRENT - 2026-10-20 09:37 EDT: Build26 PHONE REGRESSIONS: menu gear/A hidden;
captain-preview/Metal heap crashes. P2-only batch locally checked; not dispatched.
New Apple build and phone results pending. Build24 backup; P1 untouched.

CURRENT - 2026-10-20 09:19 EDT: Build26 P2-only PASSED; verified IPA ready in folder1.
Menu clarity/input on phone pending. Build24 opens; P1 untouched.

CURRENT CHECKPOINT - 2026-10-20 08:43 EDT: Build25 failed only the new test fixture;
correction locally verified. P2-only Build26 run39424440094 dispatched; result pending.
Build24 opens on phone; menu candidate remains unverified. P1 untouched.

CURRENT CHECKPOINT - 2026-10-20 08:42 EDT: Build25 failed only the new test fixture;
correction locally verified. P2-only replacement build not dispatched yet.
Build24 opens on phone; menu candidate remains unverified. P1 untouched.

LATEST BUILD: P2-only Build25 at 3013d4c2;
result/IPA/menu phone test pending. Build24 opens; P1 untouched.

CURRENT - 2026-10-20 08:33 EDT: user resumed. Build24 P2 startup/menu opening CONFIRMED.
P2 clarity/options-touch candidate implemented; local tests PASS, next Apple
build and phone checks pending. P1 untouched. Prior paused notes are historical.

# PAUSED AT USER REQUEST - 2026-10-20 01:13 EDT

The user is shutting the PC down and explicitly asked to pause until morning.
Do not resume source edits/builds/phone operations until asked to continue.
No source edits, commits, pushes, new builds or phone operations occurred in
this menu-investigation turn. Only repository/source/history reads were done.
Repository branch ios-experimental; local/fetched remote HEAD both
00bd0db831ce09d37c3da94e00ec5596e2256563, working tree clean at investigation
start. Build24 source05e33f1c0e55dc11ecb6d413a8393bf73faeb2ce/run39371370836
PASSED, and the user now CONFIRMS P2 OPENS on the phone and reaches menus.
This supersedes earlier 'new phone startup unverified' notes. Do not infer
verified audio/gameplay/full-game stability from this menu/startup observation.
Preserve Build24 allocator/thread ownership and SDL UIKit framebuffer fixes.
P1 app, data, source and its working menu/camera behavior remain untouched.

Two newly reported P2 issues (screenshots attached in chat):
1. Advanced Open Nectar menu is small/blurry, resembling P1's earlier problem.
2. Original game Options/exit-confirmation screen accepts only bottom-left X/
   Back. User clarified main-screen taps and Throw/A work; failure is specific
   to that menu/dialog. Do NOT diagnose all touchscreen input as broken.

Read-only findings before pause:
- Working P1 pc_window.cpp has SDL_WINDOW_ALLOW_HIGHDPI on iPhone; P2 lacks it.
- P1 pc_gfx.cpp latches ios_native_settings_frame and renders menus at native
  drawable resolution independently of gameplay render scale/resolution. P2
  lacks this path; its screenshot shows a low internal scene scale/resolution.
- P1 pc_settings.cpp enables the 400-high mobile canvas for iOS and Android,
  with iPhone landscape margins, matching viewport/scissor and inverse tap map.
  P2 still restricts those branches to Android. P2's shim begin_frame also sets
  virtual dimensions only on Android, so include it when adapting the solution.
- P2 TOption::doUpdateStateWait has controller input but no touch-pane handling.
  Its rows are mButtonPaneList[7]; save is row6/A; other settings use left/right.
- The pictured confirmation uses ObjWorldMapInfoWindow0 -> ObjSMenuPauseVS.
  ObjSMenuPauseVS::menu ALREADY claims game-menu touch, calls
  MenuMgr::pcTouchTappedOption and treats tapping selected option as A.
  Investigate why that existing path fails before adding duplicate handlers.
- pc_touch.cpp only allows Back plus buttons requested by visible help icons
  while a game menu owns input. Its separate MENU_CONFIRM is currently allowed
  only for port menus. Check whether this original dialog exposes a usable A
  control and whether pane tracking/projection hits its visible text correctly.
  The main-screen working controls should remain unchanged.

Exact resumption steps:
1. User says resume; read this checkpoint and newest journal; verify branch/
   status/fetch again and preserve any changes made after this pause.
2. Compare actual working P1 menu/high-DPI/render-budget code with P2. Adapt
   P2 paths, including its DGX shim, mobile layout and inverse taps; preserve
   gameplay pixel budget, startup fixes and P1 source/data.
3. Inspect TOption and inherited confirmation input/tracked panes. Implement a
   targeted original-options fix preserving main-screen/gameplay controls and
   keeping save/discard actions explicit. Do not auto-save or auto-discard.
4. Add meaningful layout/Retina/touch-state checks; build P2 only after local
   checks and review. No fixes are implemented yet and no Build25 was triggered.
5. Record exact commit/run; do not idle-poll Actions. When result known, verify
   IPA, put in folder1 with short test guide. Phone tests: readable full-width
   advanced menu, taps/scroll alignment, original options rows, confirmation
   Continue/Don't Save, Back, plus startup/gameplay/audio/control regression.
6. Keep P1 untouched. Optional packs and online with Raye remain later; online
   LAST. User is asleep; no immediate test request/audio alert is needed.

Important source locations:
games/pikmin1/pc_port/pc_window.cpp andgl/pc_gfx.cpp (working reference)
games/pikmin1/pc_port/settings/pc_settings.cpp (working mobile layout)
games/pikmin2/pc_port/pc_window.cpp andgl/pc_gfx.cpp
games/pikmin2/pc_port/settings/pc_settings.cpp andpc_settings_p2_shim.cpp
games/pikmin2/pc_port/touch/pc_touch.cpp andpc_touch.h
games/pikmin2/pikmin2-decomp/src/plugProjectEbisawaU/ebiScreenOption.cpp
games/pikmin2/pikmin2-decomp/include/ebi/Screen/TOption.h
games/pikmin2/pikmin2-decomp/src/plugProjectOgawaU/ogObjSMenuPauseVs.cpp
games/pikmin2/pikmin2-decomp/src/plugProjectOgawaU/ogObjWorldMapInfoWindow0.cpp
games/pikmin2/pikmin2-decomp/src/plugProjectOgawaU/ogMenuMgr.cpp
games/pikmin2/pikmin2-decomp/src/JSystem/J2D/J2DPane.cpp
Session work/prepare_pikmin1_menu_candidate.ps1 records the earlier P1 patch;
read it as historical evidence, do not blindly execute it against current code.

END PAUSE CHECKPOINT

LATEST CHECKPOINT - 2026-10-20 01:03 EDT: P2 Build24 SUCCESS; target ARM64 allocator
check and actual binary16-byte alignment verified. New IPA ready in folder1.
NEW phone installation/startup/audio retest pending. P1 working and untouched.
Earlier Build23 phone startup failed; read newest journal entry for current state.

CURRENT BUILD: P2-only Build24 dispatched at 05e33f1c;
result and phone retest pending. P1 untouched.

LATEST CHECKPOINT - 2026-10-20 00:46 EDT: P2 Build23 phone startup FAILED on AudioQueue
thread. Matched real crash UUID; binary new alignment is8bytes. 16-byte floor +
native/game thread allocation ownership batch implemented; local tests passed.
Next P2-only Apple build pending. P1 working/untouched. Older pending/success
checkpoints describe compilation or historical results, not a working P2 app.

LATEST CHECKPOINT - 2026-10-20 00:34 EDT: P2 Build23 SUCCESS; startup candidate IPA ready
in folder1. Source609a45b1/run39369282124. New phone installation/startup retest
PENDING. Update P2 only; preserve data/assets/art. P1 working and untouched.
Read the newest journal entry; earlier build-pending checkpoints are historical.

LATEST BUILD CHECKPOINT: P2-only Build23 dispatched at 609a45b1;
Apple result/IPA/phone retest pending. P1 untouched.

CURRENT CHECKPOINT - October 20, 2026: P2 Build22 installs but crashes at first
draw. Real phone crash reports identify an alignment fault; allocator + renderer
scope candidate implemented and local tests passed. Next P2-only Apple build and
phone retest pending. P1 working and untouched. Read newest journal entry below;
historical pending/paused instructions are superseded by this checkpoint.

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

## Build #12 dispatch checkpoint

- Run https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39269078016
- Exact local/remote commit37020a74c26748a1f78c7dbb7936c3e812934d29; initial status queued at October19 ~10:27 Eastern.
- Includes the nested Morimura adapter fix, 43-header case-insensitive self-include check, P2-only workflow precheck, and saved folder-organization documentation. No P1 source changes.
- All source and prior folder-policy documentation are pushed. Only this post-push status-journal checkpoint is uncommitted.
- User is testing P1 Build10; no appearance/control/audio feedback received yet. STOP idle polling; await user report on Build12.

## PAUSED — October 19, 2026, 10:44 AM Eastern (user request)

The user requested immediate pause because usage is nearly exhausted. Do not
resume development, commit, push or dispatch a build until asked to resume.
P1 menu readability and camera controls are now phone-confirmed by the user;
full-game completion and optional enhancement behavior are not verified.

Local HEAD and fetched origin/ios-experimental both37020a74c26748a1f78c7dbb7936c3e812934d29.
New P1 enhancement work is UNCOMMITTED: one-time QOL/visual profile with config
backup, persisted marker, native Files ZIP picker, worker bridge, staged importer,
converter output-root/ZIP checks, CMake integration, four focused tests and CI step.
No enhanced IPA, push, or build exists. Profile169checks andbridge19checks passed;
candidate transaction/actual-converter ZIP suites passed. Final repo rerun and
Apple/iPhone verification remain pending. Retain all tracked and untracked files.

P2 Build11 failed in the nested Morimura adapter; the pushed correction is in
Build12 run39269078016. Last API response queued; current completion is unknown.
Do not idle-poll builds. User will report completion. Retrieve full logs on resume.

Full independent handoff and exact next actions saved in the current session's
outputs/OPEN_NECTAR_CODEX_TO_CHATGPT_MASTER_HANDOFF.md and outputs/RESUME_HERE.txt,
and C:\Users\chazz\Documents\Open Nectar\2 - Progress and ChatGPT Handoff\
Copy This into ChatGPT.txt and 00 - RESUME HERE.txt.

Resume: preserve dirty edits, inspect/fetch Git, review integration, rerun actual
repo tests, inspect Build12 completed logs, then coordinate one verified push/build.
After build success prepare accessible IPA and phone test instructions. Separate
HD assets still need selecting/importing; none downloaded. Online iPhone co-op
with Raye for BOTH games is the final milestone, not implemented now.

## RESUMED — October19, 2026, ~16:30 Eastern

The user explicitly resumed work and said nothing had changed. The prior pause
is revoked. Starting HEAD/origin37020a74 and all previously dirty files were
verified intact; fetch found no competing remote changes.

P1: user-confirmed readable menu and working camera remain the hardware baseline.
Enhanced source/tests are now committed as
eec45217e4d1c601de2371d0dbd480f8746fc25b. They are NOT yet iOS-compiled or phone-tested.
Profile enables renderScale1, FXAA,4x anisotropy, subtle bloom, and existing QOL
actions once, preserving FPS/camera/other choices and backing up original config.
Native Files ZIP picker + worker completion + staging/backup/rollback installer
make existing texture/model loaders accessible. No external HD assets installed.
See ios/PIKMIN1_IOS_ENHANCEMENTS.md for exact choices, rollback and phone checklist.

All four suites reran against actual repo source in work/resume-verification:
169 profile checks,19 bridge checks, filesystem transaction/rollback suite and
actual-converter ZIP suite passed. First3 used MSVC17 /W4 /WX; converter/stb /W3.
All43 P2 adapter headers passed the existing audit. git diff --check passed.
Reviewed native picker cancellation, scoped copy lifetime, duplicate selection
and dismissing-presenter guards. Apple compilation/runtime remain unverified.
Phone-tested display/camera implementations and P2 source have no new changes.

Build12 run39269078016 is complete with workflow conclusion failure, but BOTH
jobs were cancelled before receiving any runner (runner_id0, empty step lists).
Exact annotation: "The job was not acquired by Runner of type hosted even after
multiple attempts"; notices cite ARM macOS capacity constraints. Empty logs ZIP,
no compiler errors or artifacts. Evidence in work/build12-jobs.json and
work/build12-annotations.json. Do not diagnose another P2 code failure from this run.

Experimental workflow now uses documented standard macos-15-intel host while
retaining explicit iphoneos ARM64 configuration. Package step verifies arm64
with lipo before producing IPA. Four P1 host suites run before full game compile.
Reference: https://docs.github.com/en/actions/reference/runners/github-hosted-runners
This is a capacity workaround, not an availability guarantee. No unrelated
workflow, account/security, signing or proprietary asset changes.

Next: commit workflow/docs with one [ios-build] marker, fetch/reconcile then push
both commits together, record exact run/commit, refresh accessible handoff, and
STOP idle polling as requested. P2's previous nested adapter fix still needs
actual Apple compiler validation. User action now: none; no candidate IPA exists.
On build completion retrieve actual logs/artifacts, prepare clearly named IPAs
in Documents/Open Nectar/1 - Install on iPhone and targeted phone instructions.
Online iPhone co-op with Raye for BOTH games remains the last milestone.

## Build13 dispatch checkpoint — October19, 2026, 16:29 Eastern

- User resumed work; no pause is active. STOP idle polling while this build runs,
  as the user requested. Await their completion report, then retrieve logs/results.
- Exact local and origin/ios-experimental HEAD: eddaf2adcaac1ebf1101ad2c5c4c8cfffc2b4238.
- Source/test commit eec45217e4d1c601de2371d0dbd480f8746fc25b plus workflow/docs
  commit eddaf2ad are both pushed. Git working tree was clean after push.
- Build13 run39319700760: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39319700760
  Initial observed status in_progress; no final compiler/IPA result established.
- P1 enhanced profile and native mod importer are in this build, NOT yet on the
  phone. No external HD texture/model payload installed. Preserve Build10 baseline.
- P2 includes the previously pending nested adapter fix; no new P2 code diagnosis
  because Build12 never received a runner. Build13 uses standard macos-15-intel,
  retains explicit iphoneos ARM64, and verifies executable architecture with lipo.
- All4 actual-repo host suites and43-header adapter audit passed before push.
  UIKit and full Apple compile/new runtime remain pending.
- Only this post-push status checkpoint is now uncommitted. All code/tests/workflow
  and prior documentation are committed/pushed. Avoid an extra build for this note.
- Next: after completion read exact jobs/logs; fix actual failures. For passing P1,
  retrieve/inspect IPA and place clearly named candidate + short test note in
  Documents/Open Nectar/1 - Install on iPhone. Alert user only when action is ready.

## Build13 result and P2 title diagnostic correction — October19, 16:46 Eastern

- Exact source eddaf2adcaac1ebf1101ad2c5c4c8cfffc2b4238;run39319700760 complete.
  P1 job118290256408 SUCCESS;P2 job118290256873 FAILURE. Standard Intel runner
  workaround acquired runners and compiled native ARM64 as intended.
- P1 all4 portable suites passed on macOS, including169profile/19bridge checks.
  Full Apple/Xcode compile,link,ARM64 verification and IPA packaging passed.
  This validates UIKit compilation,not native picker/runtime behavior on a phone.
- P1 artifact12220390882 retrieved,ZIP integrity/plist/ARM64 Mach-O verified.
  IPA2572685bytes,executable6357808bytes,bundleorg.opennectar.experimental.pikmin1,
  minimumOS15. SHA256 f266a387fc9f7d0f6a6db935b18245ddfa153f43de2531cf4cc1a2e8e08179fd.
  Copied/hash-verified as Documents/Open Nectar/1 - Install on iPhone/
  Pikmin 1 - Build 13 - QOL and Visual Enhancements.ipa with WHAT TO TEST.txt
  and Build 13 - IPA Verification.json. Audio alert played. Build10baseline retained.
- User asked to test menu/camera preservation,10-15min clarity/frame pacing/heat,
  QOL/Lock-On/Charge,touch interactions,picker cancel/reopen and setting persistence;
  saves/loading when convenient. Hardware result not yet reported. No HD asset
  payload is included. Signing/install via existing Sideloadly;preserve app data.
- P2 full logs downloaded to work/build13-logs.zip,extracted work/build13-full.
  Exactly TWO unique compiler errors,both titleSection.cpp:389:43/:72,one root:
  getCodeEnd/getCodeStart pointers cast to32bit int in a debug OSReport expression.
  No linker error reached. Prior incomplete Morimura/VsOtakaraName failures absent.
- Fixed games/pikmin2/pikmin2-decomp/src/sysGCU/titleSection.cpp::doUpdateMainTitle
  with std::uintptr_t markers/difference,guarded reversed markers,and matching
  unsigned-long-long/%llu output underPIKI_PC_PORT. Retail branch preserved.
  Native OSReport implementations usevprintf and support the format.
- Actual corrected statements extracted to work/resume-verification/
  pikmin2_title_diagnostic_test.cpp:6cases passed MSVC C++14 /W4 /WX,including
  addresses above4GiB,crossing4GiB,8GiB span,null and reversed markers.
  This is a narrow host semantic/compile check,not whole-P2/iOS validation.
  git diff --check passed. No P1 source or workflow change for this correction.
- Next:commit correction with this journal using[ios-build],fetch/reconcile,push
  one coordinated Build14,record ID,and STOP idle polling. Retrieve completed logs
  only when user reports done. P1Build13can be tested independently whileP2builds.

## Build14 dispatch checkpoint — October19, 2026, ~16:47 Eastern

Local/origin ios-experimental HEAD 36d0f156aa92f6bbedad91d3573bc1694bef131b;push succeeded.
Build14 run39322155722:https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39322155722
Initial status in_progress. STOP idle polling and await user completion report.
Includes P2 title diagnostic fix;P1 source exactly the successful enhancedBuild13.
P1Build13IPA is ready in the friendly install folder;await user hardware feedback.
No new Apple result for the P2 fix;no P2 IPA established. Only this post-push
status checkpoint is uncommitted;source/workflow/prior docs are committed/pushed.

## Build14 result / waypoint iterator fix — October 19, 2026, 17:14 Eastern

- Run39322155722 at36d0f156aa92f6bbedad91d3573bc1694bef131b completed:
  P1 job118298648192 SUCCESS; P2 job118298647821 FAILURE.
  P1 artifact12220854422; P2 failure-log artifact12221311918.
- P1 source is identical to the supplied enhanced Build13 IPA; no redundant IPA
  download/test requested. User has not yet reported its enhanced phone results.
  Readable menu/camera remain confirmed on the earlier phone-tested baseline.
- Full workflow logs retrieved to work/build14-logs.zip and work/build14-full.
  Exactly two unique compiler errors in plugProjectKandoU/routeMgr.cpp:
  line768:21 pointer-to-s16, line777:17 pointer-to-int. One root cause: pointer-
  shaped Container handles encode integer slots but are cast directly to narrow
  integers. No linker stage reached; previous title debug pointer errors absent.
- GameRouteMgr::get now decodes through std::intptr_t before intentionally
  narrowing to existing signed16-bit WayPoint ID; getNext increments pointer-width
  integer; getEnd encodes mCount via pointer-width integer. getStart zero is unchanged.
  Changes guarded by PIKI_PC_PORT; original retail bodies preserved. EditorRouteMgr
  uses actual node pointers and is unchanged. No new waypoint range or data layout.
- Actual four GameRouteMgr methods extracted into a host fixture and compiled/run
  with MSVC C++14 /W4 /WX. Passed traversals of0,1,8,32768points; -1-to-start;
  high handle above4GiB; crossing4GiB; fullu16 end-count encoding. All valid IDs
  select/order exactly their original slots; the high-handle checks do not dereference.
  Fixture: work/resume-verification/pikmin2_route_iterator_test.cpp; test-route.cmd.
  This is a narrow semantic check, not whole-game/iOS compilation or runtime proof.
- git diff --check passed. P1 source, iOS CMake and workflow are unchanged.
- Next: commit scoped route correction+journals with[ios-build],fetch/reconcile,
  push once and record Build15. STOP idle polling while GitHub compiles. Retrieve
  completed logs after user reports. Continue from real compiler/linker evidence.
- P1 additions explained to user: readable settings; sharper scene/FXAA/anisotropy/
  subtle bloom; Chain Actions, Hold to Pluck, Better Pathfinding, Idle Counter,
  Instant Whistle, Quick Grab, No Tripping, Cancel Throw withB, Throw While Moving,
  manual Lock-On/Charge; native Files ZIP importer with staged installs/backups;
  one-time config profile/backup preserving future choices. Camera preserved.
  External HD texture/model files and online co-op are not installed/implemented.
  Online with Raye for both iPhone games remains the final milestone.

## Build15 dispatch — October 19, 2026, 17:15 Eastern

Local/origin ios-experimental HEAD 31791d78ca32cca2ea88d6a21d87c03fcafb519f; push succeeded.
Build15 run39325940839: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39325940839
Initial status in_progress; final compiler/IPA results pending. STOP idle polling
and await user completion report. P1 source remains successful enhanced Build13;
no replacement download/test is needed. P2 includes tested waypoint handle fix.
Only this post-push status note is dirty. All source and prior journals pushed.

## P1 enhanced candidate feedback — October 19, 2026, 17:32 Eastern

User reports the enhanced P1 appears to fully work and looks a bit clearer.
Screenshot "Screenshot 2026-10-19 173104.png" shows Bloom Subtle, Texture Packs
0 installed and HD Models0/11files. This is expected: no external texture/model
payload has been installed. Clarity/effect changes use the original game assets.
Do not diagnose the accurate inventory as a UI bug or claim HD assets are hidden.
Record this as positive initial user runtime feedback, not full campaign or
per-feature verification. Specific charge, picker, save/load, sustained thermal/
performance and real asset import results have not been individually established.
No source/settings/app data changed in response. Next asset phase is actual mobile
texture/model file selection/import; online with Raye stays last. No build triggered
for this documentation. P2Build15result remains pending; do not idle-poll it.

## Build15 result / performance HUD / saving investigation — October19,17:48 Eastern

Build15 run39325940839 at31791d78ca32cca2ea88d6a21d87c03fcafb519f completed:
P1 job118311684052 success;P2 job118311683504 failure. Artifacts:P1 12223277348,
P2log12223476178. Existing enhanced Build13P1 remains the same source;no repeated
IPA download. Full logs savedwork/build15-logs.zip,work/build15-full;unique errors
work/build15-errors.txt. Previous route/title/adapter errors absent.

P2 has four fatal compiler errors in plugProjectKandoU/pelletMgr.cpp2890,2895,
2923,2928:PelletIterator decodes opaque pool-slot handles directly toint/u32.
Corrected native paths viaintptr_t/uintptr_t,including integer-to-handle encoding,
retaining boundedint mIndex,original unsigned32end comparisons and retail branches.
Actual6methods extracted/tested inwork/resume-verification/pikmin2_pellet_iterator_test.cpp,
test-pellet.cmd. MSVC C++14 /W4 /WX passed no-pool,leading/middle/trailing empty,
sparse active pools,ordered iteration,restart and end detection. No new data layout.
Full Apple/P2build and runtime remain pending.

User reports P1 looks clearer/appears to work and120FPS mode feels beautiful.
Record subjective feedback;actual render rate,thermal/memory headroom and sustained
behavior not measured yet. External HD texture/model payloads still not installed.

Added optional P1 iPhone Settings>Display>Performance HUD,defaultOff,persisted as
iosPerformanceHud;close settings to apply. It does not reset120FPS/user choices.
Measures completed SDL render submissions with monotonic timestamps (not physical
panel refresh),240-frame mean/p95/p99,app physical memory footprint,Mach task_info,
os_proc_available_memory advisory app headroom,process CPUtime fromgetrusage,
iOSthermalState andLowPower. CPU100%=onecore,can exceed100%. No GPUutilisation or
fake temperature/headroom-safe verdict. Native metrics/text refresh1Hz;fixed ring;
duplicate/invalid timestamps ignored;long suspension/backward clock resets history
and CPUbaseline. HUDoff performs no native sampling or per-frame clock reads.
Does not enable heavy per-draw profiling. Native Foundation/Mach code isolated in
nectar_ios_storage to avoidGameCubeBOOL conflicts. No renderer FBO binding changes.
30 actual-repo model/controller checks pass MSVC17 /W4 /WX;added P1CI host check.
One duplicate-timestamp/throttle defect caught by test was fixed before committing.
Full UIKit/Mach build and phone HUD layout/readings still require CI/hardware.

Saving investigated fromDayOverModeState,ogSave,MemoryCard::saveCurrentGame,
write/readCurrentGame,PlayerState::saveCard andnativecard saveRoot. Current behavior
is the normal end-of-day save/checkpoint flow. NO timed mid-day autosave/save-anywhere
is implemented. Existing serializer is not a complete live-world snapshot;do not
call it periodically and claim it restores mid-day enemies/Pikmin/clock/state.
No save routines,format,timing or user files modified. Expected ordinary card path:
Files>On My iPhone>Open Nectar Pikmin1>pikmin1>save>card0. Copy whole save folder
after completing save/closing app to back up checkpoints;retain appdata onupdate.
Normal save/close/relaunch/Continue still needs user verification. A proper mid-day
recovery/manual-save feature remains separate required future work,not completed.

Guide ios/PERFORMANCE_AND_SAVING.md copied to outputs andfriendlyfolder2 as
iPhone Performance and Saving Guide.txt. Explains readings/limits,120FPS8.33ms
budget,comparing representative10-15minute runs before adding mobilepacks,onepack
at a time,source references,and exact save/recovery limits. Public Apple APIs only.

Next:scoped commitsP2fix/P1diagnostics/docs,push once forBuild16,recordrun,and STOP
idle polling. After success prepare a clearly named candidate in friendlyfolder1
and ask user to enableHUD and report readings;then choose realHDassets. Continue
P2fromactual logs. Saving improvements andonlinewithRaye are not falsely marked done;
online forBOTHnativeiPhonegames remains the final milestone.

## Build16 dispatch — October19,2026,17:47 Eastern

Local/origin ios-experimental HEAD 01ea8330415171b9d8f61dbc89567ed5f5959c8e. Push succeeded;source clean atpush.
Includes4f3576c0(P2pellet casts),f9c08c55(optionalP1HUD),01ea8330(docs/buildmarker).
Build16 run39330204354:https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39330204354
Initial statusin_progress;final Apple compile/IPA outcomes unknown. STOP idle
polling;user reports completion. Only this post-push status note is dirty.
Current phone still uses enhancedBuild13;newHUD requires successfulBuild16IPA.
No actual HDassets,manual mid-day save or periodic autosave added. Save routines
and user save data unchanged. Saving/monitoring guide copied to friendlyfolder2.
Next:fetch completed logs;prepare successful P1HUDIPA in friendlyfolder1,test
Display>PerformanceHUDOn/closemenu,real readings andrender preservation;check
normal end-day save/close/relaunch;use measured readings before adding realpacks.
ContinueP2fromactual compiler/linker output. OnlinewithRaye remains last.

## Build16 result and broader P2 batch — 2026-10-19 18:18 Eastern Daylight Time

User explicitly wants bigger related batches, not smallest-safe-fix/build cycles.
Audit shared compatibility causes and related active source before pushing. Preserve
P1; do not hide errors or make unverified broad gameplay changes to appear faster.

Build16 run39330204354 at 01ea8330415171b9d8f61dbc89567ed5f5959c8e: P1 job118326155905 passed,
P2 job118326156146 failed. P1 artifact12225271604 contains the new HUD IPA;
P2 artifact12224648508 is logs, not a successful app. Full logs retrieved directly.
P2 has seven fatal diagnostics (six distinct error lines) in pcMovieInterp.cpp
container instantiations: five vector and two unordered container cases. Root cause:
forced adapter globally defines nullptr as integer0 on Apple, corrupting libc++
pointer forwarding. All are one shared cause, different from prior pellet/route casts.

Broader batch implemented, not yet Apple-compiled: exclude Apple from the legacy
nullptr macro, matching existing Android behavior; native CPlate and Stickers
get/getNext/getEnd decode/encode via intptr_t, preserving retail branches, fields,
and Stickers bounds assertion. No P1 game source changed. Opaque-index audit found
31 definitions; other narrow-cast matches inspected are comments or retail guards.
This is a targeted audit, not proof every legacy pointer assumption is eliminated.

tests/pikmin2_apple_nullptr_test.cpp checks the real adapter BEFORE affected STL
headers, keyword type and all seven container specializations. Local actual-header
Windows harness passes MSVC17 /W4 /WX; restores MSVC identity around the GCC-targeted
header and cannot validate Apple libc++. tests/pikmin2_container_handles_test.py
extracts all eight actual CPlate/Stickers methods and real bounds macro: MSVC17
/W4 /WX passes 0/1/100/110/10000 entries, ordered iteration, -1 sentinel, >4GiB next
handles, invalid and high-handle bounds rejection. Both run early on macOS in CI.
43-header adapter audit and git diff --check pass. Full iOS compilation remains pending.

P2 workflow now uses CMake Unix Makefiles + make -k to continue independent source
compiles after failures and expose a batch of errors. P1 retains verified Xcode.
Release/iphoneos/ARM64/iOS15/lipo verification and failure gating retained. Bounded
90-minute jobs. CMake officially supports Makefiles for iOS with explicit CPU/SDK;
this generator change still needs the actual Apple runner and may itself need repair.
tests/ios_build_error_summary.py writes distinct error index plus complete logs;
verified on the full Build16 log (six distinct lines from seven diagnostics).
No error suppression or success-on-failure added. GNU make -k does not guarantee
linker diagnostics until compilation succeeds; some dependent work cannot run.

P1 Build16 IPA ZIP/plist/ARM64 checked, 2575697 bytes; SHA256
02041fc3c82b757b6a0cfc62592bf855c8b6e4deca63ca4ba64eb0704747bec6.
Friendly copy verified in 1 - Install on iPhone/Pikmin 1 - Build 16 - Performance Display.ipa,
with WHAT TO TEST.txt. Hardware layout/readings remain pending. User previously
reports Build13 works, clearer and120FPS mode feels beautiful, not measured120FPS.
No external HD payload, mid-day autosave/manual recovery or online co-op added.
Normal end-day save/relaunch test still required. Online with Raye for both games last.

Next: commit scoped P2 source/tests, then workflow/journal with final [ios-build],
push once, record run ID, and STOP idle polling. User reports completion. Prepare
batch from full next run error index/logs; do not assume success before CI.

## Build17 batch dispatched — 2026-10-19 18:19 Eastern Daylight Time

Pushed once to ios-experimental. Local/origin HEAD 02ec11b866bbc39a21d6d5a8641a60790b3621d1.
Commits:5542499c (shared Apple nullptr plus CPlate/Stickers handles/tests),
02ec11b8 (P2 keep-going diagnostics, error index, journals and build marker).
Build17 run39334027043:https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39334027043
Initial queued, not compiled/packaged/runtime-verified. Stop idle polling; user
will report completion. Source/tests/workflow clean after push; only this dispatch
checkpoint in ios/OPEN_NECTAR_IOS_STATUS.md is dirty. No unexpected source changes.

P1 Build16 successful HUD IPA already copied/hash-verified to friendly folder1;
WHAT TO TEST.txt and verification JSON supplied; requested audio alert played.
Phone HUD/readings/normal save reload pending. No HD assets/autosave/co-op added.
Next agent action: when Build17 finishes retrieve full job logs and error index,
batch remaining related errors. Check generator/configure errors before compiler
diagnosis. P1 source unchanged from passed Build16; no redundant install needed
unless new evidence or source changes justify it. Online with Raye remains last.

## P1 Build16 phone HUD evidence and ProMotion opt-in — 2026-10-19 18:33 Eastern Daylight Time

User supplied a real gameplay screenshot from the new performance display, reporting
120FPS selected but very smooth gameplay. HUD visibly reports Render60.0 FPS,
average16.67ms, AppCPU40% (onecore=100%), HeatNominal, LowPowerOff. CPU40% does NOT
mean40%of all phone CPU capacity. No exact RAM/spare or frame-tail values transcribed
from the small screenshot; inspect original for those. This single snapshot validates
HUD display and live sampling during gameplay, not sustained thermals/memory/HD safety,
physicalpanel120Hz or save/reload. User has not reported a10-15minute comparison yet.

Investigated scheduler/high-rate and SDLUIKit presentation paths. Existing bundled
SDL_uikitviewcontroller.m:122-133 already creates a preferredFrameRateRange request
on >60Hz iPhone displays and explicitly requires Info.plist
CADisableMinimumFrameDurationOnPhone=true. Both source template and actual Build16
packaged IPA lack that key. Apple documents it is needed for faster iPhone ProMotion
timing hints. This is an identified configuration omission and leading explanation
for a steady60 cap; GPU saturation, OS settings or other pacing issues are not yet
excluded by hardware evidence. Do not promise120FPS from this declaration alone.

Implemented only the boolean opt-in in shared ios/Info.plist.in. Both games inherit
it when built; it permits higher rates rather than forcing120FPS or changing game
FPS configuration. Renderer, SDL framebuffer correction, camera, touch, saves and
game logic untouched. Local plistlib parse/configure for each game passes and dictionary
comparison confirms this is the sole metadata change; Build16 packaged absence verified.
No new tests added for a reversible one-key metadata fix. Actual Apple packaging and
phone60vs120 test pending. Retain user FPS preference, do not force hardware refresh.

Sources:
https://developer.apple.com/documentation/bundleresources/information-property-list/cadisableminimumframedurationonphone
https://developer.apple.com/documentation/quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays

Correction is UNCOMMITTED and NOT PUSHED, held for next coordinated batch after
Build17 so no redundant run is triggered. HEAD/origin remain02ec11b866bbc39a21d6d5a8641a60790b3621d1.
Dirty files:ios/Info.plist.in andios/OPEN_NECTAR_IOS_STATUS.md (includes dispatch note).
Build17run39334027043 uses the older plist and CANNOT validate this pending correction.
Do not ask user to reinstall Build17 expecting this fix. No build polling performed.
Next:retrieve Build17 full P2 result when user reports, batch related corrections,
include this plist change, verify generated IPA has boolean key, then ask user for
same-area120FPS HUD reading. If still60, inspect OS frame limit and actual render/pacing.
No HD payload installed, no mid-dayautosave/manualsave or online co-op implemented.

## Build17 full results, broad native-address batch, and 60FPS priority — 2026-10-19 21:45 Eastern Daylight Time

User explicitly cancels120FPS work: keep60FPS and budget for HD textures, all
supported optional character/model packs and associated compatible upstream content.
Removed ONLY our uncommitted ProMotion plist opt-in; Info.plist.in now matchesHEAD.
No P1 game source altered. Current phone still can show120selected while actual60;
user should choose Display>FPSMode60 once to match requested simulation/pacing mode.
P1 Build16 HUD confirmed live in earlier screenshot (60/16.67ms,CPU40%ofonecore,
HeatNominal,LowPowerOff); subjective smoothness positive. No sustained/HDheadroom proof.

Build17run39334027043/02ec11b8 completed: P1successjob118338903254,
P2failurejob118338902944. P1artifact12225988208 (same source as installedBuild16;
no redundant install). P2artifact12226262590 contains167591189byte complete rawlog
and26318byte error index. Downloaded directly. API logs have aggregatejobfiles
plusrunner-systemsubfolders; don't confuse system.txt with full build output.
New Makefiles keep-going configuration and Apple nullptr/container host checks PASS.

Full compilation exposes102 diagnostics:84 located pointer-width sites,11 linkage
conflicts,6 incomplete-model accesses,plus1 genPellet pointer diagnostic interleaved
into a register warning. These are a batch of earlier latent failures, not102 known
new regressions. No successful P2 link/IPA/runtime. Index/source contexts inwork/
build17-pikmin2,build17-errors.txt,build17-source-contexts.txt; concise copyoutputs/
Build17-P2-ERRORS.md. Important genPellet.cpp43 diagnostic recovered manually.

Broader source batch implemented, not Apple-compiled yet:
- P2Address/P2SignedAddress aliases use native uintptr_t/intptr_t;u32 file sizes,
  serialized offsets and packed DSP/sample fields stay32bit. Original console
  aliases stay32bit. Native class-layout comments remain originalconsole offsets.
- Widen actual RAM addresses end-to-end through ARQ/JKRAMCommand/JKRAramPcs/
  orderSync andcallback signatures;AI DMA setter/storage/getter;memoryarchive
  identities/constructor/cache lookup andcompoundarchive memorybase. Narrowing
  only at the original RAM API callsite would still truncate in receivers.
- Address arithmetic/alignment/hash/modeloffset/threadstack/checksum paths use
  full-width values first. Alignmentmask also pointer-sized for unsigned32alignment.
  Final bounded modelcounts explicitly narrowed after subtracting full addresses.
- Fontcache initialization writes typed mPrev/mNext pointers,notint[2] into64bit
  fields; handles emptycache; doesn't clobber glyph metadata.
- True32bit ARAMoffset/count values represented asvoid* usepc_p2_aram_offset,
  rejecting >UINT32_MAX rather than silently accepting a hostpointer. Wave/stream
  sources checked against their existing offset conventions (e.g. mDataOffset).
- Generator event base+alloverrides carryP2Address,includinghidden genPellet case;
  OSmessages/sentinels decoded with explicit width/wrap behavior;MapCode writes
  itsactualbyte directly;ARAMnode result is boolean success as consumed byMgr.
- Match11extern definitions orrenameprivateGXtable;includecompleteJ3DModel in
  J3DUMtxCache header for6memberaccesses. NativeDSP uses existing typed software
  tablehook instead of empty console DsetupTable with truncated addresses.
- Debugpointerformat uses%p;nativeheapchart usesrealroot start,not0x80000000.
  MatchingwideDMA diagnostic format. No hidden pointer-to-int warning suppression.

Verification: actual-header nullptr/STL test andactual8container-method suite pass
MSVC17/W4/WX. Newtests/pikmin2_native_addresses_test.py extracts actual aliases,
ARQ/AI signatures/fields/implementations,DMAdispatch,fontcache,MapCode,modeloffsets,
andheapchart intohostfixture. MSVC17/W4/WX passed highaddresses,callbackroundtrip,
32bitlength preservation,16unsignedalignmentcases,valid/rejectedARAMboundaries,
0/1/3/7fontpages+metadata,all256mapbytes,chartclamps andmodelcounts. Testfirstcaught
model-count narrowing warnings; explicit finalcounts corrected. A fixture-only
buffer allocation assumedmax_align_t16;Windows8 causedtestcrash;fixture corrected
toallocate bybytes. No claim that was a gamecrash or hardwarevalidation.
Reviewcaught remainingorderSync declaration src/destnames;fixed before finaltest.
Actual Apple complete compilation/link and first P2 runtime still pending.
Native DMA transfer stubs still only complete/store requests; no new DMAcopy engine
or claim that the game's unused legacy ARAM paths now work at runtime.

CI now runs newhostfixture early,retainsmake-k,adds onlyobsolete-register warning
silencing onAppleClang (huge167MBlognoise),prefersalready-installedgmake whenpresent,
andusesoutput-sync only ifselectedmakeadvertises it. No toolinstall/flags that
silence pointer truncation errors. One coordinated push after finalchecks.

Optional content request NOT completed yet: upstreamlauncher explicitly supplies
mobilePNGpack P1 id1870dA11T9FpuLQDnI3axoCJ_Eh5ptgWP (925049459bytes),P2
id1blzsLSFBr617h-gP7lvp_7HqsLRyQWzl (1072944206bytes). DesktopDDS variants exist
but mobilePNG is intended mobileinput. Siximportrows supported:OlimarHD,LouieP2,
LouieHD,PikminHD (3colors+3leafparts),Bulborb,Dwarf. AdditionalP2captains require
existingpc_hd_models_import_pikmin2 using privatepikis.szs (Louie/President/white/
purple/Bulbmin+portraits). No assets downloaded/installed yet in this checkpoint.
The Models Resource moved to models.spriters-resource.com;assetpages inspected
normally. Originaloldhost sometimes403,newofficial URLs work. Sources/inventory
andpackpreparation are next;keepall proprietaryassets outsideGit. Phone transfer/
activation andperformanceverification not yet done. Userauthorizedalloptionalcontent
does not mean claimunsupported models installed or enablesave-destructive modes.
No timedmid-dayautosave/manualsave oronlineco-op added. OnlinewithRaye remainsLAST.

## Build18 shared configuration failure and recovery — 2026-10-19 21:53 Eastern Daylight Time

Build18 run39355267175 at9d33219f43dd0cf69b645b7c74c8185a711967e6 failed
both games BEFORE game compilation. The shared configure step expanded an empty
CONFIGURE_ARGS array under set -u; the runner reported CONFIGURE_ARGS[@]: unbound
variable. This workflow mistake was introduced by Codex, not a new game-source
regression. No IPA was produced. P1 host profile/import/performance checks passed;
P2 adapter, Apple nullptr, container and new native-address host checks passed.
Full P2 compile/link/runtime is still unverified.

Recovery uses a non-empty complete CMake command array, appending the optional
already-installed gmake path only for P2. All iOS target arguments stay identical.
No P1 source or Info.plist edits; target remains60FPS. Both branches reviewed.
Local Apple SDK/shell validation unavailable; actual runner validation pending.
The earlier P2 batch is committed as ec702737; workflow/docs as9d33219f.
One recovery push will trigger Build19 with the same broad P2 source batch.
Optional-content preparation remains incomplete; one original Pikmin3 model ZIP
was downloaded to Downloads/302842.zip, not yet verified or installed. Mobile
PNG texture download returned an HTML confirmation page, not a verified pack.
Next: record recovery SHA/run, stop idle polling, prepare supported private
texture/character packages in Documents/Open Nectar/7 - Optional Graphics and Characters.

## Build19 reaches final P2 link; character bundle prepared — 2026-10-19 22:09 Eastern Daylight Time

Recovery0419685b02fd4da80cd91dcb83aa867fde09691c pushed; Build19run39355903504.
Configuration now succeeds for both. P1 host checks/configuration passed and compile
was in progress at last check (job118410485014). No P1 source changed.
P2job118410484796 compiled to100% then failed final arm64 link with ONE missing
symbol: thread-local wrapper routine for __GDCurrentDL. No compiler errors in
the complete127950929byte raw log. Artifact12236055046 downloaded directly into
session work/build19-pikmin2. Previous broad102-diagnostic batch now compiles.
No P2 IPA or phone runtime yet.

GDBase.c defines a constant-initialized C _Thread_local pointer; the legacy GD
header exposed it to C++ as thread_local, requesting a C++ initializer wrapper
not emitted by the C source on Apple. Both GD header copies now use Clang's
C TLS spelling in C++ as well, while retaining other-compiler/retail branches.
Thread isolation is preserved, not replaced by a process-global pointer.
Reference: https://clang.llvm.org/docs/LanguageExtensions.html (C11 _Thread_local
available with C semantics in all language modes). Actual Apple link still pending.

New tests/pikmin2_gd_tls_test.py extracts both actual declarations, real structure,
real inline writer and C storage definition into mixed C/C++ multi-unit link and
three-thread isolation check. Windows/MSVC check passed, using __declspec(thread)
for the C11 TLS spelling because MSVC lacks that C keyword. This does not validate
Clang's spelling or Apple ABI; the same fixture runs with actual C11+C++17 Clang
on macOS before full compilation. Error summary now includes actual missing symbol
names; checked against complete Build19 log and timestamped copy, excluding warnings.

Next push uses [ios-build] [ios-p2-only] to validate P2 without duplicating P1's
unchanged ongoing Build19 compile. Default marked pushes still build both. Matrix
selection uses standard Actions contains/fromJSON expressions. No idle polling.

All SIX supported public model ZIPs downloaded normally, CRC/SHA256 verified and
originals copied privately into Documents/Open Nectar/7 - Optional Graphics and
Characters/2 - Original Downloads. Upstream Python converter produced11 models.
Two source archives read-only extracted from owned GPVE01 ISO (pikis.szs354208bytes,
res_ground.szs189792bytes). Existing unmodified C++ importer produced5 extra-model
outputs including alternative Louie and3 portraits. Preserve the main Louie and
alternative separately; merge4 extra characters and3 portraits into ready bundle.

Ready PRIVATE bundle:1 - Ready for iPhone/Pikmin 1 - All Character Packs.zip
2813255bytes, SHA2567fa0bacc8f99349b0fd84d8b2a43716e91e68d033ca989c96a414a72dfc1538c.
20 entries:15 NHM models,3 portrait PNGs,2 small P2 source archives. Last2 are needed
by existing captain availability detection, under pikmin1/pikmin2/assets/. No full
P2 assets/game installed in P1. HD menu counter is11/11;4 extra-captain models are
separate. Binary headers,parts,bones,finite values,joint indices,texture sizes,
exact file boundaries,PNG decoding andZIP CRC passed locally. This is NOT phone
installation, visual validation or sustained performance proof. Target60FPS.
No save/config files included. Simple transfer guide and manifest beside bundle.

P1 official mobile texture source AND official1080p alternative both return
Google Drive QUOTA EXCEEDED HTML, not ZIP. No texture payload installed. Official
upstream releases mention this known quota scenario; no alternate official mirror
found in the focused source/release check. Do not pretend texture content present.
Optional mods already built into menus remain available; no forced difficulty,
cheats, randomizer or destructive mode changes. Mid-day saving and online withRaye
remain future work (online LAST). Phone transfer request pending; audio cue played.

## Dispatch/result checkpoint — 2026-10-19 22:12 Eastern Daylight Time

P1 Build19 SUCCESS, including unsigned IPA packaging; artifact12235976028. No
P1 game source changed; existing phone Build16 remains suitable for content tests.
P2 Build19 final-link failure above. Link fix committed/pushed06fdd716de120551fa4083d4043e6513144bd517.
Build20run39357443512 in progress at dispatch check; verified exactly ONE job,
build(pikmin2), so the P2-only matrix option works. No result/IPA confirmed yet.
https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39357443512
User postponed phone connection/transfer because busy. Do not keep requesting it.
Character bundle is prepared, NOT installed. No idle build polling; user will
report when done. These two final journal updates are intentionally uncommitted
documentation only, to include with the next source milestone without extra build.

## Build20 test-fixture dependency failure — 2026-10-19 22:14 Eastern Daylight Time

Build20run39357443512 at06fdd716de120551fa4083d4043e6513144bd517
failed job118415402674 in the early GD TLS smoke fixture, before game configure
or compilation. Generated gd-storage.c used the real GDBase.c NULL initializer
but fixture gd-0.h included stdint.h only, not stddef.h. Apple's C compiler
correctly reported undeclared NULL. Earlier Windows test passed because its
headers provided NULL transitively. This omission was Codex's test setup mistake,
not a newly observed game error. P1 did not run in Build20; Build19 P1 remains
SUCCESS with IPA artifact12235976028. Full Build20 job log saved work/build20-job.log.
Artifact12235768616 is only269bytes (no game compile log/IPA), not a P2 app.

Correction adds explicit standard stddef.h to generated fixture headers. No game
source, workflow, thread storage declaration, settings or save changes. Local
mixed C/C++ link and three-thread fixture will be regenerated/rechecked before
push; Apple ABI/link and full game build remain pending. One P2-only Build21
will validate the existing GD linkage correction after this dependency fix.
Preserve prior two pending journal appends and include them in this commit.
Character bundle remains ready privately; phone transfer explicitly postponed
by user; official texture downloads remain quota-blocked. No idle polling.

## Build21 FIRST successful P2 compilation/link; IPA metadata correction — 2026-10-19 22:37 Eastern Daylight Time

Build21run39357838317/sourcee4906f89/job118416685307 passed all Apple host tests,
including mixed C/C++ GD TLS link+three-thread test. FULL P2 iOS ARM64 target
pikmin2_pc COMPILED AND LINKED SUCCESSFULLY at100%. Error index0 compiler/linker
errors. This is a new confirmed milestone; not a runtime/IPA success yet.
The subsequent unsigned packaging step failed because CFBundleExecutable was
literal $(EXECUTABLE_NAME). Xcode expands that build-setting token for P1;
Makefiles does not. lipo attempted a nonexistent file named $(EXECUTABLE_NAME).
Actual built binary path was app/Nectar-pikmin2.app/Nectar-pikmin2.
Full job log:session work/build21-job.log. Artifact12236422070 contains logs/index
(3800110byte archive); no IPA or preserved executable in that artifact.

Fix shared bundle metadata at its source: CMake sets NECTAR_IOS_EXECUTABLE once
and uses it for OUTPUT_NAME and @ONLY-configured Info.plist CFBundleExecutable.
No fallback executable guessing or renaming. Labels, IDs and other plist fields
retain prior values. New ios/verify_bundle_info.py validates game-specific
identity/executable/name and rejects unresolved template tokens. CI calls it
immediately after CMake configure (fail before expensive compilation) and again
on the actual .app with a required nonempty binary before lipo/ZIP.
Local verification uses the installed real CMake to configure the actual template
for both games, compares every P1 configured field to the known working Build16
IPA, and checks placeholder/wrong-ID/missing/empty-binary rejection. Results will
be recorded after checks. No game source, savedata, graphics or controls edited.
Build22 will validate BOTH games because bundle metadata is shared, preserving
the working P1 output while producing P2's first IPA if packaging passes.
Character pack still ready privately; phone work postponed; HD textures quota
blocked; target60FPS, online withRayeLAST. Stop idle polling after dispatch.

## Build22 BOTH PASSED — first verified P2 IPA ready — 2026-10-19 23:07 Eastern Daylight Time

Run39359925649/sourcea16a3bae9f524ec4c2e4548a6ab5330a82031321:
P1job118423468727 SUCCESS andP2job118423468451 SUCCESS, including metadata
preflight,compilation,link,arm64/lipo and unsignedIPA packaging. P2artifact
12237930806 (7580578bytes);P1artifact12237826313 (2867471bytes). Both downloaded.
P2IPA3823331bytes,ARM64binary11064544bytes,SHA256
36976c498d943ad30b3dfe0290689638013a8fe8e5042ef0d370741c4cb94fd6.
P1IPA2575697bytes,ARM64binary6358656bytes,SHA256
2cb997dc570a1e7222e3e35d47acc614f13af4efd4556df251982d63fa559ac0.
Both ZIPCRC and exact app identity/executable passed; MachO load commands verify
iPhoneOS device platform,not simulator; linked libraries use system paths.
No code-signature command present,consistent with intentionally unsigned outputs.
No proprietary disc assets bundled. MinimumOS15.0. Hardware install/runtime for
these builds NOT verified. This is P2's FIRST successful IPA milestone.

User explicitly wants to leave working P1 app alone. Keep separate apps:
P1org.opennectar.experimental.pikmin1;P2org.opennectar.experimental.pikmin2.
No unified launcher/app migration. No P1phone update or content transfer now.
P2ready inDocuments/Open Nectar/1 - Install on iPhone/Pikmin 2 - Build 22 - First
iPhone Build.ipa. NewP1IPA retained in5 - Backups and Older Files/Build 22 - P1
Reference Only to avoid unnecessary reinstall. Existing P1Build16 remains working.

Prepared P2 assets privately from user's GPVE01ISO using unmodified upstream
gamecube_image.cpp+sha256.cpp,verifyWrites=true.2768 game files,1004985055bytes.
Every file read back and SHA256-compared by extractor; additional per-fileSHA256
manifest in3 - Game Files - Keep Private/Extracted for iPhone/Pikmin 2. Original
ISO opened read-only;SHA1before/after both63a68c656d654388e096d27a768e85823dcf3327.
Added the same .pikmin2-assets marker as upstream installer. No game data inGit.
Simple P2install/test guide and game-assets-folder shortcut in1 - Install on iPhone.
Phone transfer explicitly postponed by user; no repeated connection prompt.
Next: when ready,sign/install P2,open once/close,copyassets into separate P2app
Documents/pikmin2/assets,then verify startup/menu/graphics/audio/input/gameplay.
Do not claim runtime success from build/package checks. Optional P1models ready
privately but onhold;HDenvironmenttexturequota-blocked atlastattempt;60FPStarget;
mid-dayrecovery saving and onlinewithRaye remainfuture (onlineLAST).
This documentation-only checkpoint uses [skip ci] to avoid an extra build.

## P2 transfer completeness audit and missing touch-art correction — 2026-10-19 23:22 Eastern Daylight Time

User explicitly asked about missing Art after the earlier P1 experience. The
prepared P2 disc assets were complete, but the standalone touchscreen artwork
was omitted from the transfer folder. Codex corrected that preparation omission.
No phone operation, game-source edit or new IPA build is necessary for this fix.
Build22 source/IPA remains the verifieda16a3bae build. P1 untouched.

Independent audit reparsed current GPVE01ISO FST with the same UTF8/CP932 name
conversion as upstream and matched EVERY2768 file path,size,SHA256 to the prepared
assets and prior manifest,with zero missing/extra disc files (onlyupstreammarker).
Disc game payload1004985055bytes. Touch source references28unique PNG names.
Copied all26P2source PNGs plus shared lock_on.png andcharge.png from the P1source
art directory (not the phone);all28exact-source hashes and PNGdecodes passed.
All referencedtouchartnames covered. P2touch loader searches relative art/,not
Load/Art and not assets/art. Separate lowercase art folder now sits besideassets.

Audited8Yaz0/RARC UIarchives for exact requestedBTI/BFN entries: pauseglass,UFOdots,
repaymentbuttons,encyclopediabuttons,challengeselect,foreignfont,sprayicons and
portraitfaces. All requested entries present,including pikmin2main.bfn. P2's
fallbacksettingsfont is also compiled into pc_ui_font.h;no externalTTF needed.
Full result:privateP2folder/P2 Complete Transfer Verification.json andsession
work/p2-completeness-audit.json. Native loaders/source reviewed; caches/settings/
saves are generated at runtime,HDreplacement folders remain optional.

Correct transfer:copy BOTH assets AND art fromDocuments/Open Nectar/3 - Game
Files - Keep Private/Extracted for iPhone/Pikmin 2 into the separate P2app
Documents/pikmin2. Expectpikmin2/assets/user/... andpikmin2/art/bubble.png.
The existing game-files shortcut opens this parentfolder. START HERE andWHATTO
TEST guides corrected;previous instructions preserved in5/Instructions-Before
P2ArtAudit. No modifications to working P1app,settings,save orcontent.
Base-data/UI completeness verified onPC;phone transfer/runtime stillNOT tested.
OptionalHDtextures/models not part of basegamepayload,still not installed;last
textureattempt quota-blocked. Phoneworkonholduntiluserready. Docscheckpoint[skip ci].

## P2 startup crash investigation and allocator candidate - 2026-10-20 00:22 Eastern Daylight Time

The user installed Build22 P2 and reports immediate closure even after assets
and art transfer. P2 runtime is now confirmed FAILING; compilation/IPA success
does not imply startup success. The user connected/unlocked the phone, and Codex
read five existing P2 .ips reports without moving, deleting or synchronizing
device reports. Raw logs/device details remain private in the session workspace.
The three latest reports match the exact Build22 executable UUID
5af9412e-02a6-3446-96d4-90231accd8a5, also read from the archived IPA Mach-O.
They repeatedly show EXC_BAD_ACCESS / SIGBUS / EXC_ARM_DA_ALIGN on the main thread
about 0.24 seconds after launch. Stack: Metal compiler createConnections ->
AppleMetalGLRenderer first render pass -> glDrawArrays_ES2Exec ->
pc_gfx_flush_batch -> pc_gfx_p2_force_stretch -> JUTFader::draw.
Fault addresses have remainder 4 modulo 8 and lie inside P2's 480 MiB game arena.
This is an alignment exception, not evidence of an iOS out-of-memory kill.

Read-only VendDocuments access confirms Documents/pikmin2/assets, the asset
marker, the expected user directories, and Documents/pikmin2/art with all 28
expected PNG filenames; bubble.png is readable. This is a layout/presence check,
not a byte-for-byte rehash of the entire phone payload. The earlier PC audit
did compare all 2768 disc files with ISO paths/sizes/SHA256. No phone files changed.

Inspected JKRHeap.cpp: six global C++ new/new[] overloads routed objects into
the current JKR heap with only 4-byte/default or small explicit alignment.
This violates native fundamental object alignment. The existing host allocation
scope covered GXInit and present, but not the actual first pc_gfx_flush_batch
draw where Apple's driver lazily creates compiler objects. This is the leading
evidence-based explanation for the observed crash; phone retest is required.

Candidate implemented: native C++ new/new[] heap requests use at least
alignof(std::max_align_t). Preserve larger requested alignment, negative tail
allocation direction, explicit heap routing, malloc fallback, and delete routing.
Original non-PIKI_PC_PORT console policy and raw buffer allocation APIs unchanged.
Extend existing renderer host scope to 10 boundaries: batch submission, begin
frame, five overlay texture/draw functions, full-target dim, UI draw, and blur.
Driver work within these scopes allocates from malloc rather than section heaps.
No changes to P1 source, installed app, data, settings, saves, or optional content.

Files: games/pikmin2/pikmin2-decomp/src/JSystem/JKernel/JKRHeap.cpp;
games/pikmin2/pc_port/gl/pc_gfx.cpp; tests/pikmin2_native_allocator_test.py;
.github/workflows/ios-native-experimental.yml; these two journal documents.
The test extracts actual new/delete/policy/scope bodies, renames operators only
to avoid replacing the fixture CRT allocator, and stubs the game heap. It tests
alignment/routing/zero sizes/deallocation, positive/negative explicit alignment,
nested and exception scope restoration, and thread-local isolation. It also
checks host scope precedes executable statements at 11 renderer entries.
Local MSVC C++14 /W4 /WX: native 1344 checks PASS; console policy 1280 checks PASS.
Adapter self-include audit: 43 headers PASS. git diff --check PASS.
These are focused host regression checks, not a complete Windows/iOS game build
or a real driver execution. Apple CI runs both fixture variants before compiling
P2. New iOS compile/link/IPA/installation/runtime all pending for this candidate.

Build22 remains run39359925649/sourcea16a3bae; BOTH compiled, linked, and packaged.
New source push uses [ios-build] [ios-p2-only] so P1 is not rebuilt. Record exact
commit/run after dispatch; stop idle waiting. User watches Actions completion.
When successful, put new P2 IPA in Documents/Open Nectar/1 - Install on iPhone;
update the existing P2 installation while preserving its data (do not uninstall),
then test startup/menu/audio/touch/gameplay. If it still crashes, retrieve a fresh
P2 report, verify its executable UUID against the NEW IPA, compare exception/stack.
Do not assume subsequent failure has this same cause. Never reinstall P1 for this.

P1 remains user-confirmed working on the existing phone build: readable menu,
working camera/movement and reported smooth 60 FPS. Preserve UIKit framebuffer
fix. Optional character package prepared privately but NOT installed on phone;
environment texture download was quota blocked at last check. No timed mid-day
recovery save implemented. Online co-op with Raye remains the final long-term step.

## Startup candidate build dispatched - 2026-10-20 00:23 Eastern Daylight Time

Source commit: 609a45b184b50aeb1a71e581c2c2095f4f664f77
Actions Build23: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39369282124
Status at dispatch: in_progress. P2 only; P1 not scheduled. No new IPA or
hardware retest yet. Host tests: 1344 native + 1280 console checks passed.
The following journal-only checkpoint uses [skip ci], with no extra build.
No idle Actions polling. Retrieve result/logs after user reports completion.

## Build23 P2 startup candidate compiled and packaged - 2026-10-20 00:34 EDT

Verified actual Actions result SUCCESS. Run39369282124, job118453229169,
source 609a45b184b50aeb1a71e581c2c2095f4f664f77. P2-only job; no P1 build.
Apple adapter/standard-library/allocator/GD TLS checks passed, followed by
full iPhoneOS ARM64 compilation, linking, metadata validation and IPA packaging.
Artifact12241127170, archive7609098bytes. Retrieved build log/error index:
0 recognized compiler/linker errors, and actual job compilation/package SUCCESS.

Downloaded IPA: 3823426bytes; ARM64 executable11064832bytes; iPhoneOS device
platform; minimumOS15; exact P2 bundle/executable identity; ZIP CRC and all
Mach-O load-command boundaries PASS. Dynamic-library references are system
paths. Intentionally unsigned, no proprietary disc assets in IPA.
SHA256: 9389d36c43713794c2f0e5737c35b74e0ad8b6f32fcd54f1f5911242903a47c4
Executable UUID: cd97b20e-54c2-396d-9786-3535a215723d
This differs from crashed Build22 UUID5af9412e-02a6-3446-96d4-90231accd8a5.
New reports must match the new UUID after Sideloadly signing/repackaging;
verify the installed executable identity before drawing conclusions.

Copied and SHA256-verified to Documents/Open Nectar/1 - Install on iPhone/
Pikmin 2 - Build 23 - Startup Fix.ipa. Simple START HERE / WHAT TO TEST guides ready.
Moved only the old P2 Build22 IPA to folder5/Build 22 - P2 Startup Crash Reference,
verified unchanged hash; retained prior guides/history and logs. P1 untouched.
User should update existing P2 through Sideloadly with same signing identity,
preserve app data, reuse current phone assets/art, then test launch/title/menu.
No phone operation was performed during this build-result preparation.
Milestones: solution implemented, local checks passed, Apple compilation/link
passed, IPA generated and locally verified. New IPA installation/runtime NOT
verified; startup crash correction is still a candidate until phone evidence.
No further build needed now. This documentation-only checkpoint uses [skip ci].

## Build23 phone startup failure: audio-thread allocation batch - 2026-10-20 00:46 EDT

User updated P2 to Build23 and reports the same immediate-close symptom.
Retrieved fresh existing reports read-only after explicit connection/unlock.
Reports Nectar-pikmin2-2026-10-20-003826.ips and -003841.ips BOTH match Build23
UUIDcd97b20e-54c2-396d-9786-3535a215723d. They crash after about0.25-0.29seconds,
EXC_BAD_ACCESS/SIGBUS/EXC_ARM_DA_ALIGN on an AudioQueue thread (thread21), not
the previous main-thread Metal stack. Stack: AudioToolbox caulk concurrent
allocator -> tracking_allocator -> AQ::API::V2Impl::AllocateBuffer -> SDL
audioqueue_thread -> SDL_RunThread -> pthread. Faults are inside the480MiB JKR
arena; addresses are8-byte aligned but not16-byte aligned. No new phone files,
apps or settings were modified during diagnostic reads. P1 untouched.

Binary evidence: parsed actual Build22/23 Mach-O symbol/load-command data and
decoded MOVZ immediate arguments in ordinary new and new[]. Build22 passes4
in w2 to JKR do_alloc; Build23 passes8, not16. Thus the previous max_align_t
change under-corrected on iPhone ARM64. The Intel-host tests passed but did not
compile the fixture for the actual target. This was a Codex validation gap.
Clang's Apple max_align_t typedef is long double; Apple's ARM64 long double is
the same type format as double. Primary references:
https://clang.llvm.org/doxygen/____stddef__max__align__t_8h_source.html
https://developer.apple.com/documentation/xcode/writing-arm64-code-for-apple-platforms
The observed8-byte machine-code argument, not a host-type assumption, establishes
the actual Build23 behavior. Old graphics scopes did not transfer to SDL's
independently created AudioQueue thread. Its default global-new routing still
used the process-wide current JKR heap, risking native object lifetime/races too.

Related batch implemented:
- Native pc_object_alignment is constexpr and enforces max(16,max_align_t).
  Keep negative tail direction, larger explicit heap alignment, deletion routing,
  and original console behavior. Raw game buffer APIs unchanged.
- A thread-local game-allocation opt-in defaults FALSE on unknown native workers.
  JKRHeap::becomeCurrentHeap enables it on a game thread; pc_thread_entry scopes
  it around the actual emulated OS game callback, restoring on return/unwind.
  Native Apple/SDL threads therefore use malloc instead of the global game heap.
  This does not clear or replace the global heap pointer from a native thread.
- New pc_host_alloc.h contains noncopyable game/native host RAII scopes.
  Audio SinkLock scopes synchronous SDL/framework calls into host memory, with
  nested lock/scope restoration. beginSinkOpen and its worker explicitly use
  host allocation so the std::thread control block also avoids section heaps.
- Existing P2 graphics host scopes retained. No P1 changes or unified app.

Tests expanded from actual allocation/policy/becomeCurrentHeap/callback/scope/
audio-lock source. MSVC C++14 /W4 /WX: native1354 PASS; console1280 PASS;
Apple8-byte scalar-alignment emulation1354 PASS. Native worker default malloc,
game callback JKR opt-in, explicit heap selection, host override, exception
restoration, cross-thread isolation, audio scope nesting, and all six new forms
tested. Negative control removes16-byte floor and is rejected at compile time.
Adapter43-header audit PASS; git diff --check PASS. These are host fixtures.
CI adds Apple scalar emulation RUN plus xcrun iphoneos ARM64 C++14 syntax/static
assertion check before full game compile, catching the missed target ABI.
No local Apple SDK: actual target check/compile/link/IPA/phone retest pending.

Important source: JKRHeap.cpp; pc_host_alloc.h; dolphin_stubs/p2_os_host.cpp;
audio/jaudio_sink.cpp andjaudio_host.cpp; tests/pikmin2_native_allocator_test.py;
.github/workflows/ios-native-experimental.yml. New files contain no device IDs,
raw crash logs, credentials, assets or personal data. Raw reports remain local
in work/p2-phone-crashes and folder2/private phone report archive.

Build23 run39369282124/source609a45b1 remains compile/link/IPA SUCCESS but phone
startup FAILED. Its IPA is not a proven working app. Next P2-only build validates
this related allocation batch; no new candidate IPA or runtime evidence yet.
After success inspect new binary for16-byte w2 alignment and new UUID, prepare
verified IPA in folder1, update existing P2 with same signing identity/data,
test title/menu first. If failure, retrieve fresh matching report and diagnose
new exception/stack. Do not re-copy assets/art or touch P1 without evidence.
P1 remains existing working Build16,60FPS target; optional packs on hold; no
mid-day recovery save; online with Raye LAST. Stop idle waiting for Actions.

## Audio allocator batch dispatched - 2026-10-20 00:46 EDT

Build24: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39371370836
Exact source commit: 05e33f1c0e55dc11ecb6d413a8393bf73faeb2ce
Status at dispatch: in_progress. P2-only; P1 not scheduled. Host checks
native1354/console1280/Apple-scalar1354 pass; old8-byte-policy negative control
rejected. Real iPhone-target CI check/full compilation/IPA/runtime pending.
No idle polling. Record build result when user reports completion. Journal-only
dispatch checkpoint uses [skip ci] to avoid another build.

## Build24 P2 allocation/audio candidate SUCCESS; phone test ready - 2026-10-20 01:03 EDT

Run39371370836, job118459762543, exact source05e33f1c0e55dc11ecb6d413a8393bf73faeb2ce.
P2-only. Apple host tests, native/console/Apple-scalar allocator variants, and
the new actual iphoneos ARM64 C++14 compile/static-assert check all passed.
Full P2 iPhoneOS ARM64 compilation/link and unsigned IPA packaging succeeded.
Artifact12242386661, archive7585567bytes; compiler/linker index0 recognized errors.

IPA3824677bytes, executable11065224bytes. Verified ZIP CRC, exact P2 identity,
ARM64 Mach-O, iPhoneOS device platform, minimumOS15, load-command boundaries,
system dynamic-library paths, intentionally unsigned status, no disc assets.
SHA256 bacf33944221573fc1917de1311b5ddc328ce93b29977920f2ed7514259d9153
New executable UUID 21d95a32-9dfb-3bbb-bab8-4dd36cbc37d8
Inspected actual symbol/function instructions: ordinary new(__Znwm) and new[]
(__Znam) both pass16 in w2 to the JKR allocator. Build23 passed8 and Build22
passed4. This validates the actual target alignment correction in the produced
binary, independently of the host test. New phone crash must match new UUID;
old Build23 AudioQueue report is not evidence of this binary's failure.

Copied and hash-verified to Documents/Open Nectar/1 - Install on iPhone/
Pikmin 2 - Build 24 - Audio Startup Fix.ipa. Short START HERE/WHAT TO TEST guides updated.
Old Build23 P2 IPA/verification moved within the same project folder to folder5/
Build 23 - P2 Audio Startup Crash Reference, with unchanged SHA256. P1 untouched.

New candidate installation and startup/audio/gameplay remain UNVERIFIED.
User should update existing P2 through Sideloadly with the same identity,
preserving its data/assets/art; no asset recopy or P1 change. First test is
staying open/title/menu; then basic graphics/audio/touch/gameplay. If failure,
retrieve fresh report and confirm new UUID/exception/stack before another fix.
No phone app/file/settings operations were performed in build-result handling.
No active build or new source changes; journal checkpoint [skip ci], no extra CI.

## P2 menu clarity and original options input candidate - 2026-10-20 08:33 EDT

User resumed after shutdown. Verified origin/ios-experimental, fetched remote,
HEAD00bd0db831ce09d37c3da94e00ec5596e2256563, no divergence; only two paused
journal edits were pending and preserved. User confirms Build24 P2 OPENS on phone
and reaches menus. Main/title taps and Throw/A work. Two reported bugs: blurry,
small advanced menu; original game Options/exit-confirmation responds only to
bottom-left Back/X. Gameplay/audio/full-game stability not established by this.

Read the actual working P1 source and adapted its UI paths in P2 only:
- iPhone SDL high-DPI window flag, native-pixel menu targets independent of
  saved gameplay resolution/scale, frame-latched aspect at allocation/present.
- Keep the old logical-point gameplay pixel budget after enabling Retina;
  do not silently multiply gameplay GPU cost by3x in each dimension.
- Mobile400-high aspect-adapted menu with the same conservative iPhone margins
  as working P1; enable matching viewport/scissor and P2 DGX shim virtual sizes
  on iOS, including inverse taps. Captain-select4:3 exception remains.
- New read-only settings-open query; active game-menu touch lease also selects
  native UI rendering so original options/title/confirmation can be sharp.
  First/last transition follows the per-frame latch, not a mid-present switch.
  Font sampling remains existing linear; no texture/font replacement installed.

Original TOption had no direct touch handling. Added pane-based row selection,
explicit rumble/sound/volume/deflicker value taps through its original state,
animation/sound/saveRam handlers, virtual-stick navigation and visible familiar
Throw/A confirm. The disabled backing options never consume a modal's tap.
First Save row tap selects; second/explicit A confirms. No automatic save or
save/discard changes. JP/PAL-only hidden row0 remains unavailable in USA touch.
Confirmation already had select-then-confirm touch handling; retained that
behavior, exposed a context-only confirm control and let hit testing also use
visible row-container bounds when callback-owned text is hidden/replaced.
The row-container fallback is a source-supported candidate, not proven as the
sole cause on hardware. Expired/hidden tracked panes remain non-clickable.
Right-thumb camera gesture creation is suppressed only in these explicitly
claimed confirm menus so a slightly moving tap is not stolen by gameplay drag.
Other main-screen/gameplay button bindings remain unchanged; P1 source untouched.

Files: P2pc_window.cpp,gl/pc_gfx.cpp,settings/pc_settings.cpp/.h,touch/pc_touch.cpp/.h;
ebiScreenOption.cpp,ogMenuMgr.cpp,ogObjSMenuPauseVs.cpp; new
 tests/pikmin2_ios_menus_test.py; experimental workflow; both journals.
Build24 allocator/host-thread ownership and UIKit FBO/RBO corrections preserved.
No phone operations, signing/credential changes, assets or optional mods installed.

Local MSVC C++14 /W4 /WX actual-code fixtures: iPhone172 PASS; desktop182 PASS.
Covers native UI pixel budget vs gameplay, explicit aspect/resolution overrides,
frame latch/open-close transitions, layout and inverse taps across landscape/
portrait/fallback dimensions, confirm control lease expiration, direct option
selection/value ranges, disabled backing-menu ownership, row fallback, choice
select vs confirm, physical A/B and stale pane rejection. Host rendering/math
and state simulation only: not actual iPhone graphics/gesture verification.
Existing native allocator1354 and console1280 checks re-run PASS; adapter43 PASS.
Whitespace check PASS. CI adds iPhone/desktop host fixtures and actual iphoneos
ARM64 compile/static validation before full game compile. Apple full compile,
IPA and visual/touch hardware results for this candidate remain pending.

Next one coordinated P2-only build after committing; no P1 rebuild. Record exact
source/run; stop idle polling. On success verify IPA/identity/new UUID/alignment,
copy to folder1 and update test guide. Reinstall/update P2 only preserving data;
no asset/art recopy. Phone tests: menu readability/tabs/scroll/tap alignment,
original options rows/values/save, Continue/Don't Save selection and confirm,
Back, main-title controls, startup/gameplay/audio/camera regression. Preserve
Build24 known-opening IPA in archive. No new visual/touch fix may be called
confirmed until user reports actual phone behavior.

## P2 menu candidate dispatched - 2026-10-20 08:34 EDT

Source commit 3013d4c23035db25ba17851fe65cd2e29123830d
Build25: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39423349538
Status at dispatch: in_progress. P2 only. New Apple target/full compilation,
IPA, menu clarity and original-options touch on phone remain pending.
Local UI172/desktop182/allocator1354/console1280/adapter43 checks passed.
No idle Actions polling. Dispatch journal checkpoint [skip ci], no extra build.

## Build25 early fixture failure corrected - 2026-10-20 08:42 EDT

Build25 run39423349538, source3013d4c23035db25ba17851fe65cd2e29123830d,
job118629595502 FAILED in the new native menu test before game configure/compile.
Full job log retrieved directly: work/build25-job.log in the development session;
friendly copy: Documents/Open Nectar/2 - Progress and ChatGPT Handoff/Build 25 - Full Failed Job Log.txt.
Unique diagnostics: Clang unused-const-variable for kF1TabH, kF1OptH,
kF1OptVisible, promoted to errors by -Werror. These were imported real source
constants unused by the extracted fixture, although used by the full game.
Existing adapter/Apple library, native+console+Apple-scalar allocator, ARM64
allocator syntax and GD TLS checks PASSED. No game compile/link or IPA occurred.
This failure is not evidence of a new phone crash or a failure of menu visuals.

Correction limited to tests/pikmin2_ios_menus_test.py: meaningful geometry checks
exercise the imported metrics, checking tab/list separation and room for the
option rows in each tested layout. No warning suppressions or weakened CI.
MSVC C++14 /W4 /WX: iPhone180 and desktop190 PASS. Installed LLVM19 Clang parser
(clang-tidy with clang-diagnostic-* and warnings-as-errors) reproduced ALL THREE
original diagnostics before correction, then accepted both corrected variants.
Clang parser on Windows is not the Apple SDK/full iOS game build. The new Apple
CI/full compile and phone menu tests remain required. git diff --check passed.
No further game source, P1 app/data, startup allocator, framebuffer, assets or
signing changes. Build25 menu/source candidate remains3013d4c2, now with this
fixture correction for one P2-only retry. Do not install/retest Build24 for this
new candidate; retain its known-opening IPA until a new IPA succeeds.

P2 underlying menu findings remain: missing iOS high-DPI/native-resolution menu
path and Android-only mobile layout/shim versus working P1; original TOption
missing direct touch and game-menu confirm control not exposed. Visible row
fallback addresses potentially hidden callback text. Main/title taps and Throw/A
worked in user tests. The source candidate is implemented, NOT phone verified.

Next: commit corrected fixture and this checkpoint, push one P2-only build,
record source/run, stop idle polling. On success validate IPA and put it in
folder1 with short phone checklist. Reinstall P2 only preserving app data; no
asset/art recopy. Test clear advanced settings and tap alignment, original
options values/save, Continue/Don't Save select/confirm, A/Back, then gameplay,
audio/camera regression. Preserve P1. User involvement: none until IPA ready.

## Corrected P2 menu fixture retry dispatched - 2026-10-20 08:43 EDT

Build26, run39424440094, sourcedd5bd01557ea7f57255f869d431cd81864bca567.
https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39424440094
Status at dispatch: in_progress. P2 only, no new P1 build.
Includes menu source3013d4c2 plus the Build25 unused-constant fixture correction.
Local MSVC iPhone180/desktop190 and Clang parser both variants PASS.
Apple/full-game compilation, new IPA and phone menu behavior remain pending.
Build25 failed early test, no IPA. Build24 remains the known-opening phone build.
No idle polling; user will report completion. Dispatch documentation uses [skip ci].

## Build26 PASSED; P2 menu test IPA ready - 2026-10-20 09:19 EDT

P2-only source dd5bd01557ea7f57255f869d431cd81864bca567; run39424440094;
job118633289923; artifact12266336380. All job steps passed, including native
menu180/desktop190 host checks, actual iPhone ARM64 syntax check, existing
allocator/address/TLS checks, full game configure/compile/link and IPA packaging.
Build25's three unused fixture constant diagnostics corrected; no warnings disabled.

Downloaded artifact ZIP digest verified against GitHub metadata:
555eb99487ec310e9c9ffb795ade822fca5f9bea5f36c521653347922aa6aaac.
IPA ZIP integrity, single P2 bundle identity, ARM64 iPhoneOS device executable,
minimum iOS15, system-library load commands and unsigned state verified.
Fresh UUID0bd204c6-8a62-35ed-82e6-4ef2cfc76b14, executable11065512bytes.
Actual new/new[] ARM64 routines both still request16-byte alignment.
IPA3826605bytes SHA256ca28fbc6f423745e2babb595d1b47fac4a1222917b00c0ea61f24d23ad0325e5.
No proprietary ISO/RVZ/model/archive game assets embedded in IPA.
Copied with matching hash to Documents/Open Nectar/1 - Install on iPhone/
Pikmin 2 - Build 26 - Clear Menus and Touch.ipa, alongside verification JSON,
updated START HERE/WHAT TO TEST guide and build link. Build24 preserved.
Full successful job log in friendly folder2; full reports refreshed.

Milestones: source implemented YES; local checks YES; Apple compilation YES;
IPA YES; Build26 phone installation/runtime/menu clarity/touch verification NO.
Build24 remains last hardware-confirmed opening build. No phone operations,
P1 changes, assets/art recopy, signing changes or new build. Docs commit skip-ci.
Next user test: update existing P2 in Sideloadly with same account/ID, do not
uninstall. Check advanced clarity/tabs/scroll/tap mapping; original options
rows/values/Save; Continue/Don't Save select then confirm, visible A and Back;
then title/gameplay/audio/camera regression. No need to connect phone to Codex
unless a fresh crash report is needed. Do not call new menu bugs fixed until
actual user feedback. Wait for phone results without idle usage.

## Build26 hardware regressions and coordinated P2 fix - 2026-10-20 09:37 EDT

User Build26 phone test: title initially blurred with gameplay controls;
then sharpens and shows only Back/X, blocking advanced settings gear. Begin
campaign intermittent; third attempt entered gameplay. Pressing top-left pause
crashed. Ignore logo/flower layout differences in screenshots (opening animation).

Both fresh crashes match Build26 UUID0bd204c6-8a62-35ed-82e6-4ef2cfc76b14.
09:22:04 main thread: SIGABRT in AppleMetalGLRenderer clearBuffers -> pc_gfx_clear_depth
 -> pc_p2_captain_preview_begin -> pc_captain_select_draw_3d -> VIWaitForRetrace.
09:24:55 Metal CompletionQueueDispatch: SIGABRT OSPanic -> JKRExpHeap::joinTwoBlocks
 -> do_free -> operator delete -> AGX ResourceGroupUsage/command-buffer dealloc.
Confirms native Metal destruction reached the game heap. Likely source: missing
host routing during native graphics allocations; specific allocation site for
completion failure cannot be proven from its free-only crash stack alone.
Depth clear and numerous GL calls were unguarded; P2 VIWaitForRetrace also called
SDL_GL_SwapWindow outside pc_gfx_present's host guard. Existing native worker
thread defaults and16-byte alignment did not cover native calls on game thread.
09:20 Jetsam report contained no P2 process; no evidence it explains these crashes.
Phone settings read-only: renderScale=.666667, logical932x430, fpsMode0.
Raw reports/config are private local evidence, not committed to public repository.

Controls: title claimed touch only in interactive Wait; once it did, the menu
filter admitted Back plus help-requested buttons and explicit confirm contexts.
Title has no help icons, so gear/A disappeared at the same point native menus
became sharp. Small right-half taps could become camera gestures in generic
menus, cancelling clicks. Source supports this explanation; runtime fixes pending.

P2-only batch: restoring host-allocation scope at the beginning of all100
parsed direct-GL functions in pc_gfx.cpp (86 entries added/moved; two old inline
scope implementations unified). Includes clear depth, copy/held-frame/texture
upload/state/present helpers. Native SDL window init/swap/interval/shutdown and
narrow event-pump helper guarded. P2 VIWaitForRetrace's independent swap block
host-scoped. Preserve16-byte allocator policy, game-thread ownership, UIKit
FBO/RBO and native menu/point-budget frame latch. No JKR heap bypass for game
objects, no history rewrite, no P1 changes.

Menu filter retains Back, gear/settings and A for any active game-menu lease;
other gameplay controls still require visible context/help. Existing exclusive
modal input guards still block advanced-menu opening over their ownership.
No gameplay camera gesture begins while ANY game menu owns touch; existing
menu swipe/port scroll handlers retained. Title claims menu in OpenScreen and
Draw, not just Wait, to avoid delayed animated-title resolution/control switch.
One frame of render-context transition can still occur; no zero-flicker hardware claim.

Tests: new direct-GL scope audit (100 entries) integrated into existing allocator
fixture generation; negative control removing clear-depth guard rejected.
Actual clear-depth implementation exercised with lazy native allocations and
completion-thread frees, including nested scope restoration; native1359 and
console1280 MSVC checks PASS. Menu188/iPhone,198/desktop PASS including actual
button hitboxes for gear/A after generic menu ownership. Clang19 parser checks
for both menus and native/console/Apple-scalar allocator PASS. Includes static
checks for native SDL entry scopes, independent VI swap, title opening/drawing.
These are host mocks/parsing, not Apple graphics execution. Apple ARM64 target
compile, full game build/new IPA, phone regressions remain pending.

Candidate:not committed; not dispatched

No idle polling. Next action after successful IPA: update P2 only, preserve data,
repeat Begin selection several times, check gear/A before/during/after title
opening, advanced/original options, enter gameplay then pause/resume repeatedly.
If crash, read fresh UUID-matched report. P1 and assets/art unchanged.

## Build26 hardware regressions and coordinated P2 fix - 2026-10-20 09:38 EDT

User Build26 phone test: title initially blurred with gameplay controls;
then sharpens and shows only Back/X, blocking advanced settings gear. Begin
campaign intermittent; third attempt entered gameplay. Pressing top-left pause
crashed. Ignore logo/flower layout differences in screenshots (opening animation).

Both fresh crashes match Build26 UUID0bd204c6-8a62-35ed-82e6-4ef2cfc76b14.
09:22:04 main thread: SIGABRT in AppleMetalGLRenderer clearBuffers -> pc_gfx_clear_depth
 -> pc_p2_captain_preview_begin -> pc_captain_select_draw_3d -> VIWaitForRetrace.
09:24:55 Metal CompletionQueueDispatch: SIGABRT OSPanic -> JKRExpHeap::joinTwoBlocks
 -> do_free -> operator delete -> AGX ResourceGroupUsage/command-buffer dealloc.
Confirms native Metal destruction reached the game heap. Likely source: missing
host routing during native graphics allocations; specific allocation site for
completion failure cannot be proven from its free-only crash stack alone.
Depth clear and numerous GL calls were unguarded; P2 VIWaitForRetrace also called
SDL_GL_SwapWindow outside pc_gfx_present's host guard. Existing native worker
thread defaults and16-byte alignment did not cover native calls on game thread.
09:20 Jetsam report contained no P2 process; no evidence it explains these crashes.
Phone settings read-only: renderScale=.666667, logical932x430, fpsMode0.
Raw reports/config are private local evidence, not committed to public repository.

Controls: title claimed touch only in interactive Wait; once it did, the menu
filter admitted Back plus help-requested buttons and explicit confirm contexts.
Title has no help icons, so gear/A disappeared at the same point native menus
became sharp. Small right-half taps could become camera gestures in generic
menus, cancelling clicks. Source supports this explanation; runtime fixes pending.

P2-only batch: restoring host-allocation scope at the beginning of all100
parsed direct-GL functions in pc_gfx.cpp (86 entries added/moved; two old inline
scope implementations unified). Includes clear depth, copy/held-frame/texture
upload/state/present helpers. Native SDL window init/swap/interval/shutdown and
narrow event-pump helper guarded. P2 VIWaitForRetrace's independent swap block
host-scoped. Preserve16-byte allocator policy, game-thread ownership, UIKit
FBO/RBO and native menu/point-budget frame latch. No JKR heap bypass for game
objects, no history rewrite, no P1 changes.

Menu filter retains Back, gear/settings and A for any active game-menu lease;
other gameplay controls still require visible context/help. Existing exclusive
modal input guards still block advanced-menu opening over their ownership.
No gameplay camera gesture begins while ANY game menu owns touch; existing
menu swipe/port scroll handlers retained. Title claims menu in OpenScreen and
Draw, not just Wait, to avoid delayed animated-title resolution/control switch.
One frame of render-context transition can still occur; no zero-flicker hardware claim.

Tests: new direct-GL scope audit (100 entries) integrated into existing allocator
fixture generation; negative control removing clear-depth guard rejected.
Actual clear-depth implementation exercised with lazy native allocations and
completion-thread frees, including nested scope restoration; native1359 and
console1280 MSVC checks PASS. Menu188/iPhone,198/desktop PASS including actual
button hitboxes for gear/A after generic menu ownership. Clang19 parser checks
for both menus and native/console/Apple-scalar allocator PASS. Includes static
checks for native SDL entry scopes, independent VI swap, title opening/drawing.
These are host mocks/parsing, not Apple graphics execution. Apple ARM64 target
compile, full game build/new IPA, phone regressions remain pending.

Candidate:8d77c5337863f34800bc7b7ef990878e586d7c48; Build27/run39432157516 (in_progress at dispatch)
https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39432157516
No idle polling. Next action after successful IPA: update P2 only, preserve data,
repeat Begin selection several times, check gear/A before/during/after title
opening, advanced/original options, enter gameplay then pause/resume repeatedly.
If crash, read fresh UUID-matched report. P1 and assets/art unchanged.

## P1 optional character/model bundle INSTALLED by USB - 2026-10-20 09:52 EDT

User explicitly authorized installation; ZIP already present in P1 Documents.
Verified no running P1 process before backup, staging and promotion and after
installation. Phone ZIP SHA2567fa0bacc8f99349b0fd84d8b2a43716e91e68d033ca989c96a414a72dfc1538c,
matching prepared local bundle. ZIP integrity/path/type/size/model magic checked.
Backed up6 existing files/161965bytes: saves/card0+card1, config, original enhanced
config backup, touch layout and achievements. Existing Load Models folder empty;
no prior model files overwritten. Backup SHA256 validated locally and against
phone readback before changes. Full backup/private install manifest in:
C:\Users\chazz\Documents\Open Nectar\5 - Archives\Before P1 Character Packs - 2026-10-20 095114

Staged20 files/18360060bytes outside active Load, verified each SHA256, then
renamed only into absent destinations. No differing existing file overwritten.
Final readback SHA256 of all20 installed files PASS. All6 pre-existing protected
files remained byte-for-byte unchanged; P1 kept closed throughout. Original ZIP
preserved on phone. Recovery record retained in P1 Documents. No P2 writes,
reinstall, app signing, code or settings changes.

Content installed:15 NHM files comprising11 menu-counted HD models plus4 extra
captain choices,4 portraits and1 private source archive for existing character
recognition. HD Olimar, standard/HD Louie alternatives; red/yellow/blue Pikmin
and leaf/bud/flower; Bulborb/Dwarf Bulborb; President/White/Purple/Bulbmin extra
captains. Native loader expected11/11 counter. Read config hdModelsDisabled=0
(all model rows enabled). Do not confuse file-install verification with runtime
visual/animation/performance verification: game not launched by Codex.
Environment HD texture pack remains NOT installed (last official quota block).
P1 installed app/build and60FPS preference preserved. P2 Build27 still pending
at last dispatch; no polling/new build for this content milestone.

Next user action: reopen P1, Graphics > HD Models should show11/11, inspect
Olimar/Pikmin/Bulborbs and extra captain selector, play15-20 minutes while
watching FPS/Heat/RAM. Keep60FPS. If artifacts or slowdowns, disable affected
model rows, restart and report exact model/symptom; original game assets remain.
No further file copy or ZIP import needed. Full private record in folder2/
Pikmin 1 - Character Pack Installation.json; backup under folder5 above.

## Build27 PASSED; verified P2 crash/menu candidate IPA ready - 2026-10-20 09:57 EDT

Source8d77c5337863f34800bc7b7ef990878e586d7c48; run39432157516;
job118659675153; artifact12268693334. P2 only. All workflow steps PASS,
including100 direct-GL scope audit, native1359/console1280/Apple-scalar1359,
menu188/desktop198, actual iPhone ARM64 syntax checks, existing addresses/TLS
checks, full game compile/link and IPA packaging. No new source modifications.

Downloaded artifact ZIP digest matches GitHub metadata:
cc60012d8279edf3049dc17cddf83bb8fc7829ec8958dbc73c974a8e87020bdf.
IPA ZIP/ARM64/iPhoneOS device/min iOS15/P2 bundle/system-library loads/unsigned
state verified. Fresh UUIDaecbcead-f044-3dc2-9608-83e40dcd9540; executable11083680bytes.
Actual ARM64 new/new[] still request16-byte alignment. IPA3831561bytes,
SHA256f4a90d7da9f3b6130116caaf006b220f27b7e3a4ec17deb97b404222e0ab6b74. No ISO/RVZ/SZS/BMD game payload in IPA.
Hash-identical copy now in Documents/Open Nectar/1 - Install on iPhone/
Pikmin 2 - Build 27 - Crash and Menu Controls Fix.ipa. Verification JSON, build shortcut and simple START HERE guide
updated; folder2 full successful log and master handoff updated.

The batch targets Build26's actual phone failures: clear-depth captain-preview
abort and Metal completion-thread JKRExpHeap abort; title menu gear/A hidden
when touch ownership started, right-side menu taps lost as camera gestures.
Source fixes and tests passed; Build27 PHONE INSTALLATION/CRASH-FREEDOM/MENU
BEHAVIOR ARE NOT YET VERIFIED. Preserve Build24 allocator/thread/audio fixes,
UIKit display FBO/RBO, logical-point gameplay rendering budget and frame latch.

Next phone test: update P2 over existing app using same Sideloadly signing
account/ID; no uninstall or assets/art recopy. Check gear/A during/after title
animation, advanced settings; repeat Begin/captain selection; enter actual game
and repeat pause/resume; original Options/choice confirmation; audio/camera.
If crash, match fresh report to new UUID above. No idle polling/new build.
P1 unchanged in this result turn; its character bundle was actually installed
previously (20files/15NHM readback verified,6 protected saves/settings unchanged),
expected menu11/11; model visuals/performance still untested, environment textures
NOT installed. Keep60FPS. All private assets/backups remain outside Git.

## P2 enhancement batch locally verified - 2026-10-20 13:41 EDT

User resumed after the usage pause; no external source changes were reported.
Fetched local/remote baseline aa59864e3be6c8a6e5d9a7b4ca130861ed861e27 matches.
Build27/run39432157516/source8d77c5337863f34800bc7b7ef990878e586d7c48 passed;
user now reports P2 working so far with no crashes, with incomplete testing.
This supersedes earlier blanket Build27 phone-result-pending notes. It is not
proof of full campaign stability or of the new enhancements below.

P2 candidate:
- One-time backed-up/atomic config profile: renderScale1.0, FXAA, anisotropy4,
  subtle bloom; 60FPS; performance HUD initially on; hold-to-pluck, better
  pathfinding, idle counter, instant whistle, quick grab, no-trip, B throw
  cancellation, manual lock-on and charge. Existing active texture selection,
  saves, touch layout and unrelated settings survive. The profile marker is
  serialized; later menu choices survive restarts. Reset preserves that marker
  while resetting actual settings, so the preset does not silently reapply.
- chainActions and throwWhileMoving are also compatible profile keys, but the
  active P2 decomp does not consume these two getters. P2 already invokes nearby
  AI work on completion and calls control during throw states; no new AI hooks
  were added. Do not advertise either key as a newly implemented P2 mechanic.
- Performance HUD in Display: render submissions FPS, average/p95/p99 frame
  times, process RAM, advisory available memory, process CPU (100%=one core),
  categorical thermal state and Low Power. It measures actual SDL swaps,
  samples OS counters once/second, and skips sampling when disabled. It hides
  during advanced settings/captain selection. No GPU percentage or temperature.
- Native Files ZIP picker for P2 texture packs. Reuses the existing bounded,
  CRC-checked P1 extractor and staged transactional install/rollback code.
  CMake removes the old P2 converter source to prevent duplicate symbols.
  UIKit callbacks/bridge/worker have restoring native allocation scopes; the
  P2 game allocator and recent GL100/SDL/thread/audio protections remain intact.
  P1-specific model kinds are rejected for P2. P1 game source not changed;
  shared picker changes are gated, with P1 regression coverage.
- Workflow adds P2 profile/HUD/bridge/ZIP/rollback and actual CMake-wiring/reset
  checks before compiling. Only P2 will build via [ios-p2-only].

Source files: ios/pikmin2_ios_profile.h; ios/ios_storage.mm (P2 atomic config);
ios/CMakeLists.txt (P2 features and shared portable sources); ios/ios_mod_picker.mm;
ios/pc_ios_mod_bridge.cpp; games/pikmin2/pc_port/settings/pc_settings.cpp/.h;
games/pikmin2/pc_port/dolphin_stubs/p2_os_host.cpp. New tests: pikmin2_ios_profile_test.cpp,
pikmin2_ios_mod_bridge_test.cpp, pikmin2_ios_enhancements_test.py.

Local checks PASS: profile188; shared HUD30 with P2 includes; P2 bridge24;
P1 bridge19 and profile169; transactional install/backup/active-pack protection/
invalid data/rollback; real ZIP stored/deflate/CRC/paths/duplicate/failure tests;
actual reset execution; actual extracted CMake feature branches configure for
P1 and P2. Existing actual allocator native1359/console1280/Apple-scalar1359;
GL audit100; iOS menu188/desktop198; Clang parser for allocator three variants,
menu two variants, new profile/bridge/reset all passed. Local Windows compiler
checks do not compile UIKit or establish Apple ARM64 linking/runtime behavior.

P1 content update: user installed texture ZIP and screenshot lists GPI Inactive,
Loader off. Advised select GPI/A to activate, accept restart/full restart.
Activation/texture replacements/FPS/heat after activation not yet confirmed.
Previously installed character bundle:20 files/15NHM/4portraits/source archive,
readback SHA256 verified;6 preexisting save/settings/layout/achievement files
unchanged; backup in folder5/Before P1 Character Packs -2026-10-20 095114.
Model visual correctness remains unverified. P1 gameplay/menu/camera/audio
remain user-confirmed; no P1 app/data operations in this enhancement turn.
P1 texture ZIP SHA256 5d9254b4f1ca46fee93b57ce17e888521884634bc1fae4bc7a4cf22af7e2551b;
previous no-threat Defender plus full ZIP/PNG structural check is not a runtime
or absolute security guarantee. Keep60FPS; 120 canceled; online co-op remains last.

P2 needs its own compatible texture pack (upstream launcher Drive ID
1blzsLSFBr617h-gP7lvp_7HqsLRyQWzl, advertised1072944206bytes, folderGPV).
No P2 HD texture/model content downloaded or installed in this batch; importer
support and graphics defaults are separate from content installation. P1 GPI
pack/models cannot be treated as installed P2 content. No automatic phone changes.

NEXT: commit/push this coordinated P2-only candidate; record exact source/run;
stop idle polling per user. Once user reports completion, retrieve job/logs,
verify IPA ZIP/plist/ARM64/UUID/alignment/digest and copy to friendly folder1.
Retain Build27 working backup. Update existing P2 via same signing identity/ID;
do not uninstall or touch P1. Hardware test: title gear/A; repeat Begin and
captain selection; pause/resume; original Options; HUD toggle and 60FPS; 15-20min
FPS/frame/RAM/heat test. Then separately choose/import/enable a P2-specific pack,
restart and inspect replacements/counters. Retrieve matching fresh crash report
read-only if regression. No new source fix is claimed hardware-verified yet.

## Build 28 P2 enhancements dispatched - 2026-10-20 13:42 EDT

Source commit: 386771cabe6366b0788091f4d6d63f9ef6850c67
Run: 39468391460 / Build 28
URL: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39468391460
Observed status at dispatch: in_progress; conclusion/IPA pending.
Only P2 selected via [ios-p2-only]. Source and local tests summarized in the
preceding enhancement entry. No P1 app/data changes, no P2 content installation.
Local source push succeeded; source includes both game journals. This dispatch
checkpoint uses [skip ci] and does not start another build. Stop idle GitHub
polling per user; user will report completion. On return fetch/inspect this
exact run before new code edits, retrieve full logs/artifact, verify and stage
IPA only after success. Do not claim this candidate hardware-verified.

## Build28 failure reviewed; texture-import API correction verified - 2026-10-20 13:59 EDT

Build28/run39468391460/job118785702425/source386771cabe6366b0788091f4d6d63f9ef6850c67
FAILED in full native game compilation. Adapter, Apple allocator/TLS/addresses,
menu/input, enhancement profile/HUD/bridge/ZIP/rollback/CMake/reset preflights,
and real iPhoneOS configuration all passed. Packaging skipped; no IPA produced.
Full job log retrieved, full artifact ZIP digest/CRC verified. Artifact12286432727
contains only ios-build.log and ios-build-errors.md. Error index and full log
show exactly2 compiler diagnostics, one root cause, in settings line2900:
undeclared pc_texpack_active_pack; secondary incompatible vector/string operand
from Clang's suggested correction. No linker stage was reached, so successful
linking is still unverified.

This was an incorrect API name introduced in the new P2 iOS texture-import menu.
P2 already provides const std::string& pc_texpack_selected_pack(void). Replace
only that call with pc_texpack_selected_pack().c_str(); keep runtime enabled-state
check and '*' protection when all packs are indexed. Use the renderer's selection,
not sConfig/sPending, because menu changes do not rebuild the live index until
restart. P1 game/app/data and P2 Build27 working baseline are unchanged.

Added real boundary regression to tests/pikmin2_ios_enhancements_test.py. It
extracts actual texturePacksRowAction plus actual renderer enabled/selection
getters, compiles against real P2 texture-pack and iOS bridge headers, and tests
19 cases: disabled runtime; named pack; pending/config changes since startup;
all-indexed mode; busy/reentry; bridge refusal; activate/deactivate/save/restart
semantics. Only graphics SDK declarations are bypassed in the portable fixture.
Local MSVC strict compile/execution and Clang strict parser PASS. Negative
control recreating Build28's exact call fails as intended. Actual CMake P1/P2
feature wiring also reconfigured successfully. The previous broad candidate
preflights just passed on Apple in Build28; no unrelated changes were added.
Experimental P2 preflight now executes this boundary fixture before full build.

Next: commit/push correction+test+journals as one P2-only retry, record actual new
run/source, stop idle polling. No new IPA/phone fix claimed until verified.
Keep60FPS and complete enhancement batch; no need to rebuild P1 or reinstall assets.
P1 user screenshot now shows60.2FPS/16.60ms,1715MiB appRAM,CPU39%onecore,HeatNominal;
user says texture pack enabled but visual change uncertain. Replacement counter
screenshot requested; activation/render replacements remain unconfirmed. No P1
phone writes. P2 HD texture/model content still not installed by this batch.

## Build29 P2 retry dispatched - 2026-10-20 14:00 EDT

Source 7f7d0783e8b42870a8b6bbb1954199fbe9ffc6bb; run 39470849443/Build 29.
URL: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39470849443
Observed in_progress at dispatch. Local correction/API-boundary19 checks,
negative control and Clang PASS; Build29 Apple result/link/IPA/runtime pending.
Build28 had2 compiler diagnostics from1 incorrect API name; no IPA. Retain the
full enhancement batch and working Build27 backup. Only P2 builds. No P1 changes
or phone operations. Stop idle polling; user reports completion. On return inspect
this exact run, full logs/artifact, and only stage verified successful IPA. Docs
checkpoint uses [skip ci]. Logs and self-contained handoff saved in folder2.

## P1 HD texture runtime confirmation - 2026-10-20 14:07 EDT

User supplied an in-game Texture Packs screenshot: GPI Active; Loader1460
textures indexed (0dds,3046png);354 replaced,455 not in pack,0 failed.
The live successful-upload counter confirms texture replacement is working,
superseding earlier activation/replacement-unconfirmed notes. The455 misses
fall back to original textures and are not load failures. The count records
successful replacement uploads, not necessarily distinct textures. Screenshot
is from actual P1 gameplay, day2. User previously reported little visible
difference on the small phone screen; visual preference/model correctness and
long-session performance remain separate. Prior screenshot60.2FPS/16.60ms,
1715MiB RAM,CPU39%of one core,HeatNominal was a snapshot, not a sustained test.
No code or phone changes needed; leave GPI enabled. P1 model file installation
was previously verified but this texture counter does not verify model visuals.
P2 Build29/run39470849443/source7f7d0783e8b42870a8b6bbb1954199fbe9ffc6bb remains
pending at last observation; not polled. Only documentation changed [skip ci].

## Build29 success; verified P2 enhancements IPA staged - 2026-10-20 14:31 EDT

User confirmed success, then API/logs/artifact independently verified.
Source7f7d0783e8b42870a8b6bbb1954199fbe9ffc6bb; run39470849443/Build29;
job118794209786; artifact12287084885. P2 only. All intended workflow steps passed,
including new19-case real import-menu/API boundary; profile188/P2bridge24/P1bridge19/
HUD30/transaction/ZIP/reset/CMake, allocator1359/1280/Apple-scalar1359, menu188/198,
actual iPhone ARM64 allocator/menu syntax, headers/addresses/TLS, full compile/link
and IPA packaging. Full logs retrieved;0 distinct compiler/linker error lines.
Artifact ZIP SHA25669b13b4db9a885c711ddd2dc08aacf59bba2974e677afcb189e45263d2a7f50e
matches GitHub metadata; ZIP CRC pass. IPA integrity/plist/P2 bundle/ARM64/iPhoneOS
min15/system-only library loads/unsigned state verified; fresh UUID
03e1bc57-bc1e-356a-a65b-6474b990b91c. Actual ARM64 new/new[] both retain16-byte alignment.
IPA3897973bytes; executable11221000bytes;
SHA256429b2f4011e82cee0d8b879bf3bfc271c93c382c1c33d461f2c8a9a7c8ce1871. No proprietary ISO/RVZ/SZS/BMD payload found.

Hash-identical verified IPA copied to Documents/Open Nectar/1 - Install on iPhone/
Pikmin 2 - Build 29 - QOL Graphics and Performance.ipa. Clear START HERE/WHAT TO TEST guides, verification JSON and build
shortcut updated. Build27 backup retained; no app installation/uninstallation,
phone file writes, asset/art recopy or P1 modifications occurred in this turn.
New Build29 PHONE INSTALLATION/60FPS/QOL/HUD/menu/import/runtime tests pending.
Separate P2 HD texture/model content not downloaded/installed; this IPA adds
preset and ZIP import support, not a content bundle. Next user updates existing
P2 using same signing account/ID, tests menu/Begin/pause, controls/audio/HUD,
then screenshot stats and sustained play. Obtain compatible GPV textures later.

Future online co-op design agreed and recorded in ios/ONLINE_COOP_DESIGN_NOTES.md
and folder2/Future Online Co-op - Agreed Design.md: together-only host campaign,
shared progress/inventory, own screen/squad/allowance; forced group area/cave
travel acceptable; health-first difficulty, selected extra encounters only after
performance/stability evidence; reconnect/pings/phone interruptions/backups and
independent graphics accepted. No online implementation begun; remains last.
P1 texture uploads already screenshot-confirmed354 replaced/0 failed; P1 untouched.
