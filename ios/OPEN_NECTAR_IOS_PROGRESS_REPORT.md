# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-25T18:46:55.677177+00:00 UTC (October25,2026 EDT).

**Overall project status:** Build65 native validation and IPA verification PASSED. Two-phone update/retest is now ready; actual phone success not yet claimed.

### Pikmin 1

- Current objective: Update BOTH phones to65 and retry first real private-room connection.
- What was investigated: Actual run/jobs, artifact hash/CRC, iOS simulator receipt/full probe output and exact IPA resources/Mach-O identity.
- Root cause or leading hypothesis: Confirmed62 false mismatch from46 NFC/NFD Japanese filenames with identical base bytes. Confirmed64 delayed-close bug discarded final reliable verdict.65 carries both corrections and the related lifecycle/discovery batch.
- Files changed: This checkpoint changes documentation/checklist only.65 source batch: libs/nectar_net/src/gns_transport.cpp, src/room.cpp, include/nectar_net/room.h, tests/coop_socket_probe.cpp, tests/gns_transport_test.cpp, tests/room_test.cpp. Earlier Unicode helper/room fix retained in ios/ios_coop_content_identity.h and ios/ios_coop_room.mm.
- Tests and results: Local23 CTest,8 stress flows, final6 focused+3 full impaired flows, Clang5 translation units and13 Python regressions PASS. Now actual Apple scene/native hash tests/full app build/package and real encrypted iOS simulator slow rejection/all5 mismatch reasons/join/rejoin/session probe PASS. Post-PASS simulator shutdown20s timeout recorded as cleanup warning. IPA digest/CRC/ARM64 device SDK/identity/icons/notices/new fix markers verified.
- Confirmed working:65 compiles/packages and simulator fixture networking works; historical P1 solo and62 installs user-reported on both phones. These do not establish65 phone runtime.
- Remaining issues: Both actual65 installs and T02-T04 pending. Real shared gameplay, mid-day crash recovery, PC/phone handoff remain future work. Title-menu Online Co-op and separate Solo/shared campaign slots are approved later UX, not included65.

### Pikmin 2

- Current objective: Preserve working P2 while P1 networking is validated.
- What was investigated: No new P2 runtime investigation.
- Root cause or leading hypothesis: No new P2 issue reported.
- Files changed: None in P2;65 selected P1 only.
- Tests and results: No new P2 compile/device test requested.
- Confirmed working: Earlier user-reported working apps on both phones, not retested here.
- Remaining issues: P2 online adapter and broader campaign validation later.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: 5aab0507795ae741cddf1707c23cb6c4cfb75d86
- Latest source commit:3f650f7851ae9e38ba528f54fd42b89fbb095781 (65); later docs checkpoint in Exact Resume State.json.
- Commits created: Documentation-only verified65 checkpoint [skip ci].
- Changes pushed: Source batch already built65; current journal/checklist push will not start a native build.
- Uncommitted changes: None after checkpoint commit/push.
- GitHub Actions run IDs:65/run40220611984 SUCCESS; scene121251174574/P1121253318001 success.64/run40217032902 failed socket gate after app compile;63/run40215584390 failed older hash fixture. Historical failures retained.
- Build results:65 Apple native/simulator/package PASS; phone installation/runtime PENDING.
- Artifacts produced:12610036177, SHA256e7067d41ba9d8d00490f104f9ed3a7f4e351050954a56e0136843faef401f8d4; unsigned IPA5288159bytes, SHA256c51d6ea0e6b9e86b8321435014f27db12904be723ef9394d7f591a17b2939aad, UUIDe4efb852-b36a-3fd5-ae8a-5561105c22b5, ARM64 iPhoneOS platform2/min15/SDK27.1. Staged at C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\CURRENT - P1 Build 65 - Connection Fix\Pikmin 1 - Build 65 - Connection Fix.ipa. Standard bundle org.opennectar.experimental.pikmin1; six approved icons match; three original dependency notices match pinned bytes. Signed installation is user Sideloadly step, not done by agent.

### Next steps

- Next Pikmin 1 task: User updates BOTH existing apps from SAME staged65 IPA, then T02 first room connection; after pass T03 leave/rejoin/reverse host and T04 solo/settings.
- Next Pikmin 2 task: Keep working installation unchanged.
- GitHub/build task: None while awaiting phone observations; no additional build required.
- Anything requiring user involvement: Close P1 for update, select correct phone/account in Sideloadly, click Start, repeat on other phone. No uninstall, no game-data/pack recopy. USB can disconnect after installation; same-Wi-Fi connection test needs apps foreground, not USB.

### ChatGPT continuation notes

- Current phones presumed still62 until user reports65 updates. Never mark T02 pass from simulator/CI success.
- Important source locations: ios/ios_coop_room.mm and ios/ios_coop_content_identity.h; libs/nectar_net/src/gns_transport.cpp and room.cpp; native probe/tests listed above.
- Relevant logs: work/build65-run.json/jobs.json/artifacts.json; work/build65-package-verification.json; outputs/Build65-Pikmin1/result.json/socket-session.log/ios-build.log/cleanup-error.txt. Prior local before/after evidence is in accessible P1 - Build64 Network Failure and Batch Fix.
- Unverified fixes:65 actual phone compatibility/reconnect/solo preservation still need observations.
- Risks/warnings: Both phones need65; old62/new65 cannot join. Private room code must be fresh and kept private. Post-PASS simulator cleanup warning is not a phone issue. Existing pre62 settings/save backups and54 rollback preserved; do not call these new65 backups.
- Exact next actions: After both installs confirmed, same Wi-Fi > P1 gear > Data > Online Co-op: Connection Test > wait checks > host NEW room/copy code > host returns to P1 > other pastes/joins. Ask status from BOTH phones, then proceed only from actual results. Do not begin shared campaign gameplay testing yet.

**END PROGRESS REPORT**
