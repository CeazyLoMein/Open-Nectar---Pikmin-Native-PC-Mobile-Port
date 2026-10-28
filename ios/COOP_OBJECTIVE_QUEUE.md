## Current checkpoint — 2026-10-28: Build 81 and subsequent source work

Build 81 (run 40711881021) was submitted from e65708c7; GitHub Actions completed successfully; two-phone behavior remains untested. The P1 artifact is 12829465661 and has not been downloaded or staged in this checkpoint. Build 80 remains available for a solo launch test only. After Build 81, source commit 8f5544f0 added an isolated, tested visual blending candidate that is NOT connected to gameplay; be4d3da8 changed iOS co-op interruption observers to the actual game scene. Neither change is in Build 81. Scene change has not passed an iOS build or phone test. P1 practice is not shared campaign co-op.

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
