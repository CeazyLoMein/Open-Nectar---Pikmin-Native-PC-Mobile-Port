# OPEN NECTAR iOS — CODEX PROGRESS REPORT


**Date/time:** 2026-10-24 20:13 EDT

**Overall project status:** User accepted P1 Build53 as the current working solo baseline and explicitly authorized beginning online co-op now. Preventive P1 upstream batch implemented and locally checked. First host Onion accounting component implemented/tested, but NOT connected to game actors or live networking. Raye install copies prepared; no installation/phone data changes performed. Local source/tests ready; coordinated P1-only push pending.

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
- Latest commit: 407b7fa4f5479aeeb983de5c84a234d03641291e at report creation. Exact post-report local/remote hashes are in friendly Exact Resume State.json after push.
- Commits created:407b7fa4f5479aeeb983de5c84a234d03641291e P1 preventive batch; co-op/checkpoint commit pending.
- Changes pushed: Local source/tests ready; coordinated P1-only push pending.
- Uncommitted changes: Scoped co-op library, experimental workflow and documentation; P1 fixes already locally committed.
- GitHub Actions run IDs: Native P1-only build prepared; no new run result recorded yet. Previous53=40133259493 P1 SUCCESS,52=40131000336 P2 SUCCESS. No P2 build requested now.
- Build results: Current local tests PASS; current Apple compile/IPA/runtime not yet established.
- Artifacts produced: No new IPA from this source yet. Working P153 SHA256c483540e76cef95c002578724690fe8ebe649901b9a09906350ee0b93c5cff85; P252 SHA256fbf6b2512d91ccafc6c600ee8bddcdbbcef04a1c01ee0ea68da4c68fda40c793. Rehashed copies in Documents/Open Nectar/1 - Install on iPhone/For Raye - Start Here, with manifest and instructions. Original IPAs retained.

### Next steps

- Next Pikmin 1 task: Review one P1-only native run and verify artifact/package before an optional short carrying/Onion-skip/menu/resume hardware check. Preserve53 rollback and settings. Continue co-op actor/world vertical slice on disposable data.
- Next Pikmin 2 task: Raye solo install/asset import and basic audio/pause/resume test; no speculative P2 rebuild.
- GitHub/build task: Commit co-op foundation/checks, push both related commits together with [ios-build] [ios-p1-only], record exact run ID.
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

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

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
