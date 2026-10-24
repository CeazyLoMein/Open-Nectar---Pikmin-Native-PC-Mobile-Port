# OPEN NECTAR iOS — CODEX PROGRESS REPORT

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
