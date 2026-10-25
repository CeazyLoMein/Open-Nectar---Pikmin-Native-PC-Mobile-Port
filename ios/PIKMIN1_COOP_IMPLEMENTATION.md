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

## Research-driven session feature checkpoint — 2026-10-24 22:43 EDT

User explicitly authorized a fully fleshed mode and useful feature implementation. Read [PIKMIN1_COOP_RESEARCH_AND_FEATURES.md](PIKMIN1_COOP_RESEARCH_AND_FEATURES.md) for primary references, decisions and full player flow. New CoopSession binds actual authenticated+compatible GatedTransport to complete actor transfer, both-loaded/ready, separate pause/background blockers,500ms heartbeat/3s timeout with old-queue safety, typed temporary partner markers and20Hz/known64KiB-backlog actor-update limits.19 core tests +Clang PASS. No game actor/lifecycle/UI/socket integration activated. Current56 remains previous b28a5d7b actor-frame native build, last seen running; NEW source is saved skip-ci and needs inclusion in next native integration check. No additional phone install now. Both ordinary phone games work; preserve54/53 and optional120.

## Exact Build56 checkpoint — 2026-10-24 America/New_York

Source pushed: b28a5d7b13037c68c76e66d730dd86fc679df59c, branch ios-experimental. Build56 run40154273299, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40154273299. Last metadata status in_progress, conclusion pending; no native result/artifact verified yet. P1-only + shared scene validation.18 local core tests, actual engine capture-to-complete-replica fixture, compile-out and Clang PASS. Both phones keep working54; no new install requested. Raye60FPS confirmed after restart. No phone needed.55 separately verified SUCCESS. Stop idle CI polling; user will report completion. Next integration is actual authenticated iOS transport/session/scene compatibility and safe guest engine actor/camera application; current data replica alone isn't online gameplay. Full world, Onion engine transactions and snapshots remain.

# P1 online co-op — active implementation

<!-- CAPTURE MILESTONE -->
## Current milestone — complete actor frames, 2026-10-24

- Both games now USER-CONFIRMED open on Raye iPhone17Pro/iOS27.0.1. P1 was imported one folder high, fixed to assets/dataDir; all3529 files reverified. Settings/save preserved. Her60FPS setting works after gameplay restart. Phone not needed now. See RAYE_IPHONE_SETUP_STATUS.md.
- Build55/run40149838089/source5bfa4fba native P1+scene SUCCESS;17 core tests and real capture fixture PASS.55 artifact12581478645 uploaded; metadata only verified this phase, no new phone update requested.
- NEW: complete captain/Pikmin actor-frame envelopes and bounded atomic guest-side DATA replica. Actual P1 pc_coop_world_capture_packets feeds it through48byte version1 NCF1 fragments.18 core tests plus actual engine-to-receiver fixture and Clang PASS. New Apple build pending; exact source/run in external Exact Resume State.json.
- Captures/ownership/IDs survive pool reuse; all fragments must arrive/validate before a replica replacement or deletion. Loss/expiry/corruption keeps last good state. Session/scene/frame/tick guards and semantic validation. FNV is NOT authentication; transport must supply authenticated host and trusted accepted scene context. No guest engine writes/network socket/session UI activated. Normal app remains inactive prototype.
- Next: real authenticated iOS transport/session/compatibility+scene integration and guest actor application/own camera, actual Onion/field-cap transactions, remaining world state, then snapshot/reconnect. No claim playable online, no new phone install for this engineering batch.
<!-- END CAPTURE MILESTONE -->




User authorization: October24,2026. P1 Build53 is accepted as the working solo baseline. Online work STARTS NOW; earlier future-only notes are historical. P2 remains a working separate game and will get its own stronger validation/adapter later. No claim every solo story path has been tested.

## Preserve and reuse

Keep the verified53 IPA, normal bundle identity, assets/settings/saves and current high native resolution/AO OFF baseline.120FPS remains selectable. Develop behind an experimental session mode with a disposable campaign; don't force a fourth free-profile app or overwrite normal campaign data. This session has not enabled that mode in the game yet.

Use host-authoritative design. Each phone renders only its own fullscreen camera/HUD; each controls one captain and squad anywhere in the current area. Host owns campaign/world/save, both contribute, play together only; no independent offline merge or initial host migration. Either may host a new campaign. Shared Onions, independent per-player field allowances including workers/idle, atomic counts. Forced group area/cave travel accepted. Difficulty mainly health, extra actors only after performance evidence. No finale/boss spoilers.

## Actual upstream reuse assessment

Upstream main a6b09bfe and release1.0.8 were checked. Main's NETPLAY.md now calls old online disabled/unmaintained. Local source already contains nectar_net transport, connection codes, authentication/join gate, compatibility, simulation clocks/input, scene barriers, stable entity IDs and captain prediction/interpolation. The game adapter emits captain records; it does NOT yet provide our authoritative full campaign/world. Existing diagnostics/desktop Linux claims are not iPhone test evidence.

Reuse those engine-free components and useful adapters. Do not simply flip PC_ONLINE_ENABLED or NECTAR_ONLINE and describe that as complete online co-op. GNS/encrypted transport's Apple dependency/linking and device reachability remain to test. Direct port mapping cannot guarantee connectivity through carrier NAT; no relay/matchmaking service/provider has been selected or deployed.

## Implemented foundation in this batch

`libs/nectar_net/include/nectar_net/onion_authority.h` and `src/onion_authority.cpp`: host-thread-only Onion stock/field ownership.3 P1/5 P2 color slots, independent allowances, atomic multi-Pikmin withdraw/store, stable scene/type ID validation, wrong-owner rejection and death accounting. A last-request cache per authenticated peer makes retry idempotent and rejects changed/stale sequence reuse. Reply.replayed explicitly tells the future engine bridge not to repeat actor-side effects for a cached acknowledgement. Only one outstanding command per player is supported by this initial sequencing policy. New session must construct fresh authority; scene transfer/reconnect ledger restore not implemented.

The adapter must supply authenticated peer identity independently of untrusted payload and verify IDs against the host's actor registry. It must preflight corresponding engine changes and commit with the ledger at the SAME safe tick; this library cannot itself spawn/store Pikmin. Working/idle/following Pikmin stay counted. IDs must be assigned/recycled with generation rules by the future registry. Seed production, sprouts, new population, ownership transfer, full snapshot codec and disk restore are next work, not already supported by this module. It is not hooked into game actors, no network messages added and no save format changed.

Tests:200→Raye20 leaves180→host30 leaves150; both can have30; duplicate delivery cannot take/return twice; wrong ownership, invalid entity/scene/type, full allowance, insufficient stock, partial-invalid requests, sequence spoof/reorder and death cases.10000 cycles/40000 deliveries conserve stock. All15 offline nectar_net test executables passed locally; no GNS real socket or phone session run. CI adds host tests plus Apple ARM64 syntax checks without enabling online in the normal game.

## Concrete next milestones

1. COMPLETE native/package milestone: Build54/run40145860255, sourcea7888f24, P1+scene SUCCESS,15 offline network tests PASS, verified IPA staged. Device behavior pending;53 rollback retained. See PIKMIN1_BUILD54_VERIFICATION.md. No full campaign/finale retest demanded.
2. Raye solo baseline: prepared folder has P153 and P252 with exact hash manifest. Raye reports iPhone17Pro/public non-beta iOS; exact version/connection later. Sign/install without uninstalling unrelated apps; import existing private assets into each correct game container; verify launch/audio/input/pause/resume.52 is compiled/packaged but not newly phone-confirmed. Nothing installed by this batch.
3. Narrow disposable same-Wi-Fi co-op vertical: compile chosen transport for iOS, simple explicit session lifecycle (host/join/leave), fixed familiar area, two captains, each phone's own camera/input. Reliable authenticated connection + version/content compatibility before commands. No original save writes. Confirm separate view with wide separation.
4. Host registry: stable epoch/kind/generation IDs, safely bind actors at spawn/despawn; snapshot only valid finite state. Bridge OnionAuthority to actual withdrawals/returns and reconcile engine global Pikmin cap before promising30each. Replicate owned squad, one job, an enemy and one carried object, with stale/duplicate/reordered packet tests. Guest world must not independently award/kill/spawn/save.
5. Expand all world actions: births, sprouts, colors/maturity, idle/work ownership, attacks/hazards/carrying attachments, loot/parts, gates/bridges/Onions, clock/RNG, pause/cutscene/day transitions and forced group travel. Keep client graphics separate. Shared progress is host campaign state, not two independently advancing files.
6. Recovery: guest disconnect pauses/retains host world; secure rejoin token and complete keyframe. Host cold restore requires versioned exact-scene snapshots, validated relationships and atomic rotating files shared with future solo autosave. Existing normal card/Gekko handle is not that. Corruption/unknown-version fallback preserves last good file.
7. Private invite code/link plus real different-network/state-away testing. Select relay fallback only once iOS transport/NAT tests show requirements; don't deploy paid services or expose credentials. Then performance/thermal and together-only campaign regression, followed by P2 actor adapter/stronger cave/audio/save matrix.

Local tooling notes: Windows CMake compiler-detection failed in a debug-PDB tool environment (C1902); direct release MSVC build of the same core sources/15 tests passed. First direct compile mistakenly included optional GNS without its SDK, then corrected to the CMake core source list. Test-only CRT deprecation macro needed for standard getenv/fopen on MSVC; no runtime source workaround. Archive object list was made explicit so test main objects are excluded. Existing scene runner needed an unrestricted temp directory. These are not native-game compile passes or new game bugs.
