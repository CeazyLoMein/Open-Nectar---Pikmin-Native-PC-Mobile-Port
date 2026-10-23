# Build44 results and P2 correction

Source5f09f653b26d821079642ad23237c88ccd87b73d, run39950748289. P1 job120404306153 passed compilation/link/IPA; P2 job120404306409 failed compilation.

P1 exact GitHub IPA verified unchanged, original standard ARM64 iPhoneOS bundle, SDK27.1.0, minimum15.0, landscape-only, ProMotion permission present. SHA25649db612ed3944dcff30b5f60a93bf16ad187f343fa47cbd1a53fa38f7b8dd636. Staged in accessible folder1. Phone tests PENDING.

P2 full log: ONE unique compiler error SIX occurrences, ObjectSystem.h:20 returns char* overriding const char* base TObject.h:12. All preflight checks passed; linking/package not reached. Affected including files: baseGameSection.cpp, JSTFindCreature.cpp, JSTObjectParticleActor.cpp, JSTObjectSystem.cpp, moviePlayer.cpp, moviePlayerAudio.cpp.

Correction: both ObjectSystem declaration and implementation return char const*, matching base, sibling actor/camera and stored mName. Return mName without const_cast. No change to name contents, pointer value, virtual slot or audio/input/render/save behavior.

Regression extracts actual base/system/actor/camera signatures and actual base/system bodies.4 compile-time type assertions +3 direct/base-pointer const/null name cases PASS with MSVC/C++14 and Clang. Original source fixture fails compilation on the same override mismatch. CI runs this before the full P2 native build and syntax-checks the real ARM64 iOS target. Full native retry still required; no P2 IPA or runtime result claimed.

P2-only retry uses [ios-build] [ios-p2-only]; retain successful P1 artifact. See current progress report for exact new run when dispatched. No idle CI polling. Full P2 failure artifact ZIP and unique-error JSON saved in folder2; full raw job log remains private workspace work/build44-p2-full.log.
