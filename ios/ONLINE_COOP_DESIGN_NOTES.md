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
