# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

**Date/time:** 2026-10-24 11:58 EDT

**Overall project status:** RESUMED by user2026-10-24.50 user screenshots show P1 title/gameplay/settings, with blurry world and a restrictive editor boundary. Source-level portrait-point budget defect reproduced:466x678 budget yields466x320 on2034x1398 landscape drawable. Pixel-resolution/native-follow and manual full-view button placement implemented in BOTH equivalent ports. Local1820 actual layout/persistence +70 actual pixel/migration checks PASS; Clang PASS; actual50 source negative control reproduces fault and fails new regression. Build51/run40109396851/source1450d21e1f60c9600c8556371e6f8f2f55cd7130/startup job120917764682 dispatched; native/runtime results PENDING. Hardware fix NOT verified;50 remains current verified IPA baseline. Landscape/player-selected120/settings/icons/IDs preserved.

### Pikmin 1

- Current objective: Correct soft game rendering and editor invisible edge boundary while preserving50 startup/framebuffer and existing phone data/layout.
- What was investigated: User photos: Display Resolution466x678 0.69(native),3D1.00x, aspectAuto,120FPS, VsyncOn, HUDOff; sharp touch/settings vs soft world. Settings list used SDL desktop portrait points; window setter reused them as render budget; renderer additionally retained logical-point fallback. Editor input/draw both use drawable pixels, but manual placement was strictly clamped to inset safe frame. Examined matching P2 implementation and actual touch save/load format.
- Root cause or leading hypothesis: Actual50 code with reported466x678 config reproduces466x320 game rendering on2034x1398 landscape drawable. This confirms source mechanism consistent with blur, not a measured phone framebuffer capture. Controls strict safe-frame clamp explains an artificial manual boundary; actual device safe-inset values not captured, so extent of user wall still needs hardware test.
- Files changed: Both ports settings/pc_settings.cpp: iOS native resolution list from current physical drawable, native dimensions follow reflow, portrait legacy entry falls back to native at initialization, correct saved-budget menu selection,0.67x truthful label. pc_window.cpp native selection maps to auto drawable-follow budget; gl/pc_gfx.cpp removes logical-point fallback while retaining explicit lower budgets/scales. touch/pc_touch.cpp: per-button fullBounds flag for deliberate manual edits, physical-view clamp, safe defaults unchanged, compatible optional sixth file field, negative offsets preserved only with flag, finite-coordinate checks. tests/ios_display_layout_test.py extended with actual load/save/editability; new ios_pixel_resolution_test.py; workflow runs host+ARM64 pixel fixture. Journals only otherwise; no UIKit lifecycle, display FBO, FPS/audio/AI/save algorithm edits.
- Tests and results: 1820 actual P1/P2 safe touch/editor/resize/persistence checks PASS with MSVC/C++14, including actual legacy/current file IO, manual edges/default safety and native-follow setter.70 actual resolution-list/startup migration/render-budget/fold/fixed-budget/scale/aspect checks PASS. Both fixtures Clang diagnostics/analyzer PASS. Actual50 negative fixture compiles, prints old466x320 result, fails new native-source assertion as expected.26 startup contract +12 runner host tests PASS, Python AST/git formatting PASS. Full Apple compile/IPA/new simulator/hardware PENDING.
- Confirmed working: User screenshots after50 instructions show P1 title, gameplay and advanced settings. Installed50 identity inferred from context, not independently read by USB UUID. Prior50 actual generic simulator startup/resume and both native/IPA checks confirmed.50 package backups/current install untouched. Audio/full background-resume/FPS output/control movement fix not hardware confirmed.
- Remaining issues: New build/native package; phone compare world clarity at1.00x and native landscape pixel resolution, move buttons to edges/save/reload/flip landscape, input alignment, performance/HUD and chosen FPS. Native pixel1.00x costs more GPU/memory than old low point budget; lower quality choices stay available and120 remains selectable. Existing follower pacing/teleport, idle recall, rare clam scene/full story still open.

### Pikmin 2

- Current objective: Apply the inspected equivalent native-pixel/editor correction in same build without disrupting user-confirmed installed audio/gameplay baseline.
- What was investigated: P2 has same SDL portrait-mode resolution list, logical-point fallback, render budget setter and editor safe-frame clamp; tested actual functions for both ports. No new P2 phone feedback received.
- Root cause or leading hypothesis: Same source mechanisms corrected preventively in P2; user blur/editor symptom currently documented for P1 only. Do not invent a new P2 hardware failure.
- Files changed: P2 counterparts of settings/gl/pc_window/touch changes above. Existing audio and ObjectSystem char const* correction retained; shared lifecycle unchanged.
- Tests and results: P2 actual function paths included in1820 layout/persistence and70 pixel/migration checks and Clang PASS.50 native/link/IPA passed previously. New native/IPA/runtime PENDING; existing installed P2 untouched.
- Confirmed working: User-confirmed prior32 audio/gameplay baseline, plus50 native/IPA and shared generic simulator lifecycle. No new P250/next hardware outcome claimed.
- Remaining issues: After successful new build and P1 first check, verify P2 launch/audio/menus/touch/background-resume and display/edge behavior. Full campaign remains unverified.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; local C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental. Fetched local/remote3c7dcce624c9d4b4cb8bf346a91c6576af62dbf2 matched. Only3 documentation pause files were initially uncommitted; preserved/replaced with resumed checkpoint. No newer/pending build (latest50 SUCCESS). No AGENTS.md found.
- Starting commit: 3c7dcce624c9d4b4cb8bf346a91c6576af62dbf2; prior known-good50 source ae2d68db907cf399699c6d0ebf3b6df856a85b68 retained.
- Latest source/local/remote checkpoint: 1450d21e1f60c9600c8556371e6f8f2f55cd7130. Follow-up [skip ci] dispatch journal may be newer; external checkpoint records final exact local/remote journal SHA.
- Commits created: One scoped two-port pixel-resolution/manual-edge source/regression/workflow/journal batch; exact source above if dispatched, otherwise pending.
- Changes pushed: Build51/run40109396851/source1450d21e1f60c9600c8556371e6f8f2f55cd7130/startup job120917764682 dispatched; native/runtime results PENDING. One combined run; existing successful scene gate retained, no duplicate trigger.
- Uncommitted changes: Scoped P1/P2 source/tests/workflow/journals before source commit, dispatch journal only until [skip ci] commit. Paused documentation preserved as history. No assets/IPAs/private photos/phone reports/credentials staged.
- GitHub Actions run IDs: 50=40003458275/sourceae2d68db907cf399699c6d0ebf3b6df856a85b68 all3 PASS, both verified IPAs retained. Build51/run40109396851/source1450d21e1f60c9600c8556371e6f8f2f55cd7130/startup job120917764682 dispatched; native/runtime results PENDING. Historical44-49 failures/root causes preserved in IOS27_SCENE_LIFECYCLE.md.
- Build results: New source LOCAL actual-code checks/Clang/negative control PASS; Apple full game compilation, new IPA and phone clarity/edge behavior PENDING. Prior50 actual simulator lifecycle and both native/IPAs PASS; user P1 photos establish visible runtime, not complete stability.
- Artifacts produced: No new IPA yet.50 original-ID verified IPAs remain in Documents/Open Nectar/1 - Install on iPhone with older42/32 package backups in folder5. New test plan and copied user photos/evidence in folder2; full latest handoff updated.

### Next steps

- Next Pikmin 1 task: After new native/IPA verification, update existing app same account/ID without uninstall/reset. Confirm Display Resolution is oriented physical landscape pixels;3D1.00x compare sharpness and HUD performance. Move button to outer edge, save/reopen/rotate and test tap hitbox. Default untouched buttons should stay safely inset.
- Next Pikmin 2 task: Use same combined build only after verification; preserve installed P2 until P1 first check passes. Test equivalent display/edge behavior plus Pikmin/enemy/wind audio and pause/resume.
- GitHub/build task: Build51/run40109396851/source1450d21e1f60c9600c8556371e6f8f2f55cd7130/startup job120917764682 dispatched; native/runtime results PENDING. Capture exact run/source and startup job, update checkpoint [skip ci], then stop idle polling. On completion inspect native fixture/full-game logs and exact IPAs; no hardware claims from compile.
- Anything requiring my involvement: No phone connection or open game needed while developing/building. User reports completion; request exact focused phone checks once a verified new IPA is ready. Photos retained privately; settings/layout data not read or changed on phone. Complete current phone-data backup still not made.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User resumed2026-10-24 after explicit pause. Two P1 issues tracked together. Source confirms low portrait budget path; both equivalent ports now use physical pixels/native-follow and manual full-view control placement. Current saved settings1.00x/120 retained; no FPS cap. More pixels means more cost; keep user-controlled lower budgets/scales. Do not confuse source reproduction with verified phone fix.50 remains last verified IPA, title/gameplay/settings visible in photos.
- Important source-file locations: Per-port settings rebuildResolutionList (iOS drawable branch), mainRowValue/mainRowChange and openMenu selection; pc_window_set_window_size native->0 budget follows current drawable; gl pc_gfx_begin_frame physical budget calculation. touch ButtonLayout.fullBounds, layout_defaults/load/save/layout/layout_place. tests/ios_pixel_resolution_test.py extracts actual list/setter/render calculations and supports --ref for50 negative control; ios_display_layout_test.py actual editor/default/IO integration. Workflow host+ARM64 fixtures. UIKit lifecycle/FBO selection unchanged.
- Relevant logs: work/build51-display.cpp/exe1820 checks, build51-pixels.cpp/exe70 checks; Clang run check-build51-clang.cmd PASS. build51-pixels-old.cpp/exe generated --ref ae2d68db... prints old466x320 then fails expected assertion; Python subprocess captured nonzero (Windows abort code is signed). Existing50 verification/logs/artifacts retained. Copied user screenshots in folder2 only, no uploads/Git assets.
- Unverified fixes: New native compile/IPA/phone still pending. Actual device drawable/internal size and safe-inset values were not retrieved; reproduction uses2034x1398/678x466 representative scene dimensions and reported466x678 config. Hardware performance/sharpness/manual-edge behavior/persistence/OS gesture overlap require retest. No new P2 runtime result; full story/follower teleport/rare bugs remain open.
- Risks and warnings: Native1.00x intentionally removes old low logical-point budget; GPU/memory cost rises. Preserve player choice120/lower FPS and lower resolution/scale; no forced cap. Defaults respect safe area; deliberate manual drag may approach system gesture/cutout regions but whole button remains inside visible view. Optional sixth fullBounds field is backward-compatible with old five-value rows; only manually edited controls opt in, other settings/layout not reset. Existing50 backups retained. No complete current phone-data backup; do not erase old phone.
- Exact next actions: Build51/run40109396851/source1450d21e1f60c9600c8556371e6f8f2f55cd7130/startup job120917764682 dispatched; native/runtime results PENDING. Once dispatched stop idle polling. Inspect startup gate then both full game jobs, including new pixel fixture. Verify exact original-ID ARM64 scene-enabled IPA before staging. Phone compare landscape native Resolution/1.00x sharpness/HUD and manual edge save/reload/rotation/tap, then P2 audio/display. Report hardware results separately from compile.

**END PROGRESS REPORT**

---

## Historical handoffs (current decisions above supersede older ready/build instructions)

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

**Date/time:** 2026-10-23 09:03 EDT

**Overall project status:** Build44 P1 native/link/package PASSED and unchanged original-ID IPA VERIFIED/READY in folder1. Build44 P2 compilation FAILED: one unique virtual return-type error repeated6 times. P2 correction implemented and local regression PASS; P2-only Build45/run39958190774 IN PROGRESS at sourcedd5683cec866d7f96f6fe5dcc2321b2d8426a088. New display/120 FPS phone results PENDING. Landscape only; player controls FPS including120; no forced60 cap.

### Pikmin 1

- Current objective: Install/test verified44 adaptive-landscape update without uninstall/reset/assets import; preserve saved settings and earlier baseline.
- What was investigated: Completed job120404306153 and artifact12500492417; ZIP digest, IPA contents, executable/device ABI, bundle identity/icons, actual Mach-O SDK/minimumOS and packaged high-refresh flag.
- Root cause or leading hypothesis: Build44 contains the adaptive safe-area/drawable/editor changes and ProMotion opt-in described in ios/IOS_ADAPTIVE_DISPLAY.md. Hardware scaling/folding/120 output remain unverified.
- Files changed: NO P1 code changes in this follow-up; verified/staged exact GitHub IPA and added plain test instructions. Previous shared display changes remain at source5f09f653b26d821079642ad23237c88ccd87b73d.
- Tests and results: Native compile/link/package PASS. Unmodified unsigned ARM64 iPhoneOS standard IPA, original org.opennectar.experimental.pikmin1 ID and Pikmin1 label, six icons byte-match, no separate-solo markers, existing navigation/aim/recall markers present. SDK27.1.0 confirmed in actual executable; minimumiOS15.0; CADisableMinimumFrameDurationOnPhone=true; landscape left/right only. IPA SHA25649db612ed3944dcff30b5f60a93bf16ad187f343fa47cbd1a53fa38f7b8dd636, 2832751bytes. New runtime validation NOT performed.
- Confirmed working: Earlier user P1 baseline;44 BUILD/IPA only.42 IPA backup retained unchanged. New update preserves original app identity and does not reset settings.
- Remaining issues: Test44 title/settings/control/editor alignment on landscape sides and Duo displays, FPS setting persistence/output; normal following/box-drop pacing still awaiting clear feedback; genuine stuck-only teleport explicitly UNTESTED, ignored idle ship Pikmin/rare clam scene/full story still unproven.

### Pikmin 2

- Current objective: Fix Build44's actual compiler blocker and retry P2 alone.
- What was investigated: Complete job120404306409 log (770k+ lines), complete failure ZIP12500333884, all compiler error occurrences, JStage base/derived headers/definitions and all JSGGetName call sites.
- Root cause or leading hypothesis: CONFIRMED one unique error repeated6 times: ObjectSystem::JSGGetName returns char* while virtual base JStage::TObject::JSGGetName returns const char*. This is not a valid override. ObjectActor and ObjectCamera already match the read-only base; ObjectBase::mName is const char*. Six translation units include the same header. No additional unique compiler/linker errors were found; linking was not reached, so later errors remain possible.
- Files changed: games/pikmin2/pikmin2-decomp/include/Game/P2JST/ObjectSystem.h declaration and src/sysGCU/JSTObjectSystem.cpp definition now return char const*; remove unnecessary const_cast and return mName directly. Add tests/pikmin2_jstage_name_test.py and early host/ARM64 regression wiring in experimental workflow. No audio/input/save changes.
- Tests and results: Actual base/system/actor/camera declarations and base/system definitions extracted into fixture:4 signature assertions +3 const virtual-dispatch cases PASS with MSVC/C++14 and Clang diagnostics. Old source fixture fails override compilation and assertion, matching CI (negative control). Build44's display/layout, packaging-config, adapter/container, menu/touch, enhancement/import and audio-route preflight tests all PASSED; only native compilation failed. Fix native build/IPA/runtime PENDING.
- Confirmed working: User-reported Build32 gameplay/audio baseline retained installed. P2's Build44 artifact is logs ONLY; no P2 IPA produced.
- Remaining issues: Complete P2-only native retry, inspect actual output; verify/stage new IPA before any phone request. Preserve working installed P2 until then.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port, local C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental. Starting working tree clean; fetched local/origin bothf23c62d5e33cc7ecfb8042dee5a04e32912229b6. No external changes found.
- Starting commit: f23c62d5e33cc7ecfb8042dee5a04e32912229b6 (journal); Build44 source5f09f653b26d821079642ad23237c88ccd87b73d.
- Latest source/local/remote commit at dispatch: dd5683cec866d7f96f6fe5dcc2321b2d8426a088; following documentation checkpoint recorded by git history. Build45 source remains this exact commit.
- Commits created: dd5683cec866d7f96f6fe5dcc2321b2d8426a088 — Match P2 cutscene name override to read-only JStage interface [ios-build] [ios-p2-only].
- Changes pushed: Sourcedd5683cec866d7f96f6fe5dcc2321b2d8426a088 pushed; Build45 has only P2 job120429205992, observed in_progress. P1 is not rebuilt.
- Uncommitted changes: Only dispatch journal update before documentation commit [skip ci]; source tree was clean after source push. No unrelated/user files or private materials staged.
- GitHub Actions run IDs:44=39950748289 combined FAILURE; P1 job120404306153 SUCCESS, P2 job120404306409 FAILURE. Duplicate43 confirmed CANCELLED. Retry45=39958190774, sourcedd5683cec866d7f96f6fe5dcc2321b2d8426a088, P2-only job120429205992 IN PROGRESS at dispatch.
- Build results: P1 native/link/IPA44 PASS. P2 native44 FAIL at override type; local correction PASS, new native pending. No hardware validation this follow-up.
- Artifacts produced: P1 IPA C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\Pikmin 1 - Build 44 - Adaptive Landscape and 120 FPS.ipa; SHA25649db612ed3944dcff30b5f60a93bf16ad187f343fa47cbd1a53fa38f7b8dd636. Artifact ZIP SHA256e7a47fbacdb70cfb76f0089d007bccf68573d339f7c01b269329cac926d4249c; UUIDb0e12e37-9091-3a54-b3ac-27222d5013b1. P2 full failure ZIP3,630,733bytes SHA2560213111c9d63a0669877df39b7d2154c7de25f5b65fad92b6939a91e4fa5331d; no IPA. Older42 and32 baselines/backups retained.

### Next steps

- Next Pikmin 1 task: Update existing app using the verified44 IPA and same signing account. Read folder1/Build44 - P1 Ready and Test Steps.txt. Test menu/control alignment on both landscape sides and Duo displays, optional120 persistence and Performance HUD output. Test ordinary following separately; do not call teleport verified unless a truly stuck follower visibly relocates.
- Next Pikmin 2 task: Finish P2-only retry; inspect full logs/artifacts on completion and fix actual remaining failures if any. No repeated relaunch/reset of working app needed.
- GitHub/build task: Build45 is already running P2 alone; no new trigger needed. Stop idle polling per user and retrieve actual completed logs/artifacts when user reports completion. No P1 rebuild.
- Anything requiring my involvement: P1 phone test when convenient; phone need not remain connected. User reports P2 retry completion. No P2 installation yet.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Both games' adaptive-display batch is source5f09f653. P1 passed44; P2 failed due a legacy shared cutscene-name declaration, unrelated to assets. Current P2 fix is type-correct and preserves returned name pointer/virtual slot. No guessing about audio or runtime. FPS user-controlled with120 enabled, landscape only. Autosave/online plans remain deferred.
- Important source-file locations: ObjectSystem.h:20, JSTObjectSystem.cpp:JSGGetName ~685; base include/JSystem/JStage/TObject.h:12; siblings ObjectActor/ObjectCamera. Shared display bridge ios/ios_display.mm and pc_mobile_layout.h remain unchanged. ios/IOS_ADAPTIVE_DISPLAY.md contains design and phone checklist.
- Relevant logs: work/build44-p2-full.log (complete job); outputs/Build44-Pikmin2/ios-build.log and ios-build-errors.md; work/build44-p2-errors.json (1 unique/6 occurrences); work/p2-jstage-negative.log; work/build44-jobs-final.json,build44-artifacts.json,build44-run.json; work/build44-verification.json. Friendly folder2 has P2 full failure ZIP/error JSON, P1 full successful log/verification and this handoff. Private downloads/logs never committed.
- Unverified fixes: New P2 const return correction native/link/IPA/runtime; P1/P2 display/folding, actual high-refresh output and all unresolved prior runtime behaviors. Successful host fixtures are not full-game or phone proof.
- Risks and warnings: New SDK can expose further legacy incompatibilities; actual make -k log currently shows only this one. Do not reset either installed app or upload game assets. Keep P1 passed44 available independently of P2 retry. SDK native window lifecycle/folding requires real device evidence. No spoilers.
- Exact next actions: Await P2-only Build45/run39958190774/sourcedd5683cec866d7f96f6fe5dcc2321b2d8426a088/job120429205992; stop idle polling. User reports completion. On success verify original-ID unsigned ARM64 P2 IPA incl SDK27.1/ProMotion/landscape metadata and icons; place in folder1, alert user, give targeted tests. On failure use complete actual log, group unique errors before changes. Independently receive P1 test44 feedback.

**END PROGRESS REPORT**

---

## Historical handoffs (current decisions above supersede old instructions)

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

**Date/time:** 2026-10-23 08:07 Eastern Daylight Time

**Overall project status:** Adaptive landscape display batch implemented for BOTH games and local verification passed. Combined Build44/run39950748289 is IN PROGRESS at source5f09f653b26d821079642ad23237c88ccd87b73d. Native results, new IPA generation and phone validation are PENDING. No new phone install or settings/save changes. Latest user preference: LANDSCAPE ONLY, frame rate remains player-controlled INCLUDING 120 FPS; older 60 FPS preference is superseded.

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
- Latest source/local/remote commit at dispatch: 5f09f653b26d821079642ad23237c88ccd87b73d; following documentation-only checkpoint is discoverable with git log. Build44 always uses this exact source.
- Commits created: 5f09f653b26d821079642ad23237c88ccd87b73d — Adapt both iOS games to landscape safe areas and allow selectable120 FPS [ios-build].
- Changes pushed: Source 5f09f653b26d821079642ad23237c88ccd87b73d pushed to origin/ios-experimental. Following dispatch journal uses [skip ci]; no redundant build requested.
- Uncommitted changes: Only this dispatch documentation update before its [skip ci] commit; source tree was clean after the source commit. No user changes existed initially. No proprietary assets, credentials, videos or phone reports staged.
- GitHub Actions run IDs: Latest completed42=39861241129 SUCCESS, source dbe796adb057d0d5c92b37ad9f5976143d5329ba; no active build at initial check. P2 working32=39518825366. Build44=39950748289, source5f09f653b26d821079642ad23237c88ccd87b73d, observed in_progress with build(pikmin1) job120404306153 and build(pikmin2) job120404306409. Duplicate43=39950747746 same source/event/path; cancellation accepted HTTP202; final duplicate conclusion not re-polled.
- Build results: New batch LOCAL PASS only; native compile/link/IPA/phone PENDING. Workflow selects standard xcode-27 runner and Xcode27.1 (RC currently installed), asserts SDK>=27.1, retains minimum iOS15.0 and original app IDs. New toolchain compatibility/capacity is unverified until run.
- Artifacts produced: No new IPA. P1 Build42 unchanged backup at C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\Pikmin 1 - Build 42 - Smooth Following and Recovery.ipa; SHA256304ac9abd4c60d96d76eb95902a0716ab743a074b1c69003aad238f7f7efd6a1. P2 baseline and all backups preserved.

### Next steps

- Next Pikmin 1 task: After new IPA is validated, update existing app and test landscape on both sides, clear menus, touch/editor alignment, and ordinary following. Keep genuine teleport verification separate. Frame rate is the user's choice;120 remains experimental.
- Next Pikmin 2 task: Same display/touch checks, then verify Pikmin/enemy/wind audio remains present. No assets reimport or uninstall required.
- GitHub/build task: Build44 is already in progress for both games; do not start another run. Stop idle polling per user. On completion retrieve full job logs, fix actual errors if any, verify original-ID unsigned ARM64 IPA (including new plist permission), stage in accessible folder1 before requesting tests.
- Anything requiring my involvement: Nothing while preparing/building. Phone need not stay connected or run the game. Report build completion when convenient.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Latest display scope is BOTH games, LANDSCAPE ONLY, adaptive actual window/safe areas, user-controlled FPS with selectable120. Do not force60. New source layout uses UIKit current view safeAreaInsets divided by view bounds, then converts to drawable coordinates; saved button fractions remain unchanged by resizing. Editor uses the same inverse mapping. Release held touches on actual geometry changes, not on ordinary frames.
- Important source-file locations: ios/ios_display.mm isolated from forced GameCube BOOL headers; nectar_ios_storage links SDL2-static for native window access. P1 pc_mobile_layout.h provides shared pure geometry; P2 wrapper includes it. Header detects Apple platform before SDL is included. f1Layout uses actual aspect and safe margins; pc_gfx_get_drawable_size re-reads SDL drawable; pc_window_set_window_size adjusts only render budget on iOS. Info.plist enables ProMotion but retains landscape-only and minimum15.
- Relevant logs: work/display-start-runs.json; work/ios-display-test.cpp; work/p2-ios-menu-test.cpp; local commands check_display.cmd, check_display_clang.cmd, check_p2_menus.cmd/_clang. Prior42 full log and verification in friendly folder2. New CI logs pending.
- Unverified fixes: All new UIKit/native resize/folding and120 FPS runtime behavior. Existing SDL still uses its legacy UIKit window lifecycle; no claim that SDK upgrade alone proves live folding works. Original game HUD/cutscene aspect paths retained and need phone review. Sustained120 depends on screen, power/thermal state and workload.
- Risks and warnings: SDK27.1/Xcode27.1 runner change may uncover compiler/SDK compatibility failures; diagnose actual output. No guaranteed universal-device certification from synthetic sizes. User's prior navigation/teleport issues remain separate. No online or autosave development in this batch; agreed plans remain in repository.
- Exact next actions: Await Build44/run39950748289 completion without idle polling. User will report completion. Retrieve its full jobs/logs/artifacts for source5f09f653b26d821079642ad23237c88ccd87b73d; verify/stage each successful IPA independently; preserve installed working baselines. Check actual SDK and new plist flag in packaged binary/metadata. Update this report after native and phone results. No new build for this journal.

**END PROGRESS REPORT**

---

## Historical handoffs below (current decisions above supersede old instructions)

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

**Date/time:** 2026-10-22 18:15 EDT

**Overall project status:** P1 Build42 PASSED native compilation/linking and IPA generation. The unchanged GitHub IPA is locally verified and READY in the accessible Documents install folder. New normal-follow pacing and automatic teleport PHONE TESTS PENDING. P2 unchanged on working user-reported Build32.

### Pikmin 1

- Current objective: Install/test the verified42 update for responsive ordinary following, the same box descent and return pacing; keep genuine stuck/teleport validation separate.
- What was investigated:62.525-second1562x720 recording ScreenRecording_10-22-2026 17-42-21_1.mov,12 sampled frames/contact sheet, read-only live phone navigation/settings/layout, formation target mutation, return-intent activation, shared route budget and completed-route handling.
- Root cause or leading hypothesis: Confirmed source behaviors: (1) height/distance immediately set return intent and route takeover stopped followers while waiting for the two-searches/sec shared queue; (2) pcProtectFormationEdge changed the formation target to an old platform trail BEFORE its downward-descent return, retaining the wrong target; (3) a completed walking route was classified as a failed return, causing an extra stop/retry. These are strong explanations for the reported symptoms, not a proven explanation for every map behavior.
- Files changed: Gameplay source remains dbe796adb057d0d5c92b37ad9f5976143d5329ba: aiCrowd.cpp measured-stall route entry, downward target preservation, completed-route handoff and distant-assignment retention; two regression fixtures. This milestone changes documentation/checklist only; no new gameplay build required.
- Tests and results: 140 route/recovery/retention,105 command/edge/config and58/58/7 campaign scenarios plus Clang PASS locally; Build41 negative controls failed8+1 cases as intended. Build42 native compile/link/host and iPhoneSDK checks/IPA generation PASSED. Artifact SHA256 matched GitHub; IPA CRC, original app identity, ARM64 iPhoneOS unsigned binary, standard-campaign/new feature markers and six original PNG icons verified. Exact downloaded IPA unchanged. Phone runtime PENDING.
- Confirmed working: Read-only collection found rescueON, BetterPathfindingON, both speeds100%,60FPS, BluesOnlyWaterON. Three files read while game running; no phone writes or save backup claimed. Log records route_built, four recall_idle_seen/recall_joined samples, one rescued_follower and four rescue_no_safe_spot samples. Those bounded samples have no clip time correlation and do not establish the user's untested teleport behavior as verified.
- Remaining issues: New pacing has not been tested on the phone. Automatic teleport remains explicitly UNTESTED by user; one untimed prior log event is not a successful clip-correlated test. Ignored idle ship Pikmin remains undiagnosed; four sampled recall candidates joined but did not identify that individual. Rare clam scene/full campaign unverified; no mid-day autosave or network feature.

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
- Starting commit: a148acedf09d97e2f2c27ee4cdb88f750f19910b, clean and matched fetched origin before this result/verification milestone; Build42 source remains dbe796adb057d0d5c92b37ad9f5976143d5329ba.
- Latest local commit: a148acedf09d97e2f2c27ee4cdb88f750f19910b
- Latest fetched remote commit: a148acedf09d97e2f2c27ee4cdb88f750f19910b
- Build source: dbe796adb057d0d5c92b37ad9f5976143d5329ba
- Commits created/changes pushed: Pacing source and dispatch notes already pushed. This ready/verification documentation checkpoint follows with[skip ci]; no further game edits or redundant CI run.
- Uncommitted changes: Only current ready/verification journal and checklist before their documentation commit; private phone/video/IPA/log data never staged.
- GitHub Actions run IDs: 42=39861241129 SUCCESS, source dbe796adb057d0d5c92b37ad9f5976143d5329ba, job120112185245;41=39854014424 SUCCESS;40=39784525620;37=39617967156; P2 working32=39518825366.
- Build results: 42 native/link/IPA PASS; normal-follow pacing and teleport phone tests PENDING.41 native/link/IPA PASS but phone normal following too slow; teleport untested. P2 not rebuilt.
- Artifacts produced: Artifact12462533086 nectar-pikmin1-experimental,5928221bytes, SHA256f1f89f790de786444dfeb74da74f957c0afaa7a4b6faf23fbb36cea116db219c. Verified unchanged IPA: C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\Pikmin 1 - Build 42 - Smooth Following and Recovery.ipa, 2822527bytes, SHA256304ac9abd4c60d96d76eb95902a0716ab743a074b1c69003aad238f7f7efd6a1. Original bundleorg.opennectar.experimental.pikmin1, labelPikmin1, standard unsigned ARM64 iPhoneOS, UUIDb9bf7bf9-dff9-3cec-9c86-f52e6cf57e8a. All prior IPAs/backups preserved.

### Next steps

- Next Pikmin 1 task: Update existing P1 with the verified42 IPA in folder1 using the same Sideloadly account. Keep Better PathfindingON, Rescue Stuck FollowersON, both speeds100%,60FPS. Leave workers on safe tasks and test ordinary group movement, the same box crossing and running off it without Recall All. Watch pauses/detours; then separately test a genuine stalled follower only if one occurs.
- Next Pikmin 2 task: Preserve current app; no update.
- GitHub/build task: No build needed. Await focused phone feedback; inspect actual report if movement or rescue fails. No idle polling.
- Anything requiring my involvement: Install/test42 when convenient. Do not uninstall/reset/import assets. Phone can be disconnected after installation until a specifically requested report collection.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User's latest clarification overrides the earlier ambiguous “technically works”: none was clearly stuck long enough to test teleport; all eventually walked back too slowly. Do not claim auto-rescue phone PASS based on one untimed log event. Goal now is smooth ordinary following, not a shorter teleport timer or a faster global queue.
- Important source-file locations: aiCrowd.cpp pcProtectFormationEdge now returns BEFORE touching a target when captain is lower; pcRecoverFollower keeps distance/height return OWNERSHIP but permits ordinary movement until measured stall, starts a route only after stall, and hands completed routes back successfully; exec keeps a valid distant return assignment from being dropped during ordinary-follow handoff. Invalid slots still fail, excluded states reset ownership, original no-enhancement/multiplayer behavior retained.
- Relevant logs: work/build42-run.json,build42-jobs.json,build42-artifacts.json,build42-artifact.zip,build42-verification.json; outputs/Build42-Pikmin1/ios-build.log. Accessible folder2 has Build42 full log and verification. Private prior failure evidence is in folder2/P1 - Build41 Slow Following -2026-10-22(actual folder includes spaces), and work/p1-phone-feedback-2026-10-22 174902. Only report/settings/layout read while app running; no phone writes/save backup.
- Unverified fixes: 42 phone installation, normal following/box drop/group responsiveness/assignment retention, true stuck-only teleport and ignored idle Pikmin cause. Full campaign unverified. Safe landing, enemy proximity and occupancy can delay rescue. Normal movement speed values and teleport timer/search limits were unchanged.
- Risks and warnings: No phone writes/uninstall/reset/save changes/private uploads. P1 original app identity and normal saving retained. Ordinary descent follows stock movement; water safeguards remain. P2 unchanged. No finale spoilers. No online/autosave work added.
- Exact next actions: User installs staged42 and follows the focused checklist. Collect pacing feedback first; only mark teleport tested if a genuinely stalled follower visibly relocates safely. If failure, collect p1-navigation-report.txt before repeated relaunches and correlate evidence before more code edits. P2 stays paused. No new native build just for documentation. Future tighter crossing queues/HUD/online/shared exact-scene saving remain proposals, not features in42.

**END MASTER HANDOFF**

---

# Archived checkpoints through Build40

The following is preserved historical context, superseded by the current checkpoint above.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-22 09:30 EDT

**Overall project status:** Build40 native P1 compilation/linking PASSED, GitHub packaging FAILED. Exact compiled app RECOVERED locally and verified IPA staged in Documents folder1. No new full build needed. P1 phone test pending; installed P1/P2 apps unchanged.

### Pikmin 1

- Current objective: Install recovered Build40 and verify narrow crossing/return behavior.
- What was investigated: Full job119844062115 log and artifact12429062159 (ZIP hash matched GitHub). Xcode combined @2x/@3x icons into Icon-29/40/60.tiff, removing the expected PNGs; strict verifier rejected missing Icon-29@2x.png. Native compile/link and all preceding checks passed.
- Root cause or leading hypothesis: Confirmed Xcode image-combination packaging issue. Prior source-property fix did add resources, but Xcode transformed them. Actual copied-output format matters; configure/host-Makefile tests did not cover this Xcode behavior.
- Files changed: ios/prepare_bundle_icons.py copies six approved original PNGs after Xcode, validates identity/variant/binary/icons and refuses signed bundles; CMake disables COMBINE_HIDPI_IMAGES; workflow runs preparation before recovery archive/IPA; bundle test covers TIFF-only regression, unchanged executable/TIFF, exact source icon bytes, signed-bundle rejection for both games/all variants; journal/checklist.
- Tests and results:39 metadata/storage/icon preparation/regression checks PASS; actual recovered compiled app passed the new helper and strict verifier. Local IPA CRC, every original app-file hash, original executable hash, Mach-O ARM64 iPhoneOS device/load commands/UUID/unsigned status and standard-game marker checks PASS. Six PNGs match approved source bytes. Future modified workflow has NOT run; no new native build requested. Hardware installation/runtime PENDING.
- Confirmed working: Build40 native compilation/linking; locally generated unsigned IPA is structurally verified. Previously user passed Aim/Soft Assist/charge-whistle/save reload and separate Recall All button. No v2 navigation phone success yet.
- Remaining issues: Last phone crossing/returns failed in37 even at100% speeds. New persistent returns/reachable floor-aware routes/circling detection need exact-crossing retest and crowd/frame-rate observation. Rare clam scene/full campaign unverified. No teleport/autosave/online feature added.

### Pikmin 2

- Current objective: Preserve working user-tested Build32; game development paused.
- What was investigated: Shared PNG preparation helper tested for P2 metadata and icons.
- Root cause or leading hypothesis: Same future Xcode resource-combination risk, bypassed by final PNG preparation step.
- Files changed: Shared iOS packaging/helper only; no P2 gameplay/audio changes.
- Tests and results: P2 preparation/identity/signed-bundle guard fixture PASS. No new native P2 build or installation.
- Confirmed working: User reported prior P2 Build32 working after audio fixes; existing app untouched.
- Remaining issues: Broader solo testing later, then agreed shared co-op/snapshot recovery design.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit:c0226a45a5a7edc7829628e48fd7b29410890ca0, clean and matched fetched origin.
- Latest commit:6cd2331d1c4cc9a92d4711417d6a402aa2026d42 recovery/packaging commit, pushed; this documentation completion record follows [skip ci].
- Commits created: 6cd2331d1c4cc9a92d4711417d6a402aa2026d42 — PNG preparation safeguard, TIFF-only regression and recovered IPA record [skip ci].
- Changes pushed: Packaging safeguard and recovery journal pushed. No new build triggered; current recovered IPA is ready.
- Uncommitted changes: No uncommitted code; this documentation completion record is being saved. No gameplay edits. Private phone/video/IPA files never staged.
- GitHub Actions run IDs:40=39784525620, sourcece63c20c4ad258d202e2ccb47f36cb18c201bd4c, job119844062115;39=39666676388;38=39664622876;37=39617967156; P2 working32=39518825366.
- Build results:40 native compile/link PASS; GitHub packaging FAIL (PNG-to-TIFF). Local packaging/verification PASS.39 native compile PASS/packaging FAIL;38 configuration FAIL;37 native/IPA PASS but phone navigation FAIL. Do not label overall GitHub40 green.
- Artifacts produced: GitHub40 artifact12429062159 includes original compiled-app tar and logs. Recovered **Pikmin 1 - Build 40 - Navigation Update.ipa**, 3070929bytes, SHA256 02d057e55a2e77a0779462f37e420c2a5e665fa01c6523ee6c4129f1e65f7cdd; bundleorg.opennectar.experimental.pikmin1, executableNectar-pikmin1, labelPikmin1, standard campaign. Executable SHA256 c9d8a7a74a63435dde951d2056208a44541f8784029027c2c409d129cfc57ebc, UUID efbbdda7-b705-3781-911c-2506a447300f. Exact original files preserved; only six PNGs added. Old TIFFs harmlessly retained.

### Next steps

- Next Pikmin 1 task: Update existing P1 with recovered40, same Sideloadly account; normal100% crossing in both directions, wait safely for a stranded follower, then explicit Recall All; check basic controls/performance. No uninstall/reset/new asset transfer. Can disconnect after install.
- Next Pikmin 2 task: Keep current working app; no action now.
- GitHub/build task: Packaging safeguard and recovery journal pushed with [skip ci]; no Build41 needed solely for this packaging issue. Future native build will exercise updated workflow.
- Anything requiring my involvement: Install/test recovered40 when convenient. If still stuck, report exact attempt and connect USB only when requested for p1-navigation-report.txt; avoid repeated relaunches before collection where practical.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Build40 game compiled; recovered exact unsigned app is READY in folder1 despite failed GitHub packaging. Never make the user wait for another full build just to add these icons. No navigation hardware result yet.100% baseline reproduces old failure;500% not a development focus. Recall All includes workers, normal whistle local.
- Important source-file locations: ios/prepare_bundle_icons.py, CMakeLists.txt COMBINE_HIDPI_IMAGES, workflow pre-archive preparation; tests/pikmin1_solo_app_test.py. Navigation unchanged from2d1e2800/ce63c20c and documented in ios/PIKMIN1_STRANDED_FOLLOWERS_PLAN.md. Checklist ios/PIKMIN1_CROSSING_RECALL_SPEED_TEST.md.
- Relevant logs: work/build40-full-job.log,build40-jobs.json,build40-artifacts.json,build40-verification.json; original artifact/tar/log copied to folder5/P1 Build40 - Original Compiled App. Accessible folder2 Build40 full log, verification and recovery note. Source recordings/backups stay private.
- Unverified fixes: Phone installation, Home Screen icon appearance and real navigation/physics/crowd behavior; future automated PNG-preparation workflow. Local structural verification cannot certify full solo campaign.
- Risks and warnings: Preserve installed apps/settings/assets. No phone write/uninstall, no credentials/signing manipulation, no save reset or proprietary data uploaded. Signed bundle preparation is rejected. No teleport selected. No finale spoilers. Route graph may still lack safe paths; get real report before another speculative game fix.
- Exact next actions: Recovery code/journal pushed; user installs focused checklist. If pathing fails retrieve p1-navigation-report.txt and correlate coordinates/reason with crossing. If it passes, complete representative regression then proceed to agreed co-op prototype/shared saving plan. P2 remains paused. Saved plans: SAVE_AND_COOP_RECOVERY_PLAN.md and ONLINE_COOP_DESIGN_NOTES.md.

**END PROGRESS REPORT**


# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-22 09:09 EDT

**Overall project status:** Build39 native P1 compilation/linking PASSED, but IPA packaging FAILED because Home Screen icon files were absent. Corrected their CMake source-property scope; replacement standard P1-only Build40 queued fromce63c20c4ad258d202e2ccb47f36cb18c201bd4c. Installed games, settings and saves untouched.

### Pikmin 1

- Current objective: Package the successfully compiling navigation v2 update and test the exact narrow crossing/Recall return on phone.
- What was investigated: Complete Build39/job119453432371 log: configuration/native compilation succeeded; strict bundle verifier failed on missing Icon-29@2x.png. No compiler/linker errors; one harmless ld warning had been misclassified by the short index.
- Root cause or leading hypothesis: Confirmed source-property scope problem: native RESOURCE target files were declared from ios/, while executable sources belong to games/pikmin1/. Xcode did not put icons in its copy-resources phase. Explicit MACOSX_PACKAGE_LOCATION=Resources now set using TARGET_DIRECTORY for the actual game target. Host directory regression previously checked configuration/target lists, not real bundle copies; expanded accordingly.
- Files changed: ios/CMakeLists.txt resource source properties; tests/ios_icon_resources_test.py checks six icon properties in target scope, rejects Build38/39 forms, and builds/hashes a real tiny app bundle on Apple runners; workflow preserves a compiled-app tar archive before strict packaging; error index no longer counts ld warnings as errors; Xcode PNG conversion disabled to keep standard opaqueRGB files compatible with strict verifier; journal/checklist.
- Tests and results:6 real host CMake configuration/negative-control checks PASS;27 identity/storage/icon verifier checks PASS; full Build39 compiler index has0 errors. New fixture performs2 additional actual app-copy checks on Apple runners (not executed on this Windows host). Build39 already passed the navigation87, surface17, command82, speed283+283 and other CI fixtures, native game compilation/linking. Corrected native bundle/IPA and phone navigation are pending.
- Confirmed working: Build39 navigation v2 source compiles/links for iPhone ARM64. Existing user controls/save and Recall All button checks remain as before. Native compilation is not proof of improved crossing behavior.
- Remaining issues: Phone crossing/return still last reported FAIL on Build37 at100% speeds; v2 has not been installed. Rare clam scene/full campaign unverified. No teleport, mid-day autosave or online feature added.

### Pikmin 2

- Current objective: Preserve working user-tested Build32, game development paused.
- What was investigated: Shared icon source-property issue and regression apply to both target directories.
- Root cause or leading hypothesis: Same future packaging risk; shared setup corrected.
- Files changed: Shared packaging/workflow only; no P2 game/audio source changes.
- Tests and results: P2 child-scope positive and both historical negative controls PASS. No new P2 native build or phone test.
- Confirmed working: User reported P2 working after prior audio fixes; existing app untouched.
- Remaining issues: Broader solo campaign testing later; co-op and shared recovery foundation remain planned.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit:76c4bde91f8f9a23c7c794fec7b238229f814f47, matched fetched origin, clean before edits.
- Latest commit:ce63c20c4ad258d202e2ccb47f36cb18c201bd4c correction/build source, pushed; documentation run record follows [skip ci].
- Commits created: ce63c20c4ad258d202e2ccb47f36cb18c201bd4c — icon target-source scope, real Apple bundle fixture, compiled-app recovery archive and warning filter.
- Changes pushed: Correction pushed to ios-experimental.
- Uncommitted changes: No code changes uncommitted; documentation run record being saved. No game source edits this correction.
- GitHub Actions run IDs:40=39784525620 QUEUED sourcece63c20c4ad258d202e2ccb47f36cb18c201bd4c;39=39666676388 FAILED, sourcea7075569c07b75655ea78a151a8940303ad354ba, job119453432371;38=39664622876 configuration FAIL;37=39617967156 native/IPA SUCCESS but phone crossing FAIL. P2 working32=39518825366.
- Build results:39 native configuration/compile/link SUCCESS, strict packaging FAIL. New correction native/IPA/phone pending.
- Artifacts produced:39 artifact12379875068 contains logs only, NO IPA/app binary; compiled app was not retained in that run. New archive step preserves future compiled apps for packaging recovery. Existing35/37/P2-32 backups intact.

### Next steps

- Next Pikmin 1 task: Replacement P1-only standard build; inspect actual Apple resource-copy fixture and IPA verifier, download/verify original-ID ARM64 app/icons/standard campaign, stage folder1, then exact crossing/Recall phone test.
- Next Pikmin 2 task: Keep existing working app; no rebuild in this batch.
- GitHub/build task: Build40/run39784525620 sourcece63c20c4ad258d202e2ccb47f36cb18c201bd4c dispatched. Stop idle polling; user reports completion.
- Anything requiring my involvement: Nothing now; phone may remain disconnected. Installation/test comes after a verified IPA is staged.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: The game now compiled natively in39; failure is missing app icon resources. Do not diagnose it as navigation compiler or runtime failure. No new on-phone v2 result. Build37 normal100% speed crossing fails;500% is not the development target.
- Important source-file locations: ios/CMakeLists.txt TARGET_DIRECTORY/MACOSX_PACKAGE_LOCATION icon block; tests/ios_icon_resources_test.py actual bundle copy checks; .github/workflows/ios-native-experimental.yml archive step; ios/PIKMIN1_CROSSING_RECALL_SPEED_TEST.md. Navigation files/functions recorded in prior report/PIKMIN1_STRANDED_FOLLOWERS_PLAN.md; unchanged this correction.
- Relevant logs: work/build39-full-job.log,build39-jobs.json,build39-compiler-index.md; accessible folder2/Build39 - Full Failed Job Log.txt and Build39 - Packaging Failure.md. Error: iOS bundle validation failed: missing Icon-29@2x.png. All phone recordings/save backups remain private in folder2/folder5.
- Unverified fixes: Corrected iOS resource copies/IPA packaging, Apple-only fixture bundle builds, v2 actual crossing/crowd/return behavior. Local scope checks are not full native bundle evidence.
- Risks and warnings: No app uninstall, phone write, save reset or asset overwrite. Preserve original IDs/settings. Shared icon setup corrected for P2 but only P1 build requested. Route graph still may lack usable links. No teleport policy chosen. No finale spoilers.
- Exact next actions: Build40 dispatch recorded; stop waiting. After completion inspect full logs; if success verify/stage IPA and run focused phone checklist. If packaging fails again, new compiled-app archive should permit local recovery without rebuilding. If phone pathing fails, collect p1-navigation-report.txt before repeated relaunches. Saving/co-op roadmap unchanged in SAVE_AND_COOP_RECOVERY_PLAN.md and ONLINE_COOP_DESIGN_NOTES.md.

**END PROGRESS REPORT**


# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-21 16:01 EDT

**Overall project status:** Build38 failed during CMake configuration, before native game compilation. Exact icon-packaging cause corrected locally; replacement P1-only standard Build39 dispatched, observed queued. Navigation source retained. Installed P1/P2 apps untouched.

### Pikmin 1

- Current objective: Produce the navigation v2 IPA for the existing app, then test the same crossing/return at normal speed.
- What was investigated: Full Build38 job119446251421 log and all step results. Enhancement checks succeeded; configuration failed at ios/CMakeLists.txt:145.
- Root cause or leading hypothesis: Confirmed packaging error: add_custom_command(TARGET pikmin_pc POST_BUILD) was called in ios/, but the target is created in games/pikmin1/. CMake rejects this directory mismatch. This was introduced with the approved name/icon source integration, not a navigation compiler or phone failure.
- Files changed: ios/CMakeLists.txt now attaches icons as native RESOURCE target files; new tests/ios_icon_resources_test.py configures the actual block against child-directory P1/P2 targets and verifies the old error as negative control; experimental workflow runs it before expensive configuration. tests/ios_build_error_summary.py now recognizes configuration errors and their target-scope explanation.
- Tests and results:4 real CMake configuration/negative-control checks PASS;27 app metadata/storage/icon checks PASS; actual full-log error-index regression and compiler/linker deduplication/non-error probe controls PASS. Build38 CI87 routes,17 surfaces,82 commands,283+283 speed, campaign/profile/mod/performance checks PASS. Native game compilation was never reached. No new IPA or phone result.
- Confirmed working: Existing Build35 phone controls/save baseline, global Recall button user pass; Build37 IPA compiled but crossing failed even at100%/100%. Navigation v2 is source implemented and fixture checked only.
- Remaining issues: Exact crossing, circling/return persistence, reachable route entry and crowd performance need phone verification after successful replacement build. Rare clam scene/full campaign unverified. No teleport/autosave/online code added.

### Pikmin 2

- Current objective: Preserve user-confirmed working Build32; development remains paused.
- What was investigated: Shared icon setup would have had the same directory mismatch for P2; new cross-directory CMake regression includes P2.
- Root cause or leading hypothesis: Same shared icon packaging setup, corrected for future builds.
- Files changed: Shared iOS packaging only; no P2 gameplay/audio source changes.
- Tests and results: P2 icon configuration succeeds and old target-scope version fails as expected. No P2 native build requested.
- Confirmed working: User reported P2 working after Build32 audio changes; installed app untouched.
- Remaining issues: Broader spoiler-free solo testing and later shared co-op/recovery foundation.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: dfc632b66386dbca088ae1105387c13ab1d9fd66, fetched and matched origin.
- Latest commit: a7075569c07b75655ea78a151a8940303ad354ba correction/build source, pushed; documentation dispatch record follows [skip ci].
- Commits created: a7075569c07b75655ea78a151a8940303ad354ba — icon resource correction, real directory regression and configuration error index.
- Changes pushed: Correction pushed to ios-experimental.
- Uncommitted changes: Code committed/pushed; documentation dispatch record being saved. Navigation code unchanged from2d1e2800d2e3d42908914bdd63bba91707ac684d.
- GitHub Actions run IDs: Build39=39666676388 QUEUED sourcea7075569c07b75655ea78a151a8940303ad354ba; Build38=39664622876 FAILED, source2d1e2800d2e3d42908914bdd63bba91707ac684d, job119446251421. Build37=39617967156 SUCCESS but phone pathing FAIL; Build36 CANCELLED; P2 working32=39518825366.
- Build results: Configuration error only; not a compiled-game or runtime result. Replacement Build39 queued; native compile/IPA/phone pending.
- Artifacts produced: No Build38 IPA; failed-job log preserved. Existing P1Build35/37 and P2Build32 IPA backups unchanged.

### Next steps

- Next Pikmin 1 task: Verify replacement build/artifact, stage original-ID IPA in folder1, repeat normal-speed crossing/Recall checklist. Retrieve p1-navigation-report.txt if it fails.
- Next Pikmin 2 task: Keep working baseline; no rebuild in this batch.
- GitHub/build task: Build39/run39666676388 sourcea7075569c07b75655ea78a151a8940303ad354ba dispatched. Stop idle polling; user reports completion.
- Anything requiring my involvement: Nothing now; phone not needed until installation or a requested log collection.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Build38 blocked by confirmed icon CMake directory error. Game source retained; prior normal-speed phone failure is real and not attributed to500%. No new navigation hardware result yet.
- Important source-file locations: ios/CMakeLists.txt icon resource block; tests/ios_icon_resources_test.py; tests/ios_build_error_summary.py. Navigation: pc_follow_trail.h stalledToward, pc_follow_surface.h, pc_follow_report.h, aiCrowd.cpp pcRecoverFollower/pcProtectFormationEdge, piki.cpp pcBuildFollowerRoute/pcMoveFollowerRoute, navi.cpp shared route budget.
- Relevant logs: work/build38-full-job.log and build38-jobs.json; corrected build38-error-summary.md; accessible folder2/Build38 - Full Failed Job Log.txt and Build38 - Configuration Error.md. Private video/phone backups remain in folder2/folder5 as recorded in prior report.
- Unverified fixes: Native Apple resource copying after this correction, full navigation game compilation and phone crossing behavior. Host CMake regressions prove directory setup, not iOS runtime.
- Risks and warnings: No installed app changes or lost progress. Shared icon resource setup changed for both games but P1-only build planned. CMake documents native RESOURCE files for flat iOS bundles: https://cmake.org/cmake/help/latest/prop_tgt/RESOURCE.html . Existing route limitations remain; no guaranteed recovery if graph lacks a safe path. Keep spoilers excluded.
- Exact next actions: Build39 dispatch recorded; stop waiting. When user reports completion, retrieve full log, fix any actual compiler error or verify native ARM64 bundle/identity/icons/standard variant, stage accessible IPA, then phone test. P2 remains paused; solo/autosave/co-op plans remain unchanged.

**END PROGRESS REPORT**


# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-21 15:47 EDT

**Overall project status:** P1 Build37 compilation passed but phone navigation failed even at100% speed. Navigation v2 batch implemented and locally verified; P1-only standard Build38 dispatched and observed in progress. P2 working user baseline preserved, development paused.

### Pikmin 1

- Current objective: Reliable narrow-crossing following and walking returns after explicit Recall All.
- What was investigated: Both11:23/11:26 clips, actual formation/progress/route/terrain code, consistent read-only8-file phone backup. User100%/100% retest confirms same failure.
- Root cause or leading hypothesis: Confirmed code defects: circling counted as progress; route failure/distance could release returning followers; geometrically nearest route entrances were not validated for walkability; highest-floor queries confuse overhead platforms. Which specific failure occurred in each clip is not internally logged. Speed is not the root-cause conclusion.
- Files changed: pc_follow_trail.h, new pc_follow_surface.h/pc_follow_report.h; Piki.h/PikiAI.h; aiCrowd.cpp/Piki helpers in piki.cpp/Navi route budget in navi.cpp; settings help; command/route/surface fixtures; experimental workflow; journals/checklist.
- Tests and results:87 route/recovery,17 layered floor/wall,82 commands,283 speed P1 plus283 P2 stock control,58/58/7 campaign and27 identity/storage/icon checks PASS. MSVC and Clang checks PASS. Full Apple build, new IPA and phone validation PENDING.
- Confirmed working: User previously passed Aim/Soft Assist/charge-whistle/save-reload; separate global Recall button works. Build37 generated an IPA. New pathing is not confirmed fixed.
- Remaining issues: Crossing falls/stranded return; v2 real-map physics, route availability, crowd cost. Rare clam scene/full campaign unverified. No teleport, mid-day autosave or online feature added.

### Pikmin 2

- Current objective: Preserve user-confirmed working Build32; resume broader testing after P1.
- What was investigated: No new P2 gameplay investigation; shared speed fixture run as stock behavior control.
- Root cause or leading hypothesis: No new P2 bug diagnosis in this batch.
- Files changed: No P2 game source changes. Existing approved name/icon source remains inherited from ee380c59.
- Tests and results:283 P2 stock-speed control checks PASS; no new native P2 build/phone test.
- Confirmed working: User reported P2 working after audio fixes. This is a representative test, not full-campaign certification.
- Remaining issues: Thorough spoiler-free campaign/transition test later, then separately scoped co-op work.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: ee380c593633f8b6bc609c9e293377e79e2d9556
- Latest commit: 2d1e2800d2e3d42908914bdd63bba91707ac684d local and origin for the build source; documentation-only run record follows [skip ci].
- Commits created: 2d1e2800d2e3d42908914bdd63bba91707ac684d — P1 navigation v2 batch, [ios-build] [ios-p1-only].
- Changes pushed: All locally verified P1 changes pushed to ios-experimental.
- Uncommitted changes: No code changes left uncommitted; this documentation run record will be committed/pushed with [skip ci]. Private phone/videos never staged.
- GitHub Actions run IDs:38=39664622876 IN_PROGRESS source2d1e2800d2e3d42908914bdd63bba91707ac684d;37=39617967156 SUCCESS sourceabd06b6216f0d09bc13361ddbff693f58640a21f;36=39614665805 CANCELLED;35=39548476790 SUCCESS. Build38 observed in progress; no completion polling scheduled.
- Build results: New v2 Apple compilation PENDING. Do not confuse local fixture pass with hardware correctness.
- Artifacts produced: No v2 IPA yet. Build37 artifact12354447804 preserved; named P1Build37 SHA2567e5837bbc83e40ae3f41736b0e00da1e292e546bedc4075aa2192884c74d5654. P2 named working32 and P1Build35 restore retained.

### Next steps

- Next Pikmin 1 task: Run next original-ID standard P1-only build, verify IPA, place in folder1, retest exact crossing/Recall at100% then usual modest speed; use navigation report if it fails.
- Next Pikmin 2 task: Remain on working build; resume planned stronger solo testing after P1 fixes.
- GitHub/build task: Build38/run39664622876 dispatched from2d1e2800d2e3d42908914bdd63bba91707ac684d. Stop waiting; user will report completion. Inspect full job log/artifact then.
- Anything requiring my involvement: Nothing now; phone read complete, may disconnect. Next action will be installation/test once IPA is verified and staged.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know:100% speed reproduced;500% saved config was later experimentation. Do not restart or claim pathing is solved. No teleport selected. Regular whistle local, explicit Recall All includes workers. Preserve original app/settings/private assets and spoiler preference.
- Important source-file locations: games/pikmin1/src/plugPikiKando/aiCrowd.cpp pcRecoverFollower/pcProtectFormationEdge/exec; piki.cpp pcBuildFollowerRoute/pcMoveFollowerRoute/pcSteerFollowerGoal/pcFollowerSegmentClear; pc_port/pc_follow_trail.h stalledToward; pc_follow_surface.h; pc_follow_report.h; navi.cpp pcTakeFollowerRouteBudget. Full technical notes in ios/PIKMIN1_STRANDED_FOLLOWERS_PLAN.md.
- Relevant logs: Current two clips/contact sheets private folder2/P1 Build37 - Crossing and Recall Failures; consistent8-file phone backup in folder5/P1 Phone Backup - 2026-10-21 - Before Navigation v2. Historical solo events are Build33, not new navigation evidence. New p1-navigation-report.txt will exist only after new build runs and emits events.
- Unverified fixes: All v2 phone navigation and source icon-copy pipeline native compilation. Unit fixtures do not simulate actual cardboard collision/crowd physics.
- Risks and warnings: Route graph might lack a safe link; bounded candidate search may miss distant entrances; centerline probes do not solve all body/crowd collision. No positions overwritten. P2 source untouched. Private videos/saves/assets not uploaded.
- Exact next actions: Build38 source/run recorded; stop idle polling. On completion inspect full logs/artifact; if success verify identity/ARM64/icons/variant and stage IPA; test checklist. If failed inspect actual compiler log before patching. If phone still fails retrieve navigation report before further diagnosis. Shared exact-scene saving/co-op recovery design remains later work in ios/SAVE_AND_COOP_RECOVERY_PLAN.md and ONLINE_COOP_DESIGN_NOTES.md.

**END PROGRESS REPORT**


# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-21 11:00 EDT

**Overall project status:** Combined P1 Build37 PASSED. Original artifact verified and preserved; app names/icons added locally to P1Build37 and working P2Build32, both ready to sign/install. New Home Screen and P1 gameplay runtime checks pending. Generated artwork explicitly approved by user. No new build required for cosmetic metadata/resources.

### Pikmin 1

- Current objective: Install decorated Build37 over existing P1, then exact raised-crossing/return-route and recall/speed test.
- What was investigated: Full successful job119283713514 log, artifact12354447804, unsigned ARM64 app metadata/load commands/variant markers; original versus decorated ZIP entries/executable hashes; generated icon resources.
- Root cause or leading hypothesis: Previous crossing/route fixes implemented as documented below; Apple compilation now passed. No new gameplay issue diagnosed this turn. App previously lacked iOS icon declarations/resources and had a long OpenNectar label.
- Files changed: ios/app_variant.cmake labels; Info.plist.in CFBundleName/icons; CMakeLists.txt post-build icon copy; verify_bundle_info.py metadata/dimension/opaquePNG checks; icons assets/provenance/prompts; bundle fixture copies icon resources; journal/checklists. No gameplay source changes this turn.
- Tests and results: Build37 CI63 crossing/routes,82 command/recall,283 speed P1 and283P2 stock-speed control, campaign checks and native compile/package PASS.27 actual local CMake/identity/storage/icon-wiring checks PASS. Decorated IPA ZIP/metadata/icons and every unchanged source entry compared byte-for-byte; executable hash unchanged. Future CMake icon-copy pipeline configured, not Apple-compiled yet; local decorated IPA checked directly.
- Confirmed working: Build35 user-tested controls/save baseline; Build37 Apple compile and IPA generated. Decorated app not phone-installed or runtime-tested yet.
- Remaining issues: Exact cardboard crossing/crowd/route return, recall separation, speed and regressions need phone evidence. No teleport, mid-day autosave or online feature. Rare clam scene/full campaign remain unverified.

### Pikmin 2

- Current objective: Cosmetic rename/icon only; preserve working game baseline.
- What was investigated: Existing verified unsigned Build32 IPA and all original ZIP entries; no new game source/audio audit.
- Root cause or leading hypothesis: Old long label/no dedicated Home Screen icon metadata, now addressed in package/source.
- Files changed: Shared iOS metadata/resource pipeline and P2-specific generated icon assets. P2 game executable byte-identical to Build32.
- Tests and results: Repacked unsigned IPA integrity, original identity/minOS and opaque icons PASS; all original payload except Info.plist byte-identical; executable hash unchanged. No P2 recompile or new phone test.
- Confirmed working: Previous user-positive Build32 runtime/audio baseline retained in identical executable.
- Remaining issues: Phone Home Screen/startup/save/settings cosmetic-update check; broader future P2 readiness tests still queued.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental.
- Starting commit: bb619e65a7421e92b64bf80309d579e489d9cd60, clean/fetched/no divergence.
- Latest source: P1Build37 abd06b6216f0d09bc13361ddbff693f58640a21f; P2Build32 1f04dd8f0117b91c0e5cc6e80cd61384943603e9. Cosmetic source commit recorded after push; no game executable patched.
- Commits created / changes pushed: Persistent names/icons/verifier and result journal, skip-ci commit follows.
- Uncommitted changes: This cosmetic source/report while recording; commit before ending and append final clean commit.
- GitHub Actions run IDs: Build37/run39617967156 SUCCESS/job119283713514/artifact12354447804. Build36 cancelled. P2 baseline Build32/run39518825366.
- Build results: P1Build37 full Apple PASS. No extra CI build for local names/icons or P2.
- Artifacts produced: Original P1Build37 IPA2583201bytes SHA256afe1995feb5e285c40ade15e266bdf33229d34cfa0b0b323f89945f42b0df12a, archived in folder5/P1Build37 original artifact. Decorated P1 2809938bytes SHA2567e5837bbc83e40ae3f41736b0e00da1e292e546bedc4075aa2192884c74d5654; decorated P2 4124652bytes SHA256824fb84bbc2ddb255cb114077612e6b521922db62126e03ebf7beeceafe65291.

### Next steps

- Next Pikmin 1 task: Folder1/Pikmin1 Build37 Named App and Game Icon IPA; update over current P1 with same signing account, no uninstall. Test exact cardboard crossing at100% captain/Pikmin speed with Better Pathfinding ON, route return, ordinary/global whistle split and speed. Then prefered higher speeds/regressions/save.
- Next Pikmin 2 task: Optional current-app update from folder1/Pikmin2 Build32 Named App and Game Icon IPA; check icon/name/launch and retained content/settings/save. No new P2 gameplay changes.
- GitHub/build task: Commit cosmetic pipeline/journal with skip-ci. No polling or new build needed. Future native build must exercise new resource-copy step; current IPAs already directly verified.
- Anything requiring my involvement: User signs/installs both usual Sideloadly updates and tests. USB needed only for install, then can disconnect. No phone files accessed/written by Codex this turn.

### ChatGPT continuation notes

- Another conversation needs to know: User requested short names Pikmin1/Pikmin2 and game pictures; AI-generated art shown and explicitly accepted. Built-in image_gen used, exact prompts in ios/icons/prompts.json, masters in ios/icons/pikmin1/Artwork.png and pikmin2/Artwork.png, six opaque standard-sizePNG assets each. No extracted proprietary asset uploaded/committed.
- Important source-file locations: ios/app_variant.cmake, Info.plist.in, CMakeLists.txt, verify_bundle_info.py, icons/README.md; prior follower code and combined checklist remain current.
- Relevant logs: work/build37-pikmin1.log; work/build37-verification.json original; work/named-apps-verification.json authoritative decorated packages; output/Named-Game-Apps metadata. Package helper work/package_named_apps.py verifies executable and all non-Info original entries unchanged.
- Unverified fixes: New names/icons on actual iPhone and all Build37 movement runtime behavior. No claim hardware bug resolution. Future build pipeline resource copy not yet Apple compiled; actual local decorated package verified.
- Risks and warnings: Keep bundle IDs/executables/signing account stable. Original P1Build37 archive and Build35 rollback retained. Historical strict verifier expects old names; preserve archived verification records. Cosmetic packages require signing as usual; do not uninstall or erase saves/private content. P2 remains game-code baseline.
- Exact next actions: Install the two clearly named IPAs in folder1, check Home Screen/launch and P1 combined checklist. Report results before co-op work. No further build currently required.

**END PROGRESS REPORT**


---

<!-- P1_COMBINED_FOLLOW_CURRENT -->
# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-21 10:34 EDT

**Overall project status:** User cancelled standalone Build36 and authorized combined narrow-crossing/return-route improvements plus its Recall All/speed changes. Build36 confirmed CANCELLED. Combined source implemented/local checks pass; Build37/run39617967156, sourceabd06b6216f0d09bc13361ddbff693f58640a21f, observedqueued. No new IPA installed or phone-tested; Build35 baseline retained. P2 paused.

### Pikmin 1

- Current objective: One normal-campaign update combining crossing prevention, walking route recovery, separate Recall All and adjustable walking speed.
- What was investigated: User clip9-14s raised crossing; platform collision queries; ActCrowd formation failure/unused route starter; real route graph/findSync flags and movement code; waypoint availability and null/index hazards.
- Root cause or leading hypothesis: Terrain-only guard excluded platforms; wide formation side steering can still pull followers off raised crossings. Ordinary formation never starts its dormant return route. Missing waypoints could be dereferenced; old dynamic route may finish close horizontally on wrong floor; spline segment denominator can be zero. These source issues support targeted improvements but do not prove every clip failure's internal cause.
- Files changed: pc_follow_trail.h new bounded policy; Navi.h/navi.cpp record footsteps/search budget; PikiAI.h/aiCrowd.cpp lane following/stall recovery; Piki.h/piki.cpp optional guarded route setup and separate safe waypoint walker; settings help; command/new follower fixture; experimental workflow; journals/checklists/plan. Earlier recall/speed source remains included.
- Tests and results:63 real-method crossing/route scenarios PASS;82 command/recall/cursor/edge PASS;283 walking/config P1 and283 P2 stock-speed control PASS;58/58/7 campaign variants PASS; MSVC/Clang PASS; diff check PASS. Engine seams are not real map/physics or phone validation. Apple build/IPA/new phone result pending.
- Confirmed working: User Build35 Aim, Soft Assist, charge/whistle and save/reload PASS; global recall functional but now separated in untested new source. Working Build35 IPA backup SHA256 rechecked.
- Remaining issues: Exact crossing, high-speed/crowd collision and performance runtime unverified; routes may not exist; rare clam cutscene and full campaign unverified. No teleport/autosave/networking added.

### Pikmin 2

- Current objective: Preserve working Build32; focus P1 per user.
- What was investigated: No new P2 investigation in this crossing batch.
- Root cause or leading hypothesis: No new failure reported.
- Files changed: No P2 game source.
- Tests and results: Shared speed control still283 PASS; no new P2 build/hardware test.
- Confirmed working: Prior user-positive audio/runtime baseline, not full campaign certification.
- Remaining issues: Stronger P2 readiness tests/select upstream candidates later.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental.
- Starting commit: 8a5a157ef50708d35d7ef3843c11bf6d95fd3351, fetched remote/clean/no divergence before edits.
- Latest source/commit/build: Build37/run39617967156, sourceabd06b6216f0d09bc13361ddbff693f58640a21f, observedqueued.
- Commits created / changes pushed: Combined follower patch pending or dispatched as above; previous472937e5 recall/speed retained. Final documentation commit recorded after push.
- Uncommitted changes: This source/report batch while preparing; commit and record final clean state before ending.
- GitHub Actions run IDs: Build35/run39548476790 SUCCESS; Build36/run39614665805 CANCELLED per user; next Build37/run39617967156, sourceabd06b6216f0d09bc13361ddbff693f58640a21f, observedqueued.
- Build results: New combined Apple/IPA pending; do not call cancelled Build36 successful or deploy it.
- Artifacts produced: No new combined IPA yet. Build35 original-ID verified backup preserved; SHA256 eab4b43ccaeda4de25137e010342592a4e0fc6d2cd328be9b66d365d10e3cc89.

### Next steps

- Next Pikmin 1 task: Complete new Apple build, verify STANDARD original-ID IPA, stage in folder1, then test exact cardboard crossing and return routes at100% captain/Pikmin speed before faster cheats; test retained separate recall/speed.
- Next Pikmin 2 task: Stay paused, no new build.
- GitHub/build task: One combined P1-only run; record source/run once then stop idle polling. User reports finish or requests check.
- Anything requiring my involvement: No phone connection now; later normal Sideloadly update and short phone checklist. Do not uninstall current P1 or recopy private content.

### ChatGPT continuation notes

- Another conversation needs to know: Build36 explicitly cancelled/superseded; user wants one combined update, no isolated recall/speed install. New recovery is optional under existing Better Pathfinding, solo only. No teleport. Normal whistle local, explicit global Recall includes workers by request. Workers/healthy parked squad excluded from autonomous follower recovery.
- Important source-file locations: Navi::pcUpdateFollowTrail/pcTakeFollowerRouteBudget, ActCrowd::pcProtectFormationEdge/pcRecoverFollower, Piki::initRouteTrace recovery option/pcMoveFollowerRoute; ios/PIKMIN1_CROSSING_RECALL_SPEED_TEST.md; ios/PIKMIN1_STRANDED_FOLLOWERS_PLAN.md.
- Relevant logs: work/build36-cancel-result.json; work/p1-follow-test.cpp and compiled fixture; outputs/P1-Build35-Ledge-Review; folder2 copied clip and checkpoint. Next dispatch saved once pushed.
- Unverified fixes: Combined crossing/route and earlier recall/speed source/local validated only; no new Apple/hardware milestone yet.
- Risks and warnings: Same-floor trail, rate limits, waypoint guards and no teleport reduce risk but no guarantee every map/crowd reconnects. Missing/disconnected route may strand followers. Closed waypoint/water rechecked during walking. Route ends/abandons if stalled, captain moved far or8seconds elapsed. Normal carrier spline path unchanged. Keep Build35 rollback and full campaign/finale spoilers constraint.
- Exact next actions: Verify new build/IPA, stage and update over original P1 with same account. Test crossing both directions, wait for walking recovery if a follower remains, locally whistle if it went idle, confirm distant workers unaffected until explicit Recall All. Compare speeds/performance and regressions/save. Only after representative pass advance co-op prototype/shared snapshot plan.

**END PROGRESS REPORT**
<!-- END_P1_COMBINED_FOLLOW_CURRENT -->

<!-- P1_RECALL_SPEED_CURRENT -->
# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-21 10:11 EDT

**Overall project status:** User phone-tested Build35: Aim, Soft Assist, charge whistle and normal save/reload pass. P1 separate Recall All and Pikmin Speed implemented/local verified; Build36/run39614665805, source472937e505eef2a14d00b0c923620dbaee4bd9cd, observed in_progress. New Apple/IPA/runtime validation pending. P2 paused at working baseline.

### Pikmin 1

- Current objective: Separate intentional all-area recall from ordinary whistle, add adjustable Pikmin walking speed, preserve confirmed Build35 behavior.
- What was investigated: User's numbered phone results,32.71s clip (9-14s raised cardboard/ramp crossing), actual formation/route/water rescue/movement/control/settings code.
- Root cause or leading hypothesis: Recall setting globally widened every callPikis; changed to explicit action with false default. Raised crossing still exposes falling/stranded followers; terrain-only guard does not cover dynamic platforms. Dormant follower route starter has no callers; route validity/nearest-waypoint null handling needs work before enabling. Video does not establish exact collider/internal state.
- Files changed: Navi.h/navi.cpp explicit recall/dispatcher; touch pc_touch.cpp/.h appended button/unique key/group-whistle badge/one-shot queue; settings pc_settings.cpp/.h persistent pikiSpeedPct; piki.cpp scales all four walking entry points; command and speed fixtures; experimental P1 workflow; journals/test and stranded-follower plan.
- Tests and results:82 actual command/recall/aim/edge scenarios PASS;283 walking/config scenarios PASS in P1 and283 shared-P2 stock-speed control PASS; MSVC/Clang checks PASS. Existing58+58+7 campaign variants and shared P2menu188/198 PASS. Apple compile/IPA/new phone result pending.
- Confirmed working: User Build35 Aim, Soft Assist, charge/whistle recall and day-end save/reload. All-area recall calls workers successfully. Current video confirms raised-crossing problem persists. Baseline IPA hash-verified in folder5.
- Remaining issues: Rare clam cutscene unverified, stranded followers not fixed, all new changes need phone retest. No teleport policy selected/implemented. Autosave/co-op unchanged and deferred per plan.

### Pikmin 2

- Current objective: Preserve working Build32 while focusing P1.
- What was investigated: Shared menu/touch compatibility and new speed getter's P2 original-speed control only.
- Root cause or leading hypothesis: No new P2 failure reported.
- Files changed: No P2 game-specific source; shared P1 touch/settings keep new controls hidden/neutral in P2.
- Tests and results: P2menu188/198 and stock walking-speed control283 PASS locally; no new P2 build/phone result.
- Confirmed working: Previous user's positive runtime/audio feedback, not full campaign certification.
- Remaining issues: Stronger later P2 readiness tests and selective upstream audit follow-up.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental.
- Starting commit: a7a12cffd437d09c7e13966a6fde054447331bc8; clean, remote fetched, no divergence.
- Latest source/commit/build: Build36/run39614665805, source472937e505eef2a14d00b0c923620dbaee4bd9cd, observed in_progress.
- Commits created / changes pushed: P1-only recall/speed batch; exact source and final documentation commit recorded after push.
- Uncommitted changes: This batch while preparing; commit before ending and record final clean status.
- GitHub Actions run IDs: Build35/run39548476790 SUCCESS, source01d7e7ed. Next: Build36/run39614665805, source472937e505eef2a14d00b0c923620dbaee4bd9cd, observed in_progress.
- Build results: Build35 Apple/IPA PASS and user representative phone tests now PASS. New batch Apple/IPA unverified.
- Artifacts produced: No new IPA yet. Build35 original-ID IPA preserved; SHA256 eab4b43ccaeda4de25137e010342592a4e0fc6d2cd328be9b66d365d10e3cc89.

### Next steps

- Next Pikmin 1 task: Finish P1-only build and verify/stage new IPA; follow short recall/speed checklist. Keep Build35 installed until ready. Continue existing normal save; no reset needed.
- Next Pikmin 2 task: Stay paused, no rebuild required.
- GitHub/build task: Record one dispatch; no idle waiting/polling. Retrieve new result when user reports completion or asks.
- Anything requiring my involvement: No phone connection now. Later user installs/retests; no game assets or settings recopy needed. Await decisions on stuck-follower rescue, no mandatory user technical task.

### ChatGPT continuation notes

- What another conversation needs to know: User's Build35 tests1,2,3,7 passed;4rare clam untested;5recall functional but must be separate button, workers MUST remain included in that explicit action;6terrain following better but raised crossing strand persists;8Pikmin speed requested. Test speed/cheat values were not specified, do not invent them.
- Important source-file locations: Navi::pcUpdateRecallAll/callPikis, pc_touch_take_recall_request, pcTouchRequestRecall/pcTouchAgeRecallRequest, Piki::getSpeed and3setSpeed overloads, pc_settings_get_piki_speed_scale; ios/PIKMIN1_RECALL_SPEED_TEST.md and ios/PIKMIN1_STRANDED_FOLLOWERS_PLAN.md.
- Relevant logs: outputs/P1-Build35-Ledge-Review/contact.jpg/metadata.json; folder2 copied clip; work/p1-runtime-batch-state.json; next build dispatch once saved.
- Unverified fixes: New button/whistle split and speed setting source/local checked only. Stranded follower plan is proposal, no implementation. Full campaign/rare scene unverified.
- Risks and warnings: High movement speeds can worsen ledge collisions; no promise speed fixes navigation. Only living eligible Pikmin called; no revival/pluck/teleport. No online/autosave feature enabled. Preserve Build35 baseline, phone content/settings/saves and spoilers constraint.
- Exact next actions: Verify new Apple build, original P1 identity/STANDARD variant and expected labels; stage and retest local whistle leaving distant workers alone, separate global button including workers, speed150/200/default/persistence. Later test surface-aware narrowing/validated routes before optional stalled-only rescue. Full campaign not certified by sample passes.

**END PROGRESS REPORT**
<!-- END_P1_RECALL_SPEED_CURRENT -->

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-21 01:43 EDT

**Overall project status:** P1 Build35 PASSED; normal-campaign original-ID IPA verified and staged for installation. New phone installation and gameplay still unverified. P2 working baseline unchanged.

### Pikmin 1

- Current objective: Install Build35 over current P1 and test reported fixes on a new Normal/Standard save.
- What was investigated: Successful full job119051975776 log and artifact12322868802; ZIP integrity, Info.plist, Mach-O ARM64/iPhoneOS load commands, linked libraries and feature/variant markers.
- Root cause: Build34's missing KeyConfig.h was corrected in source01d7e7ed; Build35 compiles successfully. Earlier charge/cursor issues and test-preset cutscene hypothesis remain described below in the full handoff.
- Files changed: This result journal and ios/PIKMIN1_NORMAL_CAMPAIGN_FIXES_TEST.md readiness update only. Previous navi.cpp/header and regression correction already pushed.
- Tests and results: CI60 command/aim/recall/edge,27 identity/storage,58+58 preset and7 standard checks PASS; Apple compile PASS; unsigned IPA generated. Original org.opennectar.experimental.pikmin1 identity, STANDARD variant, device ARM64/minimum iOS15 confirmed; synthetic save/event/preset markers absent; Soft Assist/Recall All labels present. Staged copy hash verified.
- Confirmed working: Compiler/package milestones reached; existing phone baseline retained. No claim of new runtime fixes verified yet.
- Remaining issues: Phone test aim/soft/manual lock, whistle during charge, clams/cutscene, Recall All, ledges, assets/settings and save/reload. No new mid-day autosave or online feature.

### Pikmin 2

- Current objective: Preserve working Build32; later stronger gameplay/audio/cave/save tests and selected upstream follow-up.
- What was investigated: No new P2 source/runtime investigation this turn.
- Root cause or leading hypothesis: No new P2 failure reported.
- Files changed: None.
- Tests and results: No P2 job in Build35.
- Confirmed working: Previous user-positive runtime/audio feedback only, full campaign unverified.
- Remaining issues: Broader representative readiness tests and upstream candidates remain queued.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental.
- Starting commit: 395204b5e810400fd602dc2b9d308cc3419b5ab9, clean and remote synchronized.
- Latest build source: 01d7e7ed18df04cb0856ae5cab77b6df62101e39; latest documentation commit recorded after this update.
- Commits created / changes pushed: Result/checklist documentation only, skip-ci commit follows; no extra build needed.
- Uncommitted changes: This result journal/checklist while recording; commit them before ending.
- GitHub Actions run IDs: Build34/run39545404613 FAILED; Build35/run39548476790 SUCCESS, job119051975776.
- Build results: Native P1 Apple compile and packaging passed. P2 not rebuilt.
- Artifacts produced: nectar-pikmin1-experimental/artifact12322868802; P1 IPA 2579504bytes, SHA256 eab4b43ccaeda4de25137e010342592a4e0fc6d2cd328be9b66d365d10e3cc89; executable UUID fcc8e00b-be88-3972-af31-b4dc9e23e249.
- Run: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39548476790

### Next steps

- Next Pikmin 1 task: In Documents/Open Nectar/1 - Install on iPhone, install **Pikmin 1 - Build 35 - Normal Campaign and Controls.ipa** through Sideloadly with the same account, updating existing P1. Do not uninstall. Start a new normal file in an empty slot and follow **Pikmin 1 - START HERE.txt**. Existing settings/private content should remain; original save root returns, Build33 test card retained separately.
- Next Pikmin 2 task: Leave working app as-is. Stronger test follows P1 representative pass/co-op prototype according to agreed order.
- GitHub/build task: No further run or polling required. Await phone feedback.
- Anything requiring my involvement: User installs and tests; USB needed only for installation, then can disconnect. No phone content writes were performed by Codex.

### ChatGPT continuation notes

- Another conversation needs to know: New P1 app is ready, not yet phone-tested. Charge/whistle/cursor, dedicated Aim, optional Soft Assist/Recall All and bounded following-edge work retained; upstream1.0.6 RNG fix included. No finale spoilers. Existing verified rollback backups remain in folder5.
- Important source-file locations: ios/PIKMIN1_NORMAL_CAMPAIGN_FIXES_TEST.md; ios/UPSTREAM_1_0_6_IOS_AUDIT.md; ios/SAVE_AND_COOP_RECOVERY_PLAN.md; navi.cpp/piki.cpp/aiCrowd.cpp; settings/pc_settings.cpp; touch/pc_touch.cpp.
- Relevant logs: work/build35-pikmin1.log; work/build35-result.json; work/build35-verification.json; work/p1-runtime-batch-state.json. Friendly checkpoint and copies are in folder2.
- Unverified fixes: All new gameplay behavior still needs phone evidence; unrecorded clam scene hypothesis has no reproduction. Full campaign remains untested.
- Risks and warnings: Install Build35 normal update, not Build33 synthetic fixture. Normal day-end saving unchanged; unfinished mid-day progress is not autosaved. Soft Assist and Recall All need manual opt-in; saved Manual lock-on remains preserved.
- Exact next actions: User tests normal opening, dedicated Aim and Soft Assist, whistle while charged enemies still alive, clams, Recall All, ledges, day-end save/reload; reports PASS/FAIL/UNTESTED and speed/cheat settings. Then P1 co-op prototype and shared exact-scene persistence/recovery foundation; not prematurely claiming entire game complete.

**END PROGRESS REPORT**


---

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-21 01:15 EDT

**Overall project status:** Build34 failed before packaging; no IPA. Missing header corrected, local checks passed, correction pushed. P1-only normal-campaign Build35 is in_progress at this single dispatch observation. Installed apps and private phone content unchanged.

### Pikmin 1

- Current objective: Compile and phone-test the normal-campaign charge, whistle, cursor, Aim/Soft Assist, Recall All and bounded following-edge batch.
- What was investigated: Complete Build34 job119042338355 log, actual KeyConfig binding declaration, Navi include list and extracted regression fixture.
- Root cause: New whistle-priority expression uses KeyConfig, but navi.cpp lacked KeyConfig.h. The host fixture supplied a stand-in type and missed this dependency.
- Files changed: navi.cpp adds direct header; tests/pikmin1_command_test.py checks the owning source declares that dependency; status/handoff journals updated.
- Tests and results: 60 command/aim/recall/edge scenarios PASS; preset update/separate/standard58/58/7 PASS; Clang checks PASS; dependency negative control rejects Build34 source as expected; diff check PASS. Apple and hardware results pending.
- Confirmed working: Existing phone baseline remains installed; prior phone save evidence and verified rollback backups retained. No new runtime result claimed.
- Remaining issues: Every new gameplay behavior still needs normal-campaign phone retest. Unrecorded clam cutscene consequences not independently reproduced. Autosave/networking remain deferred as agreed.

### Pikmin 2

- Current objective: Preserve user-confirmed working Build32 baseline, later perform stronger readiness test and selected upstream audit follow-up.
- What was investigated: No new P2 investigation in this compiler correction.
- Root cause or leading hypothesis: No new P2 failure reported.
- Files changed: None in P2.
- Tests and results: No new P2 build or phone test.
- Confirmed working: User's previous positive runtime/audio feedback; full campaign not certified.
- Remaining issues: Later check all effects/proximity, caves/transitions, saves and heavier gameplay; upstream candidates remain queued.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental.
- Starting commit: 92e847efd253cfe96fc1138eeb3874288d6cb13f; fetched remote and found no divergence/uncommitted work.
- Latest source commit: 01d7e7ed18df04cb0856ae5cab77b6df62101e39.
- Commits created / changes pushed: 01d7e7ed, header correction, regression guard and journal.
- Uncommitted changes: Only this dispatch documentation update while recording; commit with skip-ci afterward.
- GitHub Actions run IDs: Build34=39545404613, FAILED; Build35=39548476790, in_progress at dispatch.
- Build results: Build34 one compiler error, no IPA. Build35 unknown until next completion check.
- Artifacts produced: No new IPA. Full failed log retained privately at work/build34-pikmin1.log.
- Build35: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39548476790

### Next steps

- Next Pikmin 1 task: Retrieve Build35 result; if successful verify original bundle ID/STANDARD campaign, stage in Documents/Open Nectar/1 - Install on iPhone, then fresh-save test checklist.
- Next Pikmin 2 task: Keep installed working version; no rebuild needed for this P1-only correction.
- GitHub/build task: Stop waiting/polling. User reports completion, or requests a check. Batch any actual remaining compiler errors from full logs.
- Anything requiring my involvement: No phone/USB action now; user can disconnect. No install until a verified IPA is staged.

### ChatGPT continuation notes

- Another conversation needs to know: All prior P1 changes retained, upstream1.0.6 audit recorded, normal saves unchanged. Co-op prototype/shared exact-scene recovery follow successful representative P1 retest, not a claim of full campaign completion.
- Important source-file locations: games/pikmin1/src/plugPikiKando/navi.cpp; tests/pikmin1_command_test.py; ios/PIKMIN1_NORMAL_CAMPAIGN_FIXES_TEST.md; ios/UPSTREAM_1_0_6_IOS_AUDIT.md; ios/SAVE_AND_COOP_RECOVERY_PLAN.md.
- Relevant logs: work/build34-pikmin1.log; work/build34-jobs.json; work/build35-dispatch.json; current recovery state work/p1-runtime-batch-state.json.
- Unverified fixes: New batch is source/local checked only, including this header correction; Apple compile and phone behavior unverified.
- Risks and warnings: Do not install old Build33 synthetic fixture as this new normal-campaign update. Preserve current settings/private content/restore backups. No finale spoilers or automatic networking enablement.
- Exact next actions: Inspect Build35 once reported done, retrieve log/artifact, verify/stage, update journal and give the normal-save checklist.

**END PROGRESS REPORT**


---

## Build 34 compiler correction — 2026-10-21 01:14 EDT

- Build 34 / run 39545404613 / source ff57b9ffc71b9fcd87c444630b2454bcbe4e4110 FAILED. Full job 119042338355 log inspected: one compiler error, navi.cpp:1539 undeclared KeyConfig. No new IPA was produced. Installed P1/P2 remain unchanged.
- Cause: new whistle-priority code used the correct existing binding API but navi.cpp lacked its direct KeyConfig.h include. The extracted host fixture supplied that type and missed this integration dependency.
- Correction: add the direct include; generator now rejects source using KeyConfig without that header. Negative control on Build 34 source fails with the expected dependency message.
- Local verification: 60 command/aim/recall/edge scenarios PASS; preset update/separate/standard 58/58/7 PASS; Clang checks PASS; git diff --check PASS. Apple compilation and phone runtime still pending.
- Next build is P1-only STANDARD normal campaign, original app identity, all previous fixes retained; no P2 change, no synthetic campaign, no autosave/network feature enabled. Verified restore backups remain intact. After dispatch, record run/source and stop waiting; user will report completion.

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-21 00:40 EDT

**Overall project status:** Build33 installed and user tested. Real part/day-end card write and Day3 reload supported by read-only phone event journal. User reports most other behavior consistent, but charge recall, manual cursor release, clam cutscene and large-group ledges need fixes. Coordinated P1 source changes implemented and locally checked; P1-only normal-campaign Build34/run39545404613 dispatched, last observed in_progress; Apple result/IPA/phone tests pending. User explicitly approves updating original P1 on a new normal save, then beginning co-op prototype; normal saving retained now. Exact-scene snapshot system will serve both solo autosaves/co-op later. P2 working user baseline retained.

### Pikmin 1

- Current objective: Ship one P1-only normal-campaign update with the reported fixes and better mobile aiming. Preserve original app identity/settings/private content; no forced unlocked test fixture in this build.
- What was investigated:44s phone video (cursor near16s versus26s),21s P4 aiming reference, live config/touch layout,8 small phone files and persistent events, actual charge/whistle/cursor/clam/tutorial/generator/save code, official upstream1.0.5/1.0.6 and related commits.
- Root causes: pcChargeAt changed child action but left FormationMode, which callPikis excludes. Remaining2.5s charge push could resend recalled followers. Manual/lost/off lock exits failed to consistently restore free cursor state; out-of-range cursor can resist further input. Synthetic test file credited engine but omitted tutorial flags: starting-area discovery matches ANY ship part and plays fixed-position engine scene. This source mechanism supports the user's unrecorded missing-item/warp report, but no recording/runtime retest proves every consequence. Existing Better Pathfinding did not guard wide following slots at terrain drops.
- Source implemented: AttackMode bookkeeping; whistle priority/timer cancellation; suppress ground charge on clam shell/pearl/part (keep aimed throws); uniform legal free-cursor restoration; dedicated Aim button with DPI-normalized drag, no pad action/camera rotation, manual/auto lock override; optional Soft Assist (gentle45% nudge, release on aim-away or walking away); optional Recall All Pikmin through ordinary whistle (off default, solo only, safety guards retained, no teleport); bounded following-slot terrain lookahead under Better Pathfinding; tutorial-flag repair only in synthetic test variant for new/old test files; exact upstream RNG fix/tests. Saved Manual lock choice/current settings not forcibly changed. Aim uses installed lock_on art with its own layout key; no new art transfer needed.
- Important files/functions: Piki::pcChargeAt; Navi::pcReleaseLockOn/pcUpdateLockOn/pcPinCursorToLock/callPikis and cursor input path; ActCrowd::pcProtectFormationEdge; touch/pc_touch.cpp/.h; settings/pc_settings.cpp/.h; pc_solo_test_tutorial.h; GameCoreSection::initStage (test macro only); netplay/pc_sim_rng.h/.cpp/test.cpp; tests/pikmin1_command_test.py and updated preset fixture; experimental workflow [ios-p1-only] selects standard P1 matrix only.
- Tests and results:60 real-code command/aim/recall/cursor/edge scenarios PASS; same pre-fix source fails25 checks (includes new features absent in old build).58 update/58 separate preset-and-loaded-flag checks PASS;7 standard control PASS;27 CMake/bundle/storage checks PASS; Clang parser PASS; upstream RNG tests PASS with a Windows mode seam (actual mode implementation linked by macOS CI). Shared P2 menu fixtures188 iOS/198 desktop PASS. Full Apple compilation, new IPA and phone behavior NOT yet verified.
- Hardware evidence: User saved Day2 and then played Day3. Events show real part collected(count2), day end, card flush, stage2/Day3/count2. This supports real save/load without proving all quantities match. Current settings: fpsMode2(actual60FPS), Manual lock1,charge1,instantWhistle1,betterPathfinding1,naviSpeed200,naviHealth-1,pikiInvincible1. Eight files retrieved with app closed, local hashes verified, then reread from phone unchanged. No phone writes. Phone released; can disconnect.
- Backups: Original pre-experiment Build16+six phone files still intact in folder5. Additional verified Build33 IPA+current eight-file snapshot: C:\Users\chazz\Documents\Open Nectar\5 - Archives\P1 Build 33 and Phone Checkpoint Before Normal Campaign Fixes - 2026-10-21. No proprietary assets or credentials uploaded. No settings restored/reset on phone.
- Remaining issues/limits: New build/runtime pending; soft assist approximates reference, not a port of P4's algorithm. Terrain guard is not a full navigation rewrite and excludes dynamic platforms/explicit swarms/intentional descent. Recall is current-area walking, not an instant rescue. Clam cutscene unrecorded, invincibility already guards swallow/press in source; timing of prior losses versus cheat activation not established. Full campaign/finale unverified; no spoilers or mandatory finale test. Autosave deliberately unchanged per latest user decision.

### Pikmin 2

- Current objective: Preserve working Build32 while P1 is tested. Later perform stronger unlocked readiness test, then P2 co-op.
- What was investigated: Upstream fixes compared to our current native audio, ARAM, adapters and renderer; see UPSTREAM_1_0_6_IOS_AUDIT.md.
- Root cause/leading hypothesis: No new reported failure. Prior zero-gain Pikmin/enemy categories fixed by opening exit cleanup plus earlier scalar/mixer corrections; user reports working. Upstream contains additional distinct fixes and one specifically Android cancellation issue that should not be copied to Darwin.
- Files changed: No P2-specific source. Shared settings/touch change gates new Aim and Soft Assist options to P1; menu regression fixtures pass. No new P2 build requested.
- Tests/results: Build32(run39518825366) both jobs previously PASS. Positive user phone result, not full effects/proximity/cave/campaign certification.
- Remaining: Audited ARAM/audio subframe queue, radar ordering, reused GXCopyTex memory, dialogue IDs/animations and60FPS constants should be considered in a tested P2 batch. Stronger later phone test: all sound categories/proximity, pause/radar, repeated caves/exits, area transfer, day transition/save/reload, heavy squads/combat at60FPS. No finale spoilers.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; branch ios-experimental.
- Starting local/remote:80e3f2b6b1bfae4980b57acdbfa6abcea3a1b1e2, clean before work and origin unchanged when refetched.
- Latest source: ff57b9ffc71b9fcd87c444630b2454bcbe4e4110, committed/pushed; includes upstream RNG commit baa8af2b83b33e36199a6785df652133ce5da65f. Working tree clean after source push. This dispatch checkpoint is a documentation-only skip-ci commit; final local/remote HEAD is recorded in work/p1-runtime-batch-state.json and friendly P1 Runtime Fixes - Checkpoint.json.
- Changes: scoped P1 fixes/tests plus documented upstream RNG backport; no history rewrite/main merge/broad upstream merge. Upstream fetched70c5c938 (tag1.0.6). Working iOS framebuffer/allocator/presentation/settings/content roots preserved. Only one P1-standard build intended; no P2 rebuild.
- Current Actions: Build34/run39545404613/sourceff57b9ff, observedin_progress, P1-only standard. https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39545404613
- Prior Actions: Build33/run39523034602/source8e8138684fd5e36595a89058d090240217fe66ae SUCCESS (synthetic original-ID test app); Build32/run39518825366/source1f04dd8f0117b91c0e5cc6e80cd61384943603e9 BOTH SUCCESS.
- Artifacts: No new normal-campaign IPA yet. Build33 restore SHA256 c04abe4dad2a9ecfada89ddfa53e24aa40c6a272696df1d6dd45bdc32fd7916b. Normal new build must omit synthetic preset/save-solo-test/solo-event markers and keep original identity. Do not install an artifact merely because its filename is P1.

### Next steps

- P1: Build34 is dispatched; inspect Apple result/IPA when user reports completion, stage clearly in folder1 and follow PIKMIN1_NORMAL_CAMPAIGN_FIXES_TEST.md. New Normal/Standard file in empty original slot; old Build33 test save remains separate. First test at100% speed then repeat at user's200% choice. Check fresh intro/ordinary skip, textures/layout, Aim/Soft Assist/manual release, charge-whistle before enemy dies, clams with throws, recall, terrain edges and real day-end save/reload.
- P2: Keep working build. After P1 readiness/prototype work, adopt justified upstream batch and perform stronger area/cave/audio/save stress sample before co-op.
- Build: Source/run recorded; stop consuming usage while CI runs. User reports completion; no idle polling. The next IPA must be verified as original-ID STANDARD campaign with no synthetic preset/test-card/event markers before staging.
- User involvement: None during CI. Phone can disconnect. Install and runtime checks required after IPA verification; no need to leave game running.

### ChatGPT continuation notes

- Current user order supersedes earlier autosave discussion: current fixes + normal saves/fresh-save retest -> P1 co-op prototype -> shared exact-scene snapshot system for solo persistence/co-op recovery -> intensive P2 readiness -> P2 co-op. Ship-return checkpoint briefly accepted but exact-scene preference superseded it. Do not silently substitute day-end autosave or claim mid-day protection exists.
- SAVE_AND_COOP_RECOVERY_PLAN.md records actual save-state gaps and primary-source research (Mindustry host snapshots; Factorio joining/lockstep complexity). Existing8-byte Gekko frame handles are NOT world saves. PC_ONLINE_ENABLED0 / iOS NECTAR_ONLINE OFF remain. No online multiplayer enabled or external server deployed by this patch.
- Evidence: workspace work/p1-phone-feedback-latest.json and private snapshot folder; bounded p1-solo-test-events.txt plus config/touch/save files. Phone video in Downloads (44s) and P4 reference in Videos/NVIDIA/Desktop (21s). Exact timestamp/frame sheets under outputs/P1-Build33-Phone-Review and outputs/Pikmin4-Aiming-Reference. Videos/assets not committed.
- Local scripts: work/check_p1_commands.cmd, check_p1_command_clang.cmd, check_p1_before.cmd, check_p1_rng.cmd; actual fixtures generated under work. Windows RNG mode seam only replaces mode toggling for local compiler compatibility; CI runs real mode source.
- Important caveat: returning standard variant uses Documents/pikmin1/save again. Test fixture card remains Documents/pikmin1/save-solo-test. Startup keeps existing config/art/Load/models; do not replace or recopy content without need. Use same original account/bundle ID for update/rollback; never uninstall working apps.
- Report untested items honestly. No full-campaign certification from host fixtures or a short sample. Keep final boss/ending deferred and unspoiled. Any future experimental snapshot must preserve original normal card, validate IDs/relationships and atomically rotate checksummed files before exposing restore UI.

**END PROGRESS REPORT**


## Older checkpoint history (superseded where different)

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-20 21:15 EDT

**Overall project status:** P1-only Build33 PASSED. Verified current-app update IPA staged with an exact phone checklist; installation and runtime tests pending. Pre-update working IPA/settings/layout/save backup remains intact. P2 Build32 has positive user phone feedback. No online co-op code implemented. Do not rebuild or poll CI without a new reason.

### Pikmin 1

- Current objective: Install the authorized existing-app solo-readiness experiment, preserving settings/assets; run the short spoiler-free systems sample.
- What was investigated: Build33 full job log, source identity, artifact ZIP, plist/executable, Mach-O CPU/platform/load commands, original bundle identity, compiled test-save/log/no-finale markers, and rollback IPA hash.
- Root cause or leading hypothesis: Previous separate-app install hit the free-profile three-app cap. User authorized updating the original P1 after verified backup. Build33 retains its original identity and uses existing settings/assets with separate test cards.
- Files changed in source commit: ios/app_variant.cmake, ios/CMakeLists.txt, ios/verify_bundle_info.py, ios/ios_storage.mm, ios/pikmin1_solo_app_policy.h, pc_solo_test_game.h, cardSelect.cpp fresh-file hooks, settings/pc_settings.cpp new-game label, tests and experimental workflow. This result checkpoint changes only documentation.
- Tests and results: Apple ARM64 compile/link/package SUCCESS. Runner: 27 bundle/storage checks,27 identity/settings policy,47 update preset/profile,47 separate preset,7 standard control,169 profile,19 bridge,30 performance and mod/archive checks PASS. Prior local tests also included actual backed-up settings/signed identity. Downloaded IPA ZIP/plist/device/load-command/marker checks PASS; staged copy SHA256 matched. This is not phone runtime proof.
- Verified IPA: C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\Pikmin 1 - Build 33 - UPDATE Current App - Solo Test.ipa
- IPA SHA256: c04abe4dad2a9ecfada89ddfa53e24aa40c6a272696df1d6dd45bdc32fd7916b; bytes 2578066; executable UUID be51571f-c725-3ede-a13e-bbcbd74f9a87; ARM64 iPhoneOS15+, unsigned for Sideloadly. Bundle org.opennectar.experimental.pikmin1; executable Nectar-pikmin1; variant solo-update.
- Implemented behavior: Documents/pikmin1 retains assets/art/Load/config/touch layout. Test cards use save-solo-test; original save is retained. Startup leaves nonempty current config unchanged. Fresh test slots: Day2, Main Engine credited, three booted Onions/100 leaf per color, four earlier areas open. All update slots disable finale fixture. Saved loads must not refill inventory/reset progress.
- Confirmed working: Older P1 gameplay/audio/readable menus/camera/60FPS and GPI textures are the phone baseline. New Build33 Apple build and IPA checks passed. Installation, settings/content retention and test-card gameplay/save behavior are NOT yet phone verified.
- Backup: C:\Users\chazz\Documents\Open Nectar\5 - Archives\P1 Restore Point Before In-App Test - 2026-10-20 203541. Saved Build16 working IPA SHA256 02041fc3c82b757b6a0cfc62592bf855c8b6e4deca63ca4ba64eb0704747bec6 rechecked intact now; six current phone settings/layout/save files previously copied/hash checked and reread for consistency. No phone writes in this session. Large assets remain in app, not duplicated. Restore IPA is saved unsigned working build, not extracted signed binary; same-account signing needed.
- Remaining issues/coverage: User must install/test Build33. Full campaign, normal unlock/tutorial progression and finale remain unverified. Optional invincibility bypasses damage/death coverage. No finale test required and no final-boss spoilers.

### Pikmin 2

- Current objective: Preserve working Build32; continue ordinary play and report concrete regressions.
- What was investigated: No new P2 code or logs this result checkpoint.
- Root cause or leading hypothesis: Prior native scalar-layout/mixer fixes restored ambience; opening cutscene could leave Pikmin/enemy categories muted. Native opening-exit cleanup shipped in Build32 (90785c36, included in 1f04dd8f).
- Files changed: None now.
- Tests and results: Build32 Apple build/IPA and36 cleanup/12 audit/48 scalar/28 route tests passed. User now says 'P2 is working now' in audio-test context. No fresh phone report or individual sound checklist collected.
- Confirmed working: Positive Build32 phone runtime/audio feedback; Build31 previously confirmed winter ambience and clearer HUD. Restoration of specific Pikmin/enemy effects is inferred from context, not separately itemized evidence.
- Remaining coverage: Other colors/effects, ship/Louie proximity, caves/area transitions and full campaign. No immediate USB session or rebuild required.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; branch ios-experimental.
- Starting/latest verified local and remote before this documentation checkpoint: 604808c042fb6770eca98d7d6b911a6d8b84dec1, clean and fetched.
- P1 source commit: 8e8138684fd5e36595a89058d090240217fe66ae. This is the exact source in Build33; later skip-ci journal commits do not change its binary.
- Commits created/changes pushed: Current result/checklist documentation committed with [skip ci]; exact final documentation HEAD is in friendly 'Pikmin 1 - Current App Update Checkpoint.json'. No new source modification or build needed.
- Uncommitted changes: Only this documentation checkpoint during preparation; verify clean after commit.
- GitHub Actions: Build33/run39523034602, P1 job118971161411 SUCCESS, artifact12311259642 nectar-pikmin1-solo-update. https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39523034602
- Prior Build32/run39518825366 BOTH SUCCESS, source1f04dd8f0117b91c0e5cc6e80cd61384943603e9; P2 job118957403187/artifact12309879326. P1 Build32 is the older separate-app variant and must NOT be used for the current-app update.
- Artifacts: Build33 verified update staged as above. P2 Build32 staged in folder1/Pikmin 2 - Build 32 - Pikmin and Enemy Audio Fix.ipa (SHA256 db79c3587cb2e5bbf5acfd2f355021d490acd5d49a2369143f3aa2a004003c8a). No proprietary assets included/uploaded.

### Next steps

- Next Pikmin 1 task/user involvement: Follow folder1 'Pikmin 1 - Build 33 - TEST THIS.md': install using same Sideloadly account/normal ID over current P1, never uninstall. Check settings/packs; NEW slot A Normal/Standard; movement/camera/menus; exact Onion accounting; real enemy/carry/part; large squad; pause/background; real sunset save and close/reload. Visit four earlier areas across days. Report pass/fail/untested; no finale needed.
- Next Pikmin 2 task: Normal play on working Build32; capture a specific new symptom if any.
- GitHub/build task: None pending. No idle polling, no redundant CI. On next turn read phone results before proposing changes.
- Phone: Can disconnect after installing; no need to leave game running/USB connected during ordinary testing. Request connection only for a concrete log/data task, then explicitly release it.

### ChatGPT continuation notes

- User explicitly superseded separate-app-only restriction after app cap; original P1 update now authorized AFTER rollback. Preserve settings and installed private content. No account/security changes, force push, main merge or app deletion.
- Save roots: original Documents/pikmin1/save; experiment Documents/pikmin1/save-solo-test. Never present missing old card slots as data loss without checking these separate roots. Presets execute only on NEW files. No timed mid-day autosave implemented; backgrounding is not a save guarantee.
- Settings baseline in private backup: enhanced/HUD enabled, renderScale1, fpsMode2 (runs60 on phone), health100, invincibility0, unlockZones0, allOnions0, GPI active. Values intentionally untouched for settings preservation; user dropped120FPS pursuit. Don't overwrite config for new defaults.
- Important source: ios/pikmin1_solo_app_policy.h signed-ID policy supports exact base, valid team suffix and matching wrapper; original variant rejects separate identity. ios_storage.mm gates storage and assigns card root. pc_solo_test_game.h seeds only new-file fixture. pc_solo_test_log.h writes bounded64KiB p1-solo-test-events.txt, distinguishing preset setup from actual events.
- Relevant logs: workspace work/build33-result.json, work/build33-jobs.json, work/build33-artifacts.json, work/build33-p1-job.log, work/build33-verification.json. Extracted IPA: outputs/Build33-Pikmin1-Current-App-Update. Friendly folder2 has successful log/verification. Private backup metadata work/p1-before-update-backup.json; no private contents in GitHub.
- Unverified fixes: Build33 in-place install/retention/new card/save/reload/runtime. Never call sampled/full campaign complete from fixture/CI results. Finale remains deferred by user choice; do not spoil it.
- Co-op: Notes in ios/ONLINE_COOP_DESIGN_NOTES.md. Together-only host-owned shared campaign; independent screens/cameras/squads and individual allowances; shared Onion counts; forced group area/cave transitions acceptable; mainly health scaling. Networking implementation not started. Assess test feedback before prototype work.
- Exact resumption: Read current checkpoint/checklist and user results. If installation fails, inspect exact Sideloadly error; don't remove working apps. If runtime regresses, reproduce narrow step and collect bounded event/crash logs when connected. If settings changed, compare exact backed-up config/touch hashes before targeted restore. Use saved Build16 same-identity IPA for rollback if needed. No new build just for reporting.

**END PROGRESS REPORT**


## Prior checkpoint history (superseded where different)

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

## Earlier spoiler preference (still applies; newer update authorization in report)

The user does not want the final boss identified, shown or required for this
readiness experiment. No final-boss/ending test is required before beginning the
separate co-op proof of concept. Leave that coverage explicitly deferred until
normal play reaches it. Use only a new slot A/C and familiar earlier areas;
avoid the finale preset in slot B and the final area. Do not route the user into
late encounters or spoil them in instructions/screenshots. Earlier requests for
mandatory finale testing below are superseded by this preference.

Existing advanced settings include Olimar Health = Infinite and Invincible
Pikmin = On. These can make the exploration tests easier. Normal health/death,
hazard consequences and real progression remain unverified where cheats bypass
them. Do not treat those omissions as blockers to an exploratory co-op prototype.
The current Build32 source is unchanged; the unused finale preset remains in the
test app but is optional and must not be selected for this user's short test.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-20 20:49 EDT

**Overall project status:** Both Build32 jobs passed and IPAs were verified/staged. User now reports P2 working on phone; full campaign remains unverified. Separate P1 test installation was rejected by the phone's free-profile three-app limit (P1/P2/KartPad already installed). The user now explicitly authorizes putting the solo-readiness experiment into the current P1 app after a rollback backup, prioritizing current settings. This overrides the earlier separate-app requirement for this experiment. No purchase, KartPad removal, account change or LiveContainer installation was performed. Verified backup completed BEFORE source modification; new P1-only update source is implemented and locally checked, Apple build pending. No co-op networking code started.

### Pikmin 1

- Current objective: Update current P1 with the spoiler-free solo systems test, preserving graphics/control settings and installed private content. Avoid needing a fourth sideload slot.
- What was investigated: Saved working IPA, connected app identity, current phone config/touch/save files, fresh-file versus loaded-file paths, storage/signing guards and area unlock state.
- Root cause or leading hypothesis: Installation blocker is the free developer-profile app cap. Build32's separate-app identity and strict runtime identity check prevent simply renaming its IPA into a safe original-app update. New native compilation is necessary for the changed identity/storage behavior.
- Backup: C:\Users\chazz\Documents\Open Nectar\5 - Archives\P1 Restore Point Before In-App Test - 2026-10-20 203541. Saved last documented phone-confirmed working Build16 IPA, SHA256 02041fc3c82b757b6a0cfc62592bf855c8b6e4deca63ca4ba64eb0704747bec6. This is the saved unsigned working IPA, not an extraction of the installed signed binary; it needs normal signing for rollback. Six current phone files (settings, touch layout, save/card metadata and related small files) copied and SHA256-verified locally, then reread from phone to confirm a consistent unchanged snapshot. No phone files were written. Large assets/texture/model content remain in the current app container and were not duplicated.
- Files changed: ios/app_variant.cmake, ios/CMakeLists.txt, ios/verify_bundle_info.py, ios/ios_storage.mm; new ios/pikmin1_solo_app_policy.h; pc_solo_test_game.h; fresh-file hooks in cardSelect.cpp; new-game header in settings/pc_settings.cpp; packaging/preset/policy tests; experimental workflow.
- Implemented behavior: Variant solo-update retains org.opennectar.experimental.pikmin1, Nectar-pikmin1 and Open Nectar Pikmin1 display identity. It reuses Documents/pikmin1 assets/art/Load/settings, with cards explicitly routed to Documents/pikmin1/save-solo-test. Existing normal save remains in save. Existing nonempty settings remain byte-for-byte unchanged by startup profile; touch-layout code/path unchanged.
- Signing issue accounted for: Installed CFBundleIdentifier has a Sideloadly team suffix, whereas application-identifier error text also shows a team prefix. New policy accepts the exact unsigned base, valid ten-character team suffix, or matching team wrapper; rejects the other variant's identity and malformed IDs. The exact current phone identifier passes the compiled policy test. Do not print account/team identifiers into public docs.
- Spoiler protection: All fresh update slots use the Day2/engine/all-Onions100-per-color area fixture; the finale preset is disabled in solo-update. Four earlier areas open in disposable campaign state without changing unlockZones/allOnions config keys. The final area is not opened by this update preset. Final-boss/ending tests stay deferred; no spoilers.
- Tests and results: 27 CMake/bundle/configure/storage checks PASS; 29 identity/storage/profile checks including actual backed-up phone settings PASS; actual installed signed-ID control PASS; 47 update preset/profile checks PASS, separate-app47 and standard control7 PASS; Clang parser PASS. These do not establish new app runtime/save behavior. Apple SDK/full iOS compile pending.
- Confirmed working: Prior P1 gameplay/audio/readable menu/camera/60FPS and active GPI textures remain the hardware baseline. Backup/config consistency verified now. Original phone app and data have not been updated yet.
- Remaining issues: New Apple build/IPA, in-place installation, verify settings/content retained on phone, short familiar-area combat/carry/Onion/day-end/save-reload checks. Normal progression/hazards bypassed by presets/optional invincibility remain unverified. No full story or co-op validation.

### Pikmin 2

- Current objective: Preserve the positive Build32 phone result; do not rebuild unchanged P2 for this P1 packaging change.
- What was investigated: No new P2 source/audio investigation in this batch.
- Root cause or leading hypothesis: Build31 restored snow/winter ambience, but all observed Pikmin/enemy gains were zero; opening-cutscene category mute cleanup shipped in verified Build32. User now reports "P2 is working now": positive runtime/audio feedback in this context, without itemized sound coverage.
- Files changed: None in this batch.
- Tests and results: Build32 Apple compile/link/package,36 cleanup/12 audit/48 scalar/28 routes passed previously. Verified P2 IPA remains in folder1. New hardware feedback: user reports "P2 is working now". No new diagnostic report collected.
- Confirmed working: Build31 user-confirmed winter ambience and clearer HUD; Build32 now has positive user phone feedback ("P2 is working now"). Restoration of Pikmin/enemy audio is inferred from context, not an itemized confirmation of every sound or the full campaign.
- Remaining coverage: Individual Pikmin/enemy effects, ship/Louie proximity, other colors/areas/caves and long campaign stability were not separately confirmed. These are unverified checks, not newly reported failures.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: d9ede6a5882d1a22dd912247998ef943dc857ca4, local/remote clean and fetched before edits.
- Latest source commit: 8e8138684fd5e36595a89058d090240217fe66ae, committed and pushed. This dispatch report accompanies a skip-ci documentation checkpoint.
- Commits created: 8e8138684fd5e36595a89058d090240217fe66ae (P1 test update, signed-ID/storage policy and regression checks).
- Changes pushed: Scoped P1 solo-update source, policy/tests, workflow and journals. New [ios-p1-update] marker selects P1-only matrix/solo-update variant; regular P2 is excluded from this run.
- Uncommitted changes: No source changes; dispatch documentation checkpoint being saved with skip ci.
- GitHub Actions run IDs: Build32/run39518825366/source1f04dd8f0117b91c0e5cc6e80cd61384943603e9 BOTH SUCCESS. New P1-only Build33/run39523034602, source 8e8138684fd5e36595a89058d090240217fe66ae, observed in_progress: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39523034602
- Build results: New source locally checked, full Apple build pending. Build32 separate test compile success does not validate the changed update identity/storage path.
- Artifacts produced: No new update IPA yet. Old Build32 P1 solo-test IPA must NOT be used for this in-place update. Working Build16 restore IPA and exact settings/layout backup are ready in folder5.

### Next steps

- Next Pikmin 1 task: P1-only Build33 dispatched. After success inspect IPA original bundle/executable identity, iPhone target and update/test-save marker; stage clearly in folder1. Install over current P1 with same Apple account/identity, never delete app. Verify current settings/Load content, new test card and slot fixtures. Retain rollback package.
- Next Pikmin 2 task: Continue normal play on working Build32. If another audio issue appears, identify the specific effect/location and retrieve its report. Other colors, ship/Louie distance, caves and campaign completion remain unverified; no immediate USB collection or rebuild required.
- GitHub/build task: Build33/run39523034602 dispatched with source8e813868. Stop consuming usage while GitHub runs; user reports completion. No idle polling or redundant P2 run.
- Anything requiring my involvement: None during build. P1 backup collection finished; user told they can close P1/disconnect. New IPA installation and short phone test are needed after successful build. Explicitly release phone after any future collection.

### ChatGPT continuation notes

- User changed the isolation constraint: current P1 update is now authorized after rollback backup. This is the solo-readiness experiment, not implemented online co-op. Original long-term own-screen/shared-campaign design remains in ONLINE_COOP_DESIGN_NOTES.md.
- Settings preservation is a priority; current backup contains the exact live config, touch layout and saves. Do not replace it with fresh default profiles or copy old settings over it without need. Existing fpsMode value was left untouched as requested; no settings write occurred during backup/development.
- Important source: pikmin1_solo_app_policy.h defines expected IDs/data roots; ios_storage.mm uses its signed-ID policy and separate save-solo-test card root. cardSelect fresh-file-only hooks supply inventory/earlier-area unlocks without rewriting settings. Update variant disables finale fixture.
- Relevant logs: workspace work/p1-before-update-backup.json (private actual ID and config); folder5 BACKUP MANIFEST.json/HOW TO RESTORE.txt. Prior Build32 logs/verification in work/build32-*. No private backup contents uploaded to GitHub.
- Unverified fixes: New full Apple compilation, in-place installation behavior, actual settings/content retention and test save/reload on phone. No claim of campaign completeness from host fixture tests.
- Risks and warnings: Same Apple account and original bundle identity required for update/rollback. Keep saved Build16 IPA and phone settings backup. Never delete current P1 or touch KartPad/P2 to install this update. Preserve working SDL framebuffer/native allocator fixes. Final boss/ending remain untested by choice.
- Exact next actions: Build33 is dispatched and source/run recorded. Wait for user completion report. Then verify/stage IPA and guide in-place signing. Read back settings/layout hashes before/after install with P1 closed where practical; restore verified backup only if an actual change needs rollback. User performs spoiler-free systems checks using new test card.

**END PROGRESS REPORT**


## Earlier history (superseded where the current report differs)

CURRENT - 2026-10-20 14:31 EDT: Build29 P2-only PASSED; verified enhancements IPA ready in folder1.
Source7f7d0783/run39470849443. New phone installation/runtime test pending.
P1 textures confirmed354 replacements/0 failures; P1 unchanged. Future co-op
choices recorded (notes only, implementation still last). Older pending headers historical.

CURRENT - 2026-10-20 14:07 EDT: P1 GPI HD textures CONFIRMED loading on phone:
354 successful replacements,0 failed;455 originals not in pack. No P1 changes needed.
P2 Build29 result still pending at last observation; no idle polling.
Older texture-unconfirmed notes below are superseded by this screenshot.

CURRENT - 2026-10-20 14:00 EDT: Build29 P2-only DISPATCHED, run39470849443.
Source7f7d0783e8b42870a8b6bbb1954199fbe9ffc6bb; observedin_progress.
Build28 FAILED at import API call; corrected, new19-check real API fixture PASS.
Build29 result/link/IPA/phone tests pending; Build27 working baseline. P1 untouched.
No idle polling. Next inspect Build29 when user reports done. Older entries historical.

CURRENT - 2026-10-20 13:59 EDT: Build28 FAILED (2 compiler errors,1 incorrect API call).
Correction and19-check real menu/API regression locally PASS; retry not dispatched yet.
Build27 remains limited positive phone baseline. P1 untouched; texture replacements
not confirmed. New entries supersede older pending-build headers below.

CURRENT - 2026-10-20 13:42 EDT: Build28 P2-only DISPATCHED, run39468391460.
Source386771cabe6366b0788091f4d6d63f9ef6850c67; observed in_progress.
Local checks PASS; new Apple result/IPA/phone tests pending. Build27 user reports
no crashes so far (limited test). P1 app unchanged; GPI activation unverified.
No idle polling; next action inspect Build28 when user reports completion.

CURRENT - 2026-10-20 13:41 EDT: P2 enhancements implemented; local checks PASS.
Apple build/IPA/new-profile phone tests pending. Build27 user reports no crashes
so far (limited test). P1 GPI texture pack installed/listed but inactive in screenshot;
activation unverified. P1 working app untouched; keep60FPS. New entries supersede
older current-status headers; older entries below are historical.

CURRENT - 2026-10-20 09:57 EDT: Build27 P2-only PASSED; verified IPA in folder1.
P2 phone crash/control retest pending. P1 models INSTALLED, runtime pending;
saves/settings unchanged. HD environment textures NOT installed.

CURRENT CONTENT UPDATE - 2026-10-20 09:52 EDT: P1 character bundle INSTALLED;
20 files hash-verified, saves/settings unchanged. P1 model runtime test pending.
HD environment textures NOT installed. P2 Build27 pending at last dispatch.

CURRENT - 2026-10-20 09:38 EDT: Build26 PHONE REGRESSIONS: menu gear/A hidden;
captain-preview/Metal heap crashes. P2-only batch locally checked; Build27/run39432157516 (in_progress at dispatch).
New Apple build and phone results pending. Build24 backup; P1 untouched.

CURRENT - 2026-10-20 09:37 EDT: Build26 PHONE REGRESSIONS: menu gear/A hidden;
captain-preview/Metal heap crashes. P2-only batch locally checked; not dispatched.
New Apple build and phone results pending. Build24 backup; P1 untouched.

CURRENT - 2026-10-20 09:19 EDT: Build26 P2-only PASSED; verified IPA ready in folder1.
Menu clarity/input on phone pending. Build24 opens; P1 untouched.

CURRENT CHECKPOINT - 2026-10-20 08:43 EDT: Build25 failed only the new test fixture;
correction locally verified. P2-only Build26 run39424440094 dispatched; result pending.
Build24 opens on phone; menu candidate remains unverified. P1 untouched.

CURRENT CHECKPOINT - 2026-10-20 08:42 EDT: Build25 failed only the new test fixture;
correction locally verified. P2-only replacement build not dispatched yet.
Build24 opens on phone; menu candidate remains unverified. P1 untouched.

LATEST BUILD: P2-only Build25 at 3013d4c2;
result/IPA/menu phone test pending. Build24 opens; P1 untouched.

CURRENT - 2026-10-20 08:33 EDT: user resumed. Build24 P2 startup/menu opening CONFIRMED.
P2 clarity/options-touch candidate implemented; local tests PASS, next Apple
build and phone checks pending. P1 untouched. Prior paused notes are historical.

# PAUSED AT USER REQUEST - 2026-10-20 01:13 EDT

The user is shutting the PC down and explicitly asked to pause until morning.
Do not resume source edits/builds/phone operations until asked to continue.
No source edits, commits, pushes, new builds or phone operations occurred in
this menu-investigation turn. Only repository/source/history reads were done.
Repository branch ios-experimental; local/fetched remote HEAD both
00bd0db831ce09d37c3da94e00ec5596e2256563, working tree clean at investigation
start. Build24 source05e33f1c0e55dc11ecb6d413a8393bf73faeb2ce/run39371370836
PASSED, and the user now CONFIRMS P2 OPENS on the phone and reaches menus.
This supersedes earlier 'new phone startup unverified' notes. Do not infer
verified audio/gameplay/full-game stability from this menu/startup observation.
Preserve Build24 allocator/thread ownership and SDL UIKit framebuffer fixes.
P1 app, data, source and its working menu/camera behavior remain untouched.

Two newly reported P2 issues (screenshots attached in chat):
1. Advanced Open Nectar menu is small/blurry, resembling P1's earlier problem.
2. Original game Options/exit-confirmation screen accepts only bottom-left X/
   Back. User clarified main-screen taps and Throw/A work; failure is specific
   to that menu/dialog. Do NOT diagnose all touchscreen input as broken.

Read-only findings before pause:
- Working P1 pc_window.cpp has SDL_WINDOW_ALLOW_HIGHDPI on iPhone; P2 lacks it.
- P1 pc_gfx.cpp latches ios_native_settings_frame and renders menus at native
  drawable resolution independently of gameplay render scale/resolution. P2
  lacks this path; its screenshot shows a low internal scene scale/resolution.
- P1 pc_settings.cpp enables the 400-high mobile canvas for iOS and Android,
  with iPhone landscape margins, matching viewport/scissor and inverse tap map.
  P2 still restricts those branches to Android. P2's shim begin_frame also sets
  virtual dimensions only on Android, so include it when adapting the solution.
- P2 TOption::doUpdateStateWait has controller input but no touch-pane handling.
  Its rows are mButtonPaneList[7]; save is row6/A; other settings use left/right.
- The pictured confirmation uses ObjWorldMapInfoWindow0 -> ObjSMenuPauseVS.
  ObjSMenuPauseVS::menu ALREADY claims game-menu touch, calls
  MenuMgr::pcTouchTappedOption and treats tapping selected option as A.
  Investigate why that existing path fails before adding duplicate handlers.
- pc_touch.cpp only allows Back plus buttons requested by visible help icons
  while a game menu owns input. Its separate MENU_CONFIRM is currently allowed
  only for port menus. Check whether this original dialog exposes a usable A
  control and whether pane tracking/projection hits its visible text correctly.
  The main-screen working controls should remain unchanged.

Exact resumption steps:
1. User says resume; read this checkpoint and newest journal; verify branch/
   status/fetch again and preserve any changes made after this pause.
2. Compare actual working P1 menu/high-DPI/render-budget code with P2. Adapt
   P2 paths, including its DGX shim, mobile layout and inverse taps; preserve
   gameplay pixel budget, startup fixes and P1 source/data.
3. Inspect TOption and inherited confirmation input/tracked panes. Implement a
   targeted original-options fix preserving main-screen/gameplay controls and
   keeping save/discard actions explicit. Do not auto-save or auto-discard.
4. Add meaningful layout/Retina/touch-state checks; build P2 only after local
   checks and review. No fixes are implemented yet and no Build25 was triggered.
5. Record exact commit/run; do not idle-poll Actions. When result known, verify
   IPA, put in folder1 with short test guide. Phone tests: readable full-width
   advanced menu, taps/scroll alignment, original options rows, confirmation
   Continue/Don't Save, Back, plus startup/gameplay/audio/control regression.
6. Keep P1 untouched. Optional packs and online with Raye remain later; online
   LAST. User is asleep; no immediate test request/audio alert is needed.

Important source locations:
games/pikmin1/pc_port/pc_window.cpp andgl/pc_gfx.cpp (working reference)
games/pikmin1/pc_port/settings/pc_settings.cpp (working mobile layout)
games/pikmin2/pc_port/pc_window.cpp andgl/pc_gfx.cpp
games/pikmin2/pc_port/settings/pc_settings.cpp andpc_settings_p2_shim.cpp
games/pikmin2/pc_port/touch/pc_touch.cpp andpc_touch.h
games/pikmin2/pikmin2-decomp/src/plugProjectEbisawaU/ebiScreenOption.cpp
games/pikmin2/pikmin2-decomp/include/ebi/Screen/TOption.h
games/pikmin2/pikmin2-decomp/src/plugProjectOgawaU/ogObjSMenuPauseVs.cpp
games/pikmin2/pikmin2-decomp/src/plugProjectOgawaU/ogObjWorldMapInfoWindow0.cpp
games/pikmin2/pikmin2-decomp/src/plugProjectOgawaU/ogMenuMgr.cpp
games/pikmin2/pikmin2-decomp/src/JSystem/J2D/J2DPane.cpp
Session work/prepare_pikmin1_menu_candidate.ps1 records the earlier P1 patch;
read it as historical evidence, do not blindly execute it against current code.

END PAUSE CHECKPOINT

LATEST CHECKPOINT - 2026-10-20 01:03 EDT: P2 Build24 SUCCESS; target ARM64 allocator
check and actual binary16-byte alignment verified. New IPA ready in folder1.
NEW phone installation/startup/audio retest pending. P1 working and untouched.
Earlier Build23 phone startup failed; read newest journal entry for current state.

CURRENT BUILD: P2-only Build24 dispatched at 05e33f1c;
result and phone retest pending. P1 untouched.

LATEST CHECKPOINT - 2026-10-20 00:46 EDT: P2 Build23 phone startup FAILED on AudioQueue
thread. Matched real crash UUID; binary new alignment is8bytes. 16-byte floor +
native/game thread allocation ownership batch implemented; local tests passed.
Next P2-only Apple build pending. P1 working/untouched. Older pending/success
checkpoints describe compilation or historical results, not a working P2 app.

LATEST CHECKPOINT - 2026-10-20 00:34 EDT: P2 Build23 SUCCESS; startup candidate IPA ready
in folder1. Source609a45b1/run39369282124. New phone installation/startup retest
PENDING. Update P2 only; preserve data/assets/art. P1 working and untouched.
Read the newest journal entry; earlier build-pending checkpoints are historical.

LATEST BUILD CHECKPOINT: P2-only Build23 dispatched at 609a45b1;
Apple result/IPA/phone retest pending. P1 untouched.

CURRENT CHECKPOINT - October 20, 2026: P2 Build22 installs but crashes at first
draw. Real phone crash reports identify an alignment fault; allocator + renderer
scope candidate implemented and local tests passed. Next P2-only Apple build and
phone retest pending. P1 working and untouched. Read newest journal entry below;
historical pending/paused instructions are superseded by this checkpoint.

# Open Nectar iOS continuation

LATEST USER PRIORITY: keep P1 at60FPS;120FPS/ProMotion opt-in canceled and removed.
Install/prepare ALL supported optional graphics/character content from upstream;
preserve alternatives,phone saves,andworkingP1. Content preparation pending.
Build17 P1passed/P2failed; fullkeep-goinglogexposes102diagnostics. Broad native-address
batch spansroughly55source/header/buildfiles andnewactual-codehostfixture;local
checks passed,successor Apple build pending. ReadLATESTstatusentries for exactstate.

Current policy (October19 evening): user explicitly requests broader related P2
compatibility batches. Check shared headers and related container implementations,
test together, then one coordinated build. P2 now uses Makefiles + make -k to
collect independent compiler errors; P1 keeps Xcode. Preserve actual failure status.
Read the LATEST status-journal entries before historical paused checkpoints below.
Build16: P1 passed/new HUD IPA ready, P2 failed due shared nullptr macro; batch
correction and CPlate/Stickers handles implemented, successor Apple build pending.
Stop idle polling during Actions runs; user reports completion. Test IPAs always
go in Documents/Open Nectar/1 - Install on iPhone with short instructions and audio.

Read `ios/OPEN_NECTAR_IOS_STATUS.md` first. It records both games, preservation rules, verified baseline, investigations, validation boundaries, and exact next actions.

Before edits: verify origin, branch, `git status`, fetch, compare HEAD and origin/ios-experimental, and preserve unexpected changes. Never run downloaded patch installers blindly.

Priorities: preserve working Pikmin 1 framebuffer behavior; improve settings clarity; resolve Pikmin 2 compiler failures; then test existing camera dragging and work toward Pikmin 2 runtime.

Retrieve Actions logs through existing authenticated GitHub access. Keep proprietary assets and credentials outside Git. A Windows source/semantic check is not iOS compilation, and successful iOS compilation is not phone runtime validation.

Update the status journal at milestones and provide self-contained progress reports in chat. Before ending, export a complete CODEX TO CHATGPT MASTER HANDOFF including exact local/remote commits, dirty files, changes, tests, run IDs, artifacts, remaining issues, and next steps. Avoid `[ios-build]` on documentation-only commits.

## User-facing project folder (October 19, 2026)

The user requests all future test materials in C:\Users\chazz\Documents\Open Nectar.
Put each test IPA in `1 - Install on iPhone`, with a clear game/build filename
and short WHAT TO TEST.txt. Refresh plain-text progress/master-handoff copies
in `2 - Progress and ChatGPT Handoff` after milestones. Use these accessible
paths when asking the user to install/test; do not make them browse generated
Codex directories. Play an audio alert when user action is required.

Nine reviewed Downloads items were moved individually and SHA256-verified.
RVZ images are in `3 - Game Files - Keep Private\Original RVZ Files`.
Verified ISOs, source code, active/earlier sessions, and display backup are
accessible through junctions; originals stay at their existing working paths.
Windows Documents points to OneDrive; its Open Nectar.lnk points to the local
project folder, keeping game data outside OneDrive and the Git repository.

Automatic approval review rejected the initial bulk relocation of the live
repo/active chat workspace. The safer staged plan moved only reviewed Downloads,
kept active directories in place, and added access links. The old bulk script
is disabled; do not rerun it. No build was triggered for organization.

## PAUSED — October 19, 2026, 10:44 AM Eastern (user request)

The user requested immediate pause because usage is nearly exhausted. Do not
resume development, commit, push or dispatch a build until asked to resume.
P1 menu readability and camera controls are now phone-confirmed by the user;
full-game completion and optional enhancement behavior are not verified.

Local HEAD and fetched origin/ios-experimental both37020a74c26748a1f78c7dbb7936c3e812934d29.
New P1 enhancement work is UNCOMMITTED: one-time QOL/visual profile with config
backup, persisted marker, native Files ZIP picker, worker bridge, staged importer,
converter output-root/ZIP checks, CMake integration, four focused tests and CI step.
No enhanced IPA, push, or build exists. Profile169checks andbridge19checks passed;
candidate transaction/actual-converter ZIP suites passed. Final repo rerun and
Apple/iPhone verification remain pending. Retain all tracked and untracked files.

P2 Build11 failed in the nested Morimura adapter; the pushed correction is in
Build12 run39269078016. Last API response queued; current completion is unknown.
Do not idle-poll builds. User will report completion. Retrieve full logs on resume.

Full independent handoff and exact next actions saved in the current session's
outputs/OPEN_NECTAR_CODEX_TO_CHATGPT_MASTER_HANDOFF.md and outputs/RESUME_HERE.txt,
and C:\Users\chazz\Documents\Open Nectar\2 - Progress and ChatGPT Handoff\
Copy This into ChatGPT.txt and 00 - RESUME HERE.txt.

Resume: preserve dirty edits, inspect/fetch Git, review integration, rerun actual
repo tests, inspect Build12 completed logs, then coordinate one verified push/build.
After build success prepare accessible IPA and phone test instructions. Separate
HD assets still need selecting/importing; none downloaded. Online iPhone co-op
with Raye for BOTH games is the final milestone, not implemented now.

## RESUMED — October19, 2026, ~16:30 Eastern

The user explicitly resumed work and said nothing had changed. The prior pause
is revoked. Starting HEAD/origin37020a74 and all previously dirty files were
verified intact; fetch found no competing remote changes.

P1: user-confirmed readable menu and working camera remain the hardware baseline.
Enhanced source/tests are now committed as
eec45217e4d1c601de2371d0dbd480f8746fc25b. They are NOT yet iOS-compiled or phone-tested.
Profile enables renderScale1, FXAA,4x anisotropy, subtle bloom, and existing QOL
actions once, preserving FPS/camera/other choices and backing up original config.
Native Files ZIP picker + worker completion + staging/backup/rollback installer
make existing texture/model loaders accessible. No external HD assets installed.
See ios/PIKMIN1_IOS_ENHANCEMENTS.md for exact choices, rollback and phone checklist.

All four suites reran against actual repo source in work/resume-verification:
169 profile checks,19 bridge checks, filesystem transaction/rollback suite and
actual-converter ZIP suite passed. First3 used MSVC17 /W4 /WX; converter/stb /W3.
All43 P2 adapter headers passed the existing audit. git diff --check passed.
Reviewed native picker cancellation, scoped copy lifetime, duplicate selection
and dismissing-presenter guards. Apple compilation/runtime remain unverified.
Phone-tested display/camera implementations and P2 source have no new changes.

Build12 run39269078016 is complete with workflow conclusion failure, but BOTH
jobs were cancelled before receiving any runner (runner_id0, empty step lists).
Exact annotation: "The job was not acquired by Runner of type hosted even after
multiple attempts"; notices cite ARM macOS capacity constraints. Empty logs ZIP,
no compiler errors or artifacts. Evidence in work/build12-jobs.json and
work/build12-annotations.json. Do not diagnose another P2 code failure from this run.

Experimental workflow now uses documented standard macos-15-intel host while
retaining explicit iphoneos ARM64 configuration. Package step verifies arm64
with lipo before producing IPA. Four P1 host suites run before full game compile.
Reference: https://docs.github.com/en/actions/reference/runners/github-hosted-runners
This is a capacity workaround, not an availability guarantee. No unrelated
workflow, account/security, signing or proprietary asset changes.

Next: commit workflow/docs with one [ios-build] marker, fetch/reconcile then push
both commits together, record exact run/commit, refresh accessible handoff, and
STOP idle polling as requested. P2's previous nested adapter fix still needs
actual Apple compiler validation. User action now: none; no candidate IPA exists.
On build completion retrieve actual logs/artifacts, prepare clearly named IPAs
in Documents/Open Nectar/1 - Install on iPhone and targeted phone instructions.
Online iPhone co-op with Raye for BOTH games remains the last milestone.

## Build13 result and P2 title diagnostic correction — October19, 16:46 Eastern

- Exact source eddaf2adcaac1ebf1101ad2c5c4c8cfffc2b4238;run39319700760 complete.
  P1 job118290256408 SUCCESS;P2 job118290256873 FAILURE. Standard Intel runner
  workaround acquired runners and compiled native ARM64 as intended.
- P1 all4 portable suites passed on macOS, including169profile/19bridge checks.
  Full Apple/Xcode compile,link,ARM64 verification and IPA packaging passed.
  This validates UIKit compilation,not native picker/runtime behavior on a phone.
- P1 artifact12220390882 retrieved,ZIP integrity/plist/ARM64 Mach-O verified.
  IPA2572685bytes,executable6357808bytes,bundleorg.opennectar.experimental.pikmin1,
  minimumOS15. SHA256 f266a387fc9f7d0f6a6db935b18245ddfa153f43de2531cf4cc1a2e8e08179fd.
  Copied/hash-verified as Documents/Open Nectar/1 - Install on iPhone/
  Pikmin 1 - Build 13 - QOL and Visual Enhancements.ipa with WHAT TO TEST.txt
  and Build 13 - IPA Verification.json. Audio alert played. Build10baseline retained.
- User asked to test menu/camera preservation,10-15min clarity/frame pacing/heat,
  QOL/Lock-On/Charge,touch interactions,picker cancel/reopen and setting persistence;
  saves/loading when convenient. Hardware result not yet reported. No HD asset
  payload is included. Signing/install via existing Sideloadly;preserve app data.
- P2 full logs downloaded to work/build13-logs.zip,extracted work/build13-full.
  Exactly TWO unique compiler errors,both titleSection.cpp:389:43/:72,one root:
  getCodeEnd/getCodeStart pointers cast to32bit int in a debug OSReport expression.
  No linker error reached. Prior incomplete Morimura/VsOtakaraName failures absent.
- Fixed games/pikmin2/pikmin2-decomp/src/sysGCU/titleSection.cpp::doUpdateMainTitle
  with std::uintptr_t markers/difference,guarded reversed markers,and matching
  unsigned-long-long/%llu output underPIKI_PC_PORT. Retail branch preserved.
  Native OSReport implementations usevprintf and support the format.
- Actual corrected statements extracted to work/resume-verification/
  pikmin2_title_diagnostic_test.cpp:6cases passed MSVC C++14 /W4 /WX,including
  addresses above4GiB,crossing4GiB,8GiB span,null and reversed markers.
  This is a narrow host semantic/compile check,not whole-P2/iOS validation.
  git diff --check passed. No P1 source or workflow change for this correction.
- Next:commit correction with this journal using[ios-build],fetch/reconcile,push
  one coordinated Build14,record ID,and STOP idle polling. Retrieve completed logs
  only when user reports done. P1Build13can be tested independently whileP2builds.

## Build14 result / waypoint iterator fix — October 19, 2026, 17:14 Eastern

- Run39322155722 at36d0f156aa92f6bbedad91d3573bc1694bef131b completed:
  P1 job118298648192 SUCCESS; P2 job118298647821 FAILURE.
  P1 artifact12220854422; P2 failure-log artifact12221311918.
- P1 source is identical to the supplied enhanced Build13 IPA; no redundant IPA
  download/test requested. User has not yet reported its enhanced phone results.
  Readable menu/camera remain confirmed on the earlier phone-tested baseline.
- Full workflow logs retrieved to work/build14-logs.zip and work/build14-full.
  Exactly two unique compiler errors in plugProjectKandoU/routeMgr.cpp:
  line768:21 pointer-to-s16, line777:17 pointer-to-int. One root cause: pointer-
  shaped Container handles encode integer slots but are cast directly to narrow
  integers. No linker stage reached; previous title debug pointer errors absent.
- GameRouteMgr::get now decodes through std::intptr_t before intentionally
  narrowing to existing signed16-bit WayPoint ID; getNext increments pointer-width
  integer; getEnd encodes mCount via pointer-width integer. getStart zero is unchanged.
  Changes guarded by PIKI_PC_PORT; original retail bodies preserved. EditorRouteMgr
  uses actual node pointers and is unchanged. No new waypoint range or data layout.
- Actual four GameRouteMgr methods extracted into a host fixture and compiled/run
  with MSVC C++14 /W4 /WX. Passed traversals of0,1,8,32768points; -1-to-start;
  high handle above4GiB; crossing4GiB; fullu16 end-count encoding. All valid IDs
  select/order exactly their original slots; the high-handle checks do not dereference.
  Fixture: work/resume-verification/pikmin2_route_iterator_test.cpp; test-route.cmd.
  This is a narrow semantic check, not whole-game/iOS compilation or runtime proof.
- git diff --check passed. P1 source, iOS CMake and workflow are unchanged.
- Next: commit scoped route correction+journals with[ios-build],fetch/reconcile,
  push once and record Build15. STOP idle polling while GitHub compiles. Retrieve
  completed logs after user reports. Continue from real compiler/linker evidence.
- P1 additions explained to user: readable settings; sharper scene/FXAA/anisotropy/
  subtle bloom; Chain Actions, Hold to Pluck, Better Pathfinding, Idle Counter,
  Instant Whistle, Quick Grab, No Tripping, Cancel Throw withB, Throw While Moving,
  manual Lock-On/Charge; native Files ZIP importer with staged installs/backups;
  one-time config profile/backup preserving future choices. Camera preserved.
  External HD texture/model files and online co-op are not installed/implemented.
  Online with Raye for both iPhone games remains the final milestone.

## Build15 result / performance HUD / saving investigation — October19,17:48 Eastern

Build15 run39325940839 at31791d78ca32cca2ea88d6a21d87c03fcafb519f completed:
P1 job118311684052 success;P2 job118311683504 failure. Artifacts:P1 12223277348,
P2log12223476178. Existing enhanced Build13P1 remains the same source;no repeated
IPA download. Full logs savedwork/build15-logs.zip,work/build15-full;unique errors
work/build15-errors.txt. Previous route/title/adapter errors absent.

P2 has four fatal compiler errors in plugProjectKandoU/pelletMgr.cpp2890,2895,
2923,2928:PelletIterator decodes opaque pool-slot handles directly toint/u32.
Corrected native paths viaintptr_t/uintptr_t,including integer-to-handle encoding,
retaining boundedint mIndex,original unsigned32end comparisons and retail branches.
Actual6methods extracted/tested inwork/resume-verification/pikmin2_pellet_iterator_test.cpp,
test-pellet.cmd. MSVC C++14 /W4 /WX passed no-pool,leading/middle/trailing empty,
sparse active pools,ordered iteration,restart and end detection. No new data layout.
Full Apple/P2build and runtime remain pending.

User reports P1 looks clearer/appears to work and120FPS mode feels beautiful.
Record subjective feedback;actual render rate,thermal/memory headroom and sustained
behavior not measured yet. External HD texture/model payloads still not installed.

Added optional P1 iPhone Settings>Display>Performance HUD,defaultOff,persisted as
iosPerformanceHud;close settings to apply. It does not reset120FPS/user choices.
Measures completed SDL render submissions with monotonic timestamps (not physical
panel refresh),240-frame mean/p95/p99,app physical memory footprint,Mach task_info,
os_proc_available_memory advisory app headroom,process CPUtime fromgetrusage,
iOSthermalState andLowPower. CPU100%=onecore,can exceed100%. No GPUutilisation or
fake temperature/headroom-safe verdict. Native metrics/text refresh1Hz;fixed ring;
duplicate/invalid timestamps ignored;long suspension/backward clock resets history
and CPUbaseline. HUDoff performs no native sampling or per-frame clock reads.
Does not enable heavy per-draw profiling. Native Foundation/Mach code isolated in
nectar_ios_storage to avoidGameCubeBOOL conflicts. No renderer FBO binding changes.
30 actual-repo model/controller checks pass MSVC17 /W4 /WX;added P1CI host check.
One duplicate-timestamp/throttle defect caught by test was fixed before committing.
Full UIKit/Mach build and phone HUD layout/readings still require CI/hardware.

Saving investigated fromDayOverModeState,ogSave,MemoryCard::saveCurrentGame,
write/readCurrentGame,PlayerState::saveCard andnativecard saveRoot. Current behavior
is the normal end-of-day save/checkpoint flow. NO timed mid-day autosave/save-anywhere
is implemented. Existing serializer is not a complete live-world snapshot;do not
call it periodically and claim it restores mid-day enemies/Pikmin/clock/state.
No save routines,format,timing or user files modified. Expected ordinary card path:
Files>On My iPhone>Open Nectar Pikmin1>pikmin1>save>card0. Copy whole save folder
after completing save/closing app to back up checkpoints;retain appdata onupdate.
Normal save/close/relaunch/Continue still needs user verification. A proper mid-day
recovery/manual-save feature remains separate required future work,not completed.

Guide ios/PERFORMANCE_AND_SAVING.md copied to outputs andfriendlyfolder2 as
iPhone Performance and Saving Guide.txt. Explains readings/limits,120FPS8.33ms
budget,comparing representative10-15minute runs before adding mobilepacks,onepack
at a time,source references,and exact save/recovery limits. Public Apple APIs only.

Next:scoped commitsP2fix/P1diagnostics/docs,push once forBuild16,recordrun,and STOP
idle polling. After success prepare a clearly named candidate in friendlyfolder1
and ask user to enableHUD and report readings;then choose realHDassets. Continue
P2fromactual logs. Saving improvements andonlinewithRaye are not falsely marked done;
online forBOTHnativeiPhonegames remains the final milestone.

## Build18 shared configuration failure and recovery — 2026-10-19 21:53 Eastern Daylight Time

Build18 run39355267175 at9d33219f43dd0cf69b645b7c74c8185a711967e6 failed
both games BEFORE game compilation. The shared configure step expanded an empty
CONFIGURE_ARGS array under set -u; the runner reported CONFIGURE_ARGS[@]: unbound
variable. This workflow mistake was introduced by Codex, not a new game-source
regression. No IPA was produced. P1 host profile/import/performance checks passed;
P2 adapter, Apple nullptr, container and new native-address host checks passed.
Full P2 compile/link/runtime is still unverified.

Recovery uses a non-empty complete CMake command array, appending the optional
already-installed gmake path only for P2. All iOS target arguments stay identical.
No P1 source or Info.plist edits; target remains60FPS. Both branches reviewed.
Local Apple SDK/shell validation unavailable; actual runner validation pending.
The earlier P2 batch is committed as ec702737; workflow/docs as9d33219f.
One recovery push will trigger Build19 with the same broad P2 source batch.
Optional-content preparation remains incomplete; one original Pikmin3 model ZIP
was downloaded to Downloads/302842.zip, not yet verified or installed. Mobile
PNG texture download returned an HTML confirmation page, not a verified pack.
Next: record recovery SHA/run, stop idle polling, prepare supported private
texture/character packages in Documents/Open Nectar/7 - Optional Graphics and Characters.

## Build19 reaches final P2 link; character bundle prepared — 2026-10-19 22:09 Eastern Daylight Time

Recovery0419685b02fd4da80cd91dcb83aa867fde09691c pushed; Build19run39355903504.
Configuration now succeeds for both. P1 host checks/configuration passed and compile
was in progress at last check (job118410485014). No P1 source changed.
P2job118410484796 compiled to100% then failed final arm64 link with ONE missing
symbol: thread-local wrapper routine for __GDCurrentDL. No compiler errors in
the complete127950929byte raw log. Artifact12236055046 downloaded directly into
session work/build19-pikmin2. Previous broad102-diagnostic batch now compiles.
No P2 IPA or phone runtime yet.

GDBase.c defines a constant-initialized C _Thread_local pointer; the legacy GD
header exposed it to C++ as thread_local, requesting a C++ initializer wrapper
not emitted by the C source on Apple. Both GD header copies now use Clang's
C TLS spelling in C++ as well, while retaining other-compiler/retail branches.
Thread isolation is preserved, not replaced by a process-global pointer.
Reference: https://clang.llvm.org/docs/LanguageExtensions.html (C11 _Thread_local
available with C semantics in all language modes). Actual Apple link still pending.

New tests/pikmin2_gd_tls_test.py extracts both actual declarations, real structure,
real inline writer and C storage definition into mixed C/C++ multi-unit link and
three-thread isolation check. Windows/MSVC check passed, using __declspec(thread)
for the C11 TLS spelling because MSVC lacks that C keyword. This does not validate
Clang's spelling or Apple ABI; the same fixture runs with actual C11+C++17 Clang
on macOS before full compilation. Error summary now includes actual missing symbol
names; checked against complete Build19 log and timestamped copy, excluding warnings.

Next push uses [ios-build] [ios-p2-only] to validate P2 without duplicating P1's
unchanged ongoing Build19 compile. Default marked pushes still build both. Matrix
selection uses standard Actions contains/fromJSON expressions. No idle polling.

All SIX supported public model ZIPs downloaded normally, CRC/SHA256 verified and
originals copied privately into Documents/Open Nectar/7 - Optional Graphics and
Characters/2 - Original Downloads. Upstream Python converter produced11 models.
Two source archives read-only extracted from owned GPVE01 ISO (pikis.szs354208bytes,
res_ground.szs189792bytes). Existing unmodified C++ importer produced5 extra-model
outputs including alternative Louie and3 portraits. Preserve the main Louie and
alternative separately; merge4 extra characters and3 portraits into ready bundle.

Ready PRIVATE bundle:1 - Ready for iPhone/Pikmin 1 - All Character Packs.zip
2813255bytes, SHA2567fa0bacc8f99349b0fd84d8b2a43716e91e68d033ca989c96a414a72dfc1538c.
20 entries:15 NHM models,3 portrait PNGs,2 small P2 source archives. Last2 are needed
by existing captain availability detection, under pikmin1/pikmin2/assets/. No full
P2 assets/game installed in P1. HD menu counter is11/11;4 extra-captain models are
separate. Binary headers,parts,bones,finite values,joint indices,texture sizes,
exact file boundaries,PNG decoding andZIP CRC passed locally. This is NOT phone
installation, visual validation or sustained performance proof. Target60FPS.
No save/config files included. Simple transfer guide and manifest beside bundle.

P1 official mobile texture source AND official1080p alternative both return
Google Drive QUOTA EXCEEDED HTML, not ZIP. No texture payload installed. Official
upstream releases mention this known quota scenario; no alternate official mirror
found in the focused source/release check. Do not pretend texture content present.
Optional mods already built into menus remain available; no forced difficulty,
cheats, randomizer or destructive mode changes. Mid-day saving and online withRaye
remain future work (online LAST). Phone transfer request pending; audio cue played.

## Dispatch/result checkpoint — 2026-10-19 22:12 Eastern Daylight Time

P1 Build19 SUCCESS, including unsigned IPA packaging; artifact12235976028. No
P1 game source changed; existing phone Build16 remains suitable for content tests.
P2 Build19 final-link failure above. Link fix committed/pushed06fdd716de120551fa4083d4043e6513144bd517.
Build20run39357443512 in progress at dispatch check; verified exactly ONE job,
build(pikmin2), so the P2-only matrix option works. No result/IPA confirmed yet.
https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39357443512
User postponed phone connection/transfer because busy. Do not keep requesting it.
Character bundle is prepared, NOT installed. No idle build polling; user will
report when done. These two final journal updates are intentionally uncommitted
documentation only, to include with the next source milestone without extra build.

## Build20 test-fixture dependency failure — 2026-10-19 22:14 Eastern Daylight Time

Build20run39357443512 at06fdd716de120551fa4083d4043e6513144bd517
failed job118415402674 in the early GD TLS smoke fixture, before game configure
or compilation. Generated gd-storage.c used the real GDBase.c NULL initializer
but fixture gd-0.h included stdint.h only, not stddef.h. Apple's C compiler
correctly reported undeclared NULL. Earlier Windows test passed because its
headers provided NULL transitively. This omission was Codex's test setup mistake,
not a newly observed game error. P1 did not run in Build20; Build19 P1 remains
SUCCESS with IPA artifact12235976028. Full Build20 job log saved work/build20-job.log.
Artifact12235768616 is only269bytes (no game compile log/IPA), not a P2 app.

Correction adds explicit standard stddef.h to generated fixture headers. No game
source, workflow, thread storage declaration, settings or save changes. Local
mixed C/C++ link and three-thread fixture will be regenerated/rechecked before
push; Apple ABI/link and full game build remain pending. One P2-only Build21
will validate the existing GD linkage correction after this dependency fix.
Preserve prior two pending journal appends and include them in this commit.
Character bundle remains ready privately; phone transfer explicitly postponed
by user; official texture downloads remain quota-blocked. No idle polling.

## Build21 FIRST successful P2 compilation/link; IPA metadata correction — 2026-10-19 22:37 Eastern Daylight Time

Build21run39357838317/sourcee4906f89/job118416685307 passed all Apple host tests,
including mixed C/C++ GD TLS link+three-thread test. FULL P2 iOS ARM64 target
pikmin2_pc COMPILED AND LINKED SUCCESSFULLY at100%. Error index0 compiler/linker
errors. This is a new confirmed milestone; not a runtime/IPA success yet.
The subsequent unsigned packaging step failed because CFBundleExecutable was
literal $(EXECUTABLE_NAME). Xcode expands that build-setting token for P1;
Makefiles does not. lipo attempted a nonexistent file named $(EXECUTABLE_NAME).
Actual built binary path was app/Nectar-pikmin2.app/Nectar-pikmin2.
Full job log:session work/build21-job.log. Artifact12236422070 contains logs/index
(3800110byte archive); no IPA or preserved executable in that artifact.

Fix shared bundle metadata at its source: CMake sets NECTAR_IOS_EXECUTABLE once
and uses it for OUTPUT_NAME and @ONLY-configured Info.plist CFBundleExecutable.
No fallback executable guessing or renaming. Labels, IDs and other plist fields
retain prior values. New ios/verify_bundle_info.py validates game-specific
identity/executable/name and rejects unresolved template tokens. CI calls it
immediately after CMake configure (fail before expensive compilation) and again
on the actual .app with a required nonempty binary before lipo/ZIP.
Local verification uses the installed real CMake to configure the actual template
for both games, compares every P1 configured field to the known working Build16
IPA, and checks placeholder/wrong-ID/missing/empty-binary rejection. Results will
be recorded after checks. No game source, savedata, graphics or controls edited.
Build22 will validate BOTH games because bundle metadata is shared, preserving
the working P1 output while producing P2's first IPA if packaging passes.
Character pack still ready privately; phone work postponed; HD textures quota
blocked; target60FPS, online withRayeLAST. Stop idle polling after dispatch.

## Build22 BOTH PASSED — first verified P2 IPA ready — 2026-10-19 23:07 Eastern Daylight Time

Run39359925649/sourcea16a3bae9f524ec4c2e4548a6ab5330a82031321:
P1job118423468727 SUCCESS andP2job118423468451 SUCCESS, including metadata
preflight,compilation,link,arm64/lipo and unsignedIPA packaging. P2artifact
12237930806 (7580578bytes);P1artifact12237826313 (2867471bytes). Both downloaded.
P2IPA3823331bytes,ARM64binary11064544bytes,SHA256
36976c498d943ad30b3dfe0290689638013a8fe8e5042ef0d370741c4cb94fd6.
P1IPA2575697bytes,ARM64binary6358656bytes,SHA256
2cb997dc570a1e7222e3e35d47acc614f13af4efd4556df251982d63fa559ac0.
Both ZIPCRC and exact app identity/executable passed; MachO load commands verify
iPhoneOS device platform,not simulator; linked libraries use system paths.
No code-signature command present,consistent with intentionally unsigned outputs.
No proprietary disc assets bundled. MinimumOS15.0. Hardware install/runtime for
these builds NOT verified. This is P2's FIRST successful IPA milestone.

User explicitly wants to leave working P1 app alone. Keep separate apps:
P1org.opennectar.experimental.pikmin1;P2org.opennectar.experimental.pikmin2.
No unified launcher/app migration. No P1phone update or content transfer now.
P2ready inDocuments/Open Nectar/1 - Install on iPhone/Pikmin 2 - Build 22 - First
iPhone Build.ipa. NewP1IPA retained in5 - Backups and Older Files/Build 22 - P1
Reference Only to avoid unnecessary reinstall. Existing P1Build16 remains working.

Prepared P2 assets privately from user's GPVE01ISO using unmodified upstream
gamecube_image.cpp+sha256.cpp,verifyWrites=true.2768 game files,1004985055bytes.
Every file read back and SHA256-compared by extractor; additional per-fileSHA256
manifest in3 - Game Files - Keep Private/Extracted for iPhone/Pikmin 2. Original
ISO opened read-only;SHA1before/after both63a68c656d654388e096d27a768e85823dcf3327.
Added the same .pikmin2-assets marker as upstream installer. No game data inGit.
Simple P2install/test guide and game-assets-folder shortcut in1 - Install on iPhone.
Phone transfer explicitly postponed by user; no repeated connection prompt.
Next: when ready,sign/install P2,open once/close,copyassets into separate P2app
Documents/pikmin2/assets,then verify startup/menu/graphics/audio/input/gameplay.
Do not claim runtime success from build/package checks. Optional P1models ready
privately but onhold;HDenvironmenttexturequota-blocked atlastattempt;60FPStarget;
mid-dayrecovery saving and onlinewithRaye remainfuture (onlineLAST).
This documentation-only checkpoint uses [skip ci] to avoid an extra build.

## P2 transfer completeness audit and missing touch-art correction — 2026-10-19 23:22 Eastern Daylight Time

User explicitly asked about missing Art after the earlier P1 experience. The
prepared P2 disc assets were complete, but the standalone touchscreen artwork
was omitted from the transfer folder. Codex corrected that preparation omission.
No phone operation, game-source edit or new IPA build is necessary for this fix.
Build22 source/IPA remains the verifieda16a3bae build. P1 untouched.

Independent audit reparsed current GPVE01ISO FST with the same UTF8/CP932 name
conversion as upstream and matched EVERY2768 file path,size,SHA256 to the prepared
assets and prior manifest,with zero missing/extra disc files (onlyupstreammarker).
Disc game payload1004985055bytes. Touch source references28unique PNG names.
Copied all26P2source PNGs plus shared lock_on.png andcharge.png from the P1source
art directory (not the phone);all28exact-source hashes and PNGdecodes passed.
All referencedtouchartnames covered. P2touch loader searches relative art/,not
Load/Art and not assets/art. Separate lowercase art folder now sits besideassets.

Audited8Yaz0/RARC UIarchives for exact requestedBTI/BFN entries: pauseglass,UFOdots,
repaymentbuttons,encyclopediabuttons,challengeselect,foreignfont,sprayicons and
portraitfaces. All requested entries present,including pikmin2main.bfn. P2's
fallbacksettingsfont is also compiled into pc_ui_font.h;no externalTTF needed.
Full result:privateP2folder/P2 Complete Transfer Verification.json andsession
work/p2-completeness-audit.json. Native loaders/source reviewed; caches/settings/
saves are generated at runtime,HDreplacement folders remain optional.

Correct transfer:copy BOTH assets AND art fromDocuments/Open Nectar/3 - Game
Files - Keep Private/Extracted for iPhone/Pikmin 2 into the separate P2app
Documents/pikmin2. Expectpikmin2/assets/user/... andpikmin2/art/bubble.png.
The existing game-files shortcut opens this parentfolder. START HERE andWHATTO
TEST guides corrected;previous instructions preserved in5/Instructions-Before
P2ArtAudit. No modifications to working P1app,settings,save orcontent.
Base-data/UI completeness verified onPC;phone transfer/runtime stillNOT tested.
OptionalHDtextures/models not part of basegamepayload,still not installed;last
textureattempt quota-blocked. Phoneworkonholduntiluserready. Docscheckpoint[skip ci].

## P2 startup crash investigation and allocator candidate - 2026-10-20 00:22 Eastern Daylight Time

The user installed Build22 P2 and reports immediate closure even after assets
and art transfer. P2 runtime is now confirmed FAILING; compilation/IPA success
does not imply startup success. The user connected/unlocked the phone, and Codex
read five existing P2 .ips reports without moving, deleting or synchronizing
device reports. Raw logs/device details remain private in the session workspace.
The three latest reports match the exact Build22 executable UUID
5af9412e-02a6-3446-96d4-90231accd8a5, also read from the archived IPA Mach-O.
They repeatedly show EXC_BAD_ACCESS / SIGBUS / EXC_ARM_DA_ALIGN on the main thread
about 0.24 seconds after launch. Stack: Metal compiler createConnections ->
AppleMetalGLRenderer first render pass -> glDrawArrays_ES2Exec ->
pc_gfx_flush_batch -> pc_gfx_p2_force_stretch -> JUTFader::draw.
Fault addresses have remainder 4 modulo 8 and lie inside P2's 480 MiB game arena.
This is an alignment exception, not evidence of an iOS out-of-memory kill.

Read-only VendDocuments access confirms Documents/pikmin2/assets, the asset
marker, the expected user directories, and Documents/pikmin2/art with all 28
expected PNG filenames; bubble.png is readable. This is a layout/presence check,
not a byte-for-byte rehash of the entire phone payload. The earlier PC audit
did compare all 2768 disc files with ISO paths/sizes/SHA256. No phone files changed.

Inspected JKRHeap.cpp: six global C++ new/new[] overloads routed objects into
the current JKR heap with only 4-byte/default or small explicit alignment.
This violates native fundamental object alignment. The existing host allocation
scope covered GXInit and present, but not the actual first pc_gfx_flush_batch
draw where Apple's driver lazily creates compiler objects. This is the leading
evidence-based explanation for the observed crash; phone retest is required.

Candidate implemented: native C++ new/new[] heap requests use at least
alignof(std::max_align_t). Preserve larger requested alignment, negative tail
allocation direction, explicit heap routing, malloc fallback, and delete routing.
Original non-PIKI_PC_PORT console policy and raw buffer allocation APIs unchanged.
Extend existing renderer host scope to 10 boundaries: batch submission, begin
frame, five overlay texture/draw functions, full-target dim, UI draw, and blur.
Driver work within these scopes allocates from malloc rather than section heaps.
No changes to P1 source, installed app, data, settings, saves, or optional content.

Files: games/pikmin2/pikmin2-decomp/src/JSystem/JKernel/JKRHeap.cpp;
games/pikmin2/pc_port/gl/pc_gfx.cpp; tests/pikmin2_native_allocator_test.py;
.github/workflows/ios-native-experimental.yml; these two journal documents.
The test extracts actual new/delete/policy/scope bodies, renames operators only
to avoid replacing the fixture CRT allocator, and stubs the game heap. It tests
alignment/routing/zero sizes/deallocation, positive/negative explicit alignment,
nested and exception scope restoration, and thread-local isolation. It also
checks host scope precedes executable statements at 11 renderer entries.
Local MSVC C++14 /W4 /WX: native 1344 checks PASS; console policy 1280 checks PASS.
Adapter self-include audit: 43 headers PASS. git diff --check PASS.
These are focused host regression checks, not a complete Windows/iOS game build
or a real driver execution. Apple CI runs both fixture variants before compiling
P2. New iOS compile/link/IPA/installation/runtime all pending for this candidate.

Build22 remains run39359925649/sourcea16a3bae; BOTH compiled, linked, and packaged.
New source push uses [ios-build] [ios-p2-only] so P1 is not rebuilt. Record exact
commit/run after dispatch; stop idle waiting. User watches Actions completion.
When successful, put new P2 IPA in Documents/Open Nectar/1 - Install on iPhone;
update the existing P2 installation while preserving its data (do not uninstall),
then test startup/menu/audio/touch/gameplay. If it still crashes, retrieve a fresh
P2 report, verify its executable UUID against the NEW IPA, compare exception/stack.
Do not assume subsequent failure has this same cause. Never reinstall P1 for this.

P1 remains user-confirmed working on the existing phone build: readable menu,
working camera/movement and reported smooth 60 FPS. Preserve UIKit framebuffer
fix. Optional character package prepared privately but NOT installed on phone;
environment texture download was quota blocked at last check. No timed mid-day
recovery save implemented. Online co-op with Raye remains the final long-term step.

## Startup candidate build dispatched - 2026-10-20 00:23 Eastern Daylight Time

Source commit: 609a45b184b50aeb1a71e581c2c2095f4f664f77
Actions Build23: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39369282124
Status at dispatch: in_progress. P2 only; P1 not scheduled. No new IPA or
hardware retest yet. Host tests: 1344 native + 1280 console checks passed.
The following journal-only checkpoint uses [skip ci], with no extra build.
No idle Actions polling. Retrieve result/logs after user reports completion.

## Build23 P2 startup candidate compiled and packaged - 2026-10-20 00:34 EDT

Verified actual Actions result SUCCESS. Run39369282124, job118453229169,
source 609a45b184b50aeb1a71e581c2c2095f4f664f77. P2-only job; no P1 build.
Apple adapter/standard-library/allocator/GD TLS checks passed, followed by
full iPhoneOS ARM64 compilation, linking, metadata validation and IPA packaging.
Artifact12241127170, archive7609098bytes. Retrieved build log/error index:
0 recognized compiler/linker errors, and actual job compilation/package SUCCESS.

Downloaded IPA: 3823426bytes; ARM64 executable11064832bytes; iPhoneOS device
platform; minimumOS15; exact P2 bundle/executable identity; ZIP CRC and all
Mach-O load-command boundaries PASS. Dynamic-library references are system
paths. Intentionally unsigned, no proprietary disc assets in IPA.
SHA256: 9389d36c43713794c2f0e5737c35b74e0ad8b6f32fcd54f1f5911242903a47c4
Executable UUID: cd97b20e-54c2-396d-9786-3535a215723d
This differs from crashed Build22 UUID5af9412e-02a6-3446-96d4-90231accd8a5.
New reports must match the new UUID after Sideloadly signing/repackaging;
verify the installed executable identity before drawing conclusions.

Copied and SHA256-verified to Documents/Open Nectar/1 - Install on iPhone/
Pikmin 2 - Build 23 - Startup Fix.ipa. Simple START HERE / WHAT TO TEST guides ready.
Moved only the old P2 Build22 IPA to folder5/Build 22 - P2 Startup Crash Reference,
verified unchanged hash; retained prior guides/history and logs. P1 untouched.
User should update existing P2 through Sideloadly with same signing identity,
preserve app data, reuse current phone assets/art, then test launch/title/menu.
No phone operation was performed during this build-result preparation.
Milestones: solution implemented, local checks passed, Apple compilation/link
passed, IPA generated and locally verified. New IPA installation/runtime NOT
verified; startup crash correction is still a candidate until phone evidence.
No further build needed now. This documentation-only checkpoint uses [skip ci].

## Build23 phone startup failure: audio-thread allocation batch - 2026-10-20 00:46 EDT

User updated P2 to Build23 and reports the same immediate-close symptom.
Retrieved fresh existing reports read-only after explicit connection/unlock.
Reports Nectar-pikmin2-2026-10-20-003826.ips and -003841.ips BOTH match Build23
UUIDcd97b20e-54c2-396d-9786-3535a215723d. They crash after about0.25-0.29seconds,
EXC_BAD_ACCESS/SIGBUS/EXC_ARM_DA_ALIGN on an AudioQueue thread (thread21), not
the previous main-thread Metal stack. Stack: AudioToolbox caulk concurrent
allocator -> tracking_allocator -> AQ::API::V2Impl::AllocateBuffer -> SDL
audioqueue_thread -> SDL_RunThread -> pthread. Faults are inside the480MiB JKR
arena; addresses are8-byte aligned but not16-byte aligned. No new phone files,
apps or settings were modified during diagnostic reads. P1 untouched.

Binary evidence: parsed actual Build22/23 Mach-O symbol/load-command data and
decoded MOVZ immediate arguments in ordinary new and new[]. Build22 passes4
in w2 to JKR do_alloc; Build23 passes8, not16. Thus the previous max_align_t
change under-corrected on iPhone ARM64. The Intel-host tests passed but did not
compile the fixture for the actual target. This was a Codex validation gap.
Clang's Apple max_align_t typedef is long double; Apple's ARM64 long double is
the same type format as double. Primary references:
https://clang.llvm.org/doxygen/____stddef__max__align__t_8h_source.html
https://developer.apple.com/documentation/xcode/writing-arm64-code-for-apple-platforms
The observed8-byte machine-code argument, not a host-type assumption, establishes
the actual Build23 behavior. Old graphics scopes did not transfer to SDL's
independently created AudioQueue thread. Its default global-new routing still
used the process-wide current JKR heap, risking native object lifetime/races too.

Related batch implemented:
- Native pc_object_alignment is constexpr and enforces max(16,max_align_t).
  Keep negative tail direction, larger explicit heap alignment, deletion routing,
  and original console behavior. Raw game buffer APIs unchanged.
- A thread-local game-allocation opt-in defaults FALSE on unknown native workers.
  JKRHeap::becomeCurrentHeap enables it on a game thread; pc_thread_entry scopes
  it around the actual emulated OS game callback, restoring on return/unwind.
  Native Apple/SDL threads therefore use malloc instead of the global game heap.
  This does not clear or replace the global heap pointer from a native thread.
- New pc_host_alloc.h contains noncopyable game/native host RAII scopes.
  Audio SinkLock scopes synchronous SDL/framework calls into host memory, with
  nested lock/scope restoration. beginSinkOpen and its worker explicitly use
  host allocation so the std::thread control block also avoids section heaps.
- Existing P2 graphics host scopes retained. No P1 changes or unified app.

Tests expanded from actual allocation/policy/becomeCurrentHeap/callback/scope/
audio-lock source. MSVC C++14 /W4 /WX: native1354 PASS; console1280 PASS;
Apple8-byte scalar-alignment emulation1354 PASS. Native worker default malloc,
game callback JKR opt-in, explicit heap selection, host override, exception
restoration, cross-thread isolation, audio scope nesting, and all six new forms
tested. Negative control removes16-byte floor and is rejected at compile time.
Adapter43-header audit PASS; git diff --check PASS. These are host fixtures.
CI adds Apple scalar emulation RUN plus xcrun iphoneos ARM64 C++14 syntax/static
assertion check before full game compile, catching the missed target ABI.
No local Apple SDK: actual target check/compile/link/IPA/phone retest pending.

Important source: JKRHeap.cpp; pc_host_alloc.h; dolphin_stubs/p2_os_host.cpp;
audio/jaudio_sink.cpp andjaudio_host.cpp; tests/pikmin2_native_allocator_test.py;
.github/workflows/ios-native-experimental.yml. New files contain no device IDs,
raw crash logs, credentials, assets or personal data. Raw reports remain local
in work/p2-phone-crashes and folder2/private phone report archive.

Build23 run39369282124/source609a45b1 remains compile/link/IPA SUCCESS but phone
startup FAILED. Its IPA is not a proven working app. Next P2-only build validates
this related allocation batch; no new candidate IPA or runtime evidence yet.
After success inspect new binary for16-byte w2 alignment and new UUID, prepare
verified IPA in folder1, update existing P2 with same signing identity/data,
test title/menu first. If failure, retrieve fresh matching report and diagnose
new exception/stack. Do not re-copy assets/art or touch P1 without evidence.
P1 remains existing working Build16,60FPS target; optional packs on hold; no
mid-day recovery save; online with Raye LAST. Stop idle waiting for Actions.

## Audio allocator batch dispatched - 2026-10-20 00:46 EDT

Build24: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39371370836
Exact source commit: 05e33f1c0e55dc11ecb6d413a8393bf73faeb2ce
Status at dispatch: in_progress. P2-only; P1 not scheduled. Host checks
native1354/console1280/Apple-scalar1354 pass; old8-byte-policy negative control
rejected. Real iPhone-target CI check/full compilation/IPA/runtime pending.
No idle polling. Record build result when user reports completion. Journal-only
dispatch checkpoint uses [skip ci] to avoid another build.

## Build24 P2 allocation/audio candidate SUCCESS; phone test ready - 2026-10-20 01:03 EDT

Run39371370836, job118459762543, exact source05e33f1c0e55dc11ecb6d413a8393bf73faeb2ce.
P2-only. Apple host tests, native/console/Apple-scalar allocator variants, and
the new actual iphoneos ARM64 C++14 compile/static-assert check all passed.
Full P2 iPhoneOS ARM64 compilation/link and unsigned IPA packaging succeeded.
Artifact12242386661, archive7585567bytes; compiler/linker index0 recognized errors.

IPA3824677bytes, executable11065224bytes. Verified ZIP CRC, exact P2 identity,
ARM64 Mach-O, iPhoneOS device platform, minimumOS15, load-command boundaries,
system dynamic-library paths, intentionally unsigned status, no disc assets.
SHA256 bacf33944221573fc1917de1311b5ddc328ce93b29977920f2ed7514259d9153
New executable UUID 21d95a32-9dfb-3bbb-bab8-4dd36cbc37d8
Inspected actual symbol/function instructions: ordinary new(__Znwm) and new[]
(__Znam) both pass16 in w2 to the JKR allocator. Build23 passed8 and Build22
passed4. This validates the actual target alignment correction in the produced
binary, independently of the host test. New phone crash must match new UUID;
old Build23 AudioQueue report is not evidence of this binary's failure.

Copied and hash-verified to Documents/Open Nectar/1 - Install on iPhone/
Pikmin 2 - Build 24 - Audio Startup Fix.ipa. Short START HERE/WHAT TO TEST guides updated.
Old Build23 P2 IPA/verification moved within the same project folder to folder5/
Build 23 - P2 Audio Startup Crash Reference, with unchanged SHA256. P1 untouched.

New candidate installation and startup/audio/gameplay remain UNVERIFIED.
User should update existing P2 through Sideloadly with the same identity,
preserving its data/assets/art; no asset recopy or P1 change. First test is
staying open/title/menu; then basic graphics/audio/touch/gameplay. If failure,
retrieve fresh report and confirm new UUID/exception/stack before another fix.
No phone app/file/settings operations were performed in build-result handling.
No active build or new source changes; journal checkpoint [skip ci], no extra CI.

## P2 menu clarity and original options input candidate - 2026-10-20 08:33 EDT

User resumed after shutdown. Verified origin/ios-experimental, fetched remote,
HEAD00bd0db831ce09d37c3da94e00ec5596e2256563, no divergence; only two paused
journal edits were pending and preserved. User confirms Build24 P2 OPENS on phone
and reaches menus. Main/title taps and Throw/A work. Two reported bugs: blurry,
small advanced menu; original game Options/exit-confirmation responds only to
bottom-left Back/X. Gameplay/audio/full-game stability not established by this.

Read the actual working P1 source and adapted its UI paths in P2 only:
- iPhone SDL high-DPI window flag, native-pixel menu targets independent of
  saved gameplay resolution/scale, frame-latched aspect at allocation/present.
- Keep the old logical-point gameplay pixel budget after enabling Retina;
  do not silently multiply gameplay GPU cost by3x in each dimension.
- Mobile400-high aspect-adapted menu with the same conservative iPhone margins
  as working P1; enable matching viewport/scissor and P2 DGX shim virtual sizes
  on iOS, including inverse taps. Captain-select4:3 exception remains.
- New read-only settings-open query; active game-menu touch lease also selects
  native UI rendering so original options/title/confirmation can be sharp.
  First/last transition follows the per-frame latch, not a mid-present switch.
  Font sampling remains existing linear; no texture/font replacement installed.

Original TOption had no direct touch handling. Added pane-based row selection,
explicit rumble/sound/volume/deflicker value taps through its original state,
animation/sound/saveRam handlers, virtual-stick navigation and visible familiar
Throw/A confirm. The disabled backing options never consume a modal's tap.
First Save row tap selects; second/explicit A confirms. No automatic save or
save/discard changes. JP/PAL-only hidden row0 remains unavailable in USA touch.
Confirmation already had select-then-confirm touch handling; retained that
behavior, exposed a context-only confirm control and let hit testing also use
visible row-container bounds when callback-owned text is hidden/replaced.
The row-container fallback is a source-supported candidate, not proven as the
sole cause on hardware. Expired/hidden tracked panes remain non-clickable.
Right-thumb camera gesture creation is suppressed only in these explicitly
claimed confirm menus so a slightly moving tap is not stolen by gameplay drag.
Other main-screen/gameplay button bindings remain unchanged; P1 source untouched.

Files: P2pc_window.cpp,gl/pc_gfx.cpp,settings/pc_settings.cpp/.h,touch/pc_touch.cpp/.h;
ebiScreenOption.cpp,ogMenuMgr.cpp,ogObjSMenuPauseVs.cpp; new
 tests/pikmin2_ios_menus_test.py; experimental workflow; both journals.
Build24 allocator/host-thread ownership and UIKit FBO/RBO corrections preserved.
No phone operations, signing/credential changes, assets or optional mods installed.

Local MSVC C++14 /W4 /WX actual-code fixtures: iPhone172 PASS; desktop182 PASS.
Covers native UI pixel budget vs gameplay, explicit aspect/resolution overrides,
frame latch/open-close transitions, layout and inverse taps across landscape/
portrait/fallback dimensions, confirm control lease expiration, direct option
selection/value ranges, disabled backing-menu ownership, row fallback, choice
select vs confirm, physical A/B and stale pane rejection. Host rendering/math
and state simulation only: not actual iPhone graphics/gesture verification.
Existing native allocator1354 and console1280 checks re-run PASS; adapter43 PASS.
Whitespace check PASS. CI adds iPhone/desktop host fixtures and actual iphoneos
ARM64 compile/static validation before full game compile. Apple full compile,
IPA and visual/touch hardware results for this candidate remain pending.

Next one coordinated P2-only build after committing; no P1 rebuild. Record exact
source/run; stop idle polling. On success verify IPA/identity/new UUID/alignment,
copy to folder1 and update test guide. Reinstall/update P2 only preserving data;
no asset/art recopy. Phone tests: menu readability/tabs/scroll/tap alignment,
original options rows/values/save, Continue/Don't Save selection and confirm,
Back, main-title controls, startup/gameplay/audio/camera regression. Preserve
Build24 known-opening IPA in archive. No new visual/touch fix may be called
confirmed until user reports actual phone behavior.

## P2 menu candidate dispatched - 2026-10-20 08:34 EDT

Source commit 3013d4c23035db25ba17851fe65cd2e29123830d
Build25: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39423349538
Status at dispatch: in_progress. P2 only. New Apple target/full compilation,
IPA, menu clarity and original-options touch on phone remain pending.
Local UI172/desktop182/allocator1354/console1280/adapter43 checks passed.
No idle Actions polling. Dispatch journal checkpoint [skip ci], no extra build.

## Build25 early fixture failure corrected - 2026-10-20 08:42 EDT

Build25 run39423349538, source3013d4c23035db25ba17851fe65cd2e29123830d,
job118629595502 FAILED in the new native menu test before game configure/compile.
Full job log retrieved directly: work/build25-job.log in the development session;
friendly copy: Documents/Open Nectar/2 - Progress and ChatGPT Handoff/Build 25 - Full Failed Job Log.txt.
Unique diagnostics: Clang unused-const-variable for kF1TabH, kF1OptH,
kF1OptVisible, promoted to errors by -Werror. These were imported real source
constants unused by the extracted fixture, although used by the full game.
Existing adapter/Apple library, native+console+Apple-scalar allocator, ARM64
allocator syntax and GD TLS checks PASSED. No game compile/link or IPA occurred.
This failure is not evidence of a new phone crash or a failure of menu visuals.

Correction limited to tests/pikmin2_ios_menus_test.py: meaningful geometry checks
exercise the imported metrics, checking tab/list separation and room for the
option rows in each tested layout. No warning suppressions or weakened CI.
MSVC C++14 /W4 /WX: iPhone180 and desktop190 PASS. Installed LLVM19 Clang parser
(clang-tidy with clang-diagnostic-* and warnings-as-errors) reproduced ALL THREE
original diagnostics before correction, then accepted both corrected variants.
Clang parser on Windows is not the Apple SDK/full iOS game build. The new Apple
CI/full compile and phone menu tests remain required. git diff --check passed.
No further game source, P1 app/data, startup allocator, framebuffer, assets or
signing changes. Build25 menu/source candidate remains3013d4c2, now with this
fixture correction for one P2-only retry. Do not install/retest Build24 for this
new candidate; retain its known-opening IPA until a new IPA succeeds.

P2 underlying menu findings remain: missing iOS high-DPI/native-resolution menu
path and Android-only mobile layout/shim versus working P1; original TOption
missing direct touch and game-menu confirm control not exposed. Visible row
fallback addresses potentially hidden callback text. Main/title taps and Throw/A
worked in user tests. The source candidate is implemented, NOT phone verified.

Next: commit corrected fixture and this checkpoint, push one P2-only build,
record source/run, stop idle polling. On success validate IPA and put it in
folder1 with short phone checklist. Reinstall P2 only preserving app data; no
asset/art recopy. Test clear advanced settings and tap alignment, original
options values/save, Continue/Don't Save select/confirm, A/Back, then gameplay,
audio/camera regression. Preserve P1. User involvement: none until IPA ready.

## Corrected P2 menu fixture retry dispatched - 2026-10-20 08:43 EDT

Build26, run39424440094, sourcedd5bd01557ea7f57255f869d431cd81864bca567.
https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39424440094
Status at dispatch: in_progress. P2 only, no new P1 build.
Includes menu source3013d4c2 plus the Build25 unused-constant fixture correction.
Local MSVC iPhone180/desktop190 and Clang parser both variants PASS.
Apple/full-game compilation, new IPA and phone menu behavior remain pending.
Build25 failed early test, no IPA. Build24 remains the known-opening phone build.
No idle polling; user will report completion. Dispatch documentation uses [skip ci].

## Build26 PASSED; P2 menu test IPA ready - 2026-10-20 09:19 EDT

P2-only source dd5bd01557ea7f57255f869d431cd81864bca567; run39424440094;
job118633289923; artifact12266336380. All job steps passed, including native
menu180/desktop190 host checks, actual iPhone ARM64 syntax check, existing
allocator/address/TLS checks, full game configure/compile/link and IPA packaging.
Build25's three unused fixture constant diagnostics corrected; no warnings disabled.

Downloaded artifact ZIP digest verified against GitHub metadata:
555eb99487ec310e9c9ffb795ade822fca5f9bea5f36c521653347922aa6aaac.
IPA ZIP integrity, single P2 bundle identity, ARM64 iPhoneOS device executable,
minimum iOS15, system-library load commands and unsigned state verified.
Fresh UUID0bd204c6-8a62-35ed-82e6-4ef2cfc76b14, executable11065512bytes.
Actual new/new[] ARM64 routines both still request16-byte alignment.
IPA3826605bytes SHA256ca28fbc6f423745e2babb595d1b47fac4a1222917b00c0ea61f24d23ad0325e5.
No proprietary ISO/RVZ/model/archive game assets embedded in IPA.
Copied with matching hash to Documents/Open Nectar/1 - Install on iPhone/
Pikmin 2 - Build 26 - Clear Menus and Touch.ipa, alongside verification JSON,
updated START HERE/WHAT TO TEST guide and build link. Build24 preserved.
Full successful job log in friendly folder2; full reports refreshed.

Milestones: source implemented YES; local checks YES; Apple compilation YES;
IPA YES; Build26 phone installation/runtime/menu clarity/touch verification NO.
Build24 remains last hardware-confirmed opening build. No phone operations,
P1 changes, assets/art recopy, signing changes or new build. Docs commit skip-ci.
Next user test: update existing P2 in Sideloadly with same account/ID, do not
uninstall. Check advanced clarity/tabs/scroll/tap mapping; original options
rows/values/Save; Continue/Don't Save select then confirm, visible A and Back;
then title/gameplay/audio/camera regression. No need to connect phone to Codex
unless a fresh crash report is needed. Do not call new menu bugs fixed until
actual user feedback. Wait for phone results without idle usage.

## Build26 hardware regressions and coordinated P2 fix - 2026-10-20 09:37 EDT

User Build26 phone test: title initially blurred with gameplay controls;
then sharpens and shows only Back/X, blocking advanced settings gear. Begin
campaign intermittent; third attempt entered gameplay. Pressing top-left pause
crashed. Ignore logo/flower layout differences in screenshots (opening animation).

Both fresh crashes match Build26 UUID0bd204c6-8a62-35ed-82e6-4ef2cfc76b14.
09:22:04 main thread: SIGABRT in AppleMetalGLRenderer clearBuffers -> pc_gfx_clear_depth
 -> pc_p2_captain_preview_begin -> pc_captain_select_draw_3d -> VIWaitForRetrace.
09:24:55 Metal CompletionQueueDispatch: SIGABRT OSPanic -> JKRExpHeap::joinTwoBlocks
 -> do_free -> operator delete -> AGX ResourceGroupUsage/command-buffer dealloc.
Confirms native Metal destruction reached the game heap. Likely source: missing
host routing during native graphics allocations; specific allocation site for
completion failure cannot be proven from its free-only crash stack alone.
Depth clear and numerous GL calls were unguarded; P2 VIWaitForRetrace also called
SDL_GL_SwapWindow outside pc_gfx_present's host guard. Existing native worker
thread defaults and16-byte alignment did not cover native calls on game thread.
09:20 Jetsam report contained no P2 process; no evidence it explains these crashes.
Phone settings read-only: renderScale=.666667, logical932x430, fpsMode0.
Raw reports/config are private local evidence, not committed to public repository.

Controls: title claimed touch only in interactive Wait; once it did, the menu
filter admitted Back plus help-requested buttons and explicit confirm contexts.
Title has no help icons, so gear/A disappeared at the same point native menus
became sharp. Small right-half taps could become camera gestures in generic
menus, cancelling clicks. Source supports this explanation; runtime fixes pending.

P2-only batch: restoring host-allocation scope at the beginning of all100
parsed direct-GL functions in pc_gfx.cpp (86 entries added/moved; two old inline
scope implementations unified). Includes clear depth, copy/held-frame/texture
upload/state/present helpers. Native SDL window init/swap/interval/shutdown and
narrow event-pump helper guarded. P2 VIWaitForRetrace's independent swap block
host-scoped. Preserve16-byte allocator policy, game-thread ownership, UIKit
FBO/RBO and native menu/point-budget frame latch. No JKR heap bypass for game
objects, no history rewrite, no P1 changes.

Menu filter retains Back, gear/settings and A for any active game-menu lease;
other gameplay controls still require visible context/help. Existing exclusive
modal input guards still block advanced-menu opening over their ownership.
No gameplay camera gesture begins while ANY game menu owns touch; existing
menu swipe/port scroll handlers retained. Title claims menu in OpenScreen and
Draw, not just Wait, to avoid delayed animated-title resolution/control switch.
One frame of render-context transition can still occur; no zero-flicker hardware claim.

Tests: new direct-GL scope audit (100 entries) integrated into existing allocator
fixture generation; negative control removing clear-depth guard rejected.
Actual clear-depth implementation exercised with lazy native allocations and
completion-thread frees, including nested scope restoration; native1359 and
console1280 MSVC checks PASS. Menu188/iPhone,198/desktop PASS including actual
button hitboxes for gear/A after generic menu ownership. Clang19 parser checks
for both menus and native/console/Apple-scalar allocator PASS. Includes static
checks for native SDL entry scopes, independent VI swap, title opening/drawing.
These are host mocks/parsing, not Apple graphics execution. Apple ARM64 target
compile, full game build/new IPA, phone regressions remain pending.

Candidate:not committed; not dispatched

No idle polling. Next action after successful IPA: update P2 only, preserve data,
repeat Begin selection several times, check gear/A before/during/after title
opening, advanced/original options, enter gameplay then pause/resume repeatedly.
If crash, read fresh UUID-matched report. P1 and assets/art unchanged.

## Build26 hardware regressions and coordinated P2 fix - 2026-10-20 09:38 EDT

User Build26 phone test: title initially blurred with gameplay controls;
then sharpens and shows only Back/X, blocking advanced settings gear. Begin
campaign intermittent; third attempt entered gameplay. Pressing top-left pause
crashed. Ignore logo/flower layout differences in screenshots (opening animation).

Both fresh crashes match Build26 UUID0bd204c6-8a62-35ed-82e6-4ef2cfc76b14.
09:22:04 main thread: SIGABRT in AppleMetalGLRenderer clearBuffers -> pc_gfx_clear_depth
 -> pc_p2_captain_preview_begin -> pc_captain_select_draw_3d -> VIWaitForRetrace.
09:24:55 Metal CompletionQueueDispatch: SIGABRT OSPanic -> JKRExpHeap::joinTwoBlocks
 -> do_free -> operator delete -> AGX ResourceGroupUsage/command-buffer dealloc.
Confirms native Metal destruction reached the game heap. Likely source: missing
host routing during native graphics allocations; specific allocation site for
completion failure cannot be proven from its free-only crash stack alone.
Depth clear and numerous GL calls were unguarded; P2 VIWaitForRetrace also called
SDL_GL_SwapWindow outside pc_gfx_present's host guard. Existing native worker
thread defaults and16-byte alignment did not cover native calls on game thread.
09:20 Jetsam report contained no P2 process; no evidence it explains these crashes.
Phone settings read-only: renderScale=.666667, logical932x430, fpsMode0.
Raw reports/config are private local evidence, not committed to public repository.

Controls: title claimed touch only in interactive Wait; once it did, the menu
filter admitted Back plus help-requested buttons and explicit confirm contexts.
Title has no help icons, so gear/A disappeared at the same point native menus
became sharp. Small right-half taps could become camera gestures in generic
menus, cancelling clicks. Source supports this explanation; runtime fixes pending.

P2-only batch: restoring host-allocation scope at the beginning of all100
parsed direct-GL functions in pc_gfx.cpp (86 entries added/moved; two old inline
scope implementations unified). Includes clear depth, copy/held-frame/texture
upload/state/present helpers. Native SDL window init/swap/interval/shutdown and
narrow event-pump helper guarded. P2 VIWaitForRetrace's independent swap block
host-scoped. Preserve16-byte allocator policy, game-thread ownership, UIKit
FBO/RBO and native menu/point-budget frame latch. No JKR heap bypass for game
objects, no history rewrite, no P1 changes.

Menu filter retains Back, gear/settings and A for any active game-menu lease;
other gameplay controls still require visible context/help. Existing exclusive
modal input guards still block advanced-menu opening over their ownership.
No gameplay camera gesture begins while ANY game menu owns touch; existing
menu swipe/port scroll handlers retained. Title claims menu in OpenScreen and
Draw, not just Wait, to avoid delayed animated-title resolution/control switch.
One frame of render-context transition can still occur; no zero-flicker hardware claim.

Tests: new direct-GL scope audit (100 entries) integrated into existing allocator
fixture generation; negative control removing clear-depth guard rejected.
Actual clear-depth implementation exercised with lazy native allocations and
completion-thread frees, including nested scope restoration; native1359 and
console1280 MSVC checks PASS. Menu188/iPhone,198/desktop PASS including actual
button hitboxes for gear/A after generic menu ownership. Clang19 parser checks
for both menus and native/console/Apple-scalar allocator PASS. Includes static
checks for native SDL entry scopes, independent VI swap, title opening/drawing.
These are host mocks/parsing, not Apple graphics execution. Apple ARM64 target
compile, full game build/new IPA, phone regressions remain pending.

Candidate:8d77c5337863f34800bc7b7ef990878e586d7c48; Build27/run39432157516 (in_progress at dispatch)
https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39432157516
No idle polling. Next action after successful IPA: update P2 only, preserve data,
repeat Begin selection several times, check gear/A before/during/after title
opening, advanced/original options, enter gameplay then pause/resume repeatedly.
If crash, read fresh UUID-matched report. P1 and assets/art unchanged.

## P1 optional character/model bundle INSTALLED by USB - 2026-10-20 09:52 EDT

User explicitly authorized installation; ZIP already present in P1 Documents.
Verified no running P1 process before backup, staging and promotion and after
installation. Phone ZIP SHA2567fa0bacc8f99349b0fd84d8b2a43716e91e68d033ca989c96a414a72dfc1538c,
matching prepared local bundle. ZIP integrity/path/type/size/model magic checked.
Backed up6 existing files/161965bytes: saves/card0+card1, config, original enhanced
config backup, touch layout and achievements. Existing Load Models folder empty;
no prior model files overwritten. Backup SHA256 validated locally and against
phone readback before changes. Full backup/private install manifest in:
C:\Users\chazz\Documents\Open Nectar\5 - Archives\Before P1 Character Packs - 2026-10-20 095114

Staged20 files/18360060bytes outside active Load, verified each SHA256, then
renamed only into absent destinations. No differing existing file overwritten.
Final readback SHA256 of all20 installed files PASS. All6 pre-existing protected
files remained byte-for-byte unchanged; P1 kept closed throughout. Original ZIP
preserved on phone. Recovery record retained in P1 Documents. No P2 writes,
reinstall, app signing, code or settings changes.

Content installed:15 NHM files comprising11 menu-counted HD models plus4 extra
captain choices,4 portraits and1 private source archive for existing character
recognition. HD Olimar, standard/HD Louie alternatives; red/yellow/blue Pikmin
and leaf/bud/flower; Bulborb/Dwarf Bulborb; President/White/Purple/Bulbmin extra
captains. Native loader expected11/11 counter. Read config hdModelsDisabled=0
(all model rows enabled). Do not confuse file-install verification with runtime
visual/animation/performance verification: game not launched by Codex.
Environment HD texture pack remains NOT installed (last official quota block).
P1 installed app/build and60FPS preference preserved. P2 Build27 still pending
at last dispatch; no polling/new build for this content milestone.

Next user action: reopen P1, Graphics > HD Models should show11/11, inspect
Olimar/Pikmin/Bulborbs and extra captain selector, play15-20 minutes while
watching FPS/Heat/RAM. Keep60FPS. If artifacts or slowdowns, disable affected
model rows, restart and report exact model/symptom; original game assets remain.
No further file copy or ZIP import needed. Full private record in folder2/
Pikmin 1 - Character Pack Installation.json; backup under folder5 above.

## Build27 PASSED; verified P2 crash/menu candidate IPA ready - 2026-10-20 09:57 EDT

Source8d77c5337863f34800bc7b7ef990878e586d7c48; run39432157516;
job118659675153; artifact12268693334. P2 only. All workflow steps PASS,
including100 direct-GL scope audit, native1359/console1280/Apple-scalar1359,
menu188/desktop198, actual iPhone ARM64 syntax checks, existing addresses/TLS
checks, full game compile/link and IPA packaging. No new source modifications.

Downloaded artifact ZIP digest matches GitHub metadata:
cc60012d8279edf3049dc17cddf83bb8fc7829ec8958dbc73c974a8e87020bdf.
IPA ZIP/ARM64/iPhoneOS device/min iOS15/P2 bundle/system-library loads/unsigned
state verified. Fresh UUIDaecbcead-f044-3dc2-9608-83e40dcd9540; executable11083680bytes.
Actual ARM64 new/new[] still request16-byte alignment. IPA3831561bytes,
SHA256f4a90d7da9f3b6130116caaf006b220f27b7e3a4ec17deb97b404222e0ab6b74. No ISO/RVZ/SZS/BMD game payload in IPA.
Hash-identical copy now in Documents/Open Nectar/1 - Install on iPhone/
Pikmin 2 - Build 27 - Crash and Menu Controls Fix.ipa. Verification JSON, build shortcut and simple START HERE guide
updated; folder2 full successful log and master handoff updated.

The batch targets Build26's actual phone failures: clear-depth captain-preview
abort and Metal completion-thread JKRExpHeap abort; title menu gear/A hidden
when touch ownership started, right-side menu taps lost as camera gestures.
Source fixes and tests passed; Build27 PHONE INSTALLATION/CRASH-FREEDOM/MENU
BEHAVIOR ARE NOT YET VERIFIED. Preserve Build24 allocator/thread/audio fixes,
UIKit display FBO/RBO, logical-point gameplay rendering budget and frame latch.

Next phone test: update P2 over existing app using same Sideloadly signing
account/ID; no uninstall or assets/art recopy. Check gear/A during/after title
animation, advanced settings; repeat Begin/captain selection; enter actual game
and repeat pause/resume; original Options/choice confirmation; audio/camera.
If crash, match fresh report to new UUID above. No idle polling/new build.
P1 unchanged in this result turn; its character bundle was actually installed
previously (20files/15NHM readback verified,6 protected saves/settings unchanged),
expected menu11/11; model visuals/performance still untested, environment textures
NOT installed. Keep60FPS. All private assets/backups remain outside Git.

## P2 enhancement batch locally verified - 2026-10-20 13:41 EDT

User resumed after the usage pause; no external source changes were reported.
Fetched local/remote baseline aa59864e3be6c8a6e5d9a7b4ca130861ed861e27 matches.
Build27/run39432157516/source8d77c5337863f34800bc7b7ef990878e586d7c48 passed;
user now reports P2 working so far with no crashes, with incomplete testing.
This supersedes earlier blanket Build27 phone-result-pending notes. It is not
proof of full campaign stability or of the new enhancements below.

P2 candidate:
- One-time backed-up/atomic config profile: renderScale1.0, FXAA, anisotropy4,
  subtle bloom; 60FPS; performance HUD initially on; hold-to-pluck, better
  pathfinding, idle counter, instant whistle, quick grab, no-trip, B throw
  cancellation, manual lock-on and charge. Existing active texture selection,
  saves, touch layout and unrelated settings survive. The profile marker is
  serialized; later menu choices survive restarts. Reset preserves that marker
  while resetting actual settings, so the preset does not silently reapply.
- chainActions and throwWhileMoving are also compatible profile keys, but the
  active P2 decomp does not consume these two getters. P2 already invokes nearby
  AI work on completion and calls control during throw states; no new AI hooks
  were added. Do not advertise either key as a newly implemented P2 mechanic.
- Performance HUD in Display: render submissions FPS, average/p95/p99 frame
  times, process RAM, advisory available memory, process CPU (100%=one core),
  categorical thermal state and Low Power. It measures actual SDL swaps,
  samples OS counters once/second, and skips sampling when disabled. It hides
  during advanced settings/captain selection. No GPU percentage or temperature.
- Native Files ZIP picker for P2 texture packs. Reuses the existing bounded,
  CRC-checked P1 extractor and staged transactional install/rollback code.
  CMake removes the old P2 converter source to prevent duplicate symbols.
  UIKit callbacks/bridge/worker have restoring native allocation scopes; the
  P2 game allocator and recent GL100/SDL/thread/audio protections remain intact.
  P1-specific model kinds are rejected for P2. P1 game source not changed;
  shared picker changes are gated, with P1 regression coverage.
- Workflow adds P2 profile/HUD/bridge/ZIP/rollback and actual CMake-wiring/reset
  checks before compiling. Only P2 will build via [ios-p2-only].

Source files: ios/pikmin2_ios_profile.h; ios/ios_storage.mm (P2 atomic config);
ios/CMakeLists.txt (P2 features and shared portable sources); ios/ios_mod_picker.mm;
ios/pc_ios_mod_bridge.cpp; games/pikmin2/pc_port/settings/pc_settings.cpp/.h;
games/pikmin2/pc_port/dolphin_stubs/p2_os_host.cpp. New tests: pikmin2_ios_profile_test.cpp,
pikmin2_ios_mod_bridge_test.cpp, pikmin2_ios_enhancements_test.py.

Local checks PASS: profile188; shared HUD30 with P2 includes; P2 bridge24;
P1 bridge19 and profile169; transactional install/backup/active-pack protection/
invalid data/rollback; real ZIP stored/deflate/CRC/paths/duplicate/failure tests;
actual reset execution; actual extracted CMake feature branches configure for
P1 and P2. Existing actual allocator native1359/console1280/Apple-scalar1359;
GL audit100; iOS menu188/desktop198; Clang parser for allocator three variants,
menu two variants, new profile/bridge/reset all passed. Local Windows compiler
checks do not compile UIKit or establish Apple ARM64 linking/runtime behavior.

P1 content update: user installed texture ZIP and screenshot lists GPI Inactive,
Loader off. Advised select GPI/A to activate, accept restart/full restart.
Activation/texture replacements/FPS/heat after activation not yet confirmed.
Previously installed character bundle:20 files/15NHM/4portraits/source archive,
readback SHA256 verified;6 preexisting save/settings/layout/achievement files
unchanged; backup in folder5/Before P1 Character Packs -2026-10-20 095114.
Model visual correctness remains unverified. P1 gameplay/menu/camera/audio
remain user-confirmed; no P1 app/data operations in this enhancement turn.
P1 texture ZIP SHA256 5d9254b4f1ca46fee93b57ce17e888521884634bc1fae4bc7a4cf22af7e2551b;
previous no-threat Defender plus full ZIP/PNG structural check is not a runtime
or absolute security guarantee. Keep60FPS; 120 canceled; online co-op remains last.

P2 needs its own compatible texture pack (upstream launcher Drive ID
1blzsLSFBr617h-gP7lvp_7HqsLRyQWzl, advertised1072944206bytes, folderGPV).
No P2 HD texture/model content downloaded or installed in this batch; importer
support and graphics defaults are separate from content installation. P1 GPI
pack/models cannot be treated as installed P2 content. No automatic phone changes.

NEXT: commit/push this coordinated P2-only candidate; record exact source/run;
stop idle polling per user. Once user reports completion, retrieve job/logs,
verify IPA ZIP/plist/ARM64/UUID/alignment/digest and copy to friendly folder1.
Retain Build27 working backup. Update existing P2 via same signing identity/ID;
do not uninstall or touch P1. Hardware test: title gear/A; repeat Begin and
captain selection; pause/resume; original Options; HUD toggle and 60FPS; 15-20min
FPS/frame/RAM/heat test. Then separately choose/import/enable a P2-specific pack,
restart and inspect replacements/counters. Retrieve matching fresh crash report
read-only if regression. No new source fix is claimed hardware-verified yet.

## Build 28 P2 enhancements dispatched - 2026-10-20 13:42 EDT

Source commit: 386771cabe6366b0788091f4d6d63f9ef6850c67
Run: 39468391460 / Build 28
URL: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39468391460
Observed status at dispatch: in_progress; conclusion/IPA pending.
Only P2 selected via [ios-p2-only]. Source and local tests summarized in the
preceding enhancement entry. No P1 app/data changes, no P2 content installation.
Local source push succeeded; source includes both game journals. This dispatch
checkpoint uses [skip ci] and does not start another build. Stop idle GitHub
polling per user; user will report completion. On return fetch/inspect this
exact run before new code edits, retrieve full logs/artifact, verify and stage
IPA only after success. Do not claim this candidate hardware-verified.

## Build28 failure reviewed; texture-import API correction verified - 2026-10-20 13:59 EDT

Build28/run39468391460/job118785702425/source386771cabe6366b0788091f4d6d63f9ef6850c67
FAILED in full native game compilation. Adapter, Apple allocator/TLS/addresses,
menu/input, enhancement profile/HUD/bridge/ZIP/rollback/CMake/reset preflights,
and real iPhoneOS configuration all passed. Packaging skipped; no IPA produced.
Full job log retrieved, full artifact ZIP digest/CRC verified. Artifact12286432727
contains only ios-build.log and ios-build-errors.md. Error index and full log
show exactly2 compiler diagnostics, one root cause, in settings line2900:
undeclared pc_texpack_active_pack; secondary incompatible vector/string operand
from Clang's suggested correction. No linker stage was reached, so successful
linking is still unverified.

This was an incorrect API name introduced in the new P2 iOS texture-import menu.
P2 already provides const std::string& pc_texpack_selected_pack(void). Replace
only that call with pc_texpack_selected_pack().c_str(); keep runtime enabled-state
check and '*' protection when all packs are indexed. Use the renderer's selection,
not sConfig/sPending, because menu changes do not rebuild the live index until
restart. P1 game/app/data and P2 Build27 working baseline are unchanged.

Added real boundary regression to tests/pikmin2_ios_enhancements_test.py. It
extracts actual texturePacksRowAction plus actual renderer enabled/selection
getters, compiles against real P2 texture-pack and iOS bridge headers, and tests
19 cases: disabled runtime; named pack; pending/config changes since startup;
all-indexed mode; busy/reentry; bridge refusal; activate/deactivate/save/restart
semantics. Only graphics SDK declarations are bypassed in the portable fixture.
Local MSVC strict compile/execution and Clang strict parser PASS. Negative
control recreating Build28's exact call fails as intended. Actual CMake P1/P2
feature wiring also reconfigured successfully. The previous broad candidate
preflights just passed on Apple in Build28; no unrelated changes were added.
Experimental P2 preflight now executes this boundary fixture before full build.

Next: commit/push correction+test+journals as one P2-only retry, record actual new
run/source, stop idle polling. No new IPA/phone fix claimed until verified.
Keep60FPS and complete enhancement batch; no need to rebuild P1 or reinstall assets.
P1 user screenshot now shows60.2FPS/16.60ms,1715MiB appRAM,CPU39%onecore,HeatNominal;
user says texture pack enabled but visual change uncertain. Replacement counter
screenshot requested; activation/render replacements remain unconfirmed. No P1
phone writes. P2 HD texture/model content still not installed by this batch.

## Build29 P2 retry dispatched - 2026-10-20 14:00 EDT

Source 7f7d0783e8b42870a8b6bbb1954199fbe9ffc6bb; run 39470849443/Build 29.
URL: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/39470849443
Observed in_progress at dispatch. Local correction/API-boundary19 checks,
negative control and Clang PASS; Build29 Apple result/link/IPA/runtime pending.
Build28 had2 compiler diagnostics from1 incorrect API name; no IPA. Retain the
full enhancement batch and working Build27 backup. Only P2 builds. No P1 changes
or phone operations. Stop idle polling; user reports completion. On return inspect
this exact run, full logs/artifact, and only stage verified successful IPA. Docs
checkpoint uses [skip ci]. Logs and self-contained handoff saved in folder2.

## P1 HD texture runtime confirmation - 2026-10-20 14:07 EDT

User supplied an in-game Texture Packs screenshot: GPI Active; Loader1460
textures indexed (0dds,3046png);354 replaced,455 not in pack,0 failed.
The live successful-upload counter confirms texture replacement is working,
superseding earlier activation/replacement-unconfirmed notes. The455 misses
fall back to original textures and are not load failures. The count records
successful replacement uploads, not necessarily distinct textures. Screenshot
is from actual P1 gameplay, day2. User previously reported little visible
difference on the small phone screen; visual preference/model correctness and
long-session performance remain separate. Prior screenshot60.2FPS/16.60ms,
1715MiB RAM,CPU39%of one core,HeatNominal was a snapshot, not a sustained test.
No code or phone changes needed; leave GPI enabled. P1 model file installation
was previously verified but this texture counter does not verify model visuals.
P2 Build29/run39470849443/source7f7d0783e8b42870a8b6bbb1954199fbe9ffc6bb remains
pending at last observation; not polled. Only documentation changed [skip ci].

## Build29 success; verified P2 enhancements IPA staged - 2026-10-20 14:31 EDT

User confirmed success, then API/logs/artifact independently verified.
Source7f7d0783e8b42870a8b6bbb1954199fbe9ffc6bb; run39470849443/Build29;
job118794209786; artifact12287084885. P2 only. All intended workflow steps passed,
including new19-case real import-menu/API boundary; profile188/P2bridge24/P1bridge19/
HUD30/transaction/ZIP/reset/CMake, allocator1359/1280/Apple-scalar1359, menu188/198,
actual iPhone ARM64 allocator/menu syntax, headers/addresses/TLS, full compile/link
and IPA packaging. Full logs retrieved;0 distinct compiler/linker error lines.
Artifact ZIP SHA25669b13b4db9a885c711ddd2dc08aacf59bba2974e677afcb189e45263d2a7f50e
matches GitHub metadata; ZIP CRC pass. IPA integrity/plist/P2 bundle/ARM64/iPhoneOS
min15/system-only library loads/unsigned state verified; fresh UUID
03e1bc57-bc1e-356a-a65b-6474b990b91c. Actual ARM64 new/new[] both retain16-byte alignment.
IPA3897973bytes; executable11221000bytes;
SHA256429b2f4011e82cee0d8b879bf3bfc271c93c382c1c33d461f2c8a9a7c8ce1871. No proprietary ISO/RVZ/SZS/BMD payload found.

Hash-identical verified IPA copied to Documents/Open Nectar/1 - Install on iPhone/
Pikmin 2 - Build 29 - QOL Graphics and Performance.ipa. Clear START HERE/WHAT TO TEST guides, verification JSON and build
shortcut updated. Build27 backup retained; no app installation/uninstallation,
phone file writes, asset/art recopy or P1 modifications occurred in this turn.
New Build29 PHONE INSTALLATION/60FPS/QOL/HUD/menu/import/runtime tests pending.
Separate P2 HD texture/model content not downloaded/installed; this IPA adds
preset and ZIP import support, not a content bundle. Next user updates existing
P2 using same signing account/ID, tests menu/Begin/pause, controls/audio/HUD,
then screenshot stats and sustained play. Obtain compatible GPV textures later.

Future online co-op design agreed and recorded in ios/ONLINE_COOP_DESIGN_NOTES.md
and folder2/Future Online Co-op - Agreed Design.md: together-only host campaign,
shared progress/inventory, own screen/squad/allowance; forced group area/cave
travel acceptable; health-first difficulty, selected extra encounters only after
performance/stability evidence; reconnect/pings/phone interruptions/backups and
independent graphics accepted. No online implementation begun; remains last.
P1 texture uploads already screenshot-confirmed354 replaced/0 failed; P1 untouched.
