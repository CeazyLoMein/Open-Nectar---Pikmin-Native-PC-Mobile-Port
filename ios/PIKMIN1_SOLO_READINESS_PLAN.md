# P1 - Short Solo Campaign Readiness Experiment

Status: agreed test approach; no separate test IPA or scenario harness has been
built yet. No P1 app, source, save or installed content changed by this checkpoint.

## Protect the working game

The user confirmed on 2026-10-20 that the experimental app is temporary isolation,
not the intended permanent home for co-op. Use a different bundle identifier and
an obvious test-app name, with a separate data container, settings and disposable
campaign. Never overwrite, convert or delete the working P1 installation/save.
Copy private assets locally only as needed; do not upload assets or saves.
Matching graphics/content can be copied into the isolated app for representative
tests. Keep source changes scoped and separately reviewable.

Eventually, after validation, the goal is to integrate supported co-op into the
original P1 app. That future update must preserve solo play and existing saves;
it is not permission to replace the working app now.

## Short representative test once prepared

Aim for a compact phone session, using scenario/checkpoint selection rather than
playing the entire story. Duration depends on checkpoint preparation; setup is
development work and is not included in the short play session.

1. Load each of the five campaign areas. Walk, rotate the camera and use pause,
   advanced settings and touchscreen controls. Check graphics, audio and loading.
2. Exercise red/yellow/blue abilities: fire/water, bombs, combat, hazards, carrying,
   bridges/walls, plucking and Onion withdrawal/return with inventory checks.
3. Recover a real ship part and verify delivery, collection count and relevant
   unlocks. Exercise a representative boss and a large active squad with the
   installed texture/model content, monitoring frame times and memory.
4. Run a real sunset/day transition, save normally, close/relaunch the test app
   and reload. Confirm day, area/part progress and Pikmin inventory persist.
   Test pause/background/resume separately; backgrounding is not an autosave claim.
5. With a verified disposable late-game checkpoint, test final-area loading,
   final-boss/last-part completion and the real ending/save transition. If no
   suitable checkpoint exists, record this coverage as missing rather than fake it.

Do not claim 100% campaign verification: rare enemies, optional events and long
sessions can still fail. Passing supports proceeding to a separate co-op proof
of concept; it is not a stable full-campaign release certification.

## Existing shortcuts and their limits

- settings/pc_settings.cpp has Unlock All Zones; its description says the change
  is saved into the game. Use only the disposable test campaign.
- pc_speedrun.h/cpp practice days require existing checkpoints for later days;
  they do not create arbitrary late-game saves.
- Speedrun F7/F8/F10 debug shortcuts only update tracker state, not actual
  progression. They cannot validate real ship delivery or ending logic.
- Desktop F-key shortcuts are not an iPhone test interface. Any missing scenario
  setup must be implemented and verified before asking the user to test it.

## Exact next development actions

1. Keep P2 Build31 phone audio validation as the immediate pending hardware check.
2. Inspect P1 iOS packaging/data-root code and implement a separately identified
   test app without touching the working installation or real save container.
3. Audit available legitimate checkpoints; add only the minimal test-only scenario
   selection/setup needed. Do not assume late-game checkpoints already exist.
4. Verify packaging isolation, scenario setup and save/reload, then stage a clearly
   labelled test IPA and short checklist in Documents/Open Nectar.
5. Run the representative solo checks; record passed/failed/untested coverage.
   Begin co-op implementation only after the readiness decision, with the agreed
   isolated prototype approach. No co-op code has been started here.
