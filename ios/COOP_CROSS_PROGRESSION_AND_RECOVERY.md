## Build68 phone test milestone — October25,2026 18:59 EDT

User reports "yeah all good so far, on the tests" in response to requested Build68 T05/T07/T08. Record this as overall user-reported PASS for title Online Co-op access/connection, remembered Rejoin and Done/normal game-controls-settings return. Separate per-phone timings/screenshots/repeat trials were not collected. This is limited same-Wi-Fi connection/UI testing, not shared gameplay, internet play, whole campaign completion or physical thermal validation. No new phone data writes by agent. Verified68 IPA/source54b873070d3ab331a6775e3a31aa85c8344c0ebf/run40232707062 is now the current user-accepted baseline; preserve65 and54 rollback packages, settings/packs/saves and P2. No FPS/graphics changes.

Current-code inspection: ios/ios_coop_room.mm still owns HostRoom/GuestJoin in the native screen; Done closes connection. It does not transfer an authenticated link to a running game. pc_coop_world.cpp only captures host captain/Pikmin records into complete packets; no guest engine actor creation/application. CoopSession is tested engine-free session/readiness/pause data, not a live game adapter. Old pc_online_navi.cpp has basic transforms but is under old optional netplay path and cannot by itself supply shared world or fullscreen guest control. Do NOT enable old online and call co-op complete.

Next integrated gameplay milestone: disposable familiar-area, no normal campaign writes, explicit session ownership handoff from native room to game-thread pump; authenticated start/area/epoch/ready barrier; two actual captains with host-owned movement and guest input; guest presentation from host state with its own fullscreen camera/audio/input; disconnect pauses retained host test world and stops commands; clean exit restores solo mode/settings. Loading must gate inputs and reject incompatible/missing actors rather than advancing two separate campaigns. First phone test T10 is simultaneous movement plus independent views and separation in the same area; Onion/actions/save/internet readiness must stay explicitly unavailable until implemented/verified. Add actual-source adapter/lifecycle/pause/scene tests and local impaired-network coverage, then one coordinated P1-only Apple build. Avoid a new CI run merely for this documentation result.

No additional phone action now. Phones may close P1/disconnect. Next code work is the actual session-to-engine bridge, not more connection-only phone tests. P2 remains preserved; separate shared slots, complete world replication, durable checkpoint/recovery and cross-progression remain later stages.

## Build65 TWO-PHONE SAME-WI-FI PASS — October25

User confirms BOTH65 phones installed and tests1-5 passed: connected for over a minute, delay as low as11ms (initial100+ms sometimes decreases, sometimes starts low); guest Leave keeps host room waiting; guest rejoins; reversing hosts works; Done returns to normal solo with working visuals/controls/settings. T01-T04 PASS by user observation, scoped to SAME Wi-Fi ONLY. User explicitly confirms the last different-game-data screenshot was an OLD62 failure, not a65 regression. Screenshots support Connected/88ms and waiting/closed states; private invite codes are NOT copied into public journals. No internet/separate-network, actual shared gameplay, host Messages interruption or full campaign validation claimed.

Verified current source behavior: ios_coop_room.mm backgrounded keeps HostRoom/code in memory but deliberately disconnects the active peer; foreground resumes the waiting room, provided iOS has not terminated the app. Guest background closes its link. This is a connection-only room, not retained gameplay/world persistence. There is no one-tap remembered Rejoin control yet. User requests reconnect without resending codes; next UX batch should remember the last authenticated room locally in memory, offer explicit Rejoin, revalidate/authenticate and explain expired/closed room. Full gameplay pause/wait/readiness and durable partner/campaign identity remain separate planned integration; do not claim app-kill recovery from this screen.

Next authorized work: title-menu Online Co-op access alongside existing local Co-op, clear connection-only labelling until real shared gameplay; easier Rejoin; separately labelled solo/shared save slots with no overwrite when actual campaign support is integrated. P2 preserved.

Thermal feedback: user's screenshot shows120FPS/8.33ms,CPU62%,RAM1761MiB/spare1615MiB,Heat Serious; Raye's phone user-reported less hot. Different packs/screens/devices are possible factors, not a confirmed cause. User will adjust FPS THEMSELVES. Do NOT change/cap FPS, resolution, texture/model packs or gameplay/visual quality. Latest authorization: investigate waste reduction only (hidden rendering, background/lobby work, redundant work/allocations) if it preserves visuals/gameplay. No heat test requested now and no thermal fix claimed. Graphics/120 option remain unchanged.

Both phones can disconnect; no additional build needed merely to record these results. Next source UX/efficiency batch must preserve65 as verified LAN baseline and maintain the existing backup/rollback files. Exact report/checklist/state are updated; older sections below are historical snapshots.

## Approved next UX target — title menu and separate solo/shared campaigns (October25)

User requests this AFTER the connection check is working. Add a clear Online Co-op choice directly on the title menu, alongside the existing local Co-op choice, with Host campaign / Join campaign / Back. Do not require users to find Advanced Settings > Data for ordinary online play. Keep the experimental connection checker distinguishable until real shared gameplay exists; a working connection screen must not be advertised as a playable online campaign.

Allow one personal offline solo campaign and another shared campaign with Raye in the SAME app. Existing numbered save slots are acceptable; user example Slot1 = Solo, Slot2 = Chazz and Raye. These are friendly examples, not authorization to overwrite an occupied slot or automatically convert an existing save. Use the existing slot selection/storage where practical, label mode and campaign clearly, show day/progress/host for the selected shared campaign, and make Continue use the intended campaign/mode rather than whichever slot was touched last. Creating/hosting online must select an empty or explicitly designated online campaign; joining must attach to the host's shared campaign without redirecting writes to the guest's personal solo slot.

Source check: MemoryCard::loadCurrentGame uses the selected indexed campaign; saveCurrentGame writes a selected slot block via getGameFileOffset/writeOneGameFile and existing day history is keyed by save slot. Preserve existing raw card format/slot offsets until a versioned adapter is validated. Carry durable campaign/player identity and mode separately with a verified slot association; a device-local slot number alone is not a cross-device campaign identity. New co-op metadata/checkpoints must stay associated with the correct campaign/slot, with no accidental cross-slot overwrite. Back up the whole card before changes because multiple slots may share one card file. No new save paths, migrations, menu changes or phone writes implemented by these notes.

Keep the agreed together-only shared campaign policy for first playable co-op; the separate solo campaign is independent and does not merge progress into the shared one. Shared campaign progress follows its host and authenticated campaign identity; Raye does not need the same local slot number. Settings and graphics preferences remain personal. Existing local co-op stays available. P2 should receive the equivalent clear navigation/save separation when its online adapter is ready.

Sequence: finish63 identity fix and two-phone connection/reconnect checks; then add discoverable menu navigation and campaign selection as part of the playable co-op work. Add regression coverage for slot association, new/continue/join mode selection and cross-slot protection; require actual solo/shared save-load/relaunch checks on backed-up test campaigns once supported. This is an approved future requirement, not a feature claim for Build63.

# Open Nectar — cross-progression, disconnect and host recovery

Date: October25,2026. User-requested design expansion. These are engineering targets and decisions, not implemented save/cloud/gameplay features. Continue P1 iPhone connection/gameplay milestones first; do not replace or modify working PC installations in this batch. P2 stays preserved and receives its own engine/save adapter later.

## Latest requested experience and scope

Play the same shared campaign on PC at home and native iPhones away, with both players' progress/captains/squads preserved. The host may transfer a campaign to their own other device between sessions; this is a deliberate device handoff, not live host migration or merging two independently played timelines. Either person may host a new campaign as already agreed. One official active campaign/host at a time.

User now prefers an optional host-continues mode if the guest disconnects, but accepts pause-and-wait as the first implementation. This refines earlier together-only notes: brief host continuation is a later desired option; independent concurrent offline branches/save merging remain deferred. Do not auto-enable solo continuation or invisibly assign a bot to Raye's captain. First implement safe waiting/rejoin.

## What each kind of interruption actually requires

| Event | Intended first behavior | What permits recovery | Limit |
|---|---|---|---|
| Guest loses network or closes their app; host stays alive | Host remains in the session; pause the authoritative world and show waiting | Host retains live world and both players' actors/jobs; authenticate the same player, send fresh complete guest baseline, then both ready | Resume the host's PAUSE tick, not an unknowable exact instant the last guest display disconnected; detection may take time |
| Host loses network but app/world remain alive | Retain and pause host world; guest shows waiting | Restore connectivity/room route, authenticate, resynchronize guest from live host and both ready | No disk restore is needed solely for a network drop, but keep the app alive; mobile OS may suspend/terminate it |
| Host app crashes, is force-closed, OS-terminated, phone reboots or loses power | Recover from the last complete validated mid-day checkpoint | Durable full host-world state, not just actor positions or the last displayed picture | Progress after the last completed checkpoint can be lost; cannot promise zero loss |
| Both intentionally stop/change devices | Explicit save/handoff and close active session, then continue on destination | Validated portable campaign/checkpoint package + stable player identities + one active host | Early handoff can use a normal between-days save only after round-trip validation; exact mid-day handoff needs full checkpoint support |
| Old host is permanently unavailable and guest wants to recover | Later explicit emergency recovery from latest acknowledged host-authored recovery copy | Guest has a COMPLETE recovery payload and verified revision/identity | Ordinary rendered guest replicas omit host-private AI/job state and cannot simply become a host; automatic migration/split-brain prevention is separate work |

A relay forwards network traffic; it does not automatically run/persist the world. A dedicated always-on PC/server can keep the world alive while phones disconnect, but is an optional future hosting mode, not a requirement for leaving home. No provider, service account, cloud synchronization or paid infrastructure is selected/deployed.

## Reconnect screen and honest save labels

Target: “Raye disconnected — game paused.” Host is not kicked to the title screen. Show last contact/reconnect status and which player is missing, without repeatedly spamming alerts. Rejoin authenticates Raye's durable PLAYER identity and restores her captain/squad ownership; never create duplicate captains/Pikmin or reset the day just because a socket reconnected. Disable actions until required state is loaded and both acknowledge Ready; short visible resume countdown avoids surprise combat.

First supported choices: Wait / retry connection; Quit to last verified save. Before full mid-day persistence, the quit screen must identify the actual saved day/checkpoint and clearly say later progress will be lost. Do not label this “Save here and quit” or imply current-day progress was saved. Once complete mid-day saving is verified, add Save here and quit, show writing/success, and only close after success. A write failure keeps the world open and the previous good save intact; no false successful-save indicator.

Optional Continue alone is a later policy with extra tests. Once the host continues, Raye rejoins the CURRENT world, not a rewound copy of her old moment. Decide how her captain and followers are protected and how already-working Pikmin behave without stealing ownership, duplicating workers, granting combat invulnerability exploits or silently losing her squad. Do not promise exact frozen-moment restoration at the same time as continued host progress.

## Full mid-day checkpoint direction

This is substantial engine work, not a timer around MemoryCard::writeCurrentGame. Existing source audit: memoryCard.cpp/PlayerState/card storage represents a prepared campaign/day checkpoint; it omits live state and can have day-end side effects. card_stubs.cpp writes raw card buffers/metadata; identical bytes across current Windows/iOS builds have not been round-trip proven. Current actor_frame capture covers captains/Pikmin visual data ONLY.

Capture at a consistent simulation tick with all in-flight inventory commands resolved or recorded. Include day/time/area, story/collected items/unlocks, Onions and per-player allowance accounting, durable player/squad ownership, actor types/health/positions/velocities/AI and animation-action progress where gameplay depends on it, enemy/spawn/generator state, hazards/bombs/timers, RNG, seeds, bridges/gates, jobs/carry targets/attachments and validated entity relationships. Record accepted command sequences/transaction dedup state to prevent repeating withdrawals or collected parts after recovery. Rebuild rendering/audio resources; never dump pointers, vtables, the native heap or GL/SDL handles.

Build a versioned common container with game ID/release, schema/gameplay-compatibility/content/rules identities, campaign UUID, stable player IDs, monotonic revision/parent digest, tick, checkpoint kind and checksum. Device/time stamps are for display, not authoritative conflict ordering. PC x64 and iOS ARM64 must use canonical field encodings, not native struct padding or pointer width. P1 and P2 share container/validation machinery but require separate complete world adapters.

Regular validated checkpoints while playing are safer than waiting until disconnect/crash; the process might already be gone. Use a temporary write, validation, durable flush/atomic replacement appropriate to platform and multiple last-good generations. Keep the ordinary campaign card separately backed up. Make time interval and work-budget decisions after measuring world size and phone performance, not an untested promise of per-frame/per-second autosaving. Defer capture during unsafe loading/cutscene transitions while preserving the last completed snapshot.

Networking and recovery share IDs, codecs and world representations, but reconnect-to-live-host can use a guest baseline smaller than a restorable host checkpoint. Implementing the guest view does NOT automatically solve saving. Conversely, copying a COMPLETE host recovery payload to the guest can provide a useful second backup later. Only advertise that copy as available after the guest acknowledges receiving/validating its full revision. No automatic authority transfer simply because a heartbeat was missed.

## PC/iPhone cross-progression and mod parity

Feasibility: credible for a common native codebase, but requires implementation and validation. Checkpoint handoff is a smaller milestone than exact mid-day or automatic cloud handoff. Initial safe UX: Save and close session > Take campaign to phone/PC > validate import > continue same campaign. Begin with explicit local export/import; automatic cloud sync is a later transport choice and must work on both Windows and iOS. Do not depend solely on an iPhone-only storage service or device wall-clock timestamps.

Destination verifies campaign/revision/schema/game/gameplay content before activating; back up its existing state first. Preserve the old copy until destination acknowledges successful validation/write. Reject an older or divergent same-campaign revision with a clear choice; never silently overwrite the newer campaign or merge duplicate progress. Prevent accidental two-host use through explicit handoff/session status; stronger multi-device/cloud locking requires a real authority/lease design, not only a local flag.

Portable player IDs preserve Chazz/Raye captain slots and squads when changing hardware. Device identity is not player identity, and a typed display name alone is not authentication. Keep credentials separate from the exported public campaign summary; use scoped authenticated rejoin/transfer mechanisms when implemented.

Maintain one shared gameplay-rule/mod profile across targets (difficulty, speed, day length, squad rules and gameplay changes). Keep resolution, FPS, graphical effects, volume, touch/controller layout and other device preferences LOCAL. Cosmetic packs may differ after confirming they do not change simulation. The current room test uses an iOS-specific build digest and connection-only capability; before PC interoperability, separate protocol/gameplay/data compatibility from platform-specific UI/render code. Different PC/iPhone binary hashes are expected. Match actual shared game logic/schema, not executable-file equality.

No PC game binaries/settings/mod folders are changed now. Later build the desktop target from our branch with the shared gameplay improvements, preserve its original installation and test Windows/iPhone card/checkpoint round trips plus gameplay rules. Whether at home uses two PCs or one PC/local controllers is an input/view setup question to settle later; it does not block the portable campaign design.

## Additional QOL targets worth building

- Campaign card: area/day, actual last save, saved-on-device versus transferred/available-on-other-device status, active host/device and game/mod compatibility. Never show a cloud success badge for only a local save.
- One-tap rejoin of the intended partner slot using a securely stored scoped token, with fresh state validation; show downloading/rebuilding/ready, not a misleading frozen screen.
- Shared pause/interruption indicator and short both-ready countdown. Keep network processing alive while world time/jobs/hazards are frozen.
- Clear gameplay-rule mismatch explanation and deliberate adopt-host-rules prompt; do not overwrite local graphics/control preferences.
- Rotating last-good checkpoints, backup before import/update and a readable restore menu with campaign/day/revision, avoiding manual hunting through folders.
- On first rollout, compact connection health beside optional performance display, and a single configurable sound/haptic for partner loss/rejoin. Partner pings/direction/squad status already remain in the agreed plan.
- Later handoff confirmation: “Campaign ready on phone — saved at Day X / checkpoint Y.” Leave old device paused/closed; no need to keep a PC running for a completed portable handoff.

These are planned product improvements, not features claimed present in the current phone build.

## Primary research and what is actually transferable

- [Stardew Valley developer mobile multiplayer guide](https://www.stardewvalley.net/mobile-multiplayer-guide/): officially supports experimental mobile clients joining PC-hosted farms, requires matching game versions and discusses mobile interruptions/local-network permission. This validates the relevance of cross-platform versioning and interruption handling, not our save implementation or cellular reliability.
- [Grounded developer Shared Worlds notes](https://grounded.obsidian.net/news/grounded/grounded-heads-into-the-home-stretch): shared campaign progress is restored across later hosts, with one active host. Adopt the single-authoritative-campaign/clear handoff principle; we are not adding its cloud service or independent play features now.
- [Factorio developer joining/catch-up explanation](https://www.factorio.com/blog/post/fff-149): joining receives world data then catches up, with separate synchronization state. Our initial pause-and-resynchronize approach avoids an extra catch-up race; we are not adopting its deterministic simulation/lockstep design or claiming equivalent features.

## Work order and acceptance evidence

1. Finish current P1 Apple connection-screen build and real two-phone private-room proof; working P2/solo installs preserved.
2. First playable iPhone host/guest world/ownership/actions/private views; live-host pause/re-auth/rejoin of the same captain/squad at an accepted tick.
3. Incremental complete world checkpoint capture AND restore, starting with familiar area/captains/squad/enemy/carried item, then all required systems and corruption/transaction checks. No finale spoilers.
4. Periodic atomic checkpoints + truthful Save here and quit + optional host-authored guest backup. Test guest app loss, host-only network loss, host app kill/reboot, both app closes and restoration without duplicated/vanished progress/Pikmin.
5. Windows gameplay parity and verified portable normal-save/full-checkpoint round trips. Then explicit PC/phone campaign handoff, backups and stale/divergent revision handling; cloud sync and live host migration remain later choices.
6. Optional continue-without-partner policy and different-network/relay proof; P2's own stronger world/save adapter and tests. Exact sequencing of checkpoint and desktop work may overlap after iPhone base stability, but neither should hold basic connection/UI validation indefinitely.

Progress guarantees must reflect actual evidence. Live retained-host rejoin can target the host freeze tick; crash recovery can only guarantee the last COMPLETE committed/acknowledged checkpoint, and exact PC-to-phone mid-day carryover requires that checkpoint system first.
