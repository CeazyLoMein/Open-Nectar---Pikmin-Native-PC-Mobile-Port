## Build58 — exact current checkpoint

Source 4f8ac1356f69fa1f47bbfab1ab411ab1ac4b2a76; run40161054040 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40161054040), last API snapshot IN_PROGRESS, conclusion pending. P1 only. Native Host/Join CONNECTION TEST UI + actual source/base-data fingerprints, private-code join/content-rejection probe, local-network permission and verified bundle notices. Local identity/packaging tests, strict C++ probe compile and39 app policy checks PASS. Apple/phone behavior PENDING.57 independently verified SUCCESS (native+scene+actual encrypted simulator/session), artifact/IPA checked; omitted notices corrected in58 source. No new phone install yet. User reports58 passed/failed; after native/package PASS, stage update in Documents and ask for a short two-phone same-Wi-Fi connection test. No idle polling; no phone needed now. No playable co-op campaign yet; P2 preserved.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** October25 session; recorded 2026-10-25T04:12:21.567672+00:00.

**Overall project status:** Build57 SUCCESS independently verified. Actual iOS27.1 simulator GNS encrypted UDP test transferred both captains/60Pikmin and exercised authentication, compatible join, ready/pause/background/marker/disconnect. New native P1 Host/Join CONNECTION TEST screen implemented and locally checked; Apple compilation/phone validation pending next P1-only run. This is not yet a playable online campaign. P2 remains preserved.

### Pikmin 1

- Current objective: First real two-phone private-room connection, before attaching authoritative game simulation/guest camera.
- What was investigated:57 run/jobs/full P1 log, exact checked artifact SHA256 and runtime JSON/log; actual IPA ARM64/header/bundle resources. Existing room lifecycle, settings action model, iOS native sheet/keyboard and CMake resource scope. Apple primary UIKit pasteboard documentation and CommonCrypto header confirmed APIs.
- Root cause or leading hypothesis:57 proved simulator socket/session foundations but had no reachable phone connection UI. Added native room screen under Advanced Settings > Data > Online Co-op: Connection Test. It creates/joins authenticated private rooms on the same Wi-Fi and compares actual tracked source/config SHA256 plus streamed installed assets/dataDir SHA256. No fixed fixture identity used in the phone screen. Runtime gameplay-option compatibility still required before later gameplay activation. Artifact inspection also found57 dependency notices omitted because source resource properties were set in the parent CMake directory; corrected target-directory scope and added exact shipped-byte verification.
- Files changed: ios/ios_coop_room.h/.mm; ios/generate_coop_build_identity.py; ios/verify_coop_bundle.py; ios/CMakeLists.txt; games/pikmin1/pc_port/settings/pc_settings.cpp; libs/nectar_net/tests/coop_socket_probe.cpp; tests/coop_build_identity_test.py; tests/coop_bundle_test.py; experimental workflow and project journals.
- Tests and results: Two identity tests PASS (real bytes/name/version changes, line-ending normalization, docs/order/duplicates, bad/empty paths). Actual current repository generation PASS over2874 tracked code/config files. Two packaging tests PASS (missing/tampered notices, missing permission, wrong app). Final real-socket/private-code probe translation unit MSVC/O2/W4/WX compile PASS.39 existing app/configure/identity/storage checks PASS. Four existing simulator runner evidence tests and26 scene contract checks PASS this session.57 had19 core tests and actual iOS socket/session runtime PASS. NEW Objective-C++ screen cannot be compiled on this Windows PC; strict iPhoneOS syntax + full native app compile are in next CI. New one-code/content-mismatch runtime probe also awaits Apple CI. No phone changes in this session.
- Confirmed working: Existing P1 solo baseline54 and prior user-tested fixes on both phones remain installed.57 device compilation and IPA generated; inspected IPA preserves normal org.opennectar.experimental.pikmin1 / Pikmin1 label and ARM64.57 not installed. Actual simulator receipt com.apple.CoreSimulator.SimRuntime.iOS-27-1/iPhoneDuo, probe binary SHA2566677a397e0f39e6e777524fdcb99692d9aa31496cbf4760de0a36e0090e35c16.
- Remaining issues: New room UI/data scan/local-network permission and real two-phone reachability unverified. Prototype cannot start co-op gameplay or mutate campaign, actor states, cards or settings. No full host world/guest engine/camera/audio/action/Onion/snapshot/reconnect integration yet. No internet relay selected. Optional120FPS and AO OFF baseline preserved; old abandoned online lockstep remains OFF.

### Pikmin 2

- Current objective: Preserve working app while P1 online work progresses.
- What was investigated: No new P2 investigation.
- Root cause or leading hypothesis: None asserted.
- Files changed: No P2 source, app identity or game configuration changes.
- Tests and results: No P2 rebuild or phone test in this batch.
- Confirmed working: Prior user-confirmed P2 works on both phones; latest working audio recovery retained.
- Remaining issues: Full story untested; later stronger solo validation and separate online adapter.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental.
- Starting commit:05f73662154862a51ace29dde9c52efb18c28838, clean and matched origin after fetch.
- Latest source commit: 4f8ac1356f69fa1f47bbfab1ab411ab1ac4b2a76; later documentation-only checkpoint records run58.
- Commits created: 4f8ac1356f69fa1f47bbfab1ab411ab1ac4b2a76 implements the room screen and coordinated safety/probe changes; later documentation checkpoint.
- Changes pushed: Complete room-screen source batch pushed to ios-experimental;58 dispatched.
- Uncommitted changes: Clean after the final documentation checkpoint; all source and journals pushed.
- GitHub Actions run IDs:57 =40158088407, source03cd0be08157613b020cb59c678271b44065a997.
- Build results:57 scene121063660172 SUCCESS; P1121065410338 SUCCESS; actual encrypted socket/session receipt PASS. New58 run40161054040/source4f8ac1356f69fa1f47bbfab1ab411ab1ac4b2a76, IN_PROGRESS; conclusion pending.
- Artifacts produced:57 P112586070653 SHA256ef4931034567bcc627bbf9665df36e69f573b1257cb47572cf45d00c28d37bbe (downloaded+verified); scene12585638397 metadata SHA256ad37dd82b575c769498efd1ab10d1527d9cbcc162cd8ce8b5b0b23f75a5754df.57 IPA inspected, not installed; missing dependency notices identified and corrected in new source. Private package receipt records that limitation accurately.

### Next steps

- Next Pikmin1 task: Validate native screen + actual one-code join/content mismatch in Apple CI. After PASS stage the resulting IPA in Documents and ask for a focused same-Wi-Fi two-phone connection test. Then implement actual accepted scene/world readiness, ownership-safe guest actors/private camera/audio and commands; keep normal campaigns separate.
- Next Pikmin2 task: Preserve existing working app.
- GitHub/build task: Commit/push one P1-only run including screen, private-room probe, identity and packaging safeguards. Record actual source/run. User reports completed; no idle polling.
- Anything requiring my involvement: Nothing on the phone now. Report the new build result after it is linked. Only after native PASS and verified package, install same P1 update on both phones and try connection screen; detailed instructions saved in Documents.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User wants autonomous meaningful development batches, not repeated next-step promises.57 proof is one-process iOS simulator socket/session, not playable two-phone co-op. Current engineering mode deliberately only creates rooms; do not present it as campaign co-op.
- Important source-file locations: New native screen in ios/ios_coop_room.mm; source fingerprint generator and new bundle verifier in ios/; Data row guarded by __IPHONEOS__ + NECTAR_IOS_COOP_ROOM. Network core remains libs/nectar_net; actual actor capture remains pc_coop_world. CMake NECTAR_IOS_COOP_TRANSPORT controls P1 only.
- Relevant logs: Private work/build57-p1-full.log, build57-run.json/jobs.json/artifacts.json, build57-p1-artifact.zip and build57-package-receipt.json. New CI keeps ios-coop-socket-results runtime receipt.
- Unverified fixes: Native room controller, installed game-data hashing and permission handling; packaged notices resource-copy correction; new actual room-code/content-rejection probe. These are implemented, local checks pass, Apple/phone proof pending.
- Risks and warnings: Connection-only mode uses its own required capability0x20000 and cannot start CoopSession/game simulation. Installed data hash is complete assets/dataDir and does not include cosmetic packs or runtime cheat/options; options must be negotiated before actual co-op gameplay. Data scan runs off the UI thread; cards/settings untouched. Clipboard copied only by explicit user tap, local-only and expires in5min. Host room is retained in memory while briefly sharing code; any active peer is dropped and reauth required. Guest connection closes on background. No automatic host continuation, relay deployment, online service account or paid purchase.
- Exact next actions: Verify next CI strict ObjC++ compilation, one-code runtime, native P1 and packaged permission/notices. Stage validated IPA and alert user for two-phone test. Host/Join in Data, same Wi-Fi, both permission allow, copy host code/send manually, return host to P1 BEFORE guest joins, both should show Connected. Leave/Done closes room; normal solo remains. After that attach full game adapter and actual world synchronization; do not unlock shared campaign from mere room Connected.

**END PROGRESS REPORT**
