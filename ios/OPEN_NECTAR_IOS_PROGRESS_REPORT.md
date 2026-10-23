# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-23 13:29 Eastern Daylight Time

**Overall project status:** Build47 shared SDL2/simulator app compilation PASSED, confirming46 header correction. Simulator startup FAILED to report readiness; cause UNRESOLVED. Both game builds SKIPPED; no game IPA. Early phase/exception/raw stderr/crash capture and runner reliability changes IMPLEMENTED;9 host runner tests +24 startup checks PASS, not Apple runtime proof. Next combined gated diagnostic run not yet dispatched. P144 remains DO-NOT-INSTALL; P245 compilation PASS/installation HOLD. Preserve installed P2. Landscape only; player-controlled FPS including120.

### Pikmin 1

- Current objective: Identify the exact shared simulator startup failure before another phone install; retain original app identity and display/FPS work.
- What was investigated: Full47 job120548733186 log and verified artifact12518747847: SDL2/probe BUILD SUCCEEDED with no compiler errors; simctl returned process45203, then30-second readiness check found no scene-smoke.json. Console has UIKit assertion entries but message decoding is <compose failure>. No crash report/early progress file was captured. Compared startup arrangement with official upstream SDL scene code and Apple diagnostic guidance; no supported new gameplay cause identified.
- Root cause or leading hypothesis: 47 startup cause UNRESOLVED. Do not label it a timeout-budget problem, known crash, or successful scene migration.46 missing UIScene.h is compile-resolved by47. Separate44 phone launch trap remains CONFIRMED from3 matching reports at UIKit no-scene-lifecycle enforcement.
- Files changed: tests/ios_scene_smoke/main.m writes process-entry/before-SDL-init/window/reconnect/running checkpoints, explicit report-write failures and uncaught Objective-C exceptions/stacks; live probe window180 seconds. tests/run_ios_scene_smoke.py chooses newest installed iOS27 runtime, resolves container BEFORE launch, captures raw stdout/stderr, actual built app/optional symbols/plist/inventory, failure stage and recent own-process crash reports, independently collects diagnostics and cleans up. New tests/ios_scene_runner_test.py and workflow gate wiring. SDL_uikitappdelegate.m adds launch/config/connect/game-entry log markers only. No speculative lifecycle algorithm, AI/save/DSP/render/FPS changes.
- Tests and results: 9 host runner regressions PASS: newest-runtime/tie selection, reject unsupported OS, explicit native-error/phase propagation, missing report failure, strict full orchestration and raw-log flags, reject process restart, preserve original error/cleanup despite diagnostic failure, scoped recent crash collection despite one command failure.24 scene contract/dependency checks PASS. Python AST and git diff formatting PASS.47 native simulator compilation PASS; runtime readiness FAIL; game jobs SKIPPED. New diagnostics Apple compile/runtime still PENDING. Mocked host runner tests are not UIKit proof.
- Confirmed working: Earlier P1 user hardware baseline only. Build44 installed but launch FAILED; withdrawn file marked .ipa.DO-NOT-INSTALL and archived. Pre-SDK42 backup retained unchanged, SHA256304ac9abd4c60d96d76eb95902a0716ab743a074b1c69003aad238f7f7efd6a1. No claim that42 following/teleport is hardware-verified.
- Remaining issues: Locate actual startup stop/exception with new evidence, implement its supported correction, then pass simulator startup/resume and both native builds. Only then launch-first hardware tests, display/touch/audio/FPS/resume checks. Existing follower pacing, genuine teleport (UNTESTED), idle Recall All, rare clam cutscene/full story remain open.

### Pikmin 2

- Current objective: Preserve successful Build45 const-return correction and working installed Build32 while resolving shared startup before an update.
- What was investigated: 47 downstream job120552988929 SKIPPED after shared startup readiness failure. No new P2 compile/runtime result.45 remains a successful native compile/link/IPA at dd5683ce but is held for shared startup exposure.
- Root cause or leading hypothesis: P2's earlier JSGGetName override return mismatch was resolved by45. P2 shares SDL2 startup omission proved in P1, so45 installation remains HOLD; a P245 phone crash is inferred risk, not observed runtime evidence.
- Files changed: Shared SDL startup log markers and probe/test infrastructure only; prior P2 const-return correction retained. Installed P2 app and game audio DSP untouched.
- Tests and results: 45/run39958190774/source dd5683cec866d7f96f6fe5dcc2321b2d8426a088 native compile/link/IPA PASS; held IPA SHA256c1cc05b8b0b8265acc6786b9c8b241cd8832e4a3f9125c7aa09d670282f337e1.47 P2 build SKIPPED, no new IPA. Shared probe compiled but readiness failed. New diagnostics/runtime/games/hardware PENDING.
- Confirmed working: User-confirmed installed Build32 audio/gameplay baseline preserved;45 compiler correction only, not new hardware success.
- Remaining issues: Shared gate, new native/IPA, then launch/input/menus/Pikmin-enemy-wind audio/background-resume and full-campaign testing.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; local C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental. Verified clean/fetched; local/remote5938c9b8034ce4fd946387318b3097f8e9e4bcc6 matched, no incoming changes before edits.
- Starting commit: 5938c9b8034ce4fd946387318b3097f8e9e4bcc6.47 source2034e139369df84f61fd499d0d085b4e567b1d78.
- Latest source/local/remote checkpoint: PENDING diagnostic source commit; starting local/remote5938c9b8034ce4fd946387318b3097f8e9e4bcc6. Follow-up [skip ci] journal commit may be newer; external final handoff records exact local/remote journal SHA.
- Commits created: Startup diagnostic/probe/runner/test/workflow/journal batch; exact source above after dispatch, otherwise not yet committed.
- Changes pushed: Next combined gated diagnostic run not yet dispatched. Gate retained, one combined run; no duplicate triggers or game-build bypass.
- Uncommitted changes: Scoped diagnostics/probe/runner/test/workflow/journals before source commit; dispatch journal only until [skip ci] commit. Final clean state recorded externally. No proprietary assets, private phone reports or credentials staged.
- GitHub Actions run IDs: 44=39950748289 P1 compile/IPA PASS, later phone launch FAIL;45=39958190774 P2 native/IPA PASS but HOLD;46=39991097065 gate compile FAIL (missing-header cause);47=39992850789/source2034e139369df84f61fd499d0d085b4e567b1d78/startup job120548733186 compile PASS/readiness FAIL, game job120552988929 SKIPPED. Next combined gated diagnostic run not yet dispatched.
- Build results: 46 header compile blocker resolved by47; actual simulator readiness remains FAIL, cause not known. New9 runner +24 startup checks PASS locally. No claim the underlying runtime issue is fixed. Next run gathers earlier native evidence before any full game build.
- Artifacts produced: 47 diagnostic ZIP12518747847 SHA256283b2e4f18569a26afd4e3d1f1835adf86faab47a7b11b886d370c8690354afa (build log + decoded console only), verified digest/CRC. NO game IPA. New runner will preserve raw process output, early JSON, crash reports if generated, built probe/available symbols, metadata and explicit failure stage.45 P2 held;44 withdrawn;42 backup unchanged.

### Next steps

- Next Pikmin 1 task: Wait for new diagnostic gate result; use early phase/raw exception/crash evidence to identify actual startup failure. Do not install44 or claim diagnostics fix launch. Correct supported cause before game/IPA/hardware tests.
- Next Pikmin 2 task: Preserve installed Build32; keep45 on HOLD. Shared gate must pass before a new game build and verified scene-enabled update.
- GitHub/build task: Next combined gated diagnostic run not yet dispatched. No idle polling. On completion retrieve scene diagnostic artifact first, inspect phase/error/raw stderr and own crash reports. If gate passes, inspect game builds and verify packages; if it fails, diagnose from new evidence without bypass.
- Anything requiring my involvement: No phone or open game needed now; may disconnect. Report run completion. No complete current settings/save/assets backup exists for transferring/erasing old phone; this remains separate from copied crash reports.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: 47 progressed past46 header failure and compiled the real SDL2/probe, but simulator never wrote its ready report. Root cause remains unknown; this batch improves evidence, not a claimed behavior fix. Full games skipped.44 P1 phone trap confirmed,45 P2 held, installed P2 untouched; landscape/player-selected120/original IDs retained. No co-op/autosave/AI development in this batch.
- Important source-file locations: tests/ios_scene_smoke/main.m process-entry checkpoint, exception handler and SDL/window phases; tests/run_ios_scene_smoke.py runtime selection/container-before-launch/raw stderr/failure/crash collection; tests/ios_scene_runner_test.py9 host regressions. Shared SDL UIKit appdelegate startup log markers. Prior scene helper/manifest/entry/window/filtered observers and CoreAudio owning UIScene.h import retained. ios/IOS27_SCENE_LIFECYCLE.md evidence and source links; ios/verify_scene_bundle.py actual package guard; experimental workflow retains startup dependency.
- Relevant logs: work/build47-startup-full.log, build47-scene-artifact.zip, build47-failure-verification.json and friendly folder2 copies. Artifact has only ios-scene-build.log and scene-startup-results/scene-smoke-console.log; no readiness JSON/crash report, console mostly <compose failure>.46 exact compile errors and private44 phone crash evidence retained. No private evidence uploaded to Git.
- Unverified fixes: There is NO demonstrated fix for47 startup failure yet. New native diagnostics compilation/execution pending; host mocks cannot prove UIKit behavior. Simulator probe is generic SDL window, not game GLES renderer. New full game builds/IPAs/phone/display/audio/full campaign still pending.
- Risks and warnings: Do not guess from empty report or undecodable UIKit assertion entries. Keep44 DO-NOT-INSTALL and45 HOLD. Newer simulator selected for SDK/runtime alignment, not claimed as the root-cause fix. Strict single-entry/window/resume/foreign-scene checks remain; gate not weakened. Original app IDs/settings/save paths preserved. No verified current complete phone-data backup.
- Exact next actions: Next combined gated diagnostic run not yet dispatched. Stop idle polling. When completion reported, verify/download diagnostic artifact, read raw stderr/early phase/exception/own crash reports and compiled probe metadata. Diagnose and correct the first actual failure; if gate passes inspect both native jobs/IPAs, verify original IDs/ARM64/device/unsigned/SDK/icons/compiled scene support before staging. Request phone testing only after corrected verified IPA.

**END PROGRESS REPORT**
