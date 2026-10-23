# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-23 08:04 Eastern Daylight Time

**Overall project status:** Adaptive landscape display batch implemented for BOTH games and local verification passed. Apple native compilation, new IPA generation and phone validation are PENDING. No new phone install or settings/save changes. Latest user preference: LANDSCAPE ONLY, frame rate remains player-controlled INCLUDING 120 FPS; older 60 FPS preference is superseded.

### Pikmin 1

- Current objective: Adapt the current game window, advanced settings and controls to different phone sizes without stretching; retain selectable 120 FPS.
- What was investigated: Current SDL UIKit resize events/drawable updates, Retina rendering, fixed 56-unit settings margins, editor mapping, native-window sizing, bundled SDL high-refresh support and Apple/GitHub SDK documentation.
- Root cause or leading hypothesis: Confirmed fixed settings margins and aspect-clamped menu canvas; controls ignored native safe areas and inset-only changes; applying a saved desktop resolution could request a native window resize. Confirmed missing CADisableMinimumFrameDurationOnPhone permission despite existing 120 FPS option. Build42 was compiled with SDK18.5; Apple documents compatibility window limits on Duo with older SDKs. These findings do not prove every display or high-refresh symptom is resolved on hardware.
- Files changed: pc_mobile_layout.h, settings/pc_settings.cpp, touch/pc_touch.cpp, gl/pc_gfx.cpp, pc_window.cpp; shared ios_display.mm, Info.plist.in, iOS CMake and experimental workflow; tests and journals.
- Tests and results: 1,778 checks on actual P1/P2 layout/editor/size-query/window-resolution functions; MSVC and Clang diagnostics PASS. Prior fixed menu fails the new regression (negative control). Existing P2 menu/Retina/tap inverse checks409 iOS+302 desktop PASS, Clang PASS. Original bundle/identity/storage39 and icon configuration/copy6 checks PASS. Native UIKit bridge requires Apple build; fake host geometry is not UIKit runtime evidence.
- Confirmed working: Existing P1 hardware baseline from user. Build42 native/IPA PASS; verified unchanged original-ID IPA remains in folder1. New batch retains user-selected FPS/options/config file format and existing framebuffer presentation; no gameplay/follower/charge/audio/save edits.
- Remaining issues: Build42 normal-follow pacing hardware confirmation, genuine stuck-only teleport (explicitly UNTESTED), ignored idle ship Pikmin, rare clam scene/full campaign; new safe-area layout/folding/native 120 FPS hardware tests.

### Pikmin 2

- Current objective: Apply the same landscape adaptation and ProMotion opt-in while preserving working audio/gameplay.
- What was investigated: P2's own menu/touch/window/renderer paths; existing120 FPS option and timing; previous user-confirmed audio milestone.
- Root cause or leading hypothesis: Same display/layout issues in duplicate P2 code. Existing120 FPS selection retained; no global60 FPS cap introduced.
- Files changed: P2 pc_mobile_layout.h wrapper plus settings/touch/window/renderer files; shared iOS bridge/package/workflow and tests.
- Tests and results: Shared1,778 checks cover BOTH games; P2 iOS409/desktop302 menu checks PASS with Clang; Apple build/IPA/runtime pending.
- Confirmed working: User-reported Build32 audio/gameplay baseline (run39518825366); existing install/assets left alone.
- Remaining issues: New display build must compile and be verified; follow up on controls/audio/save/gameplay after installing a verified update. Full story not proven.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; local C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental; clean starting tree and fetched origin verified before edits.
- Starting commit: 473ec14a045c3071a0dae970d05478002087dfc5 (local=origin).
- Latest commit: Pending this batch commit; record source SHA/run immediately after push.
- Commits created: None yet for this display batch.
- Changes pushed: Not yet for this display batch.
- Uncommitted changes: Scoped display/package/workflow/tests/journal changes; no user changes existed initially. No proprietary assets, credentials, videos or phone reports staged.
- GitHub Actions run IDs: Latest completed42=39861241129 SUCCESS, source dbe796adb057d0d5c92b37ad9f5976143d5329ba; no active build at initial check. P2 working32=39518825366. New combined run pending dispatch.
- Build results: New batch LOCAL PASS only; native compile/link/IPA/phone PENDING. Workflow selects standard xcode-27 runner and Xcode27.1 (RC currently installed), asserts SDK>=27.1, retains minimum iOS15.0 and original app IDs. New toolchain compatibility/capacity is unverified until run.
- Artifacts produced: No new IPA. P1 Build42 unchanged backup at C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\Pikmin 1 - Build 42 - Smooth Following and Recovery.ipa; SHA256304ac9abd4c60d96d76eb95902a0716ab743a074b1c69003aad238f7f7efd6a1. P2 baseline and all backups preserved.

### Next steps

- Next Pikmin 1 task: After new IPA is validated, update existing app and test landscape on both sides, clear menus, touch/editor alignment, and ordinary following. Keep genuine teleport verification separate. Frame rate is the user's choice;120 remains experimental.
- Next Pikmin 2 task: Same display/touch checks, then verify Pikmin/enemy/wind audio remains present. No assets reimport or uninstall required.
- GitHub/build task: Commit/push one scoped combined [ios-build] source change; record exact run/source. Stop idle polling per user. On completion retrieve full job logs, fix actual errors if any, verify original-ID unsigned ARM64 IPA (including new plist permission), stage in accessible folder1 before requesting tests.
- Anything requiring my involvement: Nothing while preparing/building. Phone need not stay connected or run the game. Report build completion when convenient.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Latest display scope is BOTH games, LANDSCAPE ONLY, adaptive actual window/safe areas, user-controlled FPS with selectable120. Do not force60. New source layout uses UIKit current view safeAreaInsets divided by view bounds, then converts to drawable coordinates; saved button fractions remain unchanged by resizing. Editor uses the same inverse mapping. Release held touches on actual geometry changes, not on ordinary frames.
- Important source-file locations: ios/ios_display.mm isolated from forced GameCube BOOL headers; nectar_ios_storage links SDL2-static for native window access. P1 pc_mobile_layout.h provides shared pure geometry; P2 wrapper includes it. Header detects Apple platform before SDL is included. f1Layout uses actual aspect and safe margins; pc_gfx_get_drawable_size re-reads SDL drawable; pc_window_set_window_size adjusts only render budget on iOS. Info.plist enables ProMotion but retains landscape-only and minimum15.
- Relevant logs: work/display-start-runs.json; work/ios-display-test.cpp; work/p2-ios-menu-test.cpp; local commands check_display.cmd, check_display_clang.cmd, check_p2_menus.cmd/_clang. Prior42 full log and verification in friendly folder2. New CI logs pending.
- Unverified fixes: All new UIKit/native resize/folding and120 FPS runtime behavior. Existing SDL still uses its legacy UIKit window lifecycle; no claim that SDK upgrade alone proves live folding works. Original game HUD/cutscene aspect paths retained and need phone review. Sustained120 depends on screen, power/thermal state and workload.
- Risks and warnings: SDK27.1/Xcode27.1 runner change may uncover compiler/SDK compatibility failures; diagnose actual output. No guaranteed universal-device certification from synthetic sizes. User's prior navigation/teleport issues remain separate. No online or autosave development in this batch; agreed plans remain in repository.
- Exact next actions: Finish combined commit/push, record source/run, update handoff with dispatch metadata [skip ci]. Await completion without usage-consuming polling. Verify/stage each successful IPA independently; preserve installed working baselines. Update this report after actual native and phone results.

**END PROGRESS REPORT**
