# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** October 25, 2026 21:47 EDT

**Overall project status:** Build70 retry passed and produced a verified IPA. New practice-save isolation is implemented and locally verified; next Apple build pending. Build68 remains the accepted installed baseline. Playable two-phone practice is not yet exposed.

### Pikmin 1

- Current objective: Protect normal solo data before wiring a disposable online practice area.
- What was investigated: Exact70 attempt2 jobs, complete P1 log/artifact, simulator binary identity, cached save root, actual CARD/history operations, separate achievement file and delayed save callbacks.
- Root cause or leading hypothesis:70 attempt1 likely unhealthy simulator; the exact same probe binary passed attempt2. A late environment-variable change cannot isolate the already cached normal save root; explicit routing and a permanent practice-session latch are needed.
- Files changed: card_stubs.cpp, pc_card_paths.h, pc_day_history.cpp, pc_achievements.cpp; tests/pikmin1_practice_card_test.py; experimental P1 workflow and project journals.
- Tests and results:70 Apple/native/simulator/package PASS. New actual-source filesystem fixture strict MSVC PASS; original file bytes preserved across mixed operations and delayed workers. Clang diagnostics/core analyzer3 units and diff PASS. New Apple/macOS actual-source fixture and full game compile pending next build. Previously committed simulator health guard local15 tests PASS, first Apple validation also pending.
- Confirmed working: User-accepted68 connection/UI/Rejoin/solo-return tests and reported thermal improvement.70 helper protocol/native evidence verified. No new phone installation or practice-area runtime evidence.
- Remaining issues: Actual scene/captain/controller/camera/guest simulation/pause driver; save worker drain and restart-only exit UX; later shared gameplay/Onions/co-op campaign/save recovery/internet.

### Pikmin 2

- Current objective: Preserve the working app.
- What was investigated: No new P2 symptom.
- Root cause or leading hypothesis: None newly reported.
- Files changed: None in P2.
- Tests and results: No new P2 build or phone test requested.
- Confirmed working: Earlier user reports; not retested here.
- Remaining issues: Broad campaign testing and later online adapter.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental.
- Starting commit: 176128c51f00641f7c10afd8c23496e885a1e470, matched fetched origin before changes.
- Latest commit: New scoped source checkpoint; exact hash and next run recorded in Exact Resume State.json after push.
- Commits created: Practice-card isolation/source fixture/workflow/journal batch [ios-build] [ios-p1-only], followed by dispatch journal [skip ci].
- Changes pushed: One coordinated native P1 build intended; no P2 source change.
- Uncommitted changes: None after successful checkpoint.
- GitHub Actions run IDs:70/run40247953593 attempt2 SUCCESS; P1 job121341674330 and scene121341711036 SUCCESS. Attempt1 failed simulator launch with no compiler/linker errors. Next source run pending lookup.
- Build results:70 retry full native/protocol fixture/IPA PASS; new save-isolation batch local PASS, Apple pending.
- Artifacts produced:70 artifact12621390344 SHA2561653a8106d4e7f2965e742b9108311a46f80e83c4e9f2c7ef9927c736d6c697c; IPA5291797bytes SHA256620be63ca87abd68dfcf9527368b8b3b1ec99a509c3fbe645530fecf7df40c8e, UUID08ea1e96-0fc5-3182-8ec5-ee7e3f44cca4, normal standard P1 bundle/deviceARM64/icons/notices verified. Saved at C:\Users\chazz\Documents\Codex\2026-10-19\got-it-you-want-codex-to\outputs\Build70-Attempt2-Pikmin1\Nectar-pikmin1-unsigned.ipa. No70 install requested; accepted68 install folder remains current.

### Next steps

- Next Pikmin 1 task: Verify next Apple result, then actual disposable area driver with drained CardUtil, explicit card admission, two loaded captains, input/own-camera routing and guest presentation, pause/background/exit. Practice requires app restart before normal solo.
- Next Pikmin 2 task: Preserve working P2.
- GitHub/build task: One P1-only native validation includes temporary-card fixture and previously committed independent simulator health guard. User reports result; no idle polling.
- Anything requiring user involvement: Nothing now. Keep68 installed; phones may close/disconnect. No repeated connection test.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know:70 attempt2 passed using IDENTICAL probe hash to failed attempt1.68 remains phone baseline. New save isolation has no game/UI caller yet and does not itself start co-op. No full campaign or live co-op claim.
- Important source-file locations: games/pikmin1/pc_port/dolphin_stubs/card_stubs.cpp and pc_card_paths.h explicit begin/active/I/O mutex; pc_day_history.cpp transaction locks; pc_achievements.cpp practice award/write guards; tests/pikmin1_practice_card_test.py; prior ios/ios_coop_handoff.h and libs/nectar_net CoopConnection/PracticeBootstrap/CoopSession helpers.
- Relevant logs: work/build70-attempt2-run.json/jobs.json/artifacts.json/p1-full.log/package-verification.json; outputs/Build70-Attempt2-Pikmin1; work/practice-card-local.log and practice-card-fixture; accessible Build70 Retry and Practice Card evidence folder.
- Unverified fixes: New Apple actual-card fixture/full game build, simulator health guard Apple path, any real engine admission/drain/lifecycle, UIKit transfer execution and two-phone practice gameplay. No phone writes this session.
- Risks and warnings: Barrier serializes filesystem access but cannot drain engine worker or protect freed engine buffers. Driver must stop requests/drain before teardown. Latch remains until process exit, so forbid normal solo Continue until restart. Temporary card is disk-backed; no nonempty cleanup implemented. Failed isolation aborts practice. Preserve68/65/54 rollback, real cards/settings/packs/FPS120/resolution/P2. Health-only success is not gameplay evidence.
- Exact next actions: Inspect exact next source/run native result and batch real failures if any; then implement title/CardSelect/GameCore actual area driver with the above contracts. Do not enable old direct boot without admission or assume transform snapshots are a complete world. T10 phone practice test remains FUTURE.

**END PROGRESS REPORT**
