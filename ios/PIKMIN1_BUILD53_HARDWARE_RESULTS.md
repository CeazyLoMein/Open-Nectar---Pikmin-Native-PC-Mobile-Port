# P1 Build53 — phone-tested display and graphics baseline

Updated 2026-10-24 19:47 EDT. User explicitly asked to retain this finding and keep the higher resolution. No new graphics change/build requested.

## Confirmed by user on installed Build53

- Gameplay is visibly sharper.
- Touch controls move farther toward screen edges. Save/relaunch persistence was not separately reported.
- Software keyboard stays closed during the reported test.
- Following feels better; this build made no AI change, and the previously stranded pair/teleport fallback were not revalidated.
- At1902x1338/1.00x the user later saw about43FPS. Turning Ambient Occlusion OFF while keeping that resolution brought the reported frame rate to120.
- The user then selected the highest2853x2007/1.00x and still reported120FPS with Ambient Occlusion OFF. This supersedes the earlier assumption that full resolution alone was too expensive on this device.

## Read-only phone evidence

Before comparison: work/p1-build53-graphics-20261024-193524/pikmin_settings.conf:1902x1338, renderScale1, fpsMode2, vsync1, antialiasing1, bloom1, ssao1, dof0, anisotropy4, GPI texture pack enabled.

After comparison: work/p1-build53-ao-off-20261024-193828/pikmin_settings.conf:2853x2007, renderScale1, fpsMode2, vsync1, antialiasing1, bloom1, ssao0, dof0, anisotropy4, same pack enabled. Files retrieved without changing phone data. Configuration does not itself measure FPS;120 is the user's runtime report.

Ambient Occlusion is the strongly supported cause of this large drop. This does not guarantee120 in every area, under all thermal conditions, or during a full campaign. Heat had previously been Fair; sustained temperature after disabling AO was not separately reported. No reason to force a lower resolution or60FPS cap. Keep current high resolution and AO OFF; avoid unnecessary code/build changes for this resolved setting issue.

Native sizing uses current oriented physical drawable automatically. Lower absolute resolution choices are explicit budgets. If a future device needs a lighter relative budget, native Resolution +0.67x 3D Resolution follows screen size; an actual-renderer local check confirmed this equals1902x1338 on2853x2007 and follows2796x1290/2034x1398 too (8 comparisons PASS). This is an available option, not a change to the user's now-working1.00x configuration.

## Still unverified / open

- Moving lines at the lowest resolution: user cannot distinguish tearing from texture shimmer, and still images do not establish cause. No confirmation whether they persist with AO OFF. Revisit only if the symptom returns; a short camera-pan clip would help.
- Earlier world-black/NaN coordinates and stranded followers remain unresolved. One successful resume or a rescue event without actor/time correlation does not close them.
- No full-campaign certification or complete current phone save/assets backup. Phone may close/disconnect; existing private evidence and package baselines retained.
