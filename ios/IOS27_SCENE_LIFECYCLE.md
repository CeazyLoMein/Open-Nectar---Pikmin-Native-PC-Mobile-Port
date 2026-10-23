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
