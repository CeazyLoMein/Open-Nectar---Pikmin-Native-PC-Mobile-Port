# OPEN NECTAR iOS — CODEX PROGRESS REPORT

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
