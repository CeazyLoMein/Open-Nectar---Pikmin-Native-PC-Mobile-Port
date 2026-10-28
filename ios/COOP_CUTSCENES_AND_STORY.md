# Co-op story scenes and transitions: design and verification queue

Updated 2026-10-28. This records the user's requested goal. It does not enable, synchronize, or verify campaign cutscenes. Avoid spoilers in player-facing messages and test instructions. Practice intentionally skips campaign arrival/tutorial scenes; that is not a campaign design.

## Source evidence

- `games/pikmin1/src/plugPikiKando/gameCoreSection.cpp`: `startMovie` applies scene-specific visibility/update flags, starts Pikmin demo states, and the PC local co-op path freezes both captains while the selected movie captain is animated. `endMovie` restores visibility, update flags, effects and camera behavior. Different scene flags may allow some Pikmin to update during a scene, so blanket assumptions about all world actors freezing need investigation.
- `games/pikmin1/src/plugPikiKando/demoInvoker.cpp`, `pikiState.cpp`, `aiCrowd.cpp`, `naviMgr.cpp`: scene initiator can be the relevant captain or a Pikmin's associated captain. Actor identity, target and position need a host-confirmed mapping, particularly when players are far apart.
- `games/pikmin1/src/plugPikiColin/cinePlayer.cpp` and `gameCoreSection.cpp` rendering include scene-driven camera/actor behavior. Independent gameplay cameras and character state must be restored after each event. Prior user saw an item absent from a scene and a displaced captain; capture a non-spoiler reproduction if it recurs, do not assert a cause.
- Existing P1 online practice snapshots carry limited captain/Pikmin presentation, not scene trigger/event, world clock, all enemies, objects, audio, rewards or story flags. The current prototype cannot synchronize full campaign scenes.

## Intended player experience

1. Either player can trigger an eligible shared event. Host validates and commits its trigger exactly once, identifies the triggering captain and relevant stable target, and tells both devices which scene/event is starting. Both see the same relevant story content on their own screens, even across the map. Keep each player's subtitles, audio volume, display quality and controls local.
2. Freeze or constrain shared gameplay according to the event's actual game semantics; prevent the other player's unacknowledged actions from causing duplicates or entering incompatible states. Some events intentionally update parts of the world, so audit each class instead of globally stopping every actor.
3. Both phones acknowledge readiness for scene start and completion. A faster phone waits at an understandable status; controls, camera and HUD return safely for both after host-authoritative completion. Do not assume both render or finish at the same frame rate.
4. Offer a clear skip policy that avoids one person accidentally skipping the other's story. A sensible initial design is a request plus agreement from both players; exact UI and behavior need implementation and testing. Never change solo skip behavior.
5. If either phone backgrounds, loses connection or crashes, hold the host-authoritative state safely and identify the waiting player. Live guest rejoin is not integrated. A reconnect must authenticate, obtain the right scene phase and a fresh consistent baseline, then require readiness; do not rerun rewards or restart an irreversible interaction. If the host is lost, do not promise exact recovery without a complete verified checkpoint.
6. Stage exits, end-of-day sequences, tutorial prompts, item discoveries, dialogue and transitions need explicit ownership, synchronized completion, correct time and atomic shared progress. Some may require a distinct flow instead of a normal cinematic. Forced group travel between areas is acceptable to the user.
7. Keep normal single-player, local co-op, saves and settings safe; do not force either player into a spoiler or overwrite an unrelated solo slot. Character/model/texture differences must remain presentation-only and may not change scene timing or shared state.

## Verification before campaign claims

- Trigger scenes once from each captain with the partner both close and far; verify correct initiator, target and shared result once.
- Compare both screens and HUD restoration with different FPS, display resolutions, local packs and audio/subtitle settings.
- Test guest slow-loading, waiting, background/return, brief loss, prolonged loss, reconnect attempt, host loss and cancel/back paths at the start, middle and end; no stale input or duplicated progress.
- Test both agree to skip, one declines, simultaneous/repeated skip requests, skip near natural completion and either participant disconnecting during a vote. Time out safely; do not auto-skip story.
- Cover dialogue, tutorial, event-triggered movement, carrying/work, stage change, day end, saving and real campaign reload. Use controlled non-spoiler fixtures first; actual device and story coverage remains essential.
- Check successful completion is equivalent on both clients and that outcomes survive a validated save/reload; protect the last good save if anything fails.

## Design references

- Existing Pikmin local co-op provides actual two-captain scene handling, but not network synchronization (files above).
- Outer Wilds QSB describes shared discoveries, game-cycle events and compatibility limits: https://github.com/qsb-dev/quantum-space-buddies/blob/master/README.md
- Nintendo's Pikmin 3 Deluxe offers an integrated Story -> player count -> save selection flow: https://en-americas-support.nintendo.com/app/answers/detail/a_id/71812

### Dialogue and story-event lessons from other co-op mods

Skyrim Together's own feature notes describe broadcasting the leader's dialogue and displaying their choices to other players, and its changelog records fixes to quest stages and item synchronization: https://github.com/tiltedphoques/gitbook-wiki/blob/main/general-information/features.md and https://github.com/tiltedphoques/TiltedEvolution/blob/dev/CHANGELOG.md . For this project, treat those as evidence that dialogue presentation and story state both require coordination. Do not copy its leader-only trigger policy: either Pikmin player should be able to initiate eligible events, with host authority resolving the shared result. A dialogue's subtitles should be individually configurable even when the shared event is the same.

### Camera and sound restoration to verify

The P1 online single-view branch in `GameCoreSection::draw` selects the local captain as the audio listener during ordinary gameplay, but uses the movie look-at position while a movie is active. `endMovie` adjusts the active camera and resets the movie captain pointer. This is existing source behavior, not evidence that guest cinematics synchronize correctly. Test that both players hear spatial sound near their own normal viewpoint after a shared event and that the scene's listener/camera don't persist afterward; local volumes remain individual. A silent/disconnected/slow participant must not change the host's authoritative outcome.

### Transition and event failure cases from released games

No Man's Sky's developer documented fixes for interactions blocked by a lost player and for joining during travel placing a player in the wrong location: https://www.nomanssky.com/expeditions-update/ and https://www.nomanssky.com/next-generation-update/ . For our implementation, explicitly test disconnect during an interaction or scene and late joining across an area transition; an unfinished remote interaction must not permanently lock the surviving player or commit the outcome twice. This is an engineering lesson, not evidence those exact bugs exist in P1.
