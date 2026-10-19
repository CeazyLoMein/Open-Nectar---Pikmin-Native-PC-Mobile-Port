# Pikmin 1 iPhone improvements

The iPhone user confirmed that Build 10's settings menu is substantially more
readable and the camera controls work. This is a limited play test, not a full
game completion or validation of every optional feature below.

## First enhanced profile

Source implemented and local host checks passed. Full iOS compilation and
phone validation are still required for these enhancements.
Apply once; later menu choices remain the player's own choices.

| Area | Existing upstream feature selected | Initial value |
| --- | --- | --- |
| Clarity | Internal scene resolution | 1.0 logical resolution |
| Clarity | FXAA antialiasing | On |
| Texture clarity | Anisotropic filtering | 4x, subject to driver support |
| Lighting | Bloom | Subtle |
| Pikmin tasks | Chain actions and Better Pathfinding | On |
| Plucking | Hold to Pluck | On |
| Squad management | Idle counter, Instant Whistle, No Tripping | On |
| Throwing | Quick Grab, cancel with B, throw while moving | On |
| Targeting | Manual Lock-On and Charge | On; requires accessible action controls |

Existing FPS mode, camera/gyro/bindings, health, day length, Pikmin limit,
story behavior, colour preferences and saves are preserved. A fresh config
retains the engine's default 30 FPS. Increased scene resolution and effects
still need thermal, performance and battery testing on the phone.

## Available but not selected by this profile

The source already includes additional graphics, gameplay, randomizer, speedrun,
local co-op and optional rule settings. These are not evidence that every path
is working on iOS. In particular, higher FPS modes remain experimental and
heavy graphics effects should be tested separately.

## Optional HD assets

Texture and model loaders are already in the iOS build. HD texture packs and
replacement character meshes require separate files; they are not included in
the app or repository. Upstream mobile texture packs are large. Do not enable
4K replacements before measuring phone memory and performance.

Data locations in the app's Files directory:

- `pikmin1/Load/Textures/GPI`: extracted texture replacements.
- `pikmin1/Load/Models`: supplied model source ZIPs/folders or converted packs.

The Texture Packs and HD Models install actions now open a native Files ZIP
picker on iOS. Texture ZIPs containing Load/Textures keep their pack folders;
other texture ZIPs use their filename as the pack folder. Models accept the
original supported Collada/PNG source ZIP for the chosen row. No downloaded
replacement assets are bundled. Importing stages files before replacement,
protects active texture folders, and keeps originals and RECOVERY.txt under
Load/.ios-import/<transaction>/previous. Restart before applying a new pack.
A crash during a multiple-folder replacement may require recovery from that
record. Failed staging is retained; inspect it before deleting backups.

## Final milestone: online co-op

The user's final goal is to play both native iPhone games online with Raye.
Keep this as the last milestone after independent game stability, graphics,
controls and saving are verified. Existing upstream networking code or planning
documents do not establish that online iPhone co-op currently works.

## Validation and recovery

The portable profile transformation passed 169 C++17 checks with MSVC `/W4 /WX`.
This checks text migration, duplicate handling and preservation of unrelated
settings; it does not compile or run the full iOS renderer. The caller must back
up the original config, write the migrated config atomically and persist the
profile marker through ordinary settings saves. The integrated storage code backs up the existing config to
`pikmin_settings.before-ios-enhanced-v1.conf` and writes the new one atomically.
To undo the whole profile, close the app, restore that backup as
`pikmin_settings.conf`, and add `iosEnhancedProfile = 1` so the migration is
not reapplied. Individual settings can also be changed in the menu; the marker
survives menu saves and Restore Defaults. Game saves are not changed.

## Phone checks after a successful iOS build

1. Keep the known Build10 IPA; install the newly labeled candidate without deleting
   app data. Check the readable settings and camera movement first.
2. Compare scene clarity, sustained frame pacing and warmth during 10-15 minutes of
   normal play. If performance drops, disable bloom/FXAA or reduce render scale.
3. Check hold-to-pluck, whistle response, grabbing/throwing, and touch Lock-On/Charge.
   Check simultaneous movement/camera input and accidental button gestures.
4. Open and cancel each ZIP picker. Confirm the game resumes and another picker opens.
   Then test a supported pack and an invalid ZIP; originals must remain usable.
5. Restart and check persistence, pack selection, model activation and saving/loading.
   These results must be recorded separately from compiler and structural checks.

## Validation checkpoint

On October19 after resuming, all four suites ran against actual repository sources:
169 profile checks,19 bridge checks, real-filesystem transaction/rollback cases,
and the actual converter's ZIP cases passed. The first three built with MSVC17
/W4 /WX; the converter/stb suite used /W3. New UIKit code still requires Xcode and
phone validation. The workflow runs the portable checks on macOS before compiling.

Build12 did not compile either game: GitHub never assigned a runner and reported
ARM macOS capacity constraints. The next run uses macos-15-intel with the existing
explicit iphoneos ARM64 target. No performance or availability guarantee is made.

Upstream feature reference:
https://github.com/SSunnKing/Open-Nectar---Pikmin-Native-PC-Mobile-Port
Runner reference: https://docs.github.com/en/actions/reference/runners/github-hosted-runners
