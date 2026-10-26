# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-26T13:20:09.142413+00:00 (UTC; user timezone America/New_York)

**Overall project status:** Paused at user usage limit. Build74 passed. Networking foundation is verified; actual online gameplay is not enabled. Keep accepted Build68 installed on both phones. No phone/USB or installation task now.

### Pikmin 1
- Current objective: connect the accepted room to a disposable two-player practice area without touching solo saves.
- What was investigated: Build74 full log, artifact, UIKit health and real encrypted socket execution, 12 room checks, IPA structure/resources; startup and rendering entry points.
- Root cause: Build73 incorrectly gave slow simulator installation/launch the short native execution allowance. Build74 separates setup deadlines from execution deadlines; actual health and socket tests now pass.
- Files changed this checkpoint: status/progress/handoff documentation only. Build74 source changed three runner files; game source unchanged by that batch.
- Tests and results: GitHub74 SUCCESS; health PASS; encrypted socket/session PASS; 12 room checks PASS; artifact SHA/ZIP CRC and unsigned ARM64 device IPA/platform/UUID/icons/notices verified; cleanup reports no errors. Local runner batch previously passed 38 regressions.
- Confirmed working: existing solo and Build68 connection behavior by earlier user tests. Build74 is compiler/simulator/package validation, not new phone gameplay validation.
- Remaining issues: real practice startup, host simulation and guest full-world rendering, independent views/input, actual Onion adapter, disconnect recovery, campaign integration and internet transport validation.

### Pikmin 2
- Current objective: preserve working port; return after P1 online foundation.
- What was investigated: no new P2 changes or tests this checkpoint.
- Root cause or leading hypothesis: no new P2 failure under investigation.
- Files changed: none.
- Tests and results: no P2 job in this P1-only run; earlier user reported working audio/gameplay.
- Confirmed working: earlier user hardware report, not a full campaign guarantee.
- Remaining issues: stronger campaign coverage and later online adapter.

### GitHub
- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: 5a11e7772f013bb69472a975d6ad4c4873e231f9
- Build74 source: e896892cd0495dcf3bd064b2b7b9a6268833d291
- Latest commit: documentation checkpoint recorded in Exact Resume State.json after commit.
- Commits created: documentation-only pause checkpoint, [skip ci].
- Changes pushed: documentation only; no extra build requested.
- Uncommitted changes: none before checkpoint; checked again after commit.
- GitHub Actions run IDs: 40265585036, Build74 attempt1.
- Build results: SUCCESS, including native runtime gate.
- Artifacts produced: artifact12627177472; IPA 5294015 bytes, SHA256 3179f2211e39d53341ebac28b143f25d62614bf50e9231c4694d9f88edb24ee4, executable UUID 3e5b2379-4fb7-3ac7-92b0-27381b14edbd. Retained privately in outputs/Build74-Pikmin1, not staged as the next phone update.
- Build link: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40265585036

### Next steps
- Next Pikmin 1 task: protected practice-area startup and real two-player engine bridge.
- Next Pikmin 2 task: preserve; resume broader validation after P1 milestone.
- GitHub/build task: no repeat build for documentation; batch meaningful driver changes and checks before next P1 run.
- Anything requiring user involvement: nothing now. Keep Build68; no installation or USB test requested.

### ChatGPT continuation notes
- All earlier additive objectives remain in ios/COOP_OBJECTIVE_QUEUE.md; four-mod research remains in ios/COOP_MOD_RESEARCH.md. Personal camera, graphics/FPS120, controls, audio and touch settings must remain independent. Host-agreed gameplay rules must not overwrite personal saved preferences.
- Actual source route: titles.cpp direct intent -> cardSelect.cpp direct setup -> ONEPLAYER_NewPikiGame -> gameCoreSection.cpp pc_coop_begin_run and two Navis. Native room is currently connection-only.
- Save safety: pc_card_begin_coop_practice provides process-latched isolated empty temporary card. Before invoking it, hold new CardUtil producers and drain pending work before scene teardown; idle alone is insufficient. No unlatch exists; app restart needed before ordinary solo resumes.
- Guest freeze hazard: newPikiGame.cpp::draw around2656–2706 advances world clock, Node update and game AI. Skipping only GameCoreSection::updateAI will NOT freeze guest. Audit draw-side mutations and presentation-role gates before actual replication.
- Reuse local co-op captains/cameras/squad ownership. Do not blindly enable old deterministic netplay: it forces30FPS and locks some personal camera settings; upstream catch-up also relies on drawing for simulation behavior.
- Relevant logs: work/build74-p1-full.log, work/build74-p1-artifact.zip, work/build74-package-verification.json. Earlier73 evidence retained.
- Unverified fixes: actual practice gameplay/guest world, phone74 behavior, full campaign and internet play remain unverified.
- Risks: unsafe title/card transition can race queued save work; render callbacks mutate simulation; no claim of mid-day persistence or exact host-loss recovery yet.
- Exact next actions: inspect clean head and saved state, finish startup/UI/render audits, implement protected practice admission with explicit ownership and readiness, then full-world baseline/input/camera bridge and meaningful regressions. Do not request a phone test until a concrete playable milestone exists.

**END PROGRESS REPORT**


---
Previous checkpoint history follows.

## Build74 dispatched — measured simulator phase-budget correction

Source e896892cd0495dcf3bd064b2b7b9a6268833d291; run40265585036; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40265585036; last observed IN_PROGRESS, no result/IPA yet. Three Python runner files only: separate install180s, launch90s, then health20s/native90s result waits after launch; phase receipts/accurate failed-operation classification; related cleanup60s/diagnostics45s. Actual native failure predicates/zero exit/ordered START+PASS/noFAIL and mandatory package gate unchanged. Local38 regression tests/syntax/diff PASS, including measured95s install+37s launch and strict stalled-native failure. Apple execution of revised budgets pending. No new workflow/game/test-body/P2/FPS/graphics/phone changes.

73/run40261792715 full P1 game/BOTH UIKit test apps/card/12 checks PASS, health installation killed by OUR20s combined setup/execution budget error; native code NOT RUN/no IPA. Same-run successful scene install95s establishes mismatch; exact older service-hang causes remain unproven. Keep accepted68 installed, no phone task. All additive objectives/research/personal settings retained. Actual protected practice area driver still next after native evidence. User reports result; no idle polling.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-26T03:44:52.943583+00:00

**Overall project status:**73 game and both UIKit test apps compiled; a confirmed runner timing mistake stopped health installation before native testing. Phase-separated timing fix implemented/local38 PASS; Apple validation pending.68 remains accepted phone baseline; actual co-op practice not yet exposed.

### Pikmin 1

- Current objective: Correct test setup timing, then actual disposable two-phone area with independent settings.
- What was investigated:73 full P1 and successful scene logs, artifact CRC/SHA, nested test app identities/binaries, exact install/launch timings and timeout accounting.
- Root cause or leading hypothesis: Confirmed20s health budget incorrectly included install/launch; successful installation in same run took95s. Earlier simulator-only diagnosis was too broad for73. No game compiler error.
- Files changed: tests/ios_coop_app_executor.py, ios_coop_app_executor_test.py, run_ios_coop_socket_probe.py and journals. No workflow/native/game code changed in this repair.
- Tests and results:73 scene/full game/both UIKit apps/card/12 room checks PASS; health install timed out before code, no encrypted fixture run/IPA. Repair38 host regressions/syntax/diff PASS. Real revised runner Apple runtime pending; no new phone evidence.
- Confirmed working:68 user phone baseline;70 attempt2 native helper runtime;73 actual UIKit wrapper SDK builds verified, not executed.
- Remaining issues: Real test app execution, actual area/controller/camera/guest presentation driver, shared actions/world/campaign, recovery/internet/PC and P2 adapter.

### Pikmin 2

- Current objective: Preserve working P2.
- What was investigated: No new symptom.
- Root cause or leading hypothesis: None new.
- Files changed: None in P2.
- Tests and results: No new P2 build/phone test requested.
- Confirmed working: Earlier user reports, not retested here.
- Remaining issues: Longer campaign testing and later co-op work.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; branch ios-experimental.
- Starting commit: 6d3aef0ea84d38b59d50f58066727ae53f9db89b, clean/matched fetched origin.
- Latest commit: New phase-budget source checkpoint; exact source/run saved after push.
- Commits created: Phase-specific simulator install/launch/execution timing batch [ios-build] [ios-p1-only], then dispatch journal [skip ci].
- Changes pushed: One P1-only build intended; no73 retry and no unrelated workflow/security changes.
- Uncommitted changes: None after checkpoint.
- GitHub Actions run IDs:73/run40261792715 failed; scene121375548655 PASS; P1 job121378419870 compile PASS/runtime gate FAIL. Next run pending exact lookup.
- Build results: Full game and both test apps compile PASS; test installation timed out; actual networking NOT RUN.
- Artifacts produced:73 artifact12625991403 SHA2566a644473c2ed4fb67868292f4c4ce4decb29500846561a790d8b0e6e90d560ec, CRC PASS, game/test apps+diagnostics. Nested test apps checked ARM64 iOS Simulator. NO IPA.68 remains installed/current accepted build.

### Next steps

- Next Pikmin 1 task: Verify phase timings, actual health/native test completion and package in next run; then real protected practice driver with independent views/settings.
- Next Pikmin 2 task: Preserve working app; later stronger validation/adapter.
- GitHub/build task: One grouped P1 source validation. No idle polling; user reports result.
- Anything requiring user involvement: Nothing on phones. Keep68 installed; phones may close/disconnect.

### ChatGPT continuation notes

- What another conversation needs:73 proves UIKit app compilation, not execution. It timed out INSTALLATION because our20s execution deadline included setup. Successful same-run scene installation took95s. Correct separate deadlines are now180 install/90 launch/20 health result or90 socket result after launch. This corrects evidence handling, not gameplay.
- Important source-file locations: tests/ios_coop_app_executor.py run_app/control_step/app-result.json; tests/run_ios_coop_socket_probe.py exact app-phase classification/owned lifecycle/gates. Actual socket fixture and UIKit apps unchanged.
- Relevant logs: work/build73-run.json/jobs.json/p1-full.log/scene-full.log/artifacts.json/p1-artifact.zip/failure-verification.json; work/build73-legacy/owned/app-tests.log. Accessible Build73 - Phase Budget Correction evidence folder.
- Unverified fixes: Revised runner on Apple; actual app/native networking runtime; all actual phone practice gameplay. Full product completion remains unmeasured.
- Risks and warnings: Separate setup allowance must never waive a real test failure. Missing/partial/failed native evidence still refuses IPA; no native retry. Maintain all queued personal camera/graphics/FPS120/control/touch requirements and optional per-player difficulty. Old replay forces30/locks camera and remains conditional candidate. Drain save worker before future temp-card admission/scene teardown; restart before solo after latch. Preserve apps/settings/saves/packs/P2.
- Exact next actions: Inspect next exact run/source and per-app phase receipt; require true native START/PASS/zero wrapper return and all gates. Then continue disposable real-area driver and saved research/queue, rather than more standalone foundations.

**END PROGRESS REPORT**
