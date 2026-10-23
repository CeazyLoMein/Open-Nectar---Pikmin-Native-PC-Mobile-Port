# Adaptive landscape display and frame-rate choice

Current source intent: both games use the current SDL drawable and UIKit view safe area, with no device-model sizing table. Landscape left/right remain the supported orientations. The advanced menu expands its virtual height on less-wide windows to retain readable columns while matching the available aspect ratio. Controls anchor inside safe bounds; the editor reverses the same mapping. A resize does not rewrite saved controls. Active touches are released when geometry changes to avoid stale held inputs.

3D resolution remains player-controlled. A saved resolution changes only the internal render budget on iOS, never the UIKit window. Automatic aspect follows the current drawable; an explicitly selected aspect ratio can intentionally retain bars. Existing framebuffer presentation, full-resolution settings rendering, game HUD/cutscene projection and audio/gameplay are retained.

30,60,120 and monitor-rate selections remain available. The iOS package opts into ProMotion using CADisableMinimumFrameDurationOnPhone; bundled SDL already supports CADisplayLink high-refresh ranges. This permits high rates, it does not promise sustained120. Existing selected FPS is preserved; no fixed60 cap or forced120 default is introduced.

## SDK and evidence

- [Apple Duo preparation](https://developer.apple.com/iphone-duo/prepare/): old SDK compatibility windows limit usable display; SDK27.1 enables full display. App code must still adapt and be tested.
- [GitHub runner labels](https://github.com/actions/runner-images/blob/main/README.md): standard xcode-27 ARM64 host.
- [Installed Xcode/SDK inventory](https://github.com/actions/runner-images/blob/main/images/macos/xcode-27-arm64-Readme.md): /Applications/Xcode_27.1.app currently points to installed27.1 RC. Pin this path and assert SDK>=27.1. Minimum OS remains15.0; actual build is required to confirm new toolchain compatibility.

1778 actual-code P1/P2 layout/editor/native-size-query/render-budget checks pass locally with MSVC and Clang, plus existing409 iOS/302 desktop menu checks,39 identity/storage and6 icon checks. Prior fixed menu fails the new regression. Host geometry is simulated; UIKit code, live fold/unfold, game HUD framing and actual120 output remain unverified until Apple CI and phone tests. SDL's legacy UIKit lifecycle is retained; if live folding fails, use actual geometry/device evidence before changing its lifecycle.

## Phone checks after verified IPAs exist

1. Update existing app using the same signing account; keep settings, saves and assets. Do not uninstall.
2. Check title/game/advanced settings in landscape left and right. Every visible control should respond at its drawn position, away from cutouts/home area.
3. On Duo check both displays: close/reopen or fold/unfold while paused, then check clear menus, aspect and controls. Re-touch controls after resizing (old touches are intentionally released). Check unpaused resizing only after pause test works.
4. Move a button in the layout editor, close/save, reopen; confirm its touch target. Switch display and back; confirm no saved-layout drift.
5. Select120 FPS if desired, close/reopen settings, confirm it stayed selected, and observe Performance HUD output in gameplay. Also confirm lower-rate choices still work; do not infer sustained120 from a smooth-looking screen alone.
6. P1: normal movement/box descent remains a separate Build42 test; automatic teleport remains explicitly untested. P2: briefly confirm Pikmin/enemy/wind audio, captain movement and menus before longer play.
