## Build62 — exact current checkpoint

Run40210863029 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40210863029), sourceb8abc62ecddd146f411d136c0ab9f6095ee9d858; last API snapshot IN_PROGRESS, no conclusion/IPA verified.61 compiled actual P1 app and PASSED the full actual iOS encrypted private-room/session probe. Overall61 failed solely because dependency notices were at app root while verifier expected Licenses/;62 supports both layouts with strict pinned-byte/duplicate checks and preserves compiled archive before package validation. Local3 package tests+39 identity/storage checks PASS. No phone test active until verified package is staged; T01-T04 pending. P2 and existing phone/PC games untouched. User reports62 result; avoid idle polling.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-25T16:16:03.734886+00:00 (October25 session).

**Overall project status:**61 compiled the actual native P1 app and PASSED the real iOS simulator encrypted session/private-room test. Overall run failed solely because packaging verifier expected a nested notices folder while Xcode copied them to the app root. Layout check corrected, exact-byte checks retained, local tests pass. One P1-only packaging validation build pending; no phone installation yet. Full campaign co-op still not implemented.

### Pikmin1

- Current objective: Produce the verified connection-screen IPA, then run checklist T01-T04 on both phones.
- What was investigated: Actual61 jobs, full P1 log and SHA256-verified artifact; complete simulator receipt/session log; exact Xcode CpResource destinations for all3 dependency notices.
- Root cause or leading hypothesis: CONFIRMED verifier-layout mismatch. Xcode copied OpenSSL.txt, protobuf.txt and GameNetworkingSockets.txt to .app ROOT; verifier checked only .app/Licenses. Native compile and runtime were successful. Corrected supported-location checks and retained pinned SHA256 verification for all copies; tampered duplicate is rejected. Updated CMake resource location to explicitly flat Resources.
- Files changed: ios/verify_coop_bundle.py; ios/CMakeLists.txt resource placement; tests/coop_bundle_test.py; workflow archive-before-package-check ordering; journal/checklist.
- Tests and results:3 packaging tests PASS (nested, observed flat, equal/different duplicate, altered/missing notice, wrong app/missing permission).39 existing app identity/storage/configure checks PASS. Git whitespace check PASS. No repeat network listeners or unchanged gameplay tests; Windows23 real/core network tests plus complete probe previously PASS. Actual next Apple package still needs validation.
- Confirmed working:61 native Xcode BUILD SUCCEEDED; actual full UIKit room code compiled.61 iOS27.1/Duo encrypted GNS probe exited0/PASS through authentication, compatible join,2captains/60Pikmin, loaded/ready, pause/background, pings, disconnect, private code and different-content rejection. Current normal bundle identity/permission checks passed before notice path failure. Existing user-tested P154 installs unchanged.
- Remaining issues: No61 IPA because packaging gate failed. New packaging layout verification and generated IPA await next run. Real phone room UI/data hashing/permission/networking still unverified. No shared gameplay/Onion/world/save/recovery/cross-progress implementation yet.

### Pikmin2

- Current objective: Preserve working app.
- What was investigated: No P2 source/phone work.
- Root cause or leading hypothesis: None.
- Files changed: None.
- Tests and results: No P2 build/install.
- Confirmed working: Prior user reports unchanged.
- Remaining issues: Later dedicated audit/adapter/recovery.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental.
- Starting commit:e5d222fad1742240e693693eb5d78bc90d38792c, clean and matched origin after fetch.
- Latest source commit:b8abc62ecddd146f411d136c0ab9f6095ee9d858; documentation-only checkpoint follows.
- Commits created:b8abc62ecddd146f411d136c0ab9f6095ee9d858 corrects package layout verification and archive order.
- Changes pushed: Packaging batch pushed;62 dispatched.
- Uncommitted changes: Clean after final documentation checkpoint; all source/journals pushed.
- GitHub Actions run IDs:61 run40208103332/source cda57702b309552934609c167c3397c15bcc3ea8.
- Build results:61 scene121213299205 SUCCESS; P1121216893603 FAILURE ONLY in Preserve compiled app packaging verification. Compile native game SUCCESS; Run real encrypted iOS session probe SUCCESS. Overall61 is FAILED, not a released/installed build.
- Artifacts produced:61 P112605154966 SHA256b5ef2dbbd2043d5e48c8d05d2b9b78e14964e55c52b7e6c16c914a0fa11d827d downloaded+verified; scene12605023389 metadata digest4fde5cdc59e89d678bc3156e5c5fc3a823057d3c2ebfafba051d20ed886ddb51. No IPA/compiled-app tar retained because old archive step followed failing package check; fixed next batch. Verified runtime receipt saved privately.

### Next steps

- Next Pikmin1 task: Validate actual flat package notice bytes and IPA generation, then download/hash/inspect/stage in Documents and activate T01-T04 only.
- Next Pikmin2 task: Preserve app.
- GitHub/build task: Push one P1-only package correction; record actual source/run and wait for user completion report.
- Anything requiring my involvement: No phones or local firewall approvals now. Report next build passed/failed when linked; install only supplied verified package afterward.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know:61 is substantial progress: native app AND complete actual iOS encrypted private-room test PASS. Remaining failure was a checker expecting the wrong resource subdirectory. Do not claim another networking failure. Root-level notices were copied by Xcode successfully according to log; exact packaged byte verification remains next CI.
- Important source-file locations: ios/verify_coop_bundle.py accepts .app/name and .app/Licenses/name, checks all present copies against pinned originals; ios/CMakeLists.txt uses flat Resources; workflow now archives compiled app before verification. Existing checks remain strict and overall runtime gates still required.
- Relevant logs: work/build61-p1-full.log, build61-run.json/jobs.json/artifacts.json, build61-p1-artifact.zip and build61-verified-runtime.json. CpResource destination evidence near full-log lines63855-63893; package error near63938; successful real runtime follows. Probe receipt SHA2565c4fbb0ebc47dc3f196ca2fda5422b59183408e0b7ee2e0a70c748e15335f698. Cleanup shutdown timeout is recorded after PASS; no claim it was successful.
- Unverified fixes: Corrected actual packaged notices verification/IPA generation awaiting new run. Full phone controller/installed data hash/permission/real two-device connection still not tested. Cross-device/host-recovery doc remains DESIGN, not implemented.
- Risks and warnings: No existing apps, files/settings/saves/PC games/firewall changed. No user hardware task marked complete from CI. USER_TESTING_CHECKLIST.md remains canonical with T01-T04 pending verified package; no new local listener starts this batch.
- Exact next actions: Push package correction, record source/run and mirrors. After actual success verify native/runtime receipts, original app identity/permission/ARM64/icons and notice bytes in downloaded IPA, preserve54/53 rollback, stage in accessible folder, then clear small connection-test request with audio alert. Do not call a room test playable co-op.

**END PROGRESS REPORT**
