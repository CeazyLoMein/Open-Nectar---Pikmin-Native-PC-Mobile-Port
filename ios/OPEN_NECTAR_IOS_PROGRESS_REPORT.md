# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-22 18:15 EDT

**Overall project status:** P1 Build42 PASSED native compilation/linking and IPA generation. The unchanged GitHub IPA is locally verified and READY in the accessible Documents install folder. New normal-follow pacing and automatic teleport PHONE TESTS PENDING. P2 unchanged on working user-reported Build32.

### Pikmin 1

- Current objective: Install/test the verified42 update for responsive ordinary following, the same box descent and return pacing; keep genuine stuck/teleport validation separate.
- What was investigated:62.525-second1562x720 recording ScreenRecording_10-22-2026 17-42-21_1.mov,12 sampled frames/contact sheet, read-only live phone navigation/settings/layout, formation target mutation, return-intent activation, shared route budget and completed-route handling.
- Root cause or leading hypothesis: Confirmed source behaviors: (1) height/distance immediately set return intent and route takeover stopped followers while waiting for the two-searches/sec shared queue; (2) pcProtectFormationEdge changed the formation target to an old platform trail BEFORE its downward-descent return, retaining the wrong target; (3) a completed walking route was classified as a failed return, causing an extra stop/retry. These are strong explanations for the reported symptoms, not a proven explanation for every map behavior.
- Files changed: Gameplay source remains dbe796adb057d0d5c92b37ad9f5976143d5329ba: aiCrowd.cpp measured-stall route entry, downward target preservation, completed-route handoff and distant-assignment retention; two regression fixtures. This milestone changes documentation/checklist only; no new gameplay build required.
- Tests and results: 140 route/recovery/retention,105 command/edge/config and58/58/7 campaign scenarios plus Clang PASS locally; Build41 negative controls failed8+1 cases as intended. Build42 native compile/link/host and iPhoneSDK checks/IPA generation PASSED. Artifact SHA256 matched GitHub; IPA CRC, original app identity, ARM64 iPhoneOS unsigned binary, standard-campaign/new feature markers and six original PNG icons verified. Exact downloaded IPA unchanged. Phone runtime PENDING.
- Confirmed working: Read-only collection found rescueON, BetterPathfindingON, both speeds100%,60FPS, BluesOnlyWaterON. Three files read while game running; no phone writes or save backup claimed. Log records route_built, four recall_idle_seen/recall_joined samples, one rescued_follower and four rescue_no_safe_spot samples. Those bounded samples have no clip time correlation and do not establish the user's untested teleport behavior as verified.
- Remaining issues: New pacing has not been tested on the phone. Automatic teleport remains explicitly UNTESTED by user; one untimed prior log event is not a successful clip-correlated test. Ignored idle ship Pikmin remains undiagnosed; four sampled recall candidates joined but did not identify that individual. Rare clam scene/full campaign unverified; no mid-day autosave or network feature.

### Pikmin 2

- Current objective: Preserve working user-reported Build32 while P1 stabilizes.
- What was investigated: No new P2 investigation needed for P1-only AI pacing.
- Root cause or leading hypothesis: No new P2 diagnosis.
- Files changed: None in P2 or shared settings/graphics/audio.
- Tests and results: No new P2 build or hardware test; prior stock-speed/bundle controls remain recorded.
- Confirmed working: User reported prior P2 working after audio fixes; installed app untouched.
- Remaining issues: Broader solo testing later, followed by agreed co-op/snapshot work.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: a148acedf09d97e2f2c27ee4cdb88f750f19910b, clean and matched fetched origin before this result/verification milestone; Build42 source remains dbe796adb057d0d5c92b37ad9f5976143d5329ba.
- Latest local commit: a148acedf09d97e2f2c27ee4cdb88f750f19910b
- Latest fetched remote commit: a148acedf09d97e2f2c27ee4cdb88f750f19910b
- Build source: dbe796adb057d0d5c92b37ad9f5976143d5329ba
- Commits created/changes pushed: Pacing source and dispatch notes already pushed. This ready/verification documentation checkpoint follows with[skip ci]; no further game edits or redundant CI run.
- Uncommitted changes: Only current ready/verification journal and checklist before their documentation commit; private phone/video/IPA/log data never staged.
- GitHub Actions run IDs: 42=39861241129 SUCCESS, source dbe796adb057d0d5c92b37ad9f5976143d5329ba, job120112185245;41=39854014424 SUCCESS;40=39784525620;37=39617967156; P2 working32=39518825366.
- Build results: 42 native/link/IPA PASS; normal-follow pacing and teleport phone tests PENDING.41 native/link/IPA PASS but phone normal following too slow; teleport untested. P2 not rebuilt.
- Artifacts produced: Artifact12462533086 nectar-pikmin1-experimental,5928221bytes, SHA256f1f89f790de786444dfeb74da74f957c0afaa7a4b6faf23fbb36cea116db219c. Verified unchanged IPA: C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\Pikmin 1 - Build 42 - Smooth Following and Recovery.ipa, 2822527bytes, SHA256304ac9abd4c60d96d76eb95902a0716ab743a074b1c69003aad238f7f7efd6a1. Original bundleorg.opennectar.experimental.pikmin1, labelPikmin1, standard unsigned ARM64 iPhoneOS, UUIDb9bf7bf9-dff9-3cec-9c86-f52e6cf57e8a. All prior IPAs/backups preserved.

### Next steps

- Next Pikmin 1 task: Update existing P1 with the verified42 IPA in folder1 using the same Sideloadly account. Keep Better PathfindingON, Rescue Stuck FollowersON, both speeds100%,60FPS. Leave workers on safe tasks and test ordinary group movement, the same box crossing and running off it without Recall All. Watch pauses/detours; then separately test a genuine stalled follower only if one occurs.
- Next Pikmin 2 task: Preserve current app; no update.
- GitHub/build task: No build needed. Await focused phone feedback; inspect actual report if movement or rescue fails. No idle polling.
- Anything requiring my involvement: Install/test42 when convenient. Do not uninstall/reset/import assets. Phone can be disconnected after installation until a specifically requested report collection.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User's latest clarification overrides the earlier ambiguous “technically works”: none was clearly stuck long enough to test teleport; all eventually walked back too slowly. Do not claim auto-rescue phone PASS based on one untimed log event. Goal now is smooth ordinary following, not a shorter teleport timer or a faster global queue.
- Important source-file locations: aiCrowd.cpp pcProtectFormationEdge now returns BEFORE touching a target when captain is lower; pcRecoverFollower keeps distance/height return OWNERSHIP but permits ordinary movement until measured stall, starts a route only after stall, and hands completed routes back successfully; exec keeps a valid distant return assignment from being dropped during ordinary-follow handoff. Invalid slots still fail, excluded states reset ownership, original no-enhancement/multiplayer behavior retained.
- Relevant logs: work/build42-run.json,build42-jobs.json,build42-artifacts.json,build42-artifact.zip,build42-verification.json; outputs/Build42-Pikmin1/ios-build.log. Accessible folder2 has Build42 full log and verification. Private prior failure evidence is in folder2/P1 - Build41 Slow Following -2026-10-22(actual folder includes spaces), and work/p1-phone-feedback-2026-10-22 174902. Only report/settings/layout read while app running; no phone writes/save backup.
- Unverified fixes: 42 phone installation, normal following/box drop/group responsiveness/assignment retention, true stuck-only teleport and ignored idle Pikmin cause. Full campaign unverified. Safe landing, enemy proximity and occupancy can delay rescue. Normal movement speed values and teleport timer/search limits were unchanged.
- Risks and warnings: No phone writes/uninstall/reset/save changes/private uploads. P1 original app identity and normal saving retained. Ordinary descent follows stock movement; water safeguards remain. P2 unchanged. No finale spoilers. No online/autosave work added.
- Exact next actions: User installs staged42 and follows the focused checklist. Collect pacing feedback first; only mark teleport tested if a genuinely stalled follower visibly relocates safely. If failure, collect p1-navigation-report.txt before repeated relaunches and correlate evidence before more code edits. P2 stays paused. No new native build just for documentation. Future tighter crossing queues/HUD/online/shared exact-scene saving remain proposals, not features in42.

**END PROGRESS REPORT**
