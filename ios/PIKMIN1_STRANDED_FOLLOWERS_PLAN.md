# P1 stranded-followers investigation

User Build35 clip: ScreenRecording_10-21-2026 09-47-51_1.mov, 32.711667s,1562x720. Relevant interval9-14s: raised cardboard/ramp crossing, some followers remain below while others cross. It shows the symptom, not collider IDs or internal AI state. User movement speed/cheat settings for this clip were not specified.

Source: ActCrowd::pcProtectFormationEdge protects grounded terrain slots, explicitly excludes dynamic platforms. ActCrowd::initRouteMove exists but has no caller in the source search; init sets mHasRoute=false. Ordinary formation code chases wide slots, reassigns slots, then fails when too far/lost too long. Existing route availability is promising, not proof a usable route exists on this crossing. Piki::initRouteTrace currently dereferences nearest-waypoint results without null checks, so blindly activating dormant paths is unsafe.

Recommended order (proposal only, NOT implemented):
1. Reproduce this exact raised crossing and compare100%/200% captain speed, ordinary terrain and platform footing; observe detached followers versus workers.
2. Prevent side spill on narrow elevated crossings using a validated surface-aware narrow formation or bounded safe captain-footstep trail, without forcing grounded samples onto platform tops below/above the actual collision surface.
3. Add bounded progress monitoring for living normal-state followers actually trying to rejoin; attempt validated existing route around an obstacle, rate-limit searches, handle missing/blocked/disconnected waypoints and moving captain, preserve water/gates/hazard rules. Do not promise a route where no connection exists.
4. If a rescue fallback is later selected, target only stalled eligible followers: assigned to this captain, not moving normally, not idle workers/haulers/builders/attackers, not thrown/swallowed/drowning/crushed/buried/dead or on a moving platform. Require sustained failed progress and validated safe destination. Healthy nearby squad must be unaffected. Prefer explicit optional rescue over silent automatic teleport initially.

User has NOT selected a teleport policy. They were unsure whether a rescue button would affect healthy squad; clarified it can be restricted to stuck followers. Do not add any teleport in the Recall All/Pikmin Speed build. Global Recall remains intentionally able to interrupt workers; normal whistle remains local. Full AI rewrite is not assumed necessary, but route adaptation/testing is real work.
