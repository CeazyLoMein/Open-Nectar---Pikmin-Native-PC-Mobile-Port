## Current checkpoint — 2026-10-28: Build 81 and subsequent source work

Build 81 (run 40711881021) was submitted from e65708c7; GitHub Actions completed successfully; two-phone behavior remains untested. The P1 artifact is 12829465661 and was downloaded, validated, and staged in Documents/Open Nectar/1 - Install on iPhone/P1 Build 81 - Co-op Practice. Build 80 remains available for a solo launch test only. After Build 81, source commit 8f5544f0 added an isolated, tested visual blending candidate that is NOT connected to gameplay; be4d3da8 changed iOS co-op interruption observers to the actual game scene. Neither change is in Build 81. Scene change has not passed an iOS build or phone test. P1 practice is not shared campaign co-op.

Next: verify Build 81 when convenient; batch later work into a meaningful iOS build; test interruption and both phones when available. Account for stale/expired invites, iOS suspension, disconnect/rejoin and preserved frozen authority without claiming a live recovery exists. Preserve player preferences, saves, user features, cross-progression and P2 objectives listed below.

---

## Current checkpoint — 2026-10-28: Build 80 verified, co-op UX in development

Build 80 passed and is staged in Documents/Open Nectar/1 - Install on iPhone/P1 Build 80 - Co-op Practice Fix. One phone can check solo launch, but not prove two-player behavior; Raye is unavailable. Following requested in-depth co-op research (see COOP_MOD_RESEARCH.md), current source adds game-inspired accessible scrolling UI, explicit private-invite sharing, background room retention without claiming iOS guarantees it, and clear ready/partner interruption messages. Local checks passed; Apple build and runtime untested. Preserve independent player options and all prior objectives below, including reconnect, different-network play, shared campaign/Onions, host loss recovery, PC cross-progression and P2 later.

---

# Current checkpoint — 2026-10-27: Build 78 ready for first two-phone test

Build 78/run 40582347682 succeeded and its verified P1 IPA is staged in Documents/Open Nectar/1 - Install on iPhone/P1 Build 78 - Co-op Practice. It is a disposable practice-area experiment, not campaign co-op; no phone installation or gameplay has been verified yet. User and Raye will test when available. Existing P1/P2 and settings must be preserved.

After Build 78, source-only checkpoints added practice-specific squad whistle ownership and an authenticated retained-room reconnection foundation; local tests including real encrypted loopback passed. Neither is included in Build 78. Reconnection is not yet integrated into the game UI or tested on iPhone; host-loss recovery, exact mid-day persistence, online across different networks, shared campaign/Onions and cross-progression remain open. Current and former requirements below remain binding. See OPEN_NECTAR_IOS_HANDOFF.md for full history and validation boundaries.

---
## Current population/pose checkpoint — 2026-10-27 11:51 EDT

Actual P1 guest population and sampled animation/render source implemented; local fixtures/Clang/24 rebuilt network tests/encrypted probe PASS. No Apple/full-engine or phone validation yet. No77 dispatched, keep installed68. Guest visual slots remain outside live AI; complete world/room/scene/input driver still pending. New mandatory native gate has17 checks. Pikmin wire schema2=50bytes. Checkpoint subject `Integrate guest Pikmin populations and host-sampled poses [skip ci]`, parent 6699108ac4ae81a0b23dcf7bb976ccbf509abc5a; resolved post-push revision in accessible Exact Resume State.json.


---

## Historical checkpoints — current entry above supersedes current-state claims below

## Current checkpoint — 2026-10-27 11:13 EDT: integrated authority source, local checks PASS, native deferred

Build76 remains SUCCESS. Working phone baseline68 retained. New host/guest authority is wired through known engine update/draw/mode/message/camera paths, with guest maturity mesh and held attachment correction. Local source fixtures/Clang/negative controls pass. Apple/full-engine and phone validation for this batch have NOT run. No Build77 requested; no playable online Start exposed. P2 unchanged. Next: population/animation/full world baseline + room/area/input driver together, then meaningful native batch. Resolved post-push commit is in accessible Exact Resume State.json; checkpoint subject `Hold replicated co-op worlds across engine update and draw [skip ci]`.


---

## Historical entries — use the current checkpoint above

# Open Nectar co-op — running objective queue

User instruction: new steering adds requirements/tasks; do not discard earlier objectives or silently replace the active task. Only explicit cancellation removes an objective. Statuses below are evidence boundaries, not completion percentages.

## Build batching rule — user reiterated after Build76

Group related work toward a concrete two-phone practice milestone; use local tests between edits. Native CI is for meaningful integrated batches or demonstrated failure correction, not the default after each internal helper.76 is verified PASS; no77 triggered this checkpoint. Preserve all existing requirements below.

## Immediate sequence

1. Build75/run40338639501 actual startup/view Apple fixtures/full native app/networking/package SUCCESS. New guest captain+Pikmin whole-cohort adapter locally checked; inspect its exact next native result when user reports it. Keep68; no phone task.
2. Research COMPLETE: QSB/Skyrim Together/Elden Ring Seamless/BBSC. Independent camera/graphics/FPS120/controls/touch/audio remain core; old settings-locking30FPS session is not enabled.
3. Actual protected title/setup and independent view context implemented. New guest explicit Pikmin binding/atomic state apply is fixed-cohort ONLY: no spawning/removal/conversion, animation/jobs, guest freeze or complete world yet. Normal Piki death has counter/seed/effect side effects; create a guest visual lifecycle adapter rather than replaying host gameplay.
4. Complete game-thread room ownership/pump, full world baseline, guest simulation/presentation separation, controller/camera mapping and restart/exit UI before enabling Start. Then request one concrete same-Wi-Fi two-phone gameplay test; avoid more connection-only retests as a substitute.

## Core requirements carried forward

- Each player has their own fullscreen camera and squad, can separate across the current area. Personal camera options, FPS/resolution/graphics/audio, controls/sensitivity and touch layouts remain independent and persist after leaving. Cosmetic packs may differ once proven rendering-only; no arbitrary-mod guarantee.
- Shared campaign is played together, host owns progress; separate solo and shared save slots. Shared Onions/population with independent player field allowances. Both players can act/progress; atomic counts and no duplicate rewards/actions.
- Main-menu Online Co-op entry and understandable Host/Join/Rejoin flow. One-tap rejoin intended partner/session where safe. Preserve local co-op and solo behavior.
- Guest disconnect: retain/pause host world, wait/rejoin with full verified state; clear quit-to-last-save label until real mid-day persistence exists. Mobile background/foreground and device differences explicitly tested.
- Forced group area/cave travel accepted. Difficulty primarily health tuning; extra actors only with performance evidence. Protect existing graphics/audio/pathing/recall/controls/mod improvements and avoid finale spoilers.
-120FPS option remains available; no unsolicited FPS/visual-quality reduction. Preserve accepted heat improvement. No untested full-campaign stability claim.
- Maintain reports/journal/exact source/run/artifact evidence and user testing checklist; new instructions add to queue. No idle CI polling or unnecessary repeat builds.

## Later milestones, still queued

- Full shared-world interactions, transitions and longer campaign testing; restore/checkpoint semantics verified before claims.
- Guest reconnect and host-loss recovery; exact mid-day persistence shared with future solo autosave. Preserve last good save on failure. No promise that input replay alone recovers a dead host.
- Different-network play and real invitation/reachability solution; same-Wi-Fi connection is not internet proof.
- PC port matching relevant gameplay/mod versions and explicit verified campaign handoff to/from iPhone; no divergent independent-play merge.
- P2 stronger campaign/unlocked test and equivalent online adapter after P1 evidence; preserve working P2 throughout.
- Optional per-player health/invincibility/difficulty if practical. Host applies per-player rules by identity; global shared world rules remain coherent. This may wait and must not displace core independent personal settings.

Historical reports and implementation/recovery docs retain all earlier investigations; consult those before marking anything complete or canceling prior work.

Build 81 artifact ZIP SHA-256 1057deff67d79bb5e9e336f4bb67c7a44a4794ac8ad99ea2209886a1a44c153d; IPA SHA-256 e0191ce3c53ce883ed6eba4f968e963f9c9604901c9354a973fb56b6180d6135. Package verified, 21 practice and 13 room checks passed, encrypted simulator probe passed. Hardware behavior remains unverified.


### Build 82 submitted (2026-10-28)
P1-only run 40720211222 at source 176615ea791ba6bd5bd182672448466c953176ff was in progress at submission: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40720211222 . Includes scene-scoped co-op interruption observers and clarified expired-invite guidance, plus isolated unused visual blending helper. Not yet iOS-compiled or device-tested at submission. P2 is not in this run. Build 81 remains a verified staged fallback.


### Practice stale-input guard (2026-10-28, after Build 82 submission)
Practice guest input previously retained unsent taps, one-shot actions and camera drag indefinitely while publication was stalled. Source now expires transient taps/actions/drag after 300 ms; live stick/held state continues from the newest sample. Individual button timestamps preserve a newer different action as an older action expires. This is an explicit compromise: a tap during an extended stall may be dropped rather than unexpectedly fire later. Focused practice input and session tests passed (including expiry and recovery); real-header local clang analysis passed with existing Windows fopen deprecation warning. Not in Build 82, and no iOS or two-phone test yet. This does not fix all lag or guarantee safe live rejoin.


### Shared Onion validation audit (2026-10-28)
The isolated OnionAuthority foundation already tests shared stock, separate per-player limits, replay/idempotency, invalid ownership, overflow and 10,000 conservation cycles. It now also rejects scene epoch zero, consistent with active co-op sessions. Local Onion authority suite passed. This is not connected to campaign gameplay, not in Build 82, and not hardware-verified; engine-side allocation/commit and full world/save integration remain required.


### Invite privacy while switching apps (2026-10-28, after Build 82)
The P1 room screen now hides the visible private invite text when its game scene deactivates and restores it on activation without clearing the room. This reduces app-switcher preview exposure; it is not a guarantee about other apps, the share sheet, or iOS behavior. Local presentation contract passed. No iOS compilation/device test yet; change is not in Build 82. Apple discusses background scene snapshots at https://developer.apple.com/documentation/uikit/uiscene/didenterbackgroundnotification .


### Weak connection simulator audit (2026-10-28, after Build 82)
Prior in-memory reliable messages were always idealized as lossless without retransmission delay, despite simulated loss configured for unreliable messages. Added an opt-in, deterministic approximation where a selected reliable message has extra delay and later ordered messages wait behind it. This is a test model, not an exact GNS retransmission or network performance claim. Tests pass for ordered blocking and for a delayed host pause: old guest movement cannot advance the host or leak into its resumed world. Local tests only; no iPhone or WAN evidence. New test and simulator are not in Build 82.
