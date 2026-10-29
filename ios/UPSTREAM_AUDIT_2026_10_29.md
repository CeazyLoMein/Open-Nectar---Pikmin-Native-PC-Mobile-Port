# Upstream audit: Open Nectar 1.1.1, 2026-10-29

Original: https://github.com/SSunnKing/Open-Nectar---Pikmin-Native-PC-Mobile-Port
Release: https://github.com/SSunnKing/Open-Nectar---Pikmin-Native-PC-Mobile-Port/releases/tag/1.1.1
Release published 2026-10-29 15:26:56 UTC (11:26:56 EDT), release commit dc92d469517aaf899c4a6be849936e274a9c7303.
Fetched upstream/main 14a922a9; compared new work since the previously inspected 77a5aaa4. No upstream commits merged/cherry-picked in this batch. The fork and its iOS work remain intact.

## Useful candidates, with integration boundaries

- dc92d469: per-program GL uniform caches avoid redundant driver uploads when switching TEV shaders. Strong performance candidate for a subsequent graphics batch. Upstream's 2.8 ms of 8.3 ms figure is THEIR profile, not a measurement of our phone. Cache invalidation, relink/program-ID reuse, overlays/post-processing and iOS presentation must be tested before adoption. Do not import the same commit's 480p default or reset saved native-resolution choices.
- 315a45fe, 47621b0f, 98a05ecb, 092fdf06: Switch layout, controller guide, bindable right-stick aiming/swarm/lie down and face-forward-to-cursor option. Reconcile action IDs and settings migrations explicitly: upstream additions collide with our appended Recall All binding/action index 26. Preserve F6, independent device controls and custom iOS gestures.
- 585a21a6 and 23950bc9: captain preview animation and captain/Pikmin head tracking only once per simulation tick. Useful animation/performance review candidates; our replica presentation must remain independent from host simulation and ordinary local split-screen.
- fd90060a: presentation vector reservation, small allocation optimization candidate.
- PADClamp branch merged by 14a922a9: stick strength/diagonal fixes. Verify with touch, PC steering, gamepad and guest camera-relative movement before adopting.
- ebcb4390: P2 randomized treasure/music, fast mouse throws and cave-map GPU debug-readback removal. Preserve as a later P2 audit, not silently changing the current user-confirmed working P2 app.

## Current bugs and upstream relationship

The upstream carry-goal code still contains the same missing-Onion `zannnen` panic. No upstream solution to the new Windows Ready/focus loop or our guest practice interpolation was found in these commits. Our current fix batch therefore addresses those directly. The new upstream control/UI features are not installed just because a release was found.

Already incorporated fork safeguards, such as seed landing, should not be duplicated or replaced blindly. Review each candidate as a scoped change with actual source and runtime checks; never wholesale replace settings/input/render files.
