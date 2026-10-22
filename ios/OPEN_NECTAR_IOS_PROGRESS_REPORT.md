# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-22 17:36 EDT

**Overall project status:** P1 Build41 PASSED native compilation and IPA generation. Its unchanged IPA was downloaded, verified and staged in the accessible Documents install folder. Automatic follower-rescue PHONE VALIDATION PENDING. P2 preserved on working user-reported Build32.

### Pikmin 1

- Current objective: Phone-test the optional automatic rescue without disturbing working Pikmin or healthy followers.
- What was investigated: Actual Build41/run39854014424, source769880462e9b0b8d2d139e0404fad015a741709f, job120087366917 and artifact12458853453; metadata, executable architecture/platform, standard campaign markers, new rescue/recall diagnostics, icons and archive integrity.
- Root cause or leading hypothesis: Confirmed source defect corrected: mIsCStickNeutral could become false merely from formation separation, disabling our new recovery. Actual C-stick input now gates trail/edge/return behavior. Some map/crowd failures can remain; approved optional rescue observes~8 seconds stalled plus failed walking before a supported dry landing beside captain. Idle ship Pikmin ignoring Recall All remains undiagnosed.
- Files changed: Source76988046 added follower monitor/safe landing/cooldowns/settings row44/defaultOFF and actual-input guards in P1 Navi/Piki/ActCrowd, plus bounded diagnostics and tests. This milestone changes journals/checklist only; no further gameplay edits or new build required.
- Tests and results:128 route/recovery/rescue,24 surface,103 command/control/config,283 P1 and283 P2 stock-speed,58/58/7 campaign variants,39 bundle/config checks passed locally; Clang diagnostics passed. P1 CI host/iPhone checks and full native compile/link/package PASSED. Download ZIP digest matched GitHub; nested IPA CRC, bundle metadata/icons, unsigned ARM64 iPhoneOS executable, new feature markers and standard campaign verification PASSED. Phone behavior not tested.
- Confirmed working: Build41 compilation and IPA generation/structural verification. Previous user-passed readable menus, aim/soft assist/charge-whistle/save reload retained. Build40 installed navigation failure at100%/100% remains the prior runtime evidence.
- Remaining issues: New auto rescue unverified on real crossing; idle ship global-recall symptom unresolved; rare clam scene and full campaign unverified. No mid-day autosave or online feature implemented.

### Pikmin 2

- Current objective: Preserve user-reported working Build32; P2 development paused.
- What was investigated: No new P2 runtime issue. Shared P1-host rescue getter is hidden/disabled for P2; isolated actual getter returned0 without P1 globals.
- Root cause or leading hypothesis: No new P2 diagnosis.
- Files changed: No P2 game/audio changes this milestone.
- Tests and results: Prior shared bundle and283 stock-speed control checks passed. No P2 job requested in41.
- Confirmed working: User previously reported P2 working after audio fixes; installed baseline unchanged.
- Remaining issues: Broader solo tests later, then agreed shared co-op/snapshot work.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit:8aa0d0649f702405d7596b90ff646d1f64c21eca, clean; source for41 remains769880462e9b0b8d2d139e0404fad015a741709f.
- Latest local commit:8aa0d0649f702405d7596b90ff646d1f64c21eca
- Latest fetched remote commit:8aa0d0649f702405d7596b90ff646d1f64c21eca
- Commits created: No new gameplay commit; documentation-only ready/verification checkpoint being saved with[skip ci].
- Changes pushed: Source and dispatch notes already pushed; no repeat native build needed.
- Uncommitted changes: Only milestone documentation/checklist before its checkpoint commit; no private evidence staged.
- GitHub Actions run IDs:41=39854014424 SUCCESS, source769880462e9b0b8d2d139e0404fad015a741709f;40=39784525620;39=39666676388;38=39664622876;37=39617967156; P2 working32=39518825366.
- Build results:41 native/link/package PASS.40 native/link PASS, CI package FAIL(TIFF icons), local package recovery PASS, phone navigation FAIL.37 native/package PASS, phone pathing FAIL.41 also validates the final PNG restoration workflow introduced after40.
- Artifacts produced:artifact12458853453 nectar-pikmin1-experimental,5927421bytes, SHA256 f0877cfef326ba57a144d95b54872cc31dc47c97cba0547ef507b0a588a17396. Verified IPA: C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\Pikmin 1 - Build 41 - Automatic Follower Rescue.ipa, 2822189bytes, SHA256 cd359d0f475b8928bcef5290f6b04a592e8e78223d09150424b2e7b6a60e39b6. Bundleorg.opennectar.experimental.pikmin1, displayPikmin1, standard, unsigned ARM64 iPhoneOS; UUID399aeded-fc99-31ad-9bff-32c87a676b0d. Exact GitHub IPA unchanged. Prior IPAs/backups remain intact.

### Next steps

- Next Pikmin 1 task: Update existing P1 using the staged41 IPA and same Sideloadly account. Enable Advanced Settings > Cheats > Rescue Stuck Followers (defaultOFF). Keep Better PathfindingON, both speeds100%,60FPS. Leave workers on tasks; cross with following squad without Recall All. If stranded, wait10-15s on open dry ground away from enemies; check worker jobs, counts, movement and FPS. More time may be needed for large groups or unsafe landing conditions.
- Next Pikmin 2 task: Keep existing working app unchanged; no install now.
- GitHub/build task: None while waiting for focused phone feedback. Do not trigger/poll another build without a new reason.
- Anything requiring my involvement: Install/test when convenient. No uninstall/reset/asset reinstall. Phone can remain disconnected except during installation or a specifically requested report collection.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Automatic rescue is independent of Recall All, optional defaultOFF, following formation only; workers/idle/unassigned/fighters/unsafe states are excluded. It measures progress and failed walking, not distance alone. Clear dry supported landing and enemy/occupancy guards, four-attempts/sec shared budget,2s failed-spot retry and12s successful per-follower cooldown may delay it. Healthy followers should not relocate; this needs phone evidence.
- Important source-file locations: games/pikmin1/src/plugPikiKando/aiCrowd.cpp pcRecoverFollower; navi.cpp pcUpdateFollowTrail/callPikis/pcTakeFollowerRescueBudget; piki.cpp pcRescueFollowerNearCaptain; pc_port/pc_follow_trail.h PcStuckFollowerMonitor; pc_follow_surface.h pcFollowRescueSpot; settings key stuckFollowerRescue/row44. Current research/design ios/PIKMIN1_FOLLOWER_RECOVERY_DESIGN.md; focused test ios/PIKMIN1_CROSSING_RECALL_SPEED_TEST.md.
- Relevant logs: work/build41-run.json,build41-jobs.json,build41-artifacts.json,build41-verification.json,build41-artifact.zip; outputs/Build41-Pikmin1/ios-build.log. Accessible folder2 has full Build41 log and verification. Previous private phone collection work/p1-phone-feedback-2026-10-22 164225 read only settings/layout while game running; no navigation report found, no save backup claimed. Private video/hashed copies in folder2/P1 - Build40 Crossing Failure -2026-10-22(actual folder includes spaces).
- Unverified fixes:41 installation, actual rescue/physics/crowds/worker exclusion/performance and ignored idle Pikmin cause. No full-campaign certification. Tighter crossing queues, shared crossing segments and optional stranded/rescue HUD are proposals saved for later.
- Risks and warnings: Preserve app IDs/settings/saves/assets and normal day-end saving; no phone writes/uninstall/private uploads. Rescue does not revive or force idle-state transitions. Ground/enemy checks cannot promise every hazard covered. No finale spoilers. P4 internal AI is not claimed known.
- Exact next actions: User follows checklist; inspect feedback. If failures persist, request USB only for p1-navigation-report.txt and correlate reasons/coordinates before further edits; avoid repeated relaunches until collection if possible. Keep P2 paused. Future online co-op remains host-owned shared campaign with separate views/squads/shared Onion stock; synchronized transitions acceptable. Shared exact-scene persistence/reconnect foundation is later work, not in41.

**END PROGRESS REPORT**
