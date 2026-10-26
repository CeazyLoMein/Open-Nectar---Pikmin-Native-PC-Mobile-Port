## Co-op reuse audit — correction and faster-path candidate (October26)

User asked whether established local co-op/upstream research could accelerate online development. Read actual local/online source, not only earlier journal summaries. No gameplay/architecture switch implemented and no native build requested for this audit.

CONFIRMED REUSE: pc_coop.h/.cpp two-captain local run state/character selection; GameCoreSection creates both captains and updates two cameras. Existing updateDynamicSplit disables merged view under older netplay; drawGameInfoHud has a local-player fullscreen HUD branch; local listener audio selects the player's captain. These should be adapted/reused, not rewritten as a new two-player game. Hooks are coupled to the old deterministic two-pass path, so cannot simply turn them on independently of input/simulation lifecycle.

IMPORTANT CORRECTION: Earlier notes saying upstream online is only captain replication are incomplete. games/pikmin1/NETPLAY.md contains a stale captain-only introduction but later documents TWO modes: default exact world replay of host-applied inputs and older --online-predictive captain-only mode. Actual pc_netplay_session.cpp::online_guest_replica_ticks (line4782 at audit source) decodes both host-approved inputs, calls online_advance for real game ticks, records state hashes and catches up a late guest. The source exists; its iOS gameplay correctness has NOT been tested. Do not repeat captain-only as a blanket claim or call existing replay production-ready.

POSSIBLE ACCELERATOR: bounded isolated SAME-iOS-build proof of existing exact replay could reuse normal local-coop world logic for Pikmin/enemies/items rather than immediately writing a complete guest entity-state adapter. Reuse current proven encrypted rooms/compatibility/input/session/save-isolation work where useful. This is a candidate to evaluate before duplicating upstream integration, not an implemented change to the accepted host-owned campaign design. Replay needs matching outcomes across phones; hashes detect divergence but do not themselves repair it. It does not solve crash recovery or complete mid-day persistence automatically.

EVIDENCE OF CONSTRAINT: exact-replay function comments say every catch-up tick still renders because skipping presentation caused item state divergence at tick12 in an upstream rejoin test. Current session timing uses30Hz; high-FPS rendering, camera independence, our gameplay mods, different device shapes and host/guest settings need explicit verification. Do not cap/change user's FPS120 choice or graphics to silently make old mode fit. iOS in-process startup/room ownership, touchscreen input and background/return paths still need integration. PC/iPhone cross-architecture replay remains a separate unproven compatibility concern. If replay diverges, authoritative full-world replication remains a fallback, with existing components retained.

RESEARCH RECHECKED: Factorio developer FFF149 describes receiving a world and buffered inputs then catch-up (https://www.factorio.com/blog/post/fff-149); useful comparison, not proof of our determinism. Stardew mobile guide documents PC-host/mobile-client experiments, matching versions and interruption/network issues (https://www.stardewvalley.net/mobile-multiplayer-guide/). Grounded Shared Worlds documents single active host and shared progress (https://grounded.obsidian.net/news/grounded/grounded-heads-into-the-home-stretch). These offer design patterns, not drop-in Pikmin synchronization code.

NEXT CANDIDATE CHECK: after reviewing72, trace existing exact-replay setup dependencies and render/input/save barriers, then isolated two-process same-build hash proof through walking, independent cameras, one squad/attack/carry/Onion transaction and scene pause/load before selecting it for iOS prototype. Avoid another large rewrite or blind old-online enable. Near-term milestone remains two phones in one disposable familiar area with independent controls/views. Longer-term campaign recovery/cross progression/P2 remain staged. Keep68 installed; no phone task now. Build72 last observed in progress, NOT polled in this audit; no newer result claimed.

## Build72 dispatched — owned simulator, bounded setup recovery, mandatory runtime gate

Source 0b2eabc7e9ccd201150a13802f2bc9e7c85535d7; run40258515054; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40258515054. Last observed IN_PROGRESS, result/IPA pending. Repair changes only test runner/experimental P1 workflow, local26 regression tests PASS. Fresh owned simulator, one setup-timeout reboot before native probe only, earlier runtime before heavy compile, preserved diagnostic attempts/owned-only cleanup, mandatory original step outcome + complete receipt and actual native log gate before packaging. No retries/waivers for real native failures and no whole-job automatic retry. Actual service recovery on Apple still unverified.

71/run40255974650/source50360b19dbb8f4ce89c86e33f69ec55e96ec766c: full game compile/actual-card macOS fixture+iPhoneOS syntax/12 room checks PASS, separate simulator health20s timeout, native socket probe NOT RUN, no IPA.70 attempt2 remains last successful native/protocol package result;68 remains accepted phone baseline. No phone action/gameplay/FPS/resolution/packs/heat/P2 change. Actual disposable area/controller/camera driver not enabled; T10 FUTURE. Stop save requests/drain CardUtil before future practice admission/teardown; restart before solo after card latch. User reports new result; no idle polling.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** October 25, 2026 22:19 EDT

**Overall project status:**71 game compilation and new save-isolation checks passed; simulator health execution failed before co-op testing. Grouped infrastructure correction implemented and locally verified; next Apple build pending. Keep accepted68 on phones. No playable co-op area exposed yet.

### Pikmin 1

- Current objective: Reliable mandatory Apple runtime checks, then disposable two-player practice driver.
- What was investigated: Full71 log, exact source/jobs, complete diagnostic artifact and CRC/SHA, independent health timeout, setup selection/ownership, workflow ordering and package failure gates.
- Root cause or leading hypothesis: Confirmed independent health program could not execute; simulator inventory/log/shutdown also timed out. This is a simulator execution failure before co-op main. Exact host-service cause unknown; no game compiler failure. Fresh ownership and earlier runtime execution target stale/default device and post-build setup risk without claiming a proven root mechanism.
- Files changed: tests/run_ios_coop_socket_probe.py, tests/ios_coop_socket_runner_test.py, new tests/ios_coop_owned_runner_test.py and experimental ios-native-experimental.yml; project journals/checklist only. No game source changed this repair.
- Tests and results:71 actual macOS save-isolation fixture and iPhoneOS syntax PASS; full native app and12 room checks PASS.71 simulator health FAIL, encrypted probe NOT RUN, no IPA. Repair local26 host regression tests PASS; Python syntax/workflow gate structure/diff PASS. New Apple lifecycle validation pending next build; no full YAML parser claim.
- Confirmed working: Accepted68 phone tests/thermal improvement reported by user;70 attempt2 actual native encrypted handoff/area/input fixture PASS.71 proves card-source Apple compilation/host filesystem test, not gameplay.
- Remaining issues: New runner Apple validation; actual practice title/area/captains/controllers/cameras/guest presentation/lifecycle, then shared gameplay, Onion ownership, campaign saving/recovery/internet.

### Pikmin 2

- Current objective: Preserve the working P2 app.
- What was investigated: No new P2 symptom.
- Root cause or leading hypothesis: None new.
- Files changed: None in P2.
- Tests and results: No new P2 native/device test requested.
- Confirmed working: Earlier user report; not retested here.
- Remaining issues: Broad campaign testing and later co-op adapter.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental.
- Starting commit: 75949deb70bba6bd3e2cfe7f9423e3d1a4b4fbc3, clean and matched fetched origin.
- Latest commit: New scoped runner/workflow checkpoint; exact source and run recorded after push in Exact Resume State.json.
- Commits created: Owned simulator lifecycle/bounded pre-native recovery/mandatory package gate [ios-build] [ios-p1-only], then dispatch documentation [skip ci].
- Changes pushed: One P1-only source build intended. No manual71 rerun dispatched and no production workflow/security changes.
- Uncommitted changes: None after checkpoint.
- GitHub Actions run IDs:71/run40255974650 failed, scene121357776731 PASS, P1 job121359982792 runtime health FAIL after native compile PASS.70/run40247953593 attempt2 SUCCESS. Next run pending exact lookup.
- Build results:71 full game/card fixture/preflight PASS, independent simulator health FAIL, native socket probe NOT RUN. Repair26 local tests PASS; Apple pending.
- Artifacts produced:71 artifact12622703467 SHA256232f9fe624eda4f0ff1b7ec0dba723baa1f9b5d810e2595e276567347417b871, CRC verified, retained compiled app/diagnostics but NO IPA.70 attempt2 IPA remains verified private engineering output;68 remains current accepted phone install.

### Next steps

- Next Pikmin 1 task: Review next Apple result; then actual disposable practice driver with save-worker drain/admission, two captains/own camera/controller and guest presentation/pause/exit. Restart before solo after practice latch.
- Next Pikmin 2 task: Preserve working P2.
- GitHub/build task: One combined P1 validation of owned simulator/recovery/gate changes. Full native runtime success still mandatory; no automatic native-test retries or health-only waiver.
- Anything requiring user involvement: Nothing now. Keep68 installed; phones may close/disconnect. User reports next run result; no idle polling.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know:71 did NOT fail compilation. New actual card fixture and full game built; tiny independent health program hung before co-op execution. New repair is only runner/workflow. Scope of host tests is orchestration correctness, not Apple runtime proof. Playable practice engine remains missing.
- Important source-file locations: tests/run_ios_coop_socket_probe.py create_owned_simulator/run/verify_result; tests/ios_coop_owned_runner_test.py; experimental workflow coop_socket_run before full compile and mandatory final runtime gate. Prior card APIs in pc_card_paths.h/card_stubs.cpp remain process-latched, no game caller enabled.
- Relevant logs: work/build71-run.json/jobs.json/p1-full.log/artifacts.json/p1-artifact.zip/failure-verification.json; outputs/Build71-Failure-Evidence; work/ios_coop_socket_runner_test-results.txt and ios_coop_owned_runner_test-results.txt. Accessible Build71 - Simulator Health Failure and Repair folder mirrors evidence.
- Unverified fixes: New owned simulator/reboot/cleanup lifecycle on Apple; whether it remedies host service hangs. No new phone/test runtime evidence. Full YAML parse unavailable; workflow critical structure checked.
- Risks and warnings: Only one setup timeout recovery BEFORE native execution; native error/timeout still fails. Never restart/delete borrowed devices or wipe global caches. Cleanup failures recorded, never used to invent success. Packaging requires original execution step outcome plus actual full runtime receipt/log. Future game driver must drain engine worker before teardown, abort failed card admission and require restart before solo. Preserve68/65/54 rollback, P2/FPS/resolution/packs/settings/saves.
- Exact next actions: Inspect next exact source/run including health, socket log/result, full compile/gates/artifact. If infrastructure still fails, keep genuine failure and investigate service diagnostics; do not blindly alter game code or waive runtime. After native success implement actual practice engine/controller/camera integration before T10 phone task.

**END PROGRESS REPORT**
