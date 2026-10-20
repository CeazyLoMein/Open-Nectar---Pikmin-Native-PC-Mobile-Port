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

# Open Nectar iOS continuation

LATEST USER PRIORITY: keep P1 at60FPS;120FPS/ProMotion opt-in canceled and removed.
Install/prepare ALL supported optional graphics/character content from upstream;
preserve alternatives,phone saves,andworkingP1. Content preparation pending.
Build17 P1passed/P2failed; fullkeep-goinglogexposes102diagnostics. Broad native-address
batch spansroughly55source/header/buildfiles andnewactual-codehostfixture;local
checks passed,successor Apple build pending. ReadLATESTstatusentries for exactstate.

Current policy (October19 evening): user explicitly requests broader related P2
compatibility batches. Check shared headers and related container implementations,
test together, then one coordinated build. P2 now uses Makefiles + make -k to
collect independent compiler errors; P1 keeps Xcode. Preserve actual failure status.
Read the LATEST status-journal entries before historical paused checkpoints below.
Build16: P1 passed/new HUD IPA ready, P2 failed due shared nullptr macro; batch
correction and CPlate/Stickers handles implemented, successor Apple build pending.
Stop idle polling during Actions runs; user reports completion. Test IPAs always
go in Documents/Open Nectar/1 - Install on iPhone with short instructions and audio.

Read `ios/OPEN_NECTAR_IOS_STATUS.md` first. It records both games, preservation rules, verified baseline, investigations, validation boundaries, and exact next actions.

Before edits: verify origin, branch, `git status`, fetch, compare HEAD and origin/ios-experimental, and preserve unexpected changes. Never run downloaded patch installers blindly.

Priorities: preserve working Pikmin 1 framebuffer behavior; improve settings clarity; resolve Pikmin 2 compiler failures; then test existing camera dragging and work toward Pikmin 2 runtime.

Retrieve Actions logs through existing authenticated GitHub access. Keep proprietary assets and credentials outside Git. A Windows source/semantic check is not iOS compilation, and successful iOS compilation is not phone runtime validation.

Update the status journal at milestones and provide self-contained progress reports in chat. Before ending, export a complete CODEX TO CHATGPT MASTER HANDOFF including exact local/remote commits, dirty files, changes, tests, run IDs, artifacts, remaining issues, and next steps. Avoid `[ios-build]` on documentation-only commits.

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

## PAUSED â€” October 19, 2026, 10:44 AM Eastern (user request)

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

## RESUMED â€” October19, 2026, ~16:30 Eastern

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

## Build13 result and P2 title diagnostic correction â€” October19, 16:46 Eastern

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

## Build14 result / waypoint iterator fix â€” October 19, 2026, 17:14 Eastern

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

## Build15 result / performance HUD / saving investigation â€” October19,17:48 Eastern

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
