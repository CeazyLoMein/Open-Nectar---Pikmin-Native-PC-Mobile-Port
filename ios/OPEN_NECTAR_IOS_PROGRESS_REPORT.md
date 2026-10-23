# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-23 14:26 EDT

**Overall project status:** Build49 real SDL2/probe compile PASS; simulator get_app_container HUNG180s before app launch. No runtime test and both game builds SKIPPED/no IPA. This does not establish recurrence or resolution of48 synthetic-test fault. Blocking query removed; native startup state now travels through already captured stdout.26 contract/safety +12 runner/transport checks PASS locally; complete native/runtime/game/phone pending. Replacement combined gated build not yet dispatched. P144 withdrawn, P245 native PASS/installation HOLD; working installed P2 preserved. Landscape/player-selected120 retained.

### Pikmin 1

- Current objective: Get a reliable complete shared startup test, then restore verified phone launch without changing installed game data.
- What was investigated: 49 full job120573614837 and artifact12522068185 digest/CRC verified. Actual SDL2/probe BUILD SUCCEEDED; simctl installed probe but get_app_container timed out after180 seconds before launch. Failure stage install and no native report/stdout/stderr artifact confirm this attempt did not exercise the probe. Full log and failure JSON copied to friendly folder2.
- Root cause or leading hypothesis: Latest failure is a confirmed simulator-tool lookup timeout, not an app crash. Why CoreSimulator lookup hung is unknown. It is removed rather than increasing the timeout. Earlier failures differ:44 phone requires scene lifecycle;46 missing UIScene header (compile-resolved);48 fake system notification test crashes Apple keyboard code (source-corrected, native retest still pending).47 same test cause inferred. These gate failures have prevented full game builds.
- Files changed: tests/ios_scene_smoke/main.m emits compact NECTAR_PROBE_STATE JSON to stdout and flushes it, retaining Documents JSON and all checkpoints/exception reporting. tests/run_ios_scene_smoke.py removes get_app_container entirely, reads latest complete marked stdout report, records parsed final JSON and logs command start before execution. tests/ios_scene_runner_test.py covers live-stream reports, partial final line/noise, error propagation after earlier-ready and complete orchestration without lookup. No production game/platform/DSP/FPS changes;48 isolated actual SDL filter test retained.
- Tests and results: 26 contract/safety checks +12 runner/transport host tests PASS. Orchestration asserts get_app_container is never called; simulated output stream still enforces entry/window/landscape/filter/real lifecycle-count/PID assertions. Partial writes/noise cannot produce a ready pass; latest native error still fails. Python syntax/git formatting PASS.49 native compile PASS, probe NOT LAUNCHED, games SKIPPED. New report transport native compilation/runtime pending; host tests are not UIKit proof.
- Confirmed working: Earlier user P1 hardware baseline.48 SIMULATOR ONLY: one entry, valid NectarSDLSceneDelegate-owned window, landscape678x466, duplicate main/reconnect retained same window. This is not full gate or game runtime success.44 phone launch FAILED; marked .ipa.DO-NOT-INSTALL. Pre-change42 backup unchanged SHA256304ac9abd4c60d96d76eb95902a0716ab743a074b1c69003aad238f7f7efd6a1;42 pacing/teleport unverified.
- Remaining issues: Complete corrected probe native compile/startup/foreign filter/real background-resume, then both native games and package verification before phone install.48 partial native window/entry/reconnect evidence retained; full game launch/display/audio/touch/120 output unverified. Existing follower pacing/teleport/idle recall/rare cutscene/full story remain open.

### Pikmin 2

- Current objective: Preserve successful Build45 const-return correction and working installed Build32 while resolving shared startup before an update.
- What was investigated: 49 downstream120581920699 SKIPPED because gate timed out before launch. No new P2 compiler/runtime result;45 native/IPA PASS but held.
- Root cause or leading hypothesis: P2's earlier JSGGetName override return mismatch was resolved by45. P2 shares SDL2 startup omission proved in P1, so45 installation remains HOLD; a P245 phone crash is inferred risk, not observed runtime evidence.
- Files changed: Probe/runner/host tests/journals only. P2 production code, previous const-return fix and installed working Build32 untouched.
- Tests and results: 45/run39958190774/source dd5683cec866d7f96f6fe5dcc2321b2d8426a088 native/link/IPA PASS; held IPA SHA256c1cc05b8b0b8265acc6786b9c8b241cd8832e4a3f9125c7aa09d670282f337e1.49 full-game jobs SKIPPED/no IPA; no runtime. New shared gate/native games/IPAs/device checks pending.
- Confirmed working: User-confirmed installed Build32 audio/gameplay baseline preserved;45 compiler correction only, not new hardware success.
- Remaining issues: Shared gate, new native/IPA, then launch/input/menus/Pikmin-enemy-wind audio/background-resume and full-campaign testing.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; local C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental, verified clean/fetched and local/remote b1dd660c02e0ba839ea0ed049dab9ac92c0c230d matched before edits; no incoming changes.
- Starting commit: b1dd660c02e0ba839ea0ed049dab9ac92c0c230d.49 source8449ef4c23820434f652c1e88fc7d94206c8302a.
- Latest source/local/remote checkpoint: PENDING transport correction; starting local/remote b1dd660c02e0ba839ea0ed049dab9ac92c0c230d. Follow-up [skip ci] journal may be newer; final external handoff records clean local/remote journal SHA.
- Commits created: Scoped startup-report transport/runner regression/journal batch; exact source above if dispatched, otherwise pending.
- Changes pushed: Replacement combined gated build not yet dispatched. One combined startup-gated run; no duplicate triggers.
- Uncommitted changes: Probe/runner/tests/journals before source commit, dispatch docs until [skip ci] checkpoint. Final clean state recorded externally. No proprietary assets, phone reports or credentials staged.
- GitHub Actions run IDs: 44=39950748289 P1 native PASS/phone launch FAIL;45=39958190774 P2 native PASS/HOLD;46=39991097065 header compile FAIL;47=39992850789 compile PASS/no ready report;48=39995580595 compile PASS/test-caused UIKit exception;49=40000088460/source8449ef4c23820434f652c1e88fc7d94206c8302a/startup120573614837 compile PASS/folder query timeout before launch, game120581920699 SKIPPED. Replacement combined gated build not yet dispatched.
- Build results: 49 SDL2/probe compile PASS, simulator query FAIL before app launch, all full games SKIPPED/no IPA. Repeated failures have been gate/source-test/tool failures rather than newly observed full-game regressions. Blocking folder dependency removed;26+12 local checks PASS. New complete native/runtime/game/phone results pending.
- Artifacts produced: 49 diagnostic artifact12522068185 ZIP SHA25695fbb0a5f338c2c00de6a9eb9ec25c8285ae015a6cc197e04de6162fce288c92 digest/CRC PASS. Compiled probe/plist/inventory/failure/console diagnostics, no app output/report because not launched. Copies in work and friendly folder2. No new game IPA;44 withdrawn/45 HOLD/42 backup unchanged.

### Next steps

- Next Pikmin 1 task: Inspect complete stdout-based startup result, then both native games/packages if gate passes. Stage original-ID verified update only after successful checks and test phone launch first.
- Next Pikmin 2 task: Keep working installed32;45 stays HOLD. Shared gate/native/package verification must pass before P2 update, followed by audio/input/gameplay regression.
- GitHub/build task: Replacement combined gated build not yet dispatched. No idle polling. On completion inspect startup-result/last JSON/raw output/failure stage first, then game jobs if gate passed. Do not bypass gate or call host mocks native proof.
- Anything requiring my involvement: No phone or open game needed now; may disconnect. Report next build completion. Do not uninstall/reset/import assets to solve CI failure. Full current settings/save/assets backup still needed before old-phone erase/transfer.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: 49 failed before app launch because simctl get_app_container hung180s; underlying service reason unknown. It did not retest48 fix. New batch removes that command entirely, uses compact flushed native JSON in known captured stdout file. Strict native gate unchanged. Earlier assistant introduced header and synthetic-event test errors; user frustrated by repeated failures; communicate exact stage and accountability, no unjustified fixed claims. Installed games preserved; landscape/120/original IDs retained.
- Important source-file locations: tests/ios_scene_smoke/main.m report() emits NECTAR_PROBE_STATE plus Documents JSON; isolated actual SDL foreign-filter check retained. tests/run_ios_scene_smoke.py read_report/await_state parses latest complete stdout state, run_probe does no container query, collect_diagnostics saves parsed last report. tests/ios_scene_runner_test.py12 tests; tests/ios_scene_contract_test.py26 checks. Existing scene entry/manifest/helper/package guard remain; ios/IOS27_SCENE_LIFECYCLE.md has full evidence.
- Relevant logs: work/build49-startup-full.log, build49-scene-artifact.zip, build49-failure-verification.json; friendly folder2 copies and Build49 - scene-smoke-failure.json. Exact TimeoutExpired stack points to get_app_container before launch.48 raw stack/partial native window evidence and47/46 logs preserved.44 private phone reports retained separately; no private evidence in Git.
- Unverified fixes: Latest stdout transport and48 isolated negative test still need Apple native execution.49 compiled48 correction but never launched; cannot claim runtime success or recurrence.48 partial entry/window/reconnect is not full background/resume or actual GLES game proof. No new game IPAs or phone success; full campaign/teleport/rare bugs open.
- Risks and warnings: Do not conflate simulator command timeout, synthetic test exception, compiler error and real phone crash. Stream parser ignores noise/partial lines, retains strict errors and actual lifecycle/PID assertions; timeout removal is not a startup pass.44 DO-NOT-INSTALL,45 HOLD, installed P2 untouched. No full current phone data backup; preserve old device.
- Exact next actions: Replacement combined gated build not yet dispatched. Stop idle polling. On completion retrieve startup result or failure/raw stdout/stderr/parsed last state; require complete entry/window/filter/landscape/real background-resume pass. Then inspect both native jobs and original-ID/ARM64/device/unsigned/SDK/icons/compiled scene support before staging. Phone tests only when verified IPA ready.

**END PROGRESS REPORT**
