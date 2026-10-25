# Raye iPhone setup — verified launch after folder repair

Updated 2026-10-24 America/New_York. User confirms P1 now opens normally with title/music/controls after the repair below; user also confirms P2 works. Phone can be unplugged. No further phone access or new IPA needed for this correction.

P1 installed executable UUID1760960b-2d27-3a21-960f-2dcc404350c6, read from three actual crash reports, confirms Build54. My original transfer copied correct files to the WRONG parent: Documents/pikmin1/dataDir. Native DVDOpen prepends assets/, so audio startup could not open its sequence archive and Jac_InitEventSystem waited forever. iOS watchdog reports0x8BADF00D identify that wait, not a graphics failure. After user closed P1, relocated only the imported disc roots into staged assets/ then activated it. Correct location: Documents/pikmin1/assets/dataDir; touch PNGs remain Documents/pikmin1/art. All3529files/669952108bytes re-read and hash-verified at correct paths. Settings hash unchanged; save/Load not modified. User fresh launch confirmed normal. Corrected local importer for future transfers. No P1/P2 source or original phone changes.

Private corrective receipt: work/raye-p1-layout-repair.json, copied to Documents/Open Nectar/folder3/Pikmin 1/Raye - Corrected Layout Verification.json. Earlier transfer receipt retained for history and is superseded on DIRECTORY PLACEMENT by corrective receipt. Original ISO log.txt is historical desktop output, not current phone evidence.

## Historical initial transfer checkpoint (superseded by correction above)

# Raye iPhone setup — current status

Updated 2026-10-24 21:15 EDT. Identified by model before all operations: iPhone17Pro (iPhone18,1), iOS27.0.1. User reported public/non-beta. Developer Mode menu was missing; exposed only the switch with AMFI action0. USER enabled/restarted/confirmed. Readback showed DeveloperMode=true. No account credentials entered or requested by agent.

P1 Build54/user's original phone: user reports very quick test seems fine; limited smoke check, not every rare fix/full story. Build53 remains preserved. Raye now has signed P1 installed. Her initial black screen coincided with missing dataDir/art: only Load/settings/save were present. We verified canonical private USA Rev1 ISO GPIE01, SHA123a153cb225fef488f57073e76df0de26789c218, extracted with existing source extractor with read-back checks, added34 source/PIL-verified touch PNGs, staged and read-back SHA256 checked ALL3529files/669952108bytes. dataDir exposed after verification, existing P1 settings hash unchanged and save/Load untouched. No need to rebuild solely for missing first-install data. Post-transfer P1 launch still awaits user result.

P2: user installed it and explicitly requested its files. Rechecked existing private2768 game-file hashes against prior ISO manifest and28 art hashes/PIL. Copied marker+data+art: ALL2797files/1013544103bytes read-back verified in Raye's P2 sandbox, staged then activated. assets/art added; saves/preferences untouched. Newer52 package still needs real-device launch/audio check on Raye's phone. Original user's working P2 unchanged.

Both copy processes completed successfully and closed their phone connections. User was immediately told PHONE MAY BE UNPLUGGED and to fully close/reopen each app. Do not keep asking for her phone just for co-op coding/CI.

Private extraction/transfer receipts: Documents/Open Nectar/3 - Game Files - Keep Private/Extracted for iPhone/Pikmin1 and Pikmin2 (actual folder names contain spaces: Pikmin 1 / Pikmin 2); work/raye-p1-import-progress.json, raye-p2-import-progress.json, raye-p1-black-screen.json, raye-pikmin-setup.json, raye-phone-developer-option.json. No game assets/ISO/Apple identity credentials committed to GitHub. No original phone writes. Installed-package executable UUID wasn't read back from her phone in this phase; signing was manual through Sideloadly.

Next user check when convenient: reopen P1/P2, see title/game, check basic input/audio/pause. P2 include Pikmin/enemy/snow sounds. If P1 stays black AFTER a fresh launch with these files, collect a new scoped startup log/crash report rather than assuming missing assets remains the cause.
