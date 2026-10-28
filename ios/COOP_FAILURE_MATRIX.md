# P1 online co-op: failure and verification matrix

Updated 2026-10-28. This is an engineering checklist, not a claim that campaign co-op or all recovery is implemented. Practice uses a disposable world. Build 81 is the latest validated iOS package in this checkpoint; later source changes require a new build.

## Practice first

| Scenario | Safe desired behavior | What remains to verify or implement |
| --- | --- | --- |
| Host enters before guest, or guest first | Both see a clear waiting state without a precise simultaneous tap; proceed only once both are ready | Test both orders and long gaps with two phones |
| Either opens a system alert, Messages or another app | Freeze authority, stop accepting old input, show which player is away; resume only when both are ready | Scene observer source changed after Build 81; iPhone test required. iOS may suspend and break the connection |
| Guest has no game world, or loading fails | Keep host state safe and give a way out; no campaign save touched | Build 80 hypothesis skips practice movies; observe both screens and logs on device. Practice exit may require a restart after isolated card admission |
| Bad latency, loss or congestion | Avoid stale actions; indicate trouble, keep world consistent and do not advertise smoothness without evidence | Reliable ordered snapshots/input can queue behind loss; test adverse network and backlog. 20 snapshot updates/second can cause display stepping |
| Guest disconnects | Host world held and guest cannot issue stale input; authenticated rejoin needs a fresh full baseline | Low-level host-rejoin foundation exists, but in-game live rejoin and full baseline are not integrated |
| Host disappears | Guest must not continue a second independent world or overwrite last good save | Reliable host-loss recovery needs complete recoverable state and authority handoff; no current exact mid-day restore |
| Invite is old, copied incorrectly, leaked or host closed | Explain issue, require a new invitation when needed, avoid exposing secrets | Remembered invite is process memory, expires, and is best effort. Never promise automatic resume |
| Different versions or incompatible gameplay data | Reject before gameplay and explain what differs | Build and content identity gate exists; compatible cosmetic differences need explicit evidence |
| Denied local network permission, cellular, Wi-Fi isolation | Explain permissions or reachability without pretending everything is Wi-Fi | Same Wi-Fi only demonstrated; different-network signaling, NAT traversal, relay and failure recovery remain unproven |
| Controller/settings menu opened by either player | Pause safely, show partner's state, retain distinct personal display and controls | Device test and world integration required; compare two differently configured phones |
| One phone is much slower, hot or backgrounded | Prevent divergent progress and tell players why gameplay is held | Test device FPS/thermal and queue backlog. Never lower user settings without consent |

## Shared campaign gates

- Host is authoritative for world, day clock, pickups, enemy health/deaths, rewards, shared Onions, construction and progress; grant unique rewards once. Two captains and squads have separate ownership and per-player field allowances; concurrently requested withdrawals must not create Pikmin.
- Both see the same transitions, doors, cutscenes, day end, discoveries and outcomes; explicitly test both players at different locations and transition requests. Forced group travel is acceptable.
- Pause and permission prompts must not permit old held inputs or duplicated actions. Lost messages, duplicated actions, stale epochs and partial baselines must fail closed.
- Solo and shared slots are separate, versioned, atomically saved with backup/rollback and identity checks. A normal day checkpoint must never be labeled exact mid-day resume. Keep cosmetic, camera, controls, display and audio personal.
- Reconnection demands reauthentication, a new epoch, full consistent world baseline and ready handshake. Host-loss takeover requires a complete validated snapshot: electing a replacement alone is insufficient. Make the user-facing choices truthful until persistence exists.
- Keep full-screen independent cameras; verify cross-map play and visibility/culling separately on each device. Different phone performance does not change authoritative simulation speed.
- Test gradual difficulty changes (primarily health) with clear settings. Extra enemies require measured performance. Preserve 120 FPS option.
- Cover PC/iPhone save transfer only after save schema, compatible gameplay settings, backup and conflict rules are proven. Transfer campaign progress without cloning player/device identity, invite secrets, or personal settings; both players play together and no independent-save merge is promised. P2 follows its own stronger campaign test.

## Evidence and references

- Apple scene activation/deactivation: https://developer.apple.com/documentation/uikit/uiscene/willdeactivatenotification and https://developer.apple.com/documentation/uikit/uiscene/didactivatenotification
- Outer Wilds Quantum Space Buddies documents both shared-world mechanics and mod incompatibility: https://github.com/qsb-dev/quantum-space-buddies/blob/master/README.md ; its open issue list illustrates real client catch-up and reset failures, without proving their cause here: https://github.com/qsb-dev/quantum-space-buddies/issues
- Host election and migrating the simulation state are distinct problems: https://docs.unity.com/en-us/mps-sdk/session-host-migration
- Snapshot smoothing trades a little display delay for jitter tolerance; this does not fix missing state or change authority: https://gafferongames.com/post/snapshot_interpolation/
- Steam networking supports separate lanes and reliable/unreliable messages, but changing the existing single reliable protocol requires a complete sequencing/fragmentation redesign and tests: https://partner.steamgames.com/doc/api/ISteamnetworkingSockets

Story/cutscene synchronization, player-specific initiators, shared skip agreement, interruption/rejoin and spoiler-safe test coverage are expanded in `COOP_CUTSCENES_AND_STORY.md`.

### Additional input limitation to investigate

`PcCoopPracticeInput` currently combines repeated occurrences of the same one-shot action into a bit until the next send. Two rapid identical taps in that interval can coalesce into one event; this is a source-level limitation, not yet observed on phones. Before changing the wire format, build a bounded, revision-scoped event queue with unique event/tick identities and tests for rapid taps, duplicate delivery, retransmit, pause, stale expiration and disconnect. Do not let retransmissions double an action or revive stale commands. This is separate from the 300 ms stale-action guard.

### Separate squads and overall capacity

The existing P1 port defines `PIKI_FIELD_LIMIT_MAX` as 999 and exposes adjustable field limits, while the experimental `ActorFrameLimits` defaults to 512 total records (including captain records). `OnionAuthority` currently allows up to 1000 per player as a generic accounting bound; it does not enforce the engine's aggregate capacity, network snapshot capacity or a phone's performance. The experimental blend helper separately caps Pikmin at 510. These are source limits, not proven playable phone counts.

Before shared-Onion gameplay is enabled, reconcile per-player allowances with a host-enforced aggregate limit, every live actor's engine allocation, snapshot record/byte limits and both phones' measured performance. Do not silently share the 30-per-player allowance the user requested as an example, and do not advertise arbitrary high counts as supported. Reject or explain an unsupported configuration before changing stock, preserve transaction atomicity, and test near all boundaries with each player withdrawing simultaneously. Future full-world snapshots may need capacity for objects beyond two captains and Pikmin.
