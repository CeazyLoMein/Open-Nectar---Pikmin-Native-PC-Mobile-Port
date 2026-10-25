## Build61 dispatched — exact checkpoint

Run40208103332 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40208103332), sourcecda57702b309552934609c167c3397c15bcc3ea8; last API snapshot IN_PROGRESS, no conclusion/IPA verified.60 Apple UI syntax passed, but simctl spawn timed out with partial stdout lost. Underlying simulator-versus-native-hang cause unknown.61 preserves failure output/stages and bounds native test lifetime; native game/resource compile happens before runtime, runtime remains required and runs independently after compile failure unless cancelled. Local23 core+actual GNS tests and full encrypted co-op/private-room probe PASS;8 runner failure-path tests PASS. No phone tests ready; T01-T04 wait verified package. Local network test processes are confirmed finished; user told Cancel both firewall prompts, no security rules changed by agent. P2/phone/PC game installs preserved; full co-op/recovery/cross-progression still pending.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-25T15:41:02.272578+00:00 (October25 America/New_York session).

**Overall project status:**60 failed during simulator launch/execution of the real network probe, after Apple compiled the room screen successfully. Exact timeout root cause is not observable because previous runner lost partial stdout. Fixed evidence capture and bounded test execution; added failure regression tests; prepared isolated Windows real-network environment and verified23 tests plus complete private-room/session probe. Next P1-only CI batch will compile native app before strict runtime probe, collecting more independent results in one run. No hardware test ready yet.

### Pikmin1

- Current objective: Finish phone room-screen/app/package validation and obtain useful exact evidence if simulator networking stalls again.
- What was investigated: Actual60 run/jobs/full log and SHA-verified artifact; runner timeout/output handling; native watchdog/room probe lifecycle; experimental workflow sequencing. Built pinned GNS/protobuf sources locally in workspace only, verified existing SHA pins, using Windows BCrypt crypto and static dependencies.
- Root cause or leading hypothesis: CONFIRMED simctl spawn timeout90s after simulator boot returned and network binary linked. No native partial output retained in old failure artifact, so simulator infrastructure versus code hang remains UNKNOWN. Confirmed diagnostic defect fixed: TimeoutExpired.output and nonzero child output now retained with stage/main-entry evidence. Native watchdog produces bounded failure if test code hangs. Local complete network test passes but does not rule out Apple-specific failures.
- Files changed: tests/run_ios_coop_socket_probe.py; tests/ios_coop_socket_runner_test.py; libs/nectar_net/tests/coop_socket_probe.cpp; experimental workflow execution order; journals/checklist status.
- Tests and results:8 runner tests PASS covering timeout bytes/text partial output, absent main marker, wrong platform, missing success marker, nonzero output, diagnostic failures and simulator ownership. Strict new probe translation-unit compile PASS. Existing ARC getter check PASS. NEW isolated Windows CMake23/23 core+GNS real-UDP tests PASS, including gated auth/room and12s stress; complete revised co-op probe PASS from encrypted join through2captains/60Pikmin, pause/background/marker/loss and private-code/content-mismatch checks. Windows native process exited0, test watchdog/cleanup completed. Not an iPhone runtime result.
- Confirmed working:60 full iPhoneOS room-screen syntax check PASSED,19 CI core tests passed; shared scene startup/resume SUCCESS. Native simulator probe binary COMPILED/LINKED with correct platform.57 remains last full native P1+simulator networking successful build. User-tested P154 apps preserved.
- Remaining issues: Underlying Apple spawn timeout unknown. Full native app/resource-copy and updated simulator runtime checks still pending. No new IPA/phone connection result. Full co-op gameplay/world/private camera/Onion/save/PC handoff remains future work; existing plans unchanged.

### Pikmin2

- Current objective: Preserve working app.
- What was investigated: No P2 source/phone investigation.
- Root cause or leading hypothesis: None.
- Files changed: None.
- Tests and results: Not rebuilt/installed.
- Confirmed working: Prior user-confirmed apps remain unchanged.
- Remaining issues: Later engine-specific audit/co-op/save adapter.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental.
- Starting commit:ac5ece003633be656597828182fb7364b021b5c5, clean and matched origin after fetch.
- Latest source commit:cda57702b309552934609c167c3397c15bcc3ea8; following documentation-only checkpoint records61.
- Commits created:cda57702b309552934609c167c3397c15bcc3ea8 implements runtime evidence/watchdog/CI batch; documentation checkpoint follows.
- Changes pushed: Complete batch pushed;61 dispatched.
- Uncommitted changes: Clean after final documentation checkpoint; all source/journals pushed.
- GitHub Actions run IDs:60 run40204287553/source53466a4065fe017d5f3fa88b311e652885300ec2.
- Build results:60 scene121201787820 SUCCESS. P1121204903697 failed runtime runner TimeoutExpired, not compiler error. Full native game configure/compile/package SKIPPED under old ordering. New ordering preserves strict overall failure while letting native compilation run before runtime probe.
- Artifacts produced:60 P112603398343 SHA2563869c339dc2a799c5dfd51ecab233260dc53b03b250870ca28e337fcd1a03347 downloaded+verified; scene12603606981 metadata digest396fb79eae2d532f3b312c146896ea903544e67fa2ac1ce0cbd6d67cdf87ca33. No IPA. Probe binary hash cee406c0c1b62adc2ff830c68f4aad5b1e686576b4078332f433ede490ab7e96.

### Next steps

- Next Pikmin1 task: Review full native build/notices and updated simulator output. If successful, verify/stage exact IPA in Documents and activate only phone-checklist T01-T04. If runtime fails, use retained last phase/native-entry/stages and bounded logs rather than guess.
- Next Pikmin2 task: Preserve app.
- GitHub/build task: Commit/push one P1-only evidence+CI batch; record run/source and stop idle polling.
- Anything requiring my involvement: User was shown Windows Firewall dialogs for our two LOCAL test executables and told Cancel; those tests already finished successfully. No need to allow firewall, connect phones or reinstall. Report next build result when linked.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Underlying60 timeout not diagnosed as a game defect. Native UI compiler issues are now cleared. New local real-network cache makes broad test batches possible without GitHub; Windows success is not Apple/OpenSSL proof. No game source/functionality changes this batch; native watchdog only test executable, never in game's room UI.
- Important source-file locations: tests/run_ios_coop_socket_probe.py stores last-command-output.log/socket-session.log and failed_stage/probe_entered_main_observed/boot_completed, collects bounded filtered simulator diagnostics. Probe emits main/stage markers and has60s watchdog; parent simctl spawn timeout90s. Workflow compiles game and verifies resources before runtime; network runtime also runs after game failure if its binary built, unless cancelled. IPA still requires all checks successful.
- Relevant logs: Private work/build60-run.json/jobs.json/artifacts.json, build60-p1-full.log, build60-p1-artifact.zip. New local work/local-net-full-check.log has23 CTest passes and final NECTAR_COOP_SOCKET_PROBE_PASS; work/local-net-win-build.log builds dependencies. Reuse work/check_local_net_full.cmd and work/local-net-win/core-build. Dependencies and generated binaries are workspace-only, not a desktop game install or uploaded game assets.
- Unverified fixes: New Apple diagnostic runner/watchdog and reordered CI require actual run. No claim that the underlying timeout is solved. Room/data hashing/permission and actual two-phone LAN still unverified. Save/recovery/cross-progression design remains unimplemented.
- Risks and warnings: Local HostRoom tests listen and can trigger Windows Firewall prompts despite clients using loopback. Agent made NO firewall/security rule changes and advised Cancel. They already completed, so do not repeatedly reopen listeners while user plays another game. First local configure hit compiler PDB-service mismatch, fixed private build to embedded debug info/Release; private core config uses existing CRT convention, EHsc and static protobuf. These are environment/test setup changes, not product fixes.
- Exact next actions: Push one P1-only batch, record actual run and update accessible checklist/handoff. After result verify native and runtime/package independently; retrieve partial stdout and main/stage marker on any timeout. Keep no human tasks active until a verified ready IPA is supplied. Preserve all working installs and54/53 rollback.

**END PROGRESS REPORT**
