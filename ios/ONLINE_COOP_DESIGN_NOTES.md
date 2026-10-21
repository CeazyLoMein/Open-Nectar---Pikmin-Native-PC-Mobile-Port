CURRENT - 2026-10-21 00:40 EDT: User agrees to keep normal saving for this P1 fixes/fresh-save retest, then prototype co-op and build shared exact-scene snapshot recovery for solo/co-op. See SAVE_AND_COOP_RECOVERY_PLAN.md for source audit/research. Ship-return option superseded by exact-scene preference. After P1, stronger P2 cave/area/audio/save tests precede P2 co-op. No final-boss spoilers.

## Current user authorization - 2026-10-20 20:43 EDT

After the free-profile fourth-app install failed, the user explicitly authorized
backing up current working P1 and putting the solo experiment into that app as an
update. This supersedes the separate-app requirement for this test. Existing game
settings should be preserved. No purchase or KartPad removal requested.
Verified rollback IPA and six current phone settings/layout/save files are in
folder5; no phone writes performed. New solo-update source retains the original
app identity/assets/settings with separate save-solo-test cards. All new slots
use the familiar-area fixture; finale preset disabled and final area not unlocked.
New Apple build/installation/runtime tests pending; online code remains unstarted.

# Future online co-op - agreed design notes

Updated 2026-10-20 14:31 EDT. Design discussion only; no online implementation started.
Online remains the final milestone after both native iPhone games are stable.
These notes record the user's decisions, separate from existing upstream features.

## Agreed experience

- Two players: user and Raye, each playing natively on an iPhone.
- Play together only. Independent offline continuation and merging divergent
  campaign saves are explicitly deferred.
- One chosen host owns the authoritative shared campaign save. Either person can
  start/host a campaign; both contribute to that campaign's progress, parts,
  treasures and unlocks. Automatic host migration is not a first-version requirement.
- Each phone shows only its own player's full-screen camera/HUD; no partner view,
  no split-screen or camera-merging requirement. Free separation within the map.
- Shared Onion storage by Pikmin type:200 stored, Raye withdraws20, both see180;
  further withdrawals/returns update the same inventory, with no duplication.
- Separate player allowances: if each player's allowance is30, each may have30,
  for60 combined; it must not silently become one shared30 limit.
- Separate squads, with clear ownership/transfer rules. Working and idle Pikmin
  need an agreed allowance rule so dismissing/recruiting cannot bypass limits.
- Private Create/Invite/Join flow with code/link sharing; no manual networking
  chores as the intended normal experience.
- Target joining from the same room or different states over suitable internet.
  Actual direct connectivity/relay fallback and service choice remain engineering
  decisions to validate; good bandwidth alone does not guarantee a direct path.

## Travel and difficulty - user explicitly accepted

- Forced group travel is acceptable. If one player enters a new area/cave,
  bringing the other along is acceptable; simultaneous different areas/floors
  are not required. This overrides any earlier suggestion that every area entry
  must require a two-player vote. Exact initiator/host handling remains to design.
- Difficulty should primarily scale enemy health, preserving phone performance.
- Selected encounters may add enemies only after performance and stability are
  validated. Blanket population increases or doubling every requirement are not
  agreed. Difficulty changes should avoid arbitrary mid-fight health jumps.
- Day-end/other shared decisions still need understandable handling; forced area
  travel does not itself settle every pause, cutscene, death or sunset rule.

## Other accepted feature goals

- Reconnect protection and a safe plan for the disconnected player's squad.
- Partner marker and pings for coordination without seeing the other screen.
- Safe shared handling of day endings, caves, pause and cutscenes.
- Phone interruptions: lock screen, backgrounding, calls and connection loss.
- Save backups and a visible confirmation that progress was saved.
- Independent graphics/control settings, compatible versions and shared gameplay rules.

## Scope and open details

No independent campaign progression, conflicting-save merge, separate simultaneous
maps/cave floors or host migration required initially. P1 has experimental netplay
and local co-op foundations; P2 lacks a functional online game adapter in the
current branch; current iOS build forces online off. No iPhone online behavior
has been verified. Shared inventory, per-player allowances, full-world consistency,
private invites, reconnects and saving must all be tested rather than inferred
from moving two captains. Do not enable online or start architecture changes as
part of the current P2 graphics/HUD work.

Possible later sequence: P1 two-iPhone LAN proof, internet connectivity, safe
campaign saves/rejoin, P2 integration, then performance-tested balance refinements.
This is a proposed sequence, not a schedule or completion promise.

## Accepted P1 prototype approach - 2026-10-20

The user asked to save this approach and said it was a good way to proceed.
This records an agreed plan; online implementation has not been authorized to
start in this exchange. Current P2 audio/HUD validation continues first.

P1 is a good candidate for a controlled exploratory prototype before P2:
its iPhone game already runs, and the repository has local two-captain co-op
plus experimental networking foundations. Online on our iPhone build is still
unproven. These foundations do not establish correct shared campaigns.

A full story completion is not a prerequisite for a separate exploratory
prototype. Reliable campaign release remains subject to broader gameplay,
networking and save-integrity validation; the original stable-release goal
and current priorities remain in place.

Protect the working P1 app and real saves: use a separately identified
experimental app with its own data container and a disposable campaign.
Do not overwrite or convert the working installation/save for the prototype.

Milestones:

1. Two iPhones on the same Wi-Fi, each rendering only its own player's
   full-screen camera/HUD. Confirm two independent captains and squads.
2. Both devices agree on enemies, Pikmin, shared Onion inventory, player
   allowances and campaign events. Test actions from both players rather than
   treating two moving captains as sufficient proof of synchronization.
3. Safe host-owned campaign saves, disconnect handling and rejoining without
   lost/duplicated progress or Pikmin. Back up saves before destructive tests.
4. Different internet connections, private Create/Invite/Join flow and the
   required connection/relay handling; then longer shared campaign testing.
5. Apply verified lessons to P2 later, followed by performance-tested balance
   changes. Keep the previously agreed together-only campaign and group-travel
   simplifications, with independent offline progress/host migration deferred.

No date, completion guarantee or claim of proven iPhone online functionality.

## Clarification and solo readiness gate - 2026-10-20

The separate P1 app is for the solo readiness experiment and later co-op
prototype. The user's eventual goal is proven co-op in the original P1 app,
preserving its solo play and existing saves. Do not replace that app now.
The user accepted a short representative solo campaign check instead of
requiring a full story playthrough before exploratory co-op. This is increased
confidence, not certification of every campaign event. See
PIKMIN1_SOLO_READINESS_PLAN.md for scope, shortcut limits and exact next actions.
No separate test IPA or co-op implementation was produced in this checkpoint.

## Latest user preference - preserve the finale surprise

The user does not want the final boss identified, shown or required for this
readiness experiment. No final-boss/ending test is required before beginning the
separate co-op proof of concept. Leave that coverage explicitly deferred until
normal play reaches it. Use only a new slot A/C and familiar earlier areas;
avoid the finale preset in slot B and the final area. Do not route the user into
late encounters or spoil them in instructions/screenshots. Earlier requests for
mandatory finale testing below are superseded by this preference.

Existing advanced settings include Olimar Health = Infinite and Invincible
Pikmin = On. These can make the exploration tests easier. Normal health/death,
hazard consequences and real progression remain unverified where cheats bypass
them. Do not treat those omissions as blockers to an exploratory co-op prototype.
The current Build32 source is unchanged; the unused finale preset remains in the
test app but is optional and must not be selected for this user's short test.

