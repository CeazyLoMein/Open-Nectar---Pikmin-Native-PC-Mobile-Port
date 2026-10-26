# Your Open Nectar testing checklist

Updated October25,2026. This is the running list of things Chazz and Raye will eventually test. **Only the Ready to test section is an active request.** Everything in Later waits until I provide a working build and clear instructions.

I will give you a small batch at a time, prepare the files in Documents, handle logs/build checks myself, and tell you whether a phone must stay connected/open. When I need you, I will send a clear message and an audio alert where available. No need to stay connected or leave a game running unless I ask.

## Completed — Build68 user reports tests all good so far (T05/T07/T08)

Verified68 IPA: Documents > Open Nectar > 1 - Install on iPhone > CURRENT - P1 Build 68 - Menu and Rejoin. Read START HERE.txt. Update BOTH existing P1 apps using SAME IPA/account/identity; no uninstall/data recopy/P2 update. Earlier65 LAN tests remain passed;68 new requested phone test bundle now user-reported PASS. No further update requested.

- [x] **T05 — Main-menu Online Co-op:** Open from title on both phones. Host fresh room, share code once, return host foreground, guest joins. Both show Connected. Still connection-only.
- [x] **T07 — Rejoin Last Room:** Guest Leave then Rejoin without pasting. Then host briefly opens Messages and returns; guest Rejoin after host returns. Keep app processes alive; no world/app-kill recovery claim.
- [x] **T08 — Return to game:** Done, normal solo/controls/settings preserved. Open native room from gameplay, wait briefly, Done; game visible/responsive without catch-up jump. Keep player FPS/graphics choices. No heat stress test.

Overall PASS reported by user October25; no independent per-phone repeat metrics. Nothing else to test now. Phones can close P1/disconnect. Full shared campaign slots/play/recovery tests below remain FUTURE.

## Completed — Build65 same-Wi-Fi room tests (T01–T04)

Build65 native build, actual simulator delayed-rejection/rejoin tests and downloaded IPA checks PASSED. The user confirms T01-T04 passed on both real phones over the SAME Wi-Fi; this does not test internet play. This is CONNECTION ONLY, not playable online campaign.

**File:** Documents > Open Nectar > 1 - Install on iPhone > CURRENT - P1 Build 65 - Connection Fix > Pikmin 1 - Build 65 - Connection Fix.ipa. Read START HERE.txt in that folder. Use an in-place update; do not delete P1/change app identity. P2 stays unchanged.

**Current step:**68 T05/T07/T08 overall user PASS, scoped to requested connection/UI test. No active phone task. Developer next: actual disposable shared-area/captain/camera integration; T10 not ready yet. T06 campaign slots remains future. Keep68 installed; FPS/graphics/P2 unchanged.

- [x] **T01 — Prepare both phones.** Have both available, unlocked and on the same Wi-Fi. I will prepare the verified update and exact file location. If signing/installing requires your input, I will give that one action; keep the existing app and its files.
- [x] **T02 — Connect a private room.** On both phones, open gear > Data > Online Co-op: Connection Test and wait for the data check. Host on your phone, copy/share the code manually, return the host to P1, then paste/join on Raye's. Allow Local Network access if asked. Tell me the status on BOTH phones; a screenshot is useful if something fails.
- [x] **T03 — Leave and reconnect.** Leave the room and join again, then try Raye hosting. We are checking the connection only; this screen does not start a shared campaign yet.
- [x] **T04 — Return to normal P1.** Close the connection screen and confirm ordinary gameplay, controls, graphics and your settings still work on both phones.

## Later — clear menu access and separate solo/shared campaigns

T05 is active above in68; T06 separate campaign saving still awaits implementation.

- [x] **T05 — Online Co-op on title menu.** Reach Host/Join directly without Advanced Settings. Existing local Co-op and normal solo remain accessible; connection-only tests must be clearly labelled until shared gameplay exists.
- [ ] **T06 — Separate campaigns and safe Continue.** On backed-up test saves, keep Solo in one slot and the shared campaign in another. Confirm correct labels/day/progress, solo save-load/relaunch, online save-load/rejoin, and that joining never overwrites the guest's solo campaign. Slot numbers may differ between devices; shared campaign identity must still match.

## Build68 tests now active above — historical task descriptions

- [x] **T07 — Rejoin without resending code.** After the new build is verified, join once, leave or briefly background the guest, then use Rejoin Last Room. Host briefly opens Messages and returns; guest should rejoin the retained room without fresh code. Memory is only for this app process; no app-kill/world recovery claim.
- [x] **T08 — Native-room pause and return.** After the new build is ready, verify the native screen stays responsive, Done returns to visible game/title with no catch-up jump, and your FPS choice/graphics/packs remain unchanged. No heat stress test requested.

## Later — first playable two-phone co-op

These wait until shared gameplay exists, not merely a Connected label.

- [ ] **T10 — Separate captains and screens.** Both move/aim/throw at once. Walk apart across a familiar area; each keeps their own camera and working world/audio, with no partner screen forced onto yours.
- [ ] **T11 — Shared Onions, separate squads.** Check that withdrawals/returns change the same Onion count. Both should get their own agreed allowance. Simultaneous requests must not duplicate Pikmin or lose stock.
- [ ] **T12 — Work, fight and recall.** Try carrying, a familiar enemy and a bridge/wall. Check normal whistle, Recall All and follower rescue affect the correct player's squad while the other player's workers keep their ownership.
- [ ] **T13 — Pause, travel and performance.** Test settings/shared pause, both-ready resume, group area travel, partner pings and a short familiar-area session with both squads. Report crashes, missing sounds, sluggish controls or excessive heat. No final-boss/ending test required.

## Later — disconnect and live reconnect

These use a disposable test campaign. I will explain each controlled interruption before you do it.

- [ ] **T20 — Raye loses connection.** Keep your host app open. Your world should pause without kicking you out; hers should show waiting. Restore the connection and check her same captain, squad, positions and jobs return after both are ready.
- [ ] **T21 — Host loses connection.** Keep the host app alive. Both should wait; after connection recovery, check the retained paused world resumes without restarting the day or duplicating anything.
- [ ] **T22 — Raye closes and reopens her app.** Host stays open. Rejoin the same player slot and check it restores her state instead of making another captain or resetting progress.
- [ ] **T23 — Phone interruptions.** When requested, test a brief screen lock/background-and-return. Check waiting/readiness messages and a deliberate resume, with no surprise attacks or stale queued throws.

## Later — mid-day saving and host-crash recovery

I must implement and verify complete mid-day checkpoints first. We will use backed-up disposable progress, not your main campaign. Until then, quitting returns to the actual last normal save and must clearly say so.

- [ ] **T30 — Save here and quit.** Save a small, recognizable mid-day situation, close both apps and reload. Compare day/time, collected progress, Onion/squad counts, captain positions and the specific work/fight state we recorded.
- [ ] **T31 — Host app closes unexpectedly.** After I confirm a recovery checkpoint exists, close/relaunch the host as instructed. Check the newest COMPLETE checkpoint is restored and that the displayed save age honestly explains any later lost progress.
- [ ] **T32 — Restore and backup screen.** Use a prepared test backup and confirm the right campaign/day is shown. I will handle file corruption/failed-write tests; you do not need to edit save files.

Guest-held emergency backups, automatic host switching and Continue alone need their own later test instructions. Do not assume they exist. If the host continues alone, a returning player rejoins the updated world rather than a frozen old moment.

## Later — PC and iPhone share one campaign

PC work follows the iPhone fundamentals. I will preserve the current PC installation and prepare the matching gameplay features; no PC setup changes requested now.

- [ ] **T40 — Choose the home setup.** At that stage, tell me whether you will use two PCs or one PC with local controllers, and which controls you prefer. No decision needed now.
- [ ] **T41 — PC to phone and back.** Use the supplied save/handoff controls, then compare the same campaign progress on the destination. Exact mid-day state is tested only once full checkpoints work. Repeat phone to PC.
- [ ] **T42 — Personal settings stay personal.** Confirm graphics, FPS, touch/controller layouts and volume remain right for each device while shared gameplay rules match. I will prepare any older-copy/conflict tests; no manual save-folder copying required from you.

## Later — internet play and Pikmin2

- [ ] **T50 — Different connections.** With a validated invite/connection method, try separate networks and mobile data when requested. Check joining, a brief interruption and reconnection. Being on the same Wi-Fi does not complete this test.
- [ ] **T51 — Longer ordinary play.** Play together in familiar areas and report real campaign problems as you encounter them. Short checks increase confidence; they do not certify an entire story.
- [ ] **T60 — Pikmin2's own test batch.** After its co-op adapter is ready, repeat the applicable tests plus caves/floor transitions, captain switching, audio and save/reload. Current working P2 is left alone meanwhile.

## Already confirmed — historical baseline

- [x] Original P1 opens and runs on both phones, per your earlier reports. This does not validate the new connection screen or full co-op.
- [x] Original P2 opens on both phones, per your earlier reports. This does not validate future P2 co-op.

## Results log

Connection/UI results are recorded below; actual shared gameplay/recovery tests remain future. I will record the exact build and phone result for each completed task. Keep failures and partial results visible rather than clearing them when a later build starts.

| Date | Task | Build / phones | What you observed | Status / next action |
|---|---|---|---|---|
| October25 | Checklist created | Existing working apps preserved | No new device test requested | Wait for verified update and a small active batch |
| October25 | T01 | Build62; your phone | Package staged and first-phone backup verified; installation not yet reported | IN PROGRESS; Raye backup/update next |

## How I maintain this list

- This repository file is the master: ios/USER_TESTING_CHECKLIST.md. Mirror it to Documents/Open Nectar/START HERE - What to Test.md and .txt whenever it changes.
- Before requesting your time, move only the relevant few tasks into Ready to test, name the exact verified build/file and give expected behavior. Use task IDs so your replies map to a clear result.
- Mark a task done only from your actual device observation or a directly observed device test. Compilation, logs from a different build, proposals and unit tests do not count as a hardware pass.
- Record partial/failing results, build, affected phone and next action. Reopen tasks only when a related change needs a retest; retain the earlier result in the log.
- Put technical checks, downloads, backups, logs, signing preparation and automated tests on my work list, not on yours. Tell you explicitly when you can close the game/unplug.
- Keep this checklist and its active-task summary linked from the project status, exact resume state and final ChatGPT handoff. Never silently change a future item into a claim of implemented behavior.

| October25,12:59 EDT | T01 | Build62; both phones | Own install user-reported complete; Raye pre-update backup verified5files/158975bytes | PARTIAL; Raye installation pending, networking/runtime untested |

October25 milestone: user reports both Build62 updates ready. T01 COMPLETE by user report; T02-T04 not yet tested.

October25 — T02 FAILED on both Build62 phones: false content mismatch from46 Unicode filename encodings. All3463 files byte-identical. Canonical NFC fix/native regression implemented; next Apple build and phone retest pending.

October25 — Build63 FAILED native Foundation regression (`hash valid fixture`), no IPA and no new phone test. Follow-up keeps all checks and adds labelled rejection stages plus consistent root/entry alias handling; native validation pending.

October25 —64 failed real socket mismatch rejection after native hash tests and app compile passed. Local delayed-close reproduction identified discarded final verdict; batch fix passes full networking and impaired/rejoin tests. Next Apple build pending; no new phone pass.

October25 —65 native compilation/package and actual simulator rejection/all5 mismatches/join/rejoin PASS; verified IPA staged. T01 ready for BOTH65 updates; T02-T04 actual phone results pending.62 failure history retained; no phone pass from CI.

October25 —65 TWO-PHONE LAN PASS: T01 both updates; T02 stable minute+/11ms minimum; T03 Leave/rejoin/reverse hosts; T04 normal solo/settings/controls. User confirms mismatch photo was older62. Host app-switch gameplay retention/internet/full co-op not tested. No new phone action now.

October25 — Next UI/efficiency batch implemented/local checks PASS; Apple/native/phone pending. Keep65 T01-T04 historical PASS. No new phone task until verified update.

October25 —66 failed BEFORE fixture compilation: strict-shell empty EXTRA flags array. Portable Python compiler runner replaces shell array; actual desktop/native fixtures PASS via real local compiler, including spaced paths. Next Apple build pending; T05/T07/T08 not ready/untested.65 T01-T04 LAN pass preserved.

October25 —67 compiler failure:3 legacy sprintf calls rejected by Apple SDK. All7 related title calls bounded; local old-API negative control and9 aggregate/gate tests PASS. Next native build collects independent errors while strict final packaging gate remains mandatory.65 LAN pass unchanged; no new phone task yet.

| October25 | T05/T07/T08 | Build68; both phones | Full native/preflight/package verification passed; update staged, actual phone tests not done | READY; user installs both and tests3 items |

| October25 | T05/T07/T08 | Build68 | User reports "all good so far, on the tests"; requested menu, remembered Rejoin and return checks accepted as overall limited pass | PASS user report; no new phone action; T10 waits real gameplay prototype |

October25 engineering: authenticated guest input + actual guest captain transform helpers implemented, local23 tests/real Windows loopback/actual adapter fixture/Clang PASS; Apple pending. Not yet connected to scene/controller/camera/UI; T10 remains FUTURE, no phone task. User reports68 gameplay heat also noticeably improved, cause unconfirmed. Keep68 installed.

October25 —69 full Apple/12 checks/simulator input+pause/package verified PASS; no install requested. New retained-link/native handoff/early-message queue/both-loaded area agreement implemented and local24 tests/real Windows encrypted probe/Clang6/ARC10/identity2 PASS, next Apple run pending. Actual disposable card+engine/camera/controller driver still missing; T10 remains future. Keep68 installed; no phone action.

October25 —70 attempt1 full game/preflight PASS; runtime simulator spawn timed out before observed main and basic diagnostics also timed out; noIPA. Same70 attempt2 already requested/in progress. New health runner guard locally15 tests PASS, saved for future source build [skip ci], not in executing retry. No phone action; keep68. T10 still future.

October25:70 attempt2 native/simulator/IPA PASS, identical binary to failed attempt1. New explicit PROCESS-LATCHED disk-backed temporary practice card actual-source test and Clang3 PASS, Apple next. No UI caller/area enabled. Future driver must drain CardUtil before teardown, abort on failed isolation and require restart before normal solo. Keep68; T10 remains FUTURE; no phone task.

October26:71 Apple actual-card/host fixture/full app/12 preflight PASS, simulator health timed out before native probe; no IPA. Owned simulator lifecycle + one setup-only recovery + early runtime + mandatory final evidence gate repair local26 tests PASS; next Apple pending. Keep68; T10 future; no phone/USB task.
