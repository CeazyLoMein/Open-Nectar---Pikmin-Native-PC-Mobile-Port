# Your Open Nectar testing checklist

Updated October25,2026. This is the running list of things Chazz and Raye will eventually test. **Only the Ready to test section is an active request.** Everything in Later waits until I provide a working build and clear instructions.

I will give you a small batch at a time, prepare the files in Documents, handle logs/build checks myself, and tell you whether a phone must stay connected/open. When I need you, I will send a clear message and an audio alert where available. No need to stay connected or leave a game running unless I ask.

## Ready to test

**Nothing requested on either phone right now.** Keep your existing apps installed. I need to verify the next usable update before asking you to install or test it.

When a GitHub build is running, sending “passed” or “failed” is helpful. I will verify the actual result myself; a successful build does not tick off a phone test.

## Next batch — private-room connection (not ready yet)

- [ ] **T01 — Prepare both phones.** Have both available, unlocked and on the same Wi-Fi. I will prepare the verified update and exact file location. If signing/installing requires your input, I will give that one action; keep the existing app and its files.
- [ ] **T02 — Connect a private room.** On both phones, open gear > Data > Online Co-op: Connection Test and wait for the data check. Host on your phone, copy/share the code manually, return the host to P1, then paste/join on Raye's. Allow Local Network access if asked. Tell me the status on BOTH phones; a screenshot is useful if something fails.
- [ ] **T03 — Leave and reconnect.** Leave the room and join again, then try Raye hosting. We are checking the connection only; this screen does not start a shared campaign yet.
- [ ] **T04 — Return to normal P1.** Close the connection screen and confirm ordinary gameplay, controls, graphics and your settings still work on both phones.

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

New connection/gameplay/recovery tests have not yet been reported. I will record the exact build and phone result for each completed task. Keep failures and partial results visible rather than clearing them when a later build starts.

| Date | Task | Build / phones | What you observed | Status / next action |
|---|---|---|---|---|
| October25 | Checklist created | Existing working apps preserved | No new device test requested | Wait for verified update and a small active batch |

## How I maintain this list

- This repository file is the master: ios/USER_TESTING_CHECKLIST.md. Mirror it to Documents/Open Nectar/START HERE - What to Test.md and .txt whenever it changes.
- Before requesting your time, move only the relevant few tasks into Ready to test, name the exact verified build/file and give expected behavior. Use task IDs so your replies map to a clear result.
- Mark a task done only from your actual device observation or a directly observed device test. Compilation, logs from a different build, proposals and unit tests do not count as a hardware pass.
- Record partial/failing results, build, affected phone and next action. Reopen tasks only when a related change needs a retest; retain the earlier result in the log.
- Put technical checks, downloads, backups, logs, signing preparation and automated tests on my work list, not on yours. Tell you explicitly when you can close the game/unplug.
- Keep this checklist and its active-task summary linked from the project status, exact resume state and final ChatGPT handoff. Never silently change a future item into a claim of implemented behavior.
