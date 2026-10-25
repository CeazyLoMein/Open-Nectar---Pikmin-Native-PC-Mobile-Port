# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-25T14:52:33.277408+00:00 (October25 America/New_York session).

**Overall project status:** User thought59 retry passed. Actual attempt2: simulator SUCCESS, overall P1 job FAILED in our ARC regression command argument order. Corrected, locally checked both invocation paths; next P1-only Apple run pending. User's PC/iPhone cross-progression and disconnect/host-crash requirements researched and saved; iPhone development remains current priority, PC app untouched. No new phone installation.

### Pikmin1

- Current objective: Complete current native Host/Join connection-screen validation and real two-phone room proof; plan durable recovery and cross-device campaigns accurately.
- What was investigated: Live59 attempt2 metadata/jobs/full log; previous save audit and actual card_stubs.cpp/card paths plus CoopSession header; official Stardew developer mobile guide, Grounded Shared Worlds notes and Factorio joining/catch-up developer article.
- Root cause or leading hypothesis: Confirmed standalone clang++ invocation put -x objective-c++ after its input, unlike clang-tidy's -- argument convention. Fixed command ordering separately for each tool. The UI property rename itself was not rejected; actual full UIKit check was never reached. Recovery design separates retained live host/network loss from host process loss. Existing normal card is not a full live-world checkpoint, and guest visual replicas are not host-recovery saves.
- Files changed: tests/ios_coop_arc_names_test.py; new ios/COOP_CROSS_PROGRESSION_AND_RECOVERY.md; saved design/save/research/implementation/status/progress/handoff notes. No game or save-system source change in this batch.
- Tests and results: Corrected test on installed Clang frontend PASS for actual8 synthesized screen getters and negative control reproducing original ownership error. Standalone driver path exercised through an argument-order-checking adapter feeding the REAL Clang frontend for both fixtures; this is NOT an actual Apple standalone compiler/SDK result. Git diff check PASS. Unchanged gameplay tests not repeated locally. Native screen/private-code/game/package checks pending next CI.
- Confirmed working:59 retry's shared simulator startup/background/resume PASS.57 remains last fully successful native P1 + real encrypted socket/session test, including2captains/60Pikmin data transfer. Existing user-tested P154 installs remain unchanged.
- Remaining issues: Connection-screen/full UIKit/code join/native app/notices packaging checks still pending. No playable full-world co-op, exact host recovery, mid-day save, cloud sync, PC cross-play/progression or auto host migration implemented. PC/iPhone save round trips not yet validated. Optional120FPS/AO OFF baseline preserved.

### Pikmin2

- Current objective: Preserve working app until its later stronger solo audit and adapter.
- What was investigated: No new P2 source or phone investigation.
- Root cause or leading hypothesis: None.
- Files changed: None.
- Tests and results: Not rebuilt or installed.
- Confirmed working: Prior user-confirmed app on both phones.
- Remaining issues: Full story not verified; P2 needs separate world/save codec despite reusable networking/container.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental.
- Starting commit:dda93a4c50183b77687c40154c944366009016ea; clean and matched origin after fetch.
- Latest commit: Correction/design batch pending commit; exact source/run checkpoint follows.
- Commits created: Pending one source-tool+design+docs commit.
- Changes pushed: None yet at report creation.
- Uncommitted changes: Listed compiler tool and design/journal files only.
- GitHub Actions run IDs:59 run40162073334, attempt2, source d698f880af334690551a9bfb692521aec1551739; last complete successful57/run40158088407.
- Build results:59 attempt1 boot timeout; retry attempt2 scene121105139764 SUCCESS, P1121107438150 FAILED compiler-test command. Actual room/native/package checks SKIPPED. No new run/result claimed yet.
- Artifacts produced:59 attempt2 scene12590981778 SHA256df64200ae68e8c1dbb83832062e9e8902fba6739bbd8b25a5e4bd16e2b93ae03 metadata; P1 log summary12591136635 SHA256128cb9d4c2e643db21a3ed0027acc88f6b6f384592c75fcdaac54aaa9752526a. No59 IPA. Full failed P1 log retrieved directly.

### Next steps

- Next Pikmin1 task: Run corrected Apple checks, then verify/stage native package and ask for focused two-phone private-room test. Continue actual game/world/guest camera/ownership integration after transport proof.
- Next Pikmin2 task: Keep working app untouched.
- GitHub/build task: One P1-only build for corrected compiler tool; record exact source/run and avoid idle polling.
- Anything requiring my involvement: Nothing on either phone now; report new build passed/failed when linked. PC installation and cloud/provider choices are deferred, not blockers to phone work.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User's two latest messages add PC-to-iPhone shared progress, exact live-host reconnect, host-loss recovery, optional continue-alone and useful researched QOL. New design file records all of them. Earlier blanket together-only wording is refined for desired temporary host continuation; independent divergent campaign merging stays deferred. First deliver pause/wait/rejoin safely.
- Important source-file locations: ios/COOP_CROSS_PROGRESSION_AND_RECOVERY.md links primary sources and staged acceptance; SAVE_AND_COOP_RECOVERY_PLAN.md and ONLINE_COOP_DESIGN_NOTES.md updated. Actual source-tool correction in tests/ios_coop_arc_names_test.py. Current connection-only UI remains ios/ios_coop_room.mm, real core session in libs/nectar_net. card_stubs.cpp writes native card buffers; cross-platform compatibility not proven by that alone.
- Relevant logs: work/build59-latest-run.json/jobs.json/artifacts.json, work/build59-attempt2-p1-full.log. Actual final error is test command ordering, not a remaining owned-object property diagnostic. Local Clang-tidy/driver-adapter diagnostics are limited-scope test evidence.
- Unverified fixes: Corrected standalone Apple invocation and full native screen/package pending. New recovery/cross-progression document is DESIGN, not implemented/runtime verified. Current frame replica does not serialize full jobs/AI/campaign state.
- Risks and warnings: Live host pause/rejoin can target host freeze tick while process remains alive; a killed host only recovers last fully committed checkpoint. Guest emergency backup must be host-authored COMPLETE recovery state, not screenshot/visual replica; it does not make live migration trivial. A relay doesn't store the campaign. Quit before mid-day persistence must disclose return to actual last verified saved day; never falsely label Save here. No cloud service, account changes or paid deployment.
- Exact next actions: Push corrected tool and durable plan in one P1-only run, record actual run. Verify actual UIKit/native/private-code/packaging output on completion. Stage verified IPA under Documents, alert user for two-phone test, preserve54/53 and P2. Then real world/ownership/rejoin adapter, complete checkpoint capture+restore, optional guest copy, later desktop parity/portable campaign handoff and cloud choice.

**END PROGRESS REPORT**
