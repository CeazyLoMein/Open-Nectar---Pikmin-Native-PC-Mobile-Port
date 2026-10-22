# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-22 17:03 EDT

**Overall project status:** Build40 phone navigation FAILED. Optional automatic rescue and a confirmed recovery guard correction are implemented and locally verified; new Apple compilation/IPA/phone result pending. P2 working baseline preserved. Build 41, run 39854014424, source 769880462e9b0b8d2d139e0404fad015a741709f; last observed in_progress (no conclusion). No idle polling.

### Pikmin 1

- Current objective: Recover genuinely stranded followers automatically without recalling working Pikmin; preserve normal touch/gameplay behavior.
- What was investigated:42.81-second16:38 phone recording, live read-only settings/layout, real formation/swarm flag, trail/route/collision/reset functions, recall eligibility; Nintendo P4/Obsidian Grounded/Recast primary references.
- Root cause or leading hypothesis: Confirmed source defect: stock makeCStick clears mIsCStickNeutral for a separated formation even with no deliberate swarm input; our new recovery was gated by that flag. Corrected three recovery/trail/edge guards to actual mCStick input. This does not explain every stranded Pikmin or prove the phone issue fixed. Route graph/crowd limits remain; conservative automatic fallback approved by user.
- Files changed: Navi.h/Piki.h/PikiAI.h; navi.cpp/Piki.cpp(real filename piki.cpp)/aiCrowd.cpp under games/pikmin1/src/plugPikiKando; pc_follow_trail.h,pc_follow_surface.h,pc_follow_report.h; settings/pc_settings.h/.cpp; three follower/surface/command tests; design/status/handoff/checklist documents.
- Tests and results:128 actual-method route/recovery/rescue scenarios,24 layered-floor/wall,103 command/recall/aim/settings scenarios,283 P1 speed and283 P2 stock-speed control,58/58/7 campaign variants and39 bundle/config checks PASS. MSVC warnings-as-errors and independent Clang diagnostics PASS. Synthetic fixtures have engine seams; full game/Apple/phone validation pending.
- Confirmed working: Existing phone settings read100% captain/100% Pikmin, BetterPathfinding1/RecallAll1; no device writes. Prior user-passed readable menu, aim/soft assist/charge-whistle/save reload and explicit global button retained. Build40 native/link PASS and recovered IPA verified, but pathing failed on phone.
- Remaining issues: New rescue has no hardware evidence yet. Idle Pikmin by ship ignoring Recall All is UNDIAGNOSED; added limited recall state diagnostics, no speculative forced state. Rare clam scene/full campaign unverified. No autosave or online feature implemented.

### Pikmin 2

- Current objective: Preserve installed working user-reported Build32; P2 development paused while P1 stabilizes.
- What was investigated: Shared settings rescue getter explicitly disabled for P2; existing shared packaging safeguards retained.
- Root cause or leading hypothesis: No new P2 failure investigated in this change.
- Files changed: No P2 gameplay/audio source changes; shared P1-host settings declares the P1-only option, hidden/inactive for P2.
- Tests and results:283 P2 stock-speed control scenarios and shared bundle safeguards PASS. No new P2 native build or phone test.
- Confirmed working: User reported P2 working after prior audio fixes; installed baseline untouched.
- Remaining issues: More extensive solo validation later; then agreed campaign/co-op test work.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: b22b70ac345680263a1c37f7f5b1f707454c377f, clean before this work; fetched again and no divergence.
- Latest local commit: 769880462e9b0b8d2d139e0404fad015a741709f
- Latest fetched remote commit: 769880462e9b0b8d2d139e0404fad015a741709f
- Build source: 769880462e9b0b8d2d139e0404fad015a741709f
- Commits created/changes pushed: Scoped rescue source commit pushed; build record follows as documentation only [skip ci].
- Uncommitted changes: Only this documentation checkpoint is being written; no private evidence staged.
- GitHub Actions run IDs: Build 41, run 39854014424, source 769880462e9b0b8d2d139e0404fad015a741709f; last observed in_progress (no conclusion). No idle polling. Previous40=39784525620;39=39666676388;38=39664622876;37=39617967156; P2 working32=39518825366.
- Build results:40 native/link PASS, CI packaging FAIL(PNGs converted to TIFF), local recovery/package PASS, phone pathing FAIL.37 native/IPA PASS but phone pathing FAIL. New rescue source has no Apple result yet.
- Artifacts produced: No new rescue IPA. Old verified original-ID Build40 IPA remains folder1 (SHA25602d057e55a2e77a0779462f37e420c2a5e665fa01c6523ee6c4129f1e65f7cdd). Known-good35/37 restore material and40 original compiled archive preserved in folder5. Future workflow includes final PNG restoration from6cd2331d.

### Next steps

- Next Pikmin 1 task: Complete native build/package validation, stage verified original-ID update and test rescue using the supplied focused checklist. Enable Cheats > Rescue Stuck Followers, default OFF. Normal60FPS retained.
- Next Pikmin 2 task: Preserve working app; broader test later. No P2 update now.
- GitHub/build task: Build 41, run 39854014424, source 769880462e9b0b8d2d139e0404fad015a741709f; last observed in_progress (no conclusion). No idle polling. Do not keep polling an unchanged build. Retrieve actual full logs if a failure is reported.
- Anything requiring my involvement: Nothing during build. Phone collection finished; game may be closed/phone disconnected. After IPA ready, focused crossing/worker/counter test; no finale required.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User explicitly approved AUTO rescue, approximately8s stalled plus failed walking return, only existing followers. This does not call workers or healthy squad and is independent of Recall All. Ground/collision/enemy/occupancy checks can delay it; never claim perfect stuck classification.
- Important source-file locations: games/pikmin1/src/plugPikiKando/aiCrowd.cpp ActCrowd::pcRecoverFollower/pcResetFollowerRecovery; navi.cpp pcUpdateFollowTrail/pcTakeFollowerRescueBudget/callPikis; piki.cpp pcRescueFollowerNearCaptain; pc_port/pc_follow_trail.h PcStuckFollowerMonitor; pc_follow_surface.h pcFollowRescueSpot; settings row44/key stuckFollowerRescue. See ios/PIKMIN1_FOLLOWER_RECOVERY_DESIGN.md.
- Relevant logs: Latest phone collection C:\Users\chazz\Documents\Codex\2026-10-19\got-it-you-want-codex-to\work\p1-phone-feedback-2026-10-22 164225; only two settings/layout files read while game open, no current navigation report found and no new save backup claimed. Private video/contact sheet and hashed copies in Documents/Open Nectar/2 - Progress and ChatGPT Handoff/P1 - Build40 Crossing Failure -2026-10-22 (actual folder spelling includes spaces). Workspace outputs/P1-Build40-Phone-Failure and work/p1-phone-feedback-latest.json; previous build40-full-job.log/build40-verification.json.
- Unverified fixes: New actual-input recovery guard/rescue/diagnostics have local evidence only. No new IPA installed. Idle ship Pikmin cause unresolved. Full map physics/performance/campaign need device evidence.
- Risks and warnings: No uninstall/reset/save/phone writes, private data upload or security/signing change. Optional rescue is a cheat; disabled in competitive/multiplayer contexts. It does not revive, pluck or recruit idle workers. No claim every hazard is detected. Preserve settings/app IDs/assets and normal day-end saving.
- Exact next actions: Check new build after user reports completion; inspect logs/IPA directly; stage verified IPA into folder1 and notify user; use checklist. If failed recovery, collect p1-navigation-report.txt before repeated relaunches and correlate reason/coordinates. Diagnose ignored idle Pikmin from that evidence. Follow-up proposals are tighter crossing queue, shared validated crossing segments and waiting/rescue HUD; NOT implemented now. P4 algorithms are not publicly verified; no Oatchi/navmesh rewrite.

**END PROGRESS REPORT**
