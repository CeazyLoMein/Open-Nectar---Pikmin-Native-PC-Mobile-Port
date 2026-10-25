# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-25T20:51:07.400812+00:00 UTC (October25,2026 EDT).

**Overall status:**65 remains tested LAN baseline.67 failed on3 deprecated title-format calls. Related7-call cleanup and independent-check aggregation/release gate batch implemented/locally verified; next Apple run pending.

### Pikmin 1

- Objective: Validate main-menu Online entry/Rejoin/opaque hidden-work pause while retaining65 behavior.
- Investigated: Full67 job, all title formatters and buffers, fixture compiler failure handling, native check dependencies/packaging gates.
- Confirmed root cause: Apple27 SDK deprecates sprintf;3 legacy calls inside actual captured title function failed strict fixture compilation. No native variant/full app or IPA produced67.
- Files changed: games/pikmin1/src/plugPikiOgawa/ogTitle.cpp, tests/pikmin1_ios_room_ux_test.py, tests/run_ios_room_checks.py, tests/ios_room_checks_runner_test.py, .github/workflows/ios-native-experimental.yml.
- Implemented:7 bounded title formatters with correct PC tag buffer; local forbidden-API negative control; both fixture modes attempted;12 independent native checks with persistent logs/timeout evidence; full app/runtime can collect independent errors; strict final outcome+complete12-check receipt gate before packaging.
- Local tests: Real desktop+native actual-source compile/run PASS. Restored sprintf negative control correctly rejected by real compiler.9 aggregation/gate/timeout/stale-binary tests PASS.10 getter ARC compile/negative control PASS;2 identity+3 bundle tests PASS; diff check PASS. No warnings disabled for title code.
- Confirmed runtime:65 both real phones same-WiFi stable minute+/11ms min, leave/rejoin/reverse host and solo/settings/controls PASS. No internet/shared-world/full-campaign pass.
- Remaining: Next Apple full native/UI/runtime/package, then new phone UI/rejoin/modal return tests. Heat reduction unmeasured; no graphics/FPS/packs changed. Solo/shared save slot integration still future.

### Pikmin 2

- Objective: Preserve working app; no P2 source changes or new build requested.
- Investigated/root cause: No new P2 issue reported.
- Tests/results: Historical both-phone working installation, not retested now.
- Remaining: Future P2 co-op engine/campaign work.

### GitHub

- Repository/branch: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port / ios-experimental.
- Starting commit: 999835141f82b133f671c0fc340500f97b23bc4c
- Latest source/commits: Next scoped P1-only formatting/preflight commit recorded in dispatch and Exact Resume State.json.
- Changes pushed: Source/test/workflow/journal batch; no history rewrite, no P2 run.
- Uncommitted changes: None after checkpoint commit/push.
- Actions:67/run40230727690/sourcea1523f08a7834376ade50cb433117c8d9f8a99fe FAILURE; scene121281673397 success/P1121284703394 failed fixture compile.66 failed earlier empty shell array.65/run40220611984 remains native+IPA+two-phone LAN PASS.
- Artifacts: No67 IPA. Existing verified65 package/known working rollback and phone backups preserved. New source IPA/native success not yet claimed.

### Next steps

- P1: Native batch build; read all collected errors if any, or verify/stage successful IPA, then small T05/T07/T08 plus room/solo retest.
- P2: Preserve existing app.
- Build: Record exact next source/run; wait user result without idle polling. Preflight collection does NOT waive any release checks.
- User involvement: None while CI runs; keep65 installed, phones may unplug. No heat/FPS test requested; user handles FPS.

### ChatGPT continuation notes

- Root cause evidence work/build67-p1-full.log; all3 same deprecation. Source cleanup covers7 calls and native PAL tag buffer.
- New runner tests/run_ios_room_checks.py always returns FAIL for any nonpass check; tests/ios_room_checks_runner_test.py exercises9 safety/failure cases. Packaging gate validates original step outcome and complete PASS receipt after independent compile/runtime, never accepts a failed continued step.
- Important pending features:66 native menu/Rejoin/opaque pause source not phone-tested. Keep connection-only labels; do not claim playable campaign or physical heat reduction.
- Resume: inspect next recorded native run, preserve logs/receipt and source build mapping, stage only successful verified IPA, then ask BOTH-phone update/test batch. Never overwrite65 rollback or existing slots/packs/settings.

**END PROGRESS REPORT**
