# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-22 17:56 EDT

**Overall project status:** P1 Build41 compiled/packaged successfully, but user reports slow stop/start normal following, single-file returns and unnecessary detours after running off a box. User explicitly clarified automatic TELEPORT RESCUE HAS NOT BEEN TESTED; do not mark it successful. New pacing correction source/local checks PASS; Apple/IPA/phone pending. Build42/run39861241129, sourcedbe796adb057d0d5c92b37ad9f5976143d5329ba, last observedin_progress; no conclusion yet. P2 paused and preserved.

### Pikmin 1

- Current objective: Restore responsive ordinary following and deliberate ledge descents while retaining walking recovery and the separate optional stuck-only teleport.
- What was investigated:62.525-second1562x720 recording ScreenRecording_10-22-2026 17-42-21_1.mov,12 sampled frames/contact sheet, read-only live phone navigation/settings/layout, formation target mutation, return-intent activation, shared route budget and completed-route handling.
- Root cause or leading hypothesis: Confirmed source behaviors: (1) height/distance immediately set return intent and route takeover stopped followers while waiting for the two-searches/sec shared queue; (2) pcProtectFormationEdge changed the formation target to an old platform trail BEFORE its downward-descent return, retaining the wrong target; (3) a completed walking route was classified as a failed return, causing an extra stop/retry. These are strong explanations for the reported symptoms, not a proven explanation for every map behavior.
- Files changed: games/pikmin1/src/plugPikiKando/aiCrowd.cpp pcProtectFormationEdge/pcRecoverFollower/exec formation retention; tests/pikmin1_follow_routes_test.py and pikmin1_command_test.py; status/handoff/design/checklist. No teleport timer, search budget, speed scale or Recall All eligibility change.
- Tests and results:140 actual-method route/recovery/retention scenarios PASS;105 command/aim/edge/settings PASS;58/58/7 campaign variants PASS; Clang diagnostics PASS. Same new fixture with actual Build41 pcRecoverFollower produced8 failures; actual old pcProtectFormationEdge produced1 failure, confirming these tests detect the old slowdown/target defects. Existing24 surface/283+283 speed/39 bundle results remain prior PASS and were not unnecessarily repeated because those methods are unchanged. Full new Apple build/IPA/phone pending.
- Confirmed working: Read-only collection found rescueON, BetterPathfindingON, both speeds100%,60FPS, BluesOnlyWaterON. Three files read while game running; no phone writes or save backup claimed. Log records route_built, four recall_idle_seen/recall_joined samples, one rescued_follower and four rescue_no_safe_spot samples. Those bounded samples have no clip time correlation and do not establish the user's untested teleport behavior as verified.
- Remaining issues: New pacing has no phone result. User still needs a genuine stuck-follower teleport test. Ignored idle Pikmin near ship remains unconfirmed/unresolved: sampled recall candidates joined, but no evidence identifies the previously ignored individual. Full campaign and rare clam scene unverified. No mid-day autosave/network code.

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
- Starting commit:ca23d8a6de5e32a1933dfad5ca51d47f66c0e90a, clean and matched fetched origin before code edits.
- Latest local commit:dbe796adb057d0d5c92b37ad9f5976143d5329ba
- Latest fetched remote commit:dbe796adb057d0d5c92b37ad9f5976143d5329ba
- Build source:dbe796adb057d0d5c92b37ad9f5976143d5329ba
- Commits created/changes pushed:Scoped pacing source commit pushed; documentation-only dispatch record follows[skip ci].
- Uncommitted changes:Only this dispatch journal before its documentation commit; no private evidence staged.
- GitHub Actions run IDs:Build42/run39861241129, sourcedbe796adb057d0d5c92b37ad9f5976143d5329ba, last observedin_progress; no conclusion yet. Prior41=39854014424 SUCCESS/source769880462e9b0b8d2d139e0404fad015a741709f;40=39784525620;37=39617967156; P2 working32=39518825366.
- Build results:41 native/link/IPA PASS; phone normal-follow usability FAIL/too slow. Automatic teleport behavior UNVERIFIED per user clarification. New pacing Apple/IPA/phone pending.
- Artifacts produced:No new pacing IPA. Existing verified41 IPA retained in folder1, SHA256cd359d0f475b8928bcef5290f6b04a592e8e78223d09150424b2e7b6a60e39b6, original P1 app ID.35/37/40 backups and P2 baseline intact.

### Next steps

- Next Pikmin 1 task: Validate the new native build/package, stage verified original-ID IPA, then retest normal following, running off the same box and return pace before a separate genuine stuck/teleport test. Keep workers on jobs; avoid Recall All during the worker-preserving test.
- Next Pikmin 2 task: Preserve current app; no update.
- GitHub/build task:Build42/run39861241129, sourcedbe796adb057d0d5c92b37ad9f5976143d5329ba, last observedin_progress; no conclusion yet. No idle polling or redundant builds; user reports completion.
- Anything requiring my involvement: Nothing during build. Phone read finished; user may close P1/disconnect. New phone test only once the new IPA is verified and staged.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User's latest clarification overrides the earlier ambiguous “technically works”: none was clearly stuck long enough to test teleport; all eventually walked back too slowly. Do not claim auto-rescue phone PASS based on one untimed log event. Goal now is smooth ordinary following, not a shorter teleport timer or a faster global queue.
- Important source-file locations: aiCrowd.cpp pcProtectFormationEdge now returns BEFORE touching a target when captain is lower; pcRecoverFollower keeps distance/height return OWNERSHIP but permits ordinary movement until measured stall, starts a route only after stall, and hands completed routes back successfully; exec keeps a valid distant return assignment from being dropped during ordinary-follow handoff. Invalid slots still fail, excluded states reset ownership, original no-enhancement/multiplayer behavior retained.
- Relevant logs: C:\Users\chazz\Documents\Codex\2026-10-19\got-it-you-want-codex-to\work\p1-phone-feedback-2026-10-22 174902; private copied evidence C:\Users\chazz\Documents\Open Nectar\2 - Progress and ChatGPT Handoff\P1 - Build 41 Slow Following - 2026-10-22; outputs/P1-Build41-Slow-Recovery/D-contact.jpg. Local positive140/105 results and negative8+1 outputs. Prior build41 full logs/verification remain in folder2 and workspace.
- Unverified fixes: New pacing in real map/crowds, true stuck-only teleport, ignored idle Pikmin cause, full campaign. Safe-landing/collision/enemy guards can delay rescue. No claim every path or hazard handled.
- Risks and warnings: No phone writes/uninstall/reset/save changes/private uploads. P1 original app identity and normal saving retained. Ordinary descent follows stock movement; water safeguards remain. P2 unchanged. No finale spoilers. No online/autosave work added.
- Exact next actions: Review next native build after user reports completion; stage verified IPA in folder1, update README/checklist and notify. Test smooth box drop/group movement first; separately establish a true stuck case for teleport (rescueON,~8s stalled+failed walk, safe dry captain position). If it fails, collect bounded report before repeated relaunches. Tight crossing queues/stranded HUD remain future proposals; do not add them while resolving this slowdown.

**END PROGRESS REPORT**
