# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-23 09:03 EDT

**Overall project status:** Build44 P1 native/link/package PASSED and unchanged original-ID IPA VERIFIED/READY in folder1. Build44 P2 compilation FAILED: one unique virtual return-type error repeated6 times. P2 correction implemented and local regression PASS; P2-only retry next. New display/120 FPS phone results PENDING. Landscape only; player controls FPS including120; no forced60 cap.

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
- Latest commit: P2 correction prepared; source SHA and new run to be recorded immediately after push.
- Commits created: P2 fix/test/journal commit pending.
- Changes pushed: None yet in this follow-up. Intended marker [ios-build] [ios-p2-only] avoids redundant P1 build.
- Uncommitted changes: Scoped two-file P2 fix, regression, experimental workflow and journal; no unrelated/user files or private materials staged.
- GitHub Actions run IDs:44=39950748289 combined FAILURE; P1 job120404306153 SUCCESS, P2 job120404306409 FAILURE. Duplicate43 cancellation was accepted202 previously. P2-only retry pending.
- Build results: P1 native/link/IPA44 PASS. P2 native44 FAIL at override type; local correction PASS, new native pending. No hardware validation this follow-up.
- Artifacts produced: P1 IPA C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\Pikmin 1 - Build 44 - Adaptive Landscape and 120 FPS.ipa; SHA25649db612ed3944dcff30b5f60a93bf16ad187f343fa47cbd1a53fa38f7b8dd636. Artifact ZIP SHA256e7a47fbacdb70cfb76f0089d007bccf68573d339f7c01b269329cac926d4249c; UUIDb0e12e37-9091-3a54-b3ac-27222d5013b1. P2 full failure ZIP3,630,733bytes SHA2560213111c9d63a0669877df39b7d2154c7de25f5b65fad92b6939a91e4fa5331d; no IPA. Older42 and32 baselines/backups retained.

### Next steps

- Next Pikmin 1 task: Update existing app using the verified44 IPA and same signing account. Read folder1/Build44 - P1 Ready and Test Steps.txt. Test menu/control alignment on both landscape sides and Duo displays, optional120 persistence and Performance HUD output. Test ordinary following separately; do not call teleport verified unless a truly stuck follower visibly relocates.
- Next Pikmin 2 task: Finish P2-only retry; inspect full logs/artifacts on completion and fix actual remaining failures if any. No repeated relaunch/reset of working app needed.
- GitHub/build task: Push scoped P2-only retry, record exact source/run/jobs, then stop idle polling per user. No P1 rebuild.
- Anything requiring my involvement: P1 phone test when convenient; phone need not remain connected. User reports P2 retry completion. No P2 installation yet.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Both games' adaptive-display batch is source5f09f653. P1 passed44; P2 failed due a legacy shared cutscene-name declaration, unrelated to assets. Current P2 fix is type-correct and preserves returned name pointer/virtual slot. No guessing about audio or runtime. FPS user-controlled with120 enabled, landscape only. Autosave/online plans remain deferred.
- Important source-file locations: ObjectSystem.h:20, JSTObjectSystem.cpp:JSGGetName ~685; base include/JSystem/JStage/TObject.h:12; siblings ObjectActor/ObjectCamera. Shared display bridge ios/ios_display.mm and pc_mobile_layout.h remain unchanged. ios/IOS_ADAPTIVE_DISPLAY.md contains design and phone checklist.
- Relevant logs: work/build44-p2-full.log (complete job); outputs/Build44-Pikmin2/ios-build.log and ios-build-errors.md; work/build44-p2-errors.json (1 unique/6 occurrences); work/p2-jstage-negative.log; work/build44-jobs-final.json,build44-artifacts.json,build44-run.json; work/build44-verification.json. Friendly folder2 has P2 full failure ZIP/error JSON, P1 full successful log/verification and this handoff. Private downloads/logs never committed.
- Unverified fixes: New P2 const return correction native/link/IPA/runtime; P1/P2 display/folding, actual high-refresh output and all unresolved prior runtime behaviors. Successful host fixtures are not full-game or phone proof.
- Risks and warnings: New SDK can expose further legacy incompatibilities; actual make -k log currently shows only this one. Do not reset either installed app or upload game assets. Keep P1 passed44 available independently of P2 retry. SDK native window lifecycle/folding requires real device evidence. No spoilers.
- Exact next actions: Commit/push P2-only source with [ios-build] [ios-p2-only], record exact retry run and update dispatch notes [skip ci]. Stop waiting on CI; user reports completion. On success verify original-ID unsigned ARM64 P2 IPA incl SDK27.1/ProMotion/landscape metadata and icons; place in folder1, alert user, give targeted tests. On failure use complete actual log, group unique errors before changes. Independently receive P1 test44 feedback.

**END PROGRESS REPORT**
