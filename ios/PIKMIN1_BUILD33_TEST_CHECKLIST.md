# P1 Build 33 - Install and Test This Version

This is an UPDATE for your existing P1 app. It is a solo-readiness test, not online co-op. The finale preset is disabled. You do not need to fight the final boss or finish the story.

## Install

1. Connect/unlock your phone. Open Sideloadly and drag in this exact IPA from Documents > Open Nectar > 1 - Install on iPhone:
   Pikmin 1 - Build 33 - UPDATE Current App - Solo Test.ipa
2. Use the SAME Apple account and the normal P1 bundle identifier. Do not change it to SOLO TEST or a new identifier. Leave bundle-ID customization as used for your existing normal P1. Click Start and let the update finish.
3. Do NOT delete your current P1 first. This replaces its executable while retaining its app data. If Sideloadly says it needs a fourth app slot or the update fails, stop and report the error instead of deleting anything.
4. You can disconnect once installation finishes. Existing assets, Art, texture packs and character packs should be reused; no recopy is expected. Actual retention still needs the checks below.

## Check in this order

1. SETTINGS FIRST: Launch P1. Check readable menus, your touch layout, camera drag, graphics choices, active GPI texture pack and character selections. Do not reinstall content or reset settings if anything changed; report it. A normal-looking app name/icon is expected.
2. NEW TEST FILE: Start a NEW single-player file, slot A recommended, Normal difficulty and Standard rules. The new-game prompt should say 'Solo systems test (no finale)'. Expected setup: Day 2, one ship part already credited, all three Onions with 100 leaf Pikmin each in storage, and the four earlier areas accessible. The original campaign card is separate; not seeing old test progress is expected. If this setup does not appear, stop and report it.
3. CONTROLS/MENUS: Walk and drag the camera together. Throw, whistle, dismiss, swarm/charge and change color. Open/close pause and advanced settings several times, both standing still and after moving. Check that touch controls return and the image stays clear.
4. ONION ACCOUNTING: With no other Pikmin outside, withdraw 20 reds: red storage should fall from 100 to 80. Return 5: it should become 85 with 15 outside. Return the rest: 100 in storage again. Repeat a withdrawal/return with yellow and blue. If anything dies or is born, account for that rather than expecting the unchanged totals.
5. REAL GAMEPLAY: Fight an ordinary familiar enemy, collect a pellet, carry something, and recover/deliver one real ship part. Confirm the part count increases from the preset's 1 to 2. Check Pikmin/enemy effects and music. Exercise a wall/bridge if convenient, plus blue-water/red-fire/yellow-bomb behavior where familiar and available. Leave anything you cannot reach as UNTESTED; do not seek late encounters or spoilers.
6. LOAD/PERFORMANCE: Work toward 100 active Pikmin with your installed graphics packs enabled. Move, throw and fight briefly. Watch for crashes, missing textures, audio cutouts or severe sustained slowdown. Optional Performance HUD is in Display settings. Take a screenshot if performance seems bad. Across test days, enter each of the four earlier areas and check loading, camera and menus. This can take several normal days; finish it later if needed.
7. PAUSE/BACKGROUND: In a safe spot, pause; switch to another app for about 10 seconds, return and resume. Controls, image and sound should recover. This is NOT an autosave test.
8. SAVE/RELOAD (essential): Finish a real day and use the game's normal end-of-day save. Note the day, part count and final Pikmin inventory AFTER sunset accounting. Only after saving completes, fully close P1, relaunch and load the SAME test slot. Those saved values should match; the preset must NOT reset the file to Day 2/one part/100 of each color. Move and open pause again after reloading.

Optional for easier exploration: advanced settings > Olimar Health = Infinite; Invincible Pikmin = On. These deliberately leave normal death/damage and some hazard behavior untested. They are not required, and will change your saved settings if you enable them.

Send back: settings/content retained yes/no; controls/menus yes/no; Onion math yes/no; real part delivered yes/no; save/reload retained values yes/no; areas visited; and any crash/audio/visual/performance problems. A screenshot of an error or the last screen before a crash helps. Say UNTESTED for skipped items. No recording or continuously connected phone is required unless we need logs.

Passing this sample supports an experimental co-op prototype. It does not certify the full campaign, every enemy, ordinary unlock progression or the ending.

## If something breaks

Stop testing and report which step failed. Do not uninstall P1 or overwrite the backup. The pre-test working Build16 IPA plus your exact settings, touch layout and normal save files are backed up here:
C:\Users\chazz\Documents\Open Nectar\5 - Archives\P1 Restore Point Before In-App Test - 2026-10-20 203541

Rollback uses the saved IPA signed with the same account/normal P1 identity. No need to delete the app. The original normal card remains under save; experiment cards use save-solo-test. The backed-up config/layout can be restored if needed. The installed signed binary was not extracted; the restore IPA is the saved last documented phone-confirmed working Build16.
