## PC7/iPhone91 successful, verified and ready to test — 2026-10-29 23:03 EDT

Windows7/run40988434328 and iPhone91/run40988434305 both SUCCESS at source0296f6a26e0600f3c66f0c8b6038a68c6ae3f3a5. PC7 INSTALLED after verified PC5 backup;3199 protected config/save/content files unchanged. Phone91 IPA STAGED, not installed by Codex. Identity31cb99e8cc7d34514117939becbc9465ce24ad08d441bc56bf643af2ec750141 matches both packages and tracked source. Full25 native tests/21 practice/13 room receipts/real UIKit socket+scene resume passed. Hardware guest stutter/audio fix NOT YET tested. No more builds or polling; user next updates phone to91 then tests with usual PC launcher. P2 unchanged. Full current report follows; older status entries are historical.

---

## Matching guest timing/audio builds submitted — 2026-10-29 21:54 EDT

Committed and pushed `0296f6a26e0600f3c66f0c8b6038a68c6ae3f3a5` to `ios-experimental`, based on synchronized local/remote`21480b5bfcba7e8f0ebc18e58c38de2f65d34070`. Tree clean after source commit. This is the source included in BOTH replacements:

- iPhone **91**, run **40988434305**, last checked **IN_PROGRESS**: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40988434305
- Windows **7**, run **40988434328**, last checked **IN_PROGRESS**: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40988434328

No new artifacts/IPA yet; no successful native compilation or new phone runtime result claimed. Installed PC5/iPhone90 stay untouched. P2 unchanged. Stop CI polling and await the user's completion report, then fetch full logs/receipts, verify BOTH packages/identity, stage in Documents and offer one short mixed PC+phone practice test. A second phone is optional. Phone USB work is complete and it may be unplugged.

Local validation:30/30 network/codec/session/engine-adapter tests passed including real encrypted sockets;120 host/guest-rate/latency/jitter combinations pass, old-clock negative control fails10 combinations. New source also coalesces sustained whistle/ready requests and prevents duplicate nested native sound commands; actual adapter regression PASS. Actual5 engine translation units pass Clang syntax/analysis with existing legacy warnings; strict new adapter/codec analysis and existing231 smoothing/14 focus/8 carry/10 exit checks pass. The new audio fixture uses fake playback resources; it does not prove audibility on iOS. Full report below provides exact scope, remaining co-op vision and verification limits.

**Exact next action:** user says build finished -> inspect project GitHub logs yourself; correct actual failures if any, otherwise validate/stage matching Windows7/iPhone91; same-app updates preserve settings/saves/texture packs. Do not reuse PC5 with phone91. User should compare guest movement and whistle/throw/Pikmin/footstep audio, then pause/resume and reverse roles. No need to keep a live game open while builds run. Next-test checklist is in Documents/Open Nectar/2 - Progress and ChatGPT Handoff/NEXT TEST - PC7 and iPhone91.txt.

---

## Current task — 2026-10-29 21:46 EDT

PC5/iPhone90 guest role stutters and lacks SFX on both PC/phone and phone/phone. Timing + bounded host-to-guest audio replacement implemented and locally verified (30 tests,120 rate/jitter combinations); GitHub/native/hardware validation pending. Both peers must update to the next matching pair. No new phone writes; may unplug. All objectives below remain queued.

---

## Progress reporting preference — 2026-10-29

When the user asks how close P1 co-op is to completion, lead with a percentage of the FULL agreed vision. Label it an engineering estimate, not a measured task count. Current estimate communicated: approximately40% IF the PC5/iPhone90 real-device practice test passes; that hardware test HAS happened and failed guest stutter/audio; no completed-full-mode percentage increase is justified. Include shared campaign world/Onions, game flow/cutscenes, mid-day persistence/recovery, internet play and PC/iPhone continuation in the denominator. Do not inflate the full-mode percentage by reporting only network-foundation completion.

---

## Verified PC5/iPhone90 ready for device test — 2026-10-29 20:42 EDT

Windows5/run40976294203 SUCCESS, verified and INSTALLED over closed PC4 after backed-up receipt/config/save protection;3199 protected files hash-unchanged. iPhone90/run40978326061 SUCCESS, strict native/simulator/package/identity checks PASS, IPA staged NOT installed. Both identity26204c2b52dcf03c59c52798930a69a9e11a4a6c9272600e9c7a8eb29e650f9e. User next: same-app Sideloadly update phone to90, then mixed both-host-role practice movement/readiness/interruption test. No USB task/new build. P2 unchanged. Full current report at end below and in Documents/Open Nectar/2 - Progress and ChatGPT Handoff. Prior current-state entries are historical.

---

## iPhone90 submitted; pair with successful PC5 — 2026-10-29 20:14 EDT

Correction source `dcfba41f178d0e8905c215b4d668da67e1f43939` pushed. iPhone90/run40978326061 last checked IN_PROGRESS: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40978326061 . Windows6 is intentionally SKIPPED because this only changes tests/workflows/docs. Keep verified PC5/run40976294203/artifact12943316091 for the pair; identical game identity26204c2b52dcf03c59c52798930a69a9e11a4a6c9272600e9c7a8eb29e650f9e. No new IPA yet. iPhone89 produced diagnostics only; its stale exit fixture is corrected with10 passing real-smoothing cleanup checks and two sensitive negative controls. Preserve installed PC4/phone88 until verified replacements; original Louie restored, no USB task. Await user build result; no idle polling. Full current handoff is at the end below and in Documents/Open Nectar/2 - Progress and ChatGPT Handoff.

---

## iPhone89 failure diagnosed; PC5 verified — 2026-10-29 20:12 EDT

PC5/run40976294203 PASSED and its package is verified, not installed. iPhone89/run40976294072 stopped in an OUTDATED extracted exit fixture: missing smoothing/presented declarations. Full game/socket probe were not reached; the later mandatory socket error is a correctly rejected skipped step. Actual21 practice/13 room receipts passed. Fixed fixture now uses real smoothing and tests10 exit/lifetime/cleanup cases; strict MSVC/Clang and two negative controls pass. Only tests/workflows/docs change; identity stays26204c2b52dcf03c59c52798930a69a9e11a4a6c9272600e9c7a8eb29e650f9e, compatible with PC5. Submit only new iPhone build, retain PC5; no [pc-coop-build] marker. Original Louie is restored, USB task complete. Latest full report is at the END below and in Documents/Open Nectar/2 - Progress and ChatGPT Handoff. Prior current-state claims below are historical.

---

## Paired fix build submitted — 2026-10-29 19:56 EDT

Source `deaaee1ee0b884c5c939f456b6a5ccfff4d23d40` pushed. Windows **5**: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40976294203 ; iPhone **89**: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40976294072 . Both last observed IN_PROGRESS, no final result/new artifacts yet.231 smoothing +14 actual focus +8 carry assertions and actual adapter/view/authority/strict frontend/Clang checks passed locally. Preserve installed PC4/phone88; wait for the user to report build completion, then verify full logs/receipts before staging BOTH clients. No idle CI polling. Original Louie restore approved but pending USB/P1 closed. Upstream1.1.1 reviewed, not merged; see UPSTREAM_AUDIT_2026_10_29.md. P2 unchanged. The latest full report is at the end of this journal and in Documents/Open Nectar/2 - Progress and ChatGPT Handoff.

---

## Current checkpoint — 2026-10-29 19:53 EDT: PC4/iPhone88 hardware feedback and coordinated fix batch

This entry supersedes older current-state claims below. Matching PC4/iPhone88 were installed and tested. PC host runs smoothly locally; phone guest actor movement stutters, reverse-role Windows Ready sticks, and PC log records missing-Onion `zannnen` panic. Guest arrival-time visual smoothing, Windows focus/Ready ordering and safe missing carry destinations are implemented and locally verified; new native builds are pending. Original low-detail Louie restore is approved but NOT done (no USB device detected; no phone writes). P2 unchanged. Read the newest full progress report at the end of this file, UPSTREAM_AUDIT_2026_10_29.md and Documents/Open Nectar/2 - Progress and ChatGPT Handoff/Exact Resume State.json for resolved commits/run IDs. Do not install unverified packages or merge all upstream files. Preserve PC4/phone88 as rollback and all save/graphics/control preferences.

---

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


### Clearer co-op join errors (after Build 82)
Room join messages now distinguish known game, region, build, game-content and capability mismatches, and report failure to initialize the network separately. Unknown mismatches remain generic. The existing compatibility gate and independent personal settings are unchanged. Source contract check passed; native iOS and device UI validation still required. Not included in Build 82.


2026-10-28: User added co-op cutscene/story requirements without changing the active task. P1 source audit and non-spoiler design/test checklist are in `ios/COOP_CUTSCENES_AND_STORY.md`. Scene synchronization is not implemented or phone-tested; practice deliberately skips campaign scenes.


### Build 82 verified and Build 83 submitted (2026-10-28)
Build 82/run 40720211222 succeeded at 176615ea791ba6bd5bd182672448466c953176ff. P1 artifact 12831464151 verified: ZIP SHA-256 d727bdbb119070e8985f2a06d3258383195b71ffbf26a60c361f9036c15fc04c, IPA SHA-256 69a52b4f7b2983d3b0c78c0d2591d6d82f5a6b901186b010a73c140d1556fb4b. 21 practice, 13 room, encrypted UIKit simulator and ARM64 packaging checks passed. Staged in Documents/Open Nectar/1 - Install on iPhone/P1 Build 82 - Co-op Interruption Fix. Not phone-tested.

P1-only Build 83/run 40727018878 at 74eb8c0aba1662676d08267819f4c39182161212 was submitted and in progress: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40727018878 . It groups post-82 stale-action expiry, invite concealment, clearer join errors, shared-Onion zero-epoch validation, and network test changes. Local 27/27 suite passed; iOS and hardware results pending. Story/cutscene plan is documentation only; the visual smoothing helper remains unintegrated. P2 unchanged.


### High-delay room feedback (after Build 83 submission)
The room screen now gives a plain-language warning when measured round-trip delay is at least 200 ms and notes that controls may feel slow. This is an advisory threshold, not a guarantee about responsiveness, loss, or other networks. It does not alter player FPS or quality. Source presentation contract passes; native iOS and phone testing pending. Not in Build 83.


### Shared-Onion aggregate capacity guard (after Build 83)
`OnionAuthority` now requires an explicit aggregate field limit in addition to separate player allowances. Host-side accounting rejects a withdrawal atomically when the combined field count would exceed that limit, retains shared stock, and caches the rejected result safely for retries. Tests cover independent allowances, a smaller combined limit, retry safety, explicit invalid limit and existing 10,000-cycle conservation; local suite passes. Choosing an actual P1 limit must account for engine and snapshot bounds and device performance. This isolated foundation is not connected to campaign gameplay, is not in Build 83, and has no iOS or hardware validation.


### Build 83 verified (2026-10-28)
P1-only Build 83/run 40727018878 completed SUCCESS at 74eb8c0aba1662676d08267819f4c39182161212. Artifact 12834424027 ZIP SHA-256 bb67baf67090fd398562b0274a611a9d0fe6e8156813cb731ee7c98db33fe729; IPA SHA-256 aaac83a9bd3913cca811f462897ed6138a0c048695524c8dad1feed8cb2786c2. Verified 21 practice, 13 room, encrypted UIKit simulator, ARM64 and package; staged at Documents/Open Nectar/1 - Install on iPhone/P1 Build 83 - Co-op Safety and Usability. Not installed or tested on phones in this checkpoint. Later source high-delay warning and Onion aggregate-capacity foundation are not included. P2 unchanged.


### Reliable-queue diagnostics (after Build 83)
The transport now distinguishes reliable bytes still queued locally from bytes sent but not yet acknowledged. P1's existing bounded local-only practice report records both once per second alongside RTT; it does not include invite codes or device IDs and is not automatically sent anywhere. This is diagnostic only: no new throttling or gameplay policy is enabled. Full local network suite 27/27 passed including encrypted GNS metrics; real-header Clang check passed with the existing Windows fopen deprecation warning. Native iOS and device validation remain pending; not included in Build 83.


### Build 84 submitted (2026-10-28)
P1-only run 40773579467 at 4a886468d3c3a263d477fe1702cae290fed2cf83 is queued: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40773579467 . It includes the post-83 high-delay room message, explicit combined Onion capacity foundation, and additional local-only reliable-queue diagnostics. Local 27/27 networking tests and P1 real-header analysis passed; no iOS result or phone validation yet. Shared Onion remains unintegrated into campaign and the scene sync plan is documentation only. Build 83 remains verified and staged; P2 is untouched.


### Stale continuous-input guard (after Build 84 submission)
P1 practice input will not publish a cached held control or stick value if local sampling has stopped or its timestamp is stale for more than 300 ms. When fresh samples resume, normal held controls publish again; host-side input expiry remains responsible for releasing missing movement. Focused input/session tests and real-header local analysis passed. This is a source-level safeguard, not proof that any observed device freeze was caused by stale sampling. Not in Build 84; iOS and phone testing pending.


### Upstream comparison (2026-10-28)
Fetched upstream/main 77a5aaa4, with releases through 1.1. Upstream changes include P1 seed landing, P1/P2 card atomic-write work, P2 local co-op cinematic fixes, P2 missing-audio fix, and desktop/Android menu and launcher changes. Do not wholesale merge: our iOS renderer, touch, save isolation and networking differ. P2 audio was already user-reported working on our build; upstream P2 changes require separate comparison and testing.

P1 source has the steep-wall seed push already, but snapped seed landing at 30 FPS as well as 60/120. Adapted upstream commits 33b5abc7 and aa18d8a4: retain the existing steep-wall push, preserve original 30 FPS bounce, and keep higher-FPS ground snap. Upstream's small decision tests passed locally and the actual itemAI translation unit passed local real-header Clang analysis with existing Windows deprecation warnings. Workflow now runs the test in future P1 iOS builds. The change is not in Build 84 and has no iOS build or device validation yet.

Upstream atomic card writes are not yet imported: our current P1 card layer includes separate practice-save isolation and concurrent I/O guards. A safe adaptation must test old-save preservation, metadata consistency, short/full disk writes, rename failures, delayed worker jobs and interrupted save stages on isolated fixtures before any integration. No claim that a simple file flush guarantees power-loss durability.


### Isolated P1 interrupted-save recovery test (after Build 84)
Added `tests/pikmin1_card_recovery_test.py`, which extracts the actual `DoSave` and `DoList` functions and links the actual P1 CARD backend to isolated temporary fixtures. It injects failures before create, write, status, old-file delete, and final rename, then invokes real listing recovery and checks that the complete expected old or new bytes remain accessible. Local Windows fixture passed for these controlled stages; no actual phone files were opened or changed. This does NOT simulate failure partway through a write, filesystem rename, metadata pair, OS termination or power loss; it does not prove durable/atomic saving. The new test is included in the next P1 native-build check, not Build 84. Upstream atomic card-write adaptation remains under investigation and was not applied.


Save-recovery fixture expansion: in addition to failures before each stage, it now deliberately writes half of a temporary test save then reports an error, and models errors reported after metadata update, old-save delete or rename have completed. In isolated Windows fixtures, actual DoSave/DoList and CARD backend recovered a complete expected old/new file for all ten scenarios. This deliberate half-write model is not an actual interrupted stream, OS crash, filesystem metadata failure, sudden power loss, iPhone test, or proof of full durability. Real saves were not touched; upstream atomic backend remains unmerged.


### P1 interrupted-save preservation guard (after Build 84)
A controlled fault fixture using actual P1 `DoSave`, `DoList`, and CARD backend showed that if the old save had been deleted and the remaining temporary file's metadata was missing, the previous recovery scan deleted that remaining file. Another simulated case truncated the remaining temp below the comment size. Source now refuses to promote a too-short temporary file and, when its final save cannot be confirmed present, returns an I/O error while preserving the temp rather than deleting it. Existing cleanup when a final file opens remains in place. This is not automatic repair and may surface a card error requiring recovery assistance.

The independent local fixture covers 12 normal/interrupted/simulated partial or missing-metadata cases; both negative-control variants fail when their respective guard is removed. Actual practice card admission fixture still passed. Real-header Clang also identified a pre-existing potentially uninitialized card-worker result for an unexpected command; PC code now initializes it to a fatal error before dispatch, and that analyzer warning disappeared. Other existing warnings remain. No real phone/save files were modified; no iOS build, crash/power-cut, or hardware behavior has been verified. Upstream's atomic write patch is still not applied.


### Clarified full PC/iPhone co-op and required mid-day recovery (2026-10-29)
User clarified that a keyboard-only diagnostic partner is insufficient: the full P1 game must run and display independently on both participants, supporting PC+PC, iPhone+iPhone and mixed PC+iPhone, either device hosting. Seamless continuation of the shared campaign between PC and iPhone is part of the target. Mid-day autosave/recovery is now REQUIRED for the finished mode, superseding any earlier plan to accept only restarting the day after closing/crashing. Account explicitly for incoming phone/FaceTime calls, full-screen interruptions, locking/unlocking, backgrounding, accidental swipe-close, guest/host crash and transport loss. Temporary interruption should hold authority and require readiness on return; process death requires a previously durable validated checkpoint, not a promised final background save. Plan periodic versioned full-world snapshots with retained last-known-good generations, bounded rollback, verified commit and shared-campaign identity/ownership protection. Exact save interval and safe coverage of clock, actors, AI/jobs, parts, Onion stock, scene/story and RNG remain implementation/measurement work; current actor visual packets are NOT sufficient save snapshots. Do not claim this works until actual capture/restore and crash/relaunch/device-switch tests pass. Guest backup of accepted recovery data is a future safety option, not implemented host migration.

The phone-host/PC diagnostic guest test on Build84 was user-confirmed visible and movable with Louie visible; automatic guest movement looked mostly smooth with some possible stutter (user uncertain). Measured LAN RTT about3-4ms with live actor frames. PC pause correctly blocked the host from resuming alone. No actual iPhone guest display test completed. Ended the diagnostic peer on user clarification. Unfinished native keyboard-controller prototype preserved only in workspace work/manual-controller-prototype; not a delivered full PC client.

Next engineering step: build real Windows P1 from the shared fork, expose the same retained-room/practice adapter in desktop UI, and produce paired compatible PC/iOS builds. Existing upstream desktop online menu uses a separate disabled path; do not silently enable it or assume compatibility. Windows game expects MinGW; no local MinGW/WSL environment is available yet. Evaluate isolated portable compiler or dedicated experimental CI cross-build rather than changing the user's OS. Campaign snapshot/transfer design and tests remain queued alongside this integration.
