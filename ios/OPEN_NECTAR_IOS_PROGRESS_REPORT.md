# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-25T21:32:27.414006+00:00 UTC.

**Overall project status:** Build68 native validation/package verification PASSED. Verified update staged for both phones; new phone behavior untested.65 remains confirmed same-Wi-Fi connection baseline.

### Pikmin 1

- Current objective: Validate new title entry, remembered Rejoin and native-screen return on both phones, before playable shared-world work.
- What was investigated: Live68 run/jobs, all12 native preflight receipts, full simulator connection output, artifact/IPA CRC and SHA256, Mach-O architecture/SDK/identity and resources.
- Root cause or leading hypothesis:66 failed a shell test wrapper;67 then exposed3 deprecated sprintf calls.68 bounds all7 related calls, corrects PC volume tag capacity and collects independent errors before strict release gate. These fixes now pass actual Apple validation.
- Files changed:68 source54b87307 changes ogTitle.cpp, tests/pikmin1_ios_room_ux_test.py, new tests/run_ios_room_checks.py and ios_room_checks_runner_test.py, experimental workflow and docs. Earlier66 feature source5bf89a24 changes ios/ios_coop_room.h/.mm, ogTitle.cpp and sysDolphin/system.cpp; retained68. Current checkpoint changes documentation only.
- Tests and results: Local actual-source desktop/native fixtures, forbidden-API negative control,9 aggregation/gate tests,10 ARC getters and5 identity/bundle checks PASS. Actual68 Apple scene startup/background-resume, full app compile, all12 preflight, encrypted simulator delayed rejection/all5 mismatch reasons/join/rejoin and package PASS. Post-PASS simulator shutdown timeout is cleanup warning. IPA hashes/resources/ARM64/device identity checked.
- Confirmed working:68 Apple compile/package/simulator tests;65 BOTH PHONE LAN connection/leave/rejoin/reverse host/solo by prior user report.68 actual phone installation and new UX NOT yet verified.
- Remaining issues: T05/T07/T08 pending. Shared world/independent captains/squads/Onion/actions/safe shared slots, live-world reconnection, durable mid-day checkpoints and PC handoff remain future work. Rejoin only remembers code in running app process; host must return foreground after Messages. Connection test does not start shared campaign.

### Pikmin 2

- Current objective: Preserve working P2.
- What was investigated: No new P2 issue or runtime audit this turn.
- Root cause or leading hypothesis: No new P2 failure reported.
- Files changed: None in P2.
- Tests and results:68 P1-only; P2 not rebuilt/retested.
- Confirmed working: Earlier user-reported working app on both phones, not new validation.
- Remaining issues: Broader campaign checks and P2 co-op later.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental.
- Starting commit: b384355b6032e61990a0413e1bbfa6204104da83 (clean, matched origin after fetch).
- Latest source commit:54b873070d3ab331a6775e3a31aa85c8344c0ebf; docs commit recorded after push in Exact Resume State.json.
- Commits created: Documentation-only Build68 verified-package/checklist checkpoint [skip ci].
- Changes pushed: Source already built68; current journal push does not trigger native compilation.
- Uncommitted changes: None after checkpoint.
- GitHub Actions run IDs:68/run40232707062 SUCCESS; scene121287640022/P1121290722481 SUCCESS.67/run40230727690 failed formatting preflight;66/run40229474228 failed shell wrapper;65/run40220611984 baseline SUCCESS.
- Build results:68 native full app/all12 required checks/final gate/runtime probe/package PASS; actual68 phone install/runtime PENDING.
- Artifacts produced:12614073052, SHA2561052b1e1b6b0445a162778f683cc5d15b74df5e7a0e26b4c6ba42778073b7a8e. IPA5288985bytes SHA2567f4599e1acb5cbb63a9403e218c510b0f970c94a40ddb634eca1503cd396716b, UUIDd7fdbb27-3997-3c86-be23-665d1df2be7a, ARM64 iPhoneOS/min15/SDK27.1. Staged: C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\CURRENT - P1 Build 68 - Menu and Rejoin\Pikmin 1 - Build 68 - Menu and Rejoin.ipa. Normal org.opennectar.experimental.pikmin1 identity, Pikmin1 label,6 approved icons/3 dependency notices match; unsigned for user Sideloadly step.

### Next steps

- Next Pikmin 1 task: Update BOTH existing apps from same staged68 IPA through Sideloadly, same account/identity; do not uninstall. T05 title Online Co-op and Connected; T07 guest Leave/Rejoin and host Messages-return/rejoin without fresh code; T08 Done/gameplay/settings/controls preserved.
- Next Pikmin 2 task: Leave P2 unchanged.
- GitHub/build task: None pending; await actual phone observations. No idle CI polling.
- Anything requiring user involvement: Both installs and3 short tests. No USB needed once installed. No need leave phone/game connected/open for agent unless logs requested. Do not change FPS/visual choices for these checks.

### ChatGPT continuation notes

- What another conversation needs:65 actual LAN connection baseline preserved.68 now verified Apple/native package, not yet phone-tested. New Online Co-op entry still connection-only. Separate shared slots and actual gameplay remain future; do not claim co-op campaign is ready.
- Important source locations: ios/ios_coop_room.mm/.h; games/pikmin1/src/plugPikiOgawa/ogTitle.cpp; games/pikmin1/src/sysDolphin/system.cpp; tests/run_ios_room_checks.py and fixture/gate tests; libs/nectar_net transport/room from65 unchanged.
- Relevant logs: work/build68-run.json/jobs.json/artifacts.json/package-verification.json; work/build68-p1-full.log; outputs/Build68-Pikmin1/ios-room-check-results and simulator log/result/cleanup warning. Accessible full job log and package receipt retained.
- Unverified fixes: Main-menu row layout, Rejoin button and opaque native-screen pause/return on real phones; no measured heat improvement. Normal FPS/graphics/packs unchanged.
- Risks and warnings: Keep same signing identity to update in-place.65 IPA and54 rollback preserved; backups are earlier pre62 snapshots, not fresh68 backups. Rejoin requires host alive/open, remembers code only in guest process. Do not publicly share room codes. No phone data writes by agent this turn.
- Exact next actions: User installs68 on both, runs T05/T07/T08 and reports each result/affected phone. Retrieve logs only if symptoms need them. On success proceed with first actual shared-area movement/independent-view adapter, not internet/recovery claims from connection tests.

**END PROGRESS REPORT**
