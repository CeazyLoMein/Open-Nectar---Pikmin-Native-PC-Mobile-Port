# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** October25,2026 18:59 EDT.

**Overall project status:** User reports Build68 requested tests all good so far. Connection/UI baseline accepted within that limited test; actual shared gameplay is next and NOT implemented yet.

### Pikmin 1

- Current objective: Build first disposable two-phone gameplay prototype, separate cameras and captains; preserve normal campaign files.
- What was investigated: Clean current branch/fetched remote and actual room ownership, capture bridge, engine-free CoopSession, old captain transform helper and build guards.
- Root cause or leading hypothesis: No new failure reported. Remaining work is integration: native Done currently closes the link; host capture has no guest engine application; camera/input/session/area startup must be connected together.
- Files changed: Documentation/checklist only this turn. No game code or user phone files changed.
- Tests and results: T05/T07/T08 overall PASS by user's "all good so far" response; per-phone/per-step timing details not independently collected. Earlier68 all12 native preflight/full app/simulator/runtime/package checks passed. No new tests needed for docs-only checkpoint.
- Confirmed working: Limited Build68 menu/connection/Rejoin/game return test bundle by user report, with65 detailed LAN baseline retained.
- Remaining issues: No actual online world yet. Need retained link+game-thread pump, agreed disposable area/scene barrier, host input authority, guest actor application, separate camera/HUD/audio and pause/clean exit. Shared jobs/Onions/actions/campaign slots/checkpoints/internet/cross-device handoff later. No measured heat improvement; only hidden connection-menu waste reduction in68.

### Pikmin 2

- Current objective: Preserve working P2 until P1 initial gameplay prototype is established.
- What was investigated: No P2 issue or runtime audit.
- Root cause or leading hypothesis: No new issue reported.
- Files changed: None.
- Tests and results: No new P2 build or test this turn.
- Confirmed working: Earlier user-reported P2 runtime on both phones, not newly retested.
- Remaining issues: Broader campaign and future co-op adapter later.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental.
- Starting commit: 401b33be159e52eafc6a71aa619cbe684c348362; clean local/fetched origin matched.
- Latest source commit:54b873070d3ab331a6775e3a31aa85c8344c0ebf; new docs-only commit recorded in Exact Resume State.json.
- Commits created: Record Build68 user phone pass and actual gameplay integration next stage [skip ci].
- Changes pushed: Documentation/checklist only, no new native build.
- Uncommitted changes: None after checkpoint.
- GitHub Actions run IDs:68/run40232707062 SUCCESS;65/run40220611984 preserved baseline. No new run requested.
- Build results:68 previously verified full app/all12 native checks/simulator socket/package PASS; user now accepts requested UI/connection checks. Shared gameplay untested.
- Artifacts produced: No new artifact. Verified68 IPA SHA2567f4599e1acb5cbb63a9403e218c510b0f970c94a40ddb634eca1503cd396716b retained in Documents/Open Nectar/1 - Install on iPhone/CURRENT - P1 Build 68 - Menu and Rejoin.65 and54 rollback retained.

### Next steps

- Next Pikmin 1 task: Integrated disposable shared-area prototype: retain authenticated room/session outside native screen, validate area/readiness, host-owned two-captain movement, guest host-state rendering with separate fullscreen camera/input, pause on loss and clean solo return. Then independent-view T10 on both phones.
- Next Pikmin 2 task: Preserve working app; no user test now.
- GitHub/build task: No CI run just for docs; coordinate source/meaningful tests before next P1-only build.
- Anything requiring user involvement: Nothing now. Close P1 and disconnect phones. Next test only after verified prototype package and exact instructions.

### ChatGPT continuation notes

- What another ChatGPT needs: Build68 T05/T07/T08 overall user PASS, same-Wi-Fi connection/UI scope. No per-phone repeat metrics, heat, shared world, campaign or internet pass inferred.68 current accepted baseline.
- Important source: ios/ios_coop_room.mm owns current room; pc_coop_world.cpp/.h captures records; pc_online_navi.cpp is old optional transform helper; libs/nectar_net/coop_session.h/.cpp supplies engine-free session. Read current implementation plan's next integrated milestone.
- Relevant logs: work/build68-run.json/jobs.json/artifacts.json/package-verification.json, work/build68-p1-full.log, outputs/Build68-Pikmin1 and accessible Full P1 Job Log. Exact Resume State alongside report.
- Unverified fixes: Actual new gameplay integration not yet written. Normal player FPS/120, resolution, texture/models, saves and P2 unchanged.
- Risks/warnings: Do not simulate two independent campaign worlds or write user's solo card from prototype. Do not call actor-position snapshots a complete world or reconnect save. Native room link currently ends on Done. Rejoin remembers private invitation in memory only; app-kill recovery not supported. Preserve exact68/65/54 artifacts and existing backups.
- Exact next actions: Implement game-thread owned retained-session handoff, explicit disposable scene bootstrap/ready handshake, host authoritative two-captain input and guest application/camera, pause/exit lifecycle as one coherent prototype. Validate local actual-source paths before coordinated Apple build. Keep future T10 inactive until package ready.

**END PROGRESS REPORT**
