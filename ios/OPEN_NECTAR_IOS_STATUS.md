## User-approved upcoming UX — main menu Online Co-op and separate campaigns

After connection validation, add title-menu Online Co-op > Host/Join beside existing local Co-op, with personal offline Solo and a separately labelled shared campaign (numbered slots acceptable). Existing indexed slot/day-history code supports this direction, but multiplayer campaign identity/slot binding and write protection still need implementation/testing. Preserve occupied slots, whole-card backup and solo progress; joining targets the host's campaign, not the guest's solo slot. Detailed approved plan in PIKMIN1_COOP_IMPLEMENTATION.md and COOP_CROSS_PROGRESSION_AND_RECOVERY.md. No menu/save/runtime changes now; Build63/source405ab5ef/run40215584390 remains the pending identity-fix validation. No extra native build triggered. T02 false mismatch on62 still awaits corrected build/retest. P2 unchanged.

## Build63 dispatched — Unicode filename identity fix

Source 405ab5ef8432e427366056fc82e607c67c8dfbc6; run40215584390 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40215584390); last observed in_progress, no conclusion or new IPA yet. Both phone base-data audits complete; all3463 files/634811175bytes match,46 Japanese filename encodings caused62's false rejection. NFC source fix plus actual native Foundation regression queued.13 local regressions PASS and corrected independent full-data digest matches. T02 FAILED62; wait for verified63 then update BOTH and repeat room test. Both phones may disconnect now; no game data/settings/save/pack writes. P2 unchanged. No idle polling requested; user reports build result.

## Build62 phone join FAILED — confirmed Unicode identity bug

Both actual phones:3463 base-game files/634811175bytes; every file size and SHA256 matches canonical private source.46 Japanese filenames use NFC on Raye/NFD on original phone. Literal path hashing falsely rejects identical data. Implemented canonical NFC hash keys mapped to original paths; real byte/name differences and ambiguous normalized duplicates still rejected. Actual helper extracted for native Foundation regression.13 local regressions PASS; independent corrected full-data digest matches on both inventories. Apple native build/phone retest pending. No phone writes or pack changes; both USB reads complete and phones may unplug. T02 FAILED62, later runtime tasks untested; both phones will require the SAME verified next update. Connection-only, no shared gameplay yet. P2 untouched. Detailed report and private audit receipts retained; next source/run follows.

## Both Build62 installations user-reported ready — October25

User confirms both phones ready after the two same-identity P1 updates. T01 installation preparation is complete by user report; both pre-update backups remain verified. No post-update phone file-hash comparison, room connection or gameplay pass is claimed. T02 is next: both on same Wi-Fi, gear > Data > Online Co-op: Connection Test, wait for data checks, host/copy code, return host to P1 before guest joins, and allow Local Network if prompted. Expect Connected and a delay reading on both. Only after that, T03 leave/rejoin/reverse host and T04 ordinary solo. USB no longer required for these Wi-Fi tests; keep both apps foreground during connection. Connection-only, no shared campaign gameplay yet. Build62/source b8abc62ecddd146f411d136c0ab9f6095ee9d858/run40210863029 unchanged. P2/PC games untouched; no new build needed.

## Build62 phone update checkpoint — October25, 12:59 EDT

User reports their own P1 updated to Build62. Installation is user-reported; no new phone runtime/networking pass or post-update settings hash comparison is claimed. Raye's iPhone17Pro/iOS27.0.1 is connected. Initial process check found P1 still present; after user opened/closed it, fresh check confirmed P1 not running. Read-only P1 backup VERIFIED:5files/158975bytes, every local SHA256 and second phone read matched. Includes settings, achievements, navigation report and save/card0; no custom touch-layout file exists on her phone. No phone files changed. Large assets/mods stay in the existing app container. P2 untouched.

Raye can now install the SAME staged Build62 IPA through Sideloadly, selecting her phone and retaining the existing signing account/app identity. Her installation is PENDING. T01 remains partial; T02-T04 untested. After both installs: same Wi-Fi, gear > Data > Online Co-op: Connection Test, wait for data checks, host/copy code, return host to P1 before guest joins; then leave/rejoin, reverse host and verify ordinary solo. Connection only; shared campaign gameplay is not implemented yet. No new native build needed. User may disconnect USB after installation/post-update checks for Wi-Fi testing.

Build62 source b8abc62ecddd146f411d136c0ab9f6095ee9d858; run40210863029 SUCCESS. Staged IPA SHA256 e74db6323261aa6cd9c621cbc00a8f5445cdd2f0d7a9975b436cea026c681f3c. Both private backups and known-working Build54 rollback are preserved in Documents/Open Nectar. Full manifests remain private, outside Git.

## Build62 SUCCESS, IPA staged; first phone backed up — October25

62/run40210863029/source b8abc62ecddd146f411d136c0ab9f6095ee9d858 SUCCESS: scene121221580833 and P1121223972527 both success. Downloaded artifact12606436543 SHA256e5277bdfc894fe5ca0afc80a85aee47590bb26b07100bff2ddeeb9737cdcda22 and verified complete unsigned device IPA (5287907bytes, SHA256e74db6323261aa6cd9c621cbc00a8f5445cdd2f0d7a9975b436cea026c681f3c). Normal app identity/Pikmin1 label, ARM64 iPhoneOS platform2/min15/SDK27.1, approved icons, compiled scene+room code, local-network description and exact3 original dependency notices verified. Actual simulator session/private-code/content-mismatch test PASS. These do not establish phone runtime yet.

Accessible package: Documents/Open Nectar/1 - Install on iPhone/CURRENT - P1 Build 62 - Connection Test/Pikmin 1 - Build 62 - Connection Test.ipa, START HERE.txt and Package Verification.json. Known-working54 rollback rehashed/copied into Rollback - Keep. Both phones user-reported available; user phone connected/unlocked/P1closed. App-scoped backup12files/352195bytes verified by second read (settings/layout/achievements/save and save-solo-test), no phone writes. User prefers familiar manual Sideloadly drag/select/Start; told proceed on own phone. Installation NOT reported complete yet. Raye backup/update pending. T01-T04 now READY, unchecked; current step T01 partial. P2 unchanged. User can disconnect USB after installation/post-update check for Wi-Fi test. No shared gameplay yet.

## Build62 — exact current checkpoint

Run40210863029 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40210863029), sourceb8abc62ecddd146f411d136c0ab9f6095ee9d858; last API snapshot IN_PROGRESS, no conclusion/IPA verified.61 compiled actual P1 app and PASSED the full actual iOS encrypted private-room/session probe. Overall61 failed solely because dependency notices were at app root while verifier expected Licenses/;62 supports both layouts with strict pinned-byte/duplicate checks and preserves compiled archive before package validation. Local3 package tests+39 identity/storage checks PASS. No phone test active until verified package is staged; T01-T04 pending. P2 and existing phone/PC games untouched. User reports62 result; avoid idle polling.

## Build61 actual native+network PASS; packaging layout mismatch corrected — October25

61/run40208103332/source cda57702: shared scene121213299205 SUCCESS; P1 job121216893603 native Xcode BUILD SUCCEEDED and independent iOS27.1 encrypted session/private-room probe PASS. Overall job FAILED solely at package verification expecting Licenses/OpenSSL.txt. Actual CpResource log confirms ALL3 dependency notices copied into FLAT .app root (OpenSSL.txt/protobuf.txt/GameNetworkingSockets.txt); checker expected nested directory. Corrected verifier to accept flat/nested supported layouts and SHA-check every existing copy; mismatched duplicate still fails. CMake now explicitly uses flat Resources. Archive compiled app BEFORE packaging checks, preserving recovery artifact if a future package check fails. No game/network behavior changed.

Three packaging tests PASS including real observed flat layout, nested layout, missing/tampered/duplicate rejection;39 identity/storage/configure checks PASS.61 runtime artifact12605154966 SHA256b5ef2dbbd2043d5e48c8d05d2b9b78e14964e55c52b7e6c16c914a0fa11d827d downloaded+verified; receipt PASS, native probehash5c4fbb0ebc47dc3f196ca2fda5422b59183408e0b7ee2e0a70c748e15335f698. Post-PASS simulator shutdown cleanup timed out20s (recorded, not a test failure). No IPA packaged in61; no phone installation. Next P1-only build verifies corrected packaging; exact source/run follows. Phone checklist remains inactive; P2/PC games preserved.

## Build61 dispatched — exact checkpoint

Run40208103332 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40208103332), sourcecda57702b309552934609c167c3397c15bcc3ea8; last API snapshot IN_PROGRESS, no conclusion/IPA verified.60 Apple UI syntax passed, but simctl spawn timed out with partial stdout lost. Underlying simulator-versus-native-hang cause unknown.61 preserves failure output/stages and bounds native test lifetime; native game/resource compile happens before runtime, runtime remains required and runs independently after compile failure unless cancelled. Local23 core+actual GNS tests and full encrypted co-op/private-room probe PASS;8 runner failure-path tests PASS. No phone tests ready; T01-T04 wait verified package. Local network test processes are confirmed finished; user told Cancel both firewall prompts, no security rules changed by agent. P2/phone/PC game installs preserved; full co-op/recovery/cross-progression still pending.

## Build60 timeout diagnosis and local real-network validation — October25

60/run40204287553: scene121201787820 SUCCESS; P1121204903697 failed simctl spawn of compiled network probe after90s. Full iPhoneOS room UI syntax and ARC property checks PASSED. Simulator probe COMPILED/LINKED, Mach-O IOSSIMULATOR verified. No partial stdout was preserved by the old runner; cannot distinguish simulator launch stall from a native test hang from this artifact. P1 actual app compile/package were skipped, no IPA. Artifact12603398343 SHA2563869c339dc2a799c5dfd51ecab233260dc53b03b250870ca28e337fcd1a03347 downloaded+verified.

Implemented evidence/reliability batch: preserve timeout/nonzero partial output and failing phase, native main-entry/stage markers,60s test-only native watchdog including teardown, bounded failure diagnostics/cleanup;8 runner tests PASS. Move runtime probe AFTER independent native app compilation/resource checks and run it even if those fail (unless cancelled). All strict runtime/PASS checks remain required for a successful run/IPA. This collects more independent failures per build instead of stopping before compiling P1.

New isolated Windows real-network setup (existing SHA-checked GNS/protobuf source archives; BCrypt backend; no game install):23/23 core+actual GNS tests PASS, including room/gate/stress; full co-op socket probe PASS through60Pikmin/readiness/pause/markers/disconnect/private code/content mismatch. MSVC/O2/W4/WX plus project's CRT convention. This is Windows/BCrypt evidence, NOT iOS/OpenSSL or phone runtime proof. Firewall prompts from room_gns_test.exe and coop_socket_probe.exe were our completed local tests; told user Cancel. No firewall rules/security settings changed by agent, no listener should remain running. Do not rerun listeners unnecessarily while user is gaming. P2/phone/PC game installations unchanged.

Next P1-only native batch still needs full app/resource/runtime validation. Phone checklist has no active tasks until verified package is prepared; next room tasks T01-T04 remain pending. Cross-progression/recovery remains design-only. Exact next source/run follows.

## Running user testing checklist — October25

User explicitly requested a maintained list of their future testing tasks. Canonical [USER_TESTING_CHECKLIST.md](USER_TESTING_CHECKLIST.md), accessible Documents/Open Nectar/START HERE - What to Test.md/.txt. Ready now: no phone test requested until a verified update is prepared. Stable task IDs track room test, actual gameplay, disconnect/rejoin, checkpoint/host loss, PC/phone handoff, internet and P2. Future lists are not active instructions or implementation claims. Promote only small ready batches, record exact build/phone observations, preserve failures/results and send clear notification when human input is needed. Compiler/CI success must never mark a device task complete. Historical app-opening confirmations separated from new co-op tasks.

## Build60 dispatched; cross-progression/host-loss design saved — exact checkpoint

Run40204287553 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40204287553), source53466a4065fe017d5f3fa88b311e652885300ec2; last API snapshot IN_PROGRESS, no conclusion/artifact yet.59 retry scene SUCCESS but P1 failed OUR ARC regression-tool clang-driver flag ordering before full UIKit compile; fixed direct driver order while retaining clang-tidy convention. Both local fixture semantics and direct-driver argument-order adapter checks PASS; actual Apple driver/UI/native/private-code/package pending60. P1 only; no phone/PC/P2 changes. No install needed; user reports60 passed/failed.

New full user requirements/research saved in COOP_CROSS_PROGRESSION_AND_RECOVERY.md: live retained-host pause/rejoin versus durable full mid-day crash checkpoint, optional guest recovery copy, later opt-in host continuation and PC-home/iPhone-away single-campaign handoff with shared gameplay rules/local graphics preferences. No save/cloud/desktop features implemented by these notes. Continue iPhone milestones first.57 remains last full native/simulator networking success.

## October25 — Build59 retry result and cross-device/host recovery requirements

59 attempt2: shared scene121105139764 SUCCESS; P1121107438150 FAILED in the new ARC regression tool command before actual screen/game compile. Exact diagnostic: clang++ -x objective-c++ appeared after the last input and was an unused-command-line-argument error under Werror. Fixed standalone clang invocation to place flags BEFORE source; clang-tidy keeps source BEFORE its -- delimiter. Local actual8-getter and original ownership-negative controls PASS; standalone argument ordering checked through a driver adapter delegating semantics to real Clang frontend. Standalone Apple driver/full UIKit/native room/package still require next CI. No phone changes, P2 preserved.

Saved new user-approved design direction: PC-home/iPhone-away one official campaign, deliberate platform handoff/mod-rule parity later; live host retained-world reconnect first, full persistent mid-day checkpoint for host app loss, optional guest recovery copy and later continue-alone behavior with explicit squad safety. Full researched decisions and QOL in COOP_CROSS_PROGRESSION_AND_RECOVERY.md. No new save/cloud/PC gameplay implementation activated. Next P1-only build includes tool correction and these durable notes; exact source/run follows.

## Build59 attempt1 infrastructure boot failure; same-run retry queued — October25

Run40162073334/source d698f880af334690551a9bfb692521aec1551739: scene job121075548313 compiled probe successfully but simctl bootstatus for iOS27.1/Duo timed out after180s BEFORE install/launch. Artifact12586923613 SHA256358852e725dd39114978ccee7e1b235e66871a76f77c5f313f905a37649ba2d2 downloaded+verified; failure.json stage=boot. Both diagnostic simctl spawn commands also timed out45s. No native app execution/error is evidenced; P1 job121078373671 SKIPPED, no IPA. Underlying simulator stall cause unknown; do not claim new gameplay regression or verified room fix.

Authorized rerun-failed-jobs POST accepted for SAME59; API now QUEUED/conclusionnull, unchanged source. Last immediate API counter still run_attempt1; requested next attempt, verify counter on next result. No new game source or new numbered build. Existing ARC correction/guard still awaits full Apple CI. No phone/install needed; user reports the retry result. Preserve working P1/P2 and avoid idle polling. If boot repeats, investigate runner boot partial output/host status and add bounded infrastructure-only recovery without suppressing real app assertions.

## Build59 correction dispatched — exact checkpoint

Run40162073334 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40162073334), sourced698f880af334690551a9bfb692521aec1551739; last API snapshot IN_PROGRESS, no conclusion.58 failed exactly one Objective-C ARC property/getter naming error in new room UI; renamed copyButton to clipboardButton. Local actual8-property synthesized-getter compilation PASS; negative control recreates exact error. Regression check and full iPhoneOS screen compile included in59. P1 only; P2/phones unchanged. Wait actual native/socket/private-code/package result, then stage verified IPA and conduct two-phone connection-only test.57 remains last full successful native/simulator result. No phone or install needed now; user reports59 passed/failed, avoid idle polling.

## Build58 failure confirmed and corrected — October25

Run40161054040/source4f8ac135 failed P1 job121074322192 at the early iPhoneOS Objective-C++ screen check; shared scene121072507969 SUCCESS. Full log has ONE compiler error: ios/ios_coop_room.mm:127 copyButton getter follows Cocoa owned-object naming convention under ARC. Renamed property and all3 uses to clipboardButton. Audited all8 properties and14 method selectors. Added a compiler regression test extracting actual declarations and synthesizing their getters without UIKit headers: corrected screen declarations PASS on installed Clang frontend with arm64-apple-ios15.0 ARC; original owned-object naming trap produces exact diagnostic (negative control PASS). Full native screen/runtime still require next Apple build. All prior19core and identity/package tests passed in58 before this check; no new IPA produced, no phone changes, P2 untouched. Correction plus guard will be one P1-only build; next exact run entry supersedes pending state.

## Build58 — exact current checkpoint

Source 4f8ac1356f69fa1f47bbfab1ab411ab1ac4b2a76; run40161054040 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40161054040), last API snapshot IN_PROGRESS, conclusion pending. P1 only. Native Host/Join CONNECTION TEST UI + actual source/base-data fingerprints, private-code join/content-rejection probe, local-network permission and verified bundle notices. Local identity/packaging tests, strict C++ probe compile and39 app policy checks PASS. Apple/phone behavior PENDING.57 independently verified SUCCESS (native+scene+actual encrypted simulator/session), artifact/IPA checked; omitted notices corrected in58 source. No new phone install yet. User reports58 passed/failed; after native/package PASS, stage update in Documents and ask for a short two-phone same-Wi-Fi connection test. No idle polling; no phone needed now. No playable co-op campaign yet; P2 preserved.

## October25 — Build57 verified; real phone room screen implemented

Build57/run40158088407/source03cd0be0 SUCCESS: scene+P1 and actual iOS27.1 encrypted UDP/session with2captains+60Pikmin. Artifact downloaded+SHA verified, native ARM64/package identity checked. Networking notices were absent in IPA due to CMake parent/target source-property scope; fixed in new batch with strict packaged-byte verifier.

NEW pending Apple/phone validation: Advanced Settings > Data > Online Co-op: Connection Test, native UIKit Host/Join/copy/paste/leave UI, OS-random private room, source/config fingerprint and actual installed base-data streaming SHA256, local-network usage description, safe sharing/background and peer-loss handling. No campaign starts or saves/actors/settings mutate. Runtime gameplay options and full engine adapter still required before playable co-op.2identity+2packaging tests, generated real source digest, strict new C++ probe translation-unit compile,39 app policy checks PASS locally. New Apple check includes actual private-code join+content rejection, strict native UI compile and exact shipped notices verification. P2 untouched. No phone needed until next native build/package passes. See latest progress report and following exact run checkpoint.

## Build57 dispatched — exact current checkpoint

Run40158088407: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40158088407
Source 03cd0be08157613b020cb59c678271b44065a997, ios-experimental. Last API snapshot IN_PROGRESS, conclusion pending. P1 only plus shared scene and new iOS simulator real encrypted socket/session probe. No new artifact or phone runtime verified. Local19 core tests + new strict C++ probe compile +4 diagnostic-runner tests +39 app identity/storage checks PASS. P2 is not rebuilt. No phone needed. User should report passed/failed when57 completes; avoid idle polling. After reading actual Apple result, proceed with game Host/Join, actual source/content identities, accepted world loading and guest engine/camera integration. Current apps stay on working54/previous P2.

## New Apple encrypted transport batch — October24 session

Implemented distinct ios-arm64 and ios-simulator-arm64 pinned dependency builds, native matching hostprotoc, platform/SDK/pin-specific successful-cache receipts, static dependency notices, opt-in P1 encrypted transport linkage and real UDP/GatedTransport/CoopSession runtime probe. Probe checks wrong secret refusal, compatible join, both captains+60Pikmin atomic transfer, ready/pause/background/marker/disconnect flow. CLI runs only on iOS Simulator, rejects wrong-platform ARM64 and retains exact runtime/binary evidence.19 core tests, strict new C++ translation-unit compile,4 runner failure-path tests and39 app identity/storage checks PASS locally. Apple compilation/runtime PENDING next P1-only build. No game UI or live online mode yet; no phones needed. P2 source and normal P1 settings/saves preserved. See latest progress report and subsequent exact run entry.

## Build56 verified SUCCESS — 2026-10-24 America/New_York

Run40154273299, sourceb28a5d7b13037c68c76e66d730dd86fc679df59c. Both shared scene121052160673 and native P1121055004543 succeeded. Full P1 log and artifact upload metadata saved privately.18 core tests and actual P1 capture-to-receiver fixture passed in CI. Package binary was not downloaded/independently inspected in this status phase; no new phone install requested. The later researched session/pause/marker batch a5bd4690b3540b04c01d565ebcd83bea57d14e20 has19 LOCAL tests+Clang PASS but is NOT in56 and still needs Apple validation with upcoming integration. No co-op phone gameplay has been verified.

Next concrete work: build/prove encrypted iOS transport and generated source/content compatibility identities, then connect accepted Room/scene to CoopSession. Add explicit Host/Join prototype UI and guest actor/camera/audio integration using disposable campaign data. First user test will be actual two-phone connection and independent captains/views on the same Wi-Fi; shared-world actions/Onions/save/reconnect and different-network tests follow. Keep working54 and53 rollback; no phone needed now. P2 preserved.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-24 22:43 EDT

**Overall project status:** User authorized researched, fully developed co-op features. Primary-source comparison completed; feature plan saved. Implemented authenticated session/data adapter, loaded/ready gates, shared pause/interruption policy, typed partner markers and bounded actor update pacing.19 local tests and Clang PASS. No usable phone co-op mode yet. Build56 is previous actor-frame source and still running; new source saved without another immediate native run.

### Pikmin 1

- Current objective: Turn researched co-op design into a complete safe two-player session foundation, preserving normal54.
- What was investigated: Nintendo Pikmin3 leader/squad guide; Stardew developer multiplayer FAQ; Factorio latency/traffic postmortems; Mindustry developer server snapshot source; Deep Rock developer teammate/waypoint notes; Grounded shared-world notes. Findings/adaptations linked in PIKMIN1_COOP_RESEARCH_AND_FEATURES.md. Live56 metadata: shared scene successful, P1 configuring; no completed native result yet.
- Root cause or leading hypothesis: Complete actor frames alone don't define readiness, safe pause, mobile interruption or authoritative command permission. Protocol now models these explicitly. Stale queued status must never revive a timed-out phone. Previous loopback reconnect fixture tried opening a new connection before draining old closed-connection events; corrected lifecycle and verified re-auth/new-scene path. Initial new module compile missed explicit protocol header include, corrected locally before commit.
- Files changed: New libs/nectar_net/include/nectar_net/coop_session.h, src/coop_session.cpp, tests/coop_session_test.cpp; protocol.h/.cpp new types; core CMake/test list; experimental workflow Apple syntax checks; research/active-plan/status/handoff journals. NO games/pikmin1 gameplay source changed in this batch; no source flags activated.
- Tests and results:19/19 core test executables PASS with MSVC/O2/W4/WX. Clang diagnostic checks PASS including new source/test/protocol and existing actor/capture fixtures. Real authenticated gate + simulator test covers60owned actors, both-ready+loaded, host-only world advance, guest commands, independent pause reasons, background/foreground, heartbeat timeout and old queued packets, wrong ownership/epoch/sequence/payload, marker TTL/cooldown/nonfinite data, complete-update backpressure and20Hz network pacing. New source Apple/native runtime PENDING; no two-phone sockets/UI/gameplay verified.
- Confirmed working: Both phones' normal P154 launch baseline, Raye60FPS after restart; P2 working. Existing prototype actor-frame tests retained. New features confirmed only through core simulated peer tests, not real phone play.
- Remaining issues: iOS encrypted sockets/permission/session UI, generated build/content identity, scene/start-tick integration, real pause/lifecycle/input hooks, guest actors/fullscreen camera/audio, full world/Onions/workers/enemies/save/reconnect. Current confirmWorldLoaded is an adapter contract; the complete world bridge is absent. Fully fleshed design is saved; fully playable mode is not finished.

### Pikmin 2

- Current objective: Preserve working separate app while P1 prototype matures.
- What was investigated: No new P2 code this batch; future design accounts for forced shared cave travel and distinct local audio perspective.
- Root cause or leading hypothesis: No new P2 failure.
- Files changed: NONE under games/pikmin2.
- Tests and results: No new native/hardware validation requested.
- Confirmed working: User-reported P2 working on Raye's phone and prior original-phone baseline.
- Remaining issues: Longer campaign checks and P2-specific actor/cave/save adapter later.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; C:/Dev/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental; clean/fetched matching673581d9c6dda927d5a227e146e1dbc18d8f6ec9 before changes.
- Starting commit:673581d9c6dda927d5a227e146e1dbc18d8f6ec9.
- Latest commit: New research/session source exact commit written to external Exact Resume State.json after push.
- Commits created: One scoped research/session-feature source+tests+journal batch with skip-ci, preserving the in-flight56 native check.
- Changes pushed: New source batch; no extra native build immediately dispatched. Include it in the next meaningful P1 integration/validation run after56 result.
- Uncommitted changes: Only scoped listed source/workflow/docs until source commit; private evidence/helpers/assets never staged.
- GitHub Actions run IDs:56=40154273299, sourceb28a5d7b13037c68c76e66d730dd86fc679df59c. scene121052160673 SUCCESS; P1121055004543 in_progress/configuring at last check.55=40149838089 SUCCESS.
- Build results:56 pending.19 local tests/Clang PASS for NEWER source, NOT included in56. No claim native57 exists.
- Artifacts produced: No newly completed56/new-source IPA at this checkpoint.55 artifact upload metadata retained, not staged as a required update. Keep54 installed and53 backup.

### Next steps

- Next Pikmin 1 task: Actual iOS transport/build-content manifest, Room+accepted scene+new CoopSession wiring; then engine lifecycle/pause/input and guest actor/camera/audio bridge. Keep existing online flags OFF until isolated activation is deliberate. Current core is compatible-policy plumbing, not game mode UI.
- Next Pikmin 2 task: Preserve current game; later stronger cave/audio/save/system test and adapter.
- GitHub/build task: Save tested batch without redundant native run; inspect56 once completed, address real failures if any, then validate newer source together with next integration step.
- Anything requiring my involvement: None now; phones can unplug, no new IPA requested. User can report56 completion; do not consume usage polling idle.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User explicitly wants complete co-op with useful features, not merely two captains connected. New research document is the product/architecture feature contract. Accepted user constraints (together-only/one host/free same-area separation/own screens/shared stock/separate allowances/forced travel/health-led difficulty) remain. Independent offline play/cloud-host switching/host migration deferred despite Grounded supporting more.
- Important source-file locations: coop_session.h/.cpp/test: requires existing authenticated compatible GatedTransport, nonzero peer build/content digests and capability0x10000; MessageTypes67/68/69; WorldSnapshot carries prior complete actor frames. Active plan/research doc detail adapter APIs. Original FPS setting applies in gameplay constructor, user restart resolved it; no forced60 change.
- Relevant logs: PRIVATE work/coop-session-core-tests.log (final all19 PASS), coop-session-clang-checks.log, build56-result-run.json/jobs.json; research links in committed design document. No external game source/assets copied into repo.
- Unverified fixes: Actual iOS transport/UI/engine hooks and world snapshot/reconstruction remain absent. Heartbeat state API does not itself pause UIKit/game actors. Marker protocol does not draw markers yet. Caller must attest full engine readiness before confirmWorldLoaded; actor replica alone insufficient. No new native pass/phone co-op proof.
- Risks and warnings: Update pacing20Hz is networking only; user's selectable120 rendering not changed. Known reliable backlog64KiB defers whole updates; unseen transport queues require their own limits. Pause requests take network travel time. Secure rejoin identity/token and full world keyframe still to implement; tests re-authenticate the same private test gate. No accounts/security settings/paid services/other projects altered. No original saves reset; no finale spoilers.
- Exact next actions: Inspect56 when complete. Then implement actual native transport/manifest/accepted-scene glue and explicit experimental menu using disposable campaign data, wire pause/foreground and guest rendering. Add ownership-safe game actions/Onion transactions, full-world snapshots and two-network tests before release. Read PIKMIN1_COOP_RESEARCH_AND_FEATURES.md and active implementation plan first.

**END PROGRESS REPORT**

---

## Exact Build56 checkpoint — 2026-10-24 America/New_York

Source pushed: b28a5d7b13037c68c76e66d730dd86fc679df59c, branch ios-experimental. Build56 run40154273299, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40154273299. Last metadata status in_progress, conclusion pending; no native result/artifact verified yet. P1-only + shared scene validation.18 local core tests, actual engine capture-to-complete-replica fixture, compile-out and Clang PASS. Both phones keep working54; no new install requested. Raye60FPS confirmed after restart. No phone needed.55 separately verified SUCCESS. Stop idle CI polling; user will report completion. Next integration is actual authenticated iOS transport/session/scene compatibility and safe guest engine actor/camera application; current data replica alone isn't online gameplay. Full world, Onion engine transactions and snapshots remain.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-24 22:23 EDT

**Overall project status:** Both games launch on Raye's phone after P1 import-layout correction. Her P1 FPS change to60 was saved but only applied on re-entering gameplay; user confirms restart resolved30FPS. No phone needed now. Co-op55 passed native compilation; next batch implements complete captain/Pikmin frame packetization and an atomic guest-side data replica. This remains inactive engineering code, NOT online gameplay.

### Pikmin 1

- Current objective: Carry actual captured captains/squads through bounded multipart frames without applying partial/old/corrupt state.
- What was investigated:55 full P1 job121040694720 and scene job121038855551 both SUCCESS.17/17 macOS core tests and actual-engine fixture passed; artifact metadata recorded. Source frame pacing reads fpsMode in NewPikiGameSection constructor; closing settings persists selection but doesn't reconfigure current gameplay clamp. Raye live config fpsMode1, native2622x1206/1.0, AO0, VSync1; restart then user-confirmed60 works.
- Root cause or leading hypothesis: Confirmed FPS setting takes effect when gameplay reloads. For co-op, old packWorldDeltas splits a keyframe into independently decodable batches; none identifies completion of the WHOLE actor list. Replacing a guest world per batch would remove actors from other batches. New prototype frame envelope explicitly groups all parts and replaces only the complete validated replica.
- Files changed: libs/nectar_net/include/nectar_net/actor_frame.h, src/actor_frame.cpp, tests/actor_frame_test.cpp; nectar_net CMake; P1 pc_coop_world.h/.cpp actual capture-to-packets API; tests/pikmin1_coop_capture_test.py; existing experimental CI and journals. No P2 game change, normal settings/save behavior untouched.
- Tests and results: All18 core test executables PASS locally (previous17 unchanged passed; corrected new fixture rerun passed). Actual P1 capture/pool/packet-receiver fixture PASS, compile-out PASS, Clang diagnostics as errors PASS. New tests exercise1000 changing squads under loss/reordering/duplicates, timeout/non-sliding retries, stale frames/ticks/session/scene, checksums, malformed lengths/bounds, duplicate actors/captains, unknown schemas, nonfinite state and invalid owner/leader association. Two early assertions assumed a multipart frame that fit one packet and used stale test ticks; corrected fixture inputs, no runtime change to mask failures. New native Apple build pending.
- Confirmed working: User's P154 quick test baseline and Raye P154 title/music/controls launch plus restarted60FPS.55 native compilation/artifact upload only; no55 install requested. New receiver guarantees tested all-or-nothing DATA state; it does NOT write guest engine actors yet.
- Remaining issues: Actual iOS transport/session/invite UI, accepted build/content identity, guest actor creation/application/camera, host Onion-to-engine transaction bridge, enemies/jobs/items/world state and snapshot/reconnect. No claim online co-op is playable or full campaign tested.

### Pikmin 2

- Current objective: Preserve working P2 and its independent install.
- What was investigated: User confirms P2 works on Raye's phone.
- Root cause or leading hypothesis: No current P2 issue; source work remains paused.
- Files changed: NONE under games/pikmin2.
- Tests and results: No new P2 compilation/extended hardware test this batch.
- Confirmed working: User-reported normal P2 launch on Raye's phone, plus prior gameplay/audio baseline on original phone.
- Remaining issues: Longer campaign/device testing and eventual separate P2 co-op adapter.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; C:/Dev/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental; clean/fetched matching e2b9d47f5660fcd31b9bf292c16073fbc50428de at start of new co-op batch.
- Starting commit: e2b9d47f5660fcd31b9bf292c16073fbc50428de.
- Latest commit: New source/run and final docs checkpoint recorded in Exact Resume State.json after push.
- Commits created: One scoped co-op frame/adapter/tests/CI/journal batch with ios-build/ios-p1-only markers; no redundant P2 build.
- Changes pushed: New frame batch after passing local tests; exact source recorded externally once created.
- Uncommitted changes: Only scoped listed source/fixture/CI/journals until commit. No game assets/private phone logs staged.
- GitHub Actions run IDs:55=40149838089 source5bfa4fba17e9083deabeddc0033bc8a4a002ce06 SUCCESS. Next source/run recorded after push; NOT passed yet at this checkpoint.54=40145860255 SUCCESS, installed working baseline.
- Build results:55 P1+scene SUCCESS. New source Apple compilation pending; no phone install needed for plumbing-only check.
- Artifacts produced:55 P1 artifact12581478645 (5964282bytes, ZIP SHA256296fa46fa35f0498a3029c224cc2cab40cd67458759722e841cfc8c9e8b6e497); scene12581757882 (354779bytes, SHA256881ba0d61cd8f89b1f295114d6e01745fbdd08f61f179bbfc689361c70038376). Metadata/log upload verified, artifact binary NOT downloaded or independently package-verified this phase. No new55 staging/installation request.

### Next steps

- Next Pikmin 1 task: Real transport/session compatibility and accepted scene wiring, followed by bounded guest actor binding/application and each phone's own camera. Do not enable obsolete PC_ONLINE_ENABLED or independent guest simulation/save writes. Connect Onion authority to actual spawn/store and per-owner field limits, then remaining world state.
- Next Pikmin 2 task: Preserve working app; ordinary user testing optional.
- GitHub/build task: One P1-only Apple check for this batch, record exact source/run, stop idle polling. Native frame tests and actual capture fixture now in CI.
- Anything requiring my involvement: None now; both phones can disconnect. Keep54 installed. No new IPA requested until a usable prototype milestone.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Raye P1 black screen was my import path mistake, corrected and phone-confirmed. P1 data belongs in assets/dataDir; art beside assets. Both phones' selectable FPS remain30/60/120/monitor; fpsMode changes require gameplay reload in current baseline. New actor-frame module solves complete DATA transfer only, not rendering/AI/state restoration.
- Important source-file locations: actor_frame.h/.cpp (48byte NCF1 version1 envelope, session/epoch/frame/tick/whole-body size/FNV64 integrity/index/count); pc_coop_world_capture_packets validates increasing frame/tick and captures actual P1 actors before packing. Existing HostEntityRegistry/OnionAuthority remain.
- Relevant logs: PRIVATE work/build55-result-run.json/jobs.json/artifacts.json, build55-p1-full.log; actor-frame-core-tests.log (17 PASS then two faulty test assumptions), actor-frame-target-tests.log corrected PASS; actor-frame-engine-tests.log, actor-frame-clang-checks.log; raye-p1-fps-investigation.json and current-fps-settings.conf. No private evidence committed.
- Unverified fixes: No real phone-to-phone transport, session, actor application or new native56 result yet. No full-world snapshot/save or co-op gameplay. Existing solo rare bugs remain individually unverified.
- Risks and warnings: Authentication is EXTERNAL and REQUIRED: receiver only accepts bytes from authenticated HOST; FNV detects accidental corruption, is NOT a MAC. Accepted session/epoch comes from trusted scene barrier, never packet. One pending frame,128KiB/512actors/512fragments default bounds, fixed2s timeout; latest complete state retained through loss/corruption. Caller must not use stale packet output after false. Current maps include only captains/Pikmin visual schema, no targets/FSM/enemies/items/campaign. No simulation/game actor writes. Future transport should reliably deliver initial keyframes; this module supplies neither ACK/retransmit nor congestion control. Queued P1 buffers must obey engine scene-heap lifetime; owning vectors aren't proof they can outlive heap reset. Keep normals saves/settings/53/54, optional120 and AO-off baseline. No spoilers.
- Exact next actions: Inspect next Apple result once complete, then implement actual authenticated session/transport and guest actor bridge using complete frames. Continue P1_COOP_IMPLEMENTATION.md and SAVE_AND_COOP_RECOVERY_PLAN.md. No more phone setup required now.

**END PROGRESS REPORT**

---

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-24 America/New_York; recorded 2026-10-25T02:10:40.760072+00:00.

**Overall project status:** Raye now confirms BOTH games open. P1's black-screen startup was caused by this session's import layout error, now corrected on her phone and verified by a fresh user launch. No game source changed, no new IPA required. Co-op Build55 remains a separate engineering milestone.

### Pikmin 1

- Current objective: Resolve Raye's black screen after first-install asset transfer.
- What was investigated: Identified Raye's iPhone17Pro (iPhone18,1), iOS27.0.1. Read P1 Documents, three existing P1 crash reports, and a brief filtered startup log. Crash executable UUID1760960b-2d27-3a21-960f-2dcc404350c6 matches Build54, independently confirming her installed version.
- Root cause or leading hypothesis: CONFIRMED folder placement error in local import helper. It copied dataDir directly into Documents/pikmin1, while DVDOpen in pc_port/dolphin_stubs/dvd_stubs.cpp ALWAYS prefixes assets/. Jac_Start requests /dataDir/SndData; the missing expected assets/dataDir/SndData/Seqs/pikiseq.arc leaves Jac_InitEventSystem waiting for track0x20000. All three reports show Jac_InitEventSystem under Jac_Start/System::Initialise; iOS watchdog0x8BADF00D killed the unresponsive app. This is startup before drawing, distinct from the earlier in-game world-only black screen.
- Files changed: Phone only: relocated already verified disc roots into Documents/pikmin1/assets; kept art at Documents/pikmin1/art. Local work/import_raye_p1_assets.py now maps disc files to assets/* and art to art/* for future imports. Corrective helper work/repair_raye_p1_asset_layout.py used staged directory rename, refuses overwrite, and supports pre-activation rollback. Project/setup journals and accessible handoff updated. No P1 gameplay/audio/renderer source changed.
- Tests and results: Critical audio archive/bank/font hashes checked before move. ALL3529files/669952108bytes read back at CORRECT paths after activation with matching original SHA256; settings hash unchanged; saves/Load not written. Corrected importer syntax and mapping checked. User then confirmed title screen/music/touch-controls open normally.
- Confirmed working: Build54 on Raye's phone now launches normally, user-confirmed after repair. Original user's working app untouched.
- Remaining issues: Full campaign, longer performance/device-specific settings and existing rare gameplay bugs remain outside this launch check. Old Jac_InitEventSystem unbounded missing-resource wait still exists in source; no claim general startup failure handling was improved.

### Pikmin 2

- Current objective: Verify Raye's first installation; preserve existing source baseline.
- What was investigated: User's direct result after completed assets/art transfer.
- Root cause or leading hypothesis: No current P2 failure; P2 importer already used assets/* correctly.
- Files changed: None in P2 source or phone during this repair.
- Tests and results: User says P2 works on her phone; prior full2797file/1013544103byte readback transfer preserved.
- Confirmed working: User-reported normal P2 launch on Raye's phone. This is not a full campaign/audio-feature certification.
- Remaining issues: Longer gameplay/full story still unverified; P2 development remains paused while P1 co-op proceeds.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port, C:/Dev/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental; fetched origin and verified clean matching b1f020b30aa468e9d153412c853d553967281507 before journal edits.
- Starting commit: b1f020b30aa468e9d153412c853d553967281507.
- Latest commit: Documentation-only checkpoint for this repair is recorded in the external Exact Resume State.json after commit/push.
- Commits created: This repair needs only a scoped documentation commit with skip-ci; no game source change.
- Changes pushed: Updated journals/setup instructions; exact new commit recorded externally after push.
- Uncommitted changes: Only journals until documentation commit; private recordings/crash reports/assets/helpers not staged.
- GitHub Actions run IDs:55=40149838089, source5bfa4fba17e9083deabeddc0033bc8a4a002ce06. Last known in_progress from previous checkpoint, NOT refreshed during this phone repair.54=40145860255, sourcea7888f24009133fd3818355e35bfc5475c279e16, previously verified SUCCESS.
- Build results: No new build needed/triggered for relocating files.55's native result remains unverified at this checkpoint;17 local core tests+capture fixture previously passed.
- Artifacts produced: No new artifact this repair. Existing Build54 IPA unchanged;53 rollback retained.

### Next steps

- Next Pikmin 1 task: Continue co-op plan in ios/PIKMIN1_COOP_IMPLEMENTATION.md. First inspect55 once complete, then real transport/session/scene compatibility and guest actor application; bridge Onion authority to real engine accounting. Current capture is inert and is NOT playable online.
- Next Pikmin 2 task: No immediate code task; user can test ordinary gameplay when convenient.
- GitHub/build task: Save docs without extra CI; inspect55 once completion is reported, avoid idle repeated polling.
- Anything requiring my involvement: NOTHING else needed from either phone now; user explicitly told Raye can unplug. No reinstall or update for this repair.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Prior “all files verified” transfer receipt verified CONTENT but used wrong P1 parent directory. This correction supersedes the prior claim that the first P1 transfer was ready to launch. Both files and paths now verified and user-confirmed boot. P2 worked already. Preserve working apps/settings and prototype isolation.
- Important source-file locations: games/pikmin1/pc_port/dolphin_stubs/dvd_stubs.cpp DVDOpen prefixes assets/; games/pikmin1/src/sysDolphin/system.cpp Jac_Start uses /dataDir/SndData/; src/jaudio/pikiinter.c Jac_InitEventSystem waits on Jam_GetTrackHandle(0x20000). Correct install root Documents/pikmin1/assets/dataDir; control art Documents/pikmin1/art. No need to duplicate game data at both levels.
- Relevant logs: PRIVATE work/raye-p1-diagnostics contains three Oct24 crash reports205748/211009/211206 and live-p1.log; old imported ISO log.txt is historical developer output, NOT current iPhone startup evidence. work/raye-p1-layout-repair.json is definitive corrected-path verification receipt. Original transfer manifest/receipt retained for history; new repair receipt appended separately.
- Unverified fixes: No source-level startup timeout/recovery implemented. No claim online play, full campaign or all sounds tested. Fresh P1 boot with music/controls is user-confirmed.
- Risks and warnings: No unrelated files deleted, no original phone changed, no save/settings reset, no security/account changes, no proprietary assets or private reports committed. Keep120 selectable and AO-off known performance baseline. No final-boss spoilers.
- Exact next actions: Inspect55 when complete, preserve54 installed baseline and53 backup, continue co-op integration from documented active plan. Future P1 fresh imports MUST map extracted disc root under assets/, art separately beside it. Phone is no longer needed.

**END PROGRESS REPORT**

---

# Open Nectar iOS — current status


**Date/time:** 2026-10-24 21:15 EDT

**Overall project status:** User's quick P154 check seems fine; proceed with co-op. New stable actor identity, Pikmin state codec and actual P1 read-only capture/lifetime hooks implemented and locally verified. Native engineering check: Build55 / run40149838089, source5bfa4fba17e9083deabeddc0033bc8a4a002ce06: in_progress / pending, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40149838089 Raye's two apps installed manually; both complete private asset/art transfers finished and verified. Her phone can be disconnected; runtime after import awaits feedback.

### Pikmin 1

- Current objective: Continue controlled co-op prototype while preserving54/53, existing settings and normal campaign.
- What was investigated: Actual MonoObjectMgr pool reuse/birth/kill, Creature init and stage heap teardown; old captain-only adapter and generic nectar_net records; Raye's startup folder contents and source assets.
- Root cause or leading hypothesis: Pool addresses are reused, so address-only identity can direct delayed commands at a different Pikmin. Worker/idle leader pointers change, so owner must persist independently. New registry prevents stale identity reuse, codec validates finite bounded state, hooks clear bindings before reuse/teardown. Raye's missing dataDir/art confirmed; likely first-install black-screen cause, fresh post-import launch not yet verified.
- Files changed: libs/nectar_net entity_registry.h/.cpp, pikmin_replication.h/.cpp +tests/CMake; games/pikmin1/pc_port/netplay/pc_coop_world.h/.cpp and minimal hooks; objectMgr.cpp birth/kill hooks plus already-audited missing diagnostic argument, creature.cpp init invalidation, gameCoreSection.cpp stage cleanup. P1 CMake opt-in NECTAR_COOP_WORLD; experimental workflow and tests/pikmin1_coop_capture_test.py. No renderer/input/save-setting rewrite.
- Tests and results:17 core network/accounting tests PASS with MSVC/O2/W4/WX (existing200000 decoder fuzz + simulated30-minute loss test, new20000 recycled identities and codec malformed/truncation/NaN cases). Actual capture translation unit and actual pool birth/kill methods compiled/run against controlled engine dependencies PASS: two captains/two Pikmin, retained working/idle ownership, no partial snapshot on bad state, stale pool command rejection, scene cleanup, inactive default. Feature-compiled-out fixture PASS. Clang diagnostics PASS for new source/tests and actual capture fixture. Negative control disabling lifetime invalidation causes fixture failure as intended. Build55 / run40149838089, source5bfa4fba17e9083deabeddc0033bc8a4a002ce06: in_progress / pending, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40149838089 No new live two-phone gameplay proof.
- Confirmed working: User's P154 brief smoke check fine; earlier53 graphics/keyboard/control edges. Raye P1 all3529files/34PNG/669952108bytes imported and SHA256 read-back verified, P1 preferences unchanged. Import does not itself prove launch/audio.
- Remaining issues: Live transport on iOS, host/join UI, guest actor creation/application, full-screen camera/input per phone, authoritative Onion spawn/store bridge and global field-limit reconciliation, complete world/jobs/enemy/item/campaign sync, atomic keyframes, exact-world save/reconnect/internet relay all remain. Capture is read-only, explicitly inactive unless begun; no online menu/playable campaign yet.

### Pikmin 2

- Current objective: Preserve existing source; finish Raye's requested game-file setup.
- What was investigated: Existing source manifest2768 disc assets +28 source touch PNGs, exact signed P2 app sandbox on identified iPhone17Pro.
- Root cause or leading hypothesis: Fresh installation also needed local proprietary assets, independent of co-op development.
- Files changed: NO P2 source. Added only assets/art in Raye's P2 sandbox; no save/preferences deletion/replacement. Original user's P2 phone untouched.
- Tests and results: Source hashes rechecked against prior canonical GPVE01 audit;2797files/1013544103bytes copied and read-back SHA256 verified; staging activated. No new P2 build or runtime test.
- Confirmed working: Prior user's P2 audio/gameplay; Raye's transfer is complete, launch after import unverified.
- Remaining issues: User's fresh relaunch/input/audio/pause feedback; stronger later campaign/cave/save tests before P2 co-op.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental; starting clean b5cb2b79ecdd4b9685b495a089f116902912f73a, fetched origin matched before edits.
- Starting commit:b5cb2b79ecdd4b9685b495a089f116902912f73a.
- Latest commit:5bfa4fba17e9083deabeddc0033bc8a4a002ce06 at checkpoint generation; new build source:5bfa4fba17e9083deabeddc0033bc8a4a002ce06. Final local/remote hashes saved in Exact Resume State.json after final push.
- Commits created: Scoped co-op capture/identity batch pushed at source above; documentation checkpoint afterward uses[skip ci].
- Changes pushed: Co-op capture code/test batch and current notes; one P1-only engineering build.
- Uncommitted changes: Current scoped code/journals before push; final external state records clean tree after checkpoint.
- GitHub Actions run IDs:Build55 / run40149838089, source5bfa4fba17e9083deabeddc0033bc8a4a002ce06: in_progress / pending, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40149838089 Previous54=40145860255 SUCCESS, sourcea7888f24009133fd3818355e35bfc5475c279e16;53=40133259493;52=40131000336.
- Build results: New capture source local tests/Clang PASS; current new Apple native result pending.54 native/IPA plus user's quick check retained. No P2 CI now.
- Artifacts produced: No new prototype IPA verified yet. User can keep54; this engineering build is not a request for another phone update.54 SHA256cdf46924e6cb350eb1df571325254f55d0a479c4fab5e4e564ad950335b50ae5;53 preserved unchanged. Raye's prepared P1 copy updated to54 with53 moved to verified backup subfolder; P252 unchanged.

### Next steps

- Next Pikmin 1 task: Review one native prototype build after completion, then implement bounded reliable session/scene handshake, guest actor binding/application and full-screen per-player camera. Next bridge actual atomic Onion spawn/store and one squad/job/enemy/carried object. Existing read-only capture is not enough to play online.
- Next Pikmin 2 task: Raye reopen/basic audio/game check; retain paused source and later stronger campaign tests.
- GitHub/build task: One P1-only technical check; no idle repeated polling. No phone update/retest demanded just for invisible capture plumbing.
- Anything requiring my involvement: NONE to continue coding/CI. Both file transfers done; user already told phone can unplug and games need full close/reopen. Raye exact public iOS27.0.1 verified; no more need to ask model/version. Report only actual runtime failures when convenient.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Co-op explicitly authorized.54 very quick smoke check seems fine, not full campaign certification. Registry/Pikmin codec plus actual-engine read-only capture now exist, beyond previous Onion-only state. No live sessions started and NECTAR_ONLINE remainsOFF. Prototype capture compiled in CI via NECTAR_COOP_WORLD=ON but begins only via explicit future API; normal solo remains inactive. No original save format changed.
- Important source-file locations: ios/PIKMIN1_COOP_IMPLEMENTATION.md, SAVE_AND_COOP_RECOVERY_PLAN.md; new pc_coop_world_begin_host/pc_coop_world_capture/pc_coop_world_forget/pc_coop_world_end_scene in pc_port/netplay; HostEntityRegistry in libs/nectar_net; PikminState codec38bytes. Registry owner persists independently of current leader. Monotonic16-bit scene epochs must not wrap; transport session IDs must never be reused.
- Relevant logs: work/coop-capture-fixture, coop-capture-bin, coop-direct; coop-capture-negative.log; work/raye-p1/p2-import-progress.json and private source/transfer receipts. Public notes only metadata, no proprietary game files. New native run metadata saved in work/coop-capture-new-runs.json after push.
- Unverified fixes: Real iOS compilation of the new bridge until CI finishes; no two-iPhone actor/world synchronization/real network/reconnect/save proof. Post-import Raye game launch/audio pending. P154 rare bugs remain untested individually.
- Risks and warnings: Never serialize local addresses; guest packets must pass session/scene/lifecycle freshness and authenticated ownership checks. Capture records are NOT full AI/job/campaign or exact-scene snapshots. Do not treat each split datagram as a whole keyframe; full keyframe assembly/application must be atomic. Registry lifecycle hooks must precede pool reuse and heap reset. Read-only capture buffers currently belong to scene lifetime; future network queues require safe owned buffers across transitions. Preserve54/53/settings/AO OFF/user120 choice, avoid fourth-app requirement, no finale spoilers or security/account changes.
- Exact next actions: Record native source/run and clean Git state; inspect resulting compile after user reports completion; implement real iOS transport/handshake + guest visual/squad vertical on disposable data, then complete game authority/Onions and recovery. User/ Raye can meanwhile reopen both freshly populated apps; if still black inspect new evidence rather than re-copy blind.

**END PROGRESS REPORT**


<!-- BEFORE CAPTURE MILESTONE -->

# Open Nectar iOS — current status


**Date/time:** 2026-10-24 20:39 EDT

**Overall project status:** P1 Build54 native compile/IPA/package verification PASS; staged for a brief optional phone regression check. New game fixes are not hardware-verified. Co-op development has started with tested shared Onion accounting; online gameplay is not yet integrated. P2 unchanged. Raye reports iPhone17Pro/public non-beta iOS; exact version/connection later when available.

### Pikmin 1

- Current objective: Preserve user-confirmed53, verify54 and continue the controlled co-op prototype.
- What was investigated: Completed Actions run40145860255, successful scene/P1 jobs, full P1 job/build logs, both artifact hashes, simulator result, ARM64 executable, bundle identity/SDK/icons and expected feature markers.
- Root cause or leading hypothesis: Preventive fixes address confirmed source hazards and carrying timing; rectangle rounding addresses numeric edge mismatches. No new evidence establishes the cause of the earlier rare black-world/stranded pair/moving-line symptoms.
- Files changed: This verification phase changes documentation only. Build54 contains prior407b7fa4 game fixes and a7888f24 co-op foundation/CI, described in PIKMIN1_COOP_IMPLEMENTATION.md. No extra game changes or build triggered.
- Tests and results: Native iPhoneOS compilation PASS; actual-method rectangle161200 cases/zero mismatches + Onion/carrying/damage/slot tests PASS;15/15 offline network tests PASS on macOS; Apple ARM64 new-fixture/authority syntax checks PASS; actual asset-free iOS27.1 simulator launch/background/resume PASS. Package digest, ZIP, ARM64/iPhoneOS, original ID, scene support, icons and ProMotion permission verified. Simulator is not the game on real hardware.
- Confirmed working: User's installed53 graphics/touch/keyboard baseline, full native resolution/1.00x with AO OFF reported120FPS.54 compiled and produced a verified IPA; not installed/tested by this phase.
- Remaining issues: Online actor/world synchronization, registry/engine bridge, camera/session UI, internet invites/relay and snapshot/reconnect still need implementation. Rare campaign issues and full-story coverage remain unverified. User does not need to reproduce every preventive bug or replay the story for this batch; a short launch/settings/input/carry/pause/resume check can detect obvious regressions while53 stays preserved.

### Pikmin 2

- Current objective: Preserve working game; later stronger stability tests and separate co-op adapter.
- What was investigated: None newly; no P2 job in54.
- Root cause or leading hypothesis: No new P2 issue diagnosed in this phase.
- Files changed: NONE under games/pikmin2.
- Tests and results: No new P2 compile/runtime. Existing52 native/IPA verification retained; earlier32 gameplay/audio user-confirmed.
- Confirmed working: User's previous installed working P2;52 package exists but is not newly phone-verified.
- Remaining issues: Raye's first solo install/assets/basic test; later cave/area/save/campaign test before P2 online.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental.
- Starting commit:4b6111091a086fa332a152e958889c6df6687f9b (clean at entry). Build54 source=a7888f24009133fd3818355e35bfc5475c279e16; fixes=407b7fa4f5479aeeb983de5c84a234d03641291e.
- Latest commit: Documentation-only verification checkpoint pending at this report creation; exact final local/remote SHA saved in friendly Exact Resume State.json after push.
- Commits created: No new game-source commit in this verification phase; documentation checkpoint only.
- Changes pushed: Documentation-only with [skip ci], no P2 rebuild or extra P1 build.
- Uncommitted changes: Only current scoped verification journals before checkpoint commit; confirm clean after push.
- GitHub Actions run IDs:54=40145860255; scene job121026926855 and P1 job121029524253 both SUCCESS. Prior53=40133259493,52=40131000336.
- Build results:54 SUCCESS. All15 offline co-op/network tests and full native P1 job passed. No hardware/co-op session result claimed.
- Artifacts produced: P1 artifact12581053357 SHA256aa0a36f05371f82349bdbf80844b83da9cbce9195ae4a90542fb47d42cbbd0bc; scene artifact12580922615 SHA2566ff701b72c9a1ad4b8dc06c9a63b1b4f49f4d0353ddcc2d7d87d1363cb98158c. Staged IPA=C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\Pikmin 1 - Build 54 - Stability Update.ipa, 2835985bytes, SHA256cdf46924e6cb350eb1df571325254f55d0a479c4fab5e4e564ad950335b50ae5, executable UUID1760960b-2d27-3a21-960f-2dcc404350c6, original IDorg.opennectar.experimental.pikmin1, unsignedARM64/iPhoneOS SDK27.1/minimum15.0. Build53 original IPA rehashed and retained unchanged.

### Next steps

- Next Pikmin 1 task: Optional brief same-ID54 update/regression check; continue same-Wi-Fi disposable captain/squad prototype and actual engine registry/Onion bridge using the saved active plan. No full campaign/finale check demanded.
- Next Pikmin 2 task: Keep current game, no new build; Raye solo installation when ready.
- GitHub/build task:54 complete, no polling and no new build needed merely for documentation. Review any new actual failure before further fix.
- Anything requiring my involvement: Handle signing/install and brief phone feedback when convenient. Raye is using her iPhone17Pro now, so don't request immediate disconnect/use; exact public iOS version can be read when available. Her prepared P153/P252 folder remains unchanged until54 hardware feedback; nothing installed on either phone in this phase.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Co-op is explicitly authorized and underway; only the engine-free Onion authority is implemented.15 passing tests do NOT mean15 game/campaign scenarios or a real two-iPhone session passed. User asks whether rare fixes can be checked: explain automated targeted evidence plus a brief device regression check, not blind hope or a full story retest.
- Important source-file locations: ios/PIKMIN1_COOP_IMPLEMENTATION.md, ONLINE_COOP_DESIGN_NOTES.md, SAVE_AND_COOP_RECOVERY_PLAN.md; libs/nectar_net/onion_authority source/header/test; old captain adapter games/pikmin1/pc_port/netplay/pc_online_navi.cpp and pc_netplay_session.cpp. Normal online flags remainOFF until a usable integration exists.
- Relevant logs: outputs/Build54-Pikmin1/ios-build.log and ios-build-errors.md; work/build54-p1-full.log; work/build54-result-run/jobs/artifacts.json; work/build54-startup-runtime-verification.json; work/build54-verification.json. Friendly folder2 has verification/log copies.
- Unverified fixes: New54 device behavior, complete campaign, old NaN/black-world/stuck-rescue cases, all actual online gameplay/save/reconnect.
- Risks and warnings: Preserve53/settings, AO OFF and user-selectable120. No raw pointer/heap snapshot or arbitrary-tick normal-card writes. No fourth-app requirement, original save overwrite, host migration, paid relay/account changes or finale spoilers. Package backup isn't current phone-data backup. P2 remains paused.
- Exact next actions: Provide staged54/checklist → receive brief optional device result; independently advance controlled iOS transport/captain+squad vertical and registry/transaction bridge, then full host-owned world/recovery. Install Raye's P1/P2 once phone available, import private assets separately, validate her solo baseline before two-phone tests.

**END PROGRESS REPORT**


<!-- BEFORE BUILD54 VERIFICATION -->

# Open Nectar iOS — current status


**Date/time:** 2026-10-24 20:14 EDT

**Overall project status:** User accepted P1 Build53 as the current working solo baseline and explicitly authorized beginning online co-op now. Preventive P1 upstream batch implemented and locally checked. First host Onion accounting component implemented/tested, but NOT connected to game actors or live networking. Raye install copies prepared; no installation/phone data changes performed. Pushed a7888f24009133fd3818355e35bfc5475c279e16 to ios-experimental. Build 54, run 40145860255: in_progress / pending; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40145860255

### Pikmin 1

- Current objective: Preserve working53, incorporate selected upstream campaign fixes, begin controlled online co-op development.
- What was investigated: Upstream release1.0.8 and main a6b09bfe, prior co-op/save notes, actual nectar_net and pc_netplay_session/pc_online_navi adapters. Last fetched origin matched8af39affa4c0c863ccaa1b41dd8b96538836faaa before edits.
- Root cause or leading hypothesis: Actual carrying retry used60 ticks regardless of user FPS, making intended2seconds=.5seconds at120. Several existing null/uninitialized/out-of-bounds/cache-lifetime hazards are confirmed in source. Main shared-edge rounding removes numeric rectangle gaps. These are preventive fixes; none is established as the cause of the old stranded pair, NaN/black world or motion-line symptom.
- Files changed: aiTransport.cpp retry/debug format; creatureMove.cpp collision-exhaustion null dereference; Demo.h/demoEvent.cpp/cinePlayer.cpp skipped Onion first-seed completion; SnakeAi.cpp/SnakeBody.cpp slot/array guards; dayMgr.cpp invalid-time fallback; damageEffect.cpp absent-captain guard; DrawContainer.h/drawMenuBase.cpp UI safety; drawGameInfo.cpp portrait-cache lifetime; pc_gfx.cpp rectangle edge math. New tests/pikmin1_upstream_safety_test.py. Separate libs/nectar_net/onion_authority.h/.cpp/test and CMake test registration; P1-only workflow checks.
- Tests and results: Actual-method fixture PASS for rectangle edges161200 cases/zero mismatches, first-seed skip/repeat/normal completion, missing/damaged captains, full/missing enemy mouth/target, invalid/dead carry target and retry timing30/60/120. Two negative controls restore old retry/rectangle behavior and fail as intended. Offline nectar_net15 test executables PASS with MSVC/O2/W4/WX; includes existing200000 decoder fuzz iterations,30SIMULATEDminutes with5% packet loss (live tick ratio.9982) and new10000 withdrawal/return cycles/40000 deliveries. No actual30-minute or two-phone session claimed. Preserved-display fixtures70 native-pixel checks,1820 touch/resize/layout checks, keyboard ownership PASS; scene contract26 + runner12 tests PASS. Clang warning/diagnostic checks also PASS for the actual-method fixture and new authority source/test. Apple ARM64/full game CI pending for this source.
- Confirmed working: User's installed53 sharper image, manual control edges, keyboard closed. At full2853x2007/1.00x with Ambient Occlusion OFF, user reports120FPS; keep higher quality and selectable120. New fixes are source/local-test verified only.
- Remaining issues: New source not installed/runtime tested; full story/rare cutscene/rescue/old black-world not certified. Co-op world replication, actor registry, engine transaction bridge, transport on iOS, full-screen per-player view, invites/relay, shared save/reconnect NOT implemented by the new accounting module.

### Pikmin 2

- Current objective: Preserve working game; prepare latest compiled package for Raye's solo compatibility test. P1 co-op first.
- What was investigated: Existing package hashes and bundle IDs; no new P2 source work in this batch.
- Root cause or leading hypothesis: No newly reproduced P2 bug; earlier audio/gameplay user-confirmed. Future upstream audit candidates remain queued.
- Files changed: NONE under games/pikmin2; existing P2 jobs/normal runtime unchanged.
- Tests and results: Build52 source a575ecf424008c7430da96a5082ffb7f68970dc1, run40131000336 compiled/IPA verified earlier. Copied package rehashed now; no new52 phone validation. Older32 audio/gameplay baseline preserved.
- Confirmed working: User's previous installed P2 audio/gameplay; do not equate this with testing newer52 on Raye's phone.
- Remaining issues: New phone/model/iOS details pending; assets/import + first run pending; stronger later cave/area/save/long-session test before P2 online.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port ; upstream SSunnKing same project.
- Branch: ios-experimental.
- Starting commit:8af39affa4c0c863ccaa1b41dd8b96538836faaa (clean local=origin).
- Latest commit: a7888f24009133fd3818355e35bfc5475c279e16 at report creation. Exact post-report local/remote hashes are in friendly Exact Resume State.json after push.
- Commits created:407b7fa4f5479aeeb983de5c84a234d03641291e P1 preventive batch; co-op/checkpoint commit pushed above.
- Changes pushed: Pushed a7888f24009133fd3818355e35bfc5475c279e16 to ios-experimental. Build 54, run 40145860255: in_progress / pending; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40145860255
- Uncommitted changes: Only this updated documentation checkpoint before final skip-ci commit; verify git status.
- GitHub Actions run IDs: Build 54, run 40145860255: in_progress / pending; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40145860255 Previous53=40133259493 P1 SUCCESS,52=40131000336 P2 SUCCESS. No P2 build requested now.
- Build results: Current local tests PASS; current Apple compile/IPA/runtime not yet established.
- Artifacts produced: No new IPA from this source yet. Working P153 SHA256c483540e76cef95c002578724690fe8ebe649901b9a09906350ee0b93c5cff85; P252 SHA256fbf6b2512d91ccafc6c600ee8bddcdbbcef04a1c01ee0ea68da4c68fda40c793. Rehashed copies in Documents/Open Nectar/1 - Install on iPhone/For Raye - Start Here, with manifest and instructions. Original IPAs retained.

### Next steps

- Next Pikmin 1 task: Review one P1-only native run and verify artifact/package before an optional short carrying/Onion-skip/menu/resume hardware check. Preserve53 rollback and settings. Continue co-op actor/world vertical slice on disposable data.
- Next Pikmin 2 task: Raye solo install/asset import and basic audio/pause/resume test; no speculative P2 rebuild.
- GitHub/build task: Inspect the recorded run after completion; no idle polling.
- Anything requiring my involvement: Raye's iPhone model/iOS and connection/unlock when ready for installation; sign in/verification stays under user's control. A read-only USB inventory probe stalled and was stopped; no phone identified or modified in this phase. No need to keep the original game/phone connected for CI.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Current user explicitly says start P1 online co-op; old notes saying online is future-only are historical/superseded. P1 ready for controlled prototype does not certify every story path. Preserve solo runtime; network flags remainOFF pending a real integration, not abandoned co-op work.
- Important source-file locations: ios/PIKMIN1_COOP_IMPLEMENTATION.md and ONLINE_COOP_DESIGN_NOTES.md; libs/nectar_net for reusable transport/identity/codecs + new OnionAuthority; games/pikmin1/pc_port/netplay/pc_netplay_session.cpp and pc_online_navi.cpp for old captain-only adapter; ios/SAVE_AND_COOP_RECOVERY_PLAN.md for exact-scene recovery target.
- Relevant logs: work/p1-upstream-safety.cpp/exe; work/p1-negative-retry.log and p1-negative-rectangle.log; work/coop-direct generated binaries; work/coop-start-actions.json and coop-start-pushed-actions.json; previous53 hardware/config evidence remains in friendly folder2.
- Unverified fixes: All new game-source behavior needs Apple build and device test; ledger isn't connected to actors or saves. No new IPA installation, full-world sync, internet service or autosave occurred.
- Risks and warnings: Do not enable old online menu and claim full co-op. Existing WorldDelta sends captain records only; other world state still needs sync. Direct networking alone cannot guarantee state-away internet/NAT traversal. Old Gekko frame/hash handle isn't a world snapshot. Normal memory-card save remains between-days; no arbitrary-tick card writes. No raw heap/pointer serialization. P1 global actor cap must be reconciled with independent per-player allowances. No finale spoilers. No full current phone-data backup claimed.
- Exact next actions: Native run → verified artifacts; Raye solo install/assets → two-phone same-Wi-Fi captain+squad vertical; stable entity registry/Onion engine bridge; host-owned Pikmin/jobs/enemies/items/obstacles + separate camera; retained-host reconnect/pause and versioned exact-world snapshots; private invites/real internet/relay tests; then stronger P2 stability and its engine adapter.

**END PROGRESS REPORT**


<!-- PRE-COOP HISTORY -->

## Current progress report — Build53 phone baseline and upstream audit — 2026-10-24 19:48 EDT

**Overall project status:** P1 Build53 user-tested: sharper gameplay, wider manual controls, keyboard closed. Current high2853x2007/1.00x with AO OFF reports120FPS. Large43FPS dip recovered after AO Off at the same1902x1338, then user raised to full native and still reports120. User explicitly retains high quality; no graphics downgrade/code/build needed. Upstream audit completed; proposed preventive fixes NOT implemented in this audit.

### Pikmin 1

- Current objective: Preserve working53 and compare original upstream for campaign stability fixes before broader solo/co-op work.
- What was investigated: User screenshots; two read-only settings captures; published release API/web pages; fetched1.0.7/1.0.8/main source; relevant current-iOS diffs including older missing carrying timeout. Actual current/tag/main rectangle arithmetic compared locally.
- Root cause or leading hypothesis: AO is strongly isolated as main observed slowdown (not resolution alone). Moving lines remain unidentified. Missing upstream carrying/collision/Onion/enemy/menu/cache/numeric guards confirmed in source; none established as cause of reported NaN/black world or stranded pair.
- Files changed: Documentation ONLY: PIKMIN1_BUILD53_HARDWARE_RESULTS.md, UPSTREAM_1_0_8_IOS_AUDIT.md and current journals. No game source, config, phone data or workflow changed; no new CI.
- Tests and results: Standalone actual map_gx_rect comparison161200 cases: current and1.0.8 tag33910 adjacent-edge mismatches, latest main0. This proves missing numeric correction, not visible iPhone symptom. Current-renderer8 relative-quality arithmetic checks PASS.53 prior native/package/simulator checks retained; user reports targeted runtime success.
- Confirmed working: Sharper game display, farther manual control positioning, unwanted keyboard closed, current high-resolution120FPS user report with AO OFF and GPI pack still enabled. Position save/relaunch persistence and long-session heat were not separately confirmed. Following feels better;53 did not introduce new AI changes.
- Remaining issues: Full campaign, stranded-pair rescue, slow/single-file return and prior black-world/NaN remain open. Lower-resolution moving lines only revisit if they persist with AO OFF. No guarantee120 across all scenes/devices/heat conditions.

### Pikmin 2

- Current objective: Preserve installed working baseline; audit future stability candidates only.
- What was investigated: Upstream gate lifetime, interpolated transition, save/card scheduler, sample formats/buses, host readable-memory bounds and allocator differences; prior1.0.6 backlog.
- Root cause or leading hypothesis: Current source lacks several upstream defensive fixes, but user has not reported those new symptoms. New GX bounds lookup is not drop-in on Darwin (/proc/self/maps missing). Port-argument ARM64 scalar fix is already present independently; avoid blanket audio replacement.
- Files changed: NONE in game/source. Candidate list saved in shared audit.
- Tests and results: No new P2 tests/build/phone results. Prior52 native/IPA SUCCESS retained.
- Confirmed working: User's installed gameplay/audio baseline;52 package verification only, not new phone proof.
- Remaining issues: Later stronger full-campaign/cave/save test; queued fixes need targeted iOS adaptation and tests, no current P2 update requested.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; upstream SSunnKing same project.
- Branch: ios-experimental; starting clean local=origin802cd294fb9fc088da1da5233687a7674d4e3c32. Fetched upstream source/tags without merging or checking out another branch.
- Starting commit:802cd294fb9fc088da1da5233687a7674d4e3c32; current tested53 sourcec25ba6a79ed975ba5face0461805bbd330e99cee.
- Latest commit / commits created: Documentation-only audit/hardware checkpoint pending commit; final exact SHA saved in external resume JSON after push.
- Changes pushed: Only scoped journals/audit/hardware report; skip ci. No upstream fix imported and no P1/P2 build triggered.
- Uncommitted changes: Scoped documentation until checkpoint commit. Private screenshots/phone configs/fixture binaries remain outside Git.
- GitHub Actions run IDs:53=40133259493 P1+startup SUCCESS;52=40131000336 P2+startup SUCCESS. No new run for audit or AO setting.
- Build results: Latest source package53 compiled/verified; user runtime feedback establishes targeted improvements, not full story. Upstream candidates are source-reviewed only.
- Artifacts produced: No new IPA. Verified53 retained folder1, SHA256c483540e76cef95c002578724690fe8ebe649901b9a09906350ee0b93c5cff85. Public latest-release metadata, exact source refs, arithmetic fixture evidence and private graphics comparison saved under work and friendly folder2.

### Next steps

- Next Pikmin 1 task: Keep working full-native/AO-OFF configuration. Prepare a scoped preventive batch from audit: high-FPS carrying wait, collision/Onion/array/UI/cache guards and edge rounding after meaningful tests. Do not blindly merge main or claim this fixes follower/NaN issues. User's current request was comparison; adoption remains next work.
- Next Pikmin 2 task: Paused; saved later gate/interpolation/card/audio/bounds checklist.
- GitHub/build task: No run now. Batch related tested P1 backports for one later P1-only native build; preserve53 baseline and iOS platform changes.
- Anything requiring my involvement: Nothing now; phone may close/disconnect. No need repeat whole campaign or lower resolution for resolved AO slowdown. If lines recur with AO Off, brief moving-camera evidence can distinguish possible causes.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User asked retain high-resolution finding, then explicitly requested upstream releases/source comparison. Latest public release1.0.8 publishedOct22, tag6319c3e354be280ab796f2c2e2504e185ce8cf96. Main a6b09bfe5a11798b2239d6072bace2e85812f245 Oct24 has seven later commits. Audit includes missing older carry fix3dcd6f25. No code backported yet.
- Important source-file locations: Full source-specific matrix in ios/UPSTREAM_1_0_8_IOS_AUDIT.md. Hardware evidence and effective relative-resolution notes in ios/PIKMIN1_BUILD53_HARDWARE_RESULTS.md. Preserve scene/FBO/Retina/menu/touch/keyboard fork fixes.
- Relevant logs: work/upstream-latest-release-oct24.json; fetched refs; work/audit_upstream_rect_edges.py, upstream108-rect-audit.cpp/exe, check_upstream_rect.cmd; current/tag33910 vs main0 mismatches. work/build53-quality-comparison.cpp/exe8 checks. Private work/p1-build53-graphics-20261024-193524 and p1-build53-ao-off-20261024-193828; friendly folder2/Build53 - Private Graphics Comparison.
- Unverified fixes: All upstream candidates NOT implemented/native-tested here. Numeric edge fix is only a candidate for user's moving lines. Current FPS is user-reported, sustained thermal/full-story performance unverified. No new save/autosave/network feature.
- Risks and warnings: Release notes mention edge/VSync corrections that are not actually in fetched1.0.8 tag; the relevant changes are in main2b65f16a. Main also introduces large custom mission/campaign/model/menu/save changes; do not import them as a stability patch. Upstream NETPLAY.md newly declares old network code disabled/unmaintained; that is source status, not an instruction overriding our user's future co-op goal. Do not assume existing netplay is production-ready.
- Exact next actions: Use audit priorities to implement/test one P1 preventive batch when continuing development; preserve existing enhancements and profile. Leave P2/graphics config untouched. Continue separate follower/NaN investigation. Report source, CI, IPA and phone milestones distinctly.

**END PROGRESS REPORT**

---
## Earlier checkpoint history

## Current verified package — P1 Build53 SUCCESS — 2026-10-24 17:53 EDT

User reported PASS; verified directly. Run40133259493/sourcec25ba6a79ed975ba5face0461805bbd330e99cee, startup job120989318144 and P1 job120991599668 both SUCCESS. This is the requested P1-only cumulative display/control/keyboard package. No P2 job or installed-app changes. Prior in-progress notes below are historical.

### Pikmin 1

- Current objective: Phone test53 for gameplay clarity/native landscape resolution, control edge placement/persistence/hitbox, and unwanted keyboard on startup/background resume.
- What was investigated: Full successful job log; exact run/source/artifact identities; package digest/ZIP/ARM64/platform/SDK/minOS/original standard P1 identity/icons/scene manifest and compiled scene selectors; actual generic simulator initial/background/resume evidence.
- Root cause or leading hypothesis:51 corrected portrait/logical-point render budget and editor safe-frame clamping.53 includes already-committed keyboard guard: iOS ends active/shown text input during gameplay while leaving the existing randomizer editor available. Exact original keyboard trigger still unidentified; guard runtime remains a candidate until user test. Prior NaN coordinates may relate to black world but root cause NOT established.
- Files changed: No new game/source change during this result-handling turn. Source53 contains P1 pc_window.cpp guard plus51 settings/window/gl/touch corrections and actual-code regression/workflow checks. Only result journals committed now.
- Tests and results: CI1820 actual layout/editor/persistence checks and70 pixel/migration/budget checks PASS; actual keyboard helper iOS+desktop host checks PASS and Apple syntax step PASS. Existing24 surface/140 route/283 walking/105 command and campaign/storage/profile regressions PASS. Full native compile/link/package PASS. Actual generic iOS27.1/iPhone Duo scene startup and same-PID background/resume PASS; does not certify game behavior.
- Confirmed working: Exact package generated and verified. Prior installed50 user-visible gameplay and earlier audio/content baseline retained;53 installation/runtime NOT yet reported. No assertion that all navigation or full campaign works.
- Remaining issues: Slow/single-file return and reported unrescued pair UNCHANGED; black-world/NaN origin UNRESOLVED. No such fixes in53. Native resolution1.00x may cost more GPU/memory; player retains resolution/scale/FPS choices incl120.

### Pikmin 2

- Current objective: Preserve working installed app; no new test/update required for current P1 task.
- What was investigated: No new P2 source or phone evidence.52 native/IPA verification already completed.
- Root cause or leading hypothesis:52 corrected the stale P2 pixel-budget test after shared51 source; no new reported P2 gameplay defect.
- Files changed: NONE.
- Tests and results:52/run40131000336 SUCCESS; verified P2 IPA preserved.53 built P1 only.
- Confirmed working: User's existing P2 audio/gameplay baseline remains authoritative, newer52 runtime unverified.
- Remaining issues: Full campaign and optional52 display/edge hardware checks remain unverified; P2 work paused while P1 prioritized.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; local C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental. Fetched clean local=remote d49e309013e35f93c81f00daf88c582ef272c378 at start of this result turn.
- Starting/latest commit: Starting journal d49e309013e35f93c81f00daf88c582ef272c378; verified build sourcec25ba6a79ed975ba5face0461805bbd330e99cee. Result-only skip-ci commit SHA recorded in external exact resume JSON afterward.
- Commits created / changes pushed: Only successful package/test/handoff documentation; no extra build requested.
- Uncommitted changes: Only scoped journal before result commit; no private evidence, IPA or game assets staged.
- GitHub Actions run IDs:53=40133259493 SUCCESS P1+startup;52=40131000336 SUCCESS P2+startup;51=40109396851 P1+startup SUCCESS/P2 obsolete host assertion FAIL. No active build requested.
- Build results:53 native tests/compile/link/package and generic simulator PASS; real phone installation/runtime PENDING.
- Artifacts produced: P1 artifact12576271886 ZIP SHA25692d6b8da27ea1e406f210e1234e8b0d3cfee09efb2a36bcc9325076783f5aa4c. IPA2835584bytes SHA256c483540e76cef95c002578724690fe8ebe649901b9a09906350ee0b93c5cff85; executable UUID92456923-027a-3544-9d20-51a2166eed02; original org.opennectar.experimental.pikmin1 unsigned ARM64 iPhoneOS SDK27.1/min15; approved icons/landscape/ProMotion flag intact. Staged folder1/Pikmin 1 - Build 53 - Display Controls and Keyboard.ipa with verification JSON. Scene artifact12576885117 ZIP SHA2565ff42ff3b41f48dc0db82292c676452ebe5a59ac71508d7532467f2b84a80a46 verified. Older51/50/42 and P2 packages preserved.

### Next steps

- Next Pikmin 1 task: User updates existing app same account/identity without uninstall/reset; follows folder1/Pikmin 1 - Build 53 - TEST THIS.txt. Compare actual landscape dimensions/game clarity at1.00x, manual control edge/save/reload/tap, Home Screen10sec/return twice and menus for keyboard, basic input. Do not ask full campaign solely for this test.
- Next Pikmin 2 task: None now; installed app untouched.
- GitHub/build task: No new run or idle polling. On phone regression use exact53 UUID above and bounded diagnostics. Future P1 work: trace NaN origin and improve stuck/slow return with evidence and meaningful crowded/oscillation tests.
- Anything requiring my involvement: Install/test53 when ready. No USB connection or open game required now. If still blurry send gameplay and Display screenshot; report keyboard/black event separately. Do not install51 first.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User explicitly requested this P1 build because guard was previously only committed while52 P2-only ran.53 now successfully packages it with all51 display/control corrections. Only package/source/host/simulator milestones established; hardware still pending. Keep scope clear and do not conflate P2 test cleanup with P1 runtime work.
- Important source-file locations: games/pikmin1/pc_port/pc_window.cpp pc_window_update_text_input/poll_events/set_window_size; settings rebuildResolutionList; gl pc_gfx_begin_frame; touch ButtonLayout.fullBounds/layout_place/load/save; tests/pikmin1_ios_keyboard_test.py; ios_display_layout_test.py; ios_pixel_resolution_test.py. AI/NaN diagnostics remain in aiCrowd.cpp/piki.cpp/navi.cpp and private Oct24 collected navigation report.
- Relevant logs: work/build53-result-run.json, build53-result-jobs.json, build53-artifacts.json, build53-p1-full.log, build53-verification.json, build53-startup-runtime-verification.json; work/verify_stage_build53_p1.py; outputs/Build53-Pikmin1 exact IPA/checked bundle/compiler log. Friendly folder2 copies of verification/full job/simulator evidence. Private phone evidence stays local.
- Unverified fixes:53 phone sharpness/edge persistence/keyboard behavior; no AI/black-world fix implemented. Prior single rescue log cannot identify the reported pair. CPU resource report says action NONE, not a crash diagnosis.
- Risks and warnings: Preserve original installed app/settings/content and player FPS choice. No complete current phone save/assets backup; package backups do not contain phone data. Do not force-push/main merge/reset/uninstall/upload assets. No spoilers.
- Exact next actions: User tests53; capture results and update journal. For failure retrieve matching current logs without overwriting prior evidence. Continue P1 recovery/NaN research; P2 stays paused. No new CI until relevant source correction warrants it.

**END PROGRESS REPORT**

---
### Earlier checkpoints (historical)

**DISPATCHED:** P1-only Build53/run40133259493, sourcec25ba6a79ed975ba5face0461805bbd330e99cee, startup job120989318144 IN PROGRESS at last inspection. Link: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40133259493. Contains native landscape pixels + manual control edges + keyboard ownership guard. Local keyboard iOS/desktop MSVC and Clang PASS; Apple compilation/new IPA and phone results PENDING. No new P2 job requested. No additional idle polling; user reports completion. Next retrieve logs and verify exact P1 IPA before staging. Old51 is preserved but user need not install it first. No AI/black-world fix claimed.

## Current action — P1-only package including keyboard guard — 2026-10-24 17:13 EDT

User explicitly requested packaging the pending P1 fixes now. Prepare ONE P1-only workflow run from current branch. No new P2 build is needed. Starting local/remote64f8276f95dbda7c9b660529579a24cbcbc315b1 clean and fetched.

### Pikmin 1

- Current objective: Produce a single standard P1 update containing all already-implemented display/control-placement changes plus the new keyboard guard.
- What was investigated: Confirmed P151 source contains physical landscape render budget/native migration and manual edge persistence; confirmed fb7880f6 adds pc_window_update_text_input before event polling and keyboard actual-helper host/Apple workflow checks.
- Root cause or leading hypothesis: Low portrait/logical-pixel budget and safe-frame editor clamp corrected in51. Keyboard guard defensively ends text input/shown IME outside the randomizer editor; exact UIKit trigger still unidentified. This is a candidate correction, not phone runtime proof.
- Files changed: Existing P1 pc_window.cpp keyboard guard and tests/pikmin1_ios_keyboard_test.py/workflow are already committed. This trigger changes journal only to build the current cumulative source; no fabricated additional gameplay fix.
- Tests and results: Actual P1 keyboard helper MSVC iOS/desktop PASS and Clang both variants PASS immediately before dispatch.51 actual pixel/layout/native game/IPA and shared simulator gate PASS retained. New Apple build/IPA/phone PENDING.
- Confirmed working: Prior installed50 visible game and one fresh/resume test;51 compilation and package verified, not user-installed. Prior rescue log contains one uncorrelated relocation, not confirmation of reported pair.
- Remaining issues: Slow/single-file following, reported missed two rescues, and black-world/NaN origin UNRESOLVED and unchanged in this candidate. Avoid presenting this as an all-bugs-fixed build. User FPS incl120 retained.

### Pikmin 2

- Current objective: None for this run; preserve working installed app and verified52 IPA.
- What was investigated:52 final native/tests/package and simulator metadata previously verified.
- Root cause or leading hypothesis:51 P2 test expected old699x323 budget; corrected52 actual2097x968 physical budget.
- Files changed: NONE in this run.
- Tests and results:52 successful;409 iOS/302 desktop and native/link/IPA PASS. No new P2 phone test.
- Confirmed working: User's older installed audio/gameplay baseline remains authoritative.
- Remaining issues: Full campaign and52 display/edge hardware validation pending; P2 update optional, not current priority.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental; start64f8276f95dbda7c9b660529579a24cbcbc315b1 local=remote, clean; no incoming change.
- Latest commit / commits created / changes pushed: P1-only build trigger with this journal is being committed now; exact source and run saved in dispatch checkpoint afterward.
- Uncommitted changes: Only scoped journal update before commit. Existing source/tests already committed.
- GitHub Actions run IDs / build results / artifacts: New P1-only run pending dispatch.52/run40131000336 sourcea575ecf424008c7430da96a5082ffb7f68970dc1 SUCCESS P2;51/run40109396851 source1450d21e1f60c9600c8556371e6f8f2f55cd7130 P1 and shared startup SUCCESS, P2 host test failed. Verified51 P1 and52 P2 IPA retained in folder1; new IPA not yet generated.

### Next steps

- Next Pikmin 1 task: On build completion retrieve logs and verify exact original-ID ARM64 IPA/scene/icons/digest, then stage ONE clearly named current P1 update in folder1. Ask user to test native landscape clarity, control edge/save/reload/hitbox and background/resume keyboard behavior. Do not require51 installation first: new successful package supersedes51 for this test.
- Next Pikmin 2 task: No new action/build/install now.
- GitHub/build task: Capture exact P1-only run/source/job; stop idle CI polling per user preference. User reports completion; no duplicate build.
- Anything requiring my involvement: Nothing on phone while build runs; phone/game may close/disconnect. No reset/uninstall needed. Test after new IPA verified.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User was confused because keyboard was committed but not built while a P2-only test retry ran. They now explicitly requested P1 build; package the already-tested cumulative source now, no need wait for AI/black-world work to finish. Explain unresolved issues accurately.
- Important source-file locations: P1 pc_window_update_text_input, pc_window_poll_events, pc_window_set_window_size; settings rebuildResolutionList and resolution migration; gl pc_gfx_begin_frame; touch ButtonLayout.fullBounds/manual placement/save/load; new keyboard regression/workflow.
- Relevant logs: work/p1-keyboard.cpp/exe, check_p1_keyboard.cmd, check_p1_keyboard_clang.cmd; earlier build51 and52 verification and private Oct24 phone diagnostics retained.
- Unverified fixes: Keyboard correction has only host verification until this new Apple build; all display/control/keyboard phone behavior pending. No AI/black-world correction implemented.
- Risks and warnings: Preserve installed apps/data and user-selected FPS; native1.0x costs more GPU/memory than old logical budget. No game assets/private data in Git. No force-push/main merge/reinstall/reset.
- Exact next actions: Dispatch P1-only, capture run/source, commit result-only checkpoint with skip ci; return build link and wait for user to report completion. After success verify and stage, then targeted phone test. Continue AI/NaN investigation independently when actively working, but do not claim this build includes those fixes.

---
### Previous checkpoint (historical)

## Current result and scope clarification — 2026-10-24 17:06 EDT

P1 is the active user priority. User explicitly clarified that “done” meant GitHub Build52 finished, NOT that P1 Build51 was installed. No new P1 hardware outcome should be inferred.

- P1 Build51/run40109396851/source1450d21e1f60c9600c8556371e6f8f2f55cd7130: native compilation/IPA and generic simulator startup/resume PASS. Changes ONLY correct physical landscape render resolution and manual control placement/persistence at screen edges. Verified original-ID IPA is folder1/Pikmin 1 - Build 51 - Native Pixels and Control Edges.ipa. Hardware sharpness/edge behavior pending. It does NOT include the keyboard guard, rescue/pacing changes, or black-world correction. Those problems may still occur.
- P1 keyboard guard: committed fb7880f66045035ec7cc53a945f34533a71c2c2c AFTER51 and AFTER52 source, host iOS/desktop helper tests PASS; native/IPA/phone pending, no package contains it yet. P1 stuck-pair, slow return and black-world root cause remain unresolved. Prior saved phone log had one uncorrelated rescue and later NaN captain coordinates. No claim of a complete fix.
- P2 Build52/run40131000336/sourcea575ecf424008c7430da96a5082ffb7f68970dc1: COMPLETED SUCCESS. Startup job120982491334 and P2 job120984917508 PASS. This retry changed only the test expectation after shared51 physical-resolution changes:699x323 old logical budget to2097x968 physical budget at.75.409 iOS and302 desktop actual-code checks PASS in CI, full game native/link/IPA PASS. No new P2 gameplay/audio change and no new user P2 bug report. P2 update is optional; keep working installed P2 untouched while focusing P1.
- P2 artifact12575447436 ZIP SHA256b21f25d5b14913dd4fae3eec73819c9121d5bec18c9660032ad853ae6357753e verified. Exact original-ID ARM64 iPhoneOS/SDK27.1/min15 unsigned IPA4161397bytes SHA256fbf6b2512d91ccafc6c600ee8bddcdbbcef04a1c01ee0ea68da4c68fda40c793, executable UUIDef989bd1-fc9a-37d2-92df-bc2bb62fe182. Approved icons and scene manifest/compiled selectors PASS. Staged folder1/Pikmin 2 - Build 52 - Native Pixels and Control Edges.ipa for preservation, not automatically installed.
- Scene artifact12575616448 ZIP SHA256e97a04ed04b706d54808b5c2c9a2c85cbe8d574a620961630f009d3a6a54be1b verified; actual generic simulator one-entry, landscape, foreign-event filtering and same-PID background/resume PASS. Does NOT certify either game's actual runtime.
- Repository fetched and clean local=remote fb7880f66045035ec7cc53a945f34533a71c2c2c before this result-only documentation update. This update uses skip ci; no new build. No phone modifications, private/proprietary uploads, P1 source changes or installation performed.
- Evidence: work/build52-result-run.json, build52-result-jobs.json, build52-artifacts.json, build52-p2-full.log, build52-verification.json and build52-startup-runtime-verification.json; outputs/Build52-Pikmin2; friendly verification/full-log copies in folder2.
- Exact next actions: Focus P1. Explain51 scope plainly; if user installs51, verify physical landscape Resolution/native1.0x clarity and control edge drag/save/reload. Existing keyboard/pacing/black issues stay tracked separately. Continue tracing invalid actor coordinates and recovery eligibility; next P1 fix batch should include already-committed keyboard guard with actual tests. Do not create another P2 build without new evidence. No idle CI waiting or further immediate phone-connection requirement. Preserve working installs/settings and all previous packages.

---
## Earlier investigation report (historical; current status above supersedes pending build text)

## Latest continuation — keyboard guard locally verified; P2-only52 dispatched

Build52/run40131000336/sourcea575ecf424008c7430da96a5082ffb7f68970dc1 is IN PROGRESS for P2 only after correcting the stale native-pixel fixture. No idle polling. Source parent cf4e959c;51 source1450d21e and its mixed results retained above.

After the report below was written, user provided a photo of the keyboard obscuring normal gameplay. Added P1-only pc_window_update_text_input in games/pikmin1/pc_port/pc_window.cpp, invoked before event polling: iOS stops text input/hides a shown keyboard outside the existing randomizer editor. Existing editor remains exempt, and desktop unchanged. This addresses text-input ownership defensively; the exact UIKit event that summoned the keyboard remains unidentified. Actual helper regression tests/pikmin1_ios_keyboard_test.py passes both iOS and desktop host variants. Next P1 workflow includes host variants plus Apple syntax check. Native and phone verification PENDING. This source is intentionally committed WITHOUT another build while52 runs; include in next P1 batch.51 staged IPA does NOT contain this new keyboard guard.

P1 root cause of NaN captain coordinates, black world, slow followers and missed rescues remains UNRESOLVED. No changes to movement/rescue/saving were made this turn. One fresh-launch and one background/resume check showed the world; that does not reproduce or solve prior black world. Existing evidence collected, user may close game/disconnect. No current further phone task.

# Current checkpoint — Oct24 phone feedback and Build51 result

51 P1 PASS and verified IPA; P2 host assertion FAILED before game compilation, corrected locally409/302+Clang. Phone P150: slow return, reported stranded pair, enabled rescue with one uncorrelated rescue log, later NaN captain coordinates/world-black unresolved. Fresh launch/resume visible once; unexpected keyboard now reported. Read latest progress/handoff first. P2-only retry next; no new P1 AI/black/keyboard source fix.

CURRENT — 2026-10-24 11:58 EDT: RESUMED. P1 photo466x678 portrait budget at1.00x/120; actual50 source reproduces466x320 landscape world. Both ports physical-pixel/native-follow and manual full-view button persistence implemented.1820+70 actual host checks, Clang and50 negative control PASS; Apple/IPA/hardware PENDING. Build51/run40109396851/source1450d21e1f60c9600c8556371e6f8f2f55cd7130/startup job120917764682 dispatched; native/runtime results PENDING.50 verified IPAs remain current backups. No phone needed/no idle polling; FPS unchanged.

CURRENT — 2026-10-24 11:57 EDT: RESUMED. P1 photo466x678 portrait budget at1.00x/120; actual50 source reproduces466x320 landscape world. Both ports physical-pixel/native-follow and manual full-view button persistence implemented.1820+70 actual host checks, Clang and50 negative control PASS; Apple/IPA/hardware PENDING. One combined startup-gated build pending commit/push.50 verified IPAs remain current backups. No phone needed/no idle polling; FPS unchanged.

CURRENT — 2026-10-23 15:06 EDT: PAUSED by user.50 P1 screenshots show title/gameplay/settings, but blurry world and editor invisible drag boundary reported. Resolution466x678 portrait-shaped,3D1.00x,FPS120; internal render/coordinate mismatch leading hypothesis only. No display correction/build performed. Documentation-only uncommitted pause note; no push. Resume only on user request.

CURRENT — 2026-10-23 14:57 EDT:50/run40003458275/sourceae2d68db907cf399699c6d0ebf3b6df856a85b68 ALL3 JOBS SUCCESS. Actual iOS27.1/Duo generic simulator startup+resume PASS; both games native/link/IPA PASS. Exact original-ID unsigned ARM64 device packages verified/staged folder1, phone installation/runtime PENDING. P1 FIRST launch/resume checklist, then P2. Original icons/min15/landscape/player120 retained; settings/assets unchanged on PC/phone.42/32 backups hash-verified/copied folder5; no complete current phone-data backup. No new build needed; success docs [skip ci].

CURRENT — 2026-10-23 14:28 EDT:49/run40000088460 SDL2/probe compile PASS; simctl folder query get_app_container hung180s BEFORE LAUNCH, games SKIPPED/no IPA. Cause of service hang unknown; folder query removed entirely, native report read from captured stdout instead.26 contract +12 runner/transport host checks PASS; latest native/runtime pending.48 test-only scope fix not executed by49. Build50/run40003458275/sourceae2d68db907cf399699c6d0ebf3b6df856a85b68/startup job120585264288 dispatched; result PENDING.44 withdrawn/45 HOLD/installed P2 preserved; landscape/120 selectable. No phone needed/no idle polling.

CURRENT — 2026-10-23 14:26 EDT:49/run40000088460 SDL2/probe compile PASS; simctl folder query get_app_container hung180s BEFORE LAUNCH, games SKIPPED/no IPA. Cause of service hang unknown; folder query removed entirely, native report read from captured stdout instead.26 contract +12 runner/transport host checks PASS; latest native/runtime pending.48 test-only scope fix not executed by49. Replacement combined gated build not yet dispatched.44 withdrawn/45 HOLD/installed P2 preserved; landscape/120 selectable. No phone needed/no idle polling.

CURRENT — 2026-10-23 14:03 EDT:48/run39995580595 CONFIRMED test-harness fault: fake UIScene notification broadcast with NSObject crashes UIKit keyboard _sceneIdentifier. Native compile/partial scene entry-window-landscape-reconnect PASS; readiness/resume/game builds NOT completed; games SKIPPED/no IPA. Probe now directly invokes actual SDL filter (no global broadcast),26 contract +9 runner checks PASS. Build49/run40000088460/source8449ef4c23820434f652c1e88fc7d94206c8302a/startup job120573614837 dispatched; no result yet.44 withdrawn/45 HOLD; installed P2 preserved. Landscape/player-selected120 retained; phone not needed/no idle polling.

CURRENT — 2026-10-23 14:02 EDT:48/run39995580595 CONFIRMED test-harness fault: fake UIScene notification broadcast with NSObject crashes UIKit keyboard _sceneIdentifier. Native compile/partial scene entry-window-landscape-reconnect PASS; readiness/resume/game builds NOT completed; games SKIPPED/no IPA. Probe now directly invokes actual SDL filter (no global broadcast),26 contract +9 runner checks PASS. Next combined gated build not yet dispatched.44 withdrawn/45 HOLD; installed P2 preserved. Landscape/player-selected120 retained; phone not needed/no idle polling.

CURRENT — 2026-10-23 13:30 Eastern Daylight Time:47/run39992850789 SDL2/probe native compile PASS; simulator readiness FAIL (empty report), cause UNRESOLVED; game jobs SKIPPED/no IPA. Diagnostic capture/early phases/raw stderr/own crash reports/newest runtime/runner reliability implemented;9 host runner +24 contract PASS, not UIKit proof. Build48/run39995580595/sourced8327ffd5ae114b4617c824c1bfacbd689d2d58c/startup job120558124436 dispatched; last observed in progress, no result yet.44 P1 withdrawn/45 P2 HOLD, installed P2 preserved; landscape/player FPS120 retained. Phone not needed; no idle polling.

CURRENT — 2026-10-23 13:29 Eastern Daylight Time:47/run39992850789 SDL2/probe native compile PASS; simulator readiness FAIL (empty report), cause UNRESOLVED; game jobs SKIPPED/no IPA. Diagnostic capture/early phases/raw stderr/own crash reports/newest runtime/runner reliability implemented;9 host runner +24 contract PASS, not UIKit proof. Next combined gated diagnostic run not yet dispatched.44 P1 withdrawn/45 P2 HOLD, installed P2 preserved; landscape/player FPS120 retained. Phone not needed; no idle polling.

CURRENT — 2026-10-23 13:10 Eastern Daylight Time: Build46/run39991097065 FAIL in SDL CoreAudio:2 undeclared UIScene names/1 missing-header cause. Runtime NOT RUN; games SKIPPED; no IPA. Owning UIScene.h added under iOS scene guard,24 local checks incl missing-import negative PASS. Build47/run39992850789, source2034e139369df84f61fd499d0d085b4e567b1d78, startup job120548733186: dispatched, no result yet. P144 phone launch FAIL/DO-NOT-INSTALL; P245 native PASS/installation HOLD; installed P2 untouched. Player-controlled120; landscape only. Phone not needed; no idle polling.

CURRENT — 2026-10-23 13:09 Eastern Daylight Time: Build46/run39991097065 FAIL in SDL CoreAudio:2 undeclared UIScene names/1 missing-header cause. Runtime NOT RUN; games SKIPPED; no IPA. Owning UIScene.h added under iOS scene guard,24 local checks incl missing-import negative PASS. Next combined build not yet dispatched; scoped source/local verification complete. P144 phone launch FAIL/DO-NOT-INSTALL; P245 native PASS/installation HOLD; installed P2 untouched. Player-controlled120; landscape only. Phone not needed; no idle polling.

CURRENT — 2026-10-23: Build46/run39991097065/source0f61ee4163ea4b47f668f50ed1f1e3511149b3bd, scene-startup gate job120542742441 IN PROGRESS. BOTH game jobs wait for actual asset-free simulator launch/background/resume PASS. P144 confirmed phone startup FAIL;44 marked DO-NOT-INSTALL and archived. P245 native/IPA PASS but HOLD installation (same shared missing-scene exposure). New UIScene source implemented,20/39/6 host checks PASS, actual44 package rejection PASS; Apple/native/IPA/phone pending. Player-controlled FPS incl120, landscape only. No phone connection needed; no idle polling.

CURRENT — 2026-10-23: P1 Build44 PHONE LAUNCH FAIL. Three reports at09:09:45/47/49 EDT UUIDb0e12e37-9091-3a54-b3ac-27222d5013b1 match44; UIKit EXC_BREAKPOINT ___UIApplicationEvaluateRuntimeIssueForNoSceneLifecycleAdoption_block_invoke before game entry. Confirmed SDK27 requires UIScene; bundled SDL2 lacks it. Shared startup migration required for BOTH games. P2 Build45/run39958190774 native/link/package SUCCESS; HOLD installation due same shared startup omission (P2 runtime not tested). P1 bad44 install file marked DO-NOT-INSTALL and archived;42 original backup retained. No phone writes; Documents read denied, no current save/settings backup claimed. Phone can disconnect. No forced60; landscape-only retained.

CURRENT — Build45/run39958190774/sourcedd5683cec866d7f96f6fe5dcc2321b2d8426a088/P2-only job120429205992 IN PROGRESS. P2 JSGGetName const override correction localPASS; native/IPA pending. Build44 P1 unchanged original-ID IPA VERIFIED/READY in folder1, phone pending. No P1 rebuild or idle polling; fps user-controlled incl120, landscape-only.

CURRENT — 2026-10-23 09:03 EDT: Build44 P1 native/IPA PASS; unchanged original-ID SDK27.1 ProMotion IPA VERIFIED/READY in folder1, phone pending. P2 FAIL:1 unique JSGGetName const override mismatch repeated6 times. Declaration/definition corrected;4+3 signature/dispatch checks and Clang PASS, old-source compile FAIL expected. P2-only retry next; P1 not rebuilt. Player-controlled FPS incl120, landscape only.

CURRENT — 2026-10-23: Combined Build44/run39950748289, source5f09f653b26d821079642ad23237c88ccd87b73d IN PROGRESS, jobs120404306153/120404306409. Duplicate43 cancellation accepted202. Adaptive landscape LOCAL PASS1778+409/302+39+6, Clang PASS; native/IPA/phone pending. LANDSCAPE ONLY, player-controlled FPS INCLUDING120; no forced60. Phone not needed; no idle polling.

CURRENT — 2026-10-23 08:04 Eastern Daylight Time: BOTH games adaptive-landscape batch LOCAL PASS (1778 shared integration,409/302 menus,39 identity,6 icons; Clang PASS). Native/IPA/phone PENDING. LANDSCAPE ONLY; player controls FPS,120 FPS retained and ProMotion permission added (NO forced60 cap). New SDK27.1 workflow; preserve42/P2-32 baselines. No gameplay/audio/save edits. See latest progress report/master handoff.

CURRENT — 2026-10-22 18:15 EDT: Build42/run39861241129/sourcedbe796adb057d0d5c92b37ad9f5976143d5329ba native/link/IPA SUCCESS. Exact original-ID standard ARM64 IPA verified/staged in folder1, SHA256304ac9abd4c60d96d76eb95902a0716ab743a074b1c69003aad238f7f7efd6a1. New pacing and automatic TELEPORT phone tests PENDING. Prior41 was too slow; user did not test teleport. No new build needed; focused box/drop/group test next. P2 untouched.

<!-- P1_PACING_CHECKPOINT -->
CURRENT — 2026-10-22 17:56 EDT: Build41 phone NORMAL FOLLOWING TOO SLOW; automatic TELEPORT UNTESTED per user. Actual-input fix preserved. Pacing source changes: ordinary following until measured stall, descent before trail mutation, route completion hands back successfully; retain distant assignments.140/105/58+58+7 and Clang PASS; actual41 negative controls8+1 failures. Build42/run39861241129, sourcedbe796adb057d0d5c92b37ad9f5976143d5329ba, last observedin_progress; no conclusion yet. New Apple/IPA/phone pending. Phone read complete/no writes; may disconnect. P2 untouched.
<!-- END_P1_PACING_CHECKPOINT -->

CURRENT — 2026-10-22 17:36 EDT: Build41/run39854014424/source769880462e9b0b8d2d139e0404fad015a741709f native/link/package SUCCESS. Exact GitHub IPA structurally verified and staged in folder1; SHA256cd359d0f475b8928bcef5290f6b04a592e8e78223d09150424b2e7b6a60e39b6. Rescue Stuck Followers defaultOFF; enable for focused worker-preserving crossing test. Phone runtime PENDING. Idle ship Recall All unexplained. P2 unchanged. No new build needed; user may disconnect. See latest handoff/checklist.

<!-- P1_AUTO_RESCUE_CHECKPOINT -->
CURRENT — 2026-10-22 17:03 EDT: Build40 PHONE NAVIGATION FAIL, including100% speeds. Actual-input recovery guard correction and optional Rescue Stuck Followers(defaultOFF) implemented. User approved auto rescue after~8s stalled+failed walk, existing followers only, safe dry landing/enemy/occupancy guards and cooldowns. Local128/24/103/283+283/58+58+7/39 checks and Clang PASS. Idle ship recall unresolved; diagnostics added. Build 41, run 39854014424, source 769880462e9b0b8d2d139e0404fad015a741709f; last observed in_progress (no conclusion). No idle polling. No new Apple/IPA/phone success. P2 unchanged. Read-only phone collection finished; may disconnect. See PIKMIN1_FOLLOWER_RECOVERY_DESIGN.md.
<!-- END_P1_AUTO_RESCUE_CHECKPOINT -->

CURRENT — 2026-10-22 09:30 EDT: Build40 compiled/linked PASS; Xcode combined icons into TIFF, GitHub packaging FAIL. Exact compiled app recovered; locally verified original-ID standard ARM64 IPA READY in folder1, SHA25602d057e55a2e77a0779462f37e420c2a5e665fa01c6523ee6c4129f1e65f7cdd. Original executable/all original files unchanged, six PNGs added.39 packaging regression checks PASS. Phone test pending. Safeguard commit [skip ci], no new build needed; P2 untouched.


CURRENT — 2026-10-22 09:11 EDT: Build40/run39784525620 QUEUED, sourcece63c20c4ad258d202e2ccb47f36cb18c201bd4c. Build39 compiled/linked successfully but failed missing-icon packaging. Target-directory package properties corrected;6 host configuration/negative controls and27 identity checks PASS. Native bundle/IPA/phone pending. Apple fixture will verify actual icon copying. Compiled app recovery archive added. P2 unchanged; phone not needed; no idle polling.

CURRENT — 2026-10-22 09:09 EDT: Build39 native compile/link PASSED; strict packaging failed missing icons. TARGET_DIRECTORY resource scope corrected,6 real configuration/negative controls and27 metadata checks PASS. Replacement P1-only build pending. No phone or IPA v2 result; P2 untouched.


CURRENT — 2026-10-21 16:01 EDT: Build39/run39666676388 QUEUED, sourcea7075569c07b75655ea78a151a8940303ad354ba. Build38 confirmed icon target-scope configuration failure corrected;4 real CMake regression/negative controls and27 metadata checks PASS. Navigation retained; Apple/IPA/phone pending. User reports completion; no idle polling. P2 untouched; phone not needed.

CURRENT — 2026-10-21 16:01 EDT: Build38/run39664622876 FAILED at CMake configuration: icon POST_BUILD target created in child directory. Native game compile skipped, no IPA. Corrected to native RESOURCE files;4 real cross-directory checks with old-error negative controls and27 identity/storage checks PASS. Navigation source unchanged. Replacement P1-only build pending. Phone not needed, P2 installed baseline untouched.

CURRENT — 2026-10-21 15:47 EDT: P1 navigation v2 source2d1e2800d2e3d42908914bdd63bba91707ac684d PUSHED; Build38/run39664622876 observed IN_PROGRESS. Local87 route/17 surface/82 command/283+283 speed/58+58+7 campaign/27 identity checks PASS; Apple/IPA/phone PENDING. Build37 pathing FAILED at100% speed per user. Phone read finished, may disconnect. P2 unchanged. No idle polling.

## Navigation v2 work in progress — 2026-10-21 15:42 EDT

Build37 phone pathing FAILED in both supplied 11:23/11:26 recordings. User repeated at Olimar100% and Pikmin100% and confirmed the same failure; later 200%/500% saved configuration was experimentation after playing, not proof of clip speed. User does not want500% optimization prioritized. Recall All itself works across map.

Current uncommitted P1 changes: progress toward destination rather than any displacement; durable follower return intent across failed routes; reachable route endpoints with layered floor/wall queries; preservation of protected crossing steering; bounded retries and per-run p1-navigation-report.txt. Local synthetic checks are in progress; no new Apple build or runtime result. No teleport, phone writes or P2 source change. Phone read completed with consistent8-file backup at work/p1-phone-feedback-2026-10-21 153224. User may disconnect. Latest remote/source baseline ee380c593633f8b6bc609c9e293377e79e2d9556.

CURRENT - 2026-10-21 11:00 EDT: Build37 P1 SUCCESS; combined app verified. User-approved generated names/icons packaged into original-ID P1Build37 and P2Build32 with executable/all non-Info original entries unchanged. Both named/icon IPAs staged in folder1, phone test pending.27 CMake metadata/icon checks PASS. No new CI build.

CURRENT - 2026-10-21 10:34 EDT: Build36 CANCELLED at user request. Combined crossing/route+Recall All/Pikmin Speed source localPASS63/82/283; Build37/run39617967156, sourceabd06b6216f0d09bc13361ddbff693f58640a21f, observedqueued. New Apple/IPA/phone pending. Build35 rollback intact, P2 paused. No teleport or phone writes.

CURRENT - 2026-10-21 10:33 EDT: Build36 CANCELLED at user request. Combined crossing/route+Recall All/Pikmin Speed source localPASS63/82/283; combined P1-only standard build pending commit/push. New Apple/IPA/phone pending. Build35 rollback intact, P2 paused. No teleport or phone writes.

CURRENT - 2026-10-21 10:11 EDT: Build35 phone Aim/SoftAssist/charge whistle/save-reload PASS; clam untested, raised crossing stranded followers persist. Separate recall button +Pikmin Speed localPASS82/283, Build36/run39614665805, source472937e505eef2a14d00b0c923620dbaee4bd9cd, observed in_progress. New Apple/IPA/phone pending; no stuck-rescue/teleport implementation; P2 paused.

CURRENT - 2026-10-21 10:10 EDT: Build35 phone Aim/SoftAssist/charge whistle/save-reload PASS; clam untested, raised crossing stranded followers persist. Separate recall button +Pikmin Speed localPASS82/283, P1-only standard build pending commit/push/dispatch. New Apple/IPA/phone pending; no stuck-rescue/teleport implementation; P2 paused.

CURRENT - 2026-10-21 01:43 EDT: P1 Build35/run39548476790 SUCCESS, source01d7e7ed18df04cb0856ae5cab77b6df62101e39. STANDARD original-ID ARM64 device IPA verified/staged in folder1; SHA256 eab4b43ccaeda4de25137e010342592a4e0fc6d2cd328be9b66d365d10e3cc89. Phone installation/runtime pending; P2 unchanged. No new build needed; await normal-save test feedback.

CURRENT - 2026-10-21 01:15 EDT: Build34 FAILED (missing KeyConfig.h), corrected/local checks PASS, source01d7e7ed18df04cb0856ae5cab77b6df62101e39. P1-only STANDARD Build35/run39548476790 in_progress at dispatch. No new IPA/phone result; P2 unchanged. No idle polling.

## Build 34 compiler correction — 2026-10-21 01:14 EDT

- Build 34 / run 39545404613 / source ff57b9ffc71b9fcd87c444630b2454bcbe4e4110 FAILED. Full job 119042338355 log inspected: one compiler error, navi.cpp:1539 undeclared KeyConfig. No new IPA was produced. Installed P1/P2 remain unchanged.
- Cause: new whistle-priority code used the correct existing binding API but navi.cpp lacked its direct KeyConfig.h include. The extracted host fixture supplied that type and missed this integration dependency.
- Correction: add the direct include; generator now rejects source using KeyConfig without that header. Negative control on Build 34 source fails with the expected dependency message.
- Local verification: 60 command/aim/recall/edge scenarios PASS; preset update/separate/standard 58/58/7 PASS; Clang checks PASS; git diff --check PASS. Apple compilation and phone runtime still pending.
- Next build is P1-only STANDARD normal campaign, original app identity, all previous fixes retained; no P2 change, no synthetic campaign, no autosave/network feature enabled. Verified restore backups remain intact. After dispatch, record run/source and stop waiting; user will report completion.

CURRENT - 2026-10-21 00:42 EDT: P1-only normal-campaign Build34/run39545404613 DISPATCHED, sourceff57b9ffc71b9fcd87c444630b2454bcbe4e4110, observedin_progress. Includes baa8af2b upstream RNG correction and locally checked command/aim/recall/edge batch. Apple/IPA/phone results pending. No new autosave/networking feature enabled. Phone may disconnect. No idle polling.

CURRENT - 2026-10-21 00:40 EDT: Build33 phone test/save evidence collected. P1 charge/whistle/cursor, Aim/Soft Assist, recall and bounded ledge fixes implemented/local PASS60+58+58+7+27 checks; P2 shared menus188/198 PASS. Standard P1-only Apple build pending dispatch. Normal saving retained; shared exact-scene snapshot/co-op plan recorded. Upstream1.0.6 audited, isolated RNG fix adopted. Phone released; no phone writes.

CURRENT - 2026-10-20 21:15 EDT: P1-only Build33/run39523034602/source8e813868 SUCCESS. Original-ID solo-update IPA verified/staged; SHA256 c04abe4dad2a9ecfada89ddfa53e24aa40c6a272696df1d6dd45bdc32fd7916b.
Backup intact; exact install/checklist in folder1. Phone install/settings/save/runtime unverified. P2 Build32 positive user feedback. No new build needed; await test results.

CURRENT - 2026-10-20 20:49 EDT: User reports "P2 is working now" after Build32. This is a positive phone runtime/audio retest in the context of the missing Pikmin/enemy sounds. Individual effects, other colors, distance attenuation, caves/area transitions and the full campaign were not separately confirmed. No new phone audio report was retrieved; do not describe every sound as independently verified.
P1-only Build33/run39523034602 remains pending at last observation; no CI polling performed.
P1 rollback backup remains verified; phone may disconnect. Documentation-only update, no build.

CURRENT - 2026-10-20 20:44 EDT: P1-only Build33 dispatched, run39523034602,
source8e8138684fd5e36595a89058d090240217fe66ae, observedin_progress.
Verified rollback backup ready; current-app test update uses preserved settings/
assets and separate test saves, no finale preset. New Apple/IPA/phone tests pending.
User can disconnect. No idle polling; next inspect once user reports completion.

CURRENT - 2026-10-20 20:43 EDT: P1 current-app test update authorized; verified rollback
IPA/settings/layout/save backup completed first. New solo-update source locally
PASS, Apple build pending. Reuses assets/settings, separate test cards, no finale.
P2 unchanged; Build32 audio phone result pending. No phone writes or new install.

CURRENT - 2026-10-20 20:26 EDT: Build32 BOTH PASSED, run39518825366, source1f04dd8f.
P1 Solo Test and P2 IPAs verified/staged in folder1; neither new app phone test confirmed.
Original P1 untouched; finale deferred. Next: P2 audio retest, separate P1 install
and private content preparation over USB, then spoiler-free A/C checks.
No new build needed; see current master handoff and folder1 instructions.

CURRENT - 2026-10-20 20:05 EDT: User requests spoiler-free P1 testing. Final boss/ending
coverage deferred; not a prerequisite for separate co-op prototype. Use A/C and
familiar earlier areas, avoid B/final area. Invincibility optional; skipped death/
hazard behavior remains unverified. Build32 source unchanged; no extra build.

CURRENT - 2026-10-20 20:03 EDT: Combined Build32 DISPATCHED, run39518825366, observedqueued.
Source 1f04dd8f0117b91c0e5cc6e80cd61384943603e9; includes90785c36 P2 mute cleanup.
P1 is the separate solo-test app; P2 retains standard identity. Local checks PASS;
new Apple results/IPAs/phone tests pending. Original P1 untouched. Phone released.
No idle polling: user reports completion. Exact source/run in current handoff.

CURRENT - 2026-10-20 20:01 EDT: P1 solo-test source/presets and P2 opening mute cleanup locally verified.
Original P1 app untouched. New test IPA/phone scenarios pending. P2 Build31 snow
ambience restored; Pikmin/enemy audio still silent. Report retrieved; nearby gains
zero only in those categories. Opening exit cleanup candidate implemented/tested.
Combined P1 test/P2 standard build pending dispatch. See latest master handoff.

CURRENT - 2026-10-20 19:43 EDT: Build31 P2-only PASSED, run39514971137, sourcedc73a848.
Verified IPA staged in folder1. New audio/proximity/report phone test pending.
P1 working app untouched. Separate solo-readiness test approach accepted;
eventual proven co-op is intended for original app. No test IPA/co-op code yet.
See PIKMIN1_SOLO_READINESS_PLAN.md and current master handoff.

CURRENT - 2026-10-20 19:26 EDT: P2-only Build31 DISPATCHED, run39514971137.
Source dc73a84887e60d4e3b7911b1e46ed64ab4a764b9; observed in_progress.
Native JAI parameter stride/report platform defects corrected; local48 parameter,
11 activation and28 routing checks PASS. Apple result/IPA/phone audio pending.
Build30 HUD clearer; audio failed on phone. P1 unchanged. No idle polling.
Phone/game not needed until next successful install/test. See current handoff.

CURRENT - 2026-10-20 19:25 EDT: Build30 phone result: HUD clearer, audio NOT resolved.
Pikmin/enemy/wind missing; ship and inactive captain breathing can ignore distance.
Confirmed native audio parameter union stride defect and report activation defect;
local48 producer/consumer and11 platform report checks PASS. New Apple build pending.
P1 unchanged. Phone had no audio reports; see current handoff/audio audit notes.

CURRENT - 2026-10-20 19:10 EDT: P2 Build30 PASSED, run39509564730, sourcee9a06beb.
New unsigned IPA verified and staged in folder1; phone install/audio/HUD test pending.
P1 untouched. All142 P2 audio assets matched phone originals. User accepted saving
separate P1 online prototype plan; no online implementation started.
See PIKMIN2_AUDIO_AUDIT.md, ONLINE_COOP_DESIGN_NOTES.md and current master handoff.

CURRENT - 2026-10-20 18:39 EDT: P2-only Build30 DISPATCHED, run39509564730.
Source e9a06bebd443e3eb5d8943a5c01c53e186512423; observed in_progress.
All142 phone audio files match originals. Local mixer/HUD/audit checks PASS.
Apple result/new IPA/phone audio and HUD validation pending. P1 unchanged.
No idle polling. See current master handoff and PIKMIN2_AUDIO_AUDIT.md.

CURRENT - 2026-10-20 18:37 EDT: P2 audio/HUD batch locally verified; Apple build not dispatched yet.
Build29 phone gameplay/settings confirmed, but voices/wind/ship-distance issues remain.
All142 phone AudioRes files SHA-256 match originals. HUD toggle resolved by user.
New mixer/HUD corrections and bounded diagnostics require Apple/phone validation.
See PIKMIN2_AUDIO_AUDIT.md and the current progress report below. P1 untouched.

CURRENT - 2026-10-20 14:31 EDT: Build29 P2-only PASSED; verified enhancements IPA ready in folder1.
Source7f7d0783/run39470849443. New phone installation/runtime test pending.
P1 textures confirmed354 replacements/0 failures; P1 unchanged. Future co-op
choices recorded (notes only, implementation still last). Older pending headers historical.

CURRENT - 2026-10-20 14:07 EDT: P1 GPI HD textures CONFIRMED loading on phone:
354 successful replacements,0 failed;455 originals not in pack. No P1 changes needed.
P2 Build29 result still pending at last observation; no idle polling.
Older texture-unconfirmed notes below are superseded by this screenshot.

CURRENT - 2026-10-20 14:00 EDT: Build29 P2-only DISPATCHED, run39470849443.
Source7f7d0783e8b42870a8b6bbb1954199fbe9ffc6bb; observedin_progress.
Build28 FAILED at import API call; corrected, new19-check real API fixture PASS.
Build29 result/link/IPA/phone tests pending; Build27 working baseline. P1 untouched.
No idle polling. Next inspect Build29 when user reports done. Older entries historical.

CURRENT - 2026-10-20 13:59 EDT: Build28 FAILED (2 compiler errors,1 incorrect API call).
Correction and19-check real menu/API regression locally PASS; retry not dispatched yet.
Build27 remains limited positive phone baseline. P1 untouched; texture replacements
not confirmed. New entries supersede older pending-build headers below.

CURRENT - 2026-10-20 13:42 EDT: Build28 P2-only DISPATCHED, run39468391460.
Source386771cabe6366b0788091f4d6d63f9ef6850c67; observed in_progress.
Local checks PASS; new Apple result/IPA/phone tests pending. Build27 user reports
no crashes so far (limited test). P1 app unchanged; GPI activation unverified.
No idle polling; next action inspect Build28 when user reports completion.

CURRENT - 2026-10-20 13:41 EDT: P2 enhancements implemented; local checks PASS.
Apple build/IPA/new-profile phone tests pending. Build27 user reports no crashes
so far (limited test). P1 GPI texture pack installed/listed but inactive in screenshot;
activation unverified. P1 working app untouched; keep60FPS. New entries supersede
older current-status headers; older entries below are historical.

CURRENT - 2026-10-20 09:57 EDT: Build27 P2-only PASSED; verified IPA in folder1.
P2 phone crash/control retest pending. P1 models INSTALLED, runtime pending;
saves/settings unchanged. HD environment textures NOT installed.

CURRENT CONTENT UPDATE - 2026-10-20 09:52 EDT: P1 character bundle INSTALLED;
20 files hash-verified, saves/settings unchanged. P1 model runtime test pending.
HD environment textures NOT installed. P2 Build27 pending at last dispatch.

CURRENT - 2026-10-20 09:38 EDT: Build26 PHONE REGRESSIONS: menu gear/A hidden;
captain-preview/Metal heap crashes. P2-only batch locally checked; Build27/run39432157516 (in_progress at dispatch).
New Apple build and phone results pending. Build24 backup; P1 untouched.

CURRENT - 2026-10-20 09:37 EDT: Build26 PHONE REGRESSIONS: menu gear/A hidden;
captain-preview/Metal heap crashes. P2-only batch locally checked; not dispatched.
New Apple build and phone results pending. Build24 backup; P1 untouched.

CURRENT - 2026-10-20 09:19 EDT: Build26 P2-only PASSED; verified IPA ready in folder1.
Menu clarity/input on phone pending. Build24 opens; P1 untouched.

CURRENT CHECKPOINT - 2026-10-20 08:43 EDT: Build25 failed only the new test fixture;
correction locally verified. P2-only Build26 run39424440094 dispatched; result pending.
Build24 opens on phone; menu candidate remains unverified. P1 untouched.

CURRENT CHECKPOINT - 2026-10-20 08:42 EDT: Build25 failed only the new test fixture;
correction locally verified. P2-only replacement build not dispatched yet.
Build24 opens on phone; menu candidate remains unverified. P1 untouched.

LATEST BUILD: P2-only Build25 at 3013d4c2;
result/IPA/menu phone test pending. Build24 opens; P1 untouched.

CURRENT - 2026-10-20 08:33 EDT: user resumed. Build24 P2 startup/menu opening CONFIRMED.
P2 clarity/options-touch candidate implemented; local tests PASS, next Apple
build and phone checks pending. P1 untouched. Prior paused notes are historical.

# PAUSED AT USER REQUEST - 2026-10-20 01:13 EDT

The user is shutting the PC down and explicitly asked to pause until morning.
Do not resume source edits/builds/phone operations until asked to continue.
No source edits, commits, pushes, new builds or phone operations occurred in
this menu-investigation turn. Only repository/source/history reads were done.
Repository branch ios-experimental; local/fetched remote HEAD both
00bd0db831ce09d37c3da94e00ec5596e2256563, working tree clean at investigation
start. Build24 source05e33f1c0e55dc11ecb6d413a8393bf73faeb2ce/run39371370836
PASSED, and the user now CONFIRMS P2 OPENS on the phone and reaches menus.
This supersedes earlier 'new phone startup unverified' notes. Do not infer
verified audio/gameplay/full-game stability from this menu/startup observation.
Preserve Build24 allocator/thread ownership and SDL UIKit framebuffer fixes.
P1 app, data, source and its working menu/camera behavior remain untouched.

Two newly reported P2 issues (screenshots attached in chat):
1. Advanced Open Nectar menu is small/blurry, resembling P1's earlier problem.
2. Original game Options/exit-confirmation screen accepts only bottom-left X/
   Back. User clarified main-screen taps and Throw/A work; failure is specific
   to that menu/dialog. Do NOT diagnose all touchscreen input as broken.

Read-only findings before pause:
- Working P1 pc_window.cpp has SDL_WINDOW_ALLOW_HIGHDPI on iPhone; P2 lacks it.
- P1 pc_gfx.cpp latches ios_native_settings_frame and renders menus at native
  drawable resolution independently of gameplay render scale/resolution. P2
  lacks this path; its screenshot shows a low internal scene scale/resolution.
- P1 pc_settings.cpp enables the 400-high mobile canvas for iOS and Android,
  with iPhone landscape margins, matching viewport/scissor and inverse tap map.
  P2 still restricts those branches to Android. P2's shim begin_frame also sets
  virtual dimensions only on Android, so include it when adapting the solution.
- P2 TOption::doUpdateStateWait has controller input but no touch-pane handling.
  Its rows are mButtonPaneList[7]; save is row6/A; other settings use left/right.
- The pictured confirmation uses ObjWorldMapInfoWindow0 -> ObjSMenuPauseVS.
  ObjSMenuPauseVS::menu ALREADY claims game-menu touch, calls
  MenuMgr::pcTouchTappedOption and treats tapping selected option as A.
  Investigate why that existing path fails before adding duplicate handlers.
- pc_touch.cpp only allows Back plus buttons requested by visible help icons
  while a game menu owns input. Its separate MENU_CONFIRM is currently allowed
  only for port menus. Check whether this original dialog exposes a usable A
  control and whether pane tracking/projection hits its visible text correctly.
  The main-screen working controls should remain unchanged.

Exact resumption steps:
1. User says resume; read this checkpoint and newest journal; verify branch/
   status/fetch again and preserve any changes made after this pause.
2. Compare actual working P1 menu/high-DPI/render-budget code with P2. Adapt
   P2 paths, including its DGX shim, mobile layout and inverse taps; preserve
   gameplay pixel budget, startup fixes and P1 source/data.
3. Inspect TOption and inherited confirmation input/tracked panes. Implement a
   targeted original-options fix preserving main-screen/gameplay controls and
   keeping save/discard actions explicit. Do not auto-save or auto-discard.
4. Add meaningful layout/Retina/touch-state checks; build P2 only after local
   checks and review. No fixes are implemented yet and no Build25 was triggered.
5. Record exact commit/run; do not idle-poll Actions. When result known, verify
   IPA, put in folder1 with short test guide. Phone tests: readable full-width
   advanced menu, taps/scroll alignment, original options rows, confirmation
   Continue/Don't Save, Back, plus startup/gameplay/audio/control regression.
6. Keep P1 untouched. Optional packs and online with Raye remain later; online
   LAST. User is asleep; no immediate test request/audio alert is needed.

Important source locations:
games/pikmin1/pc_port/pc_window.cpp andgl/pc_gfx.cpp (working reference)
games/pikmin1/pc_port/settings/pc_settings.cpp (working mobile layout)
games/pikmin2/pc_port/pc_window.cpp andgl/pc_gfx.cpp
games/pikmin2/pc_port/settings/pc_settings.cpp andpc_settings_p2_shim.cpp
games/pikmin2/pc_port/touch/pc_touch.cpp andpc_touch.h
games/pikmin2/pikmin2-decomp/src/plugProjectEbisawaU/ebiScreenOption.cpp
games/pikmin2/pikmin2-decomp/include/ebi/Screen/TOption.h
games/pikmin2/pikmin2-decomp/src/plugProjectOgawaU/ogObjSMenuPauseVs.cpp
games/pikmin2/pikmin2-decomp/src/plugProjectOgawaU/ogObjWorldMapInfoWindow0.cpp
games/pikmin2/pikmin2-decomp/src/plugProjectOgawaU/ogMenuMgr.cpp
games/pikmin2/pikmin2-decomp/src/JSystem/J2D/J2DPane.cpp
Session work/prepare_pikmin1_menu_candidate.ps1 records the earlier P1 patch;
read it as historical evidence, do not blindly execute it against current code.

END PAUSE CHECKPOINT

LATEST CHECKPOINT - 2026-10-20 01:03 EDT: P2 Build24 SUCCESS; target ARM64 allocator
check and actual binary16-byte alignment verified. New IPA ready in folder1.
NEW phone installation/startup/audio retest pending. P1 working and untouched.
Earlier Build23 phone startup failed; read newest journal entry for current state.

CURRENT BUILD: P2-only Build24 dispatched at 05e33f1c;
result and phone retest pending. P1 untouched.

LATEST CHECKPOINT - 2026-10-20 00:46 EDT: P2 Build23 phone startup FAILED on AudioQueue
thread. Matched real crash UUID; binary new alignment is8bytes. 16-byte floor +
native/game thread allocation ownership batch implemented; local tests passed.
Next P2-only Apple build pending. P1 working/untouched. Older pending/success
checkpoints describe compilation or historical results, not a working P2 app.

LATEST CHECKPOINT - 2026-10-20 00:34 EDT: P2 Build23 SUCCESS; startup candidate IPA ready
in folder1. Source609a45b1/run39369282124. New phone installation/startup retest
PENDING. Update P2 only; preserve data/assets/art. P1 working and untouched.
Read the newest journal entry; earlier build-pending checkpoints are historical.

LATEST BUILD CHECKPOINT: P2-only Build23 dispatched at 609a45b1;
Apple result/IPA/phone retest pending. P1 untouched.

CURRENT CHECKPOINT - October 20, 2026: P2 Build22 installs but crashes at first
draw. Real phone crash reports identify an alignment fault; allocator + renderer
scope candidate implemented and local tests passed. Next P2-only Apple build and
phone retest pending. P1 working and untouched. Read newest journal entry below;
historical pending/paused instructions are superseded by this checkpoint.

# Open Nectar native iOS status

Updated: 2026-10-19, America/New_York. Branch: `ios-experimental`.

## Preservation baseline

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Starting local and fetched remote commit: `ed22a5ea9c362fba953b525d5358384426f23bf2`.
- Initial working tree already contained the three-edit `EnemyMgrBase.h` v1.4 iterator correction. Preserve and attribute it as pre-existing work.
- Pikmin 1 framebuffer correction is present in `games/pikmin1/pc_port/pc_window.cpp` (`pc_window_ios_drawable`, swap binding) and `gl/pc_gfx.cpp` (`pc_gfx_display_framebuffer`). Do not revert it.
- User reports Pikmin 1 title/menu/gameplay/Olimar movement/audio/touch working on iPhone 15 Pro Max, reportedly iOS 27.2. This session has no new hardware evidence.
- No game images, extracted assets, credentials, or signing material belong in Git.

## Verified build baseline

Build #9: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39167424765

- Commit: `ed22a5ea9c362fba953b525d5358384426f23bf2`.
- Pikmin 1 job `117793183742`: success, artifact `12150844781` (`nectar-pikmin1-experimental`).
- Pikmin 2 job `117793184024`: failure, artifact `12150864586` (`nectar-pikmin2-experimental`, compiler log only).
- Full workflow logs and Pikmin 2 compiler artifact retrieved directly from GitHub on October 19.
- Compiler artifact contains exactly one fatal compiler error: `EnemyMgrBase.h:95`, pointer-to-smaller-`int` conversion in `get(void*)`, compiling `plugProjectKandoU/vsTekiMgr.cpp`. No linker stage reached. Prior `vtxAnm.cpp` errors absent.

## Pikmin 1 investigation

- Downloaded Settings Menu Fix v1.4 ZIP exists but was not applied to the baseline.
- F1 settings mobile layout/render mapping/viewport are Android-only. iOS uses a fixed 640x480 desktop canvas.
- Title Options uses a separate fixed-canvas `settings/pc_glass_menu.cpp`; changing F1 gates alone does not address it.
- Settings GX/P2D text renders into the scene framebuffer before `pc_gfx_present`, then is linearly upscaled. Default scene render scale is 2/3.
- SDL UIKit defaults to scale 1 without `SDL_WINDOW_ALLOW_HIGHDPI`; touch icons draw after presentation through the independent overlay.
- Implemented candidate: retina drawable; retain logical-pixel scene workload during normal gameplay; full drawable resolution while F1 or title Advanced settings are open; 400-high mobile canvas and matching inverse touch mapping. Menu frame mode is latched for consistent presentation aspect; saved resolution/aspect settings remain unchanged. Conservative landscape margins are 56 horizontal and 24 bottom virtual units; dynamic UIKit safe-area support remains future work.
- Local verification: 115 C++17 x64 cases compiled/executed from actual changed geometry/sizing functions: four drawable shapes, inverse touch mapping, all five aspect modes, three render scales, both menus, explicit resolution override, close restoration, and mid-frame latch. MSVC emits only isolated harness shadow warnings. This does not compile the full iOS renderer.
- Changed source: pc_window.cpp high-DPI flag; gl/pc_gfx.cpp menu-frame resolution choice; settings/pc_settings.cpp mobile F1 gates/margins; settings/pc_glass_menu.cpp mobile Advanced layout, viewport/scissor, inverse tap/drag mapping. Existing SDL drawable framebuffer correction is retained.
- Hardware clarity/performance/touch validation remains required. Opening menus temporarily allocates a larger scene target and can cost memory/time. Original basic game Options/BLO typography is not redesigned by this patch.
- Existing right-thumb camera gesture is implemented in `touch/pc_touch.cpp`: separate movement and gesture fingers, button exclusion, one-finger rotation and two-finger zoom. Do not add a duplicate camera system before testing settings/behavior.

## Pikmin 2 verification

- Existing `EnemyMgrBase.h` change includes `<cstdint>`, encodes `getEnd()` through `std::intptr_t`, and decodes `get(void*)` through `std::intptr_t` before converting the bounded slot index to `int`.
- Local x64 MSVC C++14 `/W4 /WX` check compiles the actual changed inline methods extracted from the header. Execution passes empty/end handling and valid-slot pointer/index round trips. This is not an AppleClang/iOS build.
- Corrected the same pointer-as-index conversion in `src/plugProjectYamashitaU/enemyMgrBase.cpp::getNext`, including returned slot/end tokens. CMake includes this source through GAME_YAMASHITA_SOURCES. This is a verified source hazard adjacent to the logged header error, not a separately observed Build 9 compiler error.
- Extended x64 C++14 semantic check passes actual extracted getNext code with the -1 start sentinel, empty list, skipped inactive slots, live slots 2/6, and end-of-iteration handling.

## Workflow and authority

- Existing `.github/workflows/ios-native-experimental.yml` builds both matrix games on macOS/Xcode.
- Only commit messages containing `[ios-build]` execute build jobs; documentation commits should omit it.
- User authorizes normal scoped commits/pushes to `ios-experimental`, existing workflow builds, logs, and artifacts. No force pushes, history rewriting, main merges, repository security changes, or stable releases.
- Git authentication verified with a successful dry-run push October 19. Do not store credentials in documentation or scripts.
- User is applying to jobs; only request necessary input. Play an audio alert when user action is needed.

## Exact next actions

1. Read the next build result when the user reports completion; retrieve full failed logs directly and iterate from evidence.
2. User can install the Build 10 Pikmin 1 IPA and test F1/title Advanced clarity, edge taps, scrolling, notch clearance, and restoration of gameplay/audio/touch.
3. After Pikmin 2 compiles/packages, validate its own presentation/input/audio on the phone.
4. Keep build, IPA, installation, and runtime milestones distinct. User requested no idle polling while waiting for GitHub.

## October 19 implementation milestone

- Pikmin 2 correction committed as 5543394e43f8c9b3bc51b75e995aa9b8b3752df1 (includes preserved pre-existing header work).
- Pikmin 1 candidate and journal prepared for the same push; final commit will contain [ios-build]. No new IPA or runtime result yet.
- Working source was checked with git diff --check; no proprietary assets or unrelated files staged.

## Build #10 dispatched

- Run: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39263564026
- Exact build commit: `483815d4b0d4f8b074be5381738f59af3a54b796`.
- Includes Pikmin 2 commit `5543394e43f8c9b3bc51b75e995aa9b8b3752df1` and Pikmin 1/journal commit `483815d4`.
- Push succeeded; initial live status queued on October 19 at approximately 09:50 Eastern.
- Results, IPA contents, installation, and runtime remain pending. Do not label menu appearance fixed yet.

## Pikmin 2 presentation investigation and candidate

- Its own `pc_port/gl/pc_gfx.cpp` still targeted FBO 0 in final present and touch overlay. Its own `pc_port/pc_window.cpp` swapped on iOS without binding UIKit's drawable framebuffer/color renderbuffer.
- Applied a P2-only candidate following inspection of its implementation: `pc_window_ios_drawable` uses SDL SysWM UIKit information; swap binds that FBO/RBO and restores separate prior read/draw/RBO bindings; final presentation and overlay use the SDL display FBO.
- Existing P1 source is unchanged by this follow-up. No P2 Retina, resolution, audio, or settings behavior is changed.
- Local MSVC C++17 host validation passes five states using actual candidate helpers/swap code: valid target, replaced drawable, unavailable WMInfo, wrong subsystem, and null window. Prior distinct bindings restore exactly. This is simulated host validation, not OpenGL execution on iPhone.
- These P2 display changes are not included in Build #10; they await a later commit/build. No runtime black screen has been observed for P2 in this session.
- Audio clarification: P2 uses its own JSystem JAS/JAI software DSP and SDL sink. The top-level PIKMIN_NATIVE_JAUDIO=OFF does not establish missing P2 audio. Hardware audio remains unverified.
- Camera clarification: P1 touch drag is consumed without requiring Free Camera; Free Camera Speed changes the controller stick, not touch sensitivity.

## Build #10 result and next corrections (October 19, ~10:06 Eastern)

- Build #10 is completed: Pikmin 1 job 118097217644 succeeded; Pikmin 2 job 118097217295 failed. Exact source commit remains 483815d4b0d4f8b074be5381738f59af3a54b796.
- P1 artifact 12193380985 contains Nectar-pikmin1-unsigned.ipa (2,550,357 bytes). ZIP integrity passes; Payload/Nectar-pikmin1.app has ARM64 Mach-O executable Nectar-pikmin1 (6,295,688 bytes), bundle org.opennectar.experimental.pikmin1, minimum iOS15.0. SHA256 8138f1f378a04b9597aaee8fa725611a9ddd7d57f9e0f8263fc2e872b17999cc. Not installed/tested in this session.
- P2 artifact 12192161804 contains the failed build log. Full workflow archive is retained as work/build10-logs.zip in the local task workspace.
- Ten compiler errors, one root: VsOtakaraName undeclared in vsGameSection.cpp at lines383 (three),807(two),1084,1120,1313,1347(two). No linker error/stage reached. Previous EnemyMgrBase pointer error is absent.
- Compiler warning trace shows pikmin2-decomp-adapter/VSOtakaraName.h including itself through case-only spelling VsOtakaraName.h on case-insensitive macOS. The include guard then hides the real struct.
- Corrected VSOtakaraName.h to explicitly include ../pikmin2-decomp/include/VsOtakaraName.h. Corrected the identical verified pattern in PikiAi.h to explicitly include ../pikmin2-decomp/include/PikiAI.h. No other basename self-includes were found in the adapter headers.
- Local MSVC C++14 test reproduces the old case-only alias failure on Windows, then the actual corrected VsOtakaraName header compiles under /W4 /WX. PikiAI preprocessing reaches the real _PIKIAI_H guard; it emits existing host/decomp varargs redefinition warnings, not a full source compile result.
- P2 display follow-up is committed as 762eba1b16d24976bf3cfb84f430052756c51e1a. It and the two alias corrections will be pushed together for the next build. P1 source remains exactly the Build10 version.
- User requested conserving usage: after dispatching the next build, stop polling and wait for the user to report completion.
## Build #11 dispatch and stop-wait checkpoint

- Run https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39265932808; initial status queued at October19 10:06 Eastern.
- Exact local/remote source commit 204c06ade5e82bebd528a56e46bfa76b66115fb9, including P2 display commit762eba1b16d24976bf3cfb84f430052756c51e1a. Push succeeded.
- No P1 source change since successful Build10. Build11 compiler/IPA/runtime results are pending.
- This dispatch checkpoint is the only post-push uncommitted journal update. No source edits remain uncommitted.
- STOP idle polling per user request. Resume when user reports the build result; fetch the actual run/job logs and continue from evidence.

## User-facing project folder (October 19, 2026)

The user requests all future test materials in C:\Users\chazz\Documents\Open Nectar.
Put each test IPA in `1 - Install on iPhone`, with a clear game/build filename
and short WHAT TO TEST.txt. Refresh plain-text progress/master-handoff copies
in `2 - Progress and ChatGPT Handoff` after milestones. Use these accessible
paths when asking the user to install/test; do not make them browse generated
Codex directories. Play an audio alert when user action is required.

Nine reviewed Downloads items were moved individually and SHA256-verified.
RVZ images are in `3 - Game Files - Keep Private\Original RVZ Files`.
Verified ISOs, source code, active/earlier sessions, and display backup are
accessible through junctions; originals stay at their existing working paths.
Windows Documents points to OneDrive; its Open Nectar.lnk points to the local
project folder, keeping game data outside OneDrive and the Git repository.

Automatic approval review rejected the initial bulk relocation of the live
repo/active chat workspace. The safer staged plan moved only reviewed Downloads,
kept active directories in place, and added access links. The old bulk script
is disabled; do not rerun it. No build was triggered for organization.

## Build #11 result and nested adapter fix (October 19, ~10:27 Eastern)

- Exact build commit204c06ade5e82bebd528a56e46bfa76b66115fb9. Run39265932808 completed: P1 job118105370021 success; P2 job118105369589 failure.
- Artifacts: P1 12193133375 (unsigned build bundle), P2 12193278343 (failed build log). The user is testing the existing Build10 P1 IPA; no hardware result has been reported. Do not replace that test with a redundant P1 download.
- Complete workflow logs retrieved as work/build11-logs.zip and extracted in work/build11-full. Exactly one fatal compiler error: vsGS_Title.cpp298, Morimura::DispMemberChallengeSelect incomplete. No linker stage reached. Previous VsOtakaraName errors absent.
- The warning trace identifies the same self-include hazard in pikmin2-decomp-adapter/Morimura/challengeSelect2D.h. Its include with a directory component resolves back to itself on a case-insensitive host, hiding the real challengeSelect2d.h definition.
- Previous audit only tested basename includes and missed this nested path. Corrected the adapter to include ../../pikmin2-decomp/include/Morimura/challengeSelect2d.h explicitly.
- Added tests/pikmin2_adapter_includes.py. It models case-insensitive lookup using a case-folded adapter/decomp header inventory, including directory components and normal local-header-first lookup. It detected the original recursive include; after the correction all43 adapter headers pass.
- Existing experimental workflow runs the new fast check only for the pikmin2 matrix job before CMake configuration. P1 source is unchanged. Workflow step reviewed; no local YAML parser package was available, so no YAML-parser pass is claimed.
- Actual corrected header was preprocessed by local MSVC C++14, confirming the real _MORIMURA_CHALLENGESELECT_H guard and complete DispMemberChallengeSelect declaration. Full AppleClang compilation and P2 presentation/runtime remain pending.
- Next: push this fix/test/workflow update together with the accumulated organization documentation. Record the new build ID, refresh the user-facing reports, then stop idle polling. Resume from compiler evidence when the user reports completion. P1 hardware feedback remains pending.

## Build #12 dispatch checkpoint

- Run https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39269078016
- Exact local/remote commit37020a74c26748a1f78c7dbb7936c3e812934d29; initial status queued at October19 ~10:27 Eastern.
- Includes the nested Morimura adapter fix, 43-header case-insensitive self-include check, P2-only workflow precheck, and saved folder-organization documentation. No P1 source changes.
- All source and prior folder-policy documentation are pushed. Only this post-push status-journal checkpoint is uncommitted.
- User is testing P1 Build10; no appearance/control/audio feedback received yet. STOP idle polling; await user report on Build12.

## PAUSED — October 19, 2026, 10:44 AM Eastern (user request)

The user requested immediate pause because usage is nearly exhausted. Do not
resume development, commit, push or dispatch a build until asked to resume.
P1 menu readability and camera controls are now phone-confirmed by the user;
full-game completion and optional enhancement behavior are not verified.

Local HEAD and fetched origin/ios-experimental both37020a74c26748a1f78c7dbb7936c3e812934d29.
New P1 enhancement work is UNCOMMITTED: one-time QOL/visual profile with config
backup, persisted marker, native Files ZIP picker, worker bridge, staged importer,
converter output-root/ZIP checks, CMake integration, four focused tests and CI step.
No enhanced IPA, push, or build exists. Profile169checks andbridge19checks passed;
candidate transaction/actual-converter ZIP suites passed. Final repo rerun and
Apple/iPhone verification remain pending. Retain all tracked and untracked files.

P2 Build11 failed in the nested Morimura adapter; the pushed correction is in
Build12 run39269078016. Last API response queued; current completion is unknown.
Do not idle-poll builds. User will report completion. Retrieve full logs on resume.

Full independent handoff and exact next actions saved in the current session's
outputs/OPEN_NECTAR_CODEX_TO_CHATGPT_MASTER_HANDOFF.md and outputs/RESUME_HERE.txt,
and C:\Users\chazz\Documents\Open Nectar\2 - Progress and ChatGPT Handoff\
Copy This into ChatGPT.txt and 00 - RESUME HERE.txt.

Resume: preserve dirty edits, inspect/fetch Git, review integration, rerun actual
repo tests, inspect Build12 completed logs, then coordinate one verified push/build.
After build success prepare accessible IPA and phone test instructions. Separate
HD assets still need selecting/importing; none downloaded. Online iPhone co-op
with Raye for BOTH games is the final milestone, not implemented now.

## RESUMED — October19, 2026, ~16:30 Eastern

The user explicitly resumed work and said nothing had changed. The prior pause
is revoked. Starting HEAD/origin37020a74 and all previously dirty files were
verified intact; fetch found no competing remote changes.

P1: user-confirmed readable menu and working camera remain the hardware baseline.
Enhanced source/tests are now committed as
eec45217e4d1c601de2371d0dbd480f8746fc25b. They are NOT yet iOS-compiled or phone-tested.
Profile enables renderScale1, FXAA,4x anisotropy, subtle bloom, and existing QOL
actions once, preserving FPS/camera/other choices and backing up original config.
Native Files ZIP picker + worker completion + staging/backup/rollback installer
make existing texture/model loaders accessible. No external HD assets installed.
See ios/PIKMIN1_IOS_ENHANCEMENTS.md for exact choices, rollback and phone checklist.

All four suites reran against actual repo source in work/resume-verification:
169 profile checks,19 bridge checks, filesystem transaction/rollback suite and
actual-converter ZIP suite passed. First3 used MSVC17 /W4 /WX; converter/stb /W3.
All43 P2 adapter headers passed the existing audit. git diff --check passed.
Reviewed native picker cancellation, scoped copy lifetime, duplicate selection
and dismissing-presenter guards. Apple compilation/runtime remain unverified.
Phone-tested display/camera implementations and P2 source have no new changes.

Build12 run39269078016 is complete with workflow conclusion failure, but BOTH
jobs were cancelled before receiving any runner (runner_id0, empty step lists).
Exact annotation: "The job was not acquired by Runner of type hosted even after
multiple attempts"; notices cite ARM macOS capacity constraints. Empty logs ZIP,
no compiler errors or artifacts. Evidence in work/build12-jobs.json and
work/build12-annotations.json. Do not diagnose another P2 code failure from this run.

Experimental workflow now uses documented standard macos-15-intel host while
retaining explicit iphoneos ARM64 configuration. Package step verifies arm64
with lipo before producing IPA. Four P1 host suites run before full game compile.
Reference: https://docs.github.com/en/actions/reference/runners/github-hosted-runners
This is a capacity workaround, not an availability guarantee. No unrelated
workflow, account/security, signing or proprietary asset changes.

Next: commit workflow/docs with one [ios-build] marker, fetch/reconcile then push
both commits together, record exact run/commit, refresh accessible handoff, and
STOP idle polling as requested. P2's previous nested adapter fix still needs
actual Apple compiler validation. User action now: none; no candidate IPA exists.
On build completion retrieve actual logs/artifacts, prepare clearly named IPAs
in Documents/Open Nectar/1 - Install on iPhone and targeted phone instructions.
Online iPhone co-op with Raye for BOTH games remains the last milestone.

## Build13 dispatch checkpoint — October19, 2026, 16:29 Eastern

- User resumed work; no pause is active. STOP idle polling while this build runs,
  as the user requested. Await their completion report, then retrieve logs/results.
- Exact local and origin/ios-experimental HEAD: eddaf2adcaac1ebf1101ad2c5c4c8cfffc2b4238.
- Source/test commit eec45217e4d1c601de2371d0dbd480f8746fc25b plus workflow/docs
  commit eddaf2ad are both pushed. Git working tree was clean after push.
- Build13 run39319700760: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39319700760
  Initial observed status in_progress; no final compiler/IPA result established.
- P1 enhanced profile and native mod importer are in this build, NOT yet on the
  phone. No external HD texture/model payload installed. Preserve Build10 baseline.
- P2 includes the previously pending nested adapter fix; no new P2 code diagnosis
  because Build12 never received a runner. Build13 uses standard macos-15-intel,
  retains explicit iphoneos ARM64, and verifies executable architecture with lipo.
- All4 actual-repo host suites and43-header adapter audit passed before push.
  UIKit and full Apple compile/new runtime remain pending.
- Only this post-push status checkpoint is now uncommitted. All code/tests/workflow
  and prior documentation are committed/pushed. Avoid an extra build for this note.
- Next: after completion read exact jobs/logs; fix actual failures. For passing P1,
  retrieve/inspect IPA and place clearly named candidate + short test note in
  Documents/Open Nectar/1 - Install on iPhone. Alert user only when action is ready.

## Build13 result and P2 title diagnostic correction — October19, 16:46 Eastern

- Exact source eddaf2adcaac1ebf1101ad2c5c4c8cfffc2b4238;run39319700760 complete.
  P1 job118290256408 SUCCESS;P2 job118290256873 FAILURE. Standard Intel runner
  workaround acquired runners and compiled native ARM64 as intended.
- P1 all4 portable suites passed on macOS, including169profile/19bridge checks.
  Full Apple/Xcode compile,link,ARM64 verification and IPA packaging passed.
  This validates UIKit compilation,not native picker/runtime behavior on a phone.
- P1 artifact12220390882 retrieved,ZIP integrity/plist/ARM64 Mach-O verified.
  IPA2572685bytes,executable6357808bytes,bundleorg.opennectar.experimental.pikmin1,
  minimumOS15. SHA256 f266a387fc9f7d0f6a6db935b18245ddfa153f43de2531cf4cc1a2e8e08179fd.
  Copied/hash-verified as Documents/Open Nectar/1 - Install on iPhone/
  Pikmin 1 - Build 13 - QOL and Visual Enhancements.ipa with WHAT TO TEST.txt
  and Build 13 - IPA Verification.json. Audio alert played. Build10baseline retained.
- User asked to test menu/camera preservation,10-15min clarity/frame pacing/heat,
  QOL/Lock-On/Charge,touch interactions,picker cancel/reopen and setting persistence;
  saves/loading when convenient. Hardware result not yet reported. No HD asset
  payload is included. Signing/install via existing Sideloadly;preserve app data.
- P2 full logs downloaded to work/build13-logs.zip,extracted work/build13-full.
  Exactly TWO unique compiler errors,both titleSection.cpp:389:43/:72,one root:
  getCodeEnd/getCodeStart pointers cast to32bit int in a debug OSReport expression.
  No linker error reached. Prior incomplete Morimura/VsOtakaraName failures absent.
- Fixed games/pikmin2/pikmin2-decomp/src/sysGCU/titleSection.cpp::doUpdateMainTitle
  with std::uintptr_t markers/difference,guarded reversed markers,and matching
  unsigned-long-long/%llu output underPIKI_PC_PORT. Retail branch preserved.
  Native OSReport implementations usevprintf and support the format.
- Actual corrected statements extracted to work/resume-verification/
  pikmin2_title_diagnostic_test.cpp:6cases passed MSVC C++14 /W4 /WX,including
  addresses above4GiB,crossing4GiB,8GiB span,null and reversed markers.
  This is a narrow host semantic/compile check,not whole-P2/iOS validation.
  git diff --check passed. No P1 source or workflow change for this correction.
- Next:commit correction with this journal using[ios-build],fetch/reconcile,push
  one coordinated Build14,record ID,and STOP idle polling. Retrieve completed logs
  only when user reports done. P1Build13can be tested independently whileP2builds.

## Build14 dispatch checkpoint — October19, 2026, ~16:47 Eastern

Local/origin ios-experimental HEAD 36d0f156aa92f6bbedad91d3573bc1694bef131b;push succeeded.
Build14 run39322155722:https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39322155722
Initial status in_progress. STOP idle polling and await user completion report.
Includes P2 title diagnostic fix;P1 source exactly the successful enhancedBuild13.
P1Build13IPA is ready in the friendly install folder;await user hardware feedback.
No new Apple result for the P2 fix;no P2 IPA established. Only this post-push
status checkpoint is uncommitted;source/workflow/prior docs are committed/pushed.

## Build14 result / waypoint iterator fix — October 19, 2026, 17:14 Eastern

- Run39322155722 at36d0f156aa92f6bbedad91d3573bc1694bef131b completed:
  P1 job118298648192 SUCCESS; P2 job118298647821 FAILURE.
  P1 artifact12220854422; P2 failure-log artifact12221311918.
- P1 source is identical to the supplied enhanced Build13 IPA; no redundant IPA
  download/test requested. User has not yet reported its enhanced phone results.
  Readable menu/camera remain confirmed on the earlier phone-tested baseline.
- Full workflow logs retrieved to work/build14-logs.zip and work/build14-full.
  Exactly two unique compiler errors in plugProjectKandoU/routeMgr.cpp:
  line768:21 pointer-to-s16, line777:17 pointer-to-int. One root cause: pointer-
  shaped Container handles encode integer slots but are cast directly to narrow
  integers. No linker stage reached; previous title debug pointer errors absent.
- GameRouteMgr::get now decodes through std::intptr_t before intentionally
  narrowing to existing signed16-bit WayPoint ID; getNext increments pointer-width
  integer; getEnd encodes mCount via pointer-width integer. getStart zero is unchanged.
  Changes guarded by PIKI_PC_PORT; original retail bodies preserved. EditorRouteMgr
  uses actual node pointers and is unchanged. No new waypoint range or data layout.
- Actual four GameRouteMgr methods extracted into a host fixture and compiled/run
  with MSVC C++14 /W4 /WX. Passed traversals of0,1,8,32768points; -1-to-start;
  high handle above4GiB; crossing4GiB; fullu16 end-count encoding. All valid IDs
  select/order exactly their original slots; the high-handle checks do not dereference.
  Fixture: work/resume-verification/pikmin2_route_iterator_test.cpp; test-route.cmd.
  This is a narrow semantic check, not whole-game/iOS compilation or runtime proof.
- git diff --check passed. P1 source, iOS CMake and workflow are unchanged.
- Next: commit scoped route correction+journals with[ios-build],fetch/reconcile,
  push once and record Build15. STOP idle polling while GitHub compiles. Retrieve
  completed logs after user reports. Continue from real compiler/linker evidence.
- P1 additions explained to user: readable settings; sharper scene/FXAA/anisotropy/
  subtle bloom; Chain Actions, Hold to Pluck, Better Pathfinding, Idle Counter,
  Instant Whistle, Quick Grab, No Tripping, Cancel Throw withB, Throw While Moving,
  manual Lock-On/Charge; native Files ZIP importer with staged installs/backups;
  one-time config profile/backup preserving future choices. Camera preserved.
  External HD texture/model files and online co-op are not installed/implemented.
  Online with Raye for both iPhone games remains the final milestone.

## Build15 dispatch — October 19, 2026, 17:15 Eastern

Local/origin ios-experimental HEAD 31791d78ca32cca2ea88d6a21d87c03fcafb519f; push succeeded.
Build15 run39325940839: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39325940839
Initial status in_progress; final compiler/IPA results pending. STOP idle polling
and await user completion report. P1 source remains successful enhanced Build13;
no replacement download/test is needed. P2 includes tested waypoint handle fix.
Only this post-push status note is dirty. All source and prior journals pushed.

## P1 enhanced candidate feedback — October 19, 2026, 17:32 Eastern

User reports the enhanced P1 appears to fully work and looks a bit clearer.
Screenshot "Screenshot 2026-10-19 173104.png" shows Bloom Subtle, Texture Packs
0 installed and HD Models0/11files. This is expected: no external texture/model
payload has been installed. Clarity/effect changes use the original game assets.
Do not diagnose the accurate inventory as a UI bug or claim HD assets are hidden.
Record this as positive initial user runtime feedback, not full campaign or
per-feature verification. Specific charge, picker, save/load, sustained thermal/
performance and real asset import results have not been individually established.
No source/settings/app data changed in response. Next asset phase is actual mobile
texture/model file selection/import; online with Raye stays last. No build triggered
for this documentation. P2Build15result remains pending; do not idle-poll it.

## Build15 result / performance HUD / saving investigation — October19,17:48 Eastern

Build15 run39325940839 at31791d78ca32cca2ea88d6a21d87c03fcafb519f completed:
P1 job118311684052 success;P2 job118311683504 failure. Artifacts:P1 12223277348,
P2log12223476178. Existing enhanced Build13P1 remains the same source;no repeated
IPA download. Full logs savedwork/build15-logs.zip,work/build15-full;unique errors
work/build15-errors.txt. Previous route/title/adapter errors absent.

P2 has four fatal compiler errors in plugProjectKandoU/pelletMgr.cpp2890,2895,
2923,2928:PelletIterator decodes opaque pool-slot handles directly toint/u32.
Corrected native paths viaintptr_t/uintptr_t,including integer-to-handle encoding,
retaining boundedint mIndex,original unsigned32end comparisons and retail branches.
Actual6methods extracted/tested inwork/resume-verification/pikmin2_pellet_iterator_test.cpp,
test-pellet.cmd. MSVC C++14 /W4 /WX passed no-pool,leading/middle/trailing empty,
sparse active pools,ordered iteration,restart and end detection. No new data layout.
Full Apple/P2build and runtime remain pending.

User reports P1 looks clearer/appears to work and120FPS mode feels beautiful.
Record subjective feedback;actual render rate,thermal/memory headroom and sustained
behavior not measured yet. External HD texture/model payloads still not installed.

Added optional P1 iPhone Settings>Display>Performance HUD,defaultOff,persisted as
iosPerformanceHud;close settings to apply. It does not reset120FPS/user choices.
Measures completed SDL render submissions with monotonic timestamps (not physical
panel refresh),240-frame mean/p95/p99,app physical memory footprint,Mach task_info,
os_proc_available_memory advisory app headroom,process CPUtime fromgetrusage,
iOSthermalState andLowPower. CPU100%=onecore,can exceed100%. No GPUutilisation or
fake temperature/headroom-safe verdict. Native metrics/text refresh1Hz;fixed ring;
duplicate/invalid timestamps ignored;long suspension/backward clock resets history
and CPUbaseline. HUDoff performs no native sampling or per-frame clock reads.
Does not enable heavy per-draw profiling. Native Foundation/Mach code isolated in
nectar_ios_storage to avoidGameCubeBOOL conflicts. No renderer FBO binding changes.
30 actual-repo model/controller checks pass MSVC17 /W4 /WX;added P1CI host check.
One duplicate-timestamp/throttle defect caught by test was fixed before committing.
Full UIKit/Mach build and phone HUD layout/readings still require CI/hardware.

Saving investigated fromDayOverModeState,ogSave,MemoryCard::saveCurrentGame,
write/readCurrentGame,PlayerState::saveCard andnativecard saveRoot. Current behavior
is the normal end-of-day save/checkpoint flow. NO timed mid-day autosave/save-anywhere
is implemented. Existing serializer is not a complete live-world snapshot;do not
call it periodically and claim it restores mid-day enemies/Pikmin/clock/state.
No save routines,format,timing or user files modified. Expected ordinary card path:
Files>On My iPhone>Open Nectar Pikmin1>pikmin1>save>card0. Copy whole save folder
after completing save/closing app to back up checkpoints;retain appdata onupdate.
Normal save/close/relaunch/Continue still needs user verification. A proper mid-day
recovery/manual-save feature remains separate required future work,not completed.

Guide ios/PERFORMANCE_AND_SAVING.md copied to outputs andfriendlyfolder2 as
iPhone Performance and Saving Guide.txt. Explains readings/limits,120FPS8.33ms
budget,comparing representative10-15minute runs before adding mobilepacks,onepack
at a time,source references,and exact save/recovery limits. Public Apple APIs only.

Next:scoped commitsP2fix/P1diagnostics/docs,push once forBuild16,recordrun,and STOP
idle polling. After success prepare a clearly named candidate in friendlyfolder1
and ask user to enableHUD and report readings;then choose realHDassets. Continue
P2fromactual logs. Saving improvements andonlinewithRaye are not falsely marked done;
online forBOTHnativeiPhonegames remains the final milestone.

## Build16 dispatch — October19,2026,17:47 Eastern

Local/origin ios-experimental HEAD 01ea8330415171b9d8f61dbc89567ed5f5959c8e. Push succeeded;source clean atpush.
Includes4f3576c0(P2pellet casts),f9c08c55(optionalP1HUD),01ea8330(docs/buildmarker).
Build16 run39330204354:https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39330204354
Initial statusin_progress;final Apple compile/IPA outcomes unknown. STOP idle
polling;user reports completion. Only this post-push status note is dirty.
Current phone still uses enhancedBuild13;newHUD requires successfulBuild16IPA.
No actual HDassets,manual mid-day save or periodic autosave added. Save routines
and user save data unchanged. Saving/monitoring guide copied to friendlyfolder2.
Next:fetch completed logs;prepare successful P1HUDIPA in friendlyfolder1,test
Display>PerformanceHUDOn/closemenu,real readings andrender preservation;check
normal end-day save/close/relaunch;use measured readings before adding realpacks.
ContinueP2fromactual compiler/linker output. OnlinewithRaye remains last.

## Build16 result and broader P2 batch — 2026-10-19 18:18 Eastern Daylight Time

User explicitly wants bigger related batches, not smallest-safe-fix/build cycles.
Audit shared compatibility causes and related active source before pushing. Preserve
P1; do not hide errors or make unverified broad gameplay changes to appear faster.

Build16 run39330204354 at 01ea8330415171b9d8f61dbc89567ed5f5959c8e: P1 job118326155905 passed,
P2 job118326156146 failed. P1 artifact12225271604 contains the new HUD IPA;
P2 artifact12224648508 is logs, not a successful app. Full logs retrieved directly.
P2 has seven fatal diagnostics (six distinct error lines) in pcMovieInterp.cpp
container instantiations: five vector and two unordered container cases. Root cause:
forced adapter globally defines nullptr as integer0 on Apple, corrupting libc++
pointer forwarding. All are one shared cause, different from prior pellet/route casts.

Broader batch implemented, not yet Apple-compiled: exclude Apple from the legacy
nullptr macro, matching existing Android behavior; native CPlate and Stickers
get/getNext/getEnd decode/encode via intptr_t, preserving retail branches, fields,
and Stickers bounds assertion. No P1 game source changed. Opaque-index audit found
31 definitions; other narrow-cast matches inspected are comments or retail guards.
This is a targeted audit, not proof every legacy pointer assumption is eliminated.

tests/pikmin2_apple_nullptr_test.cpp checks the real adapter BEFORE affected STL
headers, keyword type and all seven container specializations. Local actual-header
Windows harness passes MSVC17 /W4 /WX; restores MSVC identity around the GCC-targeted
header and cannot validate Apple libc++. tests/pikmin2_container_handles_test.py
extracts all eight actual CPlate/Stickers methods and real bounds macro: MSVC17
/W4 /WX passes 0/1/100/110/10000 entries, ordered iteration, -1 sentinel, >4GiB next
handles, invalid and high-handle bounds rejection. Both run early on macOS in CI.
43-header adapter audit and git diff --check pass. Full iOS compilation remains pending.

P2 workflow now uses CMake Unix Makefiles + make -k to continue independent source
compiles after failures and expose a batch of errors. P1 retains verified Xcode.
Release/iphoneos/ARM64/iOS15/lipo verification and failure gating retained. Bounded
90-minute jobs. CMake officially supports Makefiles for iOS with explicit CPU/SDK;
this generator change still needs the actual Apple runner and may itself need repair.
tests/ios_build_error_summary.py writes distinct error index plus complete logs;
verified on the full Build16 log (six distinct lines from seven diagnostics).
No error suppression or success-on-failure added. GNU make -k does not guarantee
linker diagnostics until compilation succeeds; some dependent work cannot run.

P1 Build16 IPA ZIP/plist/ARM64 checked, 2575697 bytes; SHA256
02041fc3c82b757b6a0cfc62592bf855c8b6e4deca63ca4ba64eb0704747bec6.
Friendly copy verified in 1 - Install on iPhone/Pikmin 1 - Build 16 - Performance Display.ipa,
with WHAT TO TEST.txt. Hardware layout/readings remain pending. User previously
reports Build13 works, clearer and120FPS mode feels beautiful, not measured120FPS.
No external HD payload, mid-day autosave/manual recovery or online co-op added.
Normal end-day save/relaunch test still required. Online with Raye for both games last.

Next: commit scoped P2 source/tests, then workflow/journal with final [ios-build],
push once, record run ID, and STOP idle polling. User reports completion. Prepare
batch from full next run error index/logs; do not assume success before CI.

## Build17 batch dispatched — 2026-10-19 18:19 Eastern Daylight Time

Pushed once to ios-experimental. Local/origin HEAD 02ec11b866bbc39a21d6d5a8641a60790b3621d1.
Commits:5542499c (shared Apple nullptr plus CPlate/Stickers handles/tests),
02ec11b8 (P2 keep-going diagnostics, error index, journals and build marker).
Build17 run39334027043:https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39334027043
Initial queued, not compiled/packaged/runtime-verified. Stop idle polling; user
will report completion. Source/tests/workflow clean after push; only this dispatch
checkpoint in ios/OPEN_NECTAR_IOS_STATUS.md is dirty. No unexpected source changes.

P1 Build16 successful HUD IPA already copied/hash-verified to friendly folder1;
WHAT TO TEST.txt and verification JSON supplied; requested audio alert played.
Phone HUD/readings/normal save reload pending. No HD assets/autosave/co-op added.
Next agent action: when Build17 finishes retrieve full job logs and error index,
batch remaining related errors. Check generator/configure errors before compiler
diagnosis. P1 source unchanged from passed Build16; no redundant install needed
unless new evidence or source changes justify it. Online with Raye remains last.

## P1 Build16 phone HUD evidence and ProMotion opt-in — 2026-10-19 18:33 Eastern Daylight Time

User supplied a real gameplay screenshot from the new performance display, reporting
120FPS selected but very smooth gameplay. HUD visibly reports Render60.0 FPS,
average16.67ms, AppCPU40% (onecore=100%), HeatNominal, LowPowerOff. CPU40% does NOT
mean40%of all phone CPU capacity. No exact RAM/spare or frame-tail values transcribed
from the small screenshot; inspect original for those. This single snapshot validates
HUD display and live sampling during gameplay, not sustained thermals/memory/HD safety,
physicalpanel120Hz or save/reload. User has not reported a10-15minute comparison yet.

Investigated scheduler/high-rate and SDLUIKit presentation paths. Existing bundled
SDL_uikitviewcontroller.m:122-133 already creates a preferredFrameRateRange request
on >60Hz iPhone displays and explicitly requires Info.plist
CADisableMinimumFrameDurationOnPhone=true. Both source template and actual Build16
packaged IPA lack that key. Apple documents it is needed for faster iPhone ProMotion
timing hints. This is an identified configuration omission and leading explanation
for a steady60 cap; GPU saturation, OS settings or other pacing issues are not yet
excluded by hardware evidence. Do not promise120FPS from this declaration alone.

Implemented only the boolean opt-in in shared ios/Info.plist.in. Both games inherit
it when built; it permits higher rates rather than forcing120FPS or changing game
FPS configuration. Renderer, SDL framebuffer correction, camera, touch, saves and
game logic untouched. Local plistlib parse/configure for each game passes and dictionary
comparison confirms this is the sole metadata change; Build16 packaged absence verified.
No new tests added for a reversible one-key metadata fix. Actual Apple packaging and
phone60vs120 test pending. Retain user FPS preference, do not force hardware refresh.

Sources:
https://developer.apple.com/documentation/bundleresources/information-property-list/cadisableminimumframedurationonphone
https://developer.apple.com/documentation/quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays

Correction is UNCOMMITTED and NOT PUSHED, held for next coordinated batch after
Build17 so no redundant run is triggered. HEAD/origin remain02ec11b866bbc39a21d6d5a8641a60790b3621d1.
Dirty files:ios/Info.plist.in andios/OPEN_NECTAR_IOS_STATUS.md (includes dispatch note).
Build17run39334027043 uses the older plist and CANNOT validate this pending correction.
Do not ask user to reinstall Build17 expecting this fix. No build polling performed.
Next:retrieve Build17 full P2 result when user reports, batch related corrections,
include this plist change, verify generated IPA has boolean key, then ask user for
same-area120FPS HUD reading. If still60, inspect OS frame limit and actual render/pacing.
No HD payload installed, no mid-dayautosave/manualsave or online co-op implemented.

## Build17 full results, broad native-address batch, and 60FPS priority — 2026-10-19 21:45 Eastern Daylight Time

User explicitly cancels120FPS work: keep60FPS and budget for HD textures, all
supported optional character/model packs and associated compatible upstream content.
Removed ONLY our uncommitted ProMotion plist opt-in; Info.plist.in now matchesHEAD.
No P1 game source altered. Current phone still can show120selected while actual60;
user should choose Display>FPSMode60 once to match requested simulation/pacing mode.
P1 Build16 HUD confirmed live in earlier screenshot (60/16.67ms,CPU40%ofonecore,
HeatNominal,LowPowerOff); subjective smoothness positive. No sustained/HDheadroom proof.

Build17run39334027043/02ec11b8 completed: P1successjob118338903254,
P2failurejob118338902944. P1artifact12225988208 (same source as installedBuild16;
no redundant install). P2artifact12226262590 contains167591189byte complete rawlog
and26318byte error index. Downloaded directly. API logs have aggregatejobfiles
plusrunner-systemsubfolders; don't confuse system.txt with full build output.
New Makefiles keep-going configuration and Apple nullptr/container host checks PASS.

Full compilation exposes102 diagnostics:84 located pointer-width sites,11 linkage
conflicts,6 incomplete-model accesses,plus1 genPellet pointer diagnostic interleaved
into a register warning. These are a batch of earlier latent failures, not102 known
new regressions. No successful P2 link/IPA/runtime. Index/source contexts inwork/
build17-pikmin2,build17-errors.txt,build17-source-contexts.txt; concise copyoutputs/
Build17-P2-ERRORS.md. Important genPellet.cpp43 diagnostic recovered manually.

Broader source batch implemented, not Apple-compiled yet:
- P2Address/P2SignedAddress aliases use native uintptr_t/intptr_t;u32 file sizes,
  serialized offsets and packed DSP/sample fields stay32bit. Original console
  aliases stay32bit. Native class-layout comments remain originalconsole offsets.
- Widen actual RAM addresses end-to-end through ARQ/JKRAMCommand/JKRAramPcs/
  orderSync andcallback signatures;AI DMA setter/storage/getter;memoryarchive
  identities/constructor/cache lookup andcompoundarchive memorybase. Narrowing
  only at the original RAM API callsite would still truncate in receivers.
- Address arithmetic/alignment/hash/modeloffset/threadstack/checksum paths use
  full-width values first. Alignmentmask also pointer-sized for unsigned32alignment.
  Final bounded modelcounts explicitly narrowed after subtracting full addresses.
- Fontcache initialization writes typed mPrev/mNext pointers,notint[2] into64bit
  fields; handles emptycache; doesn't clobber glyph metadata.
- True32bit ARAMoffset/count values represented asvoid* usepc_p2_aram_offset,
  rejecting >UINT32_MAX rather than silently accepting a hostpointer. Wave/stream
  sources checked against their existing offset conventions (e.g. mDataOffset).
- Generator event base+alloverrides carryP2Address,includinghidden genPellet case;
  OSmessages/sentinels decoded with explicit width/wrap behavior;MapCode writes
  itsactualbyte directly;ARAMnode result is boolean success as consumed byMgr.
- Match11extern definitions orrenameprivateGXtable;includecompleteJ3DModel in
  J3DUMtxCache header for6memberaccesses. NativeDSP uses existing typed software
  tablehook instead of empty console DsetupTable with truncated addresses.
- Debugpointerformat uses%p;nativeheapchart usesrealroot start,not0x80000000.
  MatchingwideDMA diagnostic format. No hidden pointer-to-int warning suppression.

Verification: actual-header nullptr/STL test andactual8container-method suite pass
MSVC17/W4/WX. Newtests/pikmin2_native_addresses_test.py extracts actual aliases,
ARQ/AI signatures/fields/implementations,DMAdispatch,fontcache,MapCode,modeloffsets,
andheapchart intohostfixture. MSVC17/W4/WX passed highaddresses,callbackroundtrip,
32bitlength preservation,16unsignedalignmentcases,valid/rejectedARAMboundaries,
0/1/3/7fontpages+metadata,all256mapbytes,chartclamps andmodelcounts. Testfirstcaught
model-count narrowing warnings; explicit finalcounts corrected. A fixture-only
buffer allocation assumedmax_align_t16;Windows8 causedtestcrash;fixture corrected
toallocate bybytes. No claim that was a gamecrash or hardwarevalidation.
Reviewcaught remainingorderSync declaration src/destnames;fixed before finaltest.
Actual Apple complete compilation/link and first P2 runtime still pending.
Native DMA transfer stubs still only complete/store requests; no new DMAcopy engine
or claim that the game's unused legacy ARAM paths now work at runtime.

CI now runs newhostfixture early,retainsmake-k,adds onlyobsolete-register warning
silencing onAppleClang (huge167MBlognoise),prefersalready-installedgmake whenpresent,
andusesoutput-sync only ifselectedmakeadvertises it. No toolinstall/flags that
silence pointer truncation errors. One coordinated push after finalchecks.

Optional content request NOT completed yet: upstreamlauncher explicitly supplies
mobilePNGpack P1 id1870dA11T9FpuLQDnI3axoCJ_Eh5ptgWP (925049459bytes),P2
id1blzsLSFBr617h-gP7lvp_7HqsLRyQWzl (1072944206bytes). DesktopDDS variants exist
but mobilePNG is intended mobileinput. Siximportrows supported:OlimarHD,LouieP2,
LouieHD,PikminHD (3colors+3leafparts),Bulborb,Dwarf. AdditionalP2captains require
existingpc_hd_models_import_pikmin2 using privatepikis.szs (Louie/President/white/
purple/Bulbmin+portraits). No assets downloaded/installed yet in this checkpoint.
The Models Resource moved to models.spriters-resource.com;assetpages inspected
normally. Originaloldhost sometimes403,newofficial URLs work. Sources/inventory
andpackpreparation are next;keepall proprietaryassets outsideGit. Phone transfer/
activation andperformanceverification not yet done. Userauthorizedalloptionalcontent
does not mean claimunsupported models installed or enablesave-destructive modes.
No timedmid-dayautosave/manualsave oronlineco-op added. OnlinewithRaye remainsLAST.

## Build18 shared configuration failure and recovery — 2026-10-19 21:53 Eastern Daylight Time

Build18 run39355267175 at9d33219f43dd0cf69b645b7c74c8185a711967e6 failed
both games BEFORE game compilation. The shared configure step expanded an empty
CONFIGURE_ARGS array under set -u; the runner reported CONFIGURE_ARGS[@]: unbound
variable. This workflow mistake was introduced by Codex, not a new game-source
regression. No IPA was produced. P1 host profile/import/performance checks passed;
P2 adapter, Apple nullptr, container and new native-address host checks passed.
Full P2 compile/link/runtime is still unverified.

Recovery uses a non-empty complete CMake command array, appending the optional
already-installed gmake path only for P2. All iOS target arguments stay identical.
No P1 source or Info.plist edits; target remains60FPS. Both branches reviewed.
Local Apple SDK/shell validation unavailable; actual runner validation pending.
The earlier P2 batch is committed as ec702737; workflow/docs as9d33219f.
One recovery push will trigger Build19 with the same broad P2 source batch.
Optional-content preparation remains incomplete; one original Pikmin3 model ZIP
was downloaded to Downloads/302842.zip, not yet verified or installed. Mobile
PNG texture download returned an HTML confirmation page, not a verified pack.
Next: record recovery SHA/run, stop idle polling, prepare supported private
texture/character packages in Documents/Open Nectar/7 - Optional Graphics and Characters.

## Build19 reaches final P2 link; character bundle prepared — 2026-10-19 22:09 Eastern Daylight Time

Recovery0419685b02fd4da80cd91dcb83aa867fde09691c pushed; Build19run39355903504.
Configuration now succeeds for both. P1 host checks/configuration passed and compile
was in progress at last check (job118410485014). No P1 source changed.
P2job118410484796 compiled to100% then failed final arm64 link with ONE missing
symbol: thread-local wrapper routine for __GDCurrentDL. No compiler errors in
the complete127950929byte raw log. Artifact12236055046 downloaded directly into
session work/build19-pikmin2. Previous broad102-diagnostic batch now compiles.
No P2 IPA or phone runtime yet.

GDBase.c defines a constant-initialized C _Thread_local pointer; the legacy GD
header exposed it to C++ as thread_local, requesting a C++ initializer wrapper
not emitted by the C source on Apple. Both GD header copies now use Clang's
C TLS spelling in C++ as well, while retaining other-compiler/retail branches.
Thread isolation is preserved, not replaced by a process-global pointer.
Reference: https://clang.llvm.org/docs/LanguageExtensions.html (C11 _Thread_local
available with C semantics in all language modes). Actual Apple link still pending.

New tests/pikmin2_gd_tls_test.py extracts both actual declarations, real structure,
real inline writer and C storage definition into mixed C/C++ multi-unit link and
three-thread isolation check. Windows/MSVC check passed, using __declspec(thread)
for the C11 TLS spelling because MSVC lacks that C keyword. This does not validate
Clang's spelling or Apple ABI; the same fixture runs with actual C11+C++17 Clang
on macOS before full compilation. Error summary now includes actual missing symbol
names; checked against complete Build19 log and timestamped copy, excluding warnings.

Next push uses [ios-build] [ios-p2-only] to validate P2 without duplicating P1's
unchanged ongoing Build19 compile. Default marked pushes still build both. Matrix
selection uses standard Actions contains/fromJSON expressions. No idle polling.

All SIX supported public model ZIPs downloaded normally, CRC/SHA256 verified and
originals copied privately into Documents/Open Nectar/7 - Optional Graphics and
Characters/2 - Original Downloads. Upstream Python converter produced11 models.
Two source archives read-only extracted from owned GPVE01 ISO (pikis.szs354208bytes,
res_ground.szs189792bytes). Existing unmodified C++ importer produced5 extra-model
outputs including alternative Louie and3 portraits. Preserve the main Louie and
alternative separately; merge4 extra characters and3 portraits into ready bundle.

Ready PRIVATE bundle:1 - Ready for iPhone/Pikmin 1 - All Character Packs.zip
2813255bytes, SHA2567fa0bacc8f99349b0fd84d8b2a43716e91e68d033ca989c96a414a72dfc1538c.
20 entries:15 NHM models,3 portrait PNGs,2 small P2 source archives. Last2 are needed
by existing captain availability detection, under pikmin1/pikmin2/assets/. No full
P2 assets/game installed in P1. HD menu counter is11/11;4 extra-captain models are
separate. Binary headers,parts,bones,finite values,joint indices,texture sizes,
exact file boundaries,PNG decoding andZIP CRC passed locally. This is NOT phone
installation, visual validation or sustained performance proof. Target60FPS.
No save/config files included. Simple transfer guide and manifest beside bundle.

P1 official mobile texture source AND official1080p alternative both return
Google Drive QUOTA EXCEEDED HTML, not ZIP. No texture payload installed. Official
upstream releases mention this known quota scenario; no alternate official mirror
found in the focused source/release check. Do not pretend texture content present.
Optional mods already built into menus remain available; no forced difficulty,
cheats, randomizer or destructive mode changes. Mid-day saving and online withRaye
remain future work (online LAST). Phone transfer request pending; audio cue played.

## Dispatch/result checkpoint — 2026-10-19 22:12 Eastern Daylight Time

P1 Build19 SUCCESS, including unsigned IPA packaging; artifact12235976028. No
P1 game source changed; existing phone Build16 remains suitable for content tests.
P2 Build19 final-link failure above. Link fix committed/pushed06fdd716de120551fa4083d4043e6513144bd517.
Build20run39357443512 in progress at dispatch check; verified exactly ONE job,
build(pikmin2), so the P2-only matrix option works. No result/IPA confirmed yet.
https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39357443512
User postponed phone connection/transfer because busy. Do not keep requesting it.
Character bundle is prepared, NOT installed. No idle build polling; user will
report when done. These two final journal updates are intentionally uncommitted
documentation only, to include with the next source milestone without extra build.

## Build20 test-fixture dependency failure — 2026-10-19 22:14 Eastern Daylight Time

Build20run39357443512 at06fdd716de120551fa4083d4043e6513144bd517
failed job118415402674 in the early GD TLS smoke fixture, before game configure
or compilation. Generated gd-storage.c used the real GDBase.c NULL initializer
but fixture gd-0.h included stdint.h only, not stddef.h. Apple's C compiler
correctly reported undeclared NULL. Earlier Windows test passed because its
headers provided NULL transitively. This omission was Codex's test setup mistake,
not a newly observed game error. P1 did not run in Build20; Build19 P1 remains
SUCCESS with IPA artifact12235976028. Full Build20 job log saved work/build20-job.log.
Artifact12235768616 is only269bytes (no game compile log/IPA), not a P2 app.

Correction adds explicit standard stddef.h to generated fixture headers. No game
source, workflow, thread storage declaration, settings or save changes. Local
mixed C/C++ link and three-thread fixture will be regenerated/rechecked before
push; Apple ABI/link and full game build remain pending. One P2-only Build21
will validate the existing GD linkage correction after this dependency fix.
Preserve prior two pending journal appends and include them in this commit.
Character bundle remains ready privately; phone transfer explicitly postponed
by user; official texture downloads remain quota-blocked. No idle polling.

## Build21 FIRST successful P2 compilation/link; IPA metadata correction — 2026-10-19 22:37 Eastern Daylight Time

Build21run39357838317/sourcee4906f89/job118416685307 passed all Apple host tests,
including mixed C/C++ GD TLS link+three-thread test. FULL P2 iOS ARM64 target
pikmin2_pc COMPILED AND LINKED SUCCESSFULLY at100%. Error index0 compiler/linker
errors. This is a new confirmed milestone; not a runtime/IPA success yet.
The subsequent unsigned packaging step failed because CFBundleExecutable was
literal $(EXECUTABLE_NAME). Xcode expands that build-setting token for P1;
Makefiles does not. lipo attempted a nonexistent file named $(EXECUTABLE_NAME).
Actual built binary path was app/Nectar-pikmin2.app/Nectar-pikmin2.
Full job log:session work/build21-job.log. Artifact12236422070 contains logs/index
(3800110byte archive); no IPA or preserved executable in that artifact.

Fix shared bundle metadata at its source: CMake sets NECTAR_IOS_EXECUTABLE once
and uses it for OUTPUT_NAME and @ONLY-configured Info.plist CFBundleExecutable.
No fallback executable guessing or renaming. Labels, IDs and other plist fields
retain prior values. New ios/verify_bundle_info.py validates game-specific
identity/executable/name and rejects unresolved template tokens. CI calls it
immediately after CMake configure (fail before expensive compilation) and again
on the actual .app with a required nonempty binary before lipo/ZIP.
Local verification uses the installed real CMake to configure the actual template
for both games, compares every P1 configured field to the known working Build16
IPA, and checks placeholder/wrong-ID/missing/empty-binary rejection. Results will
be recorded after checks. No game source, savedata, graphics or controls edited.
Build22 will validate BOTH games because bundle metadata is shared, preserving
the working P1 output while producing P2's first IPA if packaging passes.
Character pack still ready privately; phone work postponed; HD textures quota
blocked; target60FPS, online withRayeLAST. Stop idle polling after dispatch.

## Build22 BOTH PASSED — first verified P2 IPA ready — 2026-10-19 23:07 Eastern Daylight Time

Run39359925649/sourcea16a3bae9f524ec4c2e4548a6ab5330a82031321:
P1job118423468727 SUCCESS andP2job118423468451 SUCCESS, including metadata
preflight,compilation,link,arm64/lipo and unsignedIPA packaging. P2artifact
12237930806 (7580578bytes);P1artifact12237826313 (2867471bytes). Both downloaded.
P2IPA3823331bytes,ARM64binary11064544bytes,SHA256
36976c498d943ad30b3dfe0290689638013a8fe8e5042ef0d370741c4cb94fd6.
P1IPA2575697bytes,ARM64binary6358656bytes,SHA256
2cb997dc570a1e7222e3e35d47acc614f13af4efd4556df251982d63fa559ac0.
Both ZIPCRC and exact app identity/executable passed; MachO load commands verify
iPhoneOS device platform,not simulator; linked libraries use system paths.
No code-signature command present,consistent with intentionally unsigned outputs.
No proprietary disc assets bundled. MinimumOS15.0. Hardware install/runtime for
these builds NOT verified. This is P2's FIRST successful IPA milestone.

User explicitly wants to leave working P1 app alone. Keep separate apps:
P1org.opennectar.experimental.pikmin1;P2org.opennectar.experimental.pikmin2.
No unified launcher/app migration. No P1phone update or content transfer now.
P2ready inDocuments/Open Nectar/1 - Install on iPhone/Pikmin 2 - Build 22 - First
iPhone Build.ipa. NewP1IPA retained in5 - Backups and Older Files/Build 22 - P1
Reference Only to avoid unnecessary reinstall. Existing P1Build16 remains working.

Prepared P2 assets privately from user's GPVE01ISO using unmodified upstream
gamecube_image.cpp+sha256.cpp,verifyWrites=true.2768 game files,1004985055bytes.
Every file read back and SHA256-compared by extractor; additional per-fileSHA256
manifest in3 - Game Files - Keep Private/Extracted for iPhone/Pikmin 2. Original
ISO opened read-only;SHA1before/after both63a68c656d654388e096d27a768e85823dcf3327.
Added the same .pikmin2-assets marker as upstream installer. No game data inGit.
Simple P2install/test guide and game-assets-folder shortcut in1 - Install on iPhone.
Phone transfer explicitly postponed by user; no repeated connection prompt.
Next: when ready,sign/install P2,open once/close,copyassets into separate P2app
Documents/pikmin2/assets,then verify startup/menu/graphics/audio/input/gameplay.
Do not claim runtime success from build/package checks. Optional P1models ready
privately but onhold;HDenvironmenttexturequota-blocked atlastattempt;60FPStarget;
mid-dayrecovery saving and onlinewithRaye remainfuture (onlineLAST).
This documentation-only checkpoint uses [skip ci] to avoid an extra build.

## P2 transfer completeness audit and missing touch-art correction — 2026-10-19 23:22 Eastern Daylight Time

User explicitly asked about missing Art after the earlier P1 experience. The
prepared P2 disc assets were complete, but the standalone touchscreen artwork
was omitted from the transfer folder. Codex corrected that preparation omission.
No phone operation, game-source edit or new IPA build is necessary for this fix.
Build22 source/IPA remains the verifieda16a3bae build. P1 untouched.

Independent audit reparsed current GPVE01ISO FST with the same UTF8/CP932 name
conversion as upstream and matched EVERY2768 file path,size,SHA256 to the prepared
assets and prior manifest,with zero missing/extra disc files (onlyupstreammarker).
Disc game payload1004985055bytes. Touch source references28unique PNG names.
Copied all26P2source PNGs plus shared lock_on.png andcharge.png from the P1source
art directory (not the phone);all28exact-source hashes and PNGdecodes passed.
All referencedtouchartnames covered. P2touch loader searches relative art/,not
Load/Art and not assets/art. Separate lowercase art folder now sits besideassets.

Audited8Yaz0/RARC UIarchives for exact requestedBTI/BFN entries: pauseglass,UFOdots,
repaymentbuttons,encyclopediabuttons,challengeselect,foreignfont,sprayicons and
portraitfaces. All requested entries present,including pikmin2main.bfn. P2's
fallbacksettingsfont is also compiled into pc_ui_font.h;no externalTTF needed.
Full result:privateP2folder/P2 Complete Transfer Verification.json andsession
work/p2-completeness-audit.json. Native loaders/source reviewed; caches/settings/
saves are generated at runtime,HDreplacement folders remain optional.

Correct transfer:copy BOTH assets AND art fromDocuments/Open Nectar/3 - Game
Files - Keep Private/Extracted for iPhone/Pikmin 2 into the separate P2app
Documents/pikmin2. Expectpikmin2/assets/user/... andpikmin2/art/bubble.png.
The existing game-files shortcut opens this parentfolder. START HERE andWHATTO
TEST guides corrected;previous instructions preserved in5/Instructions-Before
P2ArtAudit. No modifications to working P1app,settings,save orcontent.
Base-data/UI completeness verified onPC;phone transfer/runtime stillNOT tested.
OptionalHDtextures/models not part of basegamepayload,still not installed;last
textureattempt quota-blocked. Phoneworkonholduntiluserready. Docscheckpoint[skip ci].

## P2 startup crash investigation and allocator candidate - 2026-10-20 00:22 Eastern Daylight Time

The user installed Build22 P2 and reports immediate closure even after assets
and art transfer. P2 runtime is now confirmed FAILING; compilation/IPA success
does not imply startup success. The user connected/unlocked the phone, and Codex
read five existing P2 .ips reports without moving, deleting or synchronizing
device reports. Raw logs/device details remain private in the session workspace.
The three latest reports match the exact Build22 executable UUID
5af9412e-02a6-3446-96d4-90231accd8a5, also read from the archived IPA Mach-O.
They repeatedly show EXC_BAD_ACCESS / SIGBUS / EXC_ARM_DA_ALIGN on the main thread
about 0.24 seconds after launch. Stack: Metal compiler createConnections ->
AppleMetalGLRenderer first render pass -> glDrawArrays_ES2Exec ->
pc_gfx_flush_batch -> pc_gfx_p2_force_stretch -> JUTFader::draw.
Fault addresses have remainder 4 modulo 8 and lie inside P2's 480 MiB game arena.
This is an alignment exception, not evidence of an iOS out-of-memory kill.

Read-only VendDocuments access confirms Documents/pikmin2/assets, the asset
marker, the expected user directories, and Documents/pikmin2/art with all 28
expected PNG filenames; bubble.png is readable. This is a layout/presence check,
not a byte-for-byte rehash of the entire phone payload. The earlier PC audit
did compare all 2768 disc files with ISO paths/sizes/SHA256. No phone files changed.

Inspected JKRHeap.cpp: six global C++ new/new[] overloads routed objects into
the current JKR heap with only 4-byte/default or small explicit alignment.
This violates native fundamental object alignment. The existing host allocation
scope covered GXInit and present, but not the actual first pc_gfx_flush_batch
draw where Apple's driver lazily creates compiler objects. This is the leading
evidence-based explanation for the observed crash; phone retest is required.

Candidate implemented: native C++ new/new[] heap requests use at least
alignof(std::max_align_t). Preserve larger requested alignment, negative tail
allocation direction, explicit heap routing, malloc fallback, and delete routing.
Original non-PIKI_PC_PORT console policy and raw buffer allocation APIs unchanged.
Extend existing renderer host scope to 10 boundaries: batch submission, begin
frame, five overlay texture/draw functions, full-target dim, UI draw, and blur.
Driver work within these scopes allocates from malloc rather than section heaps.
No changes to P1 source, installed app, data, settings, saves, or optional content.

Files: games/pikmin2/pikmin2-decomp/src/JSystem/JKernel/JKRHeap.cpp;
games/pikmin2/pc_port/gl/pc_gfx.cpp; tests/pikmin2_native_allocator_test.py;
.github/workflows/ios-native-experimental.yml; these two journal documents.
The test extracts actual new/delete/policy/scope bodies, renames operators only
to avoid replacing the fixture CRT allocator, and stubs the game heap. It tests
alignment/routing/zero sizes/deallocation, positive/negative explicit alignment,
nested and exception scope restoration, and thread-local isolation. It also
checks host scope precedes executable statements at 11 renderer entries.
Local MSVC C++14 /W4 /WX: native 1344 checks PASS; console policy 1280 checks PASS.
Adapter self-include audit: 43 headers PASS. git diff --check PASS.
These are focused host regression checks, not a complete Windows/iOS game build
or a real driver execution. Apple CI runs both fixture variants before compiling
P2. New iOS compile/link/IPA/installation/runtime all pending for this candidate.

Build22 remains run39359925649/sourcea16a3bae; BOTH compiled, linked, and packaged.
New source push uses [ios-build] [ios-p2-only] so P1 is not rebuilt. Record exact
commit/run after dispatch; stop idle waiting. User watches Actions completion.
When successful, put new P2 IPA in Documents/Open Nectar/1 - Install on iPhone;
update the existing P2 installation while preserving its data (do not uninstall),
then test startup/menu/audio/touch/gameplay. If it still crashes, retrieve a fresh
P2 report, verify its executable UUID against the NEW IPA, compare exception/stack.
Do not assume subsequent failure has this same cause. Never reinstall P1 for this.

P1 remains user-confirmed working on the existing phone build: readable menu,
working camera/movement and reported smooth 60 FPS. Preserve UIKit framebuffer
fix. Optional character package prepared privately but NOT installed on phone;
environment texture download was quota blocked at last check. No timed mid-day
recovery save implemented. Online co-op with Raye remains the final long-term step.

## Startup candidate build dispatched - 2026-10-20 00:23 Eastern Daylight Time

Source commit: 609a45b184b50aeb1a71e581c2c2095f4f664f77
Actions Build23: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39369282124
Status at dispatch: in_progress. P2 only; P1 not scheduled. No new IPA or
hardware retest yet. Host tests: 1344 native + 1280 console checks passed.
The following journal-only checkpoint uses [skip ci], with no extra build.
No idle Actions polling. Retrieve result/logs after user reports completion.

## Build23 P2 startup candidate compiled and packaged - 2026-10-20 00:34 EDT

Verified actual Actions result SUCCESS. Run39369282124, job118453229169,
source 609a45b184b50aeb1a71e581c2c2095f4f664f77. P2-only job; no P1 build.
Apple adapter/standard-library/allocator/GD TLS checks passed, followed by
full iPhoneOS ARM64 compilation, linking, metadata validation and IPA packaging.
Artifact12241127170, archive7609098bytes. Retrieved build log/error index:
0 recognized compiler/linker errors, and actual job compilation/package SUCCESS.

Downloaded IPA: 3823426bytes; ARM64 executable11064832bytes; iPhoneOS device
platform; minimumOS15; exact P2 bundle/executable identity; ZIP CRC and all
Mach-O load-command boundaries PASS. Dynamic-library references are system
paths. Intentionally unsigned, no proprietary disc assets in IPA.
SHA256: 9389d36c43713794c2f0e5737c35b74e0ad8b6f32fcd54f1f5911242903a47c4
Executable UUID: cd97b20e-54c2-396d-9786-3535a215723d
This differs from crashed Build22 UUID5af9412e-02a6-3446-96d4-90231accd8a5.
New reports must match the new UUID after Sideloadly signing/repackaging;
verify the installed executable identity before drawing conclusions.

Copied and SHA256-verified to Documents/Open Nectar/1 - Install on iPhone/
Pikmin 2 - Build 23 - Startup Fix.ipa. Simple START HERE / WHAT TO TEST guides ready.
Moved only the old P2 Build22 IPA to folder5/Build 22 - P2 Startup Crash Reference,
verified unchanged hash; retained prior guides/history and logs. P1 untouched.
User should update existing P2 through Sideloadly with same signing identity,
preserve app data, reuse current phone assets/art, then test launch/title/menu.
No phone operation was performed during this build-result preparation.
Milestones: solution implemented, local checks passed, Apple compilation/link
passed, IPA generated and locally verified. New IPA installation/runtime NOT
verified; startup crash correction is still a candidate until phone evidence.
No further build needed now. This documentation-only checkpoint uses [skip ci].

## Build23 phone startup failure: audio-thread allocation batch - 2026-10-20 00:46 EDT

User updated P2 to Build23 and reports the same immediate-close symptom.
Retrieved fresh existing reports read-only after explicit connection/unlock.
Reports Nectar-pikmin2-2026-10-20-003826.ips and -003841.ips BOTH match Build23
UUIDcd97b20e-54c2-396d-9786-3535a215723d. They crash after about0.25-0.29seconds,
EXC_BAD_ACCESS/SIGBUS/EXC_ARM_DA_ALIGN on an AudioQueue thread (thread21), not
the previous main-thread Metal stack. Stack: AudioToolbox caulk concurrent
allocator -> tracking_allocator -> AQ::API::V2Impl::AllocateBuffer -> SDL
audioqueue_thread -> SDL_RunThread -> pthread. Faults are inside the480MiB JKR
arena; addresses are8-byte aligned but not16-byte aligned. No new phone files,
apps or settings were modified during diagnostic reads. P1 untouched.

Binary evidence: parsed actual Build22/23 Mach-O symbol/load-command data and
decoded MOVZ immediate arguments in ordinary new and new[]. Build22 passes4
in w2 to JKR do_alloc; Build23 passes8, not16. Thus the previous max_align_t
change under-corrected on iPhone ARM64. The Intel-host tests passed but did not
compile the fixture for the actual target. This was a Codex validation gap.
Clang's Apple max_align_t typedef is long double; Apple's ARM64 long double is
the same type format as double. Primary references:
https://clang.llvm.org/doxygen/____stddef__max__align__t_8h_source.html
https://developer.apple.com/documentation/xcode/writing-arm64-code-for-apple-platforms
The observed8-byte machine-code argument, not a host-type assumption, establishes
the actual Build23 behavior. Old graphics scopes did not transfer to SDL's
independently created AudioQueue thread. Its default global-new routing still
used the process-wide current JKR heap, risking native object lifetime/races too.

Related batch implemented:
- Native pc_object_alignment is constexpr and enforces max(16,max_align_t).
  Keep negative tail direction, larger explicit heap alignment, deletion routing,
  and original console behavior. Raw game buffer APIs unchanged.
- A thread-local game-allocation opt-in defaults FALSE on unknown native workers.
  JKRHeap::becomeCurrentHeap enables it on a game thread; pc_thread_entry scopes
  it around the actual emulated OS game callback, restoring on return/unwind.
  Native Apple/SDL threads therefore use malloc instead of the global game heap.
  This does not clear or replace the global heap pointer from a native thread.
- New pc_host_alloc.h contains noncopyable game/native host RAII scopes.
  Audio SinkLock scopes synchronous SDL/framework calls into host memory, with
  nested lock/scope restoration. beginSinkOpen and its worker explicitly use
  host allocation so the std::thread control block also avoids section heaps.
- Existing P2 graphics host scopes retained. No P1 changes or unified app.

Tests expanded from actual allocation/policy/becomeCurrentHeap/callback/scope/
audio-lock source. MSVC C++14 /W4 /WX: native1354 PASS; console1280 PASS;
Apple8-byte scalar-alignment emulation1354 PASS. Native worker default malloc,
game callback JKR opt-in, explicit heap selection, host override, exception
restoration, cross-thread isolation, audio scope nesting, and all six new forms
tested. Negative control removes16-byte floor and is rejected at compile time.
Adapter43-header audit PASS; git diff --check PASS. These are host fixtures.
CI adds Apple scalar emulation RUN plus xcrun iphoneos ARM64 C++14 syntax/static
assertion check before full game compile, catching the missed target ABI.
No local Apple SDK: actual target check/compile/link/IPA/phone retest pending.

Important source: JKRHeap.cpp; pc_host_alloc.h; dolphin_stubs/p2_os_host.cpp;
audio/jaudio_sink.cpp andjaudio_host.cpp; tests/pikmin2_native_allocator_test.py;
.github/workflows/ios-native-experimental.yml. New files contain no device IDs,
raw crash logs, credentials, assets or personal data. Raw reports remain local
in work/p2-phone-crashes and folder2/private phone report archive.

Build23 run39369282124/source609a45b1 remains compile/link/IPA SUCCESS but phone
startup FAILED. Its IPA is not a proven working app. Next P2-only build validates
this related allocation batch; no new candidate IPA or runtime evidence yet.
After success inspect new binary for16-byte w2 alignment and new UUID, prepare
verified IPA in folder1, update existing P2 with same signing identity/data,
test title/menu first. If failure, retrieve fresh matching report and diagnose
new exception/stack. Do not re-copy assets/art or touch P1 without evidence.
P1 remains existing working Build16,60FPS target; optional packs on hold; no
mid-day recovery save; online with Raye LAST. Stop idle waiting for Actions.

## Audio allocator batch dispatched - 2026-10-20 00:46 EDT

Build24: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39371370836
Exact source commit: 05e33f1c0e55dc11ecb6d413a8393bf73faeb2ce
Status at dispatch: in_progress. P2-only; P1 not scheduled. Host checks
native1354/console1280/Apple-scalar1354 pass; old8-byte-policy negative control
rejected. Real iPhone-target CI check/full compilation/IPA/runtime pending.
No idle polling. Record build result when user reports completion. Journal-only
dispatch checkpoint uses [skip ci] to avoid another build.

## Build24 P2 allocation/audio candidate SUCCESS; phone test ready - 2026-10-20 01:03 EDT

Run39371370836, job118459762543, exact source05e33f1c0e55dc11ecb6d413a8393bf73faeb2ce.
P2-only. Apple host tests, native/console/Apple-scalar allocator variants, and
the new actual iphoneos ARM64 C++14 compile/static-assert check all passed.
Full P2 iPhoneOS ARM64 compilation/link and unsigned IPA packaging succeeded.
Artifact12242386661, archive7585567bytes; compiler/linker index0 recognized errors.

IPA3824677bytes, executable11065224bytes. Verified ZIP CRC, exact P2 identity,
ARM64 Mach-O, iPhoneOS device platform, minimumOS15, load-command boundaries,
system dynamic-library paths, intentionally unsigned status, no disc assets.
SHA256 bacf33944221573fc1917de1311b5ddc328ce93b29977920f2ed7514259d9153
New executable UUID 21d95a32-9dfb-3bbb-bab8-4dd36cbc37d8
Inspected actual symbol/function instructions: ordinary new(__Znwm) and new[]
(__Znam) both pass16 in w2 to the JKR allocator. Build23 passed8 and Build22
passed4. This validates the actual target alignment correction in the produced
binary, independently of the host test. New phone crash must match new UUID;
old Build23 AudioQueue report is not evidence of this binary's failure.

Copied and hash-verified to Documents/Open Nectar/1 - Install on iPhone/
Pikmin 2 - Build 24 - Audio Startup Fix.ipa. Short START HERE/WHAT TO TEST guides updated.
Old Build23 P2 IPA/verification moved within the same project folder to folder5/
Build 23 - P2 Audio Startup Crash Reference, with unchanged SHA256. P1 untouched.

New candidate installation and startup/audio/gameplay remain UNVERIFIED.
User should update existing P2 through Sideloadly with the same identity,
preserving its data/assets/art; no asset recopy or P1 change. First test is
staying open/title/menu; then basic graphics/audio/touch/gameplay. If failure,
retrieve fresh report and confirm new UUID/exception/stack before another fix.
No phone app/file/settings operations were performed in build-result handling.
No active build or new source changes; journal checkpoint [skip ci], no extra CI.

## P2 menu clarity and original options input candidate - 2026-10-20 08:33 EDT

User resumed after shutdown. Verified origin/ios-experimental, fetched remote,
HEAD00bd0db831ce09d37c3da94e00ec5596e2256563, no divergence; only two paused
journal edits were pending and preserved. User confirms Build24 P2 OPENS on phone
and reaches menus. Main/title taps and Throw/A work. Two reported bugs: blurry,
small advanced menu; original game Options/exit-confirmation responds only to
bottom-left Back/X. Gameplay/audio/full-game stability not established by this.

Read the actual working P1 source and adapted its UI paths in P2 only:
- iPhone SDL high-DPI window flag, native-pixel menu targets independent of
  saved gameplay resolution/scale, frame-latched aspect at allocation/present.
- Keep the old logical-point gameplay pixel budget after enabling Retina;
  do not silently multiply gameplay GPU cost by3x in each dimension.
- Mobile400-high aspect-adapted menu with the same conservative iPhone margins
  as working P1; enable matching viewport/scissor and P2 DGX shim virtual sizes
  on iOS, including inverse taps. Captain-select4:3 exception remains.
- New read-only settings-open query; active game-menu touch lease also selects
  native UI rendering so original options/title/confirmation can be sharp.
  First/last transition follows the per-frame latch, not a mid-present switch.
  Font sampling remains existing linear; no texture/font replacement installed.

Original TOption had no direct touch handling. Added pane-based row selection,
explicit rumble/sound/volume/deflicker value taps through its original state,
animation/sound/saveRam handlers, virtual-stick navigation and visible familiar
Throw/A confirm. The disabled backing options never consume a modal's tap.
First Save row tap selects; second/explicit A confirms. No automatic save or
save/discard changes. JP/PAL-only hidden row0 remains unavailable in USA touch.
Confirmation already had select-then-confirm touch handling; retained that
behavior, exposed a context-only confirm control and let hit testing also use
visible row-container bounds when callback-owned text is hidden/replaced.
The row-container fallback is a source-supported candidate, not proven as the
sole cause on hardware. Expired/hidden tracked panes remain non-clickable.
Right-thumb camera gesture creation is suppressed only in these explicitly
claimed confirm menus so a slightly moving tap is not stolen by gameplay drag.
Other main-screen/gameplay button bindings remain unchanged; P1 source untouched.

Files: P2pc_window.cpp,gl/pc_gfx.cpp,settings/pc_settings.cpp/.h,touch/pc_touch.cpp/.h;
ebiScreenOption.cpp,ogMenuMgr.cpp,ogObjSMenuPauseVs.cpp; new
 tests/pikmin2_ios_menus_test.py; experimental workflow; both journals.
Build24 allocator/host-thread ownership and UIKit FBO/RBO corrections preserved.
No phone operations, signing/credential changes, assets or optional mods installed.

Local MSVC C++14 /W4 /WX actual-code fixtures: iPhone172 PASS; desktop182 PASS.
Covers native UI pixel budget vs gameplay, explicit aspect/resolution overrides,
frame latch/open-close transitions, layout and inverse taps across landscape/
portrait/fallback dimensions, confirm control lease expiration, direct option
selection/value ranges, disabled backing-menu ownership, row fallback, choice
select vs confirm, physical A/B and stale pane rejection. Host rendering/math
and state simulation only: not actual iPhone graphics/gesture verification.
Existing native allocator1354 and console1280 checks re-run PASS; adapter43 PASS.
Whitespace check PASS. CI adds iPhone/desktop host fixtures and actual iphoneos
ARM64 compile/static validation before full game compile. Apple full compile,
IPA and visual/touch hardware results for this candidate remain pending.

Next one coordinated P2-only build after committing; no P1 rebuild. Record exact
source/run; stop idle polling. On success verify IPA/identity/new UUID/alignment,
copy to folder1 and update test guide. Reinstall/update P2 only preserving data;
no asset/art recopy. Phone tests: menu readability/tabs/scroll/tap alignment,
original options rows/values/save, Continue/Don't Save selection and confirm,
Back, main-title controls, startup/gameplay/audio/camera regression. Preserve
Build24 known-opening IPA in archive. No new visual/touch fix may be called
confirmed until user reports actual phone behavior.

## P2 menu candidate dispatched - 2026-10-20 08:34 EDT

Source commit 3013d4c23035db25ba17851fe65cd2e29123830d
Build25: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39423349538
Status at dispatch: in_progress. P2 only. New Apple target/full compilation,
IPA, menu clarity and original-options touch on phone remain pending.
Local UI172/desktop182/allocator1354/console1280/adapter43 checks passed.
No idle Actions polling. Dispatch journal checkpoint [skip ci], no extra build.

## Build25 early fixture failure corrected - 2026-10-20 08:42 EDT

Build25 run39423349538, source3013d4c23035db25ba17851fe65cd2e29123830d,
job118629595502 FAILED in the new native menu test before game configure/compile.
Full job log retrieved directly: work/build25-job.log in the development session;
friendly copy: Documents/Open Nectar/2 - Progress and ChatGPT Handoff/Build 25 - Full Failed Job Log.txt.
Unique diagnostics: Clang unused-const-variable for kF1TabH, kF1OptH,
kF1OptVisible, promoted to errors by -Werror. These were imported real source
constants unused by the extracted fixture, although used by the full game.
Existing adapter/Apple library, native+console+Apple-scalar allocator, ARM64
allocator syntax and GD TLS checks PASSED. No game compile/link or IPA occurred.
This failure is not evidence of a new phone crash or a failure of menu visuals.

Correction limited to tests/pikmin2_ios_menus_test.py: meaningful geometry checks
exercise the imported metrics, checking tab/list separation and room for the
option rows in each tested layout. No warning suppressions or weakened CI.
MSVC C++14 /W4 /WX: iPhone180 and desktop190 PASS. Installed LLVM19 Clang parser
(clang-tidy with clang-diagnostic-* and warnings-as-errors) reproduced ALL THREE
original diagnostics before correction, then accepted both corrected variants.
Clang parser on Windows is not the Apple SDK/full iOS game build. The new Apple
CI/full compile and phone menu tests remain required. git diff --check passed.
No further game source, P1 app/data, startup allocator, framebuffer, assets or
signing changes. Build25 menu/source candidate remains3013d4c2, now with this
fixture correction for one P2-only retry. Do not install/retest Build24 for this
new candidate; retain its known-opening IPA until a new IPA succeeds.

P2 underlying menu findings remain: missing iOS high-DPI/native-resolution menu
path and Android-only mobile layout/shim versus working P1; original TOption
missing direct touch and game-menu confirm control not exposed. Visible row
fallback addresses potentially hidden callback text. Main/title taps and Throw/A
worked in user tests. The source candidate is implemented, NOT phone verified.

Next: commit corrected fixture and this checkpoint, push one P2-only build,
record source/run, stop idle polling. On success validate IPA and put it in
folder1 with short phone checklist. Reinstall P2 only preserving app data; no
asset/art recopy. Test clear advanced settings and tap alignment, original
options values/save, Continue/Don't Save select/confirm, A/Back, then gameplay,
audio/camera regression. Preserve P1. User involvement: none until IPA ready.

## Corrected P2 menu fixture retry dispatched - 2026-10-20 08:43 EDT

Build26, run39424440094, sourcedd5bd01557ea7f57255f869d431cd81864bca567.
https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39424440094
Status at dispatch: in_progress. P2 only, no new P1 build.
Includes menu source3013d4c2 plus the Build25 unused-constant fixture correction.
Local MSVC iPhone180/desktop190 and Clang parser both variants PASS.
Apple/full-game compilation, new IPA and phone menu behavior remain pending.
Build25 failed early test, no IPA. Build24 remains the known-opening phone build.
No idle polling; user will report completion. Dispatch documentation uses [skip ci].

## Build26 PASSED; P2 menu test IPA ready - 2026-10-20 09:19 EDT

P2-only source dd5bd01557ea7f57255f869d431cd81864bca567; run39424440094;
job118633289923; artifact12266336380. All job steps passed, including native
menu180/desktop190 host checks, actual iPhone ARM64 syntax check, existing
allocator/address/TLS checks, full game configure/compile/link and IPA packaging.
Build25's three unused fixture constant diagnostics corrected; no warnings disabled.

Downloaded artifact ZIP digest verified against GitHub metadata:
555eb99487ec310e9c9ffb795ade822fca5f9bea5f36c521653347922aa6aaac.
IPA ZIP integrity, single P2 bundle identity, ARM64 iPhoneOS device executable,
minimum iOS15, system-library load commands and unsigned state verified.
Fresh UUID0bd204c6-8a62-35ed-82e6-4ef2cfc76b14, executable11065512bytes.
Actual new/new[] ARM64 routines both still request16-byte alignment.
IPA3826605bytes SHA256ca28fbc6f423745e2babb595d1b47fac4a1222917b00c0ea61f24d23ad0325e5.
No proprietary ISO/RVZ/model/archive game assets embedded in IPA.
Copied with matching hash to Documents/Open Nectar/1 - Install on iPhone/
Pikmin 2 - Build 26 - Clear Menus and Touch.ipa, alongside verification JSON,
updated START HERE/WHAT TO TEST guide and build link. Build24 preserved.
Full successful job log in friendly folder2; full reports refreshed.

Milestones: source implemented YES; local checks YES; Apple compilation YES;
IPA YES; Build26 phone installation/runtime/menu clarity/touch verification NO.
Build24 remains last hardware-confirmed opening build. No phone operations,
P1 changes, assets/art recopy, signing changes or new build. Docs commit skip-ci.
Next user test: update existing P2 in Sideloadly with same account/ID, do not
uninstall. Check advanced clarity/tabs/scroll/tap mapping; original options
rows/values/Save; Continue/Don't Save select then confirm, visible A and Back;
then title/gameplay/audio/camera regression. No need to connect phone to Codex
unless a fresh crash report is needed. Do not call new menu bugs fixed until
actual user feedback. Wait for phone results without idle usage.

## Build26 hardware regressions and coordinated P2 fix - 2026-10-20 09:37 EDT

User Build26 phone test: title initially blurred with gameplay controls;
then sharpens and shows only Back/X, blocking advanced settings gear. Begin
campaign intermittent; third attempt entered gameplay. Pressing top-left pause
crashed. Ignore logo/flower layout differences in screenshots (opening animation).

Both fresh crashes match Build26 UUID0bd204c6-8a62-35ed-82e6-4ef2cfc76b14.
09:22:04 main thread: SIGABRT in AppleMetalGLRenderer clearBuffers -> pc_gfx_clear_depth
 -> pc_p2_captain_preview_begin -> pc_captain_select_draw_3d -> VIWaitForRetrace.
09:24:55 Metal CompletionQueueDispatch: SIGABRT OSPanic -> JKRExpHeap::joinTwoBlocks
 -> do_free -> operator delete -> AGX ResourceGroupUsage/command-buffer dealloc.
Confirms native Metal destruction reached the game heap. Likely source: missing
host routing during native graphics allocations; specific allocation site for
completion failure cannot be proven from its free-only crash stack alone.
Depth clear and numerous GL calls were unguarded; P2 VIWaitForRetrace also called
SDL_GL_SwapWindow outside pc_gfx_present's host guard. Existing native worker
thread defaults and16-byte alignment did not cover native calls on game thread.
09:20 Jetsam report contained no P2 process; no evidence it explains these crashes.
Phone settings read-only: renderScale=.666667, logical932x430, fpsMode0.
Raw reports/config are private local evidence, not committed to public repository.

Controls: title claimed touch only in interactive Wait; once it did, the menu
filter admitted Back plus help-requested buttons and explicit confirm contexts.
Title has no help icons, so gear/A disappeared at the same point native menus
became sharp. Small right-half taps could become camera gestures in generic
menus, cancelling clicks. Source supports this explanation; runtime fixes pending.

P2-only batch: restoring host-allocation scope at the beginning of all100
parsed direct-GL functions in pc_gfx.cpp (86 entries added/moved; two old inline
scope implementations unified). Includes clear depth, copy/held-frame/texture
upload/state/present helpers. Native SDL window init/swap/interval/shutdown and
narrow event-pump helper guarded. P2 VIWaitForRetrace's independent swap block
host-scoped. Preserve16-byte allocator policy, game-thread ownership, UIKit
FBO/RBO and native menu/point-budget frame latch. No JKR heap bypass for game
objects, no history rewrite, no P1 changes.

Menu filter retains Back, gear/settings and A for any active game-menu lease;
other gameplay controls still require visible context/help. Existing exclusive
modal input guards still block advanced-menu opening over their ownership.
No gameplay camera gesture begins while ANY game menu owns touch; existing
menu swipe/port scroll handlers retained. Title claims menu in OpenScreen and
Draw, not just Wait, to avoid delayed animated-title resolution/control switch.
One frame of render-context transition can still occur; no zero-flicker hardware claim.

Tests: new direct-GL scope audit (100 entries) integrated into existing allocator
fixture generation; negative control removing clear-depth guard rejected.
Actual clear-depth implementation exercised with lazy native allocations and
completion-thread frees, including nested scope restoration; native1359 and
console1280 MSVC checks PASS. Menu188/iPhone,198/desktop PASS including actual
button hitboxes for gear/A after generic menu ownership. Clang19 parser checks
for both menus and native/console/Apple-scalar allocator PASS. Includes static
checks for native SDL entry scopes, independent VI swap, title opening/drawing.
These are host mocks/parsing, not Apple graphics execution. Apple ARM64 target
compile, full game build/new IPA, phone regressions remain pending.

Candidate:not committed; not dispatched

No idle polling. Next action after successful IPA: update P2 only, preserve data,
repeat Begin selection several times, check gear/A before/during/after title
opening, advanced/original options, enter gameplay then pause/resume repeatedly.
If crash, read fresh UUID-matched report. P1 and assets/art unchanged.

## Build26 hardware regressions and coordinated P2 fix - 2026-10-20 09:38 EDT

User Build26 phone test: title initially blurred with gameplay controls;
then sharpens and shows only Back/X, blocking advanced settings gear. Begin
campaign intermittent; third attempt entered gameplay. Pressing top-left pause
crashed. Ignore logo/flower layout differences in screenshots (opening animation).

Both fresh crashes match Build26 UUID0bd204c6-8a62-35ed-82e6-4ef2cfc76b14.
09:22:04 main thread: SIGABRT in AppleMetalGLRenderer clearBuffers -> pc_gfx_clear_depth
 -> pc_p2_captain_preview_begin -> pc_captain_select_draw_3d -> VIWaitForRetrace.
09:24:55 Metal CompletionQueueDispatch: SIGABRT OSPanic -> JKRExpHeap::joinTwoBlocks
 -> do_free -> operator delete -> AGX ResourceGroupUsage/command-buffer dealloc.
Confirms native Metal destruction reached the game heap. Likely source: missing
host routing during native graphics allocations; specific allocation site for
completion failure cannot be proven from its free-only crash stack alone.
Depth clear and numerous GL calls were unguarded; P2 VIWaitForRetrace also called
SDL_GL_SwapWindow outside pc_gfx_present's host guard. Existing native worker
thread defaults and16-byte alignment did not cover native calls on game thread.
09:20 Jetsam report contained no P2 process; no evidence it explains these crashes.
Phone settings read-only: renderScale=.666667, logical932x430, fpsMode0.
Raw reports/config are private local evidence, not committed to public repository.

Controls: title claimed touch only in interactive Wait; once it did, the menu
filter admitted Back plus help-requested buttons and explicit confirm contexts.
Title has no help icons, so gear/A disappeared at the same point native menus
became sharp. Small right-half taps could become camera gestures in generic
menus, cancelling clicks. Source supports this explanation; runtime fixes pending.

P2-only batch: restoring host-allocation scope at the beginning of all100
parsed direct-GL functions in pc_gfx.cpp (86 entries added/moved; two old inline
scope implementations unified). Includes clear depth, copy/held-frame/texture
upload/state/present helpers. Native SDL window init/swap/interval/shutdown and
narrow event-pump helper guarded. P2 VIWaitForRetrace's independent swap block
host-scoped. Preserve16-byte allocator policy, game-thread ownership, UIKit
FBO/RBO and native menu/point-budget frame latch. No JKR heap bypass for game
objects, no history rewrite, no P1 changes.

Menu filter retains Back, gear/settings and A for any active game-menu lease;
other gameplay controls still require visible context/help. Existing exclusive
modal input guards still block advanced-menu opening over their ownership.
No gameplay camera gesture begins while ANY game menu owns touch; existing
menu swipe/port scroll handlers retained. Title claims menu in OpenScreen and
Draw, not just Wait, to avoid delayed animated-title resolution/control switch.
One frame of render-context transition can still occur; no zero-flicker hardware claim.

Tests: new direct-GL scope audit (100 entries) integrated into existing allocator
fixture generation; negative control removing clear-depth guard rejected.
Actual clear-depth implementation exercised with lazy native allocations and
completion-thread frees, including nested scope restoration; native1359 and
console1280 MSVC checks PASS. Menu188/iPhone,198/desktop PASS including actual
button hitboxes for gear/A after generic menu ownership. Clang19 parser checks
for both menus and native/console/Apple-scalar allocator PASS. Includes static
checks for native SDL entry scopes, independent VI swap, title opening/drawing.
These are host mocks/parsing, not Apple graphics execution. Apple ARM64 target
compile, full game build/new IPA, phone regressions remain pending.

Candidate:8d77c5337863f34800bc7b7ef990878e586d7c48; Build27/run39432157516 (in_progress at dispatch)
https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39432157516
No idle polling. Next action after successful IPA: update P2 only, preserve data,
repeat Begin selection several times, check gear/A before/during/after title
opening, advanced/original options, enter gameplay then pause/resume repeatedly.
If crash, read fresh UUID-matched report. P1 and assets/art unchanged.

## P1 optional character/model bundle INSTALLED by USB - 2026-10-20 09:52 EDT

User explicitly authorized installation; ZIP already present in P1 Documents.
Verified no running P1 process before backup, staging and promotion and after
installation. Phone ZIP SHA2567fa0bacc8f99349b0fd84d8b2a43716e91e68d033ca989c96a414a72dfc1538c,
matching prepared local bundle. ZIP integrity/path/type/size/model magic checked.
Backed up6 existing files/161965bytes: saves/card0+card1, config, original enhanced
config backup, touch layout and achievements. Existing Load Models folder empty;
no prior model files overwritten. Backup SHA256 validated locally and against
phone readback before changes. Full backup/private install manifest in:
C:\Users\chazz\Documents\Open Nectar\5 - Archives\Before P1 Character Packs - 2026-10-20 095114

Staged20 files/18360060bytes outside active Load, verified each SHA256, then
renamed only into absent destinations. No differing existing file overwritten.
Final readback SHA256 of all20 installed files PASS. All6 pre-existing protected
files remained byte-for-byte unchanged; P1 kept closed throughout. Original ZIP
preserved on phone. Recovery record retained in P1 Documents. No P2 writes,
reinstall, app signing, code or settings changes.

Content installed:15 NHM files comprising11 menu-counted HD models plus4 extra
captain choices,4 portraits and1 private source archive for existing character
recognition. HD Olimar, standard/HD Louie alternatives; red/yellow/blue Pikmin
and leaf/bud/flower; Bulborb/Dwarf Bulborb; President/White/Purple/Bulbmin extra
captains. Native loader expected11/11 counter. Read config hdModelsDisabled=0
(all model rows enabled). Do not confuse file-install verification with runtime
visual/animation/performance verification: game not launched by Codex.
Environment HD texture pack remains NOT installed (last official quota block).
P1 installed app/build and60FPS preference preserved. P2 Build27 still pending
at last dispatch; no polling/new build for this content milestone.

Next user action: reopen P1, Graphics > HD Models should show11/11, inspect
Olimar/Pikmin/Bulborbs and extra captain selector, play15-20 minutes while
watching FPS/Heat/RAM. Keep60FPS. If artifacts or slowdowns, disable affected
model rows, restart and report exact model/symptom; original game assets remain.
No further file copy or ZIP import needed. Full private record in folder2/
Pikmin 1 - Character Pack Installation.json; backup under folder5 above.

## Build27 PASSED; verified P2 crash/menu candidate IPA ready - 2026-10-20 09:57 EDT

Source8d77c5337863f34800bc7b7ef990878e586d7c48; run39432157516;
job118659675153; artifact12268693334. P2 only. All workflow steps PASS,
including100 direct-GL scope audit, native1359/console1280/Apple-scalar1359,
menu188/desktop198, actual iPhone ARM64 syntax checks, existing addresses/TLS
checks, full game compile/link and IPA packaging. No new source modifications.

Downloaded artifact ZIP digest matches GitHub metadata:
cc60012d8279edf3049dc17cddf83bb8fc7829ec8958dbc73c974a8e87020bdf.
IPA ZIP/ARM64/iPhoneOS device/min iOS15/P2 bundle/system-library loads/unsigned
state verified. Fresh UUIDaecbcead-f044-3dc2-9608-83e40dcd9540; executable11083680bytes.
Actual ARM64 new/new[] still request16-byte alignment. IPA3831561bytes,
SHA256f4a90d7da9f3b6130116caaf006b220f27b7e3a4ec17deb97b404222e0ab6b74. No ISO/RVZ/SZS/BMD game payload in IPA.
Hash-identical copy now in Documents/Open Nectar/1 - Install on iPhone/
Pikmin 2 - Build 27 - Crash and Menu Controls Fix.ipa. Verification JSON, build shortcut and simple START HERE guide
updated; folder2 full successful log and master handoff updated.

The batch targets Build26's actual phone failures: clear-depth captain-preview
abort and Metal completion-thread JKRExpHeap abort; title menu gear/A hidden
when touch ownership started, right-side menu taps lost as camera gestures.
Source fixes and tests passed; Build27 PHONE INSTALLATION/CRASH-FREEDOM/MENU
BEHAVIOR ARE NOT YET VERIFIED. Preserve Build24 allocator/thread/audio fixes,
UIKit display FBO/RBO, logical-point gameplay rendering budget and frame latch.

Next phone test: update P2 over existing app using same Sideloadly signing
account/ID; no uninstall or assets/art recopy. Check gear/A during/after title
animation, advanced settings; repeat Begin/captain selection; enter actual game
and repeat pause/resume; original Options/choice confirmation; audio/camera.
If crash, match fresh report to new UUID above. No idle polling/new build.
P1 unchanged in this result turn; its character bundle was actually installed
previously (20files/15NHM readback verified,6 protected saves/settings unchanged),
expected menu11/11; model visuals/performance still untested, environment textures
NOT installed. Keep60FPS. All private assets/backups remain outside Git.

## P2 enhancement batch locally verified - 2026-10-20 13:41 EDT

User resumed after the usage pause; no external source changes were reported.
Fetched local/remote baseline aa59864e3be6c8a6e5d9a7b4ca130861ed861e27 matches.
Build27/run39432157516/source8d77c5337863f34800bc7b7ef990878e586d7c48 passed;
user now reports P2 working so far with no crashes, with incomplete testing.
This supersedes earlier blanket Build27 phone-result-pending notes. It is not
proof of full campaign stability or of the new enhancements below.

P2 candidate:
- One-time backed-up/atomic config profile: renderScale1.0, FXAA, anisotropy4,
  subtle bloom; 60FPS; performance HUD initially on; hold-to-pluck, better
  pathfinding, idle counter, instant whistle, quick grab, no-trip, B throw
  cancellation, manual lock-on and charge. Existing active texture selection,
  saves, touch layout and unrelated settings survive. The profile marker is
  serialized; later menu choices survive restarts. Reset preserves that marker
  while resetting actual settings, so the preset does not silently reapply.
- chainActions and throwWhileMoving are also compatible profile keys, but the
  active P2 decomp does not consume these two getters. P2 already invokes nearby
  AI work on completion and calls control during throw states; no new AI hooks
  were added. Do not advertise either key as a newly implemented P2 mechanic.
- Performance HUD in Display: render submissions FPS, average/p95/p99 frame
  times, process RAM, advisory available memory, process CPU (100%=one core),
  categorical thermal state and Low Power. It measures actual SDL swaps,
  samples OS counters once/second, and skips sampling when disabled. It hides
  during advanced settings/captain selection. No GPU percentage or temperature.
- Native Files ZIP picker for P2 texture packs. Reuses the existing bounded,
  CRC-checked P1 extractor and staged transactional install/rollback code.
  CMake removes the old P2 converter source to prevent duplicate symbols.
  UIKit callbacks/bridge/worker have restoring native allocation scopes; the
  P2 game allocator and recent GL100/SDL/thread/audio protections remain intact.
  P1-specific model kinds are rejected for P2. P1 game source not changed;
  shared picker changes are gated, with P1 regression coverage.
- Workflow adds P2 profile/HUD/bridge/ZIP/rollback and actual CMake-wiring/reset
  checks before compiling. Only P2 will build via [ios-p2-only].

Source files: ios/pikmin2_ios_profile.h; ios/ios_storage.mm (P2 atomic config);
ios/CMakeLists.txt (P2 features and shared portable sources); ios/ios_mod_picker.mm;
ios/pc_ios_mod_bridge.cpp; games/pikmin2/pc_port/settings/pc_settings.cpp/.h;
games/pikmin2/pc_port/dolphin_stubs/p2_os_host.cpp. New tests: pikmin2_ios_profile_test.cpp,
pikmin2_ios_mod_bridge_test.cpp, pikmin2_ios_enhancements_test.py.

Local checks PASS: profile188; shared HUD30 with P2 includes; P2 bridge24;
P1 bridge19 and profile169; transactional install/backup/active-pack protection/
invalid data/rollback; real ZIP stored/deflate/CRC/paths/duplicate/failure tests;
actual reset execution; actual extracted CMake feature branches configure for
P1 and P2. Existing actual allocator native1359/console1280/Apple-scalar1359;
GL audit100; iOS menu188/desktop198; Clang parser for allocator three variants,
menu two variants, new profile/bridge/reset all passed. Local Windows compiler
checks do not compile UIKit or establish Apple ARM64 linking/runtime behavior.

P1 content update: user installed texture ZIP and screenshot lists GPI Inactive,
Loader off. Advised select GPI/A to activate, accept restart/full restart.
Activation/texture replacements/FPS/heat after activation not yet confirmed.
Previously installed character bundle:20 files/15NHM/4portraits/source archive,
readback SHA256 verified;6 preexisting save/settings/layout/achievement files
unchanged; backup in folder5/Before P1 Character Packs -2026-10-20 095114.
Model visual correctness remains unverified. P1 gameplay/menu/camera/audio
remain user-confirmed; no P1 app/data operations in this enhancement turn.
P1 texture ZIP SHA256 5d9254b4f1ca46fee93b57ce17e888521884634bc1fae4bc7a4cf22af7e2551b;
previous no-threat Defender plus full ZIP/PNG structural check is not a runtime
or absolute security guarantee. Keep60FPS; 120 canceled; online co-op remains last.

P2 needs its own compatible texture pack (upstream launcher Drive ID
1blzsLSFBr617h-gP7lvp_7HqsLRyQWzl, advertised1072944206bytes, folderGPV).
No P2 HD texture/model content downloaded or installed in this batch; importer
support and graphics defaults are separate from content installation. P1 GPI
pack/models cannot be treated as installed P2 content. No automatic phone changes.

NEXT: commit/push this coordinated P2-only candidate; record exact source/run;
stop idle polling per user. Once user reports completion, retrieve job/logs,
verify IPA ZIP/plist/ARM64/UUID/alignment/digest and copy to friendly folder1.
Retain Build27 working backup. Update existing P2 via same signing identity/ID;
do not uninstall or touch P1. Hardware test: title gear/A; repeat Begin and
captain selection; pause/resume; original Options; HUD toggle and 60FPS; 15-20min
FPS/frame/RAM/heat test. Then separately choose/import/enable a P2-specific pack,
restart and inspect replacements/counters. Retrieve matching fresh crash report
read-only if regression. No new source fix is claimed hardware-verified yet.

## Build 28 P2 enhancements dispatched - 2026-10-20 13:42 EDT

Source commit: 386771cabe6366b0788091f4d6d63f9ef6850c67
Run: 39468391460 / Build 28
URL: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39468391460
Observed status at dispatch: in_progress; conclusion/IPA pending.
Only P2 selected via [ios-p2-only]. Source and local tests summarized in the
preceding enhancement entry. No P1 app/data changes, no P2 content installation.
Local source push succeeded; source includes both game journals. This dispatch
checkpoint uses [skip ci] and does not start another build. Stop idle GitHub
polling per user; user will report completion. On return fetch/inspect this
exact run before new code edits, retrieve full logs/artifact, verify and stage
IPA only after success. Do not claim this candidate hardware-verified.

## Build28 failure reviewed; texture-import API correction verified - 2026-10-20 13:59 EDT

Build28/run39468391460/job118785702425/source386771cabe6366b0788091f4d6d63f9ef6850c67
FAILED in full native game compilation. Adapter, Apple allocator/TLS/addresses,
menu/input, enhancement profile/HUD/bridge/ZIP/rollback/CMake/reset preflights,
and real iPhoneOS configuration all passed. Packaging skipped; no IPA produced.
Full job log retrieved, full artifact ZIP digest/CRC verified. Artifact12286432727
contains only ios-build.log and ios-build-errors.md. Error index and full log
show exactly2 compiler diagnostics, one root cause, in settings line2900:
undeclared pc_texpack_active_pack; secondary incompatible vector/string operand
from Clang's suggested correction. No linker stage was reached, so successful
linking is still unverified.

This was an incorrect API name introduced in the new P2 iOS texture-import menu.
P2 already provides const std::string& pc_texpack_selected_pack(void). Replace
only that call with pc_texpack_selected_pack().c_str(); keep runtime enabled-state
check and '*' protection when all packs are indexed. Use the renderer's selection,
not sConfig/sPending, because menu changes do not rebuild the live index until
restart. P1 game/app/data and P2 Build27 working baseline are unchanged.

Added real boundary regression to tests/pikmin2_ios_enhancements_test.py. It
extracts actual texturePacksRowAction plus actual renderer enabled/selection
getters, compiles against real P2 texture-pack and iOS bridge headers, and tests
19 cases: disabled runtime; named pack; pending/config changes since startup;
all-indexed mode; busy/reentry; bridge refusal; activate/deactivate/save/restart
semantics. Only graphics SDK declarations are bypassed in the portable fixture.
Local MSVC strict compile/execution and Clang strict parser PASS. Negative
control recreating Build28's exact call fails as intended. Actual CMake P1/P2
feature wiring also reconfigured successfully. The previous broad candidate
preflights just passed on Apple in Build28; no unrelated changes were added.
Experimental P2 preflight now executes this boundary fixture before full build.

Next: commit/push correction+test+journals as one P2-only retry, record actual new
run/source, stop idle polling. No new IPA/phone fix claimed until verified.
Keep60FPS and complete enhancement batch; no need to rebuild P1 or reinstall assets.
P1 user screenshot now shows60.2FPS/16.60ms,1715MiB appRAM,CPU39%onecore,HeatNominal;
user says texture pack enabled but visual change uncertain. Replacement counter
screenshot requested; activation/render replacements remain unconfirmed. No P1
phone writes. P2 HD texture/model content still not installed by this batch.

## Build29 P2 retry dispatched - 2026-10-20 14:00 EDT

Source 7f7d0783e8b42870a8b6bbb1954199fbe9ffc6bb; run 39470849443/Build 29.
URL: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39470849443
Observed in_progress at dispatch. Local correction/API-boundary19 checks,
negative control and Clang PASS; Build29 Apple result/link/IPA/runtime pending.
Build28 had2 compiler diagnostics from1 incorrect API name; no IPA. Retain the
full enhancement batch and working Build27 backup. Only P2 builds. No P1 changes
or phone operations. Stop idle polling; user reports completion. On return inspect
this exact run, full logs/artifact, and only stage verified successful IPA. Docs
checkpoint uses [skip ci]. Logs and self-contained handoff saved in folder2.

## P1 HD texture runtime confirmation - 2026-10-20 14:07 EDT

User supplied an in-game Texture Packs screenshot: GPI Active; Loader1460
textures indexed (0dds,3046png);354 replaced,455 not in pack,0 failed.
The live successful-upload counter confirms texture replacement is working,
superseding earlier activation/replacement-unconfirmed notes. The455 misses
fall back to original textures and are not load failures. The count records
successful replacement uploads, not necessarily distinct textures. Screenshot
is from actual P1 gameplay, day2. User previously reported little visible
difference on the small phone screen; visual preference/model correctness and
long-session performance remain separate. Prior screenshot60.2FPS/16.60ms,
1715MiB RAM,CPU39%of one core,HeatNominal was a snapshot, not a sustained test.
No code or phone changes needed; leave GPI enabled. P1 model file installation
was previously verified but this texture counter does not verify model visuals.
P2 Build29/run39470849443/source7f7d0783e8b42870a8b6bbb1954199fbe9ffc6bb remains
pending at last observation; not polled. Only documentation changed [skip ci].

## Build29 success; verified P2 enhancements IPA staged - 2026-10-20 14:31 EDT

User confirmed success, then API/logs/artifact independently verified.
Source7f7d0783e8b42870a8b6bbb1954199fbe9ffc6bb; run39470849443/Build29;
job118794209786; artifact12287084885. P2 only. All intended workflow steps passed,
including new19-case real import-menu/API boundary; profile188/P2bridge24/P1bridge19/
HUD30/transaction/ZIP/reset/CMake, allocator1359/1280/Apple-scalar1359, menu188/198,
actual iPhone ARM64 allocator/menu syntax, headers/addresses/TLS, full compile/link
and IPA packaging. Full logs retrieved;0 distinct compiler/linker error lines.
Artifact ZIP SHA25669b13b4db9a885c711ddd2dc08aacf59bba2974e677afcb189e45263d2a7f50e
matches GitHub metadata; ZIP CRC pass. IPA integrity/plist/P2 bundle/ARM64/iPhoneOS
min15/system-only library loads/unsigned state verified; fresh UUID
03e1bc57-bc1e-356a-a65b-6474b990b91c. Actual ARM64 new/new[] both retain16-byte alignment.
IPA3897973bytes; executable11221000bytes;
SHA256429b2f4011e82cee0d8b879bf3bfc271c93c382c1c33d461f2c8a9a7c8ce1871. No proprietary ISO/RVZ/SZS/BMD payload found.

Hash-identical verified IPA copied to Documents/Open Nectar/1 - Install on iPhone/
Pikmin 2 - Build 29 - QOL Graphics and Performance.ipa. Clear START HERE/WHAT TO TEST guides, verification JSON and build
shortcut updated. Build27 backup retained; no app installation/uninstallation,
phone file writes, asset/art recopy or P1 modifications occurred in this turn.
New Build29 PHONE INSTALLATION/60FPS/QOL/HUD/menu/import/runtime tests pending.
Separate P2 HD texture/model content not downloaded/installed; this IPA adds
preset and ZIP import support, not a content bundle. Next user updates existing
P2 using same signing account/ID, tests menu/Begin/pause, controls/audio/HUD,
then screenshot stats and sustained play. Obtain compatible GPV textures later.

Future online co-op design agreed and recorded in ios/ONLINE_COOP_DESIGN_NOTES.md
and folder2/Future Online Co-op - Agreed Design.md: together-only host campaign,
shared progress/inventory, own screen/squad/allowance; forced group area/cave
travel acceptable; health-first difficulty, selected extra encounters only after
performance/stability evidence; reconnect/pings/phone interruptions/backups and
independent graphics accepted. No online implementation begun; remains last.
P1 texture uploads already screenshot-confirmed354 replaced/0 failed; P1 untouched.
