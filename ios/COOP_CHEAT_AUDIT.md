# P1 online co-op settings and cheat audit — 2026-11-06

Scope: EVERY entry currently compiled/listed in the Cheats tab, plus reported targeting/HUD and related Controls/Gameplay options. This is a source/authority/test audit, not a claim that every cheat has passed real-phone testing in every campaign situation. No automated input was sent to a live game.

## Cheats tab inventory

| Row | Setting | Online practice ownership/availability | Evidence and limit |
|---|---|---|---|
| 5 | Day Length | Unavailable in disposable practice | Practice clock is held at noon; campaign day length is not exercised. Menu explains restriction; saved solo value unchanged. |
| 11 | Olimar Health | Host sets rule for both players | Damage scaling in navi.cpp; host applies to both captains. Source inspected; full hardware scenario coverage pending. |
| 12 | Enemy Health | Host sets rule for both players | pc_mods_teki_damage; normal attacks and Chappy head-smash action use it. Source inspected; full hardware scenario coverage pending. |
| 4 | Pikmin Limit | Unavailable in disposable practice | No Onion/withdraw system in current practice. Menu explains restriction; saved solo value unchanged. |
| 21 | Throw Speed | Host sets rule for both players | Navi/NaviState/PikiState throw timing reads host setting. Source inspected; full hardware scenario coverage pending. |
| 44 | Rescue Stuck Followers | Unavailable in disposable practice | Existing getter explicitly disables rescue in co-op; menu now says so. Menu explains restriction; saved solo value unchanged. |
| 42 | Recall All Pikmin | Independent per player | Separate per-player Recall All command, owner-filtered by host. Existing native tests; retest on new pair. |
| 20 | Whistle Radius | Host sets rule for both players | Navi.h WHISTLE_MAX_RADIUS uses host setting; sampled ring radius sent to guest. Source inspected; full hardware scenario coverage pending. |
| 26 | Invincible Pikmin | Host sets rule for both players | InteractBattle and Piki damage/environment guards read host setting. Source inspected; full hardware scenario coverage pending. |
| 27 | All Flowers | Host sets rule for both players | ViewPiki flower selection on birth reads host setting. Source inspected; full hardware scenario coverage pending. |
| 28 | Carry Speed | Unavailable in disposable practice | No replicated carrying/corpse jobs yet. Menu explains restriction; saved solo value unchanged. |
| 29 | Olimar Speed | Independent per player | Bounded per-player naviSpeedPct input; existing walking/input regression. Existing native tests; retest on new pair. |
| 43 | Pikmin Speed | Host sets rule for both players | Actual Piki speed path and mode gate; host controls both squads. Source inspected; full hardware scenario coverage pending. |
| 30 | Unlock All Zones | Unavailable in disposable practice | Campaign-only save mutation, outside disposable practice. Menu explains restriction; saved solo value unchanged. |
| 31 | No Day Limit | Unavailable in disposable practice | Campaign-only; upstream diary exhaustion fix ported and regression tested. Menu explains restriction; saved solo value unchanged. |
| 32 | All Onions | Unavailable in disposable practice | Campaign-only; no shared Onion engine adapter yet. Menu explains restriction; saved solo value unchanged. |
| 37 | Breakable Reinforced Gates | Unavailable in disposable practice | No gates in this practice scene. Menu explains restriction; saved solo value unchanged. |
| 19 | Debug Keys (F5-F8) | Unavailable in disposable practice | Debug spawn/time keys are not a practice feature. Menu explains restriction; saved solo value unchanged. |

## Related settings and confirmed defects

- Phone saved settings: Lock-On=Soft Assist(3), Idle Counter=On. Host and guest saved Enemy Health=100. These were enabled, not missed toggles.
- Soft Assist: host previously selected targets, but guest never received a target binding for the native lock ring. Prediction could also override the assisted cursor. Guest aim preference now travels separately; target indicator binds only the locally-created whitelisted enemy, with lifecycle cleanup. Manual free aim still overrides preview immediately. Input gaps stop movement while preserving assist preference.
- Idle Counter: guest GameStat has no live Pikmin because guest AI is dormant. Counter now reads fully admitted replicated FreeMode actors and bypasses the simulation-only timestamp gate. It counts idle Pikmin across both squads, as the original global counter does. Source-based tests exercise the actual UI preamble, including Off/menu/invalid-baseline behavior.
- Enemy gauge: guest fade state never advanced under the simulation-authority guard, leaving zero alpha. Co-op presentation now explicitly sets visible state, alpha and accepted health ratio. Practice host also shows full-health gauge. Actual adapter tests reject invisible gauge state; real visual result still pending.
- Shared Controls/Gameplay rules: Chain Actions, Hold to Pluck, pathfinding, Blues Only In Water, no tripping, health, Charge, throw timing/cancel/grab, whistle response/radius, bomb and colour selection are host-governed. Guest menu now explains this instead of accepting an ineffective local change.
- Personal camera, graphics, FPS, touch layout, Free Camera sensitivity, Lock-On preference, captain speed, Recall All and local display options remain personal. Split/merged-screen controls are unavailable in online practice. This audit does not establish hardware coverage for every camera/cosmetic combination.
- All Flowers applies when Pikmin are created, not as an immediate conversion of an existing squad. Practice has no live refill yet.
- Dwarf Bulborb: native head-smash action applies 100 base damage through the same Enemy Health modifier. Practice initial max life is 150 before other existing modifiers, so a couple of head hits can defeat it quickly. Ordinary attacks follow their own native damage path. User confirmed simultaneous attacks work; unusually slow ground combat remains a runtime question, not proven invulnerability. New host report logs hp/max/pending damage/FSM state to diagnose it.
- Missing PC eyes: USER A/B CONFIRMED the optional Dwarf Bulborb HD model is responsible. Original model displays correctly with that one pack option off. No pack binary or texture was modified. The low-alpha eye-related submesh is intentionally glass cornea in the converter; alpha alone does not establish a renderer defect. Underlying optional HD model compatibility fix remains OPEN, accepted workaround is original Dwarf model. Other packs can remain enabled.
- Tailscale ReceiveIPv4/MagicSock warning: user toggled/recovered connection; PC read-only checks found working UDP/IPv4/IPv6 and a direct phone pong around4ms. No VPN/firewall settings changed. Official guidance: https://tailscale.com/docs/reference/messages/client/magicsock-receive-func-error

## New upstream comparison and selected ports

Fetched upstream/main through fc8bcf94 on2026-11-06. Latest published release page still lists1.1.1 (Oct29); main contains newer source fixes. No wholesale merge of PC/Android assumptions into iOS. P2 unchanged. Selected small relevant fixes, all preserve this fork's existing interfaces:
- Gate side pieces remain drawn after the centre sinks: https://github.com/SSunnKing/Open-Nectar---Pikmin-Native-PC-Mobile-Port/commit/fc8bcf94de15e4824ccacbdad4042b654c7d50ab. Original pc_wall_sides_test passed.
- No Day Limit diary Misc pages no longer exhaust after27 plain day ends: https://github.com/SSunnKing/Open-Nectar---Pikmin-Native-PC-Mobile-Port/commit/e7d1168dac9adb718cd7e4f7fbfc22e29c48f50b. Original230-day-end source regression passed, adapted to this fork's one-argument getDocument API. This is not230 actual campaign playthroughs.
- Whistle-plucked Pikmin count toward the pluck camera threshold: https://github.com/SSunnKing/Open-Nectar---Pikmin-Native-PC-Mobile-Port/commit/3179be7a0aaabbe0842959cc536cbe068e975e79.
- Onion spawn-pool failure logs/refuses instead of crashing: https://github.com/SSunnKing/Open-Nectar---Pikmin-Native-PC-Mobile-Port/commit/af178e7559f34ed4258b5b42e059a41bc3efeff2.
- Other fetched topics include RNG order, skipped Onion cutscene events, early throw wind-up and platform CI. They remain comparison candidates for campaign regression; not silently merged or claimed present.

## Verification status

- Local source changes IMPLEMENTED.35 native networking tests passed,631 cursor checks,89 actual feedback/HUD/availability checks,1296 smoothing checks,283 walking scenarios,110 command scenarios and20 PC Recall All scenarios passed.
- Actual capture/guest gauge/idle/target/retirement fixture and network-free legacy header probe passed. Real encrypted multipart/audio/interruption/rejoin socket probe passed.
- Upstream wall and230-day-end diary regressions passed. Actual captain and changed engine header checks passed (known legacy warnings remain).
- Actual bounded diagnostic rotation test passed after health logging.
- New combined PC/iPhone compilation and hardware tests PENDING. No claim that the reported phone visuals are fixed on hardware yet.
- User tested prior PC21/iPhone105: both squads can attack together; pause/Resume works. Enemy guest sound/health/aim/counter and full cheat behavior still need the new test.
