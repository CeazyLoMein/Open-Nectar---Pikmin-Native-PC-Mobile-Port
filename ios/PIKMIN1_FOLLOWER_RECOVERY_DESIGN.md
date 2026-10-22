# P1 follower recovery: references and implementation

Updated 2026-10-22. Distinguish published game features from our proposed design and actual source changes.

## What the references support

- [Nintendo's Pikmin 4 overview](https://www.nintendo.com/en-ca/store/products/pikmin-4-switch/) shows the whole squad riding Oatchi. Our inference: carrying the squad together reduces the number of independent bodies that must negotiate a crossing. Nintendo does not disclose its follower algorithm here. We are not adding Oatchi or claiming P4 uses an eight-second teleport rule.
- [Obsidian's Grounded 1.4 notes](https://grounded.obsidian.net/news/grounded/fully-yoked) document a separate Recover Pets repair feature. This is a practical example of keeping recovery available when ordinary movement fails; our automatic follower policy is our own design.
- [Grounded's official issue tracker](https://grounded.obsidian.net/issue-tracker), Patch 1.4.3, records a fix for teleporting followers knocking players off ledges. Applied lesson: land beside the captain, check body support/occupied spots, spread rescues over time. These checks still need real engine/hardware validation.
- [Recast Navigation's official repository](https://github.com/recastnavigation/recastnavigation) separates Detour path queries from DetourCrowd local motion/avoidance. A valid route alone does not solve crowd steering. We are retaining the existing P1 engine, not integrating a new navigation library in this patch.

## Implemented now; phone result pending

1. Fix the new recovery guard to check actual C-stick input. Stock mIsCStickNeutral also becomes false for a separated formation without deliberate swarm input; this was disabling the trail/edge/return logic when needed.
2. Keep the existing captain trail and bounded walking-return attempts first. Independently monitor about eight seconds without meaningful progress toward sampled captain/route goals. Failed route attempts cannot erase this observation; movement of the captain alone is not evidence of follower movement.
3. Optional Cheats > Rescue Stuck Followers, OFF by default and saved independently of Recall All. Only normal living grounded existing followers in formation are candidates. Workers, attackers, idle/unassigned Pikmin, thrown/damaged/stuck/held/rope/tripping contexts, cutscenes/day end and moving-platform contexts are excluded by action/state/surface guards. Disabled in Hard, Speedrun and multiplayer/deterministic modes.
4. Require sustained stalled progress AND a failed/blocked/abandoned walking return before relocation. Distance alone is insufficient. This is a conservative heuristic, not perfect knowledge of player intent or map reachability.
5. Search up to 48 spots, 22/37/52 world units beside the captain. Require dry non-hole supported floor on the captain's level, a locally walkable connection, body-clearance probes and no overlapping living Pikmin. Reject nearby visible living enemies at origin or destination (harmless pellet-posy and clam contents excluded). Both captain and follower must be grounded/static. No suitable spot means wait and retry; it does not force a landing.
6. At most four new attempts per second shared by the captain, two-second retry after a rejected spot, twelve-second per-follower cooldown after rescue. Use the engine's resetPosition path, synchronize animation/velocity and let normal physics reacquire the floor; preserve squad/action/counts.
7. Bounded per-launch navigation/recall diagnostics; captain tick opens the report even if no route search occurs. The idle Pikmin near the ship ignoring Recall All remains unexplained; added eligibility evidence without forcing an unknown game state.

## Ideas saved for later; NOT implemented in this patch

- A stricter single-file crossing queue with stable order and spacing, widening again only after supported ground. Existing trail narrowing is a first pass, not a full queue controller.
- Share successful crossing segments while rechecking gates, water, moving surfaces and floor layers. Never copy an invalid route just because another Pikmin once crossed.
- A small optional HUD count for waiting/stranded/rescued followers; avoid unexplained disappearances or relying only on logs.
- Optional idle-only recall, separate from Recall All and automatic rescue; jobs must remain deliberate. Diagnose the reported ignored idle Pikmin first.
- Later multiplayer: host alone decides recovery and broadcasts the actor update, preserving ownership and shared counts. No network code in this patch.

## Verification and limits

Local fixtures execute actual selected methods with engine seams:128 route/recovery/rescue,24 layered-floor/wall,103 command/control/config,283 P1 speed and283 P2 stock-speed control,58/58/7 campaign variants and39 bundle/configuration checks passed. Clang diagnostics passed for current follower/surface/command fixtures. These do not simulate the real crowded cardboard crossing, every hazard or Apple ABI integration. Full native compilation, IPA packaging and iPhone behavior are separate pending milestones. Conservative exclusions may delay recovery. No claim of full-campaign certification.
