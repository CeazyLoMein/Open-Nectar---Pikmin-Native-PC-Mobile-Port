## Build75 SUCCESS — actual Apple practice startup/view checks verified

Verified 2026-10-26T20:02:22.080315+00:00. Source17e674e20aedf048aa0cea09de1c64ff87e1d962; run40338639501 attempt1; scene121626913542 and P1121631623643 SUCCESS. All9 practice checks PASS, including actual admission/start/cache/backend and camera/HUD/Onion/audio fixtures on macOS plus iPhoneOS syntax. Full native game BUILD SUCCEEDED;12 room checks and actual encrypted UIKit simulator health/socket runtime PASS; no cleanup errors. Artifact12659725915 SHA256d8824bc53ba70e35b2e467ca339df2b35646ccee434b65d44ff737ab6d67e45f and ZIP CRC verified. IPA5299899bytes SHA2568c7eb9819a6ac8b3e04a282e42c1361713de55faff21aa6a797f23e2631f2b5f, UUIDcf1a69ff-1596-3ff2-96b3-4c78da1ec885; ARM64 iPhoneOS/platform, existing app identity/icons/notices checked. Retained privately under outputs/Build75-Pikmin1; NOT staged as phone update.

This proves compilation/test/package validation, not real phone/shared-world gameplay. Keep accepted68 installed; no phone/USB task. P2 untouched. Next: actual guest Pikmin identity/state adapter and complete engine/world ownership/presentation/input integration; do not expose Start or attest complete world from captain-only transforms. All queued independent settings/FPS120/campaign/recovery/PC/P2 requirements retained. No new build for this documentation result.

## Current build: 75 — protected actual startup and independent views

Run 40338639501; source 17e674e20aedf048aa0cea09de1c64ff87e1d962; last observed IN_PROGRESS, no final result or new IPA yet.
https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40338639501

One P1-only batch: protected CardUtil producer gate/drain/private admission and cached MemoryCard reset; actual title/setup reuse; independent fullscreen local camera/HUD/Onion/audio selection and teardown. Local actual-source fixtures, MSVC/Clang checks,24 networking CTests,6 failure/gate regressions,5 identity/bundle checks and2 rejecting negative controls PASS. Apple/full engine and phone behavior pending. VIEW selection does not freeze guest simulation; complete shared world/engine bridge still missing. No Start/UI exposure. Keep accepted68 on both phones; no USB or installation task. P2 untouched. User reports completion; no idle CI polling.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-26T14:19:45.162331+00:00 UTC (user timezone America/New_York).

**Overall project status:** Resumed from explicit pause. Build74 remains the latest successful native package/runtime validation. This coordinated P1 source batch implements protected practice startup and independent fullscreen view selection. Apple validation is next. Online gameplay is NOT exposed; keep user-accepted Build68 on both phones. No phone/USB task.

### Pikmin 1
- Current objective: safely connect the accepted room to a disposable actual two-player area while preserving normal solo saves and independent personal settings.
- What was investigated: actual CardUtil producer/worker completion boundaries, cached MemoryCard file indices/data, direct title/setup route, camera/HUD/Onion/audio branches, legacy deterministic behavior and run teardown.
- Root cause or leading hypothesis: idle alone cannot prevent a new save job racing a root switch; old file/data/directory caches can survive admission. Existing fullscreen branches were tied to old deterministic mode, which also locks camera settings/forces30FPS elsewhere. Reuse the actual view paths without enabling that session.
- Files changed: CardUtil.h/cardutil.cpp, MemoryCard.h/memoryCard.cpp, new pc_coop_practice_start.h/.cpp, title/cardSelect hooks, pc_netplay_present.h/.cpp, pc_coop.cpp teardown, newPikiGame.cpp/gameCoreSection.cpp view branches, P1 CMake, four practice test/runner files and the existing experimental workflow.
- Source behavior: mutex-protected producer hold, nonblocking drain, explicit new private-card admission, safe pre-admission cancellation/failure retry, non-mutating readiness query, cache invalidation. Existing direct title/setup reused only after isolation, normal slot inheritance refused. Admitted practice remains process-latched; app restart required before normal solo. A future session driver must supply accepted-room intent, pump through drain/loading, timeout/cancel and show restart UI.
- View behavior: explicit player0/1 context selects own fullscreen camera/HUD/Onion and sound listener; invalid/nested/legacy ownership refused; actual co-op teardown clears view. No FPS/graphics/camera/control configuration writes. This is view selection ONLY; it does not suppress guest world simulation or attest a complete replicated world. No native Start/UI caller yet.
- Tests and results: strict MSVC actual-source admission/start/backend and view branch fixtures PASS; Clang/core-analyzer eight translation units PASS (final added race assertion subsequently MSVC compile/run PASS); 800 producer attempts, idle-window producer race, cancellation, invalid-path retry, busy-cache refusal and original bytes preserved. Actual camera/HUD/container/audio branch checks preserve ordinary solo/local split/legacy presentation. Two isolated negative controls correctly FAIL when removing producer hold or selecting the wrong audio listener.24 existing networking CTests PASS. Six new check-runner failure/timeout/gate regressions PASS. Two source-identity and three bundle tests PASS. Python AST/diff/structural workflow gate checks PASS; no full YAML parser claim.
- Confirmed working: earlier Build68 phone tests and user-reported solo baseline retained. New fixtures use controlled engine/OS/graphics leaves with real changed method bodies and real CARD backend, not a phone/GPU/full engine runtime.
- Remaining issues: game-thread room handoff/pump, actual complete world baseline and guest simulation/presentation separation, own controller/camera update mapping, world interactions, reconnect and campaign integration. Native compile/fixtures for this batch pending. No new hardware outcome claimed.

### Pikmin 2
- Current objective: preserve existing working build; stronger campaign validation/online adapter remains queued.
- What was investigated: no P2 code or phone changes in this batch.
- Root cause or leading hypothesis: no new P2 failure under investigation.
- Files changed: none.
- Tests and results: no new P2 tests/job requested.
- Confirmed working: earlier user hardware/audio report; full campaign completion unproven.
- Remaining issues: campaign coverage and later online development.

### GitHub
- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: c2d80471fa5bcc7d7a7d5001dc1a915be86a7b0a
- Latest commit: source commit recorded after this checkpoint in Exact Resume State.json.
- Commits created: scoped protected startup/view source and checks batch.
- Changes pushed: this source batch to ios-experimental, P1-only native validation requested.
- Uncommitted changes: checked and recorded after commit.
- GitHub Actions run IDs: latest completed74/run40265585036 SUCCESS; new run ID recorded after dispatch.
- Build results:74 real encrypted UIKit simulator runtime/12 room checks/full app/package PASS. New Apple checks: macOS compile/run and iPhoneOS syntax for BOTH actual-source fixtures, independent failure collection, mandatory original step outcome plus all nine receipt checks before IPA packaging. New per-check logs retained.
- Artifacts produced: no new artifact yet; verified74 IPA remains privately retained, Build68 remains phone baseline.

### Next steps
- Next Pikmin 1 task: inspect this exact native result, then continue actual room-to-engine driver and full-world/guest presentation integration. Do not enable Start using only captain transforms.
- Next Pikmin 2 task: preserve; resume broader campaign testing after P1 milestone.
- GitHub/build task: user reports new run; inspect complete logs and all new fixture receipts. No idle CI polling.
- Anything requiring user involvement: nothing until a concrete playable package is staged. Keep68; no USB/installation.

### ChatGPT continuation notes
- Important source-file locations: games/pikmin1/pc_port/netplay/pc_coop_practice_start.*, pc_netplay_present.*, games/pikmin1/src/plugPikiColin/cardutil.cpp/memoryCard.cpp/titles.cpp/cardSelect.cpp/newPikiGame.cpp and plugPikiKando/gameCoreSection.cpp.
- Relevant logs: work/practice-batch-clang.log, work/practice-checks-runner-test.log, work/practice-negative-controls.json, actual fixtures/binaries under work/practice-admission-* and work/practice-view-*;74 evidence retained.
- Unverified fixes: new Apple full app/source fixtures and actual phone behavior; guest full-world immutability and playable shared-world are NOT implemented by this view context.
- Risks and warnings: simulation advances inside newPikiGame::draw and other refresh callbacks; skipping updateAI alone is insufficient. Old lockstep mode still forces30/locks personal fields and is not enabled. Restart-only temporary routing is intentional until safe lifecycle restoration exists. New title restart guard needs a clear restart UI before exposure.
- Exact next actions: verify new run/source/package; add game-thread accepted-room ownership and continuous pumping through startup, supply scene readiness only after actual two-captain/world load, complete authoritative world/guest presentation/input adapter, then stage one concrete two-phone independent-view test. Preserve all queued research/settings/recovery/PC/P2 goals.

**END PROGRESS REPORT**

---
Earlier checkpoint history:

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

**Paused at user request:** 2026-10-26T13:39:41.923104+00:00. Stop development until resumed.

Repository C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port, branch ios-experimental.
Latest local/last fetched remote commit: c2d80471fa5bcc7d7a7d5001dc1a915be86a7b0a. No commit/push/build in this work segment.
Build74/run40265585036/sourcee896892cd0495dcf3bd064b2b7b9a6268833d291 passed; actual encrypted iOS simulator test, 12 room checks and IPA verified. Keep accepted Build68 installed on both phones. No phone/USB task. P2 untouched.

UNCOMMITTED IMPLEMENTATION, not ready for installation:
1. Actual CardUtil producer gate: closes under job-publishing mutex, drains existing work without blocking game loop, admits only the new private card, invalidates old directory/buffer pointers. Safe pre-admission cancellation, failed-path retry, non-mutating readiness query. Explicit worker idle initialization and exception-safe mutex guards.
2. MemoryCard::pcResetForCoopPractice clears old file indices, metadata and campaign byte buffer only after admitted/drained state. Personal settings untouched.
3. pc_coop_practice_start.h/.cpp wires protected requests into existing direct-title/setup route. No native UI caller is enabled. Admission precedes title exit; setup refuses a real-save fallback and inherited normal slot. After practice admission, app restart is required before normal solo.
4. pc_netplay_present practice-view context separates fullscreen local camera/HUD/container/audio selection from old deterministic netplay. Does not force FPS/camera/graphics/control settings. Actual newPikiGame.cpp/gameCoreSection.cpp branches reuse this context. No active caller yet. This is VIEW selection only, NOT guest simulation freeze/full-world replication.

VERIFICATION:
- Strict MSVC /W4 /WX compilation and actual-source admission/start/card fixture PASSED.
- Fixture tested an outstanding old job, 800 concurrent blocked producers, cancellation, invalid-path failure/retry, original-save byte preservation, actual private backend writes, stale cache reset and restart requirement.
- Diff whitespace check passed BEFORE the final view edits.
- Latest fullscreen view edits have NOT been compiled/tested yet. No Apple validation for any new work this segment. No new IPA/phone test.
- Existing card/backend tests and broader regressions need rerun once source batch is complete.

NEXT EXACT ACTIONS:
1. Inspect this uncommitted diff and saved snapshot; do not reset/reapply old installers.
2. Compile/test fullscreen context and actual camera/HUD/audio branches, including default solo/local split-screen preservation, both player identities, context teardown and legacy mode exclusion. Confirm no personal config writes/FPS cap.
3. Audit startup guards for failure/cancellation/return-to-title and rendering mutation boundaries. Actual world simulation runs inside newPikiGame::draw; skipping updateAI alone is insufficient to freeze a guest.
4. Continue game-thread room ownership/load/readiness and complete-world bridge before enabling Start Practice. Do not expose movement from incomplete captain-only state as a complete shared world.
5. Wire new admission fixture into existing Apple checks and run appropriate batch verification before source commit/push. Avoid another native build for documentation alone.

All queued objectives/research/independent personal settings/shared campaign/recovery/internet/PC/P2 requirements remain in ios/COOP_OBJECTIVE_QUEUE.md and ios/COOP_MOD_RESEARCH.md. Earlier full progress reports follow.

Uncommitted source status at pause:
```
M games/pikmin1/CMakeLists.txt
 M games/pikmin1/include/CardUtil.h
 M games/pikmin1/include/MemoryCard.h
 M games/pikmin1/pc_port/netplay/pc_netplay_present.cpp
 M games/pikmin1/pc_port/netplay/pc_netplay_present.h
 M games/pikmin1/src/plugPikiColin/cardSelect.cpp
 M games/pikmin1/src/plugPikiColin/cardutil.cpp
 M games/pikmin1/src/plugPikiColin/memoryCard.cpp
 M games/pikmin1/src/plugPikiColin/newPikiGame.cpp
 M games/pikmin1/src/plugPikiColin/titles.cpp
 M games/pikmin1/src/plugPikiKando/gameCoreSection.cpp
?? games/pikmin1/pc_port/netplay/pc_coop_practice_start.cpp
?? games/pikmin1/pc_port/netplay/pc_coop_practice_start.h
?? tests/pikmin1_practice_admission_test.py
```

Recovery snapshot: C:\Users\chazz\Documents\Open Nectar\2 - Progress and ChatGPT Handoff\Paused Work - Practice Admission and Views; includes tracked patch AND full copies of new/modified source with SHA256 manifest. These are private local backups; no game assets or credentials included.

---
Earlier checkpoint history:

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
