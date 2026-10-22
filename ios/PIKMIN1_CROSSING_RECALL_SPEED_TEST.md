# P1 Build40 — READY TO INSTALL AND TEST

Use **Pikmin 1 - Build 40 - Navigation Update.ipa** in this folder.

GitHub run39784525620 compiled the game successfully but failed icon packaging. Codex recovered its exact unsigned ARM64 app from the saved archive, added the approved six PNGs and verified the IPA locally. Every original app file, including executable and Info.plist, remains byte-identical. No new build needed. SHA256 02d057e55a2e77a0779462f37e420c2a5e665fa01c6523ee6c4129f1e65f7cdd.

1. In Sideloadly, choose this IPA and update your existing Pikmin1 with the same account. Do not uninstall the app. No new asset transfer, settings replacement or save reset needed. Original-ID standard campaign; Build35/37 rollback and phone backup remain in folder5.
2. Better Pathfinding ON. Olimar Speed100%, Pikmin Speed100% for this first retest. Repeat the same raised cardboard/ramp crossing in both directions, with turns and a normal/larger squad. Avoid deliberate swarm for this initial test.
3. If some fall below or remain behind, stop on safe ground for10-15seconds. Watch whether they find a walking route back, circle, wait, or become idle. Try the separate Recall All button once with a distant group; it intentionally includes workers. No teleport expected. Large groups share a bounded search budget.
4. Briefly check ordinary flat-ground following, local whistle, charge+whistle, Aim/Soft Assist, pause and frame rate. After the100% baseline use your usual modest speed;500% is not required. No late-game/finale test needed.
5. Tell Codex whether crossing prevention and return routing passed separately. If still stuck, avoid repeatedly relaunching: the new p1-navigation-report.txt resets per launch and may help identify the actual failed route. Codex can collect it over USB when requested.

Phone can be disconnected after installation; no need to leave the game running for Codex. Installation/runtime still unverified; local IPA validation is not proof the navigation is fixed. P2 remains on its working build. No mid-day autosave or online feature added.
