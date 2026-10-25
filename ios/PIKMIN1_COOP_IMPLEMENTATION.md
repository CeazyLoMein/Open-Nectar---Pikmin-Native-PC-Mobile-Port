# P1 online co-op — active implementation

<!-- CAPTURE MILESTONE -->

## Current milestone — 2026-10-24 21:15 EDT

- User P154 very quick smoke test seems fine; proceed with prototype, not full campaign certification.53 remains rollback.
- HostEntityRegistry +38byte Pikmin codec and actual P1 read-only captain/squad capture/lifecycle hooks now implemented/local tested.17 offline core tests, actual engine fixture, compile-out test and Clang PASS; disabling invalidation is caught by negative control. Build55 / run40149838089, source5bfa4fba17e9083deabeddc0033bc8a4a002ce06: in_progress / pending, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40149838089
- Local addresses never serialized; scene IDs/ownership survive actor reuse/working/idle transitions. Hook clears on pool birth/kill/Creature init and before stage heap reset. Prototype option is compile-time opt-in; sessions remain runtime inactive and normal online flagsOFF. No guest actor updates/transport/UI or Onion actor transaction bridge yet.
- Raye iPhone17Pro/iOS27.0.1, DeveloperMode enabled by user. Both apps installed; ALL P13529files/34art and P22797files/28art read-back verified in their own sandboxes. Both transfers finished; phone may unplug. Post-import runtime awaiting feedback. See RAYE_IPHONE_SETUP_STATUS.md.
- Next: real iOS session/scene/transport validation and guest binding/application with own full-screen camera; then actual Onion/field-cap/actor authority. Complete keyframes must apply atomically, and buffers must outlive the scene if queued. No new phone install requested for this plumbing-only compile check.
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
