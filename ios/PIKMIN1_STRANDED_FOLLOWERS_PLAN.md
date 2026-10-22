<!-- AUTO_RESCUE_PLAN_SUPERSEDES -->
# Current decision — 2026-10-22

Build40 phone pathing failed at100% speeds. User now explicitly approved optional AUTOMATIC rescue after about8s stalled and failed walking return, only existing followers. Older statements below saying no teleport selected/implemented are HISTORY and superseded. Source/local checks completed; Apple/IPA/phone pending. Actual-input guard corrected; idle ship recall remains undiagnosed. See [current design and primary references](PIKMIN1_FOLLOWER_RECOVERY_DESIGN.md), current status/handoff and crossing checklist. One P1-only standard build will be dispatched after the scoped source commit. No new run or IPA yet.
<!-- END_AUTO_RESCUE_PLAN_SUPERSEDES -->

## Navigation v2 — source implemented, local checks passed, Apple/phone pending

Build37 native build/run39617967156/sourceabd06b6216f0d09bc13361ddbff693f58640a21f passed compilation/package, but user phone crossing/return FAILED. New11:23 and11:26 recordings show stranded/lost followers; exact action states/collider IDs were not recorded. User repeated at both speeds100% and confirmed failure. Current saved200% captain/500% Pikmin were later experimentation; do not attribute the recordings to500%. User does not want500% prioritized.

Source defects found and corrected:
- Old watchdog accepted any8-unit displacement, so circling reset its timer. New stalledToward checks actual reduction in distance to its current route waypoint/captain; moving goals reset observation appropriately.
- Ordinary formation could fail/release distant recalled followers; a route failure returned to that same logic. ActCrowd now retains a return intent until back nearby, interrupted by a real action/state change or disabled enhancement. Failed first steps, retries and exhausted shared budget hold safely instead of losing the assignment.
- Old nearest-waypoint endpoint cutoff180XZ/40Y assumed geometric nearness meant reachable. New bounded search considers six candidate endpoints each side within600XZ/100Y, validates walking access on actual collision layers and tries up to six graph pairs. Closed waypoints and non-blue water remain excluded. Generic carrier routing is preserved.
- Old getMinY actually returns highest floor, including overhead surfaces. New pc_follow_surface helpers follow nearest valid floor to actor height, sample12-unit steps and reject cliffs, holes, non-blue water and wall crossings. Normal slot reassignment no longer overrides protected steering. This is not a full navigation mesh rewrite.
- Following narrow/recovery paths uses original maturity-based walking pace with arrival braking, preserving vertical physics. Open-ground configured speed/work/attack/carry behavior retains prior settings. This is local crossing safety, not a500% development target.
- Shared per-captain new searches capped at2/sec; each tries at most6 pairs. Per-follower retry2s; active route up to30s or captain relocation256units; checks current graph/walkability during movement. No teleport or forced worker recruitment outside explicit Recall All.
- Bounded per-launch p1-navigation-report.txt captures first4 events/reason, max128 lines, coordinates/reason only. Collect over USB after a failed test; no current phone report exists for v2 yet.

Verification:87 actual-method trail/progress/route/recovery scenarios PASS;17 real layered floor/wall helper numeric scenarios PASS;82 command/recall/aim/edge scenarios PASS;283 walking/config scenarios P1 and283 P2 stock control PASS; campaign58/58/7 and app/storage/icon27 PASS. MSVC warnings-as-errors and independent Clang diagnostics PASS. Fixtures use engine seams and synthetic surfaces, not full map physics. CI runs the new surface fixture on host and iPhoneSDK plus full native P1 build. No Apple or phone success claimed for v2.

Limitations: only six candidate endpoints each side, graph may lack a ramp/link, collision probes are local centerline checks, crowds/dynamic obstacles can still defeat movement. Large remote groups share a route budget. Requires exact-crossing phone retest and frame-rate observation; logs should guide any next fix. Moving platforms, commanded swarms, damaged/thrown/working/etc contexts retain ordinary behavior. Multiplayer disabled for this enhancement pending coordinated deterministic design. Full campaign and rare clam cutscene unverified.


<!-- CURRENT_FOLLOW_IMPLEMENTATION -->
# P1 narrow crossing and route recovery — source implemented, phone test pending

Updated 2026-10-21 10:34 EDT. User requested Build36 be scrapped/cancelled and a combined patch with crossing/route work plus the already implemented separate Recall All and Pikmin Speed. Build36/run39614665805 confirmed CANCELLED. Nothing installed or removed on phone. New Build37/run39617967156, sourceabd06b6216f0d09bc13361ddbff693f58640a21f, observedqueued.

Evidence: Build35 user footage ScreenRecording_10-21-2026 09-47-51_1.mov,32.71s,9-14s raised cardboard/ramp crossing. Footage shows falling/stranded followers; exact collider/internal action state was not recorded. Build35 ordinary Aim/Soft Assist/charge whistle/save-reload passed user tests; clam cutscene unverified. Working IPA backup verified in folder5. P2 remains paused.

Implemented first pass under Better Pathfinding (solo):
- Navi records a bounded64-point recent grounded footstep trail,12-unit spacing, no heap/entity references. Relocation>96units or large height jump resets it; air/cutscene/swarm/moving platform and multiplayer discard it. Captured platform markers activate a narrow lane through the crossing and immediate exit; ordinary ground retains normal formation. Followers choose nearby same-floor footsteps, not a point above/below them. This is movement steering, never position replacement.
- Terrain/platform edge sampling includes platform collision, rejects nearby drops and unreachable upward steps. Recorded crossing lane bypasses normal side circling/slot widening, while moving platforms and commanded swarms keep ordinary handling. Healthy parked formations are not classified stuck.
- ActCrowd monitors only living, normal-state, grounded followers actually trying to move (or blocked/different floor). After1.25s without8units of movement, it may request a return route; no worker/carrier/attacker/free/buried/dead/thrown/drowning/swallowed rescue. Tripping/damage/held objects/cutscenes/day-end/moving platform contexts are excluded. No automatic recall of workers beyond the explicit global Recall button.
- Searches use the existing PathFinder waypoint graph: null/count/index/open/nearby-height endpoint guards, no cached Onion/other-colour path, no closed-waypoint bypass, non-blue AvoidWater. Max10 new searches/second shared per captain and2-second per-follower backoff. Route abandonment on stall,8seconds or captain movement>100units allows later retry. Does not promise a route where none exists.
- The dormant spline driver divides by segment length and can treat horizontal closeness as arrival. Recovery uses a separate bounded waypoint walker instead: coincident points skip safely, active waypoint openness/water rechecked, wrong-floor destination cannot finish,4 coincident skips per update, no teleport. Generic carrier/spline driver is unchanged; ordinary initRouteTrace gained safe null/count guards and an optional false-default recovery argument.
- Separate Recall All button (workers included) and100/150/200/250/300/400/500% Pikmin walking-speed cheat retained from cancelled Build36 source. Normal whistle remains local. No autosave/network feature added.

Validation:63 scenarios execute real trail/progress, recovery dispatcher, route setup and waypoint-walking methods with host engine seams;82 existing command/recall/aim/edge scenarios PASS;283 movement/config scenarios each P1 and P2 stock-speed control PASS;58+58+7 campaign variant checks PASS; MSVC and Clang diagnostics PASS. CI now runs the new follower fixture and iPhoneSDK syntax check, followed by full native P1 build. This is not a physics/map/hardware simulation: exact cardboard collision, crowded lanes, high speed and performance need phone evidence.

Limits: no guarantee all followers recover or no more falls; disconnected waypoints, missing ramp links, no safe route or collisions may leave a Pikmin stranded. Idle/disbanded Pikmin are untouched: local whistle first if one left formation. No teleportation fallback selected or implemented. Raised terrain without a platform trail only receives edge protection/recovery; surface-aware lane is an initial bounded approach, not an all-map navigation rewrite. Full campaign and rare clam event remain unverified.
<!-- END_CURRENT_FOLLOW_IMPLEMENTATION -->

# P1 stranded-followers investigation

User Build35 clip: ScreenRecording_10-21-2026 09-47-51_1.mov, 32.711667s,1562x720. Relevant interval9-14s: raised cardboard/ramp crossing, some followers remain below while others cross. It shows the symptom, not collider IDs or internal AI state. User movement speed/cheat settings for this clip were not specified.

Source: ActCrowd::pcProtectFormationEdge protects grounded terrain slots, explicitly excludes dynamic platforms. ActCrowd::initRouteMove exists but has no caller in the source search; init sets mHasRoute=false. Ordinary formation code chases wide slots, reassigns slots, then fails when too far/lost too long. Existing route availability is promising, not proof a usable route exists on this crossing. Piki::initRouteTrace currently dereferences nearest-waypoint results without null checks, so blindly activating dormant paths is unsafe.

Recommended order (proposal only, NOT implemented):
1. Reproduce this exact raised crossing and compare100%/200% captain speed, ordinary terrain and platform footing; observe detached followers versus workers.
2. Prevent side spill on narrow elevated crossings using a validated surface-aware narrow formation or bounded safe captain-footstep trail, without forcing grounded samples onto platform tops below/above the actual collision surface.
3. Add bounded progress monitoring for living normal-state followers actually trying to rejoin; attempt validated existing route around an obstacle, rate-limit searches, handle missing/blocked/disconnected waypoints and moving captain, preserve water/gates/hazard rules. Do not promise a route where no connection exists.
4. If a rescue fallback is later selected, target only stalled eligible followers: assigned to this captain, not moving normally, not idle workers/haulers/builders/attackers, not thrown/swallowed/drowning/crushed/buried/dead or on a moving platform. Require sustained failed progress and validated safe destination. Healthy nearby squad must be unaffected. Prefer explicit optional rescue over silent automatic teleport initially.

User has NOT selected a teleport policy. They were unsure whether a rescue button would affect healthy squad; clarified it can be restricted to stuck followers. Do not add any teleport in the Recall All/Pikmin Speed build. Global Recall remains intentionally able to interrupt workers; normal whistle remains local. Full AI rewrite is not assumed necessary, but route adaptation/testing is real work.
