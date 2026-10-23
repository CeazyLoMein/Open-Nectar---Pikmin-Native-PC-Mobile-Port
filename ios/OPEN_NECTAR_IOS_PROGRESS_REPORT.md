# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-23 12:56 EDT

**Overall project status:** P1 Build44 PHONE LAUNCH FAILURE confirmed from3 matching crash reports; shared iOS27 scene migration SOURCE IMPLEMENTED and local checks PASS, Apple runtime/build/IPA/phone PENDING. P2 Build45 compile/link/IPA SUCCESS but installation HOLD for the same shared startup omission. One combined gated build is next. FPS remains player-controlled including120; landscape only.

### Pikmin 1

- Current objective: Restore launch using required scene lifecycle while retaining new display scaling, settings/assets and original app identity.
- What was investigated: Read-only USB collection of3 startup .ips files; all match44 UUIDb0e12e37-9091-3a54-b3ac-27222d5013b1. Inspected actual SDL UIApplication entry, window creation, lifecycle observers, audio/controller resume, URL forwarding, viewport/Retina handling; Apple requirement and upstream SDL reference.
- Root cause or leading hypothesis: CONFIRMED UIKit EXC_BREAKPOINT at ___UIApplicationEvaluateRuntimeIssueForNoSceneLifecycleAdoption_block_invoke before game entry. New SDK27.1 selected for full display support, but bundled SDL2 lacked UIScene lifecycle. This was missed in the earlier display batch. No evidence implicating assets or gameplay.
- Files changed: Guarded project SDL2 backport in uikit appdelegate.h/.m, events, window/video, opengles and viewcontroller; audio/coreaudio and optional hidapi/ios notification names. ios/CMakeLists.txt, Info.plist.in, sdl_scene_support.cmake, verify_scene_bundle.py; simulator probe/runner/contract tests, workflow and journals. No game AI/save/audio-DSP/framebuffer algorithm edits.
- Tests and results: Local20 scene metadata/entry/window/notification wiring checks with missing-key negatives PASS;39 original bundle identity/storage and6 icon checks PASS; Python syntax PASS; actual crashing44 bundle rejected by new scene package guard. Apple simulator/game compile NOT yet run for new source. Prior native/IPA44 PASS did not imply phone launch success.
- Confirmed working: Earlier P1 hardware baseline only.44 installed but FAILED launch. Its IPA withdrawn from ready status and marked DO-NOT-INSTALL, exact-byte archive retained. Pre-change42 backup retained;42 pacing/teleport still not proven by hardware feedback.
- Remaining issues: New startup source native/runtime validation; then menu/graphics/touch/FPS/landscape/Duo checks and background/resume/audio. Prior normal-follow pacing, genuinely stuck-only teleport (explicitly UNTESTED), idle recall, rare clam scene and full story remain unverified.

### Pikmin 2

- Current objective: Preserve successful45 type correction and include shared scene startup fix before another phone update.
- What was investigated: Completed45 job120429205992 SUCCESS; full logs and artifact12504090493 retrieved; exact IPA checked ARM64 unsigned iPhoneOS/original ID/SDK27.1/ProMotion, missing scene manifest confirmed.
- Root cause or leading hypothesis: Build44's one repeated JSGGetName return mismatch is compile-resolved by45. P2 shares SDL2 startup omission confirmed in P1, so new45 IPA held; P2 runtime failure is an inference, not a tested result.
- Files changed: No additional P2 game code this follow-up; shared SDL/iOS lifecycle changes affect both ports. Prior ObjectSystem declaration/definition const correction retained.
- Tests and results:45 native compile/link/IPA PASS at sourcedd5683cec866d7f96f6fe5dcc2321b2d8426a088, run39958190774, job120429205992, artifact12504090493. Held IPA4,157,515bytes SHA256c1cc05b8b0b8265acc6786b9c8b241cd8832e4a3f9125c7aa09d670282f337e1. Artifact ZIP SHA256a870da503d702f0e5674cc96db9a75de992fd9336a39c39f58f6015760283fd8. NOT installed/tested. New shared scene code Apple build/runtime pending.
- Confirmed working: User-reported installed Build32 audio/gameplay baseline preserved.45 compiler correction confirmed; no new hardware claim.
- Remaining issues: Shared startup runtime gate, fresh native build/IPA; then verify launch, menus/input, Pikmin/enemy/wind audio and lock/background/resume. Full campaign unverified.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; local C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental. Starting fetched local/remote863c6f54c7388669469f5c42811460be83fd4d65; clean tree before source work.
- Starting commit:863c6f54c7388669469f5c42811460be83fd4d65. Display source5f09f653b26d821079642ad23237c88ccd87b73d; P2 type fixdd5683cec866d7f96f6fe5dcc2321b2d8426a088.
- Latest commit: Shared scene source prepared; exact commit/run to record after push.
- Commits created: Shared scene/startup tests/journal commit pending.
- Changes pushed: Not yet for the scene migration. Intended one combined [ios-build] since shared startup affects both.
- Uncommitted changes: Scoped shared SDL/iOS/test/workflow/journal source; no proprietary assets, device credentials or private crash files staged.
- GitHub Actions run IDs:44=39950748289 P1 native PASS/P2 compile FAIL;45=39958190774 P2 SUCCESS. Next combined startup-gated run pending.
- Build results: New source LOCAL checks PASS; Objective-C/Apple simulator/native games/IPAs/phone PENDING. New scene-startup job must launch an asset-free app and background/resume it before both game jobs are allowed to run. Package checks require compiled scene support as well as manifest.
- Artifacts produced:45 P2 IPA held privately at outputs/Build45-Pikmin2, NOT staged for install; no scene-fixed IPA yet. P1 bad44 marked DO-NOT-INSTALL and archived;42 original backup in folder1 SHA256304ac9abd4c60d96d76eb95902a0716ab743a074b1c69003aad238f7f7efd6a1. Existing P2 install/backups preserved.

### Next steps

- Next Pikmin 1 task: Await successful new startup gate/native build, verify original-ID scene-enabled IPA, stage in folder1 and test launch FIRST before display/gameplay checks. Do not uninstall/reset/reimport assets. Old42 backup available if needed while waiting.
- Next Pikmin 2 task: Keep installed working version; do not install45. Use new shared-scene IPA only after verification, then audio/gameplay regression tests.
- GitHub/build task: Commit/push combined source, record exact run/source and scene-startup job; stop idle polling. On completion inspect gate logs/results first, then game jobs/artifacts. Fix actual failures before declaring readiness.
- Anything requiring my involvement: No phone connection/open game needed for current work. No new phone test until corrected IPA ready. User can report build completion. Before transfer/erase, still need a separate verified game data backup; none created from this connection.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know:44 compile success was followed by confirmed P1 iOS startup trap. Latest reports supersede old44-ready instructions.45 P2 compiles but is held. Both need the same scene migration. This retains SDL2 and opts into project-specific NECTAR_IOS_SCENES, not a full SDL upgrade. FPS120 remains selectable; no60 cap; landscape only; app IDs/settings/save paths unchanged.
- Important source-file locations: ios/IOS27_SCENE_LIFECYCLE.md full diagnosis/design. ios/sdl_scene_support.cmake shared SDL compile flag; Info.plist.in scene manifest; UIKit SDL appdelegate NectarSDLSceneDelegate, nectarConnectWindowScene, scheduled/entered guards; scene-owned native window; filtered scene notifications, audio/controller resume names and URLs. tests/ios_scene_smoke uses same SDL/helper/plist, tests/run_ios_scene_smoke.py launches and backgrounds/resumes it; ios/verify_scene_bundle.py checks compiled class/selectors. Workflow scene-startup gates both game builds.
- Relevant logs: Private work/p1-build44-launch-20261023-091109 (3 .ips + summaries + installed metadata), work/p1-launch-crash-latest.json. Exact phone failures match44 UUID. Docs root read failed; later corrected Documents path returned AppNotInstalledError, no data writes/backup. Private reports copied to friendly folder2/P1 Build44 - Private Startup Crash Evidence. P245 full logs/artifact and held-verification in workspace and friendly folder2. No private evidence in Git.
- Unverified fixes: All scene source native compilation/runtime. Host tests are not UIKit proof. Simulator probe uses a generic SDL window, not actual GLES gameplay or assets; phone graphics/audio/performance/true fold behavior still required. Full story/teleport/rare cutscene bugs remain open.
- Risks and warnings: Scene backport changes shared platform startup/lifecycle; compile/runtime errors remain possible. New startup gate catches missing adoption/window/duplicate entry/resume issues earlier. Audio/controller notification adaptation is platform-only, but must be tested on hardware. Original framebuffer presentation unchanged. No current complete game-data backup; don't erase old phone assuming reports contain assets/saves. No online/autosave development or spoilers.
- Exact next actions: Push one combined [ios-build], record run/source. Stop idle polling and wait for user's completion report. On failure retrieve scene-startup build/console/result artifact first; if gate passes inspect both native game jobs. Verify new IPA scene manifest and compiled class markers, ARM64/device/unsigned/ID/icons/SDK before staging. Only then request launch, background/resume/audio, settings/120 and display tests. Preserve working P2 and old P1 backups.

**END PROGRESS REPORT**
