## Final corrective submission — 2026-10-30 20:38 EDT

- Local/remote correction source `123d8e27db819889cac59f6863a528dd4d16d53f`, fixture/workflow/documents only. Game code unchanged from PC9 source65595c53b1582c3316c92afefb19d7e37cd56c8b. Expected/shared identity `8ac920c968812b41679d6a3ec3e4875ab818189691367b1830e4124454f2d12c` independently recomputed and verified inside PC9 package.
- Replacement **iPhone94/run41151124155 IN_PROGRESS**: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/41151124155 . iPhone93/run41114720367 FAILED mandatory captain fixture despite actual native game BUILD SUCCEEDED. No failed IPA installation allowed.
- **PC9/run41114720301 SUCCESS**, artifact13005907278 downloaded/verified: ZIP SHA256 `a7872d324fa617949d77d827076bf5fc4b3b2fefb4a267f67dd8dcf23fdb82b2`, EXE SHA256 `056efccfb4d1884ce7ed79b94a4f0a16738625c148ea4141cd1a4e21ecfcbbf4`,14 receipt files, Windows x64 PE and imported dependency closure PASS. Extracted outputs/P1-Full-PC-Coop-Build9, NOT installed. Windows workflow10/run41151124251 intentionally SKIPPED; not a failed new Windows build.
- New captain fixture now compiles full actual adapter with current Navi state/property/effect seams and extra whistle lifecycle assertions. MSVC/W4/WX execute PASS and strict Clang PASS; six runner/receipt gate tests PASS. Required21 practice checks remain mandatory. Future Windows preflight includes full captain fixture too.
- Intended next pair is **PC9 + iPhone94**, with DIFFERENT commit metadata but identical verified game code identity. On94success verify exact head123d8e27, new package/receipts/real UIKit/scene, matching8ac920identity, then backup/stage both peers. Do not require source commit strings to match when test-only corrections are proven excluded from identity.
- Installed PC8/phone92 remains user-confirmed smooth with own SFX; unchanged this turn. No new game launch/input/close, phone/asset/settings/save writes. No user action now. Stop idle polling, await user94result. Full gameplay batch, unresolved runtime tests and co-op roadmap remain in complete handoff below.

---

## PC9 success; iPhone93 fixture correction

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-30 20:36 EDT

**Overall project status:** PC9 SUCCESS; iPhone93 FAILED only its captain test fixture and refused packaging. The actual iPhone game compiled successfully. Corrected test-only integration gap locally; replacement iPhone-only build next. Installed PC8/phone92 unchanged, user-confirmed smooth with own SFX. All new gameplay fixes remain hardware UNVERIFIED.

### Pikmin 1

- Current objective: package the already-compiled guest whistle/free-aim/independent-speed/owned-recall/host-Pikmin-speed batch with all mandatory checks passing.
- Investigation: authenticated full logs and jobs from iPhone93/run41114720367; failed step30, Require actual practice startup, view and authority checks before packaging. compile-captain and ios-captain failed because controlled captain fixture lacked NaviState.h/new visual members. run-captain blocked. Other practice fixtures and scene passed. Native game log contains BUILD SUCCEEDED. Packaging correctly refused the failed fixture; do not install partial failed artifact.
- Root cause: production captain_visuals gained NaviState/NaviMgr/UtEffect dependencies and whistle presentation methods, but older whole-translation-unit fixture wasn't expanded. Previous34 extracted feedback checks and real engine syntax checks covered different dependencies and didn't catch this stale fixture.
- Files changed this correction: tests/pikmin1_practice_captain_test.py now supplies controlled state/property/effect headers, new Navi fields/declarations and guest world symbols; compiles ENTIRE actual pc_coop_captain_visuals.cpp and adds checks for wire field application, capture/stop/radius, independent original effects, no repeated allocation, release and solo preservation. .github/workflows/windows-coop-experimental.yml now adds this same full captain fixture to future Windows preflight. No game/codec/asset/config/save modifications this correction.
- Tests/results: whole captain fixture MSVC/W4/WX compile+execute CAPTAIN VISUAL PASS, strict Clang syntax/analyzer PASS for actual adapter and fixture. Six practice runner/receipt gate tests PASS. Required21-check schema and packaging gate retained. Independent identity generation still8ac920c968812b41679d6a3ec3e4875ab818189691367b1830e4124454f2d12c,2922 tracked code/configuration files; test/workflow paths are excluded, proving game bytes match PC9. Prior batch31 CTest/34 feedback/236 smoothing/283 speed/110 command/20 PC-recall/actual capture checks retained, not rerun unnecessarily for test-only change.
- Confirmed working: user PC8/phone92 smooth movement and own whistle/Pikmin/footstep sounds; other captain sound kept local by preference. Enemy sound UNTESTED because practice contains no enemies. New PC9 source/game compilation passed; not installed or runtime tested yet.
- Remaining issues: replacement iPhone native gate/package completion and paired device tests for ring/aim/speed100 reset/owned recall/shared host Pikmin speed. Host force-close/durable mid-day recovery/live rejoin/campaign still unfinished.

### Pikmin 2

- Current objective: preserve accepted working app/audio; resume campaign/co-op later.
- Investigation/root cause/files changed: none.
- Tests/results: no new P2 build or runtime validation. Existing install untouched.
- Remaining issues: broader story coverage and eventual co-op after P1.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port ; branch ios-experimental.
- Starting local/remote664e6fc34ab187765ea09d05d526383c35eb91b6; clean, fetched, synchronized before changes. Game source for PC9 and failed phone93 is65595c53b1582c3316c92afefb19d7e37cd56c8b.
- PC9 run41114720301 SUCCESS; iPhone93 run41114720367 FAILURE. Exact logs in work/run-41114720367-current.json, jobs.json, logs.zip, logs/0_build (pikmin1).txt; all unique failures grouped above. Scene success. No new IPA produced/installed.
- Commits created/pushed/latest commit: correction pending commit; final submission/commit/run checkpoint in Exact Resume State.json. Only two implementation/test files above plus journal. No game code changes; PC9 can be reused with replacement iPhone IF final packaged identities match. Different metadata source commits will be expected; compare compiled code identity, not only commit strings.
- Uncommitted: fixture/workflow/journal correction until final checkpoint. No unrelated work.
- Artifacts: PC9 artifact metadata/package will be verified before staging. Failed phone93 artifact must not be used. Installed PC8 and phone92 remain accepted rollback baseline; PC7 backup preserved at Before PC Build 8 -20261030-110203. Full staging locations/hashes in earlier handoff below and Exact Resume State.json.

### Next steps

- P1: commit/push fixture correction with [ios-build] [ios-p1-update], WITHOUT [pc-coop-build]. Record replacement iPhone run ID once, then stop polling. Windows workflow may show skipped jobs; do not mistake this for a new Windows game build.
- GitHub/build: on successful replacement, retrieve logs/21 practice +13 room/real UIKit+scene receipts, verify unsigned ARM64 IPA/resources, exact expected code identity and existing PC9 package. Verify git diff from65595c53 contains only unhashed tests/workflows/docs. Stage matching pair after PC backup and closed-process check; do not close running games automatically.
- User involvement: none now, no phone/live session required. Report replacement iPhone result when ready. Later same-app update and test both rings/free aim/independent speed100 reset/owned Recall All/host Pikmin speed/pause. No enemy sound test in empty practice.
- P2: leave working app alone.

### ChatGPT continuation notes

- This correction is a stale TEST fixture, not a newly diagnosed game rendering crash. Native iPhone build93 actually compiled; final packaging blocked by its mandatory gate. Keep all gates enabled. No source reversion or smaller feature rollbacks needed.
- Relevant paths: tests/pikmin1_practice_captain_test.py; original actual adapter games/pikmin1/pc_port/netplay/pc_coop_captain_visuals.cpp; tests/run_pikmin1_practice_checks.py (unchanged,21 required checks); Windows workflow adds whole captain preflight. Local helpers work/repair_captain_fixture.py, check_captain_fixture_repair.cmd, check_captain_fixture_clang.cmd. Evidence work/captain-fixture-repair.log, captain-fixture-repair-clang.log, captain-fixture-runner-tests.log, captain-fixture-identity.h.
- Installed PC8/phone92 smooth/audio baseline, remaining user-reported issues and full previously implemented pending batch are preserved in the preceding complete handoff below. Current code uses input21bytes/captain schema3/63bytes; older installed pair cannot connect to new pair. PC9/replacement iPhone can match because this fix doesn't alter hashed game sources.
- Full vision remains queued: independent cameras/squads/settings, shared Onion stock/separate allowance, solo/shared campaign saves, health-led difficulty, synchronized cutscenes/travel, internet invitations/rejoin, durable exact mid-day recovery for lock/calls/host close, seamless PC/iPhone continuation and P2 later. Don't expand indefinitely; resolve confirmed test/runtime gaps first.
- Unverified: actual new pair rings/free aim/speed reset/owned Recall All/Pikmin speed, enemy audio, full story, host-close recovery. No new game launch/input/close, settings/save/phone install or asset writes.
- Exact next action: final checkpoint gives corrective source and replacement run. Wait for build result, verify genuine packages with same8ac920 identity and different expected source commits, then stage/test. No idle CI polling.

**END PROGRESS REPORT**

---

## Submitted PC9/iPhone93 guest feedback batch

**Submitted checkpoint (2026-10-30 15:23 EDT):** Game source `65595c53b1582c3316c92afefb19d7e37cd56c8b` committed/pushed to ios-experimental. PC9 run41114720301 and iPhone93 run41114720367 IN_PROGRESS; no new artifacts or hardware claims. Expected matching identity `8ac920c968812b41679d6a3ec3e4875ab818189691367b1830e4124454f2d12c` (VERSION_GPIE01_01). Installed PC8/phone92 remains unchanged and user-confirmed smooth with own SFX. Phone/log task finished; may close/disconnect. Documentation-only checkpoint follows, no extra build.

Full report follows in preceding implementation checkpoint; latest accessible copy in Documents/Open Nectar/2 - Progress and ChatGPT Handoff/LATEST - CODEX TO CHATGPT MASTER HANDOFF.md. Wait user build result, retrieve exact-head logs/packages/identity, then stage both peers. No new installation this turn.

---

## Guest feedback batch: whistle, free aim and speed/recall

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-30 15:21 EDT

**Overall project status:** User confirms installed PC8/iPhone92 is smooth and own whistle/Pikmin/footstep audio works. Enemy audio remains UNTESTED: current practice has no enemies. User prefers each captain's whistle/voices local; preserved. New guest visual/control/QOL batch implemented and locally verified, native paired build pending submission. No game closed, automated input, install/settings/assets/save writes or new phone request this turn.

### Pikmin 1

- Current objective: guest whistle rings, working iPhone free-aim drag, independent captain speed reset, and bounded existing Recall All/Pikmin-speed support.
- Investigation: read live PC practice1793374355 report (copied read-only to work/practice-pc8-phone92/pc-session.txt): approximately5ms RTT,8 neutral inputs in21904 host ticks, audio_sent283/dropped0, native audio_backend_state128. User may close games/disconnect. No guest USB read needed.
- Root causes: guest snapshots omitted whistle state/radius and replica never entered native whistle effects. Particle manager AND particle generator updates intentionally refuse guest presentation; forwarding state alone would still be invisible. Free aim assumed captain0 and local mouse deltas, never sent guest drag to host. Remote captain speed had no independent current preference in input; new path sends all selected percentages including100. Exact cause of user's prior apparent individual speed behavior not independently established; don't dismiss the observation. Recall/Pikmin speed deliberately had blanket multiplayer restrictions.
- Changes implemented: captain schema3/63bytes carries host whistle active/radius, validated finite/range. Original NaviWhistle/NaviFue effects are started/stopped per captain during guest rendering; radius/cursor interpolate, host modifiers determine displayed actual radius. Only four native whistle generator types are tagged, reset on pool reuse; guest-only particle loop advances these, recycles finished effects, bounds frame step and freezes during pause/background. General AI, geometry/simple particles and unrelated particle callbacks remain frozen. Factory/member declarations/native renderer path are included, not just a mock adapter.
- Controls: existing input format now21bytes including validated naviSpeedPct100/150/200/250/300/400/500. Aim-held bit16, cursor-delta bit32 multiplexes existing dx/dy at quarter-pixel precision; both axes accumulate between sends, expire after300ms, occur once and survive redundant delivery without repeating. Host projects guest screen drag through guest camera yaw, releases lock while free aim held and doesn't clear host mouse deltas. Existing successful clock/lead/hold and75ms smoothing delay retained. Speed preference is per captain, normal100 sent every sample too.
- Recall/Pikmin speed: one-shot Recall All bit64, existing host squad-ownership filter prevents taking partner's owned workers; each player enables their own dedicated button. Host need not enable local Recall All to honor guest's enabled request. Ordinary whistle range unchanged. Pikmin walking speed enabled as one HOST setting for both squads; guest row explains host control. Captain speed remains individual. Other local/competitive multiplayer, Hard and Speedrun restrictions retained. No new recall teleport/rescue/AI system.
- Tests/results:31/31 real network CTest PASS (after network-restricted invocation couldn't connect, rerun with authorized network passed all). Codec radius/flags/speed rejection,100% reset, both axes/held/release/expiry/no-repeat,120 existing timing/jitter combinations PASS.34 extracted ACTUAL guest whistle/captain/input/settings/particle-manager checks PASS with MSVC/W4/WX and strict Clang. Original native engine headers/translation units for captain visuals/runtime/Navi and effect manager/particle manager/generator/newPikiGame/settings syntax checks PASS; legacy warnings remain.236 smoothing,14 Ready/focus,8 carry,283 walking-speed/config,110 command/recall/cursor/edge,20 non-touch Recall All checks PASS. Actual capture/pool/300-Pikmin fixture including whistle field transport PASS, compile-out PASS. Both experimental workflows now require practice_feedback preflight. Native iPhone/PC package builds and hardware behavior for this batch NOT yet tested.
- Confirmed working: user PC8/phone92 smooth movement and own sounds; accepted graphics/touch/keyboards/120FPS/native pixels/low-detail Louie/GPI baseline preserved. Enemy audio untested. New effects/input fixes need real devices before marked fixed.
- Remaining issues: actual new pair visual/aim/speed/recall validation; host force-close/durable exact mid-day recovery/live rejoin still not implemented. Practice disposable, not full campaign, End/loss still restart. Main-story solo completion not proven. Save-solo-test separate from ordinary save retained.

### Pikmin 2

- Current objective: preserve user-confirmed working game/audio, later campaign testing/co-op.
- Investigation/root cause: none this turn. Shared net codec evolved for P1; no P2-specific source/app/device modification, no new P2 build requested.
- Tests/results: no new P2 runtime evidence. Existing accepted app untouched.
- Remaining issues: full campaign test and eventual P2 co-op after P1.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port ; branch ios-experimental.
- Starting local/remote6ac6bc8d3f7b09fdee419c3ad57968f46c65a69e, clean/fetched/synchronized before edits. Installed game source7720d26cb7c31c7bb8843c7d96e34bbc726eae59.
- Latest game commit / commits created / pushed: new batch pending commit; final source/run IDs will be recorded in Exact Resume State.json after submission. No unrelated edits.
- Uncommitted: scoped whistle/aim/speed/recall implementation, tests/workflow/journals. Preserve if interrupted; do not describe as hardware verified.
- Previous builds: PC8 run41070915761 SUCCESS/artifact12984489349; phone92 run41070915736 SUCCESS/artifact12986162794, scene12985201795, full packages independently verified/staged in prior checkpoint.
- Existing PC8 installed at Documents/Open Nectar/4 - Windows Version/Pikmin 1 - Full PC Co-op - Experimental, same PLAY PIKMIN1.cmd (actual filename PLAY PIKMIN 1.cmd). PC7 rollback Before PC Build8 -20261030-110203 (actual folder Before PC Build 8 - 20261030-110203).3199 protected settings/save/content hashes unchanged at that update.
- Existing phone92 staged at Documents/Open Nectar/1 - Install on iPhone/P1 Build 92 - Guest Movement and Audio/Pikmin 1 - Build 92.ipa, user now confirms installed/tested. SHA256b39285aadc7344cb496b6a3189dae80ee568df04a8bfe8aa008bc90c636284c1,5366883bytes, UUID0b3fe965-5974-3eb0-acd6-7e2f5f013722. PC8/phone92 shared identityd6d042250ff4364f8910f8418a856e03ddc5cb6f360659fe731be38602c23e96.

### Next steps

- P1: submit one matching PC/iPhone batch, stop idle polling, wait user completion feedback. Then strict exact-head artifact/native receipts/identity checks, PC backup/stage and same-app phone update. BOTH peers must update because input/captain layouts changed; mixed pairs should be rejected by build identity.
- P2: preserve accepted app.
- User involvement: none now; can close games/disconnect. Later test both normal whistle rings, free aim drag while stationary/walking, speed increase then100 on each player, own-squad Recall All with partner's Pikmin working, host Pikmin speed and pause/resume. Enemy sounds remain outside this empty practice's coverage. Do not ask for enemy sound test here.

### ChatGPT continuation notes

- Files: games/pikmin1/pc_port/netplay/pc_coop_captain_visuals.cpp, pc_coop_world.cpp, pc_coop_visual_smoothing.h, pc_coop_practice_input.h, pc_coop_practice_runtime.cpp/.h; original navi.cpp/Navi.h; original EffectMgr.h, zen/particle.h, effectMgr.cpp, particleManager.cpp, particleGenerator.cpp, newPikiGame.cpp; settings/pc_settings.cpp; libs/nectar_net input/replication codecs and tests. Guard new particle behavior with NECTAR_COOP_WORLD; do not globally reopen replica authority.
- New test tests/pikmin1_practice_feedback_test.py extracts actual methods, settings policy and particle update loop; workflow includes MSVC/macOS/iOS syntax. Existing solo command/recall/speed fixtures updated for practice seams, original expectations preserved. Tests do not prove rendered ring visibility or hardware input. Audio unchanged intentionally, own-only captain sound accepted by user.
- Evidence: work/feedback-net-ctest-authorized.log, feedback-checks.log, feedback-strict.log, feedback-capture.log, feedback-smoothing.log, feedback-actual-engine.log, feedback-actual-particles.log. Native .c test extraction/backend gates from7720d26c retained. No private recordings/game assets committed. Phone logs not needed for this diagnosis.
- Full mode vision remains COOP_OBJECTIVE_QUEUE.md / COOP_MIDDAY_RECOVERY_REQUIREMENTS.md: own screens/squads, shared Onion stock/separate allowances, solo/shared saves, health-led difficulty, synchronized cutscenes/travel, private internet invites/live reconnect, durable exact mid-day recovery for calls/lock/host force-close, seamless PC/iPhone continuation, P2 later. User wants finite progress: address confirmed issues, don't expand indefinitely. Percentage-first only when asked, not inflated by CI.
- Exact next action: after final source/run checkpoint, wait meaningful build result, verify/stage paired update, collect hardware evidence. Do not launch/close/control a user's running game or install a phone automatically. No new mod downloads, graphics/FPS or asset changes.

**END PROGRESS REPORT**

---

## PC8 and iPhone92 verified and staged

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-30 11:04 EDT

**Overall project status:** PC8 and iPhone92 both passed, downloaded and independently verified against authenticated GitHub artifact digests and shared source identity. PC8 installed with verified rollback; phone92 staged, NOT installed. No new device/runtime audio or movement validation yet. P2 unchanged. Next action is user same-app phone92 update followed by PC8/phone92 practice test.

### Pikmin 1

- Current objective: restore guest gameplay audio and reduce remaining cursor/camera judder; obtain actual paired runtime evidence.
- Investigation/root cause: user-tested PC7/phone91 made movement substantially smoother (subjective80% ->15% stutter), but guest heard music without gameplay SFX on PC/phone and phone/phone. Retrieved private reports read-only after user connected phone. Input neutral ticks were below1% on PC host; guest cue apply attempts were NOT proof of audibility. Confirmed production PIKI_USE_JAUDIO=1 uses original src/jaudio, whereas previous raw captain/system hooks were in fallback audio_stubs.cpp and compiled out. Previous fallback-only adapter test missed this integration gap.
- Changes implemented in7720d26c: ORIGINAL src/jaudio/piki_player.c and verysimple.c capture captain voice/whistle/footstep/formation/system commands with nested-call deduplication and local ownership filtering. pc_coop_audio.cpp/.h uses original native pause/unpause gates, coalesces ready calls, reports audio_backend_state (128=native plus numeric1=pause,2=demo). Runtime report includes this field. pc_coop_visual_smoothing.h and pc_coop_world.cpp interpolate/apply captain cursors with poses because camera reads that cursor; large changes snap. No new smoothing latency or input-clock rewrite. Preserve successful0296f6 clock/lead/hold correction.
- Tests:31/31 local CTest,234 smoothing,14 focus,8 carry,10 actual exit checks PASS; actual capture/pool/300-Pikmin lifecycle and cursor application PASS. Actual native entrypoint body extraction and explicit native adapter variant PASS; removing hooks caused six expected regression failures. Actual original engine translation units compile with production flag and real headers in Clang. CI confirmed original native backend, native entry test PASS on Windows and macOS/iOS syntax,26 native network/audio tests, full iPhone BUILD SUCCEEDED,21 practice/13 room checks all PASS, real encrypted UIKit simulator socket check and scene resume PASS with no health retry or cleanup errors.
- Confirmed working: previous user-tested movement improvement; host audio. This turn validates compilation, packaging, simulator and code checks only. PC8 installed without launching/input/closing game; all3199 current configs/save/content hashes unchanged. Existing PC assets junctions preserved. No phone settings/save/asset/install writes or new USB task.
- Remaining issues: verify guest sounds and residual stutter on new pair. Host force-close loses RAM authority/room; live rejoin and durable exact mid-day recovery are NOT implemented and remain mandatory. Practice is not a shared campaign and still needs restart after admitted End/loss. Solo unlocked test preset/save-solo-test remains separate from ordinary save; no full-story validation claimed.

### Pikmin 2

- Current objective: preserve user-confirmed working game/audio while P1 co-op is prioritized.
- Investigation/root cause/files changed: none this batch.
- Tests/results: no new P2 build or device test; previous user confirmation does not establish full-story coverage.
- Remaining issues: later campaign regression and co-op after P1.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port ; branch ios-experimental.
- Starting local a9cceb80cbf07619cbe4ece27e25083c897c740e, remote7720d26cb7c31c7bb8843c7d96e34bbc726eae59 (documentation push previously hit GitHub Internal Server Error). Game code was already pushed. New documentation-only checkpoint will push both safe normal commits; fetch/reconcile before push, no rewrite/force/main merge.
- Game/source commit: 7720d26cb7c31c7bb8843c7d96e34bbc726eae59. Shared PC8/iPhone92 identity d6d042250ff4364f8910f8418a856e03ddc5cb6f360659fe731be38602c23e96, independently matches generated local source identity (VERSION_GPIE01_01).
- PC8: run41070915761 SUCCESS, artifact12984489349; ZIP SHA256 ea15f7eadd25d00123f3ec9acd2cab9261e290946da4cc9642e29a7f747ab105; EXE SHA256 91955c6cd55b7d88ffc4e75b433e127eb06b1387d65014377c800c60507ad769. Verified14 receipt files, Windows x64 PE and full imported runtime dependency closure.
- iPhone92: run41070915736 SUCCESS, artifact12986162794; outer ZIP SHA256 569878a1aa33a30497a2aab9c8c336dc82c8b1a328260ce7d523ba0e80a6db0e; IPA 5366883bytes, SHA256 b39285aadc7344cb496b6a3189dae80ee568df04a8bfe8aa008bc90c636284c1, executable UUID 0b3fe965-5974-3eb0-acd6-7e2f5f013722. Unsigned ARM64 device platform, existing bundle ID org.opennectar.experimental.pikmin1/display Pikmin1, landscape, notices/approved icons verified. Real scene artifact12985201795 SHA256ca42a13c90170648c7604a16720af82b19ea1ea7e39e787817c0271b5c7d2b89, same process/single entry resume PASS.
- PC8 installed at Documents/Open Nectar/4 - Windows Version/Pikmin 1 - Full PC Co-op - Experimental; use SAME PLAY PIKMIN 1.cmd/shortcut. PC7 rollback: C:\Users\chazz\Documents\Open Nectar\4 - Windows Version\Pikmin 1 - Full PC Co-op - Experimental\Backups\Before PC Build 8 - 20261030-110203. All3199 protected files verified unchanged, no game launched. Receipt source/identity match packaged files.
- iPhone92 staged: C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\P1 Build 92 - Guest Movement and Audio\Pikmin 1 - Build 92.ipa. Package Verification.json, START HERE.txt and TEST CHECKLIST.txt alongside it. Same-app Sideloadly update required; do NOT uninstall or recopy assets. Raye's phone optional but also needs92 if used. Current phone remains user-tested91 until updated. No new installation claimed.
- Uncommitted: none after documentation checkpoint. Latest exact docs commit can be resolved from git log; build head remains7720d26c. No extra CI for docs.

### Next steps

- Pikmin1/user task: update own phone to92, use installed PC8, PC hosts NEW practice room, phone joins, enter and Ready each. No simultaneous tap required. Listen on GUEST for whistle/throw/Pikmin/footstep/enemy sounds; music alone fails. Compare body/cursor/camera judder. Pause on either side, then Ready both; verify sound/movement resume. Reverse roles if convenient. Report host and precisely which guest sounds remain absent. No USB needed unless new saved reports are requested. No host force-close recovery expected yet.
- Pikmin2: leave working app alone.
- GitHub/build: builds complete/verified; wait for meaningful runtime feedback, no redundant build or idle polling.
- Anything requiring user involvement: phone92 same-app installation and practice test. Full checklist: NEXT TEST - PC8 and iPhone92.txt in Documents/Open Nectar/2 - Progress and ChatGPT Handoff.

### ChatGPT continuation notes

- Native hooks are original src/jaudio/piki_player.c and verysimple.c, CMake compiles .c as C++ for this native build. Tests/pikmin1_native_audio_entry_test.py extracts real bodies; libs/nectar_net/tests/coop_audio_engine_test.cpp now also explicitly compiles PIKI_USE_JAUDIO=1. Fake track tests do not establish actual audible PCM. Preserve production audio/backend/receipt gates.
- Evidence: work/run-41070915761-current.json/artifacts.json/logs.zip and run-41070915736 equivalents, extracted logs folders, work/pair8_92-verification.log, windows-coop-build8-verification.json, build92-package-verification.json, pc8-iphone92-stage-result.json. work/verify_pair8_92.py and stage_pc8_iphone92.py reproducible scoped helpers. Original reports/recordings in work/practice-pc7-phone91 and private Downloads/Videos; sampled overview frames viewed, no full recording/audio listening claim. Do not commit proprietary assets/recordings.
- Preserve GPI textures, removed phone HD character packs, only original low-detail Louie restored on own phone (Raye may show two Olimars cosmetically); user-selected120FPS option/native pixel scaling/touch placement/keyboard fix/framebuffer fix. Do not change graphics/settings to diagnose role-dependent audio. P1 model performance previously A/B proven by user120FPS after HD Pikmin off.
- Full vision stays queued: independent screens/cameras/squads; shared Onion stock with separate allowances; solo/shared campaign save separation; mostly health-led difficulty; both-ready cutscenes/travel; private invitations over different networks; live reconnect; exact durable mid-day autosaves and host-loss recovery for calls/lock/accidental close; seamless PC/iPhone campaign continuation; P2 later. See COOP_OBJECTIVE_QUEUE.md and COOP_MIDDAY_RECOVERY_REQUIREMENTS.md. Current connection/practice is not finished campaign co-op. Percentage-first only when asked; do not inflate from CI passes.
- Exact next actions: user tests matching PC8/phone92; collect role-specific audio/movement result. If still silent, retrieve NEW guest report and inspect audio_backend_state, counts plus actual native event lifecycle/pause/listener before guessing. Host-close recovery remains a separately queued durable-save objective. Do not silently forget it.

**END PROGRESS REPORT**

---

## Submitted PC8/iPhone92 native audio and cursor batch — 2026-10-30 10:22 EDT

Game source/local/remote: `7720d26cb7c31c7bb8843c7d96e34bbc726eae59`. PC8 run **41070915761**, iPhone92 run **41070915736**, both IN_PROGRESS when submitted; no new artifacts, installation or hardware validation yet. Expected shared source identity `d6d042250ff4364f8910f8418a856e03ddc5cb6f360659fe731be38602c23e96` (VERSION_GPIE01_01).31 local CTest tests,234 smoothing assertions, actual original-engine entrypoint tests and negative control, native production-flag syntax checks, actual capture/lifecycle, focus/carry/exit checks PASS. Current installed PC7/phone91 has greatly improved movement but guest SFX still FAIL; native audio hooks correct a confirmed backend integration error. Host force-close recovery remains NOT implemented, queued with durable mid-day saves. Phone logs collected read-only, may unplug. Wait for user build-completion feedback; then retrieve exact-head logs/receipts, verify packages, back up/stage matching peers. No idle polling or extra documentation build. Full current report is in Documents/Open Nectar/2 - Progress and ChatGPT Handoff/LATEST - CODEX TO CHATGPT MASTER HANDOFF.md.

---

## Native audio integration correction; hardware movement improved — 2026-10-30 10:16 EDT

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-30 10:16 EDT

**Overall project status:** PC7/iPhone91 hardware feedback confirms a LARGE movement improvement (user estimates stutter80% ->15%, subjective) on PC/phone and phone/phone. Guest SFX still absent; host-close cannot resume the same in-memory practice room. Original-engine audio integration correction and cursor smoothing are implemented and locally verified; replacement builds NOT submitted yet. P2 unchanged. Phone reports collected read-only and user told they may unplug.

### Pikmin 1

- Current objective: restore guest gameplay sounds through the ACTUAL audio backend and reduce remaining presentation judder.
- What was investigated: new simultaneous recordings ScreenRecording_10-30-2026 00-05-30_1.mov and Base Profile2026.10.30 -00.05.28.05.mp4 (sampled frames viewed, metadata checked; full real-time motion/audio not independently listened to). Saved PC report1793333042 and phone guest1793333042/host1793333409, captured under work/practice-pc7-phone91/. Host PC41 neutral ticks /21648 total versus earlier roughly40%; guest records81 sound apply attempts,21 drops. Those counters do not prove audible output.
- Root cause: production full build compiles `PIKI_USE_JAUDIO=1` / original `src/jaudio`; previous raw voice/whistle/footstep/system hooks lived inside fallback `audio_stubs.cpp`'s !PIKI_USE_JAUDIO branch and were absent from the running game. Earlier adapter test used fallback defaults, so passing it missed this integration error. Positional hooks did send some cues, explaining guest apply attempts. Remaining positional/audibility behavior still needs hardware verification.
- Files changed: `games/pikmin1/src/jaudio/piki_player.c` and `verysimple.c` now capture original-engine captain/system commands with nested-call scopes and local captain ownership. `pc_coop_audio.cpp/.h` uses native pause/unpause system commands under PIKI_USE_JAUDIO=1, coalesces per-source ready voices, and exposes native pause/demo bits for reports. `pc_coop_practice_runtime.cpp` logs audio_backend_state (128=native;bit1 pause,bit2 demo). `pc_coop_visual_smoothing.h` and `pc_coop_world.cpp` interpolate and apply each captain's cursor with its pose, preserving visibility/metadata; large target changes snap. Camera code reads that cursor, which previously remained20Hz despite smoothed body positions. Tests/CMake/both experimental workflows updated to cover the actual backend.
- Tests and results:31/31 local CTest tests PASS, including new explicit PIKI_USE_JAUDIO=1 adapter variant, fallback adapter,120 authenticated timing/jitter combinations, real encrypted GNS/socket/room/stress/companion tests. Actual original-engine entrypoint bodies compile/execute against controlled fake tracks: native voice/whistle/footstep/formation/system start/stop, captain ownership, nested-command deduplication and native pause/resume gates PASS. Removing the six native hook blocks causes six expected regression failures. Strict MSVC/Clang entrypoint checks PASS. Actual original JAudio translation units plus runtime/adapter/soundMgr/seMgr compile in Clang with production PIKI_USE_JAUDIO=1 and real engine headers; existing legacy warnings remain, no errors.234 smoothing,14 focus,8 carry and10 actual exit checks PASS. Actual world capture/pool/300-Pikmin lifecycle fixture PASS, including applied cursor assertion and preserved authoritative health/ownership. These are code/adapter validations, not actual native PCM audibility or phone runtime proof.
- Confirmed working: user reports movement substantially smoother on both tested pair types; host movement/audio working. Accepted solo/graphics/touch/FPS/model/texture baseline preserved. No new game launch/input/close, graphics/settings/save/asset/phone writes.
- Remaining issues: guest sounds need the corrected paired build and device test; residual stutter needs reevaluation after cursor fix. Host process termination destroys current practice's in-memory authority and room; live rejoin/durable mid-day recovery are NOT implemented. User requires host-close recovery, so it stays queued with persistence, not marked fixed. Existing practice still needs app restart after End Practice/loss. Full shared campaign/Onions/jobs/cutscenes remain unfinished.

### Pikmin 2

- Current objective: preserve user-confirmed working build while P1 co-op is prioritized.
- What was investigated / root cause: no new P2 diagnosis.
- Files changed: none.
- Tests and results: no new P2 tests or build requested.
- Confirmed working: previously user-reported gameplay and repaired audio; no full-story validation.
- Remaining issues: broader campaign regression and eventual P2 co-op, after P1.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental.
- Starting local/remote:57c3403afb24b86e29f07f0db1ddf780dcbf58fb; fetched/synchronized and initially clean.
- Latest game source in installed PC7/phone91:0296f6a26e0600f3c66f0c8b6038a68c6ae3f3a5; identity31cb99e8cc7d34514117939becbc9465ce24ad08d441bc56bf643af2ec750141.
- Commits created / pushed: none yet for new batch. Intended subject `Wire native JAudio co-op cues and smooth guest cursor [ios-build] [ios-p1-update] [pc-coop-build]`. Resolve commit/run IDs after submission.
- Uncommitted: scoped native audio/cursor implementation/tests/workflows/journal, no unrelated work.
- GitHub Actions: existing PC7/run40988434328 SUCCESS, artifact12947874604; phone91/run40988434305 SUCCESS, P1 artifact12948319637 and scene12948820852. They passed compilation but guest audio FAILED hardware. No newer artifacts yet.
- Phone91 IPA5366580bytes SHA25667151b43afc883294af15d785641b3b179d5ce6bd15dbac98c56ef43a5d748f2, UUID5e077209-7b07-3a4f-a268-585d7435b1c4. PC7 EXE SHA25616e9821031cdb625050dfe05a04f553c94c55bc7581195b8f2044a705aac08e8.
- PC7 installed in Documents/Open Nectar/4 - Windows Version/Pikmin 1 - Full PC Co-op - Experimental; usual PLAY PIKMIN1.cmd (actual filename PLAY PIKMIN 1.cmd) remains. PC5 rollback is Backups/Before PC Build7 -20261029-230037 (actual folder `Before PC Build 7 - 20261029-230037`);3199 settings/save/content files hash-unchanged at update. No new installation this turn.

### Next steps

- Next Pikmin1 task: submit one matching native-audio/cursor PC+iPhone pair; after user build completion feedback retrieve full logs/receipts, validate artifacts/shared source identity, back up and stage without closing any running game.
- Next Pikmin2 task: preserve working build.
- GitHub/build task: record source/run IDs and stop polling while compiling. No build just for documentation.
- Anything requiring user involvement: NONE now; phone USB read is finished, may unplug. After verified updates, own PC+phone is sufficient: guest whistle, throw, Pikmin voices and footsteps; pause/resume; compare body/cursor/camera movement; reverse roles. Raye's second phone is optional. Do not uninstall P1 or recopy assets. No further live session requested now.

### ChatGPT continuation notes

- New native hooks are in ORIGINAL `src/jaudio/piki_player.c` and `verysimple.c`, not just fallback audio_stubs.cpp. CMake compiles these .c files as C++; guards keep non-PC/non-co-op builds unchanged. Do not revert the successful0296f6 input clock/lead/hold fix.
- New test `tests/pikmin1_native_audio_entry_test.py` extracts actual native bodies. Both experimental workflows now require it (MSVC and native/mac+iOS syntax). `libs/nectar_net/tests/coop_audio_engine_test.cpp` is compiled a second time with PIKI_USE_JAUDIO=1. Fake tracks validate routing/gates, not real waveform output. Preserve native package/runtime gates and21 practice/13 room receipt schemas.
- Logs/evidence: work/practice-pc7-phone91/ (PC session, copied phone reports, sampled PC/phone overview images); source recordings remain private in Downloads/Videos. Phone read originated work/practice-pc5-phone90/phone-read-095535 and was copied; don't mistake the historical parent folder for Build90 evidence. New logs native-audio-cursor-ctest.log, actual-native-audio-engine.log, native-entry-strict.log, native-audio-negative.log, native-audio-cursor-capture.log, native-audio-exit.log. No proprietary assets/recordings committed.
- Unverified: replacement native compilation/package/device sound; subjective remaining stutter. Cursor fix is targeted presentation work; no guarantee that it removes every source of judder. No broad network/simulation rewrite or extra smoothing latency was added.
- Risks/limits: native pause path must be tested on devices; report audio_backend_state128 expected while running unless native demo/pause is active. Applying a cue is not proof of audible output. Preserve original low-detail Louie/GPI selection and removed HD characters on phone, PC optional packs, user-selectable120FPS, sharp native resolution, framebuffer correction, settings and independent cosmetics/controls.
- Full vision remains queued: own-screen cameras and independent squads, shared Onion stock/separate field allowance, host campaign/solo save separation, health-led difficulty, synchronized cutscenes/travel, private internet invites, live rejoin, durable exact mid-day autosave/host-loss recovery for calls/lock/force close, seamless PC/iPhone continuation, P2 later. Current unlocked solo test preset uses save-solo-test; ordinary save preserved. No full-story proof or completed co-op claimed. User wants full-vision percentage first only when asking; do not inflate from build passes.
- Exact next actions: find final submitted source/run checkpoint in Exact Resume State.json; on build success, verify actual PIKI_USE_JAUDIO=1 compilation and native entry PASS plus26 native CMake tests, then staged same-app update of BOTH peers. Do not use old PC7 with new phone. Await movement/audio evidence before claiming fixed. Host-close recovery remains a separately tracked persistence objective.

**END PROGRESS REPORT**

---

## PC7/iPhone91 successful, verified and ready to test — 2026-10-29 23:03 EDT

Windows7/run40988434328 and iPhone91/run40988434305 both SUCCESS at source0296f6a26e0600f3c66f0c8b6038a68c6ae3f3a5. PC7 INSTALLED after verified PC5 backup;3199 protected config/save/content files unchanged. Phone91 IPA STAGED, not installed by Codex. Identity31cb99e8cc7d34514117939becbc9465ce24ad08d441bc56bf643af2ec750141 matches both packages and tracked source. Full25 native tests/21 practice/13 room receipts/real UIKit socket+scene resume passed. Hardware guest stutter/audio fix NOT YET tested. No more builds or polling; user next updates phone to91 then tests with usual PC launcher. P2 unchanged. Full current report follows; older status entries are historical.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-29 23:03 EDT

**Overall project status:** PC7 and iPhone91 both PASSED, full packages/identity verified. PC7 installed over the CLOSED PC5 after verified backup,3199 settings/save/content files hash-unchanged. Phone91 IPA staged in Documents; NOT installed by Codex. New guest movement/audio behavior is still awaiting hardware testing. P2 unchanged.

### Pikmin 1

- Current objective: verify smoother guest movement and audible guest gameplay sounds in online practice.
- What was investigated: live GitHub run/jobs/artifact metadata, full successful PC and native iOS build logs, unsigned IPA, Windows executable/dependencies, current tracked source identity, actual native receipts and real encrypted UIKit simulator results.
- Root cause / implemented fix: previous PC5/phone90 tests failed in the GUEST role on PC/phone and phone/phone: stutter plus music-only audio. Prior source investigation found host-clock aliasing / inadequate input lead/hold and no gameplay sound relay for the dormant guest AI. Source0296f6a2 implements250ms clock measurement,50ms scheduling padding, trusted-host bounded time-sized hold, ReliableNoNagle, and bounded host-owned positional/player/system/formation/footstep sound cues. Whistle coalescing, nested-command deduplication, local captain ownership, guest listener position, pause/resume/stop/loop cleanup, stale one-shot expiry and private diagnostics are included. No guest AI, framebuffer/graphics/FPS/pathing/settings/content changes.
- Files changed this verification/staging turn: journals and accessible guides/receipts; verified PC package files only. No new source fix or workflow change.
- Tests and results: both runs SUCCESS at EXACT source`0296f6a26e0600f3c66f0c8b6038a68c6ae3f3a5`. iOS full game BUILD SUCCEEDED;25 native CMake network/audio tests PASS;21 practice and13 room native receipt checks PASS; actual encrypted UIKit simulator probe PASS with health/main observation and no setup retry/cleanup errors; scene initial/resume each enter once with the same launch ID. Existing231 smoothing/14 focus/8 carry/10 exit regression outputs PASS. Local previous30-test suite includes real encrypted GNS tests and120 host/guest-rate/latency/jitter combinations; OLD-clock negative control failed10 cases. Package SHA256 matches authenticated GitHub artifact digests, IPA ARM64/device/unsigned identity/icons/licenses verified; PC14 receipt files/x64 PE/import closure verified. Both packages AND independently recomputed tracked source share `31cb99e8cc7d34514117939becbc9465ce24ad08d441bc56bf643af2ec750141` (2921 tracked code/config files).
- Confirmed working: user previously confirmed solo gameplay, sharper graphics, readable settings, camera/touch/keyboard fixes and improved pathing;120FPS after HD Pikmin removal. GPI texture retained, only original low-detail Louie restored on user's phone earlier. Old host practice ran smoothly and compatible peers connected. No new hardware/runtime claim for91/7, full campaign completion or completed campaign co-op.
- Remaining issues: hardware validation of guest stutter and SFX, reverse-role Windows Ready and interruption behavior. Full campaign world/Onions, travel/cutscenes, durable mid-day saves, exact live recovery, different-network testing and cross-progression remain queued.

### Pikmin 2

- Current objective: preserve user-confirmed working build while P1 is prioritized.
- What was investigated / root cause: no new investigation.
- Files changed: none.
- Tests and results: no new P2 tests/builds.
- Confirmed working: user-reported gameplay and repaired audio; no full-story completion verified.
- Remaining issues: broader gameplay regression and eventual online co-op after P1.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: `ios-experimental`.
- Starting local/remote: `0d259751fefdfbf11134e597cbb04e3d86e24b23`; fetched and synchronized, clean before journal edit.
- Latest GAME commit in both builds: `0296f6a26e0600f3c66f0c8b6038a68c6ae3f3a5`. Documentation-only verification checkpoint is being committed with `[skip ci]`; final latest local/remote and clean status are in Exact Resume State.json.
- Commits created this turn: documentation only, subject `Record verified PC7 and iPhone91 staging and test readiness [skip ci]`.
- Changes pushed: prior timing/audio source already pushed; this turn only verification journal, no extra build.
- Uncommitted changes: only this scoped journal checkpoint until commit; final clean state recorded after commit.
- Windows7: run40988434328 SUCCESS, artifact12947874604, ZIP SHA256`1f75f3661c9b1cb2535a85dede176b8fb421fd0c0fd721dabd25d71e95f956a4`, EXE SHA256`16e9821031cdb625050dfe05a04f553c94c55bc7581195b8f2044a705aac08e8`.
- iPhone91: run40988434305 SUCCESS, P1 artifact12948319637, ZIP SHA256`c20c6b89fa502439d1fcc49e257607a530828f13788d1069baf6b63d5b1be721`, IPA 5366580bytes SHA256`67151b43afc883294af15d785641b3b179d5ce6bd15dbac98c56ef43a5d748f2`, executable UUID`5e077209-7b07-3a4f-a268-585d7435b1c4`. Scene artifact12948820852 SHA256`f449984bf3adfe67b17816d36690ce74794e7a5367c3ef8e86edc73fb852b703`.
- Artifacts produced/staged: phone`C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\P1 Build 91 - Guest Movement and Audio\Pikmin 1 - Build 91.ipa` with START HERE/TEST CHECKLIST/Package Verification. PC installed at Documents/Open Nectar/4 - Windows Version/Pikmin1 - Full PC Co-op - Experimental (actual folder name is `Pikmin 1 - Full PC Co-op - Experimental`), same PLAY PIKMIN1.cmd launcher (actual filename `PLAY PIKMIN 1.cmd`).
- Backup: `C:\Users\chazz\Documents\Open Nectar\4 - Windows Version\Pikmin 1 - Full PC Co-op - Experimental\Backups\Before PC Build 7 - 20261029-230037`. All14 old package receipt files verified/copied before replacing;3199 current configs/saves/optional-content hashes unchanged after update. Existing asset junctions and launcher preserved. No game launched, closed or controlled.

### Next steps

- Next Pikmin1 task: user updates existing phone P1 with91 through Sideloadly, uses installed PC7 and tests same-Wi-Fi practice. No second phone needed initially.
- Next Pikmin2 task: retain working version.
- GitHub/build task: no new build or CI polling needed. Retrieve actual new runtime reports only after feedback; do not invent another fix before seeing results.
- Anything requiring user involvement: close P1 on phone, install the staged IPA over the same app/signing identity, then PC-host/phone-guest movement and whistle/throw/Pikmin/footstep audio, pause/Ready both, and reverse roles if convenient. Do not uninstall or recopy game assets. Phone USB is not needed for the Wi-Fi test. Both peers MUST be updated;91 is incompatible with PC5. Raye remains optional; if testing her phone too it also needs91. Her missing optional Louie means two Olimars, not a network fault.

### ChatGPT continuation notes

- Exact current state: verified installed PC7 + staged NOT automatically installed phone91, both native builds passed, hardware still pending. Most recent reported hardware problems came from PC5/phone90; do not confuse those with91/7 results. Preserve P2 and all user options.
- Important source files: games/pikmin1/pc_port/netplay/pc_coop_practice_input.h, pc_coop_practice_runtime.cpp, pc_coop_audio.h/.cpp; src/plugPikiKando/soundMgr.cpp, seMgr.cpp; pc_port/dolphin_stubs/audio_stubs.cpp and audio/pc_audio_source.h; libs/nectar_net/coop_session/protocol/input/gns_transport and coop_audio.h. Full file paths are relative to C:/Dev/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Relevant logs: workspace work/build91-p1-full.log, windows7-full.log, pair7-91-verification.log, windows-coop-build7-verification.json, build91-package-verification.json, pc7-iphone91-stage-result.json. Old hardware reports/recordings preserved under work/practice-pc5-phone90/. No recordings/proprietary game data committed.
- Unverified fixes: ALL new visual/audio behavior needs hardware evidence; simulator and fake-backend adapter tests do not prove device audibility or smoothness.
- Risks/limits: disposable practice only,16 positional sound voices, no fully shared campaign, automatic live rejoin or durable mid-day recovery. End Practice/admitted scene/lost link still requires app restart. Phone91 still carries the earlier unlocked solo test preset using separate save-solo-test; ordinary save is preserved. Do not relock/delete saves or claim normal new-campaign final release. Original iOS framebuffer fix stays intact. User wants120FPS available and independent visual/control/camera settings.
- Upstream1.1.1 was already reviewed Oct29; no bulk merge. See ios/UPSTREAM_AUDIT_2026_10_29.md. GL uniform cache remains a separate possible optimization. Avoid overwriting native resolution defaults/control indices with upstream PC/Android choices.
- Full co-op vision retained in ios/COOP_OBJECTIVE_QUEUE.md and COOP_MIDDAY_RECOVERY_REQUIREMENTS.md: own-screen cameras/independent squads, shared Onion inventory and separate field allowance, host shared campaign/solo save separation, health-led difficulty, travel/cutscene agreement, private invites/internet, reconnect/host-loss protection, durable exact mid-day autosaves, mixed PC/iPhone play and continuation, P2 later. Do not inflate percentage from passing builds; user requests full-vision percentage-first only when asked.
- Exact resumption: wait for91/7 test feedback. If not installed yet, point to staged IPA and ordinary PC launcher. If a symptom remains, establish host/guest/builds/actions and inspect saved reports with new host_hz/actor_age/target/hold/audio_sent/audio_played/audio_dropped counters. Never send game input, close a game, alter a phone or change graphics merely to test a hypothesis.

**END PROGRESS REPORT**

---

## Matching guest timing/audio builds submitted — 2026-10-29 21:54 EDT

Committed and pushed `0296f6a26e0600f3c66f0c8b6038a68c6ae3f3a5` to `ios-experimental`, based on synchronized local/remote`21480b5bfcba7e8f0ebc18e58c38de2f65d34070`. Tree clean after source commit. This is the source included in BOTH replacements:

- iPhone **91**, run **40988434305**, last checked **IN_PROGRESS**: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40988434305
- Windows **7**, run **40988434328**, last checked **IN_PROGRESS**: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40988434328

No new artifacts/IPA yet; no successful native compilation or new phone runtime result claimed. Installed PC5/iPhone90 stay untouched. P2 unchanged. Stop CI polling and await the user's completion report, then fetch full logs/receipts, verify BOTH packages/identity, stage in Documents and offer one short mixed PC+phone practice test. A second phone is optional. Phone USB work is complete and it may be unplugged.

Local validation:30/30 network/codec/session/engine-adapter tests passed including real encrypted sockets;120 host/guest-rate/latency/jitter combinations pass, old-clock negative control fails10 combinations. New source also coalesces sustained whistle/ready requests and prevents duplicate nested native sound commands; actual adapter regression PASS. Actual5 engine translation units pass Clang syntax/analysis with existing legacy warnings; strict new adapter/codec analysis and existing231 smoothing/14 focus/8 carry/10 exit checks pass. The new audio fixture uses fake playback resources; it does not prove audibility on iOS. Full report below provides exact scope, remaining co-op vision and verification limits.

**Exact next action:** user says build finished -> inspect project GitHub logs yourself; correct actual failures if any, otherwise validate/stage matching Windows7/iPhone91; same-app updates preserve settings/saves/texture packs. Do not reuse PC5 with phone91. User should compare guest movement and whistle/throw/Pikmin/footstep audio, then pause/resume and reverse roles. No need to keep a live game open while builds run. Next-test checklist is in Documents/Open Nectar/2 - Progress and ChatGPT Handoff/NEXT TEST - PC7 and iPhone91.txt.

---

## Guest timing/audio batch locally verified — 2026-10-29 21:46 EDT

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-29 21:46 EDT

**Overall project status:** PC5/iPhone90 compile/package successfully but FAILED guest movement/audio hardware testing. A coordinated replacement is implemented and locally verified; native GitHub compilation, package generation and real-device behavior are still pending. This update supersedes the earlier ready-for-test status.

### Pikmin 1

- Current objective: smooth guest movement and restore guest gameplay sound in disposable online practice, preserving working solo, settings, packs and saves.
- What was investigated: user-supplied simultaneous PC/phone and phone/phone recordings, PC session log and four latest phone reports collected read-only. On both pairs the host is smooth while the guest stutters and hears only music. Raye's two Olimars are her missing optional Louie model, unrelated to authority/network identity.
- Root cause or leading hypothesis: the old input helper measures consecutive20Hz picture arrivals, which can alias against a30/60/120Hz guest and underestimate a fast host. Only16ms scheduling padding and a fixed6-host-tick hold allow regular neutral gaps. Reports show190Hz PC host with about40% neutral guest input, and120Hz phone host with about50%, despite3–9ms reported RTT. Actual authenticated-session reproductions demonstrated timing starvation. Guest AI is intentionally dormant and no host gameplay sound events were delivered, so local music plays while voices/effects do not. These are concrete source findings; remaining visual stutter on hardware is not ruled out.
- Files changed: practice input/runtime, trusted host input hold, reliable GNS send flags; new `pc_coop_audio.h/.cpp` and `nectar_net/coop_audio.h`; CoopSession/protocol; central `soundMgr.cpp`, `seMgr.cpp`, `audio_stubs.cpp`, `pc_audio_source.h`; CMake and regression fixtures; journals. No framebuffer/graphics/FPS/AI/pathing/P2/settings/content changes.
- Implemented movement changes: cumulative250ms host-clock window;50ms command lead; trusted-host rate-sized approximately150ms continuous-input hold, hard bounded; reliable ordered encrypted messages use ReliableNoNagle. One-shot controls still do not repeat, stale transient actions still expire, and pause revisions clear input.
- Implemented audio changes: bounded host-owned cues over the existing authenticated compatible scene/session; spatial start/stop/move/release, player voices/whistle, system gameplay cues, formation and footsteps. Capture before host-local captain filtering. Guest uses its own listening position and local original sound assets. Opaque emitter tokens,16 positional voices,24 cues/packet,256 queue bound, malformed/role/revision/replay rejection; pause freezes host effects and clears guest voices, resume restores active positional loops, and old one-shots expire by receipt age and newer picture frame. Guest load-time contexts cannot overwrite replayed audio. Normal solo capture stays inactive.
- Tests and results: full30-test CTest suite PASSED, including real encrypted loopback/GNS room/stress/companion tests;120 independent host30/60/120/190/240Hz versus guest30/60/120Hz / latency2/8/16/24ms / jitter0/12ms authenticated-session combinations pass continuous movement, release, hold bound and readiness. Replacing the helper with the OLD clock causes10 starvation failures, proving sensitivity. Actual audio adapter exercised with narrow fake playback/session resources; actual session delivery tested separately. Codec truncation/range/NaN/ownership/overflow, sound position/stop/release/pause/loop and stale-catch-up tests pass.231 existing smoothing,14 actual Windows Ready/focus,8 carry-goal and10 actual exit/cleanup checks pass. Six practice runner orchestration tests pass. Actual five touched engine translation units pass Clang syntax/analysis with real engine headers, with existing legacy warnings; strict new adapter/codec fixture analysis passes. No native iPhone compilation or hardware result exists for this batch yet.
- Confirmed working: USER confirms ordinary P1 gameplay, clear settings, camera/touch/keyboard fixes and better pathing. User confirms120FPS with HD Pikmin removed; GPI retained, original low-detail Louie restored and phone-readback verified earlier. PC5 host smooth, both old practice peers connect with independent cosmetic packs. Neither a full campaign playthrough nor completed online campaign is claimed.
- Remaining issues: replacement hardware test; possible residual guest presentation latency/stutter; full shared world/Onion/progress and campaign integration; main-menu polish; cutscenes/travel; durable mid-day save/recovery and live rejoin; different-network play; seamless PC/iPhone continuation. Existing practice requires app restart after ending/admitted scene or lost link. Don't describe it as completed campaign co-op.

### Pikmin 2

- Current objective: preserve user-confirmed working build while P1 online practice is prioritized.
- What was investigated: no new P2 work in this batch.
- Root cause or leading hypothesis: no new diagnosis.
- Files changed: none.
- Tests and results: no new P2 build/runtime tests.
- Confirmed working: user previously reported P2 gameplay and restored audio working; a full-story completion is not verified.
- Remaining issues: broader campaign regression and eventual P2 online co-op after P1.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: `ios-experimental`.
- Starting/local/remote commit before this batch: `21480b5bfcba7e8f0ebc18e58c38de2f65d34070`; origin fetched and reconciled, no remote divergence.
- Latest game source in INSTALLED pair: PC5 `deaaee1ee0b884c5c939f456b6a5ccfff4d23d40`; phone90 `dcfba41f178d0e8905c215b4d668da67e1f43939` (test-only correction, same game identity).
- Commits created / changes pushed for new batch: not yet at report creation; commit subject `Fix guest input starvation and deliver practice gameplay audio [ios-build] [ios-p1-update] [pc-coop-build]`. Resolved commit/run IDs will be appended after submission.
- Uncommitted changes: only the scoped timing/audio/tests/journal batch; no user work overwritten.
- Existing GitHub Actions run IDs: PC5 `40976294203` SUCCESS/artifact`12943316091`; iPhone90 `40978326061` SUCCESS/artifact`12945005446`. Windows6 intentionally skipped. No replacement artifacts yet.
- Existing verified pair identity: `26204c2b52dcf03c59c52798930a69a9e11a4a6c9272600e9c7a8eb29e650f9e`. New game source changes identity: update BOTH peers once matching replacements are verified.
- Existing IPA: `Documents/Open Nectar/1 - Install on iPhone/P1 Build90 - Full PC Co-op Pair` (actual folder has `Build 90`); SHA256`63b75ed059cf288da64fd99c7992a19c36f7dfe24f8411237a025e60735683d8`.
- Existing PC EXE SHA256`d93bd8dcc7f80b46dc31e7767595940b9c352773f1da80fd401a48dcae831d9a`; launcher remains `Documents/Open Nectar/4 - Windows Version/Pikmin 1 - Full PC Co-op - Experimental/PLAY PIKMIN 1.cmd`.

### Next steps

- Next Pikmin1 task: submit one matching PC/iPhone build; after success inspect full logs/receipts/identity/packages before staging. Preserve all required checks. Do not install unverified artifacts.
- Next Pikmin2 task: retain current working version.
- GitHub/build task: record new commit and run IDs; wait for user completion feedback instead of polling CI.
- Anything requiring user involvement: nothing during compilation; phone may be unplugged. Later update both peers and compare guest movement, whistle/throw/Pikmin/footsteps, pause/resume and reverse host roles with PC+phone first; Raye is optional for that mixed test. No promise that a compile proves the symptoms fixed.

### ChatGPT continuation notes

- Important source-file locations: `games/pikmin1/pc_port/netplay/pc_coop_practice_input.h`, `pc_coop_practice_runtime.cpp`, `pc_coop_audio.h/.cpp`; `games/pikmin1/src/plugPikiKando/soundMgr.cpp`, `seMgr.cpp`; `pc_port/dolphin_stubs/audio_stubs.cpp`, `audio/pc_audio_source.h`; `libs/nectar_net/include/nectar_net/coop_audio.h`, `coop_session.h`, `input.h`; `libs/nectar_net/src/coop_session.cpp`, `gns_transport.cpp`, `protocol.cpp`.
- Relevant private logs: workspace `work/practice-pc5-phone90/` including `phone-read-210428`, PC reports and protected recordings. Test logs `work/guest-batch-final-ctest.log`, `guest-jitter-result.log`, `guest-timing-negative.log`, `guest-final-engine-check2.log`, `guest-audio-strict-final.log`, `guest-batch-exit-check.log`. No proprietary assets/recordings committed.
- Unverified fixes: all NEW timing/audio changes need full native builds and hardware validation. Audio backend fixture proves adapter calls/cleanup, not audibility on iOS. Low reported RTT does not measure all queue/pump delay; NoNagle is a latency reduction, not a proven sole root cause.
- Risks:16-emitter prototype capacity and high-latency sound behavior need real testing; changes do not synchronize enemies/jobs/items/cutscenes/campaign state or implement mid-day saves/live recovery. Do not enable guest AI to produce sound. Preserve separate ordinary `save` and unlocked `save-solo-test`; this is still a solo-update testing profile. No model/FPS/graphics changes needed for network test.
- Upstream:1.1.1 Oct29 reviewed earlier, main`14a922a9`, no bulk merge. See `ios/UPSTREAM_AUDIT_2026_10_29.md`; possible GL uniform cache is separate work, not in this batch. Keep iOS framebuffer/native pixels. New control indices collide with Recall All, reconcile before any adoption.
- Full vision stays queued: separate own-screen cameras/squads, shared Onion stock with separate squad allowances, shared host campaign with solo/co-op save separation, mostly health-based difficulty, both-ready cutscenes/travel, private invites/internet, independent graphics/camera/controls/cosmetics, durable mid-day autosaves with exact reconnect and host-loss protection, PC/iPhone cross progression, P2 later. User wants percentage-first progress for the full vision; previous conditional40% was not earned by the failed old test. No new percentage claim here.
- Exact next actions: confirm new submitted run identities from the checkpoint below / Exact Resume State.json; on user build result, retrieve full project logs yourself, correct actual compiler output if needed, then strict package verification, accessible staging, same-app update with backups, and short mixed-device test. Never idle poll, close a game or send automated game input.

**END PROGRESS REPORT**

---

## PC5/iPhone90 hardware feedback; guest timing/audio batch IN PROGRESS

Both PC-host/phone-guest and phone-host/phone-guest reproduce: host movement smooth, guest movement stutters, guest hears music but no gameplay SFX. This supersedes the earlier ready-for-test checkpoint. Original Louie is restored only on the user's phone; Raye's fallback Olimar is cosmetic.

Read-only current phone reports collected into work/practice-pc5-phone90/phone-read-210428; both videos preserved privately in that evidence folder. No game input, process close, save/config/content writes or P2 changes. Phone may be unplugged. PC host report: about190 logical ticks/sec and40% neutral guest input; phone host120 ticks/sec and about50% neutral, despite3-9ms reported RTT. Controlled actual authenticated CoopSession repro demonstrates guest rate aliasing / insufficient command lead can cause matching starvation. Guest presentation also lacks host audio-event delivery because its AI is intentionally not simulated. These are source findings, not yet proof of a complete runtime fix.

Uncommitted timing changes: 250ms cumulative host-rate measurement, 50ms input lead, trusted-host time-sized bounded hold, reliable NoNagle transport. Audio relay and regression tests still being implemented. Do not submit a timing-only partial build. Early local suite:22/28 pass; timing test expectations require updating for intentional lead changes;5 real-socket tests could not connect under restricted execution and require a permitted network rerun. No new build submitted, installed pair stays PC5/iPhone90. Starting local/remote commit21480b5bfcba7e8f0ebc18e58c38de2f65d34070; no new commits or pushes yet.

Next: finish bounded host-owned audio cues, test ownership/positions/stops/pause/replay, validate independent-rate input matrix and actual source fixtures, then one matching PC+iPhone build. Preserve native framebuffer, graphics/input preferences, solo-update save isolation and all existing mandatory native/socket/package gates. No hardware result claimed for unbuilt changes.

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

## Original Louie restored — 2026-10-29 20:01 EDT

Completed the user's approved content-only restoration on their connected phone, with P1 confirmed closed. Restored ONLY the340588-byte original low-detail `Load/Models/Louie/louie.nhm`; phone read-back SHA256 `c61f484c955e3944dded7535efe8bedd91214454a86620a343ec79842c16bf8d` matches the verified private backup. `Load/Models` contains only Louie. All HD character models remain removed. The existing GPI texture selection/content was retained; full textures were not rehashed this time. Current config was backed up locally and on the phone before replacement; the final config was read back and matches the original with only `hdModelsDisabled=63` changed to61. No app update, save write, PC/P2 change or automatic game input.

Backup: Documents/Open Nectar/5 - Backups and Older Files/P1 Before Character Removal and Build88 -20261029-153051 (actual existing folder is `P1 Before Character Removal and Build 88 - 20261029-153051`), config `Before Original Louie-195955.conf`; machine-readable result in work/original-louie-restored.json. Phone may be disconnected and P1 reopened. Louie's in-game appearance is still NOT runtime-tested. Previous statements that restoration is pending are historical and superseded by this entry.

Gameplay source remains deaaee1ee0b884c5c939f456b6a5ccfff4d23d40. PC5/run40976294203 and iPhone89/run40976294072 were last observed IN_PROGRESS; this phone-only action did not check their final result. Await completion feedback, then verify full logs/receipts and matching artifacts before updating clients. No new build needed for restoring this optional model.

---

## Paired fix build submitted — 2026-10-29 19:56 EDT

Source `deaaee1ee0b884c5c939f456b6a5ccfff4d23d40` pushed. Windows **5**: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40976294203 ; iPhone **89**: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40976294072 . Both last observed IN_PROGRESS, no final result/new artifacts yet.231 smoothing +14 actual focus +8 carry assertions and actual adapter/view/authority/strict frontend/Clang checks passed locally. Preserve installed PC4/phone88; wait for the user to report build completion, then verify full logs/receipts before staging BOTH clients. No idle CI polling. Original Louie restore approved but pending USB/P1 closed. Upstream1.1.1 reviewed, not merged; see UPSTREAM_AUDIT_2026_10_29.md. P2 unchanged. The latest full report is at the end of this journal and in Documents/Open Nectar/2 - Progress and ChatGPT Handoff.

---

## Current checkpoint — 2026-10-29 19:53 EDT: PC4/iPhone88 hardware feedback and coordinated fix batch

This entry supersedes older current-state claims below. Matching PC4/iPhone88 were installed and tested. PC host runs smoothly locally; phone guest actor movement stutters, reverse-role Windows Ready sticks, and PC log records missing-Onion `zannnen` panic. Guest arrival-time visual smoothing, Windows focus/Ready ordering and safe missing carry destinations are implemented and locally verified; new native builds are pending. Original low-detail Louie restore is approved but NOT done (no USB device detected; no phone writes). P2 unchanged. Read the newest full progress report at the end of this file, UPSTREAM_AUDIT_2026_10_29.md and Documents/Open Nectar/2 - Progress and ChatGPT Handoff/Exact Resume State.json for resolved commits/run IDs. Do not install unverified packages or merge all upstream files. Preserve PC4/phone88 as rollback and all save/graphics/control preferences.

---

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

2026-10-27 11:51 EDT. Current checkpoint: actual guest Pikmin visual population, sampled animation and render integration; local PASS, Apple/phone validation deferred. No next native build dispatched.

1. Repository: C:/Dev/Open-Nectar---Pikmin-Native-PC-Mobile-Port; fork CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; branch ios-experimental.
2. Revisions: parent/local/remote at start 6699108ac4ae81a0b23dcf7bb976ccbf509abc5a; checkpoint subject `Integrate guest Pikmin populations and host-sampled poses [skip ci]`; final accessible Exact Resume State.json resolves the post-push hash.
3. Working tree: this report is committed with the source batch; inspect status on resume and consult exact accessible final state. Never overwrite unrelated changes.
4. P1: installed68 retained. Prior solo/connection/menu limited tests accepted; no full campaign completion claim. Latest native76 covers earlier source0ced5bbe only.
5. P2: last user-confirmed working launch/gameplay/audio retained; no game edits/update or test this batch.
6. Fixes: actual dormant visual pool admission, full atomic guest population replacement, additions/removals/color changes without local gameplay birth/death, pool/scene lifetime invalidation, two-channel host pose capture/codec/apply, event-free local HD/original body/leaf draw, held BaseShape matrix/AnimContext timing correction.
7. Not implemented: complete enemies/items/Onions/jobs/HUD/world/captain/cursor state; actual room/game-thread area/input driver; playable Start/Ready; live durable saving or internet/cross-progression/P2 adapter.
8. Functions: pc_coop_world_prepare_guest_visuals/apply_guest_visuals/draw_guest_pikmin; PikiMgr::pcCoopVisualSlots/SlotsValid; ViewPiki::pcCoopVisualReady/Validate/Apply/Draw; PikiMgr::refresh; BaseShape::updateAnim/AnimContext::animate. Host capture now samples upper/lower mCurrentAnimID and mAnimationCounter.
9. Tests: MSVC actual adapter/pool/300 records/compile-out and actual visual implementation PASS; Clang/core analyzer PASS; old view/authority PASS;6 runner/gate tests;24 rebuilt core/network tests + real encrypted socket/bootstrap/input probe PASS; malformed final pose-wire test PASS;2 negative controls correctly fail. Full engine/Apple/phone remains untested.
10. Latest Actions:76/run40393742757/source0ced5bbe83504842602cd03872409dc584065169, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40393742757.
11. Results:76 SUCCESS and75 SUCCESS. No77 triggered. Earlier71–73 were repaired native test-harness failures; not current game compiler/runtime evidence.
12. IPA: no new IPA. Private76 outputs/Build76-Pikmin1/Nectar-pikmin1-unsigned.ipa5299633bytes SHA25666ad7aa47f99465874fb676ae1c815fd709782a63df1e1785d3acd621ab7ba16; UUID484f4c5d-796c-3b1e-b78c-60544382fced; unsignedARM64iPhoneOS, artifact12686618220. Keep68 installed;65/54 rollback retained.
13. iPhone: no new hardware test; both working apps retained. Earlier LAN connection, reversed hosting and native connection UI checks accepted; real shared gameplay/internet are not verified.
14. Unresolved: world load/asset coverage, owner-thread handoff/input/server tick loop, complete world/HUD/captain state, interpolation and actual mobile graphics/performance.
15. Supporting findings: normal Piki::doKill changes work/death counts and can leave a sprout; AnimMgr::findAnim can load from disk; old BaseShape presentation guard only recognized legacy lockstep. New display path avoids normal death/init/FSM/animation events and uses a pure loaded-asset lookup, with all incoming values checked first.
16. Resume details: Pikmin visual schema2 is50bytes (was schema1/38); local pose frame bounded against actual loaded animation, exact end marker clamped to last valid frame. Dormant display objects never enter PikiMgr live count/allowance; incoming metadata supplies ownership. Keep same-build/content handshake, personal graphics/FPS120/camera/audio/control/touch and optional HD packs independent. Driver must fully load the world before confirming Ready, pump while held, and use authoritative host ticks rather than render serials. Temporary card admission remains process-latched; restart before normal solo after practice.
17. User actions: none now. No phone connection/reinstall requested. Next test should be a concrete two-phone shared area with a short checklist.
18. Exact next work: inspect tree/origin and this report; integrate trusted practice area/assets, complete world baseline and owner-thread room/bootstrap/input/server loop; keep Start closed until it is truthful; require17 native practice checks plus existing full build/network/package gates for one larger milestone. Then two-phone LAN gameplay test. Later campaign main-menu Host/Join/Rejoin, separate solo/shared slots, shared Onion stock/own squads/allowances, forced shared travel, health-based difficulty, safe disconnect/rejoin and durable recovery, internet, PC/iPhone progression and P2. Preserve existing progress and finale surprise.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-27 11:51 EDT

**Overall project status:** Working installed P1/P2 retained. Continued the larger shared-area integration with actual guest population/animation/render code. Local checks passed; no new native build or phone test. Latest successful native build remains76. Playable two-phone gameplay is not enabled yet.

### Pikmin 1

- Current objective: complete the host-owned shared practice area with independent full-screen views and controls.
- What was investigated: actual PikiMgr pool/create/refresh, Piki init/death side effects, ViewPiki model/animation contexts, AnimMgr lazy loading, BaseShape/AnimContext render-time clocks, host capture and complete actor frames.
- Root cause or leading hypothesis: ordinary guest birth/death would replay gameplay effects/counters/seeds; a fixed local cohort cannot display host population changes. Normal animation selection can load assets or run gameplay callbacks. BaseShape previously treated only legacy two-pass rendering as presentation, so a held snapshot guest could still advance a separate animation clock.
- Files changed: pc_coop_world.h/.cpp/hooks; NEW pc_coop_pikmin_visuals.cpp; PikiMgr.h/ViewPiki.h, pikiMgr.cpp and shapeBase.cpp; PikminState wire codec/tests; CMake source list and actual-source fixtures/check runner; journals.
- Source changes implemented: explicitly admit a completely dormant initialized local PikiMgr pool; keep all slots OUTSIDE its live population. Complete host snapshots atomically choose local display slots for new, retained, removed and recolored Pikmin. Validate all IDs/session/epoch/captains/capacity/resources/poses before any actor/model write. Removed IDs disappear without normal kill, death statistics, sprout creation or work interruption. Pool/scene reuse invalidates ownership and suppresses stale normal rendering. Guest display directly samples both host animation channels with listeners disabled; no FSM/action/animation events run. Per-device original or installed HD body/leaf models draw locally. Held shape clocks stay frozen and use presentation matrices even outside old deterministic netplay.
- Tests and results: actual adapter plus actual pool admission/300-Pikmin multipart fixture MSVC PASS; compile-out PASS; new actual visual translation unit/resource/render fixture MSVC and Clang/core analyzer PASS; actual world TU/fixture Clang PASS; prior authority/view regressions PASS;6 mandatory-check runner tests PASS. Rebuilt networking24/24 PASS plus real encrypted socket/room/bootstrap/input probe PASS with normal localhost access. Final malformed pose-wire regression PASS. Two deliberately broken controls compile and correctly fail (skip final pose validation; remove end-frame clamp).
- Confirmed working: these are LOCAL source fixtures, not real phone visuals. Build68 remains installed and user-accepted for prior solo/connection/menu tests. Build76 native/package success validates its earlier source, not this batch.
- Remaining issues: full world baseline still needs enemies/items/Onions/jobs/HUD/interaction state; actual owner-thread room/load/input driver is incomplete. Captain animation/health/full cursor state and smooth render interpolation remain pending. The new guest display population intentionally contains no live AI/jobs; host gameplay input must drive the real host population. Trusted scene loading must ensure required animation data is loaded; packet-selected missing data rejects atomically and NEVER starts disk loading. No playable Start exposed.

### Pikmin 2

- Current objective: preserve its last user-confirmed working build while P1 online integration continues.
- What was investigated: no P2 runtime/source investigation in this batch.
- Root cause or leading hypothesis: none new.
- Files changed: no P2 game files. Shared networking Pikmin visual schema advanced from1/38bytes to2/50bytes; no P2 update/build or multiplayer adapter enabled.
- Tests and results: no new P2 build or phone test.
- Confirmed working: last user-confirmed launch/gameplay and repaired audio retained; full campaign completion remains unverified.
- Remaining issues: later stronger campaign testing and P2 online adapter.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental.
- Starting commit: 6699108ac4ae81a0b23dcf7bb976ccbf509abc5a; fetched origin still matched before saving this batch.
- Latest commit: this checkpoint is saved with subject `Integrate guest Pikmin populations and host-sampled poses [skip ci]`. Its resolved post-push hash is recorded in the accessible Exact Resume State.json.
- Commits created: one scoped population/pose/render/schema/test/journal checkpoint, with [skip ci].
- Changes pushed: normal development checkpoint only, no release/history rewrite.
- Uncommitted changes: batch is saved with this report; final accessible state records post-commit status.
- GitHub Actions run IDs: last independently verified native run40393742757 / Build76 / source0ced5bbe83504842602cd03872409dc584065169.
- Build results:76 SUCCESS. This batch has NOT had Apple/full-engine compilation or hardware validation. No77 requested.
- Artifacts produced: none new. Private Build76 IPA5299633bytes SHA25666ad7aa47f99465874fb676ae1c815fd709782a63df1e1785d3acd621ab7ba16, artifact12686618220; keep installed68 and65/54 rollback.

### Next steps

- Next Pikmin 1 task: integrate the complete bounded practice world and owner-thread room/bootstrap/area/input driver with this population renderer. Confirm all required world state and assets before Ready. Keep host simulation tick independent of phone rendering, including120FPS option.
- Next Pikmin 2 task: preserve baseline now; deeper testing and its online adapter later.
- GitHub/build task: continue meaningful related integration batches and local regressions. The next native build must require all17 admission/view/authority/population checks, full game build, existing room/socket gates and packaging checks. Do not build each helper separately.
- Anything requiring my involvement: nothing now; no USB/reinstall/new phone test. Keep working apps installed.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: guest visual lifecycle and host-sampled Pikmin pose paths now exist in actual engine code. They are NOT a complete gameplay replica or room driver. Fixed live-cohort adapter remains a separate diagnostic path and cannot mix with dormant display mode.
- Important source-file locations: pc_coop_world_prepare_guest_visuals/apply_guest_visuals/draw_guest_pikmin; PikiMgr::pcCoopVisualSlots/SlotsValid; ViewPiki::pcCoopVisualReady/Validate/Apply/Draw in new pc_coop_pikmin_visuals.cpp; PikiMgr::refresh dispatch; BaseShape::updateAnim and AnimContext::animate in shapeBase.cpp. New tests/pikmin1_practice_population_test.py compiles the actual visual TU with controlled engine resources; capture fixture compiles actual world TU and actual admission method bodies.
- Relevant logs: workspace work/population-capture.log, population-visual-local.log, population-world-clang.log, population-visual-clang.log, population-network-suite.log, population-protocol-final.log, population-authority-regression.log, population-runner-tests.log, population-negative-controls.json. Previous76 log/receipt retained.
- Unverified fixes: full Apple/game compilation, actual appearance/animation/performance on phones, loaded animation coverage, full shared world and gameplay. Local HD fallback test does not prove phone pack rendering.
- Risks and warnings: wire schema2 is50bytes; schema1/38bytes is refused. Same-build/content room compatibility remains required while personal graphics/camera/audio/controls/touch/cosmetic models stay local. Explicit guest display admission requires no live or pending-destruction Piki slots; do not abandon a loaded local job to force it through. Never call normal Piki::doKill/initColor/setFlower for these replicas. All applies/draws and scene teardown run on the owning game thread. Clear context before heap/shape reset. Pool capacity refusal must not silently drop actors. No network-triggered lazy asset loading.
- Exact next actions: verify status/origin; inspect this batch; trace trusted practice loading to ensure empty guest pool and complete assets, then connect room ownership/bootstrap/load barrier/input/server ticks and complete world adapters. Use actual-source checks before one meaningful native build. Preserve separate solo/shared save slots, shared Onion stock, own squads/allowances, safe host pause/exact rejoin, durable recovery and PC cross-progression/internet/P2 objectives. Restart remains required after process-latched temporary practice card admission. No finale spoilers.

**END PROGRESS REPORT**


---

## Historical checkpoints — current entry above supersedes current-state claims below

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

2026-10-27 11:13 EDT. Latest checkpoint: host/guest engine authority plus held-world camera and replica model integration. No new iOS build has been triggered.

1. **Repository/branch:** C:/Dev/Open-Nectar---Pikmin-Native-PC-Mobile-Port; CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; ios-experimental.
2. **Revisions:** fetched local/origin parent 5d6d4b9169b63630f599a6a76628d59b27cc27b4; this source/test/journal checkpoint has subject `Hold replicated co-op worlds across engine update and draw [skip ci]`. Exact resolved post-push revisions are in Documents/Open Nectar/2 - Progress and ChatGPT Handoff/Exact Resume State.json and its latest report.
3. **Working tree:** this entry is committed with the scoped batch; always inspect git status on resume. Never overwrite another session's work. No binaries/proprietary assets are included.
4. **P1:** installed Build68 retained. User-accepted solo/connection UI baseline; campaign completion not proven. Latest native Build76 verifies fixed-cohort captain/Pikmin apply, not playable online gameplay. New authority batch is local-only verification.
5. **P2:** last user-confirmed working launch/gameplay/audio retained; no changes or new tests this batch.
6. **Implemented:** explicit host running latch defaults held; invalidated guest remains non-authoritative; engine frame phase before update; clock/Node/AI/mode/message/timer guards; local controller and own camera updates while held; cursor/input-log side-effect guards; guest maturity mesh sync; held mouth drawing cannot change replica position.
7. **Proposed but not implemented:** dynamic replica spawning/removal/conversion/animation/jobs, complete world baseline, live room/game-thread transfer, network gameplay input, playable Start UI. Do not treat an assembled ActorFrame as the full world.
8. **Functions/files:** pc_coop_world_may_advance/has_guest/set_host_running; PlugPikiApp::idle; NewPikiGameSetupSection::update/draw; GameCoreSection::update/updateAI/pcUpdateCoopHeldView; PcamCamera::control; ViewPiki::refresh. Contract/compile-out hooks in pc_coop_world_hooks.h; independent presentation in pc_netplay_present.
9. **Validation:** actual-source controlled fixtures PASS under MSVC strict; Clang/core analyzer PASS;300-actor packet fixture and compile-out PASS;6 runner/gate tests PASS;2 negative controls correctly detect removed guards.20 pure network tests PASS in restricted execution;4 encrypted localhost tests fail there but PASS unchanged with normal access. No new Apple/full-engine/hardware validation.
10. **Latest native run:**76 /40393742757 / source0ced5bbe83504842602cd03872409dc584065169 / https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40393742757.
11. **Native results:**76 SUCCESS (scene job121821186343; P1 job121828968175).75 SUCCESS. Earlier71–73 test-runner failures were repaired before74; do not diagnose them as current gameplay/compiler failures.
12. **IPA:**76 private outputs/Build76-Pikmin1/Nectar-pikmin1-unsigned.ipa,5299633bytes SHA25666ad7aa47f99465874fb676ae1c815fd709782a63df1e1785d3acd621ab7ba16, UUID484f4c5d-796c-3b1e-b78c-60544382fced, unsignedARM64iPhoneOS, artifact12686618220. No new IPA. Preserve68/65/54 rollback.
13. **Phone results:** no new phone test. Existing68 limited menus/rejoin/return tests accepted; user reported heat improvement. Same-Wi-Fi connection previously passed, including reversed host. Internet play and actual shared-area gameplay unverified.
14. **Unresolved:** world lifecycle/animation/AI callback audit, world/HUD/interaction state, driver/thread/controls/load barriers, hardware validation. No automatic durable live save or host migration.
15. **Next supported fixes:** Piki::doKill has gameplay side effects (seed creation/death/work counters), so add explicit replica lifecycle/visual cleanup rather than running normal death twice. ViewPiki::setFlower can apply local All Flowers cheat; new render mesh sync avoids that. Keep host tick independent of phone render rate.
16. **Resume details:** local tools/receipts in workspace work/. Protected card admission drains worker under its queue lock and is process-latched; ending a practice run requires restart before normal solo. Match accepted session/epoch and pump session while paused. Independent view does not complete the full world. Native check runner now requires13 receipts (admission/view/authority), not9; all are mandatory before packaging.
17. **User involvement:** none now; no USB required. Do not ask for another phone reinstall until there is a concrete integrated shared-area test with exact steps.
18. **Exact development sequence:** inspect current tree/origin; extend population/lifecycle/visual baseline with tests; wire room ownership/bootstrap/loading/input to actual engine; expose truthful Start/Ready only after complete bounded practice world; run local batch checks; then one P1 native build and targeted two-phone test. Next stages: campaign main-menu flow and separate solo/shared slots, shared Onion stock/own squads/allowances, host pause and exact live rejoin, crash recovery/mid-day saves, internet reachability, PC/iPhone cross-progression, P2. Preserve personal views/settings and no finale spoilers.

The full milestone progress report follows, then dated historical records.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-27 11:13 EDT

**Overall project status:** Working installed P1/P2 baselines preserved. Build76 passed native compilation and packaging; the larger next integration batch is in source and locally checked. No Build77 dispatched. Real two-phone shared-area gameplay remains unfinished; the current phone screen is still a connection test.

### Pikmin 1

- Current objective: one host-owned shared practice world, each phone with its own full-screen camera and controls, before campaign co-op.
- What was investigated: actual PlugPikiApp frame loop, NewPikiGame update/draw/mode flow, GameCoreSection update/AI/cameras, Pcam camera-to-cursor writes, ViewPiki maturity/attachment rendering, and existing host/guest lifetime adapter.
- Root cause or leading hypothesis: stopping updateAI alone would leave a guest advancing clock/Node updates, movie/mode callbacks and gameplay messages in drawing. Camera controls also write gameplay cursor state. Applying mHappa alone leaves its displayed leaf/bud/flower model stale. These are source findings, not newly reproduced phone bugs.
- Files changed: games/pikmin1/pc_port/netplay/pc_coop_world.h/.cpp, pc_coop_world_hooks.h, pc_netplay_present.h/.cpp; include/GameCoreSection.h; src/plugPikiColin/plugPiki.cpp and newPikiGame.cpp; src/plugPikiKando/gameCoreSection.cpp and viewPiki.cpp; src/plugPikiNakata/pcamcamera.cpp; actual-source fixtures/mandatory practice-check runner and descriptions.
- Source changes implemented: admitted hosts start held, and only a matching session/epoch can grant running after readiness. Guests stay held even after invalidated bindings; they cannot obtain host authority. The actual frame enters presentation before update, known gameplay update/draw/mode/message paths are gated, and local controllers/own camera remain available. Camera recenter/drag cannot write authoritative aiming/input while held. Guest maturity selects the matching local model without invoking the local All Flowers cheat. Mouth attachment drawing cannot overwrite a held replica's position.
- Tests and results: strict MSVC actual adapter/pool/300-Pikmin packet fixture PASS, compile-out defaults PASS; actual local camera/HUD/Onion/audio branch fixture PASS; actual gameplay update/draw/frame/cursor/model fixture PASS across120 held frames; Clang diagnostics/core analyzer PASS;6 practice-runner/gate tests PASS;2 deliberately broken controls compile but correctly FAIL.20 pure network tests passed with restricted access;4 unchanged encrypted UDP tests timed out there and all4 passed with normal localhost access. No product networking fix was made for that environment failure.
- Confirmed working: Build68 remains the user-accepted limited phone baseline. Build76 source0ced5bbe83504842602cd03872409dc584065169 has an independently verified native IPA. New authority/camera/model source is locally checked only.
- Remaining issues: no room-to-game owner-thread driver, full accepted world baseline, dynamic replica birth/death/conversion/animation/job mapping, complete HUD/cursor/interaction state or actual phone gameplay yet. Additional render callbacks still need audit; do not call this an exhaustive guest-world proof. No playable Start is exposed.

### Pikmin 2

- Current objective: preserve its last user-confirmed working build while P1 co-op integration continues.
- What was investigated: no new P2 source or phone investigation in this batch.
- Root cause or leading hypothesis: none newly asserted.
- Files changed: none.
- Tests and results: no new P2 build/runtime test.
- Confirmed working: last user reports P2 launches and missing Pikmin/enemy/environment audio was resolved; full campaign completion is not verified.
- Remaining issues: later stronger campaign test and P2 online adapter; preserve existing installation/assets/settings.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental.
- Starting commit: 5d6d4b9169b63630f599a6a76628d59b27cc27b4; fetched origin matched before this checkpoint.
- Latest commit: this authority checkpoint is saved with subject `Hold replicated co-op worlds across engine update and draw [skip ci]`; its parent is 5d6d4b9169b63630f599a6a76628d59b27cc27b4. The accessible Exact Resume State.json records its resolved local/remote hash after commit/push.
- Commits created: one scoped source/test/journal checkpoint intended, with [skip ci].
- Changes pushed: normal branch checkpoint only; no history rewrite or stable release.
- Uncommitted changes: source/test/journal batch is being committed with this entry; any interrupted checkpoint must be recovered with git status before further edits. Accessible final state records post-commit status.
- GitHub Actions run IDs: latest verified native run40393742757 (Build76), source0ced5bbe83504842602cd03872409dc584065169.
- Build results: Build76 SUCCESS; new authority batch NOT compiled by Apple/Xcode yet. No new native run requested.
- Artifacts produced: no new artifact. Existing verified Build76 IPA5299633bytes, SHA25666ad7aa47f99465874fb676ae1c815fd709782a63df1e1785d3acd621ab7ba16, artifact12686618220. Build68 remains installed;76 is private engineering evidence.

### Next steps

- Next Pikmin 1 task: integrate guest population lifecycle and safe visual animation with the actual world baseline. Ordinary Piki::doKill is unsafe for replica despawn because it changes counters, plays death effects and can generate a seed.
- Next Pikmin 2 task: preserve working baseline; resume deeper testing/online adapter after the P1 practice milestone.
- GitHub/build task: keep related population/animation/world/input/room-driver changes in a larger batch. Use local checks until a meaningful integrated native checkpoint, then one P1-only build. Do not dispatch one build per helper.
- Anything requiring my involvement: nothing now; keep Build68. No phone connection, reinstall or new hardware test is requested.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: this is a source integration checkpoint, not a playable co-op release. Build76 validates the earlier fixed-cohort adapter only. Personal graphics/FPS120/camera/controls/touch settings are retained; no new frame-rate cap or texture downgrade.
- Important source-file locations: pc_coop_world.cpp authority/context; PlugPikiApp::idle phase/message guards; NewPikiGameSetupSection::update/draw; GameCoreSection::pcUpdateCoopHeldView/update/updateAI; PcamCamera::control; ViewPiki::refresh. New fixture tests/pikmin1_practice_authority_test.py exercises actual extracted branches with controlled engine leaves.
- Relevant logs: workspace work/authority-final-local.log, authority-clang.log, authority-world-clang.log, authority-runner-tests.log, authority-negative-controls.json, authority-gns-permitted.log. Prior Build76 receipt work/build76-package-verification.json and full log work/build76-p1-full.log.
- Unverified fixes: Apple/full-engine compilation and all phone behavior for this batch; dynamic/full-world replication, visual animation, complete HUD and new co-op interaction input are unfinished.
- Risks and warnings: a render-phase serial is NOT the authoritative simulation tick. Drive set_host_running with CoopSession::hostShouldAdvanceWorld after each session pump; keep pumping while held. Establish the complete world/local view before confirming loaded. Held gameplay mode input cannot itself unpause the world; the driver must route session controls. Preserve process-latched private card admission and restart-required exit. Do not reuse session IDs or wrap scene epochs. Do not enable old deterministic netplay unchanged: it locks30FPS/personal settings.
- Exact next actions: verify git/status/origin; read current authority entry; inspect Piki/ViewPiki creation/cleanup and animation callbacks; build a complete admitted baseline/lifecycle adapter, then wire owner-thread room/bootstrap/scene/input. Keep playable UI closed until those paths and local/native checks cover the bounded shared area. Later integrate campaign slots/shared Onion/per-player squads, disconnect/rejoin, durable recovery, internet, PC cross-progression and P2.

**END PROGRESS REPORT**


---

## Historical entries — use the current checkpoint above

## Build76 verified PASS; larger integration batches required

2026-10-26T21:03:01.111910+00:00 UTC. Run40393742757/source0ced5bbe83504842602cd03872409dc584065169 SUCCESS. Full log confirms expanded actual capture/pool/whole-squad/300-Pikmin packet fixture PASS; full native game BUILD SUCCEEDED;9 practice checks,12 room checks and real encrypted UIKit simulator runtime PASS; no cleanup errors. Artifact12686618220 SHA256c5409b50b594ef783566b8fc660ea8a085df32813c68ea06443d0090ae6d66bf and CRC verified; IPA5299633bytes SHA25666ad7aa47f99465874fb676ae1c815fd709782a63df1e1785d3acd621ab7ba16 UUID484f4c5d-796c-3b1e-b78c-60544382fced, ARM64 device, original identity/icons/notices checked. Retained privately under outputs/Build76-Pikmin1. No installation requested. Keep accepted68; P2 unchanged.

USER PROCESS CORRECTION: User asked why more builds follow successful builds.75 validated new startup/view code;76 validated newly added guest squad code, so these were distinct sources, not retries. Nevertheless prior requests for larger batches were not adequately reflected: internal pieces were sent to native CI too frequently. From here, group related lifecycle/animation/authority/input/scene-driver work toward a concrete two-phone practice milestone, run local regressions between edits, and trigger native CI for a meaningful integrated batch or a demonstrated failure requiring correction. Do not make one new native run the default for each internal API/helper. An Apple-dependent validation checkpoint may be justified by concrete evidence, but explain why and minimize it. This turn records76 and this policy ONLY; no next build triggered, no phone task.

Current engineering boundary: fixed-cohort actor apply is verified, not playable co-op. Birth/death/conversion/animation/jobs and complete world baseline/guest simulation authority/actual room-area-input driver remain incomplete. Next work continues toward an actual shared test area with independent views. Preserve independent personal settings/FPS120, working solo, existing apps/assets/saves, all queued campaign/recovery/internet/PC/P2 requirements. Full earlier reports below.

## Current run: Build76 — actual guest Pikmin cohort adapter

Run40393742757; source0ced5bbe83504842602cd03872409dc584065169; last observed IN_PROGRESS, no final result/new IPA yet.
https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40393742757

75/run40338639501 full native startup/view/networking/package SUCCESS independently verified. New source binds explicit host IDs to current local Pikmin and validates ALL captains/squad before any writes; rejects missing/extra/recycled/bad actors without partial movement. Local actual adapter fixtures/300-Pikmin reordered packet test/MSVC/Clang/compile-out and2 negative controls PASS. Fixed-cohort step only: population lifecycle, animation/jobs, full-world state, guest simulation authority and actual room/area/input driver still required. No playable Start enabled; keep accepted68 installed, no phone/USB task. P2/personal graphics/FPS120/settings unchanged. User reports result; no idle CI polling.

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-26T20:13:32.229011+00:00 UTC (America/New_York user timezone).

**Overall project status:** Build75 SUCCESS independently verified. Next P1-only source batch extends the real guest engine adapter from captain transforms to a complete explicitly bound Pikmin cohort. It is internal, not playable online co-op. Keep accepted68 on both phones; no phone/USB/installation task. All previous objectives remain queued.

### Pikmin 1
- Current objective: authoritative shared-world integration, preserving the working solo build and independent personal settings.
- What was investigated:75 complete log/artifact/9 Apple practice receipts/12 room checks/real encrypted UIKit runtime/IPA; actual Piki/PikiMgr lifecycle and guest state mapping.
- Root cause or leading hypothesis: captain-only application can leave a partial world. Actor order/address reuse cannot identify the host's Pikmin safely. Ordinary Piki::doKill also changes GameStat counters, plays effects and can create a seed; replaying that as guest removal would duplicate host gameplay.
- Files changed: pc_port/netplay/pc_coop_world.h/.cpp; tests/pikmin1_coop_capture_test.py; project journals/implementation/objective queue.
- Source changes: explicit accepted session/epoch + host-ID to LOCAL live-Piki bindings, with no pointer/order guessing; all currently live local Pikmin required. Validate every captain and Pikmin BEFORE any engine write; apply transforms/velocity/facing/coherent previous position/health/maturity/local captain association together. Owner/action remain host metadata and do not execute or overwrite guest AI actions. Missing/extra/foreign/recycled/invalid actors reject the ENTIRE update. Captain-only apply is refused after binding a squad. Pool forget invalidates the complete guest context; scene exit clears all pointers. Bounded scratch storage reused for population checks instead of per-Pikmin tree allocation each frame.
- Tests and results: strict MSVC /W4 /WX actual adapter + existing capture/pool fixture PASS, including wrong sessions/epochs/kinds, duplicate IDs/pointers, unknown/missing population, changed local captain/color, bad final actor/NaN/Inf/health/maturity/owner/leader, clock rewind, unchanged metadata on rejection, cancellation of partial output, whole-scene lifetime and empty squads.300 Pikmin through real packActorFrame/ActorFrameReceiver with reordered fragments apply only after complete assembly. Compile-out fixture PASS. Final Clang/core-analyzer actual adapter + fixture PASS. Two isolated negative controls correctly FAIL when removing last-Pikmin value validation or Pikmin pool-lifetime invalidation. Python AST/diff PASS. Apple/full game validation for this batch PENDING.
- Confirmed working:75 macOS actual admission/view fixture runs + iPhoneOS syntax/full native app/package and real networking PASS.75 artifact12659725915 SHA256d8824bc53ba70e35b2e467ca339df2b35646ccee434b65d44ff737ab6d67e45f; IPA5299899bytes SHA2568c7eb9819a6ac8b3e04a282e42c1361713de55faff21aa6a797f23e2631f2b5f UUIDcf1a69ff-1596-3ff2-96b3-4c78da1ec885, existing icons/identity/notices preserved, no cleanup errors. No75 phone install requested.
- Remaining issues: this is a FIXED-COHORT visual/state step. It does not create/remove/convert Pikmin, reproduce animation/jobs/targets, freeze guest simulation, replicate enemies/items/Onions/campaign, or start an actual room/area. A population change currently rejects rather than guessing. Native UI still connection-only; no Start caller enabled. Do not attest a complete world from this adapter alone.

### Pikmin 2
- Current objective: preserve working port; later campaign coverage and online adapter.
- What was investigated: no new P2 code/phone behavior.
- Root cause or leading hypothesis: no new P2 failure under investigation.
- Files changed: none.
- Tests and results: no P2 job requested.
- Confirmed working: earlier user hardware report; full campaign unproven.
- Remaining issues: stronger campaign validation, later online integration.

### GitHub
- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: 4a8862c5451dc51c1be3d013959df6308740daa8
- Latest commit: new source commit recorded in Exact Resume State.json after commit.
- Commits created: verified75 documentation checkpoint4a8862c5; this scoped guest Pikmin source/fixture batch.
- Changes pushed: P1-only native validation for whole-squad adapter; no P2/workflow/graphics/FPS/settings changes.
- Uncommitted changes: checked after source commit.
- GitHub Actions run IDs:75/run40338639501 SUCCESS; next run recorded after dispatch.
- Build results:75 fully verified; next native result pending.
- Artifacts produced:75 IPA retained privately under outputs/Build75-Pikmin1; no new batch artifact yet. Build68 remains installed baseline.

### Next steps
- Next Pikmin 1 task: inspect exact next native result, then guest-only population lifecycle/animation and engine simulation/presentation separation, actual room/area/input bridge. Reuse local co-op camera/captain/squad paths; preserve independent personal settings/FPS120.
- Next Pikmin 2 task: preserve; broader campaign testing later.
- GitHub/build task: existing actual adapter Apple fixture automatically covers this expanded code; one P1-only run, no idle polling. User reports result.
- Anything requiring user involvement: nothing yet; keep68 and existing assets/settings/saves installed.

### ChatGPT continuation notes
- Important functions: pc_coop_world_bind_guest_pikmin, pc_coop_world_apply_guest_actors, pc_coop_world_guest_pikmin_state, shared prepareCaptains/commitCaptains and pc_coop_world_forget.
- Relevant logs: work/build75-p1-full.log, work/build75-p1-artifact.zip, work/build75-package-verification.json; work/guest-pikmin-final-clang.log, work/guest-pikmin-negative-controls.json and generated actual adapter fixture/binaries under work/coop-capture-*.
- Unverified fixes: new adapter Apple compilation/runtime and actual phone behavior; no real two-phone gameplay or thermal improvement claimed by this change.300-Pikmin fixture is an adapter/network transaction test, not a phone performance benchmark.
- Risks/warnings: use explicit engine-created identities, never pointer values from packets or local enumeration order. Guest AI must be suppressed by future driver. Keep mode/FSM changes out of plain snapshot assignment. Ordinary death/birth paths have host gameplay side effects and need a separate visual population adapter. World simulation still lives partly in newPikiGame::draw; skipping updateAI alone is insufficient. Temporary practice card remains restart-latched and Start needs clear restart UI before exposure.
- Exact next actions: verify native result for this exact source; implement safe replica population/animation callbacks, complete world baseline and engine presentation authority, then connect room startup/readiness/input. Keep queued shared saves/reconnect/host-loss/mid-day persistence/internet/PC/P2 work, all documented in COOP_OBJECTIVE_QUEUE.md and COOP_MOD_RESEARCH.md. No original install changes until a concrete playable milestone.

**END PROGRESS REPORT**

---
Earlier checkpoint history:

## Build75 SUCCESS — actual Apple practice startup/view checks verified

Verified 2026-10-26T20:02:22.080315+00:00. Source17e674e20aedf048aa0cea09de1c64ff87e1d962; run40338639501 attempt1; scene121626913542 and P1121631623643 SUCCESS. All9 practice checks PASS, including actual admission/start/cache/backend and camera/HUD/Onion/audio fixtures on macOS plus iPhoneOS syntax. Full native game BUILD SUCCEEDED;12 room checks and actual encrypted UIKit simulator health/socket runtime PASS; no cleanup errors. Artifact12659725915 SHA256d8824bc53ba70e35b2e467ca339df2b35646ccee434b65d44ff737ab6d67e45f and ZIP CRC verified. IPA5299899bytes SHA2568c7eb9819a6ac8b3e04a282e42c1361713de55faff21aa6a797f23e2631f2b5f, UUIDcf1a69ff-1596-3ff2-96b3-4c78da1ec885; ARM64 iPhoneOS/platform, existing app identity/icons/notices checked. Retained privately under outputs/Build75-Pikmin1; NOT staged as phone update.

This proves compilation/test/package validation, not real phone/shared-world gameplay. Keep accepted68 installed; no phone/USB task. P2 untouched. Next: actual guest Pikmin identity/state adapter and complete engine/world ownership/presentation/input integration; do not expose Start or attest complete world from captain-only transforms. All queued independent settings/FPS120/campaign/recovery/PC/P2 requirements retained. No new build for this documentation result.

## Current build: 75 — protected actual startup and independent views

Run 40338639501; source 17e674e20aedf048aa0cea09de1c64ff87e1d962; last observed IN_PROGRESS, no final result or new IPA yet.
https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40338639501

One P1-only batch: protected CardUtil producer gate/drain/private admission and cached MemoryCard reset; actual title/setup reuse; independent fullscreen local camera/HUD/Onion/audio selection and teardown. Local actual-source fixtures, MSVC/Clang checks,24 networking CTests,6 failure/gate regressions,5 identity/bundle checks and2 rejecting negative controls PASS. Apple/full engine and phone behavior pending. VIEW selection does not freeze guest simulation; complete shared world/engine bridge still missing. No Start/UI exposure. Keep accepted68 on both phones; no USB or installation task. P2 untouched. User reports completion; no idle CI polling.

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-26T14:19:45.162331+00:00 UTC (user timezone America/New_York).

**Overall project status:** Resumed from explicit pause. Build74 remains the latest successful native package/runtime validation. This coordinated P1 source batch implements protected practice startup and independent fullscreen view selection. Apple validation is next. Online gameplay is NOT exposed; keep user-accepted Build68 on both phones. No phone/USB task.

### Pikmin 1
- Current objective: safely connect the accepted room to a disposable actual two-player area while preserving normal solo saves and independent personal settings.
- What was investigated: actual CardUtil producer/worker completion boundaries, cached MemoryCard file indices/data, direct title/setup route, camera/HUD/Onion/audio branches, legacy deterministic behavior and run teardown.
- Root cause or leading hypothesis: idle alone cannot prevent a new save job racing a root switch; old file/data/directory caches can survive admission. Existing fullscreen branches were tied to old deterministic mode, which also locks camera settings/forces30FPS elsewhere. Reuse the actual view paths without enabling that session.
- Files changed: CardUtil.h/cardutil.cpp, MemoryCard.h/memoryCard.cpp, new pc_coop_practice_start.h/.cpp, title/cardSelect hooks, pc_netplay_present.h/.cpp, pc_coop.cpp teardown, newPikiGame.cpp/gameCoreSection.cpp view branches, P1 CMake, four practice test/runner files and the existing experimental workflow.
- Source behavior: mutex-protected producer hold, nonblocking drain, explicit new private-card admission, safe pre-admission cancellation/failure retry, non-mutating readiness query, cache invalidation. Existing direct title/setup reused only after isolation, normal slot inheritance refused. Admitted practice remains process-latched; app restart required before normal solo. A future session driver must supply accepted-room intent, pump through drain/loading, timeout/cancel and show restart UI.
- View behavior: explicit player0/1 context selects own fullscreen camera/HUD/Onion and sound listener; invalid/nested/legacy ownership refused; actual co-op teardown clears view. No FPS/graphics/camera/control configuration writes. This is view selection ONLY; it does not suppress guest world simulation or attest a complete replicated world. No native Start/UI caller yet.
- Tests and results: strict MSVC actual-source admission/start/backend and view branch fixtures PASS; Clang/core-analyzer eight translation units PASS (final added race assertion subsequently MSVC compile/run PASS); 800 producer attempts, idle-window producer race, cancellation, invalid-path retry, busy-cache refusal and original bytes preserved. Actual camera/HUD/container/audio branch checks preserve ordinary solo/local split/legacy presentation. Two isolated negative controls correctly FAIL when removing producer hold or selecting the wrong audio listener.24 existing networking CTests PASS. Six new check-runner failure/timeout/gate regressions PASS. Two source-identity and three bundle tests PASS. Python AST/diff/structural workflow gate checks PASS; no full YAML parser claim.
- Confirmed working: earlier Build68 phone tests and user-reported solo baseline retained. New fixtures use controlled engine/OS/graphics leaves with real changed method bodies and real CARD backend, not a phone/GPU/full engine runtime.
- Remaining issues: game-thread room handoff/pump, actual complete world baseline and guest simulation/presentation separation, own controller/camera update mapping, world interactions, reconnect and campaign integration. Native compile/fixtures for this batch pending. No new hardware outcome claimed.

### Pikmin 2
- Current objective: preserve existing working build; stronger campaign validation/online adapter remains queued.
- What was investigated: no P2 code or phone changes in this batch.
- Root cause or leading hypothesis: no new P2 failure under investigation.
- Files changed: none.
- Tests and results: no new P2 tests/job requested.
- Confirmed working: earlier user hardware/audio report; full campaign completion unproven.
- Remaining issues: campaign coverage and later online development.

### GitHub
- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: c2d80471fa5bcc7d7a7d5001dc1a915be86a7b0a
- Latest commit: source commit recorded after this checkpoint in Exact Resume State.json.
- Commits created: scoped protected startup/view source and checks batch.
- Changes pushed: this source batch to ios-experimental, P1-only native validation requested.
- Uncommitted changes: checked and recorded after commit.
- GitHub Actions run IDs: latest completed74/run40265585036 SUCCESS; new run ID recorded after dispatch.
- Build results:74 real encrypted UIKit simulator runtime/12 room checks/full app/package PASS. New Apple checks: macOS compile/run and iPhoneOS syntax for BOTH actual-source fixtures, independent failure collection, mandatory original step outcome plus all nine receipt checks before IPA packaging. New per-check logs retained.
- Artifacts produced: no new artifact yet; verified74 IPA remains privately retained, Build68 remains phone baseline.

### Next steps
- Next Pikmin 1 task: inspect this exact native result, then continue actual room-to-engine driver and full-world/guest presentation integration. Do not enable Start using only captain transforms.
- Next Pikmin 2 task: preserve; resume broader campaign testing after P1 milestone.
- GitHub/build task: user reports new run; inspect complete logs and all new fixture receipts. No idle CI polling.
- Anything requiring user involvement: nothing until a concrete playable package is staged. Keep68; no USB/installation.

### ChatGPT continuation notes
- Important source-file locations: games/pikmin1/pc_port/netplay/pc_coop_practice_start.*, pc_netplay_present.*, games/pikmin1/src/plugPikiColin/cardutil.cpp/memoryCard.cpp/titles.cpp/cardSelect.cpp/newPikiGame.cpp and plugPikiKando/gameCoreSection.cpp.
- Relevant logs: work/practice-batch-clang.log, work/practice-checks-runner-test.log, work/practice-negative-controls.json, actual fixtures/binaries under work/practice-admission-* and work/practice-view-*;74 evidence retained.
- Unverified fixes: new Apple full app/source fixtures and actual phone behavior; guest full-world immutability and playable shared-world are NOT implemented by this view context.
- Risks and warnings: simulation advances inside newPikiGame::draw and other refresh callbacks; skipping updateAI alone is insufficient. Old lockstep mode still forces30/locks personal fields and is not enabled. Restart-only temporary routing is intentional until safe lifecycle restoration exists. New title restart guard needs a clear restart UI before exposure.
- Exact next actions: verify new run/source/package; add game-thread accepted-room ownership and continuous pumping through startup, supply scene readiness only after actual two-captain/world load, complete authoritative world/guest presentation/input adapter, then stage one concrete two-phone independent-view test. Preserve all queued research/settings/recovery/PC/P2 goals.

**END PROGRESS REPORT**

---
Earlier checkpoint history:

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

**Paused at user request:** 2026-10-26T13:39:41.923104+00:00. Stop development until resumed.

Repository C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port, branch ios-experimental.
Latest local/last fetched remote commit: c2d80471fa5bcc7d7a7d5001dc1a915be86a7b0a. No commit/push/build in this work segment.
Build74/run40265585036/sourcee896892cd0495dcf3bd064b2b7b9a6268833d291 passed; actual encrypted iOS simulator test, 12 room checks and IPA verified. Keep accepted Build68 installed on both phones. No phone/USB task. P2 untouched.

UNCOMMITTED IMPLEMENTATION, not ready for installation:
1. Actual CardUtil producer gate: closes under job-publishing mutex, drains existing work without blocking game loop, admits only the new private card, invalidates old directory/buffer pointers. Safe pre-admission cancellation, failed-path retry, non-mutating readiness query. Explicit worker idle initialization and exception-safe mutex guards.
2. MemoryCard::pcResetForCoopPractice clears old file indices, metadata and campaign byte buffer only after admitted/drained state. Personal settings untouched.
3. pc_coop_practice_start.h/.cpp wires protected requests into existing direct-title/setup route. No native UI caller is enabled. Admission precedes title exit; setup refuses a real-save fallback and inherited normal slot. After practice admission, app restart is required before normal solo.
4. pc_netplay_present practice-view context separates fullscreen local camera/HUD/container/audio selection from old deterministic netplay. Does not force FPS/camera/graphics/control settings. Actual newPikiGame.cpp/gameCoreSection.cpp branches reuse this context. No active caller yet. This is VIEW selection only, NOT guest simulation freeze/full-world replication.

VERIFICATION:
- Strict MSVC /W4 /WX compilation and actual-source admission/start/card fixture PASSED.
- Fixture tested an outstanding old job, 800 concurrent blocked producers, cancellation, invalid-path failure/retry, original-save byte preservation, actual private backend writes, stale cache reset and restart requirement.
- Diff whitespace check passed BEFORE the final view edits.
- Latest fullscreen view edits have NOT been compiled/tested yet. No Apple validation for any new work this segment. No new IPA/phone test.
- Existing card/backend tests and broader regressions need rerun once source batch is complete.

NEXT EXACT ACTIONS:
1. Inspect this uncommitted diff and saved snapshot; do not reset/reapply old installers.
2. Compile/test fullscreen context and actual camera/HUD/audio branches, including default solo/local split-screen preservation, both player identities, context teardown and legacy mode exclusion. Confirm no personal config writes/FPS cap.
3. Audit startup guards for failure/cancellation/return-to-title and rendering mutation boundaries. Actual world simulation runs inside newPikiGame::draw; skipping updateAI alone is insufficient to freeze a guest.
4. Continue game-thread room ownership/load/readiness and complete-world bridge before enabling Start Practice. Do not expose movement from incomplete captain-only state as a complete shared world.
5. Wire new admission fixture into existing Apple checks and run appropriate batch verification before source commit/push. Avoid another native build for documentation alone.

All queued objectives/research/independent personal settings/shared campaign/recovery/internet/PC/P2 requirements remain in ios/COOP_OBJECTIVE_QUEUE.md and ios/COOP_MOD_RESEARCH.md. Earlier full progress reports follow.

Uncommitted source status at pause:
```
M games/pikmin1/CMakeLists.txt
 M games/pikmin1/include/CardUtil.h
 M games/pikmin1/include/MemoryCard.h
 M games/pikmin1/pc_port/netplay/pc_netplay_present.cpp
 M games/pikmin1/pc_port/netplay/pc_netplay_present.h
 M games/pikmin1/src/plugPikiColin/cardSelect.cpp
 M games/pikmin1/src/plugPikiColin/cardutil.cpp
 M games/pikmin1/src/plugPikiColin/memoryCard.cpp
 M games/pikmin1/src/plugPikiColin/newPikiGame.cpp
 M games/pikmin1/src/plugPikiColin/titles.cpp
 M games/pikmin1/src/plugPikiKando/gameCoreSection.cpp
?? games/pikmin1/pc_port/netplay/pc_coop_practice_start.cpp
?? games/pikmin1/pc_port/netplay/pc_coop_practice_start.h
?? tests/pikmin1_practice_admission_test.py
```

Recovery snapshot: C:\Users\chazz\Documents\Open Nectar\2 - Progress and ChatGPT Handoff\Paused Work - Practice Admission and Views; includes tracked patch AND full copies of new/modified source with SHA256 manifest. These are private local backups; no game assets or credentials included.

---
Earlier checkpoint history:

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-26T13:20:09.142413+00:00 (UTC; user timezone America/New_York)

**Overall project status:** Paused at user usage limit. Build74 passed. Networking foundation is verified; actual online gameplay is not enabled. Keep accepted Build68 installed on both phones. No phone/USB or installation task now.

### Pikmin 1
- Current objective: connect the accepted room to a disposable two-player practice area without touching solo saves.
- What was investigated: Build74 full log, artifact, UIKit health and real encrypted socket execution, 12 room checks, IPA structure/resources; startup and rendering entry points.
- Root cause: Build73 incorrectly gave slow simulator installation/launch the short native execution allowance. Build74 separates setup deadlines from execution deadlines; actual health and socket tests now pass.
- Files changed this checkpoint: status/progress/handoff documentation only. Build74 source changed three runner files; game source unchanged by that batch.
- Tests and results: GitHub74 SUCCESS; health PASS; encrypted socket/session PASS; 12 room checks PASS; artifact SHA/ZIP CRC and unsigned ARM64 device IPA/platform/UUID/icons/notices verified; cleanup reports no errors. Local runner batch previously passed 38 regressions.
- Confirmed working: existing solo and Build68 connection behavior by earlier user tests. Build74 is compiler/simulator/package validation, not new phone gameplay validation.
- Remaining issues: real practice startup, host simulation and guest full-world rendering, independent views/input, actual Onion adapter, disconnect recovery, campaign integration and internet transport validation.

### Pikmin 2
- Current objective: preserve working port; return after P1 online foundation.
- What was investigated: no new P2 changes or tests this checkpoint.
- Root cause or leading hypothesis: no new P2 failure under investigation.
- Files changed: none.
- Tests and results: no P2 job in this P1-only run; earlier user reported working audio/gameplay.
- Confirmed working: earlier user hardware report, not a full campaign guarantee.
- Remaining issues: stronger campaign coverage and later online adapter.

### GitHub
- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: 5a11e7772f013bb69472a975d6ad4c4873e231f9
- Build74 source: e896892cd0495dcf3bd064b2b7b9a6268833d291
- Latest commit: documentation checkpoint recorded in Exact Resume State.json after commit.
- Commits created: documentation-only pause checkpoint, [skip ci].
- Changes pushed: documentation only; no extra build requested.
- Uncommitted changes: none before checkpoint; checked again after commit.
- GitHub Actions run IDs: 40265585036, Build74 attempt1.
- Build results: SUCCESS, including native runtime gate.
- Artifacts produced: artifact12627177472; IPA 5294015 bytes, SHA256 3179f2211e39d53341ebac28b143f25d62614bf50e9231c4694d9f88edb24ee4, executable UUID 3e5b2379-4fb7-3ac7-92b0-27381b14edbd. Retained privately in outputs/Build74-Pikmin1, not staged as the next phone update.
- Build link: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40265585036

### Next steps
- Next Pikmin 1 task: protected practice-area startup and real two-player engine bridge.
- Next Pikmin 2 task: preserve; resume broader validation after P1 milestone.
- GitHub/build task: no repeat build for documentation; batch meaningful driver changes and checks before next P1 run.
- Anything requiring user involvement: nothing now. Keep Build68; no installation or USB test requested.

### ChatGPT continuation notes
- All earlier additive objectives remain in ios/COOP_OBJECTIVE_QUEUE.md; four-mod research remains in ios/COOP_MOD_RESEARCH.md. Personal camera, graphics/FPS120, controls, audio and touch settings must remain independent. Host-agreed gameplay rules must not overwrite personal saved preferences.
- Actual source route: titles.cpp direct intent -> cardSelect.cpp direct setup -> ONEPLAYER_NewPikiGame -> gameCoreSection.cpp pc_coop_begin_run and two Navis. Native room is currently connection-only.
- Save safety: pc_card_begin_coop_practice provides process-latched isolated empty temporary card. Before invoking it, hold new CardUtil producers and drain pending work before scene teardown; idle alone is insufficient. No unlatch exists; app restart needed before ordinary solo resumes.
- Guest freeze hazard: newPikiGame.cpp::draw around2656–2706 advances world clock, Node update and game AI. Skipping only GameCoreSection::updateAI will NOT freeze guest. Audit draw-side mutations and presentation-role gates before actual replication.
- Reuse local co-op captains/cameras/squad ownership. Do not blindly enable old deterministic netplay: it forces30FPS and locks some personal camera settings; upstream catch-up also relies on drawing for simulation behavior.
- Relevant logs: work/build74-p1-full.log, work/build74-p1-artifact.zip, work/build74-package-verification.json. Earlier73 evidence retained.
- Unverified fixes: actual practice gameplay/guest world, phone74 behavior, full campaign and internet play remain unverified.
- Risks: unsafe title/card transition can race queued save work; render callbacks mutate simulation; no claim of mid-day persistence or exact host-loss recovery yet.
- Exact next actions: inspect clean head and saved state, finish startup/UI/render audits, implement protected practice admission with explicit ownership and readiness, then full-world baseline/input/camera bridge and meaningful regressions. Do not request a phone test until a concrete playable milestone exists.

**END PROGRESS REPORT**


---
Previous checkpoint history follows.

## Build74 dispatched — measured simulator phase-budget correction

Source e896892cd0495dcf3bd064b2b7b9a6268833d291; run40265585036; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40265585036; last observed IN_PROGRESS, no result/IPA yet. Three Python runner files only: separate install180s, launch90s, then health20s/native90s result waits after launch; phase receipts/accurate failed-operation classification; related cleanup60s/diagnostics45s. Actual native failure predicates/zero exit/ordered START+PASS/noFAIL and mandatory package gate unchanged. Local38 regression tests/syntax/diff PASS, including measured95s install+37s launch and strict stalled-native failure. Apple execution of revised budgets pending. No new workflow/game/test-body/P2/FPS/graphics/phone changes.

73/run40261792715 full P1 game/BOTH UIKit test apps/card/12 checks PASS, health installation killed by OUR20s combined setup/execution budget error; native code NOT RUN/no IPA. Same-run successful scene install95s establishes mismatch; exact older service-hang causes remain unproven. Keep accepted68 installed, no phone task. All additive objectives/research/personal settings retained. Actual protected practice area driver still next after native evidence. User reports result; no idle polling.

## Build73 concrete runner budget error; phase-separated fix — 2026-10-26T03:44:52.943583+00:00

73/run40261792715/source3fedaf80a384fda8dba6bab0c10eeb7a4800fc6d FAILED after compiling BOTH new UIKit test apps and full P1 game successfully. Scene job121375548655 PASS; P1 job121378419870 actual card fixture/iPhoneOS syntax/12 room checks PASS, zero distinct compiler/linker errors. Health app installation was killed by a20s combined install+launch+execution deadline; no health app code or encrypted test executed. Recovery shutdown also hit old20s limit. Mandatory runtime gate correctly refused IPA. Artifact12625991403 SHA2566a644473c2ed4fb67868292f4c4ce4decb29500846561a790d8b0e6e90d560ec/ZIP CRC PASS; compiled app plus nested health/socket apps retained and independently checked as ARM64 iOS Simulator with expected identities/markers. No73 IPA.

CONCRETE EVIDENCE: successful shared scene job in the SAME run spent 95.08s between installation and launch, then 37.02s between first launch and next command/readiness. The wrapper adapter incorrectly used the tiny health's20s EXECUTION budget for simulator installation and launch too. This was OUR test-runner mistake. Prior blanket broken-simulator attribution was too broad for73; this proves a budget mismatch, not the exact cause of every older service stall.

REPAIR BATCH (three Python test-runner files only): install has its own180s deadline, launch90s, then health20s or actual native socket90s result wait starts AFTER launch returns. Separate app-result.json records phase budgets/results/durations and failed phase. Timeout exceptions retain their actual phase/budget/partial native output. Install/launch failures are classified as such, not as executed native failures. One pre-native setup recovery unchanged; real native failures never retried. Related app terminate/owned simulator recovery/shutdown/delete deadlines60s and diagnostics45s accommodate observed slow control-plane work. No predicate/assertion/zero-exit/native START+PASS/noFAIL or mandatory packaging gate weakened. No test body/app/native-game/library/graphics/FPS/P2 changes. New timing source still needs Apple validation.

LOCAL38 host regressions PASS:15 legacy+11 owner/gate+12 app-pipeline tests. New tests reproduce95s install/37s launch and still pass with independent20/90 execution; install181s fails as install without native entry; launch91s fails as launch; a native hang after slow setup still fails at90s and retains START without retry. Per-phase receipts and false-pass gates verified. Python syntax/diff PASS. No Apple simulator or hardware execution performed locally; new native result pending next P1-only batch.73 already proves real Apple CMake/SDK compilation of UIKit wrappers, not their runtime behavior. Keep accepted68; no phone task. All independent settings/queued objectives/research and practice-card drain/latch contracts retained.

## Build73 dispatched — UIKit simulator app entry for exact native probes

Source 3fedaf80a384fda8dba6bab0c10eeb7a4800fc6d; run40261792715; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40261792715; last observed IN_PROGRESS, no result/IPA yet. This batch wraps the unchanged real socket and independent health test bodies in two separate scene-based UIKit apps, then install/launch/polls captured output and strict return markers. Full native START/PASS/noFAIL + zero wrapper return, UIKit entry, original execution step outcome and final receipt/log gate remain mandatory. Health20s/native90s not relaxed. Owned simulator lifecycle/one pre-native setup recovery/cleanup and diagnostic preservation retained. Local34 host tests +2 strict controlled-SDK ARC/core variants/plists/Python/workflow structure/diff PASS; real Apple CMake/app compile/runtime pending. No game/P2/FPS/packs/phone changes.

72/run40258515054 full app/card fixture/12 room checks PASS, standalone health and recovery shutdown timeouts on fresh owned simulator; native test NOT RUN; no IPA. Prior simulator ownership change did not solve it. Exact service cause unknown.70 attempt2 last socket/native success; accepted68 stays on phones. Actual practice area/input/camera driver still not exposed; T10 future. Independent settings and every earlier objective retained in COOP_OBJECTIVE_QUEUE.md. User reports new result; no idle polling.

## Build72 failure verified; native test moved to ordinary UIKit app entry — 2026-10-26T02:59:10.352738+00:00

72/run40258515054/source0b2eabc7e9ccd201150a13802f2bc9e7c85535d7 FAILED. Scene121365511495 PASS; P1 job121367822867 full native app BUILD SUCCEEDED, actual-card macOS fixture/iPhoneOS syntax and12 room gates PASS; zero distinct compiler/linker errors. New owned simulator c769b4b6-3912-4aff-865b-c9d9cb68acf2 booted, but20s standalone health spawn timed out again; diagnostics hung; recovery shutdown20s timed out before second setup attempt. Real co-op probe NEVER entered. Mandatory final runtime gate correctly refused IPA. Artifact12623948247 SHA256851b0eb8475e054e54090b47c2d8151766810b6c1e481610a34c55705ef15455, ZIP CRC PASS, compiled app and diagnostics retained; NO IPA. Same standalone socket hash as successful70 attempt2. Fresh simulator/early execution did NOT fix it; exact simulator-service cause unproven.

REPAIR changes TEST HARNESS only: two minimal scene-based UIKit simulator apps wrap the exact existing health and encrypted socket fixture bodies by renaming their entry symbols. Separate health app links no nectar_net/GNS/game. Normal simctl install+launch with stdout/stderr paths replaces standalone spawn for test executables; simctl spawn remains diagnostics-only. App wrapper runs once off main thread after scene connection, flushes native output before exact UIKit return-code marker, keeps UIKit responsive. No test assertions removed and no game body changed. Executor requires ordered UIKit entry+unique zero exit; runner still requires native START then PASS/no FAIL, authenticated real protocol work and mandatory original-step outcome+receipt/log gate. Health20s/native90s unchanged; one setup-only timeout reboot remains, no real native retry. Only owned app bundles terminated and owned simulator shutdown/deleted. Preserve built test apps, launch logs, partial stdout/stderr and failures. New mandatory receipt mode=uikit-app prevents old CLI receipts satisfying packaging.

LOCAL:34 host regressions PASS (15 existing failures,11 owned lifecycle/gates,8 new app pipeline). Covers real install/launch file plumbing via controlled backend, no executable spawn, failed/nonzero/missing/duplicate app completion, native timeout retaining START without retry, health recovery before one native launch, wrong app identity/platform/scene, and final native-log rejection. Both real wrapper macro variants strict Objective-C++ ARC/core-analyzer PASS against controlled UIKit/dispatch leaves; plist identities/scenes/platform parsed, Python syntax and workflow order/mandatory outcome checked, diff PASS. Those local checks are NOT Apple SDK compilation/runtime proof. New CMake app target and actual UIKit/socket execution pending next P1-only native build; unproven until CI. Independent shared scene check remains mandatory. No full YAML parser claim.

CORE OBJECTIVES PRESERVED: independent camera/graphics/FPS120/controls/touch layout; optional per-player difficulty later. QSB/Skyrim/Elden/Bloodborne research and additive objective queue retained. Existing old replay still forces30 and locks camera fields, so not enabled unchanged. Actual disposable practice area/controller/camera driver still missing; no new phone test/install. Keep accepted68 and65/54 rollback, normal settings/saves/packs, P2 and heat baseline. After new native result continue reusable local-coop driver with drained CardUtil/admitted process-latched temp card, real two captains, own camera/input/guest presentation/pause, restart before solo. No idle CI polling; user reports result.

## Research complete; independent personal settings and additive queue confirmed — October26

See COOP_MOD_RESEARCH.md for source-based QSB/Skyrim Together/Elden Ring Seamless/BBSC comparison, evidence limits and transferred design patterns; COOP_OBJECTIVE_QUEUE.md retains earlier and new objectives. New steering adds work unless explicitly canceled. Independent camera, graphics/FPS, controls and touch layout are CORE; per-player difficulty optional. Host-agreed gameplay rules may be temporary without overwriting personal config. Different cosmetic packs intended after validation; arbitrary gameplay mods need explicit support.

NEW REUSE LIMIT FOUND: old pc_settings_netplay_session_begin forces30FPS; PC_NETPLAY_SESSION_FIELDS includes freeCamera/firstPerson/gyro/coop camera fields. Exact replay cannot be enabled unchanged under user requirements. It remains a bounded candidate with a strict independence test, not an architectural switch or production shortcut. Keep host-owned world/campaign and reuse local two-captain/camera/HUD/audio/room/input/storage mechanisms. Research did not implement gameplay or trigger a build.72 last observed in progress, not polled here; keep68, no phone task.

## Co-op reuse audit — correction and faster-path candidate (October26)

User asked whether established local co-op/upstream research could accelerate online development. Read actual local/online source, not only earlier journal summaries. No gameplay/architecture switch implemented and no native build requested for this audit.

CONFIRMED REUSE: pc_coop.h/.cpp two-captain local run state/character selection; GameCoreSection creates both captains and updates two cameras. Existing updateDynamicSplit disables merged view under older netplay; drawGameInfoHud has a local-player fullscreen HUD branch; local listener audio selects the player's captain. These should be adapted/reused, not rewritten as a new two-player game. Hooks are coupled to the old deterministic two-pass path, so cannot simply turn them on independently of input/simulation lifecycle.

IMPORTANT CORRECTION: Earlier notes saying upstream online is only captain replication are incomplete. games/pikmin1/NETPLAY.md contains a stale captain-only introduction but later documents TWO modes: default exact world replay of host-applied inputs and older --online-predictive captain-only mode. Actual pc_netplay_session.cpp::online_guest_replica_ticks (line4782 at audit source) decodes both host-approved inputs, calls online_advance for real game ticks, records state hashes and catches up a late guest. The source exists; its iOS gameplay correctness has NOT been tested. Do not repeat captain-only as a blanket claim or call existing replay production-ready.

POSSIBLE ACCELERATOR: bounded isolated SAME-iOS-build proof of existing exact replay could reuse normal local-coop world logic for Pikmin/enemies/items rather than immediately writing a complete guest entity-state adapter. Reuse current proven encrypted rooms/compatibility/input/session/save-isolation work where useful. This is a candidate to evaluate before duplicating upstream integration, not an implemented change to the accepted host-owned campaign design. Replay needs matching outcomes across phones; hashes detect divergence but do not themselves repair it. It does not solve crash recovery or complete mid-day persistence automatically.

EVIDENCE OF CONSTRAINT: exact-replay function comments say every catch-up tick still renders because skipping presentation caused item state divergence at tick12 in an upstream rejoin test. Current session timing uses30Hz; high-FPS rendering, camera independence, our gameplay mods, different device shapes and host/guest settings need explicit verification. Do not cap/change user's FPS120 choice or graphics to silently make old mode fit. iOS in-process startup/room ownership, touchscreen input and background/return paths still need integration. PC/iPhone cross-architecture replay remains a separate unproven compatibility concern. If replay diverges, authoritative full-world replication remains a fallback, with existing components retained.

RESEARCH RECHECKED: Factorio developer FFF149 describes receiving a world and buffered inputs then catch-up (https://www.factorio.com/blog/post/fff-149); useful comparison, not proof of our determinism. Stardew mobile guide documents PC-host/mobile-client experiments, matching versions and interruption/network issues (https://www.stardewvalley.net/mobile-multiplayer-guide/). Grounded Shared Worlds documents single active host and shared progress (https://grounded.obsidian.net/news/grounded/grounded-heads-into-the-home-stretch). These offer design patterns, not drop-in Pikmin synchronization code.

NEXT CANDIDATE CHECK: after reviewing72, trace existing exact-replay setup dependencies and render/input/save barriers, then isolated two-process same-build hash proof through walking, independent cameras, one squad/attack/carry/Onion transaction and scene pause/load before selecting it for iOS prototype. Avoid another large rewrite or blind old-online enable. Near-term milestone remains two phones in one disposable familiar area with independent controls/views. Longer-term campaign recovery/cross progression/P2 remain staged. Keep68 installed; no phone task now. Build72 last observed in progress, NOT polled in this audit; no newer result claimed.

## Build72 dispatched — owned simulator, bounded setup recovery, mandatory runtime gate

Source 0b2eabc7e9ccd201150a13802f2bc9e7c85535d7; run40258515054; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40258515054. Last observed IN_PROGRESS, result/IPA pending. Repair changes only test runner/experimental P1 workflow, local26 regression tests PASS. Fresh owned simulator, one setup-timeout reboot before native probe only, earlier runtime before heavy compile, preserved diagnostic attempts/owned-only cleanup, mandatory original step outcome + complete receipt and actual native log gate before packaging. No retries/waivers for real native failures and no whole-job automatic retry. Actual service recovery on Apple still unverified.

71/run40255974650/source50360b19dbb8f4ce89c86e33f69ec55e96ec766c: full game compile/actual-card macOS fixture+iPhoneOS syntax/12 room checks PASS, separate simulator health20s timeout, native socket probe NOT RUN, no IPA.70 attempt2 remains last successful native/protocol package result;68 remains accepted phone baseline. No phone action/gameplay/FPS/resolution/packs/heat/P2 change. Actual disposable area/controller/camera driver not enabled; T10 FUTURE. Stop save requests/drain CardUtil before future practice admission/teardown; restart before solo after card latch. User reports new result; no idle polling.

## Build71 health failure verified; owned-simulator lifecycle batch — October 25, 2026 22:19 EDT

71/run40255974650/source50360b19dbb8f4ce89c86e33f69ec55e96ec766c FAILED at independent simulator health execution, BEFORE the real encrypted co-op probe. Scene job121357776731 PASS; P1 job121359982792 full app BUILD SUCCEEDED, zero distinct compiler/linker errors,12 room preflight/final gates PASS, actual temporary CARD/history/achievement original-byte fixture on macOS PASS and iPhoneOS ARM64 syntax PASS. Separate health binary compiled/platform checked but simctl spawn timed out20s, no output; follow-up simctl inventory and console diagnostics also timed out, cleanup timed out. Receipt failure_kind=simulator_execution_unhealthy_before_probe; probe_entered_main_observed=false. Exact host-service mechanism remains unproven. Socket binary SHA2040870bdd912cb23eff89e7542ddacf8c85e69929508d84b7c6929b9d290dab matches70 successful attempt2. No71 IPA; compiled app retained in artifact12622703467 SHA256232f9fe624eda4f0ff1b7ec0dba723baa1f9b5d810e2595e276567347417b871, ZIP CRC verified. No phone install requested.

REPAIR BATCH changes only tests and experimental workflow: CLI now creates a fresh uniquely named owned simulator from available newest27 template/runtime metadata. UUID parsed and refused if equal to ANY pre-existing inventory device; no borrowed simulator boot/restart/erase/delete, no shutdown-all/cache wipe/security edits. Explicit host-fixture opt-out only in old tests. Records inventory/device-type fallback/owned UUID, each setup attempt and diagnostics. Only a timed-out boot/independent-health SETUP can have one owned-device shutdown/reboot; this occurs before any real native probe. Wrong markers/nonzero native failures/no-entry native timeouts are NOT retried or waived. Full probe remains one90s execution requiring ordered exact START/PASS and no FAIL. Health remains20s (not relaxed). Cleanup attempts shutdown+delete of the UUID created by this run only; failures retained separately.

Runtime execution moved BEFORE expensive full device build to avoid waiting until after that build to discover broken simulator setup. Its step may continue collecting independent compile evidence, but a NEW mandatory final gate checks actual step OUTCOME=success, PASS+health+native-entry receipt, owned UUID/hashes and actual ordered socket log before packaging. Health alone, waived step failure, missing receipt, incomplete/malformed/FAIL log all refuse IPA. Independent room preflight gate retained; native build/package remains required. No full-job automatic rerun. This is a scoped response to observed runner failure, not proof that a fresh simulator will solve the host service.

LOCAL26 runner tests PASS: existing15 failure-path tests plus11 owned-lifecycle/recovery/gate tests including both setup timeouts, second timeout fails, failed recovery shutdown stops, borrowed/ambiguous create refuses without mutations, no native retry, cleanup warning retention, waived/partial evidence blocks packaging. Python syntax and workflow order/outcome/gate structure/diff PASS; no full YAML parser installed or claimed. Apple execution of NEW lifecycle pending next one P1-only build. Actual71 card/isolation compilation succeeded; native socket runtime still unvalidated on71.70 attempt2 helper native runtime PASS remains last successful result. Keep accepted68 installed; P2, saves/settings/packs/FPS120/resolution/heat/game source unchanged.

NEXT: Inspect new source run. If native runtime passes, continue actual disposable practice engine driver (not yet exposed): stop save requests and drain CardUtil, explicit process-latched card admission, main-thread retained room handoff, real area/two captains, full ready baseline, correct local/remote controls and own-camera yaw, guest non-simulating fullscreen view/HUD/audio, pause/background/exit. Restart required before normal solo after practice-card latch. Failed admission aborts practice. T10 phone practice remains FUTURE; no USB/test action now. User reports CI result; no idle polling.

## Build71 dispatched — practice-card isolation and simulator health diagnostics

Source 50360b19dbb8f4ce89c86e33f69ec55e96ec766c; run 40255974650; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40255974650. Last observed IN_PROGRESS, no result or IPA yet. This source adds explicit process-latched temporary practice card, overlap refusal, full CARD/history transaction barrier, callback separation, practice achievement write/award guards and actual-source preservation test. Includes previously committed176128 independent simulator health guard (not part of70 retry). Strict actual-source MSVC/Clang3/local preservation PASS; Apple pending. Normal card not switched: no practice API game/UI caller enabled. Future driver MUST stop new save requests/drain CardUtil before teardown, abort failed admission and require restart before normal solo after practice latch. Disk-backed temp child, no existing solo copy or nonempty cleanup. Actual title/area/two-captain/controller/own-camera/guest non-sim/pause driver still required; T10 remains future.

70 attempt2/run40247953593/source8bf43c8fd7a02d04c35bbd8ba2c8193daf1e77ab native/12 gates/simulator/package SUCCESS. Same probe SHA as failed attempt1 strongly supports simulator/runner problem; original failure retained. Keep phone-accepted68 installed. No new phone task or FPS/resolution/packs/heat/P2 change. Await user result; no idle polling.

## Build70 attempt2 verified; explicit practice-card isolation implemented — October 25, 2026 21:47 EDT

70/run40247953593/attempt2/source8bf43c8fd7a02d04c35bbd8ba2c8193daf1e77ab SUCCESS, P1 job121341674330 and scene job121341711036 SUCCESS. All12 required preflight/final gates, full actual UIKit/game build, actual captain fixture, encrypted simulator handoff/both-loaded area/input/pause/mismatch/rejoin and package PASS. Probe SHA2562040870bdd912cb23eff89e7542ddacf8c85e69929508d84b7c6929b9d290dab is IDENTICAL to failed attempt1; this strongly supports a runner/simulator problem. Attempt1 failure remains recorded, not erased. Simulator cleanup succeeded. Artifact12621390344 ZIP SHA2561653a8106d4e7f2965e742b9108311a46f80e83c4e9f2c7ef9927c736d6c697c; unsigned standard P1 IPA5291797bytes SHA256620be63ca87abd68dfcf9527368b8b3b1ec99a509c3fbe645530fecf7df40c8e UUID08ea1e96-0fc5-3182-8ec5-ee7e3f44cca4; deviceARM64/icons/notices checked. Retained privately, NOT installed. Keep accepted68 on both phones.

NEW SOURCE: pc_card_begin_coop_practice explicitly creates a NEW unique child under an existing absolute scratch directory (OS temp default), refusing uninitialized normal root, overlapping real-save root/ancestors/descendants/aliases, relative paths and repeat admission. No solo save copied. All actual CARD/history I/O and speedrun path transactions serialize with a recursive filesystem barrier; asynchronous callbacks execute outside it. Practice card is PROCESS-LATCHED with NO return-to-real-card API. Restart is required to regain normal solo saves. Delayed practice jobs cannot switch back onto the real card. Achievements block new practice awards and skip writes to the separate normal achievement file. Normal routing is unchanged until the explicit API is called; NO GAME/UI CALLER HAS BEEN ENABLED.

LOCAL PASS: actual CARD/history translation units + actual extracted achievement policy/write bodies, strict MSVC W4/WX fixture; original card/metadata/day-history bytes identical after create/read/write/rename/delete/format, both channels, stale handle, concurrent delayed writes and history operations. Admission waits for in-flight I/O; callback test proves another thread can take the barrier during callback. Failed admissions preserve original files. Clang diagnostics/core analyzer on three units PASS; diff check PASS. SDK/mode dependencies controlled; executable-location discovery unused under explicit test save root. New Apple/macOS fixture and full app checks pending next coordinated P1-only build. No phone behavior claimed.

CRITICAL DRIVER CONTRACT: stop new engine save requests and DRAIN CardUtil before scene teardown/admission. The filesystem lock does NOT prove engine buffer lifetimes or drain an upstream work queue. Once practice begins, do not offer normal solo Continue in the same process; require restart. Temporary files are on disk under OS temp, not RAM-only; nonempty directory cleanup is deferred. No existing data is recursively cleaned. Next actual driver still required: explicit title practice intent -> drained save worker + successful isolation -> main-thread native lease handoff -> actual disposable area/two captains -> full baseline/ready -> local/remote controller and own camera yaw -> guest non-simulating fullscreen presentation/HUD/audio -> safe pause/background/exit. Failed admission must abort practice, never fall back to normal card. No Start button/practice scene activated in this batch. No P2/FPS/resolution/packs/graphics/thermal change.

The independent simulator health guard committed176128 is also included in the NEXT source build;70 unchanged-source retry did NOT validate it. Local15 failure-path tests and strict C health check already PASS; Apple validation pending next build. Native failures remain failures; health success never substitutes for the real socket probe. No automatic repeated retries.

## Build70 attempt1 diagnosis; SAME70 attempt2 running; future health guard saved — October25,2026 20:51 EDT

70/run40247953593/source8bf43c8fd7a02d04c35bbd8ba2c8193daf1e77ab attempt1 FAILED. Scene121333441321 SUCCESS. P1121337183324 passed actual full UIKit/game compilation,the GNS-disabled core suite, ALL12 preflight checks and compiler/linker index0 distinct errors. Only failure: real simulator socket runtime gate. simctl spawn timed out90s with EMPTY stdout, no NECTAR_COOP_SOCKET_PROBE_STARTED observed; simulator basic device-list and process-log diagnostics EACH also timed out15s with empty output. Runtime receipt FAIL/failed_stage probe/no main entry observed. This strongly suggests an unhealthy simulator runner; pre-main binary/loader failure is not excluded without an independent health program. Do NOT invent a gameplay/network deadlock or mark70 runtime passed. Compiled app tar preserved; strict runtime gate correctly prevented IPA. Artifact12620159096 SHA25622298a98183169f363b4d53923d309adc057bc24526d2471afe2646b46983679 verified, no IPA in it.

Bounded recovery already dispatched: POST rerun-failed-jobs accepted for SAME70, unchanged8bf43 source; latest API run_attempt2/statusin_progress/conclusionNone. A fresh GitHub runner retries only failed job; existing scene result kept. No new numbered native run. Await attempt2 result; inspect attempt2-specific logs/artifact instead of reusing attempt1. No idle polling, no phone action; keep accepted68/65+54 backups and working P2.

Related diagnostic batch implemented/local-only and committed [skip ci] for NEXT source build (NOT executing in70 attempt2): separate tiny simulator health C executable, SDK/platform/hash verification and bounded20s health execution before real probe. A no-entry probe timeout gets separate health recheck, distinguishing healthy-simulator/pre-main-probe trouble from simulator execution failure. Any actual native entry/failure remains a native failure; health success never replaces co-op success. Require exact ordered START then PASS and no FAIL text, still nonzero exit/90s timeout fails. Preserve all partial progress/stage/error/health/diagnostics; shut down only runner-owned simulator. No automatic retry/waiver in new runner. Production CLI requires --health-binary; experimental workflow compiles/passes it. 15 meaningful mocked failure-path tests PASS, actual recorded good69 native log passes strengthened gate, Windows strict C11 health compile/run PASS and workflow flag/order structure+diff check PASS. Native health binary/runner changes still need future Apple source build; do not credit them to70 retry. No game/transport/graphics/FPS/packs/cards/P2 code changed for this diagnostic batch.

Next actual co-op engine work remains explicit no-I/O/temporary practice card (saveRoot caches env statically), title/CardSelect/GameCore disposable scene and real actors, controls+own camera yaw, guest simulation suppression/fullscreen HUD/audio, pause/background/exit. No playable Start UI yet; T10 remains future. Do not distract user with another connection-only install/test.

## Build70 dispatched — retained-room, buffered handoff and area agreement

Source8bf43c8fd7a02d04c35bbd8ba2c8193daf1e77ab; run40247953593 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40247953593); last observed IN_PROGRESS, no conclusion/new IPA yet. Combined source includes native explicit main-thread detach, exclusive room/session owner and shutdown order, bounded64/64KiB early-message queue/replay and both actual-load/area/seed agreement before HELD session. Local24CTest/real Windows encrypted early-message+area+input/Clang6/ARC10/identity2/diff PASS. New Apple/UIKit/simulator probe pending.69 separately verified native/12 gates/simulator/package PASS, no cleanup warning and no69 install requested. Keep68 installed; no phone action. Actual disposable card/engine/camera/controller/guest-sim driver not activated; T10 remains future. card_stubs.saveRoot caches env statically: late NECTAR_SAVE_DIR change cannot protect normal card. No P2/FPS/packs/save changes or new thermal claim. Await user result, no idle polling.

## Build69 verified; retained room + area-agreement batch implemented — October25,2026 20:09 EDT

69/run40243925821/source3ee9dcfbc9e562bf9a67d8945f4924fde3ed14f5 SUCCESS. Scene121321406659/P1121323818559 success. All12 preflight/final package gate, actual game compile, existing actual-source guest-captain fixture, simulator input/pause-queue/mismatch5/join/rejoin PASS. Downloaded artifact12618896083 SHA2564b37b417051db8935829ed94d522eda119cab5923b5c3c81f6a5d72e5b0a510c verified; IPA5288997bytes SHA25696d9464924c0d3b36e4dbea5ad4588447d34b7df7bdeb9bb339465b909048710 UUIDf2958444-a438-3617-a8e2-57308563ddf7, normal P1 identity/deviceARM64/icons/notices verified. Simulator cleanup succeeded this time (NO cleanup warning).69 retained privately in outputs/Build69-Pikmin1; no phone install requested because helpers still do not expose practice gameplay.68 remains accepted phone baseline/thermal improvement user report;65/54 rollback and settings/saves/packs/P2 preserved.

NEW integrated source batch: CoopConnection exclusively MOVES accepted HostRoom/GuestJoin ownership; requires authenticated compatible nonzero identities + gameplay capability, preserves caller on failed adoption, retains host lease, forbids bootstrap polling/sending after CoopSession starts, ends borrowed session BEFORE closing link, and retires issued scene context even if initial status send fails. Native main-thread-only explicit detach API stops old timer/observers, transfers ownership and dismisses only the screen; ordinary Done still closes the connection. No Start button or area launch activated. Native compatibility now also requires session capability, so future phone updates must use the same new build on both.

Related race prevented: old native UI discarded application messages while the other phone could already begin startup. New IN-MEMORY handoff queue accepts only bounded decoded authenticated application events (max64/64KiB), strips address/detail, resets across old link/background/close, moves with accepted room, and replays through the bootstrap/CoopSession BEFORE later socket bytes. Post-adoption UI append/poll is refused. No private code/data written to disk. Overflow/invalid native startup traffic closes safely with reconnect message.

PracticeBootstrap agrees a local-policy area ID (default0), host unique session/epoch/seed; both actual engine load callbacks required; rejects wrong role/area/stale or premature high-sequence start without poisoning valid sequence. Explicit60s/clock-backwards/link-failure timeout, no play-alone fallback. Host sends SceneStart only after BOTH loads; then both enter HELD CoopSession Loading, still needing complete actor baseline and deliberate ready. It does NOT load the actual engine, create actors, write campaign or claim complete world from transforms. Future driver must supply cryptographically unique session ID and actual scene-load attestations, keep pumping during loading, and own all lifecycle callbacks.

LOCAL: all24 CTest PASS; actual encrypted WINDOWS LOOPBACK probe PASS including early message handoff, both-loaded agreement, post-transfer captain records/input and clean peer-close; six Clang/core-analyzer units PASS; actual10 UI getters ARC+negative control PASS;2 source-identity tests and diff check PASS. Apple full UIKit/new handoff/scene probe pending next coordinated P1-only build. No new phone behavior or playable mode claimed.

NEXT ACTUAL ENGINE DRIVER: title practice start intent -> native main-thread lease handoff -> disposable area0 bootstrap/actual two captains -> guest apply + no autonomous guest simulation -> correct player controller/own-camera-yaw mapping -> own fullscreen camera/HUD/audio -> host wait/pause/background/clean exit restoring solo flags. SAVE HAZARD FOUND: card_stubs.cpp::saveRoot caches NECTAR_SAVE_DIR in static const path; changing env after launch DOES NOT isolate practice. Add/test explicit temporary card context or no-I/O practice card before any direct boot, including open/cached handles and restoration; do not point existing card at a fresh game. Old pc_coop_direct defaults can write normal card and must not be enabled blindly. Native handoff/baseline alone is not a playable world. Keep T10 FUTURE until verified complete practice package. No phone/USB action now. No FPS/resolution/packs/gameplay/heat/P2 changes.

## Build69 dispatched — guest input and actual captain bridge

Source3ee9dcfbc9e562bf9a67d8945f4924fde3ed14f5; run40243925821 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40243925821); last observed IN_PROGRESS, no conclusion/new IPA. Local23CTest/real encrypted Windows loopback input+pause+rejoin/actual guest engine fixture/compile-out/Clang5/diff PASS. Apple full real game headers and expanded simulator probe pending. Explicit helpers remain inactive in ordinary game; no room-to-game retained link, disposable scene bootstrap, controller/camera mapping or actual shared gameplay activated yet. Keep accepted68 installed; no new phone task.68 heat improved during gameplay by user report, cause unconfirmed; no FPS/graphics/packs/P2/save changes. Await user result, no idle CI polling.

## Gameplay-data batch implemented; Apple validation pending — October25,2026 19:15 EDT

User reports Build68 heat buildup noticeably improved INCLUDING normal gameplay; cause not independently isolated. A cooler starting phone after hidden menu work stopped is plausible, not proven. Record as user-observed thermal improvement so far, no temperature measurement/guarantee or automatic FPS/graphics changes.68 remains accepted phone baseline; preserve exact68/65/54 IPAs and earlier backups. No further heat tweak needed now.

NEW SOURCE: CoopSession now carries guest input through its already authenticated/build-content-compatible transport. Guest alone publishes bounded redundant input bundles addressed to HOST simulation ticks; host alone consumes them once per increasing tick. 33ms minimum send cadence prevents120FPS flood; reliable backlog defers send. Malformed/huge-future/rewound/wrapped ticks, invalid sticks, wrong roles and stale session/scene/revision rejected. Each pause/readiness revision clears all buffered controls and tags new packets so pre-pause movement cannot execute after resume. Missing input briefly holds continuous state then neutralizes; one-shot action edges never repeat. Large trusted host-tick skips clear history in bounded time. receivedGuestInputTick is diagnostic arrival acknowledgement ONLY, not world time/application proof. Existing actor frame/pause/rejoin core remains intact.

NEW ACTUAL GAME ADAPTER: pc_coop_world_begin_guest explicitly binds TWO already-loaded local captain lifetimes to accepted session/epoch, separate from read-only host capture. apply_guest_captains validates BOTH typed host IDs/players/epoch/finite bounded transforms, frame/tick monotonicity and current live local pointers before ANY engine write. Writes both position/previous-position/velocity/facing/rotation coherently. Rejects partial/duplicate actors, invalid second actor, changed remote IDs, recycled local actor addresses and old contexts without partial movement. Existing pool forget/scene-end hooks invalidate guest references before heap reuse. No spawning, Piki/jobs/world simulation, camera selection, stage startup, save mutation or menu activation. Explicit trusted session context required; ActorFrame alone is not authenticated.

LOCAL VERIFIED: strict MSVC actual adapter/capture/pool fixture plus compile-out check PASS; full23 CTest suite including impaired latency/loss/duplication input and pause tests PASS; actual encrypted WINDOWS LOOPBACK socket probe PASS including guest movement, single action edge and queued-input pause invalidation plus all5 mismatch/join/rejoin. First attempt under restricted execution failed wrong-secret reachability; same probe with authorized local network access passed, no game source change to hide it. Second compiler Clang/core-analyzer5 changed/fixture translation units PASS. diff check PASS. Apple/full actual game headers/simulator validation PENDING next coordinated P1-only build. No new IPA/phone gameplay claim.

IMPORTANT REMAINING INTEGRATION: Native room still closes link on Done; retain/hand it to game-thread owner, add explicit disposable scene/area loading with both-ready barrier, map local/guest controls with correct own-camera yaw, suppress guest autonomous simulation, render own fullscreen camera/HUD/audio, and implement retained-test-world pause/clean exit before exposing playable Start. Thus this is real engine/network data-path groundwork, NOT yet an exposed two-phone gameplay mode. No phone install/test requested; user keeps68. P2, normal saves/settings/FPS120/resolution/packs unchanged. Build run/source recorded after dispatch, no idle polling.

## Build68 phone test milestone — October25,2026 18:59 EDT

User reports "yeah all good so far, on the tests" in response to requested Build68 T05/T07/T08. Record this as overall user-reported PASS for title Online Co-op access/connection, remembered Rejoin and Done/normal game-controls-settings return. Separate per-phone timings/screenshots/repeat trials were not collected. This is limited same-Wi-Fi connection/UI testing, not shared gameplay, internet play, whole campaign completion or physical thermal validation. No new phone data writes by agent. Verified68 IPA/source54b873070d3ab331a6775e3a31aa85c8344c0ebf/run40232707062 is now the current user-accepted baseline; preserve65 and54 rollback packages, settings/packs/saves and P2. No FPS/graphics changes.

Current-code inspection: ios/ios_coop_room.mm still owns HostRoom/GuestJoin in the native screen; Done closes connection. It does not transfer an authenticated link to a running game. pc_coop_world.cpp only captures host captain/Pikmin records into complete packets; no guest engine actor creation/application. CoopSession is tested engine-free session/readiness/pause data, not a live game adapter. Old pc_online_navi.cpp has basic transforms but is under old optional netplay path and cannot by itself supply shared world or fullscreen guest control. Do NOT enable old online and call co-op complete.

Next integrated gameplay milestone: disposable familiar-area, no normal campaign writes, explicit session ownership handoff from native room to game-thread pump; authenticated start/area/epoch/ready barrier; two actual captains with host-owned movement and guest input; guest presentation from host state with its own fullscreen camera/audio/input; disconnect pauses retained host test world and stops commands; clean exit restores solo mode/settings. Loading must gate inputs and reject incompatible/missing actors rather than advancing two separate campaigns. First phone test T10 is simultaneous movement plus independent views and separation in the same area; Onion/actions/save/internet readiness must stay explicitly unavailable until implemented/verified. Add actual-source adapter/lifecycle/pause/scene tests and local impaired-network coverage, then one coordinated P1-only Apple build. Avoid a new CI run merely for this documentation result.

No additional phone action now. Phones may close P1/disconnect. Next code work is the actual session-to-engine bridge, not more connection-only phone tests. P2 remains preserved; separate shared slots, complete world replication, durable checkpoint/recovery and cross-progression remain later stages.

## Build68 SUCCESS — verified menu/Rejoin IPA ready for BOTH phones

2026-10-25T21:32:27.414006+00:00. Run40232707062/source54b873070d3ab331a6775e3a31aa85c8344c0ebf SUCCESS. Scene121287640022 and P1121290722481 success. ALL12 required native room checks passed and final original-outcome/complete-receipt packaging gate passed. Full app compilation/package and real encrypted iOS27.1 simulator connection/rejection5/join/rejoin probe PASS. Simulator cleanup timeout AFTER completed PASS retained as warning, not phone runtime evidence. Exact artifact12614073052 SHA2561052b1e1b6b0445a162778f683cc5d15b74df5e7a0e26b4c6ba42778073b7a8e; verified IPA5288985bytes SHA2567f4599e1acb5cbb63a9403e218c510b0f970c94a40ddb634eca1503cd396716b UUIDd7fdbb27-3997-3c86-be23-665d1df2be7a, ARM64 device/min15/SDK27.1, normal P1 identity/icons/pinned notices verified. No game assets/signing credentials bundled.

Staged: C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\CURRENT - P1 Build 68 - Menu and Rejoin\Pikmin 1 - Build 68 - Menu and Rejoin.ipa. START HERE.txt and Package Verification.json alongside it.65 verified IPA retained as known BOTH PHONE LAN baseline;54 rollback and earlier pre62 save/settings backups kept.68 source includes native title Online Co-op entry, memory-only Rejoin Last Room after authenticated join, opaque connection-screen hidden tick/render pause, and related formatting/strict preflight batch. These new UX/runtime features still require PHONE tests T05/T07/T08; no installation or real-phone success claimed. Separate solo/shared campaign slots, shared-world gameplay, internet matchmaking and durable mid-day recovery still future. FPS120/player choices/visible graphics/packs/saves/P2 unchanged; no measured heat claim. User updates BOTH existing P1 apps in-place with same68 IPA/account/identity, no uninstall/data recopy, then small same-Wi-Fi checklist. No further native build needed while awaiting phone observations.

## Build68 dispatched — related formatting and full error-collection batch

Source54b873070d3ab331a6775e3a31aa85c8344c0ebf; run40232707062 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40232707062); last observed IN_PROGRESS.67 failed3 deprecated sprintf calls copied from title function under Apple SDK/Werror, no IPA.68 bounds ALL7 related title formatters and fixes PC volume-tag buffer; local forbidden-API negative control catches regression on Windows. Actual desktop/native fixtures PASS;9 collection/gate/failure/timeout/stale-binary tests PASS;10 ARC getters and2 identity+3 bundle checks PASS. Native preflight now collects12 independent checks and preserves logs; independent full app/runtime may run to collect more errors, but final mandatory original-outcome AND complete12-PASS receipt gate blocks any IPA on failure. No warning bypass. Native menu/Rejoin/opaque pause still await full Apple/phone validation.65 BOTH PHONE LAN baseline preserved; no phone/visual/FPS/packs/save/P2 changes or measured heat claim. Await user result; no idle polling.

## Build67 exact compiler cause corrected as formatting/preflight batch

67/run40230727690/sourcea1523f08a7834376ade50cb433117c8d9f8a99fe FAILURE; scene121281673397 SUCCESS. P1 job121284703394 now reached desktop fixture compilation but failed on THREE uses of sprintf copied from actual pcInsertCoopItem. Apple27 SDK marks sprintf deprecated; fixture correctly uses -Werror. Native variant/full UIKit/app/runtime/IPA were skipped by the old early-stop step. Exact cause confirmed from full log, not another shell guess.

Batch source correction: replace ALL7 related sprintf calls in ogTitle.cpp with size-bounded std::snprintf, including title scan/labels, options/advanced pane tags and volume tags. PC builds get8-byte volume-tag array even in PAL variant (on20 needs4chars+terminator). No warning suppression or fixture weakening. Add forbidden-API macro to actual-source fixture so reintroducing old sprintf fails on this Windows SDK too; negative control verified real compiler failure for that API. Both actual-source desktop/native fixtures compile/run PASS through portable runner, including spaced paths;10 actual UI getters pass iOS ARC;2 identity+3 bundle checks PASS.

Batch verification/process correction: fixture runner attempts BOTH modes and reports all failures, never executing a stale binary after failed compile. New run_ios_room_checks.py collects12 independent SDK/compiler/fixture/identity/bundle/Foundation/ARC/header/UI checks and preserves per-check logs, partial timeout output and a complete result receipt. Preflight step may continue solely to collect full game compilation/runtime evidence; a NEW final mandatory gate checks BOTH original step outcome AND all12 successful receipt entries BEFORE success-only IPA packaging. Any failed/blocked/missing check/outcome refuses IPA.9 local failure-path tests PASS (multiple independent errors, dependency skipping, mode aggregation, stale-binary prevention, timeout evidence, false/missing receipts/outcomes). Workflow gate/order/diagnostic-upload structure manually/programmatically verified without claiming a full YAML parser or local Apple execution. All check output is retained; expected mock failures are kept out of real build logs.

UI/Rejoin/opaque-room pause source from66 retained; new native/runtime validation still pending.65 remains BOTH-PHONE SAME-WIFI T01-T04 PASS, old mismatch photo was earlier62. No new phone installs, no visual/FPS/120/pack/save/P2 changes, no measured heat claim. Native Online title row and process-memory authenticated Rejoin plus hidden-screen work reduction await verified next package. Separate Solo/shared campaign storage remains later. Full67 log saved privately and accessible; next P1-only run/source recorded at dispatch.

## Build67 dispatched — portable fixture compiler orchestration

Sourcea1523f08a7834376ade50cb433117c8d9f8a99fe; run40230727690 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40230727690); last snapshot IN_PROGRESS.66 failed shell EXTRA empty-array expansion under nounset BEFORE C++/app compilation; no IPA.67 removes shell flags/loop handling in favor of checked Python subprocess argument lists for both desktop/native fixtures with explicit compiler/SDK. Real local compiler runs through same runner PASS in both modes including paths with spaces. New title Online/Rejoin/opaque pause source remains unchanged from66; Apple full UI/app/runtime/package and phone behavior still pending.65 SAME-WIFI BOTH-PHONE T01-T04 PASS preserved. No phone/FPS/graphics/packs/saves/P2 changes or heat benefit claim. Await user result, retrieve logs/artifact, stage only verified new IPA for next small UI/room/solo test batch. No idle polling.

## Build66 failed test-shell wrapper; portable compiler runner verified

66/run40229474228/source5bf89a24b059fb37fd4aba9da99aeda16ad8a579 FAILURE. Scene121277899635 SUCCESS. P1 job121280013198 failed native room-check step BEFORE its C++ compilation: exact shell error `EXTRA[@]: unbound variable`. New optional flags array was empty in desktop mode under `set -euo pipefail`; the shell rejected its expansion. This is a confirmed CI-wrapper error, not a diagnosed game/UI failure. Full new app/UIKit/transport/package checks were skipped;66 produced no IPA. Existing65 phones remain unchanged and LAN-tested.

Corrected related wrapper as a batch: remove optional Bash-array orchestration entirely; actual fixture generator now owns desktop/native compile/run via Python subprocess argument lists, checked compiler/executable exit codes and bounded timeouts. Supports MSVC plus Clang with explicit macOS SDK root. CI invokes one Python command with quoted compiler/SDK paths. Real local compiler runs through THIS new runner PASS for both actual source fixtures, with spaces in output paths. Other workflow arrays audited: SOURCES/CONFIGURE_COMMAND are nonempty; existing BUILD_ARGS is outside nounset and65 previously compiled successfully. No unrelated P2 workflow changes or test bypass. No local Bash available, so do not claim local Apple/Bash execution; actual Mac Clang/SDK and full UI/app validation await next run.

The66 source features are retained unchanged: native title Online Co-op entry, authenticated process-memory Rejoin, opaque-room hidden game tick/draw pause with SDL/audio pump/scheduler rebase.30/60/120 choice, graphics/packs/saves and P2 remain untouched. New UI/runtime/physical heat benefit still UNVERIFIED on phones.65 remains BOTH-PHONE SAME-WIFI T01-T04 PASS. Next P1-only run/source recorded at dispatch; no phone action until verified package. Full66 job log retained privately and copied to accessible handoff folder.

## Build66 dispatched — native room convenience and hidden-work reduction

Source5bf89a24b059fb37fd4aba9da99aeda16ad8a579; run40229474228 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40229474228); last observed IN_PROGRESS, no new IPA/native/phone pass.66 adds native title Online Co-op row, Rejoin Last Room from authenticated invitation held only in process memory, and narrow opaque-room hidden tick/draw pause with SDL/audio pumping and scheduler rebase. Local actual-source native/desktop menu+pause fixtures PASS;10 getters pass iOS ARC;2 identity+3 bundle checks PASS. No FPS/120 option, resolution, textures/models, save/P2 changes. Physical heat benefit unmeasured, especially during normal gameplay.65 remains BOTH-PHONE SAME-WIFI T01-T04 PASS; old mismatch photo clarified as previous62. Full campaign/internet/host-kill recovery and separate Solo/shared slot adapter are not implemented. No phone action until verified new package; await user build result without idle polling.

## Native room UX/hidden-work batch implemented — awaiting Apple build

Build65 is the new confirmed BOTH-PHONE SAME-WIFI baseline: stable minute+,11ms low; Leave/rejoin/reverse hosts/normal solo pass. Old mismatch screenshot clarified as older62. No internet/shared gameplay pass claimed. Preserve65 IPA/backups.

Implemented next source batch: direct native-only title-menu Online Co-op row alongside existing local Co-op; retained desktop row layout/actions and challenge unlock; Online row opens clearly labelled connection-only screen without changing campaign/rules/slot. Added Rejoin Last Room, remembering only a successfully authenticated guest invitation in PROCESS MEMORY, never preferences/files/logs. Fresh join gates always run again. It survives guest link loss/background and closing/reopening the room screen while this app process lives; expired/refused/mismatched remembered rooms clear that target, unrelated failed typed-code/host attempts do not discard it. Successful hosting clears the old guest-role target. Host Messages behavior still retains the same room/code only while app process remains alive; no durable gameplay/host-crash recovery claim.

Efficiency: actual System::run previously kept calling app->idle behind opaque native room (hidden drawing/title animation/game ticks). Added narrow atomic visible-cover flag: only while that screen covers the game, pump existing SDL/UIKit/audio, honor quit, rebase scheduler/previous tick and sleep8ms; skip hidden app idle/rendering. Dismissal completion clears flag. Outside the native room, original loop and all player-selected FPS/120 availability, resolution, texture/model packs and graphics settings are unchanged. This reduces unnecessary lobby work by construction; physical heat/in-game heat improvement NOT measured or claimed. User handles FPS themselves; no quality/gameplay downgrade or heat test requested.

Local verification PASS: extracted ACTUAL title-label function and row mapping for native/desktop, challenge locked/unlocked, original local modes/options; ACTUAL opaque-pause block tested with real frame scheduler for all30/60/120 clamps, visible path unchanged, hidden tick suppression, event/audio pumping, quit and no paused catch-up backlog. MSVC/W4/WX compile/run in BOTH modes PASS;10 actual native UI getters pass iOS ARC naming compilation/negative control;2 build-identity+3 bundle regressions PASS; diff check PASS. Next native build must compile full UIKit/game and run fixtures/socket probe/package checks; no new IPA or phone result yet.

Files: ios/ios_coop_room.h/.mm; games/pikmin1/src/plugPikiOgawa/ogTitle.cpp; games/pikmin1/src/sysDolphin/system.cpp; tests/pikmin1_ios_room_ux_test.py; experimental workflow. No P2/save or graphics-setting changes. Separately labelled Solo/shared slots remain approved design until actual campaign adapter is ready; do not claim they are implemented. Next run/source recorded at dispatch. No phone action now.

## Build65 TWO-PHONE SAME-WI-FI PASS — October25

User confirms BOTH65 phones installed and tests1-5 passed: connected for over a minute, delay as low as11ms (initial100+ms sometimes decreases, sometimes starts low); guest Leave keeps host room waiting; guest rejoins; reversing hosts works; Done returns to normal solo with working visuals/controls/settings. T01-T04 PASS by user observation, scoped to SAME Wi-Fi ONLY. User explicitly confirms the last different-game-data screenshot was an OLD62 failure, not a65 regression. Screenshots support Connected/88ms and waiting/closed states; private invite codes are NOT copied into public journals. No internet/separate-network, actual shared gameplay, host Messages interruption or full campaign validation claimed.

Verified current source behavior: ios_coop_room.mm backgrounded keeps HostRoom/code in memory but deliberately disconnects the active peer; foreground resumes the waiting room, provided iOS has not terminated the app. Guest background closes its link. This is a connection-only room, not retained gameplay/world persistence. There is no one-tap remembered Rejoin control yet. User requests reconnect without resending codes; next UX batch should remember the last authenticated room locally in memory, offer explicit Rejoin, revalidate/authenticate and explain expired/closed room. Full gameplay pause/wait/readiness and durable partner/campaign identity remain separate planned integration; do not claim app-kill recovery from this screen.

Next authorized work: title-menu Online Co-op access alongside existing local Co-op, clear connection-only labelling until real shared gameplay; easier Rejoin; separately labelled solo/shared save slots with no overwrite when actual campaign support is integrated. P2 preserved.

Thermal feedback: user's screenshot shows120FPS/8.33ms,CPU62%,RAM1761MiB/spare1615MiB,Heat Serious; Raye's phone user-reported less hot. Different packs/screens/devices are possible factors, not a confirmed cause. User will adjust FPS THEMSELVES. Do NOT change/cap FPS, resolution, texture/model packs or gameplay/visual quality. Latest authorization: investigate waste reduction only (hidden rendering, background/lobby work, redundant work/allocations) if it preserves visuals/gameplay. No heat test requested now and no thermal fix claimed. Graphics/120 option remain unchanged.

Both phones can disconnect; no additional build needed merely to record these results. Next source UX/efficiency batch must preserve65 as verified LAN baseline and maintain the existing backup/rollback files. Exact report/checklist/state are updated; older sections below are historical snapshots.

## Build65 SUCCESS — verified IPA ready for BOTH phones

65/run40220611984/source3f650f7851ae9e38ba528f54fd42b89fbb095781 SUCCESS. Scene121251174574 and P1121253318001 both success. Actual iOS27.1 simulator encrypted probe PASS:100ms slow polling, wrong secret, all5 exact mismatch verdicts, valid join/rejoin, ready/pause/background/markers and complete60-Pikmin fixture data. Unicode/path native tests, app compilation and IPA packaging PASS. Downloaded artifact12610036177 SHA256e7067d41ba9d8d00490f104f9ed3a7f4e351050954a56e0136843faef401f8d4; staged exact unsigned IPA5288159bytes/SHA256c51d6ea0e6b9e86b8321435014f27db12904be723ef9394d7f591a17b2939aad, UUIDe4efb852-b36a-3fd5-ae8a-5561105c22b5. Normal P1 app identity/label/icons, ARM64 iPhoneOS/min15/SDK27.1, local-network permission, compiled new Unicode+close fixes and all3 exact pinned notices verified. Simulator shutdown cleanup timed out AFTER completed PASS; warning retained, not a native test failure or evidence of phone behavior.

Accessible: Documents/Open Nectar/1 - Install on iPhone/CURRENT - P1 Build 65 - Connection Fix/Pikmin 1 - Build 65 - Connection Fix.ipa, START HERE.txt and Package Verification.json.54 rollback copied/rehashed;62 original kept and guide marked superseded. Existing pre62 backups kept, not falsely presented as fresh65 snapshots. Both65 phone installations/runtime still PENDING. User updates BOTH existing P1 apps with SAME65 IPA and signing identity, no uninstall/data recopy/P2 update. Then same-Wi-Fi T02 NEW Host Room/code, return host to P1 before guest Join; T03 leave/rejoin/reverse roles; T04 ordinary solo/settings preservation. Connection ONLY, no shared gameplay yet. USB unnecessary after installations. No new native build pending. Approved title-menu/solo-shared-slot UX remains later work after room validation.

## Build65 — verified networking batch dispatched

Source3f650f7851ae9e38ba528f54fd42b89fbb095781; run40220611984 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40220611984); last snapshot IN_PROGRESS, no new IPA/native/phone pass.64 actual hash/Unicode/path regression and full P1 app compilation PASS; later socket verdict loss was reproduced locally, then fixed with bounded receive-before-close, queue ordering, retired callback/null guards, injected endpoint discovery and explicit probe loopback. Slow secret rejection, all5 compatibility reasons, room reuse/rejoin covered. Full23 CTest+8 full stress flows PASS; final rebuilt code6 focused tests+3 complete flows PASS; Clang5 translation units and13 Python tests PASS. Both phone apps/data unchanged; wait for user result, retrieve actual evidence and stage verified new IPA for BOTH before T02 retry. No idle CI polling. P2 untouched; title-menu Online Co-op/separate solo-shared slots remain approved later work.

## Build64 socket verdict loss reproduced and batch-corrected — October25

64 native Unicode/path identity regression ALL PASS and actual P1 app BUILD SUCCEEDED. Later encrypted room probe failed mismatch-reason assertion. Confirmed locally: GNS close callback destroyed unread final reliable verdict;100ms delayed GuestJoin polling fell back through endpoints to unreachable. Raw150ms delayed receiver also lost its final message. Both tests failed before fix and pass after. Batch: bounded drain-before-close/message-first ordering; queued events first; retired Connected callback and null-interface guards; honor injected discovery with router mapping OFF; explicit test-only loopback bind/manual endpoint; deliberate slow polling tests for secret rejection, all5 mismatch reasons, no partner bans and same-room rejoin. Full23 CTest PASS,8 complete impaired/baseline flows PASS; Clang5 translation units PASS; final rebuilt code6 focused CTest+3 full flows PASS.13 identity/bundle/runner checks PASS. No failed test bypassed. Full report/logs/private evidence saved; next P1-only native build pending. No phone writes, current62 unchanged, both may unplug. P2 unchanged; new IPA/real phones/internet/shared gameplay still unverified.

## Build64 dispatched — exact recovery checkpoint

Sourcef5a71297ab9c54b43157e402d6e05751a128fc35; run40217032902 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40217032902); last observed IN_PROGRESS, no conclusion/IPA yet.63 scene startup PASS; native content regression compiled but rejected a valid fixture with no branch detail.64 keeps strict tests, standardizes root AND enumerated scope paths consistently, reads original paths, adds exact rejection stages/labelled fixtures and /var/private alias coverage. Exact63 branch remains unknown;64 validates the supported path-handling hypothesis and will identify any remaining failure precisely.13 local regressions PASS; no Apple/phone pass claimed. Phone data unchanged and USB not required. On success stage same new IPA for BOTH phones, then T02 room retry. P2 unchanged; title-menu entry/separate campaign slots remain future approved work. No idle polling.

## Build63 native regression failure; path handling and diagnostic follow-up — October25

63/run40215584390/source405ab5ef8432e427366056fc82e607c67c8dfbc6 completed FAILURE. Scene startup job121235891954 SUCCESS. P1 job121238470144 failed Check native Host Join screen and generated build identity: the actual new Foundation test COMPILED, then exited with exactly `FAIL: hash valid fixture`. No compiler/linker error was present; full P1 build/IPA did not run. The original test did not identify which valid fixture or which rejection branch. Exact branch/cause therefore remains UNCONFIRMED; do not record a proven macOS-alias cause from this log alone.

Implemented a scoped follow-up: stable rejection-stage enum (no room-code/private-data logging), labelled fixture progress/failure, explicit intended reasons for empty-tree/symlink rejection, consistent standardization of BOTH root and enumerated paths for scope checks, raw enumerated filesystem paths retained for reads, and native /var-versus-/private/var alias coverage. Apple documents that Foundation standardization/resolution can remove /private (https://developer.apple.com/documentation/foundation/nsurl/standardizingpath?language=objc); alias handling is a supported hardening hypothesis, not a verified diagnosis of63. NFC identity keys and strict byte/name/case/symlink/alias-collision checks remain. Local2 build-identity+3 bundle+8 runner tests PASS; diff check PASS. Actual Foundation/iOS compilation/runtime awaits next P1-only build. Native regression was not disabled or bypassed.

Both-phone audit remains proven:3463 files/634811175bytes identical;46 Japanese NFC/NFD names caused62 false content rejection. No phone files changed.63 produced no installable IPA; current installed62 still needs corrected build on BOTH phones, then repeat T02. T03/T04 remain untested. Both phones can stay disconnected/closed while CI runs. P2 unchanged. Main-menu Online Co-op and separate Solo/shared slots are approved future work after connection passes, not implemented by this follow-up. Full63 job log saved privately in work/build63-p1-full.log and accessible handoff folder. Next source/run follows; avoid idle CI polling.

## User-approved upcoming UX — main menu Online Co-op and separate campaigns

After connection validation, add title-menu Online Co-op > Host/Join beside existing local Co-op, with personal offline Solo and a separately labelled shared campaign (numbered slots acceptable). Existing indexed slot/day-history code supports this direction, but multiplayer campaign identity/slot binding and write protection still need implementation/testing. Preserve occupied slots, whole-card backup and solo progress; joining targets the host's campaign, not the guest's solo slot. Detailed approved plan in PIKMIN1_COOP_IMPLEMENTATION.md and COOP_CROSS_PROGRESSION_AND_RECOVERY.md. No menu/save/runtime changes now; Build63/source405ab5ef/run40215584390 remains the pending identity-fix validation. No extra native build triggered. T02 false mismatch on62 still awaits corrected build/retest. P2 unchanged.

## Build63 dispatched — Unicode filename identity fix

Source 405ab5ef8432e427366056fc82e607c67c8dfbc6; run40215584390 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40215584390); last observed in_progress, no conclusion or new IPA yet. Both phone base-data audits complete; all3463 files/634811175bytes match,46 Japanese filename encodings caused62's false rejection. NFC source fix plus actual native Foundation regression queued.13 local regressions PASS and corrected independent full-data digest matches. T02 FAILED62; wait for verified63 then update BOTH and repeat room test. Both phones may disconnect now; no game data/settings/save/pack writes. P2 unchanged. No idle polling requested; user reports build result.

## Build62 phone join FAILED — confirmed Unicode identity bug

Both actual phones:3463 base-game files/634811175bytes; every file size and SHA256 matches canonical private source.46 Japanese filenames use NFC on Raye/NFD on original phone. Literal path hashing falsely rejects identical data. Implemented canonical NFC hash keys mapped to original paths; real byte/name differences and ambiguous normalized duplicates still rejected. Actual helper extracted for native Foundation regression.13 local regressions PASS; independent corrected full-data digest matches on both inventories. Apple native build/phone retest pending. No phone writes or pack changes; both USB reads complete and phones may unplug. T02 FAILED62, later runtime tasks untested; both phones will require the SAME verified next update. Connection-only, no shared gameplay yet. P2 untouched. Detailed report and private audit receipts retained; next source/run follows.

## Both Build62 installations user-reported ready — October25

User confirms both phones ready after the two same-identity P1 updates. T01 installation preparation is complete by user report; both pre-update backups remain verified. No post-update phone file-hash comparison, room connection or gameplay pass is claimed. T02 is next: both on same Wi-Fi, gear > Data > Online Co-op: Connection Test, wait for data checks, host/copy code, return host to P1 before guest joins, and allow Local Network if prompted. Expect Connected and a delay reading on both. Only after that, T03 leave/rejoin/reverse host and T04 ordinary solo. USB no longer required for these Wi-Fi tests; keep both apps foreground during connection. Connection-only, no shared campaign gameplay yet. Build62/source b8abc62ecddd146f411d136c0ab9f6095ee9d858/run40210863029 unchanged. P2/PC games untouched; no new build needed.

## Build62 phone update checkpoint — October25, 12:59 EDT

User reports their own P1 updated to Build62. Installation is user-reported; no new phone runtime/networking pass or post-update settings hash comparison is claimed. Raye's iPhone17Pro/iOS27.0.1 is connected. Initial process check found P1 still present; after user opened/closed it, fresh check confirmed P1 not running. Read-only P1 backup VERIFIED:5files/158975bytes, every local SHA256 and second phone read matched. Includes settings, achievements, navigation report and save/card0; no custom touch-layout file exists on her phone. No phone files changed. Large assets/mods stay in the existing app container. P2 untouched.

Raye can now install the SAME staged Build62 IPA through Sideloadly, selecting her phone and retaining the existing signing account/app identity. Her installation is PENDING. T01 remains partial; T02-T04 untested. After both installs: same Wi-Fi, gear > Data > Online Co-op: Connection Test, wait for data checks, host/copy code, return host to P1 before guest joins; then leave/rejoin, reverse host and verify ordinary solo. Connection only; shared campaign gameplay is not implemented yet. No new native build needed. User may disconnect USB after installation/post-update checks for Wi-Fi testing.

Build62 source b8abc62ecddd146f411d136c0ab9f6095ee9d858; run40210863029 SUCCESS. Staged IPA SHA256 e74db6323261aa6cd9c621cbc00a8f5445cdd2f0d7a9975b436cea026c681f3c. Both private backups and known-working Build54 rollback are preserved in Documents/Open Nectar. Full manifests remain private, outside Git.

## Build62 SUCCESS, IPA staged; first phone backed up — October25

62/run40210863029/source b8abc62ecddd146f411d136c0ab9f6095ee9d858 SUCCESS: scene121221580833 and P1121223972527 both success. Downloaded artifact12606436543 SHA256e5277bdfc894fe5ca0afc80a85aee47590bb26b07100bff2ddeeb9737cdcda22 and verified complete unsigned device IPA (5287907bytes, SHA256e74db6323261aa6cd9c621cbc00a8f5445cdd2f0d7a9975b436cea026c681f3c). Normal app identity/Pikmin1 label, ARM64 iPhoneOS platform2/min15/SDK27.1, approved icons, compiled scene+room code, local-network description and exact3 original dependency notices verified. Actual simulator session/private-code/content-mismatch test PASS. These do not establish phone runtime yet.

Accessible package: Documents/Open Nectar/1 - Install on iPhone/CURRENT - P1 Build 62 - Connection Test/Pikmin 1 - Build 62 - Connection Test.ipa, START HERE.txt and Package Verification.json. Known-working54 rollback rehashed/copied into Rollback - Keep. Both phones user-reported available; user phone connected/unlocked/P1closed. App-scoped backup12files/352195bytes verified by second read (settings/layout/achievements/save and save-solo-test), no phone writes. User prefers familiar manual Sideloadly drag/select/Start; told proceed on own phone. Installation NOT reported complete yet. Raye backup/update pending. T01-T04 now READY, unchecked; current step T01 partial. P2 unchanged. User can disconnect USB after installation/post-update check for Wi-Fi test. No shared gameplay yet.

## Build62 — exact current checkpoint

Run40210863029 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40210863029), sourceb8abc62ecddd146f411d136c0ab9f6095ee9d858; last API snapshot IN_PROGRESS, no conclusion/IPA verified.61 compiled actual P1 app and PASSED the full actual iOS encrypted private-room/session probe. Overall61 failed solely because dependency notices were at app root while verifier expected Licenses/;62 supports both layouts with strict pinned-byte/duplicate checks and preserves compiled archive before package validation. Local3 package tests+39 identity/storage checks PASS. No phone test active until verified package is staged; T01-T04 pending. P2 and existing phone/PC games untouched. User reports62 result; avoid idle polling.

## Build61 actual native+network PASS; packaging layout mismatch corrected — October25

61/run40208103332/source cda57702: shared scene121213299205 SUCCESS; P1 job121216893603 native Xcode BUILD SUCCEEDED and independent iOS27.1 encrypted session/private-room probe PASS. Overall job FAILED solely at package verification expecting Licenses/OpenSSL.txt. Actual CpResource log confirms ALL3 dependency notices copied into FLAT .app root (OpenSSL.txt/protobuf.txt/GameNetworkingSockets.txt); checker expected nested directory. Corrected verifier to accept flat/nested supported layouts and SHA-check every existing copy; mismatched duplicate still fails. CMake now explicitly uses flat Resources. Archive compiled app BEFORE packaging checks, preserving recovery artifact if a future package check fails. No game/network behavior changed.

Three packaging tests PASS including real observed flat layout, nested layout, missing/tampered/duplicate rejection;39 identity/storage/configure checks PASS.61 runtime artifact12605154966 SHA256b5ef2dbbd2043d5e48c8d05d2b9b78e14964e55c52b7e6c16c914a0fa11d827d downloaded+verified; receipt PASS, native probehash5c4fbb0ebc47dc3f196ca2fda5422b59183408e0b7ee2e0a70c748e15335f698. Post-PASS simulator shutdown cleanup timed out20s (recorded, not a test failure). No IPA packaged in61; no phone installation. Next P1-only build verifies corrected packaging; exact source/run follows. Phone checklist remains inactive; P2/PC games preserved.

## Build61 dispatched — exact checkpoint

Run40208103332 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40208103332), sourcecda57702b309552934609c167c3397c15bcc3ea8; last API snapshot IN_PROGRESS, no conclusion/IPA verified.60 Apple UI syntax passed, but simctl spawn timed out with partial stdout lost. Underlying simulator-versus-native-hang cause unknown.61 preserves failure output/stages and bounds native test lifetime; native game/resource compile happens before runtime, runtime remains required and runs independently after compile failure unless cancelled. Local23 core+actual GNS tests and full encrypted co-op/private-room probe PASS;8 runner failure-path tests PASS. No phone tests ready; T01-T04 wait verified package. Local network test processes are confirmed finished; user told Cancel both firewall prompts, no security rules changed by agent. P2/phone/PC game installs preserved; full co-op/recovery/cross-progression still pending.

## Build60 timeout diagnosis and local real-network validation — October25

60/run40204287553: scene121201787820 SUCCESS; P1121204903697 failed simctl spawn of compiled network probe after90s. Full iPhoneOS room UI syntax and ARC property checks PASSED. Simulator probe COMPILED/LINKED, Mach-O IOSSIMULATOR verified. No partial stdout was preserved by the old runner; cannot distinguish simulator launch stall from a native test hang from this artifact. P1 actual app compile/package were skipped, no IPA. Artifact12603398343 SHA2563869c339dc2a799c5dfd51ecab233260dc53b03b250870ca28e337fcd1a03347 downloaded+verified.

Implemented evidence/reliability batch: preserve timeout/nonzero partial output and failing phase, native main-entry/stage markers,60s test-only native watchdog including teardown, bounded failure diagnostics/cleanup;8 runner tests PASS. Move runtime probe AFTER independent native app compilation/resource checks and run it even if those fail (unless cancelled). All strict runtime/PASS checks remain required for a successful run/IPA. This collects more independent failures per build instead of stopping before compiling P1.

New isolated Windows real-network setup (existing SHA-checked GNS/protobuf source archives; BCrypt backend; no game install):23/23 core+actual GNS tests PASS, including room/gate/stress; full co-op socket probe PASS through60Pikmin/readiness/pause/markers/disconnect/private code/content mismatch. MSVC/O2/W4/WX plus project's CRT convention. This is Windows/BCrypt evidence, NOT iOS/OpenSSL or phone runtime proof. Firewall prompts from room_gns_test.exe and coop_socket_probe.exe were our completed local tests; told user Cancel. No firewall rules/security settings changed by agent, no listener should remain running. Do not rerun listeners unnecessarily while user is gaming. P2/phone/PC game installations unchanged.

Next P1-only native batch still needs full app/resource/runtime validation. Phone checklist has no active tasks until verified package is prepared; next room tasks T01-T04 remain pending. Cross-progression/recovery remains design-only. Exact next source/run follows.

## Running user testing checklist — October25

User explicitly requested a maintained list of their future testing tasks. Canonical [USER_TESTING_CHECKLIST.md](USER_TESTING_CHECKLIST.md), accessible Documents/Open Nectar/START HERE - What to Test.md/.txt. Ready now: no phone test requested until a verified update is prepared. Stable task IDs track room test, actual gameplay, disconnect/rejoin, checkpoint/host loss, PC/phone handoff, internet and P2. Future lists are not active instructions or implementation claims. Promote only small ready batches, record exact build/phone observations, preserve failures/results and send clear notification when human input is needed. Compiler/CI success must never mark a device task complete. Historical app-opening confirmations separated from new co-op tasks.

## Build60 dispatched; cross-progression/host-loss design saved — exact checkpoint

Run40204287553 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40204287553), source53466a4065fe017d5f3fa88b311e652885300ec2; last API snapshot IN_PROGRESS, no conclusion/artifact yet.59 retry scene SUCCESS but P1 failed OUR ARC regression-tool clang-driver flag ordering before full UIKit compile; fixed direct driver order while retaining clang-tidy convention. Both local fixture semantics and direct-driver argument-order adapter checks PASS; actual Apple driver/UI/native/private-code/package pending60. P1 only; no phone/PC/P2 changes. No install needed; user reports60 passed/failed.

New full user requirements/research saved in COOP_CROSS_PROGRESSION_AND_RECOVERY.md: live retained-host pause/rejoin versus durable full mid-day crash checkpoint, optional guest recovery copy, later opt-in host continuation and PC-home/iPhone-away single-campaign handoff with shared gameplay rules/local graphics preferences. No save/cloud/desktop features implemented by these notes. Continue iPhone milestones first.57 remains last full native/simulator networking success.

## October25 — Build59 retry result and cross-device/host recovery requirements

59 attempt2: shared scene121105139764 SUCCESS; P1121107438150 FAILED in the new ARC regression tool command before actual screen/game compile. Exact diagnostic: clang++ -x objective-c++ appeared after the last input and was an unused-command-line-argument error under Werror. Fixed standalone clang invocation to place flags BEFORE source; clang-tidy keeps source BEFORE its -- delimiter. Local actual8-getter and original ownership-negative controls PASS; standalone argument ordering checked through a driver adapter delegating semantics to real Clang frontend. Standalone Apple driver/full UIKit/native room/package still require next CI. No phone changes, P2 preserved.

Saved new user-approved design direction: PC-home/iPhone-away one official campaign, deliberate platform handoff/mod-rule parity later; live host retained-world reconnect first, full persistent mid-day checkpoint for host app loss, optional guest recovery copy and later continue-alone behavior with explicit squad safety. Full researched decisions and QOL in COOP_CROSS_PROGRESSION_AND_RECOVERY.md. No new save/cloud/PC gameplay implementation activated. Next P1-only build includes tool correction and these durable notes; exact source/run follows.

## Build59 attempt1 infrastructure boot failure; same-run retry queued — October25

Run40162073334/source d698f880af334690551a9bfb692521aec1551739: scene job121075548313 compiled probe successfully but simctl bootstatus for iOS27.1/Duo timed out after180s BEFORE install/launch. Artifact12586923613 SHA256358852e725dd39114978ccee7e1b235e66871a76f77c5f313f905a37649ba2d2 downloaded+verified; failure.json stage=boot. Both diagnostic simctl spawn commands also timed out45s. No native app execution/error is evidenced; P1 job121078373671 SKIPPED, no IPA. Underlying simulator stall cause unknown; do not claim new gameplay regression or verified room fix.

Authorized rerun-failed-jobs POST accepted for SAME59; API now QUEUED/conclusionnull, unchanged source. Last immediate API counter still run_attempt1; requested next attempt, verify counter on next result. No new game source or new numbered build. Existing ARC correction/guard still awaits full Apple CI. No phone/install needed; user reports the retry result. Preserve working P1/P2 and avoid idle polling. If boot repeats, investigate runner boot partial output/host status and add bounded infrastructure-only recovery without suppressing real app assertions.

## Build59 correction dispatched — exact checkpoint

Run40162073334 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40162073334), sourced698f880af334690551a9bfb692521aec1551739; last API snapshot IN_PROGRESS, no conclusion.58 failed exactly one Objective-C ARC property/getter naming error in new room UI; renamed copyButton to clipboardButton. Local actual8-property synthesized-getter compilation PASS; negative control recreates exact error. Regression check and full iPhoneOS screen compile included in59. P1 only; P2/phones unchanged. Wait actual native/socket/private-code/package result, then stage verified IPA and conduct two-phone connection-only test.57 remains last full successful native/simulator result. No phone or install needed now; user reports59 passed/failed, avoid idle polling.

## Build58 failure confirmed and corrected — October25

Run40161054040/source4f8ac135 failed P1 job121074322192 at the early iPhoneOS Objective-C++ screen check; shared scene121072507969 SUCCESS. Full log has ONE compiler error: ios/ios_coop_room.mm:127 copyButton getter follows Cocoa owned-object naming convention under ARC. Renamed property and all3 uses to clipboardButton. Audited all8 properties and14 method selectors. Added a compiler regression test extracting actual declarations and synthesizing their getters without UIKit headers: corrected screen declarations PASS on installed Clang frontend with arm64-apple-ios15.0 ARC; original owned-object naming trap produces exact diagnostic (negative control PASS). Full native screen/runtime still require next Apple build. All prior19core and identity/package tests passed in58 before this check; no new IPA produced, no phone changes, P2 untouched. Correction plus guard will be one P1-only build; next exact run entry supersedes pending state.

## Build58 — exact current checkpoint

Source 4f8ac1356f69fa1f47bbfab1ab411ab1ac4b2a76; run40161054040 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40161054040), last API snapshot IN_PROGRESS, conclusion pending. P1 only. Native Host/Join CONNECTION TEST UI + actual source/base-data fingerprints, private-code join/content-rejection probe, local-network permission and verified bundle notices. Local identity/packaging tests, strict C++ probe compile and39 app policy checks PASS. Apple/phone behavior PENDING.57 independently verified SUCCESS (native+scene+actual encrypted simulator/session), artifact/IPA checked; omitted notices corrected in58 source. No new phone install yet. User reports58 passed/failed; after native/package PASS, stage update in Documents and ask for a short two-phone same-Wi-Fi connection test. No idle polling; no phone needed now. No playable co-op campaign yet; P2 preserved.

## October25 — Build57 verified; real phone room screen implemented

Build57/run40158088407/source03cd0be0 SUCCESS: scene+P1 and actual iOS27.1 encrypted UDP/session with2captains+60Pikmin. Artifact downloaded+SHA verified, native ARM64/package identity checked. Networking notices were absent in IPA due to CMake parent/target source-property scope; fixed in new batch with strict packaged-byte verifier.

NEW pending Apple/phone validation: Advanced Settings > Data > Online Co-op: Connection Test, native UIKit Host/Join/copy/paste/leave UI, OS-random private room, source/config fingerprint and actual installed base-data streaming SHA256, local-network usage description, safe sharing/background and peer-loss handling. No campaign starts or saves/actors/settings mutate. Runtime gameplay options and full engine adapter still required before playable co-op.2identity+2packaging tests, generated real source digest, strict new C++ probe translation-unit compile,39 app policy checks PASS locally. New Apple check includes actual private-code join+content rejection, strict native UI compile and exact shipped notices verification. P2 untouched. No phone needed until next native build/package passes. See latest progress report and following exact run checkpoint.

## Build57 dispatched — exact current checkpoint

Run40158088407: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40158088407
Source 03cd0be08157613b020cb59c678271b44065a997, ios-experimental. Last API snapshot IN_PROGRESS, conclusion pending. P1 only plus shared scene and new iOS simulator real encrypted socket/session probe. No new artifact or phone runtime verified. Local19 core tests + new strict C++ probe compile +4 diagnostic-runner tests +39 app identity/storage checks PASS. P2 is not rebuilt. No phone needed. User should report passed/failed when57 completes; avoid idle polling. After reading actual Apple result, proceed with game Host/Join, actual source/content identities, accepted world loading and guest engine/camera integration. Current apps stay on working54/previous P2.

## New Apple encrypted transport batch — October24 session

Implemented distinct ios-arm64 and ios-simulator-arm64 pinned dependency builds, native matching hostprotoc, platform/SDK/pin-specific successful-cache receipts, static dependency notices, opt-in P1 encrypted transport linkage and real UDP/GatedTransport/CoopSession runtime probe. Probe checks wrong secret refusal, compatible join, both captains+60Pikmin atomic transfer, ready/pause/background/marker/disconnect flow. CLI runs only on iOS Simulator, rejects wrong-platform ARM64 and retains exact runtime/binary evidence.19 core tests, strict new C++ translation-unit compile,4 runner failure-path tests and39 app identity/storage checks PASS locally. Apple compilation/runtime PENDING next P1-only build. No game UI or live online mode yet; no phones needed. P2 source and normal P1 settings/saves preserved. See latest progress report and subsequent exact run entry.

## Build56 verified SUCCESS — 2026-10-24 America/New_York

Run40154273299, sourceb28a5d7b13037c68c76e66d730dd86fc679df59c. Both shared scene121052160673 and native P1121055004543 succeeded. Full P1 log and artifact upload metadata saved privately.18 core tests and actual P1 capture-to-receiver fixture passed in CI. Package binary was not downloaded/independently inspected in this status phase; no new phone install requested. The later researched session/pause/marker batch a5bd4690b3540b04c01d565ebcd83bea57d14e20 has19 LOCAL tests+Clang PASS but is NOT in56 and still needs Apple validation with upcoming integration. No co-op phone gameplay has been verified.

Next concrete work: build/prove encrypted iOS transport and generated source/content compatibility identities, then connect accepted Room/scene to CoopSession. Add explicit Host/Join prototype UI and guest actor/camera/audio integration using disposable campaign data. First user test will be actual two-phone connection and independent captains/views on the same Wi-Fi; shared-world actions/Onions/save/reconnect and different-network tests follow. Keep working54 and53 rollback; no phone needed now. P2 preserved.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-24 22:43 EDT

**Overall project status:** User authorized researched, fully developed co-op features. Primary-source comparison completed; feature plan saved. Implemented authenticated session/data adapter, loaded/ready gates, shared pause/interruption policy, typed partner markers and bounded actor update pacing.19 local tests and Clang PASS. No usable phone co-op mode yet. Build56 is previous actor-frame source and still running; new source saved without another immediate native run.

### Pikmin 1

- Current objective: Turn researched co-op design into a complete safe two-player session foundation, preserving normal54.
- What was investigated: Nintendo Pikmin3 leader/squad guide; Stardew developer multiplayer FAQ; Factorio latency/traffic postmortems; Mindustry developer server snapshot source; Deep Rock developer teammate/waypoint notes; Grounded shared-world notes. Findings/adaptations linked in PIKMIN1_COOP_RESEARCH_AND_FEATURES.md. Live56 metadata: shared scene successful, P1 configuring; no completed native result yet.
- Root cause or leading hypothesis: Complete actor frames alone don't define readiness, safe pause, mobile interruption or authoritative command permission. Protocol now models these explicitly. Stale queued status must never revive a timed-out phone. Previous loopback reconnect fixture tried opening a new connection before draining old closed-connection events; corrected lifecycle and verified re-auth/new-scene path. Initial new module compile missed explicit protocol header include, corrected locally before commit.
- Files changed: New libs/nectar_net/include/nectar_net/coop_session.h, src/coop_session.cpp, tests/coop_session_test.cpp; protocol.h/.cpp new types; core CMake/test list; experimental workflow Apple syntax checks; research/active-plan/status/handoff journals. NO games/pikmin1 gameplay source changed in this batch; no source flags activated.
- Tests and results:19/19 core test executables PASS with MSVC/O2/W4/WX. Clang diagnostic checks PASS including new source/test/protocol and existing actor/capture fixtures. Real authenticated gate + simulator test covers60owned actors, both-ready+loaded, host-only world advance, guest commands, independent pause reasons, background/foreground, heartbeat timeout and old queued packets, wrong ownership/epoch/sequence/payload, marker TTL/cooldown/nonfinite data, complete-update backpressure and20Hz network pacing. New source Apple/native runtime PENDING; no two-phone sockets/UI/gameplay verified.
- Confirmed working: Both phones' normal P154 launch baseline, Raye60FPS after restart; P2 working. Existing prototype actor-frame tests retained. New features confirmed only through core simulated peer tests, not real phone play.
- Remaining issues: iOS encrypted sockets/permission/session UI, generated build/content identity, scene/start-tick integration, real pause/lifecycle/input hooks, guest actors/fullscreen camera/audio, full world/Onions/workers/enemies/save/reconnect. Current confirmWorldLoaded is an adapter contract; the complete world bridge is absent. Fully fleshed design is saved; fully playable mode is not finished.

### Pikmin 2

- Current objective: Preserve working separate app while P1 prototype matures.
- What was investigated: No new P2 code this batch; future design accounts for forced shared cave travel and distinct local audio perspective.
- Root cause or leading hypothesis: No new P2 failure.
- Files changed: NONE under games/pikmin2.
- Tests and results: No new native/hardware validation requested.
- Confirmed working: User-reported P2 working on Raye's phone and prior original-phone baseline.
- Remaining issues: Longer campaign checks and P2-specific actor/cave/save adapter later.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; C:/Dev/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental; clean/fetched matching673581d9c6dda927d5a227e146e1dbc18d8f6ec9 before changes.
- Starting commit:673581d9c6dda927d5a227e146e1dbc18d8f6ec9.
- Latest commit: New research/session source exact commit written to external Exact Resume State.json after push.
- Commits created: One scoped research/session-feature source+tests+journal batch with skip-ci, preserving the in-flight56 native check.
- Changes pushed: New source batch; no extra native build immediately dispatched. Include it in the next meaningful P1 integration/validation run after56 result.
- Uncommitted changes: Only scoped listed source/workflow/docs until source commit; private evidence/helpers/assets never staged.
- GitHub Actions run IDs:56=40154273299, sourceb28a5d7b13037c68c76e66d730dd86fc679df59c. scene121052160673 SUCCESS; P1121055004543 in_progress/configuring at last check.55=40149838089 SUCCESS.
- Build results:56 pending.19 local tests/Clang PASS for NEWER source, NOT included in56. No claim native57 exists.
- Artifacts produced: No newly completed56/new-source IPA at this checkpoint.55 artifact upload metadata retained, not staged as a required update. Keep54 installed and53 backup.

### Next steps

- Next Pikmin 1 task: Actual iOS transport/build-content manifest, Room+accepted scene+new CoopSession wiring; then engine lifecycle/pause/input and guest actor/camera/audio bridge. Keep existing online flags OFF until isolated activation is deliberate. Current core is compatible-policy plumbing, not game mode UI.
- Next Pikmin 2 task: Preserve current game; later stronger cave/audio/save/system test and adapter.
- GitHub/build task: Save tested batch without redundant native run; inspect56 once completed, address real failures if any, then validate newer source together with next integration step.
- Anything requiring my involvement: None now; phones can unplug, no new IPA requested. User can report56 completion; do not consume usage polling idle.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User explicitly wants complete co-op with useful features, not merely two captains connected. New research document is the product/architecture feature contract. Accepted user constraints (together-only/one host/free same-area separation/own screens/shared stock/separate allowances/forced travel/health-led difficulty) remain. Independent offline play/cloud-host switching/host migration deferred despite Grounded supporting more.
- Important source-file locations: coop_session.h/.cpp/test: requires existing authenticated compatible GatedTransport, nonzero peer build/content digests and capability0x10000; MessageTypes67/68/69; WorldSnapshot carries prior complete actor frames. Active plan/research doc detail adapter APIs. Original FPS setting applies in gameplay constructor, user restart resolved it; no forced60 change.
- Relevant logs: PRIVATE work/coop-session-core-tests.log (final all19 PASS), coop-session-clang-checks.log, build56-result-run.json/jobs.json; research links in committed design document. No external game source/assets copied into repo.
- Unverified fixes: Actual iOS transport/UI/engine hooks and world snapshot/reconstruction remain absent. Heartbeat state API does not itself pause UIKit/game actors. Marker protocol does not draw markers yet. Caller must attest full engine readiness before confirmWorldLoaded; actor replica alone insufficient. No new native pass/phone co-op proof.
- Risks and warnings: Update pacing20Hz is networking only; user's selectable120 rendering not changed. Known reliable backlog64KiB defers whole updates; unseen transport queues require their own limits. Pause requests take network travel time. Secure rejoin identity/token and full world keyframe still to implement; tests re-authenticate the same private test gate. No accounts/security settings/paid services/other projects altered. No original saves reset; no finale spoilers.
- Exact next actions: Inspect56 when complete. Then implement actual native transport/manifest/accepted-scene glue and explicit experimental menu using disposable campaign data, wire pause/foreground and guest rendering. Add ownership-safe game actions/Onion transactions, full-world snapshots and two-network tests before release. Read PIKMIN1_COOP_RESEARCH_AND_FEATURES.md and active implementation plan first.

**END PROGRESS REPORT**

---

## Exact Build56 checkpoint — 2026-10-24 America/New_York

Source pushed: b28a5d7b13037c68c76e66d730dd86fc679df59c, branch ios-experimental. Build56 run40154273299, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40154273299. Last metadata status in_progress, conclusion pending; no native result/artifact verified yet. P1-only + shared scene validation.18 local core tests, actual engine capture-to-complete-replica fixture, compile-out and Clang PASS. Both phones keep working54; no new install requested. Raye60FPS confirmed after restart. No phone needed.55 separately verified SUCCESS. Stop idle CI polling; user will report completion. Next integration is actual authenticated iOS transport/session/scene compatibility and safe guest engine actor/camera application; current data replica alone isn't online gameplay. Full world, Onion engine transactions and snapshots remain.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-24 22:23 EDT

**Overall project status:** Both games launch on Raye's phone after P1 import-layout correction. Her P1 FPS change to60 was saved but only applied on re-entering gameplay; user confirms restart resolved30FPS. No phone needed now. Co-op55 passed native compilation; next batch implements complete captain/Pikmin frame packetization and an atomic guest-side data replica. This remains inactive engineering code, NOT online gameplay.

### Pikmin 1

- Current objective: Carry actual captured captains/squads through bounded multipart frames without applying partial/old/corrupt state.
- What was investigated:55 full P1 job121040694720 and scene job121038855551 both SUCCESS.17/17 macOS core tests and actual-engine fixture passed; artifact metadata recorded. Source frame pacing reads fpsMode in NewPikiGameSection constructor; closing settings persists selection but doesn't reconfigure current gameplay clamp. Raye live config fpsMode1, native2622x1206/1.0, AO0, VSync1; restart then user-confirmed60 works.
- Root cause or leading hypothesis: Confirmed FPS setting takes effect when gameplay reloads. For co-op, old packWorldDeltas splits a keyframe into independently decodable batches; none identifies completion of the WHOLE actor list. Replacing a guest world per batch would remove actors from other batches. New prototype frame envelope explicitly groups all parts and replaces only the complete validated replica.
- Files changed: libs/nectar_net/include/nectar_net/actor_frame.h, src/actor_frame.cpp, tests/actor_frame_test.cpp; nectar_net CMake; P1 pc_coop_world.h/.cpp actual capture-to-packets API; tests/pikmin1_coop_capture_test.py; existing experimental CI and journals. No P2 game change, normal settings/save behavior untouched.
- Tests and results: All18 core test executables PASS locally (previous17 unchanged passed; corrected new fixture rerun passed). Actual P1 capture/pool/packet-receiver fixture PASS, compile-out PASS, Clang diagnostics as errors PASS. New tests exercise1000 changing squads under loss/reordering/duplicates, timeout/non-sliding retries, stale frames/ticks/session/scene, checksums, malformed lengths/bounds, duplicate actors/captains, unknown schemas, nonfinite state and invalid owner/leader association. Two early assertions assumed a multipart frame that fit one packet and used stale test ticks; corrected fixture inputs, no runtime change to mask failures. New native Apple build pending.
- Confirmed working: User's P154 quick test baseline and Raye P154 title/music/controls launch plus restarted60FPS.55 native compilation/artifact upload only; no55 install requested. New receiver guarantees tested all-or-nothing DATA state; it does NOT write guest engine actors yet.
- Remaining issues: Actual iOS transport/session/invite UI, accepted build/content identity, guest actor creation/application/camera, host Onion-to-engine transaction bridge, enemies/jobs/items/world state and snapshot/reconnect. No claim online co-op is playable or full campaign tested.

### Pikmin 2

- Current objective: Preserve working P2 and its independent install.
- What was investigated: User confirms P2 works on Raye's phone.
- Root cause or leading hypothesis: No current P2 issue; source work remains paused.
- Files changed: NONE under games/pikmin2.
- Tests and results: No new P2 compilation/extended hardware test this batch.
- Confirmed working: User-reported normal P2 launch on Raye's phone, plus prior gameplay/audio baseline on original phone.
- Remaining issues: Longer campaign/device testing and eventual separate P2 co-op adapter.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; C:/Dev/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental; clean/fetched matching e2b9d47f5660fcd31b9bf292c16073fbc50428de at start of new co-op batch.
- Starting commit: e2b9d47f5660fcd31b9bf292c16073fbc50428de.
- Latest commit: New source/run and final docs checkpoint recorded in Exact Resume State.json after push.
- Commits created: One scoped co-op frame/adapter/tests/CI/journal batch with ios-build/ios-p1-only markers; no redundant P2 build.
- Changes pushed: New frame batch after passing local tests; exact source recorded externally once created.
- Uncommitted changes: Only scoped listed source/fixture/CI/journals until commit. No game assets/private phone logs staged.
- GitHub Actions run IDs:55=40149838089 source5bfa4fba17e9083deabeddc0033bc8a4a002ce06 SUCCESS. Next source/run recorded after push; NOT passed yet at this checkpoint.54=40145860255 SUCCESS, installed working baseline.
- Build results:55 P1+scene SUCCESS. New source Apple compilation pending; no phone install needed for plumbing-only check.
- Artifacts produced:55 P1 artifact12581478645 (5964282bytes, ZIP SHA256296fa46fa35f0498a3029c224cc2cab40cd67458759722e841cfc8c9e8b6e497); scene12581757882 (354779bytes, SHA256881ba0d61cd8f89b1f295114d6e01745fbdd08f61f179bbfc689361c70038376). Metadata/log upload verified, artifact binary NOT downloaded or independently package-verified this phase. No new55 staging/installation request.

### Next steps

- Next Pikmin 1 task: Real transport/session compatibility and accepted scene wiring, followed by bounded guest actor binding/application and each phone's own camera. Do not enable obsolete PC_ONLINE_ENABLED or independent guest simulation/save writes. Connect Onion authority to actual spawn/store and per-owner field limits, then remaining world state.
- Next Pikmin 2 task: Preserve working app; ordinary user testing optional.
- GitHub/build task: One P1-only Apple check for this batch, record exact source/run, stop idle polling. Native frame tests and actual capture fixture now in CI.
- Anything requiring my involvement: None now; both phones can disconnect. Keep54 installed. No new IPA requested until a usable prototype milestone.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Raye P1 black screen was my import path mistake, corrected and phone-confirmed. P1 data belongs in assets/dataDir; art beside assets. Both phones' selectable FPS remain30/60/120/monitor; fpsMode changes require gameplay reload in current baseline. New actor-frame module solves complete DATA transfer only, not rendering/AI/state restoration.
- Important source-file locations: actor_frame.h/.cpp (48byte NCF1 version1 envelope, session/epoch/frame/tick/whole-body size/FNV64 integrity/index/count); pc_coop_world_capture_packets validates increasing frame/tick and captures actual P1 actors before packing. Existing HostEntityRegistry/OnionAuthority remain.
- Relevant logs: PRIVATE work/build55-result-run.json/jobs.json/artifacts.json, build55-p1-full.log; actor-frame-core-tests.log (17 PASS then two faulty test assumptions), actor-frame-target-tests.log corrected PASS; actor-frame-engine-tests.log, actor-frame-clang-checks.log; raye-p1-fps-investigation.json and current-fps-settings.conf. No private evidence committed.
- Unverified fixes: No real phone-to-phone transport, session, actor application or new native56 result yet. No full-world snapshot/save or co-op gameplay. Existing solo rare bugs remain individually unverified.
- Risks and warnings: Authentication is EXTERNAL and REQUIRED: receiver only accepts bytes from authenticated HOST; FNV detects accidental corruption, is NOT a MAC. Accepted session/epoch comes from trusted scene barrier, never packet. One pending frame,128KiB/512actors/512fragments default bounds, fixed2s timeout; latest complete state retained through loss/corruption. Caller must not use stale packet output after false. Current maps include only captains/Pikmin visual schema, no targets/FSM/enemies/items/campaign. No simulation/game actor writes. Future transport should reliably deliver initial keyframes; this module supplies neither ACK/retransmit nor congestion control. Queued P1 buffers must obey engine scene-heap lifetime; owning vectors aren't proof they can outlive heap reset. Keep normals saves/settings/53/54, optional120 and AO-off baseline. No spoilers.
- Exact next actions: Inspect next Apple result once complete, then implement actual authenticated session/transport and guest actor bridge using complete frames. Continue P1_COOP_IMPLEMENTATION.md and SAVE_AND_COOP_RECOVERY_PLAN.md. No more phone setup required now.

**END PROGRESS REPORT**

---

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-24 America/New_York; recorded 2026-10-25T02:10:40.760072+00:00.

**Overall project status:** Raye now confirms BOTH games open. P1's black-screen startup was caused by this session's import layout error, now corrected on her phone and verified by a fresh user launch. No game source changed, no new IPA required. Co-op Build55 remains a separate engineering milestone.

### Pikmin 1

- Current objective: Resolve Raye's black screen after first-install asset transfer.
- What was investigated: Identified Raye's iPhone17Pro (iPhone18,1), iOS27.0.1. Read P1 Documents, three existing P1 crash reports, and a brief filtered startup log. Crash executable UUID1760960b-2d27-3a21-960f-2dcc404350c6 matches Build54, independently confirming her installed version.
- Root cause or leading hypothesis: CONFIRMED folder placement error in local import helper. It copied dataDir directly into Documents/pikmin1, while DVDOpen in pc_port/dolphin_stubs/dvd_stubs.cpp ALWAYS prefixes assets/. Jac_Start requests /dataDir/SndData; the missing expected assets/dataDir/SndData/Seqs/pikiseq.arc leaves Jac_InitEventSystem waiting for track0x20000. All three reports show Jac_InitEventSystem under Jac_Start/System::Initialise; iOS watchdog0x8BADF00D killed the unresponsive app. This is startup before drawing, distinct from the earlier in-game world-only black screen.
- Files changed: Phone only: relocated already verified disc roots into Documents/pikmin1/assets; kept art at Documents/pikmin1/art. Local work/import_raye_p1_assets.py now maps disc files to assets/* and art to art/* for future imports. Corrective helper work/repair_raye_p1_asset_layout.py used staged directory rename, refuses overwrite, and supports pre-activation rollback. Project/setup journals and accessible handoff updated. No P1 gameplay/audio/renderer source changed.
- Tests and results: Critical audio archive/bank/font hashes checked before move. ALL3529files/669952108bytes read back at CORRECT paths after activation with matching original SHA256; settings hash unchanged; saves/Load not written. Corrected importer syntax and mapping checked. User then confirmed title screen/music/touch-controls open normally.
- Confirmed working: Build54 on Raye's phone now launches normally, user-confirmed after repair. Original user's working app untouched.
- Remaining issues: Full campaign, longer performance/device-specific settings and existing rare gameplay bugs remain outside this launch check. Old Jac_InitEventSystem unbounded missing-resource wait still exists in source; no claim general startup failure handling was improved.

### Pikmin 2

- Current objective: Verify Raye's first installation; preserve existing source baseline.
- What was investigated: User's direct result after completed assets/art transfer.
- Root cause or leading hypothesis: No current P2 failure; P2 importer already used assets/* correctly.
- Files changed: None in P2 source or phone during this repair.
- Tests and results: User says P2 works on her phone; prior full2797file/1013544103byte readback transfer preserved.
- Confirmed working: User-reported normal P2 launch on Raye's phone. This is not a full campaign/audio-feature certification.
- Remaining issues: Longer gameplay/full story still unverified; P2 development remains paused while P1 co-op proceeds.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port, C:/Dev/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental; fetched origin and verified clean matching b1f020b30aa468e9d153412c853d553967281507 before journal edits.
- Starting commit: b1f020b30aa468e9d153412c853d553967281507.
- Latest commit: Documentation-only checkpoint for this repair is recorded in the external Exact Resume State.json after commit/push.
- Commits created: This repair needs only a scoped documentation commit with skip-ci; no game source change.
- Changes pushed: Updated journals/setup instructions; exact new commit recorded externally after push.
- Uncommitted changes: Only journals until documentation commit; private recordings/crash reports/assets/helpers not staged.
- GitHub Actions run IDs:55=40149838089, source5bfa4fba17e9083deabeddc0033bc8a4a002ce06. Last known in_progress from previous checkpoint, NOT refreshed during this phone repair.54=40145860255, sourcea7888f24009133fd3818355e35bfc5475c279e16, previously verified SUCCESS.
- Build results: No new build needed/triggered for relocating files.55's native result remains unverified at this checkpoint;17 local core tests+capture fixture previously passed.
- Artifacts produced: No new artifact this repair. Existing Build54 IPA unchanged;53 rollback retained.

### Next steps

- Next Pikmin 1 task: Continue co-op plan in ios/PIKMIN1_COOP_IMPLEMENTATION.md. First inspect55 once complete, then real transport/session/scene compatibility and guest actor application; bridge Onion authority to real engine accounting. Current capture is inert and is NOT playable online.
- Next Pikmin 2 task: No immediate code task; user can test ordinary gameplay when convenient.
- GitHub/build task: Save docs without extra CI; inspect55 once completion is reported, avoid idle repeated polling.
- Anything requiring my involvement: NOTHING else needed from either phone now; user explicitly told Raye can unplug. No reinstall or update for this repair.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Prior “all files verified” transfer receipt verified CONTENT but used wrong P1 parent directory. This correction supersedes the prior claim that the first P1 transfer was ready to launch. Both files and paths now verified and user-confirmed boot. P2 worked already. Preserve working apps/settings and prototype isolation.
- Important source-file locations: games/pikmin1/pc_port/dolphin_stubs/dvd_stubs.cpp DVDOpen prefixes assets/; games/pikmin1/src/sysDolphin/system.cpp Jac_Start uses /dataDir/SndData/; src/jaudio/pikiinter.c Jac_InitEventSystem waits on Jam_GetTrackHandle(0x20000). Correct install root Documents/pikmin1/assets/dataDir; control art Documents/pikmin1/art. No need to duplicate game data at both levels.
- Relevant logs: PRIVATE work/raye-p1-diagnostics contains three Oct24 crash reports205748/211009/211206 and live-p1.log; old imported ISO log.txt is historical developer output, NOT current iPhone startup evidence. work/raye-p1-layout-repair.json is definitive corrected-path verification receipt. Original transfer manifest/receipt retained for history; new repair receipt appended separately.
- Unverified fixes: No source-level startup timeout/recovery implemented. No claim online play, full campaign or all sounds tested. Fresh P1 boot with music/controls is user-confirmed.
- Risks and warnings: No unrelated files deleted, no original phone changed, no save/settings reset, no security/account changes, no proprietary assets or private reports committed. Keep120 selectable and AO-off known performance baseline. No final-boss spoilers.
- Exact next actions: Inspect55 when complete, preserve54 installed baseline and53 backup, continue co-op integration from documented active plan. Future P1 fresh imports MUST map extracted disc root under assets/, art separately beside it. Phone is no longer needed.

**END PROGRESS REPORT**

---

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF


**Date/time:** 2026-10-24 21:15 EDT

**Overall project status:** User's quick P154 check seems fine; proceed with co-op. New stable actor identity, Pikmin state codec and actual P1 read-only capture/lifetime hooks implemented and locally verified. Native engineering check: Build55 / run40149838089, source5bfa4fba17e9083deabeddc0033bc8a4a002ce06: in_progress / pending, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40149838089 Raye's two apps installed manually; both complete private asset/art transfers finished and verified. Her phone can be disconnected; runtime after import awaits feedback.

### Pikmin 1

- Current objective: Continue controlled co-op prototype while preserving54/53, existing settings and normal campaign.
- What was investigated: Actual MonoObjectMgr pool reuse/birth/kill, Creature init and stage heap teardown; old captain-only adapter and generic nectar_net records; Raye's startup folder contents and source assets.
- Root cause or leading hypothesis: Pool addresses are reused, so address-only identity can direct delayed commands at a different Pikmin. Worker/idle leader pointers change, so owner must persist independently. New registry prevents stale identity reuse, codec validates finite bounded state, hooks clear bindings before reuse/teardown. Raye's missing dataDir/art confirmed; likely first-install black-screen cause, fresh post-import launch not yet verified.
- Files changed: libs/nectar_net entity_registry.h/.cpp, pikmin_replication.h/.cpp +tests/CMake; games/pikmin1/pc_port/netplay/pc_coop_world.h/.cpp and minimal hooks; objectMgr.cpp birth/kill hooks plus already-audited missing diagnostic argument, creature.cpp init invalidation, gameCoreSection.cpp stage cleanup. P1 CMake opt-in NECTAR_COOP_WORLD; experimental workflow and tests/pikmin1_coop_capture_test.py. No renderer/input/save-setting rewrite.
- Tests and results:17 core network/accounting tests PASS with MSVC/O2/W4/WX (existing200000 decoder fuzz + simulated30-minute loss test, new20000 recycled identities and codec malformed/truncation/NaN cases). Actual capture translation unit and actual pool birth/kill methods compiled/run against controlled engine dependencies PASS: two captains/two Pikmin, retained working/idle ownership, no partial snapshot on bad state, stale pool command rejection, scene cleanup, inactive default. Feature-compiled-out fixture PASS. Clang diagnostics PASS for new source/tests and actual capture fixture. Negative control disabling lifetime invalidation causes fixture failure as intended. Build55 / run40149838089, source5bfa4fba17e9083deabeddc0033bc8a4a002ce06: in_progress / pending, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40149838089 No new live two-phone gameplay proof.
- Confirmed working: User's P154 brief smoke check fine; earlier53 graphics/keyboard/control edges. Raye P1 all3529files/34PNG/669952108bytes imported and SHA256 read-back verified, P1 preferences unchanged. Import does not itself prove launch/audio.
- Remaining issues: Live transport on iOS, host/join UI, guest actor creation/application, full-screen camera/input per phone, authoritative Onion spawn/store bridge and global field-limit reconciliation, complete world/jobs/enemy/item/campaign sync, atomic keyframes, exact-world save/reconnect/internet relay all remain. Capture is read-only, explicitly inactive unless begun; no online menu/playable campaign yet.

### Pikmin 2

- Current objective: Preserve existing source; finish Raye's requested game-file setup.
- What was investigated: Existing source manifest2768 disc assets +28 source touch PNGs, exact signed P2 app sandbox on identified iPhone17Pro.
- Root cause or leading hypothesis: Fresh installation also needed local proprietary assets, independent of co-op development.
- Files changed: NO P2 source. Added only assets/art in Raye's P2 sandbox; no save/preferences deletion/replacement. Original user's P2 phone untouched.
- Tests and results: Source hashes rechecked against prior canonical GPVE01 audit;2797files/1013544103bytes copied and read-back SHA256 verified; staging activated. No new P2 build or runtime test.
- Confirmed working: Prior user's P2 audio/gameplay; Raye's transfer is complete, launch after import unverified.
- Remaining issues: User's fresh relaunch/input/audio/pause feedback; stronger later campaign/cave/save tests before P2 co-op.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental; starting clean b5cb2b79ecdd4b9685b495a089f116902912f73a, fetched origin matched before edits.
- Starting commit:b5cb2b79ecdd4b9685b495a089f116902912f73a.
- Latest commit:5bfa4fba17e9083deabeddc0033bc8a4a002ce06 at checkpoint generation; new build source:5bfa4fba17e9083deabeddc0033bc8a4a002ce06. Final local/remote hashes saved in Exact Resume State.json after final push.
- Commits created: Scoped co-op capture/identity batch pushed at source above; documentation checkpoint afterward uses[skip ci].
- Changes pushed: Co-op capture code/test batch and current notes; one P1-only engineering build.
- Uncommitted changes: Current scoped code/journals before push; final external state records clean tree after checkpoint.
- GitHub Actions run IDs:Build55 / run40149838089, source5bfa4fba17e9083deabeddc0033bc8a4a002ce06: in_progress / pending, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40149838089 Previous54=40145860255 SUCCESS, sourcea7888f24009133fd3818355e35bfc5475c279e16;53=40133259493;52=40131000336.
- Build results: New capture source local tests/Clang PASS; current new Apple native result pending.54 native/IPA plus user's quick check retained. No P2 CI now.
- Artifacts produced: No new prototype IPA verified yet. User can keep54; this engineering build is not a request for another phone update.54 SHA256cdf46924e6cb350eb1df571325254f55d0a479c4fab5e4e564ad950335b50ae5;53 preserved unchanged. Raye's prepared P1 copy updated to54 with53 moved to verified backup subfolder; P252 unchanged.

### Next steps

- Next Pikmin 1 task: Review one native prototype build after completion, then implement bounded reliable session/scene handshake, guest actor binding/application and full-screen per-player camera. Next bridge actual atomic Onion spawn/store and one squad/job/enemy/carried object. Existing read-only capture is not enough to play online.
- Next Pikmin 2 task: Raye reopen/basic audio/game check; retain paused source and later stronger campaign tests.
- GitHub/build task: One P1-only technical check; no idle repeated polling. No phone update/retest demanded just for invisible capture plumbing.
- Anything requiring my involvement: NONE to continue coding/CI. Both file transfers done; user already told phone can unplug and games need full close/reopen. Raye exact public iOS27.0.1 verified; no more need to ask model/version. Report only actual runtime failures when convenient.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Co-op explicitly authorized.54 very quick smoke check seems fine, not full campaign certification. Registry/Pikmin codec plus actual-engine read-only capture now exist, beyond previous Onion-only state. No live sessions started and NECTAR_ONLINE remainsOFF. Prototype capture compiled in CI via NECTAR_COOP_WORLD=ON but begins only via explicit future API; normal solo remains inactive. No original save format changed.
- Important source-file locations: ios/PIKMIN1_COOP_IMPLEMENTATION.md, SAVE_AND_COOP_RECOVERY_PLAN.md; new pc_coop_world_begin_host/pc_coop_world_capture/pc_coop_world_forget/pc_coop_world_end_scene in pc_port/netplay; HostEntityRegistry in libs/nectar_net; PikminState codec38bytes. Registry owner persists independently of current leader. Monotonic16-bit scene epochs must not wrap; transport session IDs must never be reused.
- Relevant logs: work/coop-capture-fixture, coop-capture-bin, coop-direct; coop-capture-negative.log; work/raye-p1/p2-import-progress.json and private source/transfer receipts. Public notes only metadata, no proprietary game files. New native run metadata saved in work/coop-capture-new-runs.json after push.
- Unverified fixes: Real iOS compilation of the new bridge until CI finishes; no two-iPhone actor/world synchronization/real network/reconnect/save proof. Post-import Raye game launch/audio pending. P154 rare bugs remain untested individually.
- Risks and warnings: Never serialize local addresses; guest packets must pass session/scene/lifecycle freshness and authenticated ownership checks. Capture records are NOT full AI/job/campaign or exact-scene snapshots. Do not treat each split datagram as a whole keyframe; full keyframe assembly/application must be atomic. Registry lifecycle hooks must precede pool reuse and heap reset. Read-only capture buffers currently belong to scene lifetime; future network queues require safe owned buffers across transitions. Preserve54/53/settings/AO OFF/user120 choice, avoid fourth-app requirement, no finale spoilers or security/account changes.
- Exact next actions: Record native source/run and clean Git state; inspect resulting compile after user reports completion; implement real iOS transport/handshake + guest visual/squad vertical on disposable data, then complete game authority/Onions and recovery. User/ Raye can meanwhile reopen both freshly populated apps; if still black inspect new evidence rather than re-copy blind.

**END PROGRESS REPORT**


<!-- BEFORE CAPTURE MILESTONE -->

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF


**Date/time:** 2026-10-24 20:39 EDT

**Overall project status:** P1 Build54 native compile/IPA/package verification PASS; staged for a brief optional phone regression check. New game fixes are not hardware-verified. Co-op development has started with tested shared Onion accounting; online gameplay is not yet integrated. P2 unchanged. Raye reports iPhone17Pro/public non-beta iOS; exact version/connection later when available.

### Pikmin 1

- Current objective: Preserve user-confirmed53, verify54 and continue the controlled co-op prototype.
- What was investigated: Completed Actions run40145860255, successful scene/P1 jobs, full P1 job/build logs, both artifact hashes, simulator result, ARM64 executable, bundle identity/SDK/icons and expected feature markers.
- Root cause or leading hypothesis: Preventive fixes address confirmed source hazards and carrying timing; rectangle rounding addresses numeric edge mismatches. No new evidence establishes the cause of the earlier rare black-world/stranded pair/moving-line symptoms.
- Files changed: This verification phase changes documentation only. Build54 contains prior407b7fa4 game fixes and a7888f24 co-op foundation/CI, described in PIKMIN1_COOP_IMPLEMENTATION.md. No extra game changes or build triggered.
- Tests and results: Native iPhoneOS compilation PASS; actual-method rectangle161200 cases/zero mismatches + Onion/carrying/damage/slot tests PASS;15/15 offline network tests PASS on macOS; Apple ARM64 new-fixture/authority syntax checks PASS; actual asset-free iOS27.1 simulator launch/background/resume PASS. Package digest, ZIP, ARM64/iPhoneOS, original ID, scene support, icons and ProMotion permission verified. Simulator is not the game on real hardware.
- Confirmed working: User's installed53 graphics/touch/keyboard baseline, full native resolution/1.00x with AO OFF reported120FPS.54 compiled and produced a verified IPA; not installed/tested by this phase.
- Remaining issues: Online actor/world synchronization, registry/engine bridge, camera/session UI, internet invites/relay and snapshot/reconnect still need implementation. Rare campaign issues and full-story coverage remain unverified. User does not need to reproduce every preventive bug or replay the story for this batch; a short launch/settings/input/carry/pause/resume check can detect obvious regressions while53 stays preserved.

### Pikmin 2

- Current objective: Preserve working game; later stronger stability tests and separate co-op adapter.
- What was investigated: None newly; no P2 job in54.
- Root cause or leading hypothesis: No new P2 issue diagnosed in this phase.
- Files changed: NONE under games/pikmin2.
- Tests and results: No new P2 compile/runtime. Existing52 native/IPA verification retained; earlier32 gameplay/audio user-confirmed.
- Confirmed working: User's previous installed working P2;52 package exists but is not newly phone-verified.
- Remaining issues: Raye's first solo install/assets/basic test; later cave/area/save/campaign test before P2 online.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental.
- Starting commit:4b6111091a086fa332a152e958889c6df6687f9b (clean at entry). Build54 source=a7888f24009133fd3818355e35bfc5475c279e16; fixes=407b7fa4f5479aeeb983de5c84a234d03641291e.
- Latest commit: Documentation-only verification checkpoint pending at this report creation; exact final local/remote SHA saved in friendly Exact Resume State.json after push.
- Commits created: No new game-source commit in this verification phase; documentation checkpoint only.
- Changes pushed: Documentation-only with [skip ci], no P2 rebuild or extra P1 build.
- Uncommitted changes: Only current scoped verification journals before checkpoint commit; confirm clean after push.
- GitHub Actions run IDs:54=40145860255; scene job121026926855 and P1 job121029524253 both SUCCESS. Prior53=40133259493,52=40131000336.
- Build results:54 SUCCESS. All15 offline co-op/network tests and full native P1 job passed. No hardware/co-op session result claimed.
- Artifacts produced: P1 artifact12581053357 SHA256aa0a36f05371f82349bdbf80844b83da9cbce9195ae4a90542fb47d42cbbd0bc; scene artifact12580922615 SHA2566ff701b72c9a1ad4b8dc06c9a63b1b4f49f4d0353ddcc2d7d87d1363cb98158c. Staged IPA=C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\Pikmin 1 - Build 54 - Stability Update.ipa, 2835985bytes, SHA256cdf46924e6cb350eb1df571325254f55d0a479c4fab5e4e564ad950335b50ae5, executable UUID1760960b-2d27-3a21-960f-2dcc404350c6, original IDorg.opennectar.experimental.pikmin1, unsignedARM64/iPhoneOS SDK27.1/minimum15.0. Build53 original IPA rehashed and retained unchanged.

### Next steps

- Next Pikmin 1 task: Optional brief same-ID54 update/regression check; continue same-Wi-Fi disposable captain/squad prototype and actual engine registry/Onion bridge using the saved active plan. No full campaign/finale check demanded.
- Next Pikmin 2 task: Keep current game, no new build; Raye solo installation when ready.
- GitHub/build task:54 complete, no polling and no new build needed merely for documentation. Review any new actual failure before further fix.
- Anything requiring my involvement: Handle signing/install and brief phone feedback when convenient. Raye is using her iPhone17Pro now, so don't request immediate disconnect/use; exact public iOS version can be read when available. Her prepared P153/P252 folder remains unchanged until54 hardware feedback; nothing installed on either phone in this phase.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Co-op is explicitly authorized and underway; only the engine-free Onion authority is implemented.15 passing tests do NOT mean15 game/campaign scenarios or a real two-iPhone session passed. User asks whether rare fixes can be checked: explain automated targeted evidence plus a brief device regression check, not blind hope or a full story retest.
- Important source-file locations: ios/PIKMIN1_COOP_IMPLEMENTATION.md, ONLINE_COOP_DESIGN_NOTES.md, SAVE_AND_COOP_RECOVERY_PLAN.md; libs/nectar_net/onion_authority source/header/test; old captain adapter games/pikmin1/pc_port/netplay/pc_online_navi.cpp and pc_netplay_session.cpp. Normal online flags remainOFF until a usable integration exists.
- Relevant logs: outputs/Build54-Pikmin1/ios-build.log and ios-build-errors.md; work/build54-p1-full.log; work/build54-result-run/jobs/artifacts.json; work/build54-startup-runtime-verification.json; work/build54-verification.json. Friendly folder2 has verification/log copies.
- Unverified fixes: New54 device behavior, complete campaign, old NaN/black-world/stuck-rescue cases, all actual online gameplay/save/reconnect.
- Risks and warnings: Preserve53/settings, AO OFF and user-selectable120. No raw pointer/heap snapshot or arbitrary-tick normal-card writes. No fourth-app requirement, original save overwrite, host migration, paid relay/account changes or finale spoilers. Package backup isn't current phone-data backup. P2 remains paused.
- Exact next actions: Provide staged54/checklist → receive brief optional device result; independently advance controlled iOS transport/captain+squad vertical and registry/transaction bridge, then full host-owned world/recovery. Install Raye's P1/P2 once phone available, import private assets separately, validate her solo baseline before two-phone tests.

**END PROGRESS REPORT**


<!-- BEFORE BUILD54 VERIFICATION -->

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF


**Date/time:** 2026-10-24 20:14 EDT

**Overall project status:** User accepted P1 Build53 as the current working solo baseline and explicitly authorized beginning online co-op now. Preventive P1 upstream batch implemented and locally checked. First host Onion accounting component implemented/tested, but NOT connected to game actors or live networking. Raye install copies prepared; no installation/phone data changes performed. Pushed a7888f24009133fd3818355e35bfc5475c279e16 to ios-experimental. Build 54, run 40145860255: in_progress / pending; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40145860255

### Pikmin 1

- Current objective: Preserve working53, incorporate selected upstream campaign fixes, begin controlled online co-op development.
- What was investigated: Upstream release1.0.8 and main a6b09bfe, prior co-op/save notes, actual nectar_net and pc_netplay_session/pc_online_navi adapters. Last fetched origin matched8af39affa4c0c863ccaa1b41dd8b96538836faaa before edits.
- Root cause or leading hypothesis: Actual carrying retry used60 ticks regardless of user FPS, making intended2seconds=.5seconds at120. Several existing null/uninitialized/out-of-bounds/cache-lifetime hazards are confirmed in source. Main shared-edge rounding removes numeric rectangle gaps. These are preventive fixes; none is established as the cause of the old stranded pair, NaN/black world or motion-line symptom.
- Files changed: aiTransport.cpp retry/debug format; creatureMove.cpp collision-exhaustion null dereference; Demo.h/demoEvent.cpp/cinePlayer.cpp skipped Onion first-seed completion; SnakeAi.cpp/SnakeBody.cpp slot/array guards; dayMgr.cpp invalid-time fallback; damageEffect.cpp absent-captain guard; DrawContainer.h/drawMenuBase.cpp UI safety; drawGameInfo.cpp portrait-cache lifetime; pc_gfx.cpp rectangle edge math. New tests/pikmin1_upstream_safety_test.py. Separate libs/nectar_net/onion_authority.h/.cpp/test and CMake test registration; P1-only workflow checks.
- Tests and results: Actual-method fixture PASS for rectangle edges161200 cases/zero mismatches, first-seed skip/repeat/normal completion, missing/damaged captains, full/missing enemy mouth/target, invalid/dead carry target and retry timing30/60/120. Two negative controls restore old retry/rectangle behavior and fail as intended. Offline nectar_net15 test executables PASS with MSVC/O2/W4/WX; includes existing200000 decoder fuzz iterations,30SIMULATEDminutes with5% packet loss (live tick ratio.9982) and new10000 withdrawal/return cycles/40000 deliveries. No actual30-minute or two-phone session claimed. Preserved-display fixtures70 native-pixel checks,1820 touch/resize/layout checks, keyboard ownership PASS; scene contract26 + runner12 tests PASS. Clang warning/diagnostic checks also PASS for the actual-method fixture and new authority source/test. Apple ARM64/full game CI pending for this source.
- Confirmed working: User's installed53 sharper image, manual control edges, keyboard closed. At full2853x2007/1.00x with Ambient Occlusion OFF, user reports120FPS; keep higher quality and selectable120. New fixes are source/local-test verified only.
- Remaining issues: New source not installed/runtime tested; full story/rare cutscene/rescue/old black-world not certified. Co-op world replication, actor registry, engine transaction bridge, transport on iOS, full-screen per-player view, invites/relay, shared save/reconnect NOT implemented by the new accounting module.

### Pikmin 2

- Current objective: Preserve working game; prepare latest compiled package for Raye's solo compatibility test. P1 co-op first.
- What was investigated: Existing package hashes and bundle IDs; no new P2 source work in this batch.
- Root cause or leading hypothesis: No newly reproduced P2 bug; earlier audio/gameplay user-confirmed. Future upstream audit candidates remain queued.
- Files changed: NONE under games/pikmin2; existing P2 jobs/normal runtime unchanged.
- Tests and results: Build52 source a575ecf424008c7430da96a5082ffb7f68970dc1, run40131000336 compiled/IPA verified earlier. Copied package rehashed now; no new52 phone validation. Older32 audio/gameplay baseline preserved.
- Confirmed working: User's previous installed P2 audio/gameplay; do not equate this with testing newer52 on Raye's phone.
- Remaining issues: New phone/model/iOS details pending; assets/import + first run pending; stronger later cave/area/save/long-session test before P2 online.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port ; upstream SSunnKing same project.
- Branch: ios-experimental.
- Starting commit:8af39affa4c0c863ccaa1b41dd8b96538836faaa (clean local=origin).
- Latest commit: a7888f24009133fd3818355e35bfc5475c279e16 at report creation. Exact post-report local/remote hashes are in friendly Exact Resume State.json after push.
- Commits created:407b7fa4f5479aeeb983de5c84a234d03641291e P1 preventive batch; co-op/checkpoint commit pushed above.
- Changes pushed: Pushed a7888f24009133fd3818355e35bfc5475c279e16 to ios-experimental. Build 54, run 40145860255: in_progress / pending; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40145860255
- Uncommitted changes: Only this updated documentation checkpoint before final skip-ci commit; verify git status.
- GitHub Actions run IDs: Build 54, run 40145860255: in_progress / pending; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40145860255 Previous53=40133259493 P1 SUCCESS,52=40131000336 P2 SUCCESS. No P2 build requested now.
- Build results: Current local tests PASS; current Apple compile/IPA/runtime not yet established.
- Artifacts produced: No new IPA from this source yet. Working P153 SHA256c483540e76cef95c002578724690fe8ebe649901b9a09906350ee0b93c5cff85; P252 SHA256fbf6b2512d91ccafc6c600ee8bddcdbbcef04a1c01ee0ea68da4c68fda40c793. Rehashed copies in Documents/Open Nectar/1 - Install on iPhone/For Raye - Start Here, with manifest and instructions. Original IPAs retained.

### Next steps

- Next Pikmin 1 task: Review one P1-only native run and verify artifact/package before an optional short carrying/Onion-skip/menu/resume hardware check. Preserve53 rollback and settings. Continue co-op actor/world vertical slice on disposable data.
- Next Pikmin 2 task: Raye solo install/asset import and basic audio/pause/resume test; no speculative P2 rebuild.
- GitHub/build task: Inspect the recorded run after completion; no idle polling.
- Anything requiring my involvement: Raye's iPhone model/iOS and connection/unlock when ready for installation; sign in/verification stays under user's control. A read-only USB inventory probe stalled and was stopped; no phone identified or modified in this phase. No need to keep the original game/phone connected for CI.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Current user explicitly says start P1 online co-op; old notes saying online is future-only are historical/superseded. P1 ready for controlled prototype does not certify every story path. Preserve solo runtime; network flags remainOFF pending a real integration, not abandoned co-op work.
- Important source-file locations: ios/PIKMIN1_COOP_IMPLEMENTATION.md and ONLINE_COOP_DESIGN_NOTES.md; libs/nectar_net for reusable transport/identity/codecs + new OnionAuthority; games/pikmin1/pc_port/netplay/pc_netplay_session.cpp and pc_online_navi.cpp for old captain-only adapter; ios/SAVE_AND_COOP_RECOVERY_PLAN.md for exact-scene recovery target.
- Relevant logs: work/p1-upstream-safety.cpp/exe; work/p1-negative-retry.log and p1-negative-rectangle.log; work/coop-direct generated binaries; work/coop-start-actions.json and coop-start-pushed-actions.json; previous53 hardware/config evidence remains in friendly folder2.
- Unverified fixes: All new game-source behavior needs Apple build and device test; ledger isn't connected to actors or saves. No new IPA installation, full-world sync, internet service or autosave occurred.
- Risks and warnings: Do not enable old online menu and claim full co-op. Existing WorldDelta sends captain records only; other world state still needs sync. Direct networking alone cannot guarantee state-away internet/NAT traversal. Old Gekko frame/hash handle isn't a world snapshot. Normal memory-card save remains between-days; no arbitrary-tick card writes. No raw heap/pointer serialization. P1 global actor cap must be reconciled with independent per-player allowances. No finale spoilers. No full current phone-data backup claimed.
- Exact next actions: Native run → verified artifacts; Raye solo install/assets → two-phone same-Wi-Fi captain+squad vertical; stable entity registry/Onion engine bridge; host-owned Pikmin/jobs/enemies/items/obstacles + separate camera; retained-host reconnect/pause and versioned exact-world snapshots; private invites/real internet/relay tests; then stronger P2 stability and its engine adapter.

**END PROGRESS REPORT**


<!-- PRE-COOP HISTORY -->

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

## Current progress report — Build53 phone baseline and upstream audit — 2026-10-24 19:48 EDT

**Overall project status:** P1 Build53 user-tested: sharper gameplay, wider manual controls, keyboard closed. Current high2853x2007/1.00x with AO OFF reports120FPS. Large43FPS dip recovered after AO Off at the same1902x1338, then user raised to full native and still reports120. User explicitly retains high quality; no graphics downgrade/code/build needed. Upstream audit completed; proposed preventive fixes NOT implemented in this audit.

### Pikmin 1

- Current objective: Preserve working53 and compare original upstream for campaign stability fixes before broader solo/co-op work.
- What was investigated: User screenshots; two read-only settings captures; published release API/web pages; fetched1.0.7/1.0.8/main source; relevant current-iOS diffs including older missing carrying timeout. Actual current/tag/main rectangle arithmetic compared locally.
- Root cause or leading hypothesis: AO is strongly isolated as main observed slowdown (not resolution alone). Moving lines remain unidentified. Missing upstream carrying/collision/Onion/enemy/menu/cache/numeric guards confirmed in source; none established as cause of reported NaN/black world or stranded pair.
- Files changed: Documentation ONLY: PIKMIN1_BUILD53_HARDWARE_RESULTS.md, UPSTREAM_1_0_8_IOS_AUDIT.md and current journals. No game source, config, phone data or workflow changed; no new CI.
- Tests and results: Standalone actual map_gx_rect comparison161200 cases: current and1.0.8 tag33910 adjacent-edge mismatches, latest main0. This proves missing numeric correction, not visible iPhone symptom. Current-renderer8 relative-quality arithmetic checks PASS.53 prior native/package/simulator checks retained; user reports targeted runtime success.
- Confirmed working: Sharper game display, farther manual control positioning, unwanted keyboard closed, current high-resolution120FPS user report with AO OFF and GPI pack still enabled. Position save/relaunch persistence and long-session heat were not separately confirmed. Following feels better;53 did not introduce new AI changes.
- Remaining issues: Full campaign, stranded-pair rescue, slow/single-file return and prior black-world/NaN remain open. Lower-resolution moving lines only revisit if they persist with AO OFF. No guarantee120 across all scenes/devices/heat conditions.

### Pikmin 2

- Current objective: Preserve installed working baseline; audit future stability candidates only.
- What was investigated: Upstream gate lifetime, interpolated transition, save/card scheduler, sample formats/buses, host readable-memory bounds and allocator differences; prior1.0.6 backlog.
- Root cause or leading hypothesis: Current source lacks several upstream defensive fixes, but user has not reported those new symptoms. New GX bounds lookup is not drop-in on Darwin (/proc/self/maps missing). Port-argument ARM64 scalar fix is already present independently; avoid blanket audio replacement.
- Files changed: NONE in game/source. Candidate list saved in shared audit.
- Tests and results: No new P2 tests/build/phone results. Prior52 native/IPA SUCCESS retained.
- Confirmed working: User's installed gameplay/audio baseline;52 package verification only, not new phone proof.
- Remaining issues: Later stronger full-campaign/cave/save test; queued fixes need targeted iOS adaptation and tests, no current P2 update requested.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; upstream SSunnKing same project.
- Branch: ios-experimental; starting clean local=origin802cd294fb9fc088da1da5233687a7674d4e3c32. Fetched upstream source/tags without merging or checking out another branch.
- Starting commit:802cd294fb9fc088da1da5233687a7674d4e3c32; current tested53 sourcec25ba6a79ed975ba5face0461805bbd330e99cee.
- Latest commit / commits created: Documentation-only audit/hardware checkpoint pending commit; final exact SHA saved in external resume JSON after push.
- Changes pushed: Only scoped journals/audit/hardware report; skip ci. No upstream fix imported and no P1/P2 build triggered.
- Uncommitted changes: Scoped documentation until checkpoint commit. Private screenshots/phone configs/fixture binaries remain outside Git.
- GitHub Actions run IDs:53=40133259493 P1+startup SUCCESS;52=40131000336 P2+startup SUCCESS. No new run for audit or AO setting.
- Build results: Latest source package53 compiled/verified; user runtime feedback establishes targeted improvements, not full story. Upstream candidates are source-reviewed only.
- Artifacts produced: No new IPA. Verified53 retained folder1, SHA256c483540e76cef95c002578724690fe8ebe649901b9a09906350ee0b93c5cff85. Public latest-release metadata, exact source refs, arithmetic fixture evidence and private graphics comparison saved under work and friendly folder2.

### Next steps

- Next Pikmin 1 task: Keep working full-native/AO-OFF configuration. Prepare a scoped preventive batch from audit: high-FPS carrying wait, collision/Onion/array/UI/cache guards and edge rounding after meaningful tests. Do not blindly merge main or claim this fixes follower/NaN issues. User's current request was comparison; adoption remains next work.
- Next Pikmin 2 task: Paused; saved later gate/interpolation/card/audio/bounds checklist.
- GitHub/build task: No run now. Batch related tested P1 backports for one later P1-only native build; preserve53 baseline and iOS platform changes.
- Anything requiring my involvement: Nothing now; phone may close/disconnect. No need repeat whole campaign or lower resolution for resolved AO slowdown. If lines recur with AO Off, brief moving-camera evidence can distinguish possible causes.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User asked retain high-resolution finding, then explicitly requested upstream releases/source comparison. Latest public release1.0.8 publishedOct22, tag6319c3e354be280ab796f2c2e2504e185ce8cf96. Main a6b09bfe5a11798b2239d6072bace2e85812f245 Oct24 has seven later commits. Audit includes missing older carry fix3dcd6f25. No code backported yet.
- Important source-file locations: Full source-specific matrix in ios/UPSTREAM_1_0_8_IOS_AUDIT.md. Hardware evidence and effective relative-resolution notes in ios/PIKMIN1_BUILD53_HARDWARE_RESULTS.md. Preserve scene/FBO/Retina/menu/touch/keyboard fork fixes.
- Relevant logs: work/upstream-latest-release-oct24.json; fetched refs; work/audit_upstream_rect_edges.py, upstream108-rect-audit.cpp/exe, check_upstream_rect.cmd; current/tag33910 vs main0 mismatches. work/build53-quality-comparison.cpp/exe8 checks. Private work/p1-build53-graphics-20261024-193524 and p1-build53-ao-off-20261024-193828; friendly folder2/Build53 - Private Graphics Comparison.
- Unverified fixes: All upstream candidates NOT implemented/native-tested here. Numeric edge fix is only a candidate for user's moving lines. Current FPS is user-reported, sustained thermal/full-story performance unverified. No new save/autosave/network feature.
- Risks and warnings: Release notes mention edge/VSync corrections that are not actually in fetched1.0.8 tag; the relevant changes are in main2b65f16a. Main also introduces large custom mission/campaign/model/menu/save changes; do not import them as a stability patch. Upstream NETPLAY.md newly declares old network code disabled/unmaintained; that is source status, not an instruction overriding our user's future co-op goal. Do not assume existing netplay is production-ready.
- Exact next actions: Use audit priorities to implement/test one P1 preventive batch when continuing development; preserve existing enhancements and profile. Leave P2/graphics config untouched. Continue separate follower/NaN investigation. Report source, CI, IPA and phone milestones distinctly.

**END PROGRESS REPORT**

---
## Earlier checkpoint history


## Current verified package — P1 Build53 SUCCESS — 2026-10-24 17:53 EDT

User reported PASS; verified directly. Run40133259493/sourcec25ba6a79ed975ba5face0461805bbd330e99cee, startup job120989318144 and P1 job120991599668 both SUCCESS. This is the requested P1-only cumulative display/control/keyboard package. No P2 job or installed-app changes. Prior in-progress notes below are historical.

### Pikmin 1

- Current objective: Phone test53 for gameplay clarity/native landscape resolution, control edge placement/persistence/hitbox, and unwanted keyboard on startup/background resume.
- What was investigated: Full successful job log; exact run/source/artifact identities; package digest/ZIP/ARM64/platform/SDK/minOS/original standard P1 identity/icons/scene manifest and compiled scene selectors; actual generic simulator initial/background/resume evidence.
- Root cause or leading hypothesis:51 corrected portrait/logical-point render budget and editor safe-frame clamping.53 includes already-committed keyboard guard: iOS ends active/shown text input during gameplay while leaving the existing randomizer editor available. Exact original keyboard trigger still unidentified; guard runtime remains a candidate until user test. Prior NaN coordinates may relate to black world but root cause NOT established.
- Files changed: No new game/source change during this result-handling turn. Source53 contains P1 pc_window.cpp guard plus51 settings/window/gl/touch corrections and actual-code regression/workflow checks. Only result journals committed now.
- Tests and results: CI1820 actual layout/editor/persistence checks and70 pixel/migration/budget checks PASS; actual keyboard helper iOS+desktop host checks PASS and Apple syntax step PASS. Existing24 surface/140 route/283 walking/105 command and campaign/storage/profile regressions PASS. Full native compile/link/package PASS. Actual generic iOS27.1/iPhone Duo scene startup and same-PID background/resume PASS; does not certify game behavior.
- Confirmed working: Exact package generated and verified. Prior installed50 user-visible gameplay and earlier audio/content baseline retained;53 installation/runtime NOT yet reported. No assertion that all navigation or full campaign works.
- Remaining issues: Slow/single-file return and reported unrescued pair UNCHANGED; black-world/NaN origin UNRESOLVED. No such fixes in53. Native resolution1.00x may cost more GPU/memory; player retains resolution/scale/FPS choices incl120.

### Pikmin 2

- Current objective: Preserve working installed app; no new test/update required for current P1 task.
- What was investigated: No new P2 source or phone evidence.52 native/IPA verification already completed.
- Root cause or leading hypothesis:52 corrected the stale P2 pixel-budget test after shared51 source; no new reported P2 gameplay defect.
- Files changed: NONE.
- Tests and results:52/run40131000336 SUCCESS; verified P2 IPA preserved.53 built P1 only.
- Confirmed working: User's existing P2 audio/gameplay baseline remains authoritative, newer52 runtime unverified.
- Remaining issues: Full campaign and optional52 display/edge hardware checks remain unverified; P2 work paused while P1 prioritized.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; local C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental. Fetched clean local=remote d49e309013e35f93c81f00daf88c582ef272c378 at start of this result turn.
- Starting/latest commit: Starting journal d49e309013e35f93c81f00daf88c582ef272c378; verified build sourcec25ba6a79ed975ba5face0461805bbd330e99cee. Result-only skip-ci commit SHA recorded in external exact resume JSON afterward.
- Commits created / changes pushed: Only successful package/test/handoff documentation; no extra build requested.
- Uncommitted changes: Only scoped journal before result commit; no private evidence, IPA or game assets staged.
- GitHub Actions run IDs:53=40133259493 SUCCESS P1+startup;52=40131000336 SUCCESS P2+startup;51=40109396851 P1+startup SUCCESS/P2 obsolete host assertion FAIL. No active build requested.
- Build results:53 native tests/compile/link/package and generic simulator PASS; real phone installation/runtime PENDING.
- Artifacts produced: P1 artifact12576271886 ZIP SHA25692d6b8da27ea1e406f210e1234e8b0d3cfee09efb2a36bcc9325076783f5aa4c. IPA2835584bytes SHA256c483540e76cef95c002578724690fe8ebe649901b9a09906350ee0b93c5cff85; executable UUID92456923-027a-3544-9d20-51a2166eed02; original org.opennectar.experimental.pikmin1 unsigned ARM64 iPhoneOS SDK27.1/min15; approved icons/landscape/ProMotion flag intact. Staged folder1/Pikmin 1 - Build 53 - Display Controls and Keyboard.ipa with verification JSON. Scene artifact12576885117 ZIP SHA2565ff42ff3b41f48dc0db82292c676452ebe5a59ac71508d7532467f2b84a80a46 verified. Older51/50/42 and P2 packages preserved.

### Next steps

- Next Pikmin 1 task: User updates existing app same account/identity without uninstall/reset; follows folder1/Pikmin 1 - Build 53 - TEST THIS.txt. Compare actual landscape dimensions/game clarity at1.00x, manual control edge/save/reload/tap, Home Screen10sec/return twice and menus for keyboard, basic input. Do not ask full campaign solely for this test.
- Next Pikmin 2 task: None now; installed app untouched.
- GitHub/build task: No new run or idle polling. On phone regression use exact53 UUID above and bounded diagnostics. Future P1 work: trace NaN origin and improve stuck/slow return with evidence and meaningful crowded/oscillation tests.
- Anything requiring my involvement: Install/test53 when ready. No USB connection or open game required now. If still blurry send gameplay and Display screenshot; report keyboard/black event separately. Do not install51 first.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User explicitly requested this P1 build because guard was previously only committed while52 P2-only ran.53 now successfully packages it with all51 display/control corrections. Only package/source/host/simulator milestones established; hardware still pending. Keep scope clear and do not conflate P2 test cleanup with P1 runtime work.
- Important source-file locations: games/pikmin1/pc_port/pc_window.cpp pc_window_update_text_input/poll_events/set_window_size; settings rebuildResolutionList; gl pc_gfx_begin_frame; touch ButtonLayout.fullBounds/layout_place/load/save; tests/pikmin1_ios_keyboard_test.py; ios_display_layout_test.py; ios_pixel_resolution_test.py. AI/NaN diagnostics remain in aiCrowd.cpp/piki.cpp/navi.cpp and private Oct24 collected navigation report.
- Relevant logs: work/build53-result-run.json, build53-result-jobs.json, build53-artifacts.json, build53-p1-full.log, build53-verification.json, build53-startup-runtime-verification.json; work/verify_stage_build53_p1.py; outputs/Build53-Pikmin1 exact IPA/checked bundle/compiler log. Friendly folder2 copies of verification/full job/simulator evidence. Private phone evidence stays local.
- Unverified fixes:53 phone sharpness/edge persistence/keyboard behavior; no AI/black-world fix implemented. Prior single rescue log cannot identify the reported pair. CPU resource report says action NONE, not a crash diagnosis.
- Risks and warnings: Preserve original installed app/settings/content and player FPS choice. No complete current phone save/assets backup; package backups do not contain phone data. Do not force-push/main merge/reset/uninstall/upload assets. No spoilers.
- Exact next actions: User tests53; capture results and update journal. For failure retrieve matching current logs without overwriting prior evidence. Continue P1 recovery/NaN research; P2 stays paused. No new CI until relevant source correction warrants it.

**END PROGRESS REPORT**

---
### Earlier checkpoints (historical)


**DISPATCHED:** P1-only Build53/run40133259493, sourcec25ba6a79ed975ba5face0461805bbd330e99cee, startup job120989318144 IN PROGRESS at last inspection. Link: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40133259493. Contains native landscape pixels + manual control edges + keyboard ownership guard. Local keyboard iOS/desktop MSVC and Clang PASS; Apple compilation/new IPA and phone results PENDING. No new P2 job requested. No additional idle polling; user reports completion. Next retrieve logs and verify exact P1 IPA before staging. Old51 is preserved but user need not install it first. No AI/black-world fix claimed.


## Current action — P1-only package including keyboard guard — 2026-10-24 17:13 EDT

User explicitly requested packaging the pending P1 fixes now. Prepare ONE P1-only workflow run from current branch. No new P2 build is needed. Starting local/remote64f8276f95dbda7c9b660529579a24cbcbc315b1 clean and fetched.

### Pikmin 1

- Current objective: Produce a single standard P1 update containing all already-implemented display/control-placement changes plus the new keyboard guard.
- What was investigated: Confirmed P151 source contains physical landscape render budget/native migration and manual edge persistence; confirmed fb7880f6 adds pc_window_update_text_input before event polling and keyboard actual-helper host/Apple workflow checks.
- Root cause or leading hypothesis: Low portrait/logical-pixel budget and safe-frame editor clamp corrected in51. Keyboard guard defensively ends text input/shown IME outside the randomizer editor; exact UIKit trigger still unidentified. This is a candidate correction, not phone runtime proof.
- Files changed: Existing P1 pc_window.cpp keyboard guard and tests/pikmin1_ios_keyboard_test.py/workflow are already committed. This trigger changes journal only to build the current cumulative source; no fabricated additional gameplay fix.
- Tests and results: Actual P1 keyboard helper MSVC iOS/desktop PASS and Clang both variants PASS immediately before dispatch.51 actual pixel/layout/native game/IPA and shared simulator gate PASS retained. New Apple build/IPA/phone PENDING.
- Confirmed working: Prior installed50 visible game and one fresh/resume test;51 compilation and package verified, not user-installed. Prior rescue log contains one uncorrelated relocation, not confirmation of reported pair.
- Remaining issues: Slow/single-file following, reported missed two rescues, and black-world/NaN origin UNRESOLVED and unchanged in this candidate. Avoid presenting this as an all-bugs-fixed build. User FPS incl120 retained.

### Pikmin 2

- Current objective: None for this run; preserve working installed app and verified52 IPA.
- What was investigated:52 final native/tests/package and simulator metadata previously verified.
- Root cause or leading hypothesis:51 P2 test expected old699x323 budget; corrected52 actual2097x968 physical budget.
- Files changed: NONE in this run.
- Tests and results:52 successful;409 iOS/302 desktop and native/link/IPA PASS. No new P2 phone test.
- Confirmed working: User's older installed audio/gameplay baseline remains authoritative.
- Remaining issues: Full campaign and52 display/edge hardware validation pending; P2 update optional, not current priority.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental; start64f8276f95dbda7c9b660529579a24cbcbc315b1 local=remote, clean; no incoming change.
- Latest commit / commits created / changes pushed: P1-only build trigger with this journal is being committed now; exact source and run saved in dispatch checkpoint afterward.
- Uncommitted changes: Only scoped journal update before commit. Existing source/tests already committed.
- GitHub Actions run IDs / build results / artifacts: New P1-only run pending dispatch.52/run40131000336 sourcea575ecf424008c7430da96a5082ffb7f68970dc1 SUCCESS P2;51/run40109396851 source1450d21e1f60c9600c8556371e6f8f2f55cd7130 P1 and shared startup SUCCESS, P2 host test failed. Verified51 P1 and52 P2 IPA retained in folder1; new IPA not yet generated.

### Next steps

- Next Pikmin 1 task: On build completion retrieve logs and verify exact original-ID ARM64 IPA/scene/icons/digest, then stage ONE clearly named current P1 update in folder1. Ask user to test native landscape clarity, control edge/save/reload/hitbox and background/resume keyboard behavior. Do not require51 installation first: new successful package supersedes51 for this test.
- Next Pikmin 2 task: No new action/build/install now.
- GitHub/build task: Capture exact P1-only run/source/job; stop idle CI polling per user preference. User reports completion; no duplicate build.
- Anything requiring my involvement: Nothing on phone while build runs; phone/game may close/disconnect. No reset/uninstall needed. Test after new IPA verified.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User was confused because keyboard was committed but not built while a P2-only test retry ran. They now explicitly requested P1 build; package the already-tested cumulative source now, no need wait for AI/black-world work to finish. Explain unresolved issues accurately.
- Important source-file locations: P1 pc_window_update_text_input, pc_window_poll_events, pc_window_set_window_size; settings rebuildResolutionList and resolution migration; gl pc_gfx_begin_frame; touch ButtonLayout.fullBounds/manual placement/save/load; new keyboard regression/workflow.
- Relevant logs: work/p1-keyboard.cpp/exe, check_p1_keyboard.cmd, check_p1_keyboard_clang.cmd; earlier build51 and52 verification and private Oct24 phone diagnostics retained.
- Unverified fixes: Keyboard correction has only host verification until this new Apple build; all display/control/keyboard phone behavior pending. No AI/black-world correction implemented.
- Risks and warnings: Preserve installed apps/data and user-selected FPS; native1.0x costs more GPU/memory than old logical budget. No game assets/private data in Git. No force-push/main merge/reinstall/reset.
- Exact next actions: Dispatch P1-only, capture run/source, commit result-only checkpoint with skip ci; return build link and wait for user to report completion. After success verify and stage, then targeted phone test. Continue AI/NaN investigation independently when actively working, but do not claim this build includes those fixes.

---
### Previous checkpoint (historical)


## Current result and scope clarification — 2026-10-24 17:06 EDT

P1 is the active user priority. User explicitly clarified that “done” meant GitHub Build52 finished, NOT that P1 Build51 was installed. No new P1 hardware outcome should be inferred.

- P1 Build51/run40109396851/source1450d21e1f60c9600c8556371e6f8f2f55cd7130: native compilation/IPA and generic simulator startup/resume PASS. Changes ONLY correct physical landscape render resolution and manual control placement/persistence at screen edges. Verified original-ID IPA is folder1/Pikmin 1 - Build 51 - Native Pixels and Control Edges.ipa. Hardware sharpness/edge behavior pending. It does NOT include the keyboard guard, rescue/pacing changes, or black-world correction. Those problems may still occur.
- P1 keyboard guard: committed fb7880f66045035ec7cc53a945f34533a71c2c2c AFTER51 and AFTER52 source, host iOS/desktop helper tests PASS; native/IPA/phone pending, no package contains it yet. P1 stuck-pair, slow return and black-world root cause remain unresolved. Prior saved phone log had one uncorrelated rescue and later NaN captain coordinates. No claim of a complete fix.
- P2 Build52/run40131000336/sourcea575ecf424008c7430da96a5082ffb7f68970dc1: COMPLETED SUCCESS. Startup job120982491334 and P2 job120984917508 PASS. This retry changed only the test expectation after shared51 physical-resolution changes:699x323 old logical budget to2097x968 physical budget at.75.409 iOS and302 desktop actual-code checks PASS in CI, full game native/link/IPA PASS. No new P2 gameplay/audio change and no new user P2 bug report. P2 update is optional; keep working installed P2 untouched while focusing P1.
- P2 artifact12575447436 ZIP SHA256b21f25d5b14913dd4fae3eec73819c9121d5bec18c9660032ad853ae6357753e verified. Exact original-ID ARM64 iPhoneOS/SDK27.1/min15 unsigned IPA4161397bytes SHA256fbf6b2512d91ccafc6c600ee8bddcdbbcef04a1c01ee0ea68da4c68fda40c793, executable UUIDef989bd1-fc9a-37d2-92df-bc2bb62fe182. Approved icons and scene manifest/compiled selectors PASS. Staged folder1/Pikmin 2 - Build 52 - Native Pixels and Control Edges.ipa for preservation, not automatically installed.
- Scene artifact12575616448 ZIP SHA256e97a04ed04b706d54808b5c2c9a2c85cbe8d574a620961630f009d3a6a54be1b verified; actual generic simulator one-entry, landscape, foreign-event filtering and same-PID background/resume PASS. Does NOT certify either game's actual runtime.
- Repository fetched and clean local=remote fb7880f66045035ec7cc53a945f34533a71c2c2c before this result-only documentation update. This update uses skip ci; no new build. No phone modifications, private/proprietary uploads, P1 source changes or installation performed.
- Evidence: work/build52-result-run.json, build52-result-jobs.json, build52-artifacts.json, build52-p2-full.log, build52-verification.json and build52-startup-runtime-verification.json; outputs/Build52-Pikmin2; friendly verification/full-log copies in folder2.
- Exact next actions: Focus P1. Explain51 scope plainly; if user installs51, verify physical landscape Resolution/native1.0x clarity and control edge drag/save/reload. Existing keyboard/pacing/black issues stay tracked separately. Continue tracing invalid actor coordinates and recovery eligibility; next P1 fix batch should include already-committed keyboard guard with actual tests. Do not create another P2 build without new evidence. No idle CI waiting or further immediate phone-connection requirement. Preserve working installs/settings and all previous packages.

---
## Earlier investigation report (historical; current status above supersedes pending build text)


## Latest continuation — keyboard guard locally verified; P2-only52 dispatched

Build52/run40131000336/sourcea575ecf424008c7430da96a5082ffb7f68970dc1 is IN PROGRESS for P2 only after correcting the stale native-pixel fixture. No idle polling. Source parent cf4e959c;51 source1450d21e and its mixed results retained above.

After the report below was written, user provided a photo of the keyboard obscuring normal gameplay. Added P1-only pc_window_update_text_input in games/pikmin1/pc_port/pc_window.cpp, invoked before event polling: iOS stops text input/hides a shown keyboard outside the existing randomizer editor. Existing editor remains exempt, and desktop unchanged. This addresses text-input ownership defensively; the exact UIKit event that summoned the keyboard remains unidentified. Actual helper regression tests/pikmin1_ios_keyboard_test.py passes both iOS and desktop host variants. Next P1 workflow includes host variants plus Apple syntax check. Native and phone verification PENDING. This source is intentionally committed WITHOUT another build while52 runs; include in next P1 batch.51 staged IPA does NOT contain this new keyboard guard.

P1 root cause of NaN captain coordinates, black world, slow followers and missed rescues remains UNRESOLVED. No changes to movement/rescue/saving were made this turn. One fresh-launch and one background/resume check showed the world; that does not reproduce or solve prior black world. Existing evidence collected, user may close game/disconnect. No current further phone task.


**Date/time:** 2026-10-24T20:42:32.072908+00:00

**Overall project status:** Build51 completed: shared simulator startup/resume and P1 succeeded; P2 stopped on a stale host regression assertion BEFORE game compilation. P1 phone currently runs Build50 (UUID matches its CPU resource report). Latest user clips show improved but slow return and two reported stranded Pikmin. Black world with HUD remains unresolved. Phone diagnostics collected READ ONLY.

### Pikmin 1

- Current objective: Diagnose slow/single-file return, failed rescue, world-only black screen, and newly reported unwanted keyboard; preserve display/control improvements and settings.
- What was investigated: Both Oct24 clips sampled across38.47s and40.44s. Formation narrows on the cardboard crossing; some followers remain above the captain. Existing phone configuration/layout/navigation log and one CPU resource report retrieved without modifying phone files.
- Root cause or leading hypothesis: Rescue is ON (stuckFollowerRescue=1), Better Pathfinding ON, speeds100%, solo, textureGPI active,120FPS. Navigation log records ONE rescued_follower; cannot identify it as either reported stuck actor. Last recall entry has captain and target NaN coordinates. Invalid simulation coordinates could explain world-only blackness; initial source of NaN NOT found. Route budget two searches/second and conservative eligibility/safe spots may contribute to delays; not yet proven sole cause. No current crash report: CPU resource report says action taken NONE; not evidence of an OS kill. User fresh launch and one Home Screen10s/return preserved visible world; unwanted software keyboard then appeared and stayed.
- Files changed: No new P1 movement, rescue, renderer, keyboard or save source changes this turn. Previous51 native landscape pixel/control-edge changes retained. Private evidence NOT committed.
- Tests and results:51 P1 native compile/link/IPA PASS. Exact artifact digest, IPA ZIP, original standard identity/icons, ARM64 iPhoneOS SDK27.1/min15, compiled scene support/manifest verified. Generic scene simulator initial/background/resume PASS. No51 hardware test yet. Existing50 phone launch/resume visible once, not broad stability proof.
- Confirmed working: User sees game/HUD and better distant recall on50. Saved config confirms optional rescue enabled. One logged rescue occurred, without clip correlation. Earlier menu/control/audio baseline retained.
- Remaining issues: Two stranded actors NOT confirmed rescued, return pacing still poor; NaN origin/black world unresolved; unwanted keyboard screenshot during gameplay. No claim these are fixed by51. Native pixel/edge behavior requires installing51 then focused test; full story remains unverified.

### Pikmin 2

- Current objective: Restore CI validation after intended physical-pixel rendering change.
- What was investigated: Complete job120920446462 log retrieved directly. Assertion expected699x323 native render budget (logical932x430 at.75). New real code correctly derives2097x968 from physical2796x1290 at.75.
- Root cause or leading hypothesis: CONFIRMED stale regression expectation. This was a test failure before CMake/game compilation, not a newly observed compiler/linker or phone crash.
- Files changed: tests/pikmin2_ios_menus_test.py expected native pixel budget and explanatory comment only. Explicit user640x480/.75 and desktop expectations retained.
- Tests and results:409 actual iOS menu/render/input checks PASS,302 desktop checks PASS; Clang both variants with warnings-as-errors PASS. Other related test expectations searched. New Apple retry PENDING.
- Confirmed working: Previously confirmed P2 audio/gameplay baseline and50 native/IPA retained. Installed P2 untouched.
- Remaining issues: Re-run P2 native job, verify exact IPA if successful; phone native resolution/control edges/full campaign remain unverified.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental; clean matching cf4e959c5d2b9596cecaf39d8dd2409e8606e8dd at start; fetched remote before edits.
- Starting commit: cf4e959c5d2b9596cecaf39d8dd2409e8606e8dd.
- Latest commit: Build51 source1450d21e1f60c9600c8556371e6f8f2f55cd7130; upcoming P2-only test/journal commit exact SHA recorded in external checkpoint after push.
- Commits created: Scoped P2 regression/journal retry prepared; no speculative P1 fix included.
- Changes pushed: P2-only retry to be dispatched once tests/docs checked, exact source/run recorded separately. No duplicate P1 rebuild.
- Uncommitted changes: P2 fixture plus these journals until source commit. No private evidence/assets/phone files staged.
- GitHub Actions run IDs:51=40109396851 source1450d21e1f60c9600c8556371e6f8f2f55cd7130; startup120917764682 PASS; P1120920446401 PASS; P2120920446462 FAIL at host menu assertion.50=40003458275 all jobs PASS.
- Build results:51 MIXED. P2 corrected local fixture passes; new Apple compilation pending.
- Artifacts produced:51 P1 artifact12567035238; staged Pikmin 1 - Build 51 - Native Pixels and Control Edges.ipa in folder1,2835690bytes SHA2564cc90a7bacf02257c9df7b1f2c70534c7656e8f998a3ac19295ea0cfe84383fb, executable UUIDe845087d-e09e-3d8b-a89a-a9670aad56e9.51 P2 artifact12566495886 only error summary, NO IPA. Scene artifact12566192640 independently verified. Older50/42/32 IPA backups retained.

### Next steps

- Next Pikmin 1 task: Trace earliest invalid captain/actor coordinates; inspect collision/route/recall numeric boundaries. Capture bounded fresh navigation state if needed, with prior evidence preserved. Diagnose keyboard text-input ownership and close behavior. Do not call black screen fixed from one successful resume. Evaluate fair route scheduling and oscillation-aware stuck detection with actual method tests before changing rescue limits. No blind teleport or worker inclusion.
- Next Pikmin 2 task: One P2-only native retry for corrected expected physical-pixel budget. On completion retrieve full job, verify original-ID IPA, stage separately.
- GitHub/build task: Capture new run/source and then stop idle CI polling. Documentation-only updates use skip ci.
- Anything requiring my involvement: No further immediate reproduction needed; phone can close/disconnect after collection. If keyboard remains, force-close/reopen P1 as temporary workaround; do not reset/reinstall.51 update optional, contains only pixel/edge corrections, does NOT resolve AI/black/keyboard. No complete current phone-data backup made; configuration/layout evidence is not an assets/save backup.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User requested efficient continued work with~10min usage window. Phone connected/unlocked. First collector used denied container root; corrected to /Documents and succeeded. Do not ask user to unlock again for that path error. Installed P1 confirmed50 by UUID8b032bf3-2580-3708-886c-620a0ded22f7 in CPU report. No trap/crash report found for current world-black symptom. CPU53% average report explicitly action NONE; keep separate from44 startup trap.
- Important source-file locations: games/pikmin1/src/plugPikiKando/aiCrowd.cpp pcRecoverFollower/pcProtectFormationEdge; piki.cpp pcRescueFollowerNearCaptain/pcMoveFollowerRoute/pcSteerFollowerGoal; navi.cpp pcUpdateFollowTrail/pcTakeFollowerRouteBudget/callPikis; pc_port/pc_follow_trail.h stuck monitor; pc_follow_surface.h geometry; pc_follow_report.h bounded4 events/reason, overwrites on launch. Keyboard: SDL defaults text input active in SDL_video.c; only explicit P1 editor calls StartTextInput in settings rndTextInputOn/rndShareEnd. Root cause of unintended keyboard not established.
- Relevant logs: PRIVATE work/p1-feedback-oct24-20261024-163651, screenshots/recordings original user paths; local contact sheets work/clip-12-29-32.jpg and clip-12-30-58.jpg; work/build51-p2-full.log; build51-verification.json; build51-startup-runtime-verification.json; build51-feedback-run/jobs.json; verify_stage_build51_p1.py. Relevant copies in Documents/Open Nectar/folder2.
- Unverified fixes: No new P1 AI/black/keyboard fix implemented.51 native-resolution/edge change is compiler/package/simulator verified, hardware pending. Corrected P2 fixture locally verified, full Apple retry pending.
- Risks and warnings: No history rewrites/force push/main merge/uninstall/reset. No game assets or private phone data in Git.120FPS stays user-controlled; native1.0x costs more GPU/memory. No spoilers. Network/co-op/save redesign deferred per existing design documents.
- Exact next actions: Inspect pending P2-only run once user reports completion; don't poll idle. For P1 first fix unintended keyboard with explicit text-input ownership without breaking randomizer editor; trace NaN from earliest event with non-finite guards and timestamped actor/state diagnostics. Add crowd/oscillation regressions before pacing changes. Preserve51 package separately from current50 runtime evidence.

**END PROGRESS REPORT**

## 2026-10-27 — P1 co-op practice integration, before native build

User asked for continuous work until a meaningful build is submitted, larger batches, and preserving the installed P1/P2 baselines. Working tree starts at 8509f715. This batch connects the private, disposable-card practice area to the authenticated room, with two captains and separate small squads, a guest display, camera-relative input, pause/readiness, and explicit fail-closed behavior. It does not implement campaign co-op, enemies, Onions, internet, durable saves or seamless live reconnect. It has not run on either phone and its iPhone build has not yet passed.

Local checks: 25 network tests plus encrypted socket probe passed; actual host/guest capture/pool and captain visual fixtures passed; view/authority fixtures and 15 check-runner tests passed; changed game translation units passed a Windows Clang syntax pass using actual game headers. Full Apple compilation and physical behavior remain unverified. Guest may need assets already installed; the practice map uses locally owned original game material. P1 Build 68 is the previously accepted phone baseline; P2 is untouched. Practice uses process-latched disposable card storage: close and reopen P1 to return to solo. Preserve existing saves and settings.

Next: submit one P1-only native build, record its run and source revision, examine any failure logs and correct in batches. On success inspect IPA before staging. Phone test should begin only after successful packaging; first verify solo still starts, then both phones connect on the same Wi-Fi, each chooses Start Co-op Practice at title, Ready, and tries independent movement, throw, whistle, pause, and leaving. Do not claim these behaviors are verified until actually observed. Resume requires rebuilding the practice session after a disconnect for this first experiment; exact live rejoin and the full campaign remain planned.

## Build 77 dispatched

P1-only build 77, run 40579562780, source 02c3e5efa9ace37852db0d8b1d9859a653050ca6: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40579562780 . Status when dispatched: in progress; no IPA or hardware validation yet. Once the user reports completion, retrieve actual results/logs. If it passes, inspect the unsigned artifact and its identity before staging it in the user's accessible install folder. If it fails, batch the evidenced errors and preserve working P1/P2 installs. The user wants no polling while waiting and requests an audible notification when user action is needed.

## Build 77 failure and follow-up

Build 77, run 40579562780: startup passed; P1 failed before full application compilation. Actual logs show missing guest HUD methods in the view fixture, missing co-op input stubs in the extracted command fixture, and Apple's compiler rejecting ambiguous boolean precedence. Socket and room checks were skipped after the earlier failure, so their later gate errors were consequences. Fixed all three together; local view/authority, command scenarios and strict Clang checks pass. Room checks now collect independent diagnostics even after earlier failure. No IPA or device verification yet. Full log: work/build77-p1.log in the Codex workspace.

Build 78 dispatched: run 40582347682, source 0cc123675a5290f9e378500f4577695ec6581a36, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40582347682. In progress at last check; no IPA or hardware testing. Wait for user to report result, then inspect full diagnostics or verify artifact before asking for phone tests.

## Build 78 passed and first practice test prepared

Build 78 run 40582347682 source 0cc123675a5290f9e378500f4577695ec6581a36 passed scene startup, P1 app compilation, 21 practice checks, 13 room checks, encrypted simulator socket probe, and IPA packaging. Artifact 12772078241 SHA256 ae050af7909f5778ce3ee0f67666571602237691cd236da3935c8d16f0dc2ea5. Unsigned P1 IPA SHA256 bf64735ef2e90435d1dea5ec99fae37a183480c972aab77721d380d4923c9f02, device ARM64, bundle identity and icons verified. Staged in Documents/Open Nectar/1 - Install on iPhone/P1 Build 78 - Co-op Practice with START HERE - What to Test.txt. The user initially said fail but confirmed they had looked at something else. No phone install or gameplay verified yet; awaiting two-phone experiment. Practice uses disposable state, not a full campaign; reconnect after disconnect still requires both to reopen. Preserve Build 68 and existing P1/P2 data/settings. Full run log work/build78-p1.log, verification work/build78-package-verification.json.

## Background work while awaiting Build 78 phone test

Build 78 remains the staged test package and has not been installed or tested on phones yet. Ran the actual practice map compiler and virtual-file bridge locally against the user's private extracted P1 dataDir: map and stage produced in memory, generator suppression passed; no game assets uploaded or written to the repository. Added a practice-only whistle ownership guard so one captain cannot take the other captain's assigned Pikmin when idle or working; normal solo/local co-op remains unchanged. Local source-order test, ownership scenarios, and strict Clang passed. This guard is new source after Build 78 and is not included in the staged Build 78 IPA; validate it on a later batched iOS build and on hardware. Continue building co-op features while awaiting Raye; do not claim this fixes a hardware-observed issue.

## Rejoin foundation, not in Build 78

Added an inactive networking API for a host to retire a disconnected session, retain the existing room/listener, clear old peer events, and accept a newly authenticated compatible guest. It refuses to reset an active session, requires a new session identity and fresh baseline/readiness, and does not resume game simulation or integrate with the P1 UI yet. Local network suite 25/25 passed; real encrypted Windows loopback rejected an incompatible returning guest without closing the host room, then accepted a matching guest using the same code and refused to advance without a fresh baseline. In simulated tests, the mismatched guest can report Unreachable rather than Incompatible; it was still rejected, and the subsequent compatible rejoin succeeded. Actual iPhone rejoin, world reconstruction, host-loss recovery, and internet remain unverified. Logs: work/rejoin-core-network-guard2.log and work/rejoin-socket-mismatch.log. Existing Build 78 test package unchanged.

## Latest continuation checkpoint — after Build 78

Build 78 is staged for first physical two-phone practice testing; it is not full campaign co-op. While Raye was unavailable, local-only tests verified private-data map generation and subsequent source changes for practice squad ownership and disconnected-host room reuse. The newest changes require a held host world, reject delayed old-session packets, rebuild idle squad ownership, and require a fresh baseline plus both ready confirmations. 25/25 network tests, encrypted loopback and capture fixtures passed locally; Apple build and hardware behavior of these new changes are unverified. No seamless live reconnect UI or actual retained-world restore has been integrated. Next resume: conduct the staged Build 78 guide when both players can test; continue integrating and testing reconnect in a later batched P1 build while protecting original campaign saves, P2, settings and the Build 78 IPA. See OPEN_NECTAR_IOS_STATUS.md for logs and limitations.

## After Build 78 hardware test — resume checkpoint

Build 78 connected both phones but failed starting practice, showing host control initialization failure, peer disconnect, and another generic timeout. A source ordering bug was found and fixed: do not publish/confirm the first world until host controls are configured. Local network 25/25 and encrypted probe passed, including delayed 10-second guest entry; practice exit tests verify safe early return only before scratch save admission. Once admitted, a restart remains required to protect solo data. Distinct startup error messages are added, but the specific cause of the earlier generic timeout has not been established. Actual iOS build and both-device verification are pending. Preserve Build 78 and working P1/P2; submit and inspect a single P1-only build, then test both host orders, delayed tapping and safe exit. Collect no proprietary game data or secrets in Git.

Build 79 is in progress: P1 only, run 40606994758, source 925747d734ccb88b64ae6bff9fb0ef6f2623fa0e. User prefers to notify when Actions finishes; do not idle-poll. Verify logs and artifact after completion, then prepare the update and a focused two-phone test. Full return to title after scratch-card admission and actual live reconnect remain outstanding.

Build 79 passed, run 40606994758, source 925747d734ccb88b64ae6bff9fb0ef6f2623fa0e. Verified IPA staged with guide in Documents/Open Nectar/1 - Install on iPhone/P1 Build 79 - Co-op Practice Fix. Await two-phone installation and test; no runtime success claimed. After scratch-card admission, returning to title still requires closing and reopening P1. Live rejoin remains unimplemented.

## Build 79 hardware results and next P1 batch

Build 79 entered practice on both phones, but Raye saw mostly black, guest movement was stuttery, and host controls stayed frozen after briefly backgrounding. Both phones were read only; no persisted co-op log existed. New source rearms Ready after interruption, accounts for the full round trip in guest movement timing, suppresses story landing/tutorial movies in isolated practice, and writes a bounded local practice diagnostic for the next run. Tests passed locally: 25 network tests plus encrypted socket, sustained input delay simulation, and actual-source movie/resume fixtures. The movie explanation is a leading hypothesis, not proven. Next P1 build and iPhone retest pending. Return to title after practice card admission and live rejoin remain unfinished. Preserve P1/P2 app data and the working prior IPA.

P1-only Build 80 run 40616355146 source ebcce25120dec369eb8b2c051d6b5b39e7fbaf0b is in progress. Wait for user notification; inspect results and verify artifact before preparing the two-phone test. Includes leading guest black-screen fix, improved guest input timing, resume prompt and local diagnostics. These remain unverified on iPhone. P2 is not selected.

## Build 80 verified and co-op menu work — 2026-10-28

Build80 run40616355146 source ebcce25120dec369eb8b2c051d6b5b39e7fbaf0b passed; verified IPA in Documents/Open Nectar/1 - Install on iPhone/P1 Build 80 - Co-op Practice Fix. Raye's phone unavailable, so actual guest view/movement/resume remain unverified. PC local fixtures cannot substitute for the full two-phone practice game. User requests polished, game-like UI and broad multiplayer research, adding to all prior requirements. COOP_MOD_RESEARCH.md has sources, failure scenarios and detailed queue. Current source batch adds blue/gold scrollable UI, user-initiated Share Invite, avoids voluntarily disconnecting room when backgrounded, and explains which player needs to return or ready. Local room/source tests and ARC checks passed; native/UI phone validation pending. iOS may still suspend network; rejoin and host migration are not implemented. Keep P1/P2 data and solo settings intact. Next build P1 only for the integrated UI batch, verify artifact and offer single-phone menu test; later both phones test actual co-op.

P1-only Build81 run40711881021 source e65708c71626b04fccdd8265afe2dfcb1cdeb42c is in progress. UI and interruption changes require Apple compile and real-device tests. User will report completion; do not idle-poll. If passed verify/stage IPA; one phone can check UI and solo, real guest practice still needs compatible second device. Full co-op vision, research links and remaining queue are in COOP_MOD_RESEARCH.md and COOP_OBJECTIVE_QUEUE.md.

After Build81 was submitted, added a standalone, currently unused visual-frame blend candidate; tested locally (26/26 network, encrypted loopback, strict Clang). It cannot yet smooth the actual game. Further work must design visual clock/buffering, unchanged host authority, snap/teleport/actor lifetime behavior, pause/background and local-camera responsiveness before integration. Build81 does not contain this candidate; review its actual result independently. Sources and limitations are in COOP_MOD_RESEARCH.md.


### Co-op interruption audit (2026-10-28)
- P1 room and practice lifecycle observers now track the active game window's UIScene notifications, scoped to that scene. UIKit's scene lifecycle differs from application-level lifecycle callbacks. This is a preventive correction, not a proven explanation for Build 79's freeze.
- Practice continues to pause on interruption and requires the existing readiness flow; room code does not intentionally close the link. iOS may suspend networking, so live reconnection remains unimplemented and unverified.
- Local source contract checks cover observer scoping; iOS compilation and real-device interruption/reconnect behavior remain unverified. Build 81 predates this change.
- Apple references: https://developer.apple.com/documentation/uikit/uiscene/willdeactivatenotification and https://developer.apple.com/documentation/uikit/uiscene/didactivatenotification


Build 81 run 40711881021 completed SUCCESS at source e65708c71626b04fccdd8265afe2dfcb1cdeb42c. P1 artifact 12829465661 exists; downloaded and validated; staged at Documents/Open Nectar/1 - Install on iPhone/P1 Build 81 - Co-op Practice. Not yet tested on phones. Post-build scene lifecycle work (be4d3da8) and isolated visual blender (8f5544f0) are not included.

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


Additional weak-connection test: under an artificial four-second one-way reliable delay, the local test session times out, freezes host authority, refuses guest commands, and does not silently revive merely because delivery resumes. This is a simulated result, not proof of device behavior or live rejoin. The simulator also resets old ordering deadlines when a new connection replaces a disconnected one. Tests added after Build 82.


### Clearer co-op join errors (after Build 82)
Room join messages now distinguish known game, region, build, game-content and capability mismatches, and report failure to initialize the network separately. Unknown mismatches remain generic. The existing compatibility gate and independent personal settings are unchanged. Source contract check passed; native iOS and device UI validation still required. Not included in Build 82.


2026-10-28: User added co-op cutscene/story requirements without changing the active task. P1 source audit and non-spoiler design/test checklist are in `ios/COOP_CUTSCENES_AND_STORY.md`. Scene synchronization is not implemented or phone-tested; practice deliberately skips campaign scenes.

2026-10-28: Rebuilt and ran the full local network suite after the simulator changes: 27/27 passed when loopback networking was available, including encrypted transport and stress tests. A first restricted run could not establish the encrypted loopback and was interrupted; the rerun passed. This is not an iPhone or real-internet test.


### Build 82 verified and Build 83 submitted (2026-10-28)
Build 82/run 40720211222 succeeded at 176615ea791ba6bd5bd182672448466c953176ff. P1 artifact 12831464151 verified: ZIP SHA-256 d727bdbb119070e8985f2a06d3258383195b71ffbf26a60c361f9036c15fc04c, IPA SHA-256 69a52b4f7b2983d3b0c78c0d2591d6d82f5a6b901186b010a73c140d1556fb4b. 21 practice, 13 room, encrypted UIKit simulator and ARM64 packaging checks passed. Staged in Documents/Open Nectar/1 - Install on iPhone/P1 Build 82 - Co-op Interruption Fix. Not phone-tested.

P1-only Build 83/run 40727018878 at 74eb8c0aba1662676d08267819f4c39182161212 was submitted and in progress: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40727018878 . It groups post-82 stale-action expiry, invite concealment, clearer join errors, shared-Onion zero-epoch validation, and network test changes. Local 27/27 suite passed; iOS and hardware results pending. Story/cutscene plan is documentation only; the visual smoothing helper remains unintegrated. P2 unchanged.


### High-delay room feedback (after Build 83 submission)
The room screen now gives a plain-language warning when measured round-trip delay is at least 200 ms and notes that controls may feel slow. This is an advisory threshold, not a guarantee about responsiveness, loss, or other networks. It does not alter player FPS or quality. Source presentation contract passes; native iOS and phone testing pending. Not in Build 83.


### Isolated ICE compile experiment (2026-10-28)
Pinned GameNetworkingSockets d534c19aa760df3fb75fd20db13ba1932b8a5463 has native ICE source and iOS platform configuration. An isolated Windows static-library build with `ENABLE_ICE=ON`, `USE_STEAMWEBRTC=OFF` and existing pinned protobuf succeeded (44 build steps; `work/local-net-win/ice-probe-build`). The first restricted Windows compiler probe failed C1902 before compiling source; a retry with normal toolchain access passed. This is Windows compile-only: no P2P session, iOS build, signaling, STUN/TURN service, relay, or internet/device test. The production iOS dependencies remain ICE=OFF, and the current transport uses `CreateListenSocketIP` / `ConnectByIPAddress`; enabling the flag alone would not switch it to the P2P signaling API. No existing app, dependencies or saves were modified. Valve guidance: https://github.com/ValveSoftware/GameNetworkingSockets/blob/master/README_P2P.md


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

Shared-Onion foundation follow-up: locally tested competing same-tick requests in both host-processing orders; only available stock is granted and no duplicate is created. Campaign engine integration and real-phone behavior remain untested. Test added after Build 84 submission.


### Upstream comparison (2026-10-28)
Fetched upstream/main 77a5aaa4, with releases through 1.1. Upstream changes include P1 seed landing, P1/P2 card atomic-write work, P2 local co-op cinematic fixes, P2 missing-audio fix, and desktop/Android menu and launcher changes. Do not wholesale merge: our iOS renderer, touch, save isolation and networking differ. P2 audio was already user-reported working on our build; upstream P2 changes require separate comparison and testing.

P1 source has the steep-wall seed push already, but snapped seed landing at 30 FPS as well as 60/120. Adapted upstream commits 33b5abc7 and aa18d8a4: retain the existing steep-wall push, preserve original 30 FPS bounce, and keep higher-FPS ground snap. Upstream's small decision tests passed locally and the actual itemAI translation unit passed local real-header Clang analysis with existing Windows deprecation warnings. Workflow now runs the test in future P1 iOS builds. The change is not in Build 84 and has no iOS build or device validation yet.

Upstream atomic card writes are not yet imported: our current P1 card layer includes separate practice-save isolation and concurrent I/O guards. A safe adaptation must test old-save preservation, metadata consistency, short/full disk writes, rename failures, delayed worker jobs and interrupted save stages on isolated fixtures before any integration. No claim that a simple file flush guarantees power-loss durability.


Save safety follow-up: P1 `CardUtil::DoSave` creates a `~` temporary game-card file, writes and sets metadata, deletes the old file, then renames the new one. `DoList` has a recovery path that tries to restore a valid temporary file; when the final name already exists, a failed rename can result in the temp being deleted. Both the temp metadata and recovery behavior matter. The upstream file-level temp/replace change is not by itself proof of an atomic entire save transaction or durable power-loss safety. The current fork has process-latched practice routing and recursive I/O synchronization; preserve those and existing saves. Next build isolated tests from the real `DoSave`/`DoList` and CARD backend with failure injection at each stage, both channels and stale/delayed workers, then evaluate a minimal adaptation. Do not switch routes or alter installed phone saves for these experiments.


### Isolated P1 interrupted-save recovery test (after Build 84)
Added `tests/pikmin1_card_recovery_test.py`, which extracts the actual `DoSave` and `DoList` functions and links the actual P1 CARD backend to isolated temporary fixtures. It injects failures before create, write, status, old-file delete, and final rename, then invokes real listing recovery and checks that the complete expected old or new bytes remain accessible. Local Windows fixture passed for these controlled stages; no actual phone files were opened or changed. This does NOT simulate failure partway through a write, filesystem rename, metadata pair, OS termination or power loss; it does not prove durable/atomic saving. The new test is included in the next P1 native-build check, not Build 84. Upstream atomic card-write adaptation remains under investigation and was not applied.


Save-recovery fixture expansion: in addition to failures before each stage, it now deliberately writes half of a temporary test save then reports an error, and models errors reported after metadata update, old-save delete or rename have completed. In isolated Windows fixtures, actual DoSave/DoList and CARD backend recovered a complete expected old/new file for all ten scenarios. This deliberate half-write model is not an actual interrupted stream, OS crash, filesystem metadata failure, sudden power loss, iPhone test, or proof of full durability. Real saves were not touched; upstream atomic backend remains unmerged.


### P1 interrupted-save preservation guard (after Build 84)
A controlled fault fixture using actual P1 `DoSave`, `DoList`, and CARD backend showed that if the old save had been deleted and the remaining temporary file's metadata was missing, the previous recovery scan deleted that remaining file. Another simulated case truncated the remaining temp below the comment size. Source now refuses to promote a too-short temporary file and, when its final save cannot be confirmed present, returns an I/O error while preserving the temp rather than deleting it. Existing cleanup when a final file opens remains in place. This is not automatic repair and may surface a card error requiring recovery assistance.

The independent local fixture covers 12 normal/interrupted/simulated partial or missing-metadata cases; both negative-control variants fail when their respective guard is removed. Actual practice card admission fixture still passed. Real-header Clang also identified a pre-existing potentially uninitialized card-worker result for an unexpected command; PC code now initializes it to a fatal error before dispatch, and that analyzer warning disappeared. Other existing warnings remain. No real phone/save files were modified; no iOS build, crash/power-cut, or hardware behavior has been verified. Upstream's atomic write patch is still not applied.


Save-recovery follow-up: the isolated fixture now also forces recovery rename failure with no final file and a failure checking a final file that does exist. In both cases the preservation guard reports an error and retains the temporary file; the existing final file remains when present. Fourteen modeled scenarios pass locally. These tests simulate errors in controlled wrappers; they do not establish actual power-loss durability, automatic repair, or iPhone behavior.


### Independent recent-development audit (2026-10-29)
Reviewed recent practice/save/iOS/network changes through 37a0e779 against fetched origin. No confirmed new critical regression found within this bounded audit. Independently reran 27/27 local networking tests, regenerated/compiled/passed 14 isolated save recovery cases, seed test and menu source contract. Build84/run40773579467 is SUCCESS at 4a886468; its IPA was not inspected in this audit. Post84 source still needs iOS compilation; recent phones have not verified guest view/stutter/interruption fixes. Foundation tests do not establish delivered campaign co-op or internet traversal. Full findings and exact next priorities: ios/RECENT_DEVELOPMENT_AUDIT_2026-10-29.md. No gameplay changes or phone/save operations during audit.


### PC practice diagnostic partner (2026-10-29)
Added opt-in standalone tools/practice_companion.cpp (under libs/nectar_net), profile generator and simple Windows launcher. PHONE-host mode receives actual actor frames and can send controlled walking; PC-host mode publishes a simple two-captain/24-Pikmin fixture to test the phone guest display and input. Real room authentication, compatibility gates, bootstrap and session code are reused. The PC fixture is not the game engine and does not test combat/AI/campaign saves or arbitrary-internet traversal. No existing iOS engine/UI/P2 code changed or phone installed. Local 28/28 networking tests (including staggered-start companion encrypted loopback), 4 profile hashing tests and CLI/profile/launcher checks passed; phone behavior remains unverified. Prepared matching diagnostic profiles for phone Builds78-84 using artifact headers and the real local base assets. No new iOS build is required to try an already installed supported build. Exact instructions and limits: ios/PC_PRACTICE_COMPANION.md. Post84 save/seed/input source still needs a future batched iOS validation.


### Build84 package and single-phone test preparation (2026-10-29)
Connected phone metadata exposes only 0.1.0/version1, so the installed build was NOT determined. User authorized proceeding and phone is connected/unlocked. Read-only USB collection backed up and hash-verified five current settings/layout/achievement/save files; private backup retained under Documents/Open Nectar/5 - Backups and Older Files/P1 Before PC Partner Test with timestamp. Build84 artifact and complete package checks passed: 21 practice, 13 room, encrypted UIKit simulator, ARM64, icons/notices; IPA SHA256 4db1e9ee113ffbb6ca8e97e58a397fae29a6f4dee577d02cbc96f2de19e255dd; executable UUID d10b5921-e13a-34b5-a348-4dd70cbcb9fc. Staged Documents/Open Nectar/1 - Install on iPhone/P1 Build 84 - PC Partner Test/Pikmin 1 - Build 84.ipa. In-place Sideloadly update using existing identity requested; NOT installed/phone-tested yet. PC partner's Build84 profile is ready. Next: user confirms install, then Test A (phone hosts) and Test B (PC hosts) with same LAN. No Raye phone needed. Existing post84 source changes remain locally validated only.


### Clarified full PC/iPhone co-op and required mid-day recovery (2026-10-29)
User clarified that a keyboard-only diagnostic partner is insufficient: the full P1 game must run and display independently on both participants, supporting PC+PC, iPhone+iPhone and mixed PC+iPhone, either device hosting. Seamless continuation of the shared campaign between PC and iPhone is part of the target. Mid-day autosave/recovery is now REQUIRED for the finished mode, superseding any earlier plan to accept only restarting the day after closing/crashing. Account explicitly for incoming phone/FaceTime calls, full-screen interruptions, locking/unlocking, backgrounding, accidental swipe-close, guest/host crash and transport loss. Temporary interruption should hold authority and require readiness on return; process death requires a previously durable validated checkpoint, not a promised final background save. Plan periodic versioned full-world snapshots with retained last-known-good generations, bounded rollback, verified commit and shared-campaign identity/ownership protection. Exact save interval and safe coverage of clock, actors, AI/jobs, parts, Onion stock, scene/story and RNG remain implementation/measurement work; current actor visual packets are NOT sufficient save snapshots. Do not claim this works until actual capture/restore and crash/relaunch/device-switch tests pass. Guest backup of accepted recovery data is a future safety option, not implemented host migration.

The phone-host/PC diagnostic guest test on Build84 was user-confirmed visible and movable with Louie visible; automatic guest movement looked mostly smooth with some possible stutter (user uncertain). Measured LAN RTT about3-4ms with live actor frames. PC pause correctly blocked the host from resuming alone. No actual iPhone guest display test completed. Ended the diagnostic peer on user clarification. Unfinished native keyboard-controller prototype preserved only in workspace work/manual-controller-prototype; not a delivered full PC client.

Next engineering step: build real Windows P1 from the shared fork, expose the same retained-room/practice adapter in desktop UI, and produce paired compatible PC/iOS builds. Existing upstream desktop online menu uses a separate disabled path; do not silently enable it or assume compatibility. Windows game expects MinGW; no local MinGW/WSL environment is available yet. Evaluate isolated portable compiler or dedicated experimental CI cross-build rather than changing the user's OS. Campaign snapshot/transfer design and tests remain queued alongside this integration.


### Full Windows/iPhone practice integration candidate (2026-10-29)
Implemented an opt-in NECTAR_DESKTOP_COOP_ROOM frontend in the FULL Windows P1 game, using the shared HostRoom/GuestJoin/CoopConnection and existing actual-engine practice runtime. Windows title Online Co-op exposes native host/join/code/practice controls; the actual game renders and accepts its own mapped keyboard/controller input. No diagnostic profile identity borrowing is used. Preserves early authenticated scene messages in the same owner through handoff. Desktop focus loss clears movement and blocks shared practice; explicit Ready returns to the game. Current practice end/rejoin still requires process restart after isolated card admission.

Native Windows content hashing was implemented with the exact iOS NFC/UTF16 ordering/domain/framing. Strict MSVC compile of frontend passed; actual Windows content golden, NFC/NFD equivalence, changed-byte/empty/missing-root tests passed. Real local 3463-file tree produced 26719287a52022d2ced07b74edb4c7a990c310e8554a63e91deec87652bfb8ba, matching the independently prepared iOS-format identity. Actual extracted title/modal source fixtures passed in normal desktop, native iOS and desktop-coop modes. Existing iOS room presentation contract passed. This is NOT a full Windows game link/start/runtime or mixed-device result.

Added a dedicated experimental Windows workflow (read-only repo permissions) and isolated Linux/MinGW cross-build script, using existing pinned networking sources and official SDL2 2.32.10 source SHA256 5f5993c530f084535c65a6879e9b26ad441169b3e25d789d83287040a9ca5165. Builds a Windows full-game EXE, not the earlier headless helper. The Windows/iOS builds must be paired at the same source identity; installed84 is not a matching counterpart. The pending paired iOS build also includes previously locally-verified post84 seed, input and CARD recovery changes. P2 remains untouched.

Required interruption/mid-day autosave/cross-device campaign requirements and acceptance tests are in ios/COOP_MIDDAY_RECOVERY_REQUIREMENTS.md. They remain UNIMPLEMENTED; practice has no shared campaign or complete durable snapshot. Next: submit paired builds, inspect both results and artifacts; if successful stage a separate PC game/assets/settings/save folder, perform user-controlled Windows solo/render/audio/input smoke test, then mixed-device practice in both host roles before campaign/snapshot development. No phone needed during compilation; user may close P1/disconnect.


### Paired full-game build submission (2026-10-29)
Source 2b7abe8d40675a78d76ba50f77f41e666ce20858 pushed and both workflows are in progress: iOS P1 Build85/run40896542118 https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40896542118 ; experimental full Windows P1 Build1/run40896542358 https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40896542358 . These are a matching source pair; source is NOT yet CI-validated and no PC EXE/new IPA has been verified or installed. User may close P1 and unplug while compiling. Do not idle-poll; user reports build completion. Next inspect both workflow results and complete logs if failed; if successful verify artifact source/identity, stage isolated full Windows game with copied original assets and private separate config/save roots, and prepare the matching iPhone IPA. Do not replace the installed84 until the candidate artifacts are verified. Autosave/recovery remains requirements-only and must not be advertised as finished.


### Windows Build1 failure diagnosed and packaging fix (2026-10-29)
Run40896542358 Windows content check PASSED and full MinGW game build compiled/linked all555 steps, including the desktop frontend. No compiler/linker failure caused this run to fail. Actual failure was post-link `cp: cannot stat .../deps/share/nectar-net/licenses/*.txt`: the dependency script creates that installed notice directory only for iOS. The final EXE package was not uploaded, so Windows runtime remains unverified. Complete job log downloaded to workspace work/windows-coop-build1.log (job123527456955).

Fixed packaging through scripts/package-windows-coop.py using original notices from the actual pinned extracted dependency sources; added preflight for all8 required notices before the heavy build, and a complete recursive file-hash receipt after runtime DLL staging. Four controlled local packaging tests passed (paths, missing notice, complete package/receipt, missing identity). A local Bash syntax check was unavailable because no Bash executable is installed; actual Bash execution remains pending in the retry. No gameplay or iOS source changes. Independently recomputed current gameplay fingerprint04fd0786b221591f28d4c695410ba9459510dc2d39527eac44cc1cde82b307b9, exactly matching the full Windows Build1 compile; therefore the retry remains compatible with iPhone85 if that passes. Retry Windows only; do not rerun iPhone just for packaging.

Windows-only retry Build2/run40899127561 is in progress at source11fbbc88: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40899127561 . iOS workflow run86/40899127677 was SKIPPED as expected (no iOS build marker), not a new compiled candidate or failure. iPhone85 remains the paired build. Check Windows2 package/runtime dependencies and matching fingerprint before staging. No user phone action until artifacts verified.


### iPhone85 gate failure and Windows2 verification (2026-10-29)
Windows2/run40899127561 SUCCEEDED; artifact12908732335 downloaded and ZIP SHA2569f1746a0e3aa3c71a52dce6c0511cdc0d0b091ff5402ab6a5a0e605d0a127970 verified. All14 receipt entries, x64 PE architecture/import closure and source fingerprint04fd0786b221591f28d4c695410ba9459510dc2d39527eac44cc1cde82b307b9 verified. EXE SHA2569b4d768096bd715258886b487c52fe64b799dd3f414399517ef8da01a3277a26. No game launched yet; extracted under workspace outputs/P1-Full-PC-Coop-Build2.

iPhone85/run40896542118 FAILED AFTER successful full game compile, real UIKit startup, encrypted socket probe, practice checks and bundle preservation. Actual blocker: two tests in tests/ios_room_checks_runner_test.py expected2 mode compiles, while the real fixture now correctly runs3 (desktop, native iOS, desktop-coop). Runner tests failed before the actual13 room checks were run, so result.json did not exist and the mandatory gate correctly blocked packaging. Native room checks must still run successfully; do not bypass them or install a manually packaged85. Full log work/ios-build85-full.log; failed-job123534677251; preserved artifact12908687983 ZIP SHA25674ff3d37adc16604c853b0d81a8545b896ea13dae84524b169d51747cc7d6ec6 downloaded for evidence/recovery only.

Fixed runner tests to cover all3 independent modes and ensure failures never execute stale binaries, including an explicit desktop-coop-only failure case. Ten runner tests passed locally; actual extracted room/title fixture compiled and ran successfully in all3 modes. Changes are tests/docs only and keep gameplay identity unchanged, so Windows2 remains compatible. Submit iPhone-only retry; Windows2 does not need rebuilding. Phone84 remains installed/user-tested; no newer iPhone IPA ready yet.


### Full PC game staged; iPhone87 submitted (2026-10-29)
Full verified Windows2 game staged in Documents/Open Nectar/4 - Windows Version/Pikmin 1 - Full PC Co-op - Experimental. PLAY PIKMIN 1.cmd launches the actual game, with its own Game settings, independent Saves and Logs/last-run.log. Copied and SHA256-verified3520 original asset/art files (656443576 bytes); originals, existing Windows download and phones unchanged. Executable and all package files verified. No optional packs or phone configuration imported. Not launched or runtime-tested yet; user should check title, music, controls and a short solo view first.

iPhone-only retry Build87/run40902351675 is in progress at source312a5920: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40902351675 . Test/docs-only fix retains Windows2 gameplay identity. Windows workflow3/run40902351634 is SKIPPED as expected, not a replacement for successful Windows2. Next: inspect87 result/artifact, verify all native receipts/package/fingerprint, stage matching IPA; then user-controlled real PC/iPhone practice in both host roles. Actual shared campaign, mid-day autosave/recovery, cross-device progress remain unfinished. Do not claim build success proves runtime.


### First full Windows launch failure: staged asset paths (2026-10-29)
User reported a grey nonresponding window. Read actual Logs/last-run.log: SDL/OpenGL context, NVIDIA GPU and shaders all initialized; JAudio repeatedly failed DVDOpen for assets/dataDir/SndData/Seqs/pikiseq.arc and assets/dataDir/SndData/Banks/pikibank.bx. Staging had copied dataDir at Game/dataDir, but actual DVD backend prefixes ALL original paths with assets/. This was a local staging mistake, not a compiler or confirmed GPU failure.

Stopped only the exact experimental process identified by its full executable path, before title/gameplay. Archived first startup log locally. Added scoped non-cyclic Game/assets/{dataDir,art,banner&icons,Debug,plugins} junctions pointing to the existing copied sibling folders; originals were neither moved nor duplicated. Verified missing startup files through mapped paths against their original SHA256. Kept the real Game/dataDir for the desktop content scanner (which correctly refuses reparse roots). Updated PLAY launcher to refuse launch before the two mandatory audio files exist. No new build or source/gameplay change required. Runtime RELAUNCH STILL PENDING: user must open PLAY PIKMIN 1.cmd and confirm title/music/controls. Do not claim this is fully fixed until logs/user confirm successful startup.


# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-29 14:35 EDT

**Overall project status:** Full Windows P1 Build2 is now USER-CONFIRMED running well after the local asset-path correction. PC graphics packs installed and enabled; their actual rendering and RTSS overlay need a new user check. iPhone87 failed in simulator installation before the device game build. Source now adds a separate PC Recall All key, locally verified; paired builds will be submitted together.

### Pikmin 1
- Current objective: working full PC/iPhone practice pair, optional PC visual content and missing PC Recall All input.
- Investigated: actual saved keyboard bindings, desktop non-touch recall guard, model/texture paths, actual RTSS SDK/profile state and iPhone87 failure diagnostics.
- Root cause: Recall All's consumer was compiled only with touch support. Current PC2 has no Recall All key. Charge is C; R lock-on; T/F/G/H are the original directional squad-steering controls. RTSS global OSD was off and no P1-specific profile existed; borderless itself does not enable the overlay.
- Files changed: pc_window.cpp/.h, new pc_recall_input.h, navi.cpp, settings/pc_settings.cpp; tests/pikmin1_command_test.py plus new pikmin1_pc_recall_test.py; the two experimental build workflows only add required PC recall checks. Original saved binding indices0-25 retained; new index26 defaults F6 and can be remapped. Recall remains a separate solo cheat, default off; existing touch control and normal whistle preserved. Menu/focus cancellation, release-before-rearm and250ms expiry prevent stale commands.
- Tests/results:20 real non-touch consumer/input scenarios and110 actual command/recall/cursor/edge scenarios passed under strict MSVC. Scene runner12, room runner10, package4 and source identity2 tests passed locally. One identity test attempt hit Windows test-temp permissions; rerun using writable work/test-temp passed. No full native compile or hardware validation of this source yet.
- Installed locally: original verified texture ZIP downloaded from exact existing Open Nectar launcher URL, SHA256 5d9254b4f1ca46fee93b57ce17e888521884634bc1fae4bc7a4cf22af7e2551b;3046 PNGs extracted only,15 NHM models and3 portraits from existing verified character bundle. Enabled GPI textures and HD model mask0. Backed up settings in C:\Users\chazz\Documents\Open Nectar\4 - Windows Version\Pikmin 1 - Full PC Co-op - Experimental\Backups\Before HD Content - 20261029-142650. PC saves hash-unchanged; original game assets/apps unchanged. Full manifest: HD CONTENT INSTALL RECORD.json in this PC folder.
- RTSS: prepared one executable-specific profile, installed after Windows administrator approval; SDK readback EnableOSD1/AppDetectionLevel1, global profile hash unchanged. Actual visible overlay not yet verified. No game input sent by Codex.
- Confirmed working: user says full PC game works very well; observed saved log ended normally. Prior accepted phone solo baseline retained. Remaining: pack/overlay visuals, new F6 key in compiled build, cross-platform runtime and larger co-op scope.

### Pikmin 2
- Objective/status: preserve user's last confirmed working phone version. No P2 edits/build/install/test this batch; earlier audio fixes retained. No new runtime claim.

### GitHub
- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; branch ios-experimental.
- Starting commit:4042b7b8, synchronized with origin after fetch. No pre-existing uncommitted changes.
- Latest/created/pushed commit: consult companion Exact Resume State after submission; this report is included with the scoped F6 batch.
- iPhone87/run40902351675/source312a592020963c565a066ea297acab8e323886ec FAILED. Actual startup probe compiled, but simctl install timed out after180s on iOS27.1/iPhone Duo. Even simulator log collection then timed out45s. No game-code error identified; startup gate correctly blocked the main game job, so no IPA. Exact underlying simulator stall is unproven; retry on a fresh CI worker without weakening the gate.
- Logs: workspace work/ios-build87-scene.log and work/build87-scene-artifact.zip, artifact12910064968. Preserved failure.json identifies install stage. Windows2/run40899127561 remains the successfully compiled/user-tested PC baseline. Installed phone84 retained; no matched new iPhone IPA ready.

### Next steps
- P1/user: restart PC P1; check GPI Active and replacement counters, HD models and RTSS after15 seconds. C is charge; installed PC2 still has no F6 recall until new build.
- Build task: submit one paired Windows/iPhone batch; capture exact commit and run IDs, verify receipts/artifacts/source identity before staging. Retain current working PC2 and phone84 until replacements are validated. Do not idle-poll.
- Hardware: after matched pair prepared, test full PC+phone practice first, host roles both directions, move both captains/squads, check guest view/camera, pause/ready/background/exit. Phone not needed during CI.
- P2: stay paused while P1 cross-platform mode is developed.

### ChatGPT continuation notes
- User-confirmed PC success is short gameplay validation, not a completed campaign test. New F6 source has only local verification. Optional graphics installed; rendering counters and RTSS need user evidence.
- Keep player graphics/controls/cosmetics independent; shared simulation rules still need agreement. Never use the old headless PC helper as the full PC game.
- Mid-day autosave/recovery and seamless PC/iPhone shared progression remain REQUIRED final objectives, not implemented. Practice arena is not campaign co-op; do not promise process-death recovery or live host migration.
- Exact next actions: verify paired build results/receipts, stage matching executables/IPA without overwriting saves/settings/Load content, then user-controlled mixed-device test. Keep private assets outside public Git.

**END PROGRESS REPORT**


### Paired build submission (2026-10-29)
Committed and pushed source 2b9844da663314a2eb2f9b41bc6f2dca1af58b6b, source identity92e732019066b603cae94bdcb1d75a18394f6a74c5f586dd65375baf4a1855e3. Working tree clean after source push. Final local checks:20 non-touch recall/input plus110 command scenarios,12 scene runner,10 room runner,4 packaging and2 identity tests PASS.
- Experimental Windows P1 co-op game Build4: run40932444780, in_progress at dispatch check, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40932444780 . No outcome/artifact verified yet.
- Experimental native iOS game build (unsigned) Build88: run40932444692, in_progress at dispatch check, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40932444692 . No outcome/artifact verified yet.
RTSS Windows approval completed; P1-only profile installed, API readback OSD1/detection1, global profile unchanged. Actual overlay still needs user confirmation. All PC content files installed/enabled with verified hashes; next user test is reopening PC P1 to check texture replacement counters/HD models and visible RTSS. Current working Windows2 executable remains installed; F6 is only in pending source. Do not repeatedly poll builds. When user reports completion, read both results/receipts, verify matching source identity, back up current working executable/settings/saves, and stage in-place replacements preserving Load packs and configuration. Installed iPhone84 remains unchanged and does not match current full PC game.


# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-29 15:34 EDT

**Overall project status:** Matching full PC4/iPhone88 builds PASSED and packages verified. PC4 installed with a verified PC2 rollback; iPhone88 IPA staged but NOT installed. User's current phone test regained steady120FPS by disabling HD Pikmin; user then explicitly requested character-pack removal while retaining textures. That removal and verified backup are complete. Phone may be unplugged now; user was told this.

### Pikmin 1
- Current objective: mixed full PC+iPhone practice, preserve working solo baseline, remove unwanted phone HD characters and explain unlocked new saves.
- Investigated: exact CI artifacts/native receipts, paired identity in actual iPhone executable and Windows generated header, current phone settings, live phone test journal and HD model draw implementation. Phone current saved FPS mode2 requests120; AO0; Low Power Off reported by user. Initial user Heat Nominal later Fair. USB direct screenshot service unavailable (InvalidService); P1-only live syslog stream terminated without samples. No invented live CPU/GPU measurements.
- Confirmed performance: roughly52–54FPS initially with53 followers and active HD models/4K textures, roughly69 after user lowered only3DResolution to0.67x, then USER-CONFIRMED steady120 after disabling only Pikmin HD models. Texture pack remained active. This implicates HD Pikmin model rendering in this scene; exact profiling or a general FPS guarantee was not established. HD renderer pc_hd_models.cpp::drawPart skins vertices on CPU, explaining why resolution changes alone need not remove all cost. No engine optimization was implemented this turn.
- Unlock explanation: current phone journal logs preset_new_file_slot_parts and its SOLO TEST README documents the deliberately supplied Onions/Pikmin/unlocked areas. Ordinary unlockZones/allOnions settings are0. The earlier solo-update variant invokes pc_solo_test_prepare_new_campaign and pc_solo_test_unlock_areas, with separate save-solo-test cards. This is the solo systems-test preset, not co-op practice accidentally unlocking normal saves. Build88 retains this SAME fixture. Standard variant must be built later for normal new-save progression; do not present88 as a normal campaign release or alter existing saves to relock them.
- Local files changed: verified PC4 package replaced only executable/package files in existing Windows folder. Backed up original14 receipt entries/receipt, config and saves in C:\Users\chazz\Documents\Open Nectar\4 - Windows Version\Pikmin 1 - Full PC Co-op - Experimental\Backups\Before PC Build 4 - 20261029-152220.3195 protected settings/save/optional-content files verified unchanged. F6 now present in PC4; enable F1 > Cheats > Recall All Pikmin for solo use. Phone88 IPA at C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\P1 Build 88 - Full PC Co-op Pair\Pikmin 1 - Build 88.ipa, with START HERE and Package Verification. It is the existing P1 app identity; do not uninstall/reimport assets.
- Phone changes AUTHORIZED by user: removed15 optional model NHMs,3 optional portraits,2 P1-local auxiliary P2 model-conversion source archives, and the inactive character ZIP from Documents. Actual P2 application/its assets were NOT touched. Removed auxiliary sources prevent the P1 importer from regenerating the models. Set only hdModelsDisabled=63 in P1 config; preserved user's selected120FPS/0.67x and all other settings, including activeGPI texture pack. The untouched old recovery archive on phone remains a backup, not active installed models. PC model packs retained, as scoped in commentary.
- Backup: C:\Users\chazz\Documents\Open Nectar\5 - Backups and Older Files\P1 Before Character Removal and Build 88 - 20261029-153051. Actual installed optional files were backed up and reread/hash-verified, including valid NHM models regenerated by the game's own importer with hashes differing from the original ZIP. Both save and save-solo-test, touch layout, settings and achievements copied/verified. Model/portrait/source removal completed. A post-removal verification script had an async-generator programming error; corrected it and independently rechecked actual phone state before reporting completion. Removal record retains this error history plus complete/verification-corrected flags; no new phone game build installed.
- Post-removal validation: model folder and auxiliary P1/pikmin2 folder absent, character ZIP absent;3046 texture PNG inventory unchanged and5 sampled texture hashes unchanged, GPI/enabled1 preserved, six save/layout/achievement files hash-unchanged and complete original config differs only in model mask. Full texture content was NOT rehashed over USB. Phone runtime after actual removal remains untested; user's120FPS observation preceded uninstall and followed the live HD Pikmin toggle.
- Confirmed working: earlier PC2 short gameplay; both native builds; user's HD-off phone performance test. Remaining: PC4 runtime/F6, phone88 installation, actual full PC/phone mixed practice in both host roles, normal campaign build option and broad finished co-op scope.

### Pikmin 2
- Objective/status: retain user's last confirmed working application. No P2 build/install/source/asset changes. The two deleted .szs files were optional model-import copies INSIDE P1's container; P2 itself untouched. No new runtime result.

### GitHub
- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port ; branch ios-experimental.
- Starting commit this turn415351fee50ea97ba603ad2ab80dd5241192afe1, equal to fetched origin. Gameplay source2b9844da663314a2eb2f9b41bc6f2dca1af58b6b. This turn only journals change; no new engine code/build required for local content removal. Final HEAD in Exact Resume State.json after documentation-only push.
- Windows4/run40932444780 SUCCESS; artifact12923288453, ZIP SHA2561f0ecb7ecd0c35aef72c6b2e3e7893115a40f44e476e1d7ba1acbf8a2db79f0c; executable5dc7eb00c8a5375c69dfc20caf1789a9e914db1d0fd56fa2b6b1002b4db211ac. All14 receipt files, x64 PE and imported runtime DLL closure checked. PC4 installed, not launched by Codex.
- iPhone88/run40932444692 SUCCESS; artifact12924694374, ZIP SHA25634e09c6486db66317b7bac6d5acca61a3b0aed5bd348db99f678198a1ed8f29f; IPA5350110bytes SHA2560a845813dfde4beb6055185c8c1f58b8d228bb8df48e678b6ca2d6687878a49e; UUID7ec0a828-d624-34bf-b485-4e8d5166cd2b. Unsigned ARM64 iPhoneOS, same org.opennectar.experimental.pikmin1 ID, approved icons/licenses verified.21 practice+13 room checks all passed, scene startup/background/resume one process/window passed. Real encrypted UIKit socket runtime passed after the existing bounded simulator health-setup retry; first health-app launch timed out90s, recovery passed, no cleanup errors. No gate weakening.
- Shared source identity92e732019066b603cae94bdcb1d75a18394f6a74c5f586dd65375baf4a1855e3 matched between both artifacts AND found inside actual phone executable. Simulator evidence does not prove actual paired gameplay.
- Logs/receipts: work/windows-coop-build4-verification.json, work/build88-package-verification.json, work/build88-run.json, work/build88-scene-artifact.zip, work/build88-p1-artifact.zip, work/pc4-iphone88-stage-result.json, work/p1-current-graphics-latest.json, work/p1-character-removal-latest.json. Private backups excluded from Git. Build87 earlier simulator install failure remains historical;88 is successful.

### Next steps
- User: phone file work done; unplug/reopen freely. Current0.67x is the user's diagnostic resolution, not an imposed cap. Can compare1.00x later with models absent. Texture pack remains enabled.
- Installation: existing latest phone settings/both card folders now backed up. In Sideloadly update same P1 with staged Build88 using SAME signing identity; no uninstall, no copying game files. Its solo new-save unlock fixture remains intentional; normal campaign progression requires standard variant, not a settings toggle. Do not silently choose/delete normal/test cards.
- Runtime test: same LAN, PC4 host and iPhone88 guest; Connected on both, Start Co-op Practice independently, wait loaded then Ready/Resume on both, check both visible worlds/captains, movement/cameras/squads; then pause/background/exit, reverse host roles. Raye's phone not required. Stop for exact failures and collect logs. Do not automate game input.
- GitHub/build task: no fresh builds needed for this local cleanup. Await actual install/runtime feedback. P2 remains paused.

### ChatGPT continuation notes
- All prior vision remains queued: own views/cameras/squads, shared stock/independent allowances, independent graphics/controls/cosmetics, host-authoritative campaign, cutscenes/travel, internet, true durable mid-day recovery/rejoin and PC/iPhone progression. Practice is not full campaign multiplayer. No claim completed solo campaign.
- Phone character packs are now intentionally REMOVED per user. Do not reinstall them automatically or synchronize PC visuals onto the phone. GPI textures retained; phone HD model mask63. PC models are retained unless user says otherwise.
- Do not mistake the unlocked solo-test campaign for a corrupted normal save. Existing normal save cards are preserved and separately backed up. Standard variant may be preferable when user wants ordinary new-game progression, but88 remains an unlocked test update.
- Exact resumption: inspect status/origin and Exact Resume State; read latest report; verify whether user installed88, then guide the short actual PC/phone test. Keep outstanding normal-campaign choice and all larger co-op objectives visible. No more idle polling of completed builds.

**END PROGRESS REPORT**


# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-29 19:56 EDT

**Overall project status:** Full PC4 and iPhone88 practice ran on the user's devices. PC-host play was smooth locally but iPhone guest actor movement stuttered; phone-host/PC-guest Ready was stuck. The PC later exited itself with an engine panic. A coordinated fix batch is implemented and locally verified; Windows5 and iPhone89 native builds have been submitted and were last observed IN_PROGRESS. No new executable/IPA has been installed, and no running-game input or process termination was performed by Codex.

### Pikmin 1

- Current objective: fix mixed PC/iPhone guest presentation, Windows readiness and the observed host crash before extending campaign co-op.
- Investigated: four per-session PC reports, current phone reports/settings copied read-only, PC launcher log, both supplied PC recordings via sampled frames, runtime/world/focus/carry source and original upstream 1.1.1. The phone MOV files opened for initial metadata but later were absent at their supplied paths; no claim of visually reviewing those phone recordings. The screenshot and user's observations remain evidence.
- Root cause/evidence: guest receives complete actor snapshots at about 19–20 Hz while its camera renders near120 Hz. Guest transforms previously jumped directly to each snapshot with no between-snapshot presentation. LAN RTT was about3 ms in captured reports, so this is not evidence of generally slow Wi-Fi. PC guest reports remained `away=1`; queued SDL focus events and native panel focus could clear readiness immediately. PC last-run log ended in the unique `zannnen` carry-goal panic, whose source requires an absent Onion. Exact cargo leading to the panic was not identified.
- Implemented: bounded eight-frame,75 ms arrival-time presentation buffer for guest captains and Pikmin, sampling at each device's render rate. No extrapolation. Latest population/ownership/health/action remain authoritative, births/deaths retain exact IDs, large teleports snap, angles wrap by shortest path, animation loops/clip changes do not interpolate backward. Pause/revision/teardown reset history.
- Implemented: actual engine redraw adapter validates the current admitted sequence/population/pool before any writes; redraw cannot consume host sequence, change stored ownership/health/job metadata or start guest simulation. It reuses latest accepted metadata and only blends compatible poses/transforms.
- Implemented: Windows game/owned room/practice windows share one foreground-family check after queued messages drain. Ready is deferred until focus reaches the game. External apps/minimizing still pause, and coming back still requires readiness. Removed duplicate stale SDL co-op focus notifications; iOS interruption logic unchanged.
- Implemented: missing Onion/ship or nearest route safely fails a carry attempt instead of panic/null dereference. Vanished cargo and empty destination choice are guarded. Original valid color/owner destination selection remains unchanged; console-only fatal assertions remain conditional outside the PC port. Cargo references are retained while route-point callers finish the same tick.
- Files changed: pc_port/netplay/pc_coop_visual_smoothing.h (new), pc_coop_practice_runtime.cpp, pc_coop_world.h/.cpp, pc_desktop_coop.cpp, pc_window.cpp; src/plugPikiKando/aiTransport.cpp; relevant tests; two experimental workflows; project journals and upstream audit.
- Local verification PASS:231 standalone presentation assertions,14 actual extracted Windows Ready/focus checks,8 actual extracted carry-goal/route checks; strict MSVC /W4 /WX. Actual world adapter plus existing pool/300-Pikmin packet/lifetime/compile-out fixture passes with new redraw cases. Actual Windows frontend compiles with strict warnings. Existing actual independent-view/camera/HUD/audio and gameplay-authority guards pass. Clang diagnostic/core analysis with warnings treated as errors passes for new fixtures/smoothing and actual world adapter.13 full actual engine/header translation-unit checks pass with existing decompilation warnings. Four Windows packaging tests pass after using the workspace test-temp directory. Python AST parses. New checks are required before packaging in both workflows.
- Additional bounded experiment: actual practice input helper plus InputReceiver, continuous movement at host30/60/120/180/240 Hz with2 ms one-way delay and20 Hz snapshots had zero post-warmup neutral movement gaps. This does not exclude jitter/packet-loss issues; no speculative input-policy rewrite was made.
- Verification repairs: initial carry fixture exposed a legacy float-to-int warning, fixed with an explicit semantically equivalent cast. Explicit UTF-8 fixes Windows source decoding. A core analyzer found an unguarded empty destination-choice path; guarded and rechecked. None of the checks or existing native runtime/package gates were weakened. Local workflow YAML parser unavailable; no YAML-parser pass claimed. Git diff whitespace check passed.
- Confirmed working: user's PC4 local gameplay smooth; phone88 renders world/camera, original solo/touch/native pixels previously confirmed. Phone HD Pikmin Off gave user-reported steady120; HD character removal and preserved GPI textures previously verified. Current mixed practice is still experimental and not shared campaign co-op.
- Remaining: actual new PC/iPhone native compilation/artifacts and runtime test in both host roles; device pause/background behavior after update; internet/full shared world/campaign/reconnect/durable mid-day recovery/cross-progression. New visual fix is NOT yet hardware-confirmed.
- Original Louie: user approved restoring only the340588-byte original low-detail Louie. Prepared restore script validates backup SHA c61f484c955e3944dded7535efe8bedd91214454a86620a343ec79842c16bf8d, keeps all HD characters absent, changes only model-mask63 to61 and backs up config. Latest attempt failed with NoDeviceConnectedError before writes. Restoration still pending; do not say completed. Reconnect/unlock with P1 CLOSED when convenient, preferably at the next build update.

### Pikmin 2

- Current objective: preserve the last user-confirmed working P2 while P1 co-op is validated.
- Investigated: upstream release notes/source candidates only; no new P2 runtime fault.
- Root cause/hypothesis: none new.
- Files changed: no P2 source, app or assets.
- Tests/results: no P2 build requested.
- Confirmed working: earlier user hardware report; full campaign remains unproven.
- Remaining: broader campaign test and eventual P2 online adaptation; selected upstream P2 fixes queued separately.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental. Starting local/remote987d254d5fb5129edaca097ec277471f5c47590e; last accepted gameplay source2b9844da663314a2eb2f9b41bc6f2dca1af58b6b. Fetch showed no divergence or third-party fork pushes.
- Latest gameplay commit: deaaee1ee0b884c5c939f456b6a5ccfff4d23d40, committed and pushed safely to ios-experimental. Local and remote matched after push. Documentation-only checkpoint follows; resolved final journal SHA is in Exact Resume State.json. No upstream merge or branch/history rewrite.
- Uncommitted changes: no source edits after the pushed batch. Only this final documentation/run-ID checkpoint is being saved; final clean status is recorded in Exact Resume State.json.
- Last successful runs: Windows4/run40932444780; iPhone88/run40932444692. Both source2b9844da, shared identity92e732019066b603cae94bdcb1d75a18394f6a74c5f586dd65375baf4a1855e3. User installed/tested matching pair; old `iphone88_installed=false` resume field is corrected now.
- Current builds: Windows5/run40976294203 and iPhone89/run40976294072, both sourcedeaaee1ee0b884c5c939f456b6a5ccfff4d23d40, last checked IN_PROGRESS. Computed source identity26204c2b52dcf03c59c52798930a69a9e11a4a6c9272600e9c7a8eb29e650f9e (2908 tracked files); verify against actual produced packages after success. No new artifacts or runtime claims yet. Windows4 artifact12923288453 and iPhone88 artifact12924694374 remain verified rollback.
- Submitted build: one coordinated push with [ios-build] [ios-p1-update] [pc-coop-build], preserving the current same-app unlocked solo-update test variant. Do not silently change normal/test save behavior. Both clients must update to the same new source identity. P2 excluded. Do not idle-poll; user will report completion.

### Next steps

- Next P1 task: await user build-completion report; retrieve full results/logs and verify/stage matching packages only after success. Then test PC host/phone guest movement, reverse roles Ready, pause/Alt-Tab/background, and longer stability. Raye's phone is unnecessary for this mixed test.
- Next P2 task: preserve current install; later broader campaign coverage and separate upstream review.
- GitHub/build task: one paired validation batch, no redundant builds for documentation; preserve all existing receipts and native UIKit scene/socket tests.
- User involvement: none while building. No need to keep a live session open. Original Louie needs USB/unlocked/P1 closed when convenient; no repeated launch/install or asset replacement needed now.

### ChatGPT continuation notes

- New upstream release1.1.1 today, current fetched upstream/main14a922a9. Read ios/UPSTREAM_AUDIT_2026_10_29.md. Strong next candidate is per-program shader cache, but do not import480p default. New control action IDs conflict with our Recall All index26; reconcile before adoption. No release feature has been silently merged.
- Important source functions: PcCoopVisualSmoothing::push/sample; pc_coop_practice_tick_begin/leave; pc_coop_world_present_guest/commitCaptains; Windows resume/updateFocus; ActTransport::doLift/decideGoal/crGetPoint.
- Logs: work/practice-pair-pc4-iphone88/pc-last-run.log and per-session reports; work/p1-current-graphics-20261029-155548/pikmin1 reports; work/pair-real-headers.log, pair-strict-clang.log, pair-clock-repro.cpp; upstream-releases-oct29.json. No room tokens or private game assets committed.
- Existing PC folder: C:/Users/chazz/Documents/Open Nectar/4 - Windows Version/Pikmin 1 - Full PC Co-op - Experimental. Launch PLAY PIKMIN 1.cmd; preserve Game/Load, Saves, config and assets junctions. Do not mistake launcher `The game stopped` terminal for proof of normal exit; inspect last-run.log.
- Existing phone backup: Documents/Open Nectar/5 - Backups and Older Files/P1 Before Character Removal and Build 88 - 20261029-153051. Keep GPI active, HD packs intentionally removed, restore only original Louie after permission already given.
- Unverified: new hardware behavior, actual native compilation/package for new source; original Louie not restored. New P1 remains unlocked solo-update test variant with separate save-solo-test; normal `save` preserved. This is not a completed campaign/co-op product.
- Preserve all queued vision: independent personal graphics/camera/controls, own screens/squads, shared Onion stock with independent allowances, host-owned campaign, cutscenes/travel, same/different Wi-Fi, PC/iPhone mixed play and migration, automatic exact mid-day recovery for calls/suspension/closing/crashes, reconnect and clear exit UI. None is canceled by this batch.
- Exact next actions after a reset: read this report and Exact Resume State; verify Git status/fetch; use recorded source/run IDs for full logs and receipts; stage only verified matching artifacts; restore original Louie when the user reconnects; guide both-role practice test and collect reports for any remaining faults.

**END PROGRESS REPORT**


# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-29 20:12 EDT

**Overall project status:** Windows5 PASSED and its full package is verified. iPhone89 FAILED before the full game compile because an extracted exit test lacked the newly added smoothing objects. Test correction is implemented and locally verified. iPhone90/run40978326061 has been submitted and was last observed IN_PROGRESS; keep installed PC4/phone88 until the matching replacement packages are verified. Original low-detail Louie is now restored/hash-verified on the user's phone; HD packs remain removed and GPI textures retained.

### Pikmin 1
- Current objective: get the existing coordinated guest-stutter/PC-Ready/missing-Onion fixes through iPhone validation, preserving the passing PC5 game.
- Investigated: COMPLETE iPhone89 run log ZIP and full P1 job log; failed steps and diagnostics-only artifact; Windows5 run/package; actual exit fixture and both workflow invocation sites.
- Root cause: tests/pikmin1_practice_exit_test.py extracts the real pc_coop_practice_leave body. That body now resets smoothing and presented, but its controlled test environment did not declare either object. Apple reported two undeclared identifiers in practice-exit-test.cpp line35. This is a stale fixture, not an observed game compiler error. I missed running this existing exit fixture in the previous local batch.
- Related failure grouping: the later socket-runtime gate correctly rejected `outcome=skipped`, since the first failure prevented building/running that probe. NOT an independent socket execution failure or simulator timeout. Simulated compile failures/timeouts printed by the runner's unit tests were EXPECTED negative cases; the actual21 practice checks and13 room checks PASSED. No successful runtime gate is being invented or bypassed.
- Files changed: tests/pikmin1_practice_exit_test.py; .github/workflows/ios-native-experimental.yml and windows-coop-experimental.yml; journals. NO game/renderer/controls/network/save source changes.
- Implemented: fixture now includes the actual PcCoopVisualSmoothing header and a real ActorFrame, initializes stale buffered state, and checks both objects clear on safe early exit/cancel. Late admitted-card exits retain the frozen scene for required restart; wrong-thread leave cannot alter it. Both Apple host/iPhoneOS test commands include the real header paths. Added the same exit test to future Windows content checks, so Windows can catch this class of stale fixture too.
- Tests/results:10 actual extracted exit/real-smoothing cleanup checks PASS with strict MSVC /W4 /WX; strict Clang diagnostics/core analysis PASS. Two isolated negative controls removing either smoothing.reset or presented reset both FAIL as intended. Python source generator executes; final source whitespace check PASS. Actual full Apple compile and owned UIKit socket execution for the replacement remain PENDING.
- Compatibility: computed identity remains26204c2b52dcf03c59c52798930a69a9e11a4a6c9272600e9c7a8eb29e650f9e across2908 tracked code/config files. This matches the verified PC5 header. Test/workflow/documentation-only changes do not change compiled game identity. Reuse PC5; do not rebuild it merely to get the same game code.
- Confirmed working: user's PC4 local play and phone88 solo/render controls as previously reported; Windows5 compilation/package checks and iPhone89's new231 smoothing/14 Ready/8 carry and existing scene-startup/capture checks passed. These are NOT new co-op hardware results.
- Remaining: replacement iPhone full compile/runtime/package, install verified PC5 plus new iPhone pair, repeat both-host-role movement/readiness/interruption tests. Broader campaign/rejoin/durable mid-day saves/cross-progression/internet remain open. New iPhone uses same unlocked solo-update test variant; normal save storage remains protected.

### Pikmin 2
- Current objective: preserve the working install.
- Investigated/root cause: no new P2 fault; no new P2 investigation in this fix.
- Files changed/tests: none; no P2 build/install requested.
- Confirmed working: prior user report; full campaign not attested.
- Remaining: broader campaign coverage and later online adaptation.

### GitHub
- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port ; branch ios-experimental.
- Starting local/remote:cd6e39ef5e2c65efd1d0a69e8a1cbbaf15dbcc31, fetched and no divergence. Last game code commit:deaaee1ee0b884c5c939f456b6a5ccfff4d23d40.
- Latest build source commit:dcfba41f178d0e8905c215b4d668da67e1f43939, committed and pushed with [ios-build] [ios-p1-update], WITHOUT [pc-coop-build]. iPhone90/run40978326061 IN_PROGRESS at last check. Windows6/run40978326030 SKIPPED by design; reuse successful Windows5, whose compiled game identity matches. No new game code.
- Uncommitted changes: no test or game edits after the pushed correction; this documentation-only run-ID checkpoint is being saved. Final journal SHA and clean local/remote state are in Exact Resume State.json.
- Build results: PC5/run40976294203 SUCCESS, artifact12943316091. iPhone89/run40976294072 FAILURE; P1 job123808448668 primary failure at enhancement check, later mandatory socket gate refuses skipped runtime. Scene-startup job123805033631 PASSED. No IPA or full compiled-app artifact from89.
- Artifacts: PC5 ZIP SHA25693b822b5cc7ae9c5b08cb16437d43240b00cfa42c166ce9e4db9e3904711969a; EXE SHA256d93bd8dcc7f80b46dc31e7767595940b9c352773f1da80fd401a48dcae831d9a.14 receipt file hashes, safe archive paths/no game assets, x64 PE, runtime-DLL closure and shared identity verified. Retained in outputs/P1-Full-PC-Coop-Build5; NOT installed over PC4 yet. iPhone89 artifact12943032855 is diagnostics ONLY, ZIP SHA2567a37b2e6c4d0dd85a93dadff54be60f910e44ef08c546a6275378fcd65a38dd4, checked21/13 PASS receipts/no IPA.

### Next steps
- Next P1 task: verify replacement iPhone result/full logs/runtime receipts/artifact against PC5 identity; stage/install the matching pair after success, then repeat both host roles and interruptions.
- Next P2 task: preserve current app and queue; no new test needed now.
- GitHub/build task: submitted iPhone90/run40978326061: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40978326061 . Windows6 was SKIPPED by design. Keep existing mandatory native socket/scene/practice/room gates. No idle polling.
- User involvement: no phone/USB task now; original Louie restoration already complete. Tell Codex when the replacement iPhone build finishes. Do not install PC5 alone with phone88 because their game identities differ.

### ChatGPT continuation notes
- Logs: work/build89-logs.zip, build89-p1-full.log, build89-run.json, build89-jobs.json, build89-artifact.zip; windows-coop-build5-verification.json and windows-coop-build5.zip. Generated fixed fixture work/practice-exit-test.cpp; local verification work/check_build89_exit_fix.cmd; two sensitive negative-control results work/exit-cleanup-negative-results.json.
- Important source: pc_coop_practice_leave cleanup now referenced by the updated fixture; no game code needs changing for this failure. New movement/Ready/carry game fixes remain deaaee1e as documented in the previous full report.
- Upstream1.1.1 review remains in ios/UPSTREAM_AUDIT_2026_10_29.md; no wholesale merge, performance/control candidates queued. Avoid480p default and action-index26 conflict.
- Preserved requirements: independent device graphics/camera/controls; own views/squads; shared stock/independent allowances; host campaign; cutscenes/travel; live rejoin, calls/background/crash handling, durable mid-day recovery, PC/iPhone migration and eventual P2. Current disposable practice is not finished campaign co-op.
- Exact resumption: read Exact Resume State for replacement run ID and final commit; user reports its result, fetch full logs and verify real runtime and IPA, compare identity to PC5, stage both without deleting assets/settings/saves. Use NEXT TEST - PC5 and iPhone90.txt after verification. Phone may be unplugged. No automated running-game input.

**END PROGRESS REPORT**


# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-29 20:42 EDT

**Overall project status:** iPhone90 SUCCESS independently verified and matched to PC5. PC5 installed after a verified PC4 rollback backup;3199 current settings/save/optional-content files hash unchanged. iPhone90 IPA staged in Documents, NOT installed by Codex. Ready for user's mixed PC/iPhone practice test. No new game source changes or further builds this turn.

### Pikmin 1
- Current objective: validate real paired behavior after guest smoothing, Windows Ready/focus and missing-Onion carry panic fixes.
- Investigated:90 full P1 job log, scene-startup artifact, device IPA/resources/CPU/platform,21 practice/13 room receipts and actual encrypted UIKit socket-runtime evidence; PC5 package and existing PC4 install.
- Root cause/history:89 failed because its extracted exit fixture omitted smoothing/presented declarations. That fixture and include paths were corrected in dcfba41f; no game-code change versus PC5/deaaee1e, so they have an identical compatibility identity.90 now passes that exit test and proceeds through the actual full game/runtime/package. No weakened or skipped required gate.
- Changes installed/staged: PC5's package files replaced the closed PC4 install; game assets, current settings, saves and optional textures/HD models protected and verified unchanged. No game process was launched/closed or controlled by Codex. Phone IPA copied to the accessible folder only; no phone app update or file changes this turn. P2 untouched.
- Native tests/results: full iPhone ARM64 game **BUILD SUCCEEDED**;231 smoothing,14 Windows focus,8 carry-goal and10 exit/real-smoothing checks passed on Apple runner, including iPhoneOS syntax checks. Existing21 practice and13 room checks PASS. Real encrypted UIKit socket probe PASS in an owned disposable simulator, observed entry into main/health PASS, no setup retry and no cleanup errors. Scene startup/resume uses one launch/process/window and PASS. Runtime-on-simulator is not a real-device gameplay test.
- Package verification: iPhone90 unsigned ARM64 iPhoneOS bundle org.opennectar.experimental.pikmin1/display Pikmin1, existing approved icons/notices, landscape metadata and required network/scene markers verified. No bundled proprietary game assets, profiles or signatures. IPA5354907bytes SHA25663b75ed059cf288da64fd99c7992a19c36f7dfe24f8411237a025e60735683d8; UUID9cd03b77-653b-3b37-bf14-0b5e223dc1e1. Source identity26204c2b52dcf03c59c52798930a69a9e11a4a6c9272600e9c7a8eb29e650f9e found in actual device executable and exactly matches PC5's header.
- Installed PC path: C:/Users/chazz/Documents/Open Nectar/4 - Windows Version/Pikmin 1 - Full PC Co-op - Experimental. Launch PLAY PIKMIN 1.cmd. Before replacement, all14 prior receipt files matched PC4. PC4 rollback: C:\Users\chazz\Documents\Open Nectar\4 - Windows Version\Pikmin 1 - Full PC Co-op - Experimental\Backups\Before PC Build 5 - 20261029-204019. All3199 CURRENT protected config/save/optional-content files hash-unchanged after update; importer-regenerated optional bytes are protected as currently installed rather than overwritten to old downloaded hashes. assets junctions/dataDir/Load/Saves retained. New PC5 runtime remains untested.
- Staged phone IPA: C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\P1 Build 90 - Full PC Co-op Pair\Pikmin 1 - Build 90.ipa. START HERE.txt and Package Verification.json beside it. Use Sideloadly with SAME signing account/app identity to update the existing P1; do not uninstall/reimport assets. Existing phone/settings/save backups retained. Phone90 installation and gameplay remain NOT VERIFIED.
- Current phone content: original low-detail Louie restored/hash-verified in previous action; all HD characters intentionally removed, model mask61, GPI texture pack retained. In-game Louie appearance untested. No USB task required now.
- Confirmed working: earlier user's PC4 smooth local play and phone88 solo/touch/render baseline; PC5/iPhone90 native/package/simulator results as above. No new hardware co-op result yet.
- Remaining: phone90 installation, actual phone guest movement smoothness, reverse phone-host/PC-guest Ready, pause/Alt-Tab/iOS background recovery, longer practice stability, original Louie appearance. Continue broader world/campaign/rejoin/exact mid-day persistence/internet/PC-phone progression once core practice feedback is good. This remains a disposable practice test, not finished campaign co-op.

### Pikmin 2
- Current objective: preserve user's working application.
- Investigated/root cause: no new P2 fault.
- Files changed/tests: no P2 changes or new build/install.
- Confirmed working: prior user report; full campaign unproven.
- Remaining: broader testing and later online adaptation, with original vision/queue retained.

### GitHub
- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port ; branch ios-experimental.
- Starting local/remote journal commit:c3ff55b2611708c6edfc66cde12a6f33f7c78c6d. Status clean, fetched origin with no divergence before documentation.
- Latest gameplay source:deaaee1ee0b884c5c939f456b6a5ccfff4d23d40 in PC5. iPhone90 build source:dcfba41f178d0e8905c215b4d668da67e1f43939, test/workflow correction only; identical compiled game identity. Current turn creates only a [skip ci] verification/handoff journal commit; final resolved local/remote SHA in Exact Resume State.json.
- Uncommitted changes: only this documentation checkpoint; no game/CI/test edits after90.
- Windows5/run40976294203 SUCCESS; artifact12943316091, ZIP SHA25693b822b5cc7ae9c5b08cb16437d43240b00cfa42c166ce9e4db9e3904711969a; EXE d93bd8dcc7f80b46dc31e7767595940b9c352773f1da80fd401a48dcae831d9a;14 files/x64/dependency closure verified and now installed, no runtime claim.
- iPhone90/run40978326061 SUCCESS; artifact12945005446, ZIP SHA256b460cf52e0f8b34842ce4766c583fce7069f42aae883f07d2abb5f299976f039; scene artifact12943343205 SHA2568fdec5b552551ff7be69da243b463c1ac3734969d7ce3935c1abbe9d94ca3798. IPA staged, phone not updated by Codex.
- Windows6/run40978326030 intentionally SKIPPED, not failed; do not rebuild PC5 unnecessarily. iPhone89 diagnostics-only failure is superseded by successful90. No additional build needed for staging/documentation.

### Next steps
- User installation: close phone P1; drag the staged Build90 IPA into Sideloadly, select the correct phone and same signing identity, Start update. PC5 is already installed. No game-data import or P2 update. Raye's phone is unnecessary for this PC+phone test.
- First test: same LAN, PC hosts/phone joins, start practice independently, Ready on both after loading. Slowly walk both captains and squads; watch the PHONE view for actor stutter (camera was already smooth).
- Second test: pause/Alt-Tab on PC, return/Ready on both; briefly background/return on phone/Ready; neither side should remain stuck solely from focus changes. Do not expect full crash recovery/live campaign reconnection yet.
- Third test: PHONE hosts/PC joins; PC Ready should dismiss its native panel and allow control. Check phone Louie appearance. Report host role, device, exact message/action for any failure. A short clip helps if movement still stutters.
- GitHub/build task: await actual installation/runtime feedback, no polling or new builds now. Keep installed/staged rollback packages and all settings/data. P2 unchanged.

### ChatGPT continuation notes
- Current patch functions: PcCoopVisualSmoothing::push/sample; pc_coop_world_present_guest; runtime tick/leave; Windows resume/updateFocus; ActTransport::doLift/decideGoal/crGetPoint. The90 correction changes only the extracted exit fixture and CI include paths, not gameplay.
- Relevant logs/receipts: work/build90-run.json, build90-jobs.json, build90-p1-full.log, build90-p1-artifact.zip, build90-scene-artifact.zip, build90-package-verification.json; windows-coop-build5-verification.json; pc5-iphone90-stage-result.json. Native artifacts retained privately under outputs/Build90-Pikmin1 and outputs/P1-Full-PC-Coop-Build5.
- Unverified fixes: actual new-device appearance/smoothness/readiness/crash stability; phone90 install. Do not label these fixed on hardware before feedback. Do not confuse the solo-update unlocked new-save test preset (save-solo-test) with a normal new campaign; normal save directory remains separate and protected.
- Upstream1.1.1 audit remains ios/UPSTREAM_AUDIT_2026_10_29.md: shader-cache and controller candidates queued, no wholesale merge or480p default change, preserve custom input action26/F6. All broader co-op requirements remain in COOP_OBJECTIVE_QUEUE.md/COOP_MIDDAY_RECOVERY_REQUIREMENTS.md, including independent views/options/squads, shared Onion stock/independent allowances, cutscenes/travel, host campaign, calls/background/disconnect/crash handling, durable mid-day saves and mixed-PC/iPhone migration, P2 later.
- Exact resumption: read current Exact Resume State and this report; confirm user installed90 (PC5 already installed), obtain both-role test results; collect fresh reports if a fault remains. Never automate input into a running game. Do not replace working apps/assets/saves unnecessarily.

**END PROGRESS REPORT**
