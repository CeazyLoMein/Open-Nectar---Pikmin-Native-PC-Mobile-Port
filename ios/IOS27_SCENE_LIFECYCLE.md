# iOS27 scene lifecycle: confirmed startup regression and migration

## Evidence

P1 Build44 source5f09f653b26d821079642ad23237c88ccd87b73d passed compilation and packaging, then failed on the phone before game entry. Three reports captured2026-10-23 at09:09:45/47/49 EDT have executable UUIDb0e12e37-9091-3a54-b3ac-27222d5013b1 (exact44 match), EXC_BREAKPOINT/SIGTRAP, main-thread top frame ___UIApplicationEvaluateRuntimeIssueForNoSceneLifecycleAdoption_block_invoke. This is positive evidence of UIKit's scene-lifecycle enforcement, not a guessed asset/audio/save problem.

[Apple TN3187](https://developer.apple.com/documentation/Technotes/tn3187-Migrating-to-the-UIKit-scene-based-life-cycle) documents the required migration with the new SDK. The previously selected SDK27.1 requires scenes; the bundled SDL2 had only UIApplicationDelegate startup. [Current upstream SDL scene entry](https://github.com/libsdl-org/SDL/blob/main/src/video/uikit/SDL_uikitappdelegate.m) was inspected as a reference. This project retains SDL2 and marks its own guarded backport; no broad SDL3 or engine migration.

P2 Build45/run39958190774/source dd5683cec866d7f96f6fe5dcc2321b2d8426a088/job120429205992 passed native compile/link/IPA, confirming the JSGGetName const correction. Its actual IPA also lacks UIApplicationSceneManifest; hold installation due shared startup exposure. P2 phone failure is inferred, NOT tested.

## Implemented source

- ios/sdl_scene_support.cmake sets NECTAR_IOS_SCENES privately on the bundled SDL2 for production and simulator probe. Other platform/legacy SDL paths stay guarded.
- Info.plist declares one application UIWindowScene/NectarSDLSceneDelegate, multiple scenes disabled. Original IDs, iOS15 minimum, landscape-only and ProMotion/player-controlled120 selection remain.
- SDLUIKitDelegate performs process setup only. NectarSDLSceneDelegate connects the scene; an initial scene-owned launch window is created before queueing game entry. Scheduled/entered guards reject duplicate/reconnect entry. Existing SDL game window reattaches on reconnect; no campaign reinitialization.
- UIKit_CreateWindow creates the actual SDL game window with initWithWindowScene and records it on scene.delegate.window. Initial layout uses native-window bounds; subsequent frame queries use current scene/window bounds instead of global status-bar orientation. View traits supply Retina scale. No framebuffer bind/present algorithm changes.
- SDL lifecycle observer uses filtered scene activation/background/foreground notifications instead of duplicate app notifications. Termination/memory warnings remain process notifications. SDL audio interruption-recovery and optional Steam-controller reconnect observers use scene notification names in the opted-in target; game audio/DSP/input logic unchanged.
- Cold file URLs queue until the SDL loop starts; live scene URL callbacks forward to the existing drop-file path. Picker already locates the active scene's key window.

## Validation

Local:20 contract/metadata/wiring checks including missing-key negative controls PASS;39 actual original bundle/identity/storage configure checks PASS;6 icon scope/copy/negative controls PASS; Python runner/guard syntax PASS. The exact crashing44 app is rejected by the new package guard for missing scene manifest. These host checks are NOT native compilation/runtime evidence.

Experimental CI: shared scene-startup job first builds an asset-free iOS simulator app using the same SDL2/helper/plist as production. It must actually launch on iOS27, attach a landscape SDL window to NectarSDLSceneDelegate, retain one entry/window after duplicate/reconnect callbacks, ignore foreign scene events, background/resume the same process with one notification per transition. Both full game jobs depend on this gate. Logs/results archived even on failure. No proprietary game assets or iPhone credentials needed.

Each packaged game must also pass ios/verify_scene_bundle.py: valid manifest plus compiled scene class/connect selector/entry-guard markers. A plist-only declaration cannot silently satisfy that package check.

Apple simulator execution, full native rebuilds, new IPAs and phone results remain PENDING. Simulator probe validates startup/window/lifecycle, NOT game graphics/audio/performance/assets/full campaign. It uses a generic SDL window and does not exercise the real GLES game renderer. Phone checks after a verified new IPA: launch first; menus/touch/clear graphics; lock/background/resume with audio; settings/120 persistence; both landscape sides and Duo views; normal following remains separate from true-stuck teleport.

## Recovery and privacy

P1 crashing44 IPA is marked .ipa.DO-NOT-INSTALL in folder1 and byte-identical archive preserved under folder5/P1 Build44 - Launch Failure. Pre-SDK P1 Build42 IPA remains available unchanged, SHA256304ac9abd4c60d96d76eb95902a0716ab743a074b1c69003aad238f7f7efd6a1. Do not uninstall/reset/reimport assets to address this launch failure.

Private three crash reports + summaries + installed-identity JSON are in workspace work/p1-build44-launch-20261023-091109 and friendly folder2/P1 Build44 - Private Startup Crash Evidence. No phone writes. First Documents root read denied; corrected /Documents/pikmin1 read later returned AppNotInstalledError on the then-current connection. No current settings/save/asset backup claimed. Phone need not stay connected or game open for builds. Do not upload private reports/assets.

## Dispatch checkpoint

Build46/run39991097065, source0f61ee4163ea4b47f668f50ed1f1e3511149b3bd, startup gate job120542742441 IN PROGRESS at dispatch. Both full games depend on this gate. No simulator/native/IPA/phone result yet for this source. Do not poll while waiting; user reports completion.

## Build46 compile failure and correction

Run39991097065/source0f61ee4163ea4b47f668f50ed1f1e3511149b3bd startup job120542742441 FAILED compiling the actual SDL_coreaudio.m. Exactly two compiler errors: UISceneDidActivateNotification (line494) and UISceneWillEnterForegroundNotification (line504) undeclared. One root cause: SDL_coreaudio.h imported the narrow UIApplication.h; it did not import UIScene.h. Earlier static tests checked notification names but missed declaration ownership. Simulator runtime did NOT run; both downstream game builds SKIPPED, no IPA.

Correction: import UIKit/UIScene.h in SDL_coreaudio.h inside existing iOS branch, guarded by NECTAR_IOS_SCENES && !TARGET_OS_TV. macOS/tvOS/legacy opt-out retain prior includes. Other scene notification users audited: UIKit appdelegate and iOS HID already import full UIKit.h. No DSP, input, rendering or FPS logic changed. Local24 contract/dependency checks PASS including missing-import rejection. Native compilation/runtime remain pending; real simulator gate retained without bypass.

Complete diagnostic artifact12517803044 contains only ios-scene-build.log; ZIP SHA2566710fccadf47fccf23b7a6eb76c9d2bd73597f0b3d0a408aa430d42878165602 verified, entries CRC-tested. Full job/log/verification retained privately in workspace and friendly folder2. P144 remains withdrawn and P245 installation held.

Correction dispatch: Build47/run39992850789, source2034e139369df84f61fd499d0d085b4e567b1d78, startup job120548733186: dispatched, no result yet. Stop idle polling; await user completion report.

## Build47 native compilation passes; startup readiness unresolved

Run39992850789/source2034e139369df84f61fd499d0d085b4e567b1d78/startup job120548733186 compiled the actual bundled SDL2 and asset-free probe successfully.46 header correction is natively compile-validated. simctl returned process45203 on iOS27.0/iPhone18Pro, then the readiness check timed out with last report={}. No JSON or crash stack captured. Console has UIKit assertion records rendered <compose failure>, insufficient to identify their cause or prove a crash. Full game job120552988929 SKIPPED; no game IPA.

Artifact12518747847 SHA256283b2e4f18569a26afd4e3d1f1835adf86faab47a7b11b886d370c8690354afa digest/CRC verified. Contains only build log and decoded console. Full evidence copied privately to workspace/friendly folder2. This batch does NOT claim a startup fix: it adds earliest process/SDL/window/reconnect progress JSON, raw stderr/stdout and Objective-C exception/stack capture, actual probe/app metadata/available symbols, recent own-process crash files, explicit failure stage and independent diagnostics/cleanup. Resolves data container before launch and selects newest installed iOS27 runtime (27.1 present); probe lives180s to cover slow orchestration. No assertion/gate weakened, no algorithmic platform/gameplay change; production has launch markers only.

9 host runner regressions PASS plus24 metadata/dependency checks PASS. Host runner fixtures are not native startup proof. New diagnostic compilation/runtime pending. Retain strict single-entry/window/resume/foreign-scene assertions and both-game dependency.

References reviewed: [SDL official scene entry](https://github.com/libsdl-org/SDL/blob/main/src/video/uikit/SDL_uikitappdelegate.m), [Apple crash/log collection](https://developer.apple.com/documentation/xcode/acquiring-crash-reports-and-diagnostic-logs). Their patterns inform diagnostics, not proof of a cause for47.

Diagnostic dispatch: Build48/run39995580595/sourced8327ffd5ae114b4617c824c1bfacbd689d2d58c/startup job120558124436 dispatched; last observed in progress, no result yet. No idle polling.

## Build48: synthetic notification test caused the exception

Run39995580595/source d8327ffd5ae114b4617c824c1bfacbd689d2d58c/startup120558124436 compiled the real SDL2/probe successfully. On iPhone Duo/iOS27.1, entry_count1, valid NectarSDLSceneDelegate-owned window, landscape678x466 and duplicate-main/reconnect preservation were observed. The test then globally posted UISceneDidActivateNotification with NSObject as object. Apple's _UIRemoteKeyboards sceneDidActivate: observer called _sceneIdentifier on that invalid object; raw stderr and captured exception stack CONFIRM NSInvalidArgumentException in scene_main's synthetic negative test. It never reached ready/background-resume. Both game builds SKIPPED/no IPA.47 used the same code, so same cause is inferred there, not independently stack-proven.

Artifact12520446669 SHA256acc4f499de272af88586d50cd096a18a02720a3d31e6e9f17a25b0e37689c078 digest/CRC verified; exact built probe contains SDL_LifecycleObserver and nectarSceneLifecycle: markers. Retained raw output/phase/stack/probe/plist privately in workspace and friendly folder2. Diagnostics succeeded; no longer treat48 cause as unresolved.

Correction is TEST-ONLY: use NSClassFromString to instantiate the actual SDL lifecycle observer implementation, require its nectarSceneLifecycle: selector, construct NSNotification objects and invoke that method directly for foreign-event rejection. Do not send fake system lifecycle events to Apple's unrelated observers. The real registered observer is still tested via actual simulator background/resume. Strict readiness/one-entry/window/landscape/filter/event-count checks retained.26 contract checks include old-broadcast negative rejection;9 host runner tests PASS. Production SDL lifecycle/game/render/audio/FPS/save code unchanged. Correction Apple compile/runtime/game/hardware pending; partial generic-window startup is not a full game result.
