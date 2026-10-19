# Open Nectar iOS continuation

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
