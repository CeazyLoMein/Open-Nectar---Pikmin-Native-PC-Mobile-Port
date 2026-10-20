# Current follow-up: Build30 audio failure and native parameter layout

Build30's clearer HUD is confirmed by the user; Pikmin, enemy and winter/wind
sounds remain missing. Louie's breathing/ship sounds can remain audible far away.
The earlier rear-route patch did not establish a runtime fix for these symptoms.

The active JAI parameter setters index a union array whose element includes a
pointer. Its stride expands to8 bytes on ARM64, but JASPortArgs' scalar fields
are still4 bytes after the native pointer. Float slot3 intended for volume lands
in pan; word slot2 intended for update flags overwrites volume. Other scalar and
stop-interrupt updates similarly miss their consumers. Native setters now use
named logical fields. Original console path unchanged; unused PS16 helper retained.
An actual producer/layout/consumer fixture failed13 checks before correction,
then passed48 after the patch, including repeated near/far volume changes and
stop interrupts. This is code-level evidence; phone restoration remains unverified.

Build30 also produced no audit report. Its standalone helper depended on SDL's
__IPHONEOS__ macro without including SDL. The shipped binary contains the
non-iOS opt-in string. Detection now includes Apple's TargetConditionals identity;
a platform regression failed6 of11 before and passes11 after. CI additionally
checks activation and parameter fixtures against the actual iPhone ARM64 SDK.

No new camera/listener remapping, content installation, save edit, P1 app change
or online implementation. New source must compile and be tested on iPhone before
claiming the reported effects or attenuation are restored.

## Earlier investigation and report/test instructions

# P2 missing/spatial audio audit and HUD candidate

The user reports missing red Pikmin voices, missing snowy wind, ship audio audible across the map as Louie, and blurry/small performance text during gameplay. They found the existing HUD toggle; no new toggle is needed.

## Verified findings

All 142 files in the phone's `pikmin2/assets/AudioRes` match extracted local originals by SHA-256 (2026-10-20). This includes 49 wave archives, bank/control files, sequence archives, streams and conductor data. No phone data was written during the comparison. This establishes asset integrity, not correct playback.

The actual software mixer incorrectly multiplied rear positional gain by the reverb send, causing zero-reverb rear sounds to disappear. It also omitted the rear direct bus IDs `0x0F40`/`0x0CA0`. Both are corrected; existing FX approximations and the established global gain are retained. The regression compiles the actual mixer/ARAM code, with DSP structs extracted from the real interface header, and fails 13 checks on the prior source before passing all 28 after correction.

The direct/reverb distinction and bus mapping were checked against the [Dolphin project's documented DSP implementation](https://github.com/dolphin-emu/dolphin/blob/master/Source/Core/Core/HW/DSPHLE/UCodes/Zelda.cpp). This is a technical reference; this project still runs native game code. No new external implementation was copied.

The original DSP tests had four stale expectations from before the earlier console gain correction. The same four fail on HEAD and the new source. Tests now explicitly set master gain to 1, expect the existing half-gain channel scaling, and use three loud voices to test saturation; game master gain was not raised.

Captain-switch source calls `PSSetCurCameraNo` for either captain. Single-player config was confirmed over USB. Do not claim the ship-distance cause is proven or change listener behavior without runtime evidence.

## Bounded report in the next candidate

`pc_p2_audio_audit.cpp/.h` counts captain/system/Pikmin/item/environment/enemy sound submissions and sequencer triggers, creature culling/scene gates, observed distance/gain/listener, bank-note failures, DSP source usage and mixed output peak. Wind IDs 0x402D/0x402E and ship piston 0x3043 have dedicated rows. Bank counts include music and effects together. The report does not yet correlate an individual bank note to its originating effect ID. Creature request counters do not cover every animation sound entry point.

On iOS it writes `p2-audio-report.txt` in the P2 working folder (`Files > Open Nectar Pikmin 2 > pikmin2`) every five seconds for at most ten minutes after audio startup. It retains one prior-launch report as `p2-audio-previous.txt`. Non-iOS builds opt in with PIKMIN_AUDIO_AUDIT. Fixed-size atomic counters avoid allocations and file operations at game callback sites. File writes use the host allocator scope. Reports contain counters/IDs, no PCM audio, game assets, saves or personal identifiers.

A 'started' counter means a sequence port received the trigger; it does not demonstrate audibility. The 11 report regression checks cover concurrent counters, wind/ship distinction, listener/distance/gain, output peak, previous launch retention, allocator restoration and time/size bounds. Full sound restoration remains a phone test.

## HUD

The HUD moves after game presentation and touch drawing, uses the SDL-managed display framebuffer at native drawable resolution, a consistent built-in font, larger spacing and a more opaque panel. Game render resolution/pixel budget is unchanged. Other menu calls default to their existing render target. Advanced settings/captain selection still hide the HUD; existing On/Off setting is unchanged. Sixteen real-code checks verify routing, order, larger text, disabled cases and framebuffer restoration; no real GL/iPhone visual result yet.

## Phone retest after successful build

1. Update P2 in place; preserve app, game files and saves. Leave P1 alone.
2. In the snow area whistle, grab, throw and dismiss reds; listen for individual voices, landing/attack sounds and wind. Rotate camera around the squad and compare both sides.
3. Leave one captain by the ship, switch to the other and walk away/return; repeat in the opposite direction. Report whether ship sound fades with distance and nearby effects follow the active captain.
4. Check menu clicks, captain whistle/voice/steps, enemy movement/hits/death, Pikmin carrying/plucking, cutscene audio, pause/resume and an available cave/area transition. Other colors when naturally unlocked. Do not risk a save solely to test death.
5. Compare HUD readability during gameplay/pause and check touch buttons remain usable. Keep 60 FPS and current content unchanged for comparison.
6. Keep the session within the first ten minutes after launch for diagnostics. Connect/unlock afterward; Codex retrieves both reports directly. Do not relaunch repeatedly before collection because only one previous report is retained.
