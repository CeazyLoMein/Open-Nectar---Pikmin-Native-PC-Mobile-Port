# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-25T16:53:40.117833+00:00 (October25 session).

**Overall project status:**62 SUCCESS independently verified. Complete IPA inspected and staged in Documents with instructions and working54 rollback. User's first phone app-data backup verified; user is performing familiar manual Sideloadly update. No phone installation completion or runtime pass reported yet. First human batch T01-T04 is ready; Raye backup/update pending. No new source changes/native build.

### Pikmin1

- Current objective: Update both existing P1 apps safely and perform the first real same-Wi-Fi private-room test.
- What was investigated:62 live jobs/artifact, actual IPA CRC/metadata/Mach-O/scene+room markers/icons/notices and simulator receipt. Confirmed first phone is user's iPhoneDuo/iOS27.2, exactly one normal installed P1 identity. Read-only app-scoped configuration/save backup with P1 closed.
- Root cause or leading hypothesis: Prior packaging-path mismatch resolved. No new failure asserted. Real phone UI/data hash/permission/network behavior remains untested.
- Files changed: Documentation/checklist only; no game or PC/P2 source change. Private staging/backup receipts saved.
- Tests and results:62 native+scene+real encrypted simulator session/private-code/content mismatch SUCCESS. Artifact digest verified. Downloaded IPA CRC valid, normal org.opennectar.experimental.pikmin1/Pikmin1, ARM64 iPhoneOS platform2/min15/SDK27.1, executable UUID38750961-9ca5-35f6-b5b8-96c26647013f; compiled scene delegate and room entry present; original6 icon bytes and original3 notice bytes match sources. Unsigned, no game data/ISO/RVZ bundled. Working54 rollback hash verified. Phone backup12files/352195bytes, second source reread hashes unchanged, no source-phone writes.
- Confirmed working: Compilation and IPA generation/inspection PASS. Simulator runtime PASS. Existing P1 user-confirmed solo baseline remains; NEW62 hardware install/runtime not yet reported.
- Remaining issues: T01 install both phones, T02 connect, T03 leave/rejoin/reverse roles, T04 ordinary solo still works. Shared online campaign/world/actions/Onions/private cameras/save recovery not activated. Current screen is connection test only.

### Pikmin2

- Current objective: Preserve working app.
- What was investigated: No P2 app/source work.
- Root cause or leading hypothesis: None.
- Files changed: None.
- Tests and results: No update or rebuild.
- Confirmed working: Previous phone results retained.
- Remaining issues: Later separate game adapter/audit.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental.
- Starting commit:0aff10f7b7e054557c5d76313162d6091ae50b51; clean/matched origin after fetch.
- Latest commit: Documentation/checklist milestone pending at report creation; exact final HEAD in accessible state.
- Commits created: Documentation-only checkpoint; no new native run intended.
- Changes pushed: Journal/checklist after staging/backup; source62 unchanged.
- Uncommitted changes: Clean after final documentation checkpoint.
- GitHub Actions run IDs:62 run40210863029/source b8abc62ecddd146f411d136c0ab9f6095ee9d858.
- Build results:62 SUCCESS, scene121221580833/P1121223972527 SUCCESS. Runtime receipt iOS27.1/Duo PASS; post-test simulator cleanup timeout recorded separately, no claim cleanup succeeded.
- Artifacts produced: P112606436543 SHA256e5277bdfc894fe5ca0afc80a85aee47590bb26b07100bff2ddeeb9737cdcda22 downloaded+verified; scene12605757693 metadata SHA25617ae37e9e09aaf229e66912a4d1ca7cd1ea3780f395cbb0e98f339ff0e89dd1f. IPA5287907bytes SHA256e74db6323261aa6cd9c621cbc00a8f5445cdd2f0d7a9975b436cea026c681f3c staged, not installed by agent.

### Next steps

- Next Pikmin1 task: User completes Sideloadly installation on own phone; before launching compare protected settings/save hashes where possible. Then connect Raye's phone with P1 closed, back up app-scoped settings/saves and update with same62 IPA. Both on same Wi-Fi for T02.
- Next Pikmin2 task: Leave alone.
- GitHub/build task: No new build while awaiting device results.
- Anything requiring my involvement: User is doing familiar drag IPA > select phone > Start. Only one phone currently connected. Agent prepared file/rollback/backup; no credential entry or account change automated. Tell agent when own phone installation completes; Raye backup precedes her update.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: This build is finally SUCCESS and staged. Do not restart build loops or mark phone tests passed from CI. User clarified manual Sideloadly is familiar; accommodate that and avoid unnecessary desktop UI takeover. Computer-use skill/docs were read and announced, but no Sideloadly UI input was performed. Any Apple authentication remains user-operated.
- Important source-file locations: ios/USER_TESTING_CHECKLIST.md now active T01-T04; ios/ios_coop_room.mm connection-only screen. Package under Documents/OpenNectar/1 - Install on iPhone/CURRENT - P1 Build62 - Connection Test (actual friendly path includes spaces as staged receipt). Source/backup paths and hashes in private exact state.
- Relevant logs: work/build62-run.json/jobs.json/artifacts.json, build62-p1-artifact.zip, build62-package-verification.json; outputs/Build62-Pikmin1 runtime/socket logs. work/build62-your-phone-backup.json and backup folder manifest. Private backup helper work/backup_p1_before_build62.py targets user's phone only; do not reuse its fixed target for Raye without identification.
- Unverified fixes: NEW62 not yet installed or phone-tested. USB availability/user P1 closure confirmed; no actual phone writes by backup. No Raye backup performed in this phase.
- Risks and warnings: Preserve existing signed app identity/account for update, never uninstall or modify save/card/asset folders. Existing signed bundle team suffix discovered but no credentials read/transmitted by agent. Large base/mod assets are not duplicated in small backup; in-place update should retain them, verify after update. First-phone backup includes BOTH save and save-solo-test so real current progress protected. No desktop/firewall/P2 changes.
- Exact next actions: Await installation completion; check same app and protected document hashes with P1 closed, then first launch/connection screen. Back up/update Raye after she connects. HostCopy/share code then return to hostP1 before guestJoin; allow Local Network prompt manually, retry join if interrupted. Record exact messages on both phones without publishing private code. T03 reverse host/rejoin, T04 solo sanity; only then proceed with next engine integration.

**END PROGRESS REPORT**
