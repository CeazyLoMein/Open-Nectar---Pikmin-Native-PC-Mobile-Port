# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-27 11:51 EDT

**Overall project status:** Working installed P1/P2 retained. Continued the larger shared-area integration with actual guest population/animation/render code. Local checks passed; no new native build or phone test. Latest successful native build remains76. Playable two-phone gameplay is not enabled yet.

### Pikmin 1

- Current objective: complete the host-owned shared practice area with independent full-screen views and controls.
- What was investigated: actual PikiMgr pool/create/refresh, Piki init/death side effects, ViewPiki model/animation contexts, AnimMgr lazy loading, BaseShape/AnimContext render-time clocks, host capture and complete actor frames.
- Root cause or leading hypothesis: ordinary guest birth/death would replay gameplay effects/counters/seeds; a fixed local cohort cannot display host population changes. Normal animation selection can load assets or run gameplay callbacks. BaseShape previously treated only legacy two-pass rendering as presentation, so a held snapshot guest could still advance a separate animation clock.
- Files changed: pc_coop_world.h/.cpp/hooks; NEW pc_coop_pikmin_visuals.cpp; PikiMgr.h/ViewPiki.h, pikiMgr.cpp and shapeBase.cpp; PikminState wire codec/tests; CMake source list and actual-source fixtures/check runner; journals.
- Source changes implemented: explicitly admit a completely dormant initialized local PikiMgr pool; keep all slots OUTSIDE its live population. Complete host snapshots atomically choose local display slots for new, retained, removed and recolored Pikmin. Validate all IDs/session/epoch/captains/capacity/resources/poses before any actor/model write. Removed IDs disappear without normal kill, death statistics, sprout creation or work interruption. Pool/scene reuse invalidates ownership and suppresses stale normal rendering. Guest display directly samples both host animation channels with listeners disabled; no FSM/action/animation events run. Per-device original or installed HD body/leaf models draw locally. Held shape clocks stay frozen and use presentation matrices even outside old deterministic netplay.
- Tests and results: actual adapter plus actual pool admission/300-Pikmin multipart fixture MSVC PASS; compile-out PASS; new actual visual translation unit/resource/render fixture MSVC and Clang/core analyzer PASS; actual world TU/fixture Clang PASS; prior authority/view regressions PASS;6 mandatory-check runner tests PASS. Rebuilt networking24/24 PASS plus real encrypted socket/room/bootstrap/input probe PASS with normal localhost access. Final malformed pose-wire regression PASS. Two deliberately broken controls compile and correctly fail (skip final pose validation; remove end-frame clamp).
- Confirmed working: these are LOCAL source fixtures, not real phone visuals. Build68 remains installed and user-accepted for prior solo/connection/menu tests. Build76 native/package success validates its earlier source, not this batch.
- Remaining issues: full world baseline still needs enemies/items/Onions/jobs/HUD/interaction state; actual owner-thread room/load/input driver is incomplete. Captain animation/health/full cursor state and smooth render interpolation remain pending. The new guest display population intentionally contains no live AI/jobs; host gameplay input must drive the real host population. Trusted scene loading must ensure required animation data is loaded; packet-selected missing data rejects atomically and NEVER starts disk loading. No playable Start exposed.

### Pikmin 2

- Current objective: preserve its last user-confirmed working build while P1 online integration continues.
- What was investigated: no P2 runtime/source investigation in this batch.
- Root cause or leading hypothesis: none new.
- Files changed: no P2 game files. Shared networking Pikmin visual schema advanced from1/38bytes to2/50bytes; no P2 update/build or multiplayer adapter enabled.
- Tests and results: no new P2 build or phone test.
- Confirmed working: last user-confirmed launch/gameplay and repaired audio retained; full campaign completion remains unverified.
- Remaining issues: later stronger campaign testing and P2 online adapter.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental.
- Starting commit: 6699108ac4ae81a0b23dcf7bb976ccbf509abc5a; fetched origin still matched before saving this batch.
- Latest commit: this checkpoint is saved with subject `Integrate guest Pikmin populations and host-sampled poses [skip ci]`. Its resolved post-push hash is recorded in the accessible Exact Resume State.json.
- Commits created: one scoped population/pose/render/schema/test/journal checkpoint, with [skip ci].
- Changes pushed: normal development checkpoint only, no release/history rewrite.
- Uncommitted changes: batch is saved with this report; final accessible state records post-commit status.
- GitHub Actions run IDs: last independently verified native run40393742757 / Build76 / source0ced5bbe83504842602cd03872409dc584065169.
- Build results:76 SUCCESS. This batch has NOT had Apple/full-engine compilation or hardware validation. No77 requested.
- Artifacts produced: none new. Private Build76 IPA5299633bytes SHA25666ad7aa47f99465874fb676ae1c815fd709782a63df1e1785d3acd621ab7ba16, artifact12686618220; keep installed68 and65/54 rollback.

### Next steps

- Next Pikmin 1 task: integrate the complete bounded practice world and owner-thread room/bootstrap/area/input driver with this population renderer. Confirm all required world state and assets before Ready. Keep host simulation tick independent of phone rendering, including120FPS option.
- Next Pikmin 2 task: preserve baseline now; deeper testing and its online adapter later.
- GitHub/build task: continue meaningful related integration batches and local regressions. The next native build must require all17 admission/view/authority/population checks, full game build, existing room/socket gates and packaging checks. Do not build each helper separately.
- Anything requiring my involvement: nothing now; no USB/reinstall/new phone test. Keep working apps installed.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: guest visual lifecycle and host-sampled Pikmin pose paths now exist in actual engine code. They are NOT a complete gameplay replica or room driver. Fixed live-cohort adapter remains a separate diagnostic path and cannot mix with dormant display mode.
- Important source-file locations: pc_coop_world_prepare_guest_visuals/apply_guest_visuals/draw_guest_pikmin; PikiMgr::pcCoopVisualSlots/SlotsValid; ViewPiki::pcCoopVisualReady/Validate/Apply/Draw in new pc_coop_pikmin_visuals.cpp; PikiMgr::refresh dispatch; BaseShape::updateAnim and AnimContext::animate in shapeBase.cpp. New tests/pikmin1_practice_population_test.py compiles the actual visual TU with controlled engine resources; capture fixture compiles actual world TU and actual admission method bodies.
- Relevant logs: workspace work/population-capture.log, population-visual-local.log, population-world-clang.log, population-visual-clang.log, population-network-suite.log, population-protocol-final.log, population-authority-regression.log, population-runner-tests.log, population-negative-controls.json. Previous76 log/receipt retained.
- Unverified fixes: full Apple/game compilation, actual appearance/animation/performance on phones, loaded animation coverage, full shared world and gameplay. Local HD fallback test does not prove phone pack rendering.
- Risks and warnings: wire schema2 is50bytes; schema1/38bytes is refused. Same-build/content room compatibility remains required while personal graphics/camera/audio/controls/touch/cosmetic models stay local. Explicit guest display admission requires no live or pending-destruction Piki slots; do not abandon a loaded local job to force it through. Never call normal Piki::doKill/initColor/setFlower for these replicas. All applies/draws and scene teardown run on the owning game thread. Clear context before heap/shape reset. Pool capacity refusal must not silently drop actors. No network-triggered lazy asset loading.
- Exact next actions: verify status/origin; inspect this batch; trace trusted practice loading to ensure empty guest pool and complete assets, then connect room ownership/bootstrap/load barrier/input/server ticks and complete world adapters. Use actual-source checks before one meaningful native build. Preserve separate solo/shared save slots, shared Onion stock, own squads/allowances, safe host pause/exact rejoin, durable recovery and PC cross-progression/internet/P2 objectives. Restart remains required after process-latched temporary practice card admission. No finale spoilers.

**END PROGRESS REPORT**

---

## Historical checkpoints — current entry above supersedes current-state claims below

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-27 11:13 EDT

**Overall project status:** Working installed P1/P2 baselines preserved. Build76 passed native compilation and packaging; the larger next integration batch is in source and locally checked. No Build77 dispatched. Real two-phone shared-area gameplay remains unfinished; the current phone screen is still a connection test.

### Pikmin 1

- Current objective: one host-owned shared practice world, each phone with its own full-screen camera and controls, before campaign co-op.
- What was investigated: actual PlugPikiApp frame loop, NewPikiGame update/draw/mode flow, GameCoreSection update/AI/cameras, Pcam camera-to-cursor writes, ViewPiki maturity/attachment rendering, and existing host/guest lifetime adapter.
- Root cause or leading hypothesis: stopping updateAI alone would leave a guest advancing clock/Node updates, movie/mode callbacks and gameplay messages in drawing. Camera controls also write gameplay cursor state. Applying mHappa alone leaves its displayed leaf/bud/flower model stale. These are source findings, not newly reproduced phone bugs.
- Files changed: games/pikmin1/pc_port/netplay/pc_coop_world.h/.cpp, pc_coop_world_hooks.h, pc_netplay_present.h/.cpp; include/GameCoreSection.h; src/plugPikiColin/plugPiki.cpp and newPikiGame.cpp; src/plugPikiKando/gameCoreSection.cpp and viewPiki.cpp; src/plugPikiNakata/pcamcamera.cpp; actual-source fixtures/mandatory practice-check runner and descriptions.
- Source changes implemented: admitted hosts start held, and only a matching session/epoch can grant running after readiness. Guests stay held even after invalidated bindings; they cannot obtain host authority. The actual frame enters presentation before update, known gameplay update/draw/mode/message paths are gated, and local controllers/own camera remain available. Camera recenter/drag cannot write authoritative aiming/input while held. Guest maturity selects the matching local model without invoking the local All Flowers cheat. Mouth attachment drawing cannot overwrite a held replica's position.
- Tests and results: strict MSVC actual adapter/pool/300-Pikmin packet fixture PASS, compile-out defaults PASS; actual local camera/HUD/Onion/audio branch fixture PASS; actual gameplay update/draw/frame/cursor/model fixture PASS across120 held frames; Clang diagnostics/core analyzer PASS;6 practice-runner/gate tests PASS;2 deliberately broken controls compile but correctly FAIL.20 pure network tests passed with restricted access;4 unchanged encrypted UDP tests timed out there and all4 passed with normal localhost access. No product networking fix was made for that environment failure.
- Confirmed working: Build68 remains the user-accepted limited phone baseline. Build76 source0ced5bbe83504842602cd03872409dc584065169 has an independently verified native IPA. New authority/camera/model source is locally checked only.
- Remaining issues: no room-to-game owner-thread driver, full accepted world baseline, dynamic replica birth/death/conversion/animation/job mapping, complete HUD/cursor/interaction state or actual phone gameplay yet. Additional render callbacks still need audit; do not call this an exhaustive guest-world proof. No playable Start is exposed.

### Pikmin 2

- Current objective: preserve its last user-confirmed working build while P1 co-op integration continues.
- What was investigated: no new P2 source or phone investigation in this batch.
- Root cause or leading hypothesis: none newly asserted.
- Files changed: none.
- Tests and results: no new P2 build/runtime test.
- Confirmed working: last user reports P2 launches and missing Pikmin/enemy/environment audio was resolved; full campaign completion is not verified.
- Remaining issues: later stronger campaign test and P2 online adapter; preserve existing installation/assets/settings.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental.
- Starting commit: 5d6d4b9169b63630f599a6a76628d59b27cc27b4; fetched origin matched before this checkpoint.
- Latest commit: this authority checkpoint is saved with subject `Hold replicated co-op worlds across engine update and draw [skip ci]`; its parent is 5d6d4b9169b63630f599a6a76628d59b27cc27b4. The accessible Exact Resume State.json records its resolved local/remote hash after commit/push.
- Commits created: one scoped source/test/journal checkpoint intended, with [skip ci].
- Changes pushed: normal branch checkpoint only; no history rewrite or stable release.
- Uncommitted changes: source/test/journal batch is being committed with this entry; any interrupted checkpoint must be recovered with git status before further edits. Accessible final state records post-commit status.
- GitHub Actions run IDs: latest verified native run40393742757 (Build76), source0ced5bbe83504842602cd03872409dc584065169.
- Build results: Build76 SUCCESS; new authority batch NOT compiled by Apple/Xcode yet. No new native run requested.
- Artifacts produced: no new artifact. Existing verified Build76 IPA5299633bytes, SHA25666ad7aa47f99465874fb676ae1c815fd709782a63df1e1785d3acd621ab7ba16, artifact12686618220. Build68 remains installed;76 is private engineering evidence.

### Next steps

- Next Pikmin 1 task: integrate guest population lifecycle and safe visual animation with the actual world baseline. Ordinary Piki::doKill is unsafe for replica despawn because it changes counters, plays death effects and can generate a seed.
- Next Pikmin 2 task: preserve working baseline; resume deeper testing/online adapter after the P1 practice milestone.
- GitHub/build task: keep related population/animation/world/input/room-driver changes in a larger batch. Use local checks until a meaningful integrated native checkpoint, then one P1-only build. Do not dispatch one build per helper.
- Anything requiring my involvement: nothing now; keep Build68. No phone connection, reinstall or new hardware test is requested.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: this is a source integration checkpoint, not a playable co-op release. Build76 validates the earlier fixed-cohort adapter only. Personal graphics/FPS120/camera/controls/touch settings are retained; no new frame-rate cap or texture downgrade.
- Important source-file locations: pc_coop_world.cpp authority/context; PlugPikiApp::idle phase/message guards; NewPikiGameSetupSection::update/draw; GameCoreSection::pcUpdateCoopHeldView/update/updateAI; PcamCamera::control; ViewPiki::refresh. New fixture tests/pikmin1_practice_authority_test.py exercises actual extracted branches with controlled engine leaves.
- Relevant logs: workspace work/authority-final-local.log, authority-clang.log, authority-world-clang.log, authority-runner-tests.log, authority-negative-controls.json, authority-gns-permitted.log. Prior Build76 receipt work/build76-package-verification.json and full log work/build76-p1-full.log.
- Unverified fixes: Apple/full-engine compilation and all phone behavior for this batch; dynamic/full-world replication, visual animation, complete HUD and new co-op interaction input are unfinished.
- Risks and warnings: a render-phase serial is NOT the authoritative simulation tick. Drive set_host_running with CoopSession::hostShouldAdvanceWorld after each session pump; keep pumping while held. Establish the complete world/local view before confirming loaded. Held gameplay mode input cannot itself unpause the world; the driver must route session controls. Preserve process-latched private card admission and restart-required exit. Do not reuse session IDs or wrap scene epochs. Do not enable old deterministic netplay unchanged: it locks30FPS/personal settings.
- Exact next actions: verify git/status/origin; read current authority entry; inspect Piki/ViewPiki creation/cleanup and animation callbacks; build a complete admitted baseline/lifecycle adapter, then wire owner-thread room/bootstrap/scene/input. Keep playable UI closed until those paths and local/native checks cover the bounded shared area. Later integrate campaign slots/shared Onion/per-player squads, disconnect/rejoin, durable recovery, internet, PC cross-progression and P2.

**END PROGRESS REPORT**

---

## Historical entries — use the current checkpoint above

## Build76 verified PASS; larger integration batches required

2026-10-26T21:03:01.111910+00:00 UTC. Run40393742757/source0ced5bbe83504842602cd03872409dc584065169 SUCCESS. Full log confirms expanded actual capture/pool/whole-squad/300-Pikmin packet fixture PASS; full native game BUILD SUCCEEDED;9 practice checks,12 room checks and real encrypted UIKit simulator runtime PASS; no cleanup errors. Artifact12686618220 SHA256c5409b50b594ef783566b8fc660ea8a085df32813c68ea06443d0090ae6d66bf and CRC verified; IPA5299633bytes SHA25666ad7aa47f99465874fb676ae1c815fd709782a63df1e1785d3acd621ab7ba16 UUID484f4c5d-796c-3b1e-b78c-60544382fced, ARM64 device, original identity/icons/notices checked. Retained privately under outputs/Build76-Pikmin1. No installation requested. Keep accepted68; P2 unchanged.

USER PROCESS CORRECTION: User asked why more builds follow successful builds.75 validated new startup/view code;76 validated newly added guest squad code, so these were distinct sources, not retries. Nevertheless prior requests for larger batches were not adequately reflected: internal pieces were sent to native CI too frequently. From here, group related lifecycle/animation/authority/input/scene-driver work toward a concrete two-phone practice milestone, run local regressions between edits, and trigger native CI for a meaningful integrated batch or a demonstrated failure requiring correction. Do not make one new native run the default for each internal API/helper. An Apple-dependent validation checkpoint may be justified by concrete evidence, but explain why and minimize it. This turn records76 and this policy ONLY; no next build triggered, no phone task.

Current engineering boundary: fixed-cohort actor apply is verified, not playable co-op. Birth/death/conversion/animation/jobs and complete world baseline/guest simulation authority/actual room-area-input driver remain incomplete. Next work continues toward an actual shared test area with independent views. Preserve independent personal settings/FPS120, working solo, existing apps/assets/saves, all queued campaign/recovery/internet/PC/P2 requirements. Full earlier reports below.

## Current run: Build76 — actual guest Pikmin cohort adapter

Run40393742757; source0ced5bbe83504842602cd03872409dc584065169; last observed IN_PROGRESS, no final result/new IPA yet.
https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40393742757

75/run40338639501 full native startup/view/networking/package SUCCESS independently verified. New source binds explicit host IDs to current local Pikmin and validates ALL captains/squad before any writes; rejects missing/extra/recycled/bad actors without partial movement. Local actual adapter fixtures/300-Pikmin reordered packet test/MSVC/Clang/compile-out and2 negative controls PASS. Fixed-cohort step only: population lifecycle, animation/jobs, full-world state, guest simulation authority and actual room/area/input driver still required. No playable Start enabled; keep accepted68 installed, no phone/USB task. P2/personal graphics/FPS120/settings unchanged. User reports result; no idle CI polling.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-26T20:13:32.229011+00:00 UTC (America/New_York user timezone).

**Overall project status:** Build75 SUCCESS independently verified. Next P1-only source batch extends the real guest engine adapter from captain transforms to a complete explicitly bound Pikmin cohort. It is internal, not playable online co-op. Keep accepted68 on both phones; no phone/USB/installation task. All previous objectives remain queued.

### Pikmin 1
- Current objective: authoritative shared-world integration, preserving the working solo build and independent personal settings.
- What was investigated:75 complete log/artifact/9 Apple practice receipts/12 room checks/real encrypted UIKit runtime/IPA; actual Piki/PikiMgr lifecycle and guest state mapping.
- Root cause or leading hypothesis: captain-only application can leave a partial world. Actor order/address reuse cannot identify the host's Pikmin safely. Ordinary Piki::doKill also changes GameStat counters, plays effects and can create a seed; replaying that as guest removal would duplicate host gameplay.
- Files changed: pc_port/netplay/pc_coop_world.h/.cpp; tests/pikmin1_coop_capture_test.py; project journals/implementation/objective queue.
- Source changes: explicit accepted session/epoch + host-ID to LOCAL live-Piki bindings, with no pointer/order guessing; all currently live local Pikmin required. Validate every captain and Pikmin BEFORE any engine write; apply transforms/velocity/facing/coherent previous position/health/maturity/local captain association together. Owner/action remain host metadata and do not execute or overwrite guest AI actions. Missing/extra/foreign/recycled/invalid actors reject the ENTIRE update. Captain-only apply is refused after binding a squad. Pool forget invalidates the complete guest context; scene exit clears all pointers. Bounded scratch storage reused for population checks instead of per-Pikmin tree allocation each frame.
- Tests and results: strict MSVC /W4 /WX actual adapter + existing capture/pool fixture PASS, including wrong sessions/epochs/kinds, duplicate IDs/pointers, unknown/missing population, changed local captain/color, bad final actor/NaN/Inf/health/maturity/owner/leader, clock rewind, unchanged metadata on rejection, cancellation of partial output, whole-scene lifetime and empty squads.300 Pikmin through real packActorFrame/ActorFrameReceiver with reordered fragments apply only after complete assembly. Compile-out fixture PASS. Final Clang/core-analyzer actual adapter + fixture PASS. Two isolated negative controls correctly FAIL when removing last-Pikmin value validation or Pikmin pool-lifetime invalidation. Python AST/diff PASS. Apple/full game validation for this batch PENDING.
- Confirmed working:75 macOS actual admission/view fixture runs + iPhoneOS syntax/full native app/package and real networking PASS.75 artifact12659725915 SHA256d8824bc53ba70e35b2e467ca339df2b35646ccee434b65d44ff737ab6d67e45f; IPA5299899bytes SHA2568c7eb9819a6ac8b3e04a282e42c1361713de55faff21aa6a797f23e2631f2b5f UUIDcf1a69ff-1596-3ff2-96b3-4c78da1ec885, existing icons/identity/notices preserved, no cleanup errors. No75 phone install requested.
- Remaining issues: this is a FIXED-COHORT visual/state step. It does not create/remove/convert Pikmin, reproduce animation/jobs/targets, freeze guest simulation, replicate enemies/items/Onions/campaign, or start an actual room/area. A population change currently rejects rather than guessing. Native UI still connection-only; no Start caller enabled. Do not attest a complete world from this adapter alone.

### Pikmin 2
- Current objective: preserve working port; later campaign coverage and online adapter.
- What was investigated: no new P2 code/phone behavior.
- Root cause or leading hypothesis: no new P2 failure under investigation.
- Files changed: none.
- Tests and results: no P2 job requested.
- Confirmed working: earlier user hardware report; full campaign unproven.
- Remaining issues: stronger campaign validation, later online integration.

### GitHub
- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: 4a8862c5451dc51c1be3d013959df6308740daa8
- Latest commit: new source commit recorded in Exact Resume State.json after commit.
- Commits created: verified75 documentation checkpoint4a8862c5; this scoped guest Pikmin source/fixture batch.
- Changes pushed: P1-only native validation for whole-squad adapter; no P2/workflow/graphics/FPS/settings changes.
- Uncommitted changes: checked after source commit.
- GitHub Actions run IDs:75/run40338639501 SUCCESS; next run recorded after dispatch.
- Build results:75 fully verified; next native result pending.
- Artifacts produced:75 IPA retained privately under outputs/Build75-Pikmin1; no new batch artifact yet. Build68 remains installed baseline.

### Next steps
- Next Pikmin 1 task: inspect exact next native result, then guest-only population lifecycle/animation and engine simulation/presentation separation, actual room/area/input bridge. Reuse local co-op camera/captain/squad paths; preserve independent personal settings/FPS120.
- Next Pikmin 2 task: preserve; broader campaign testing later.
- GitHub/build task: existing actual adapter Apple fixture automatically covers this expanded code; one P1-only run, no idle polling. User reports result.
- Anything requiring user involvement: nothing yet; keep68 and existing assets/settings/saves installed.

### ChatGPT continuation notes
- Important functions: pc_coop_world_bind_guest_pikmin, pc_coop_world_apply_guest_actors, pc_coop_world_guest_pikmin_state, shared prepareCaptains/commitCaptains and pc_coop_world_forget.
- Relevant logs: work/build75-p1-full.log, work/build75-p1-artifact.zip, work/build75-package-verification.json; work/guest-pikmin-final-clang.log, work/guest-pikmin-negative-controls.json and generated actual adapter fixture/binaries under work/coop-capture-*.
- Unverified fixes: new adapter Apple compilation/runtime and actual phone behavior; no real two-phone gameplay or thermal improvement claimed by this change.300-Pikmin fixture is an adapter/network transaction test, not a phone performance benchmark.
- Risks/warnings: use explicit engine-created identities, never pointer values from packets or local enumeration order. Guest AI must be suppressed by future driver. Keep mode/FSM changes out of plain snapshot assignment. Ordinary death/birth paths have host gameplay side effects and need a separate visual population adapter. World simulation still lives partly in newPikiGame::draw; skipping updateAI alone is insufficient. Temporary practice card remains restart-latched and Start needs clear restart UI before exposure.
- Exact next actions: verify native result for this exact source; implement safe replica population/animation callbacks, complete world baseline and engine presentation authority, then connect room startup/readiness/input. Keep queued shared saves/reconnect/host-loss/mid-day persistence/internet/PC/P2 work, all documented in COOP_OBJECTIVE_QUEUE.md and COOP_MOD_RESEARCH.md. No original install changes until a concrete playable milestone.

**END PROGRESS REPORT**

---
Earlier checkpoint history:

## Build75 SUCCESS — actual Apple practice startup/view checks verified

Verified 2026-10-26T20:02:22.080315+00:00. Source17e674e20aedf048aa0cea09de1c64ff87e1d962; run40338639501 attempt1; scene121626913542 and P1121631623643 SUCCESS. All9 practice checks PASS, including actual admission/start/cache/backend and camera/HUD/Onion/audio fixtures on macOS plus iPhoneOS syntax. Full native game BUILD SUCCEEDED;12 room checks and actual encrypted UIKit simulator health/socket runtime PASS; no cleanup errors. Artifact12659725915 SHA256d8824bc53ba70e35b2e467ca339df2b35646ccee434b65d44ff737ab6d67e45f and ZIP CRC verified. IPA5299899bytes SHA2568c7eb9819a6ac8b3e04a282e42c1361713de55faff21aa6a797f23e2631f2b5f, UUIDcf1a69ff-1596-3ff2-96b3-4c78da1ec885; ARM64 iPhoneOS/platform, existing app identity/icons/notices checked. Retained privately under outputs/Build75-Pikmin1; NOT staged as phone update.

This proves compilation/test/package validation, not real phone/shared-world gameplay. Keep accepted68 installed; no phone/USB task. P2 untouched. Next: actual guest Pikmin identity/state adapter and complete engine/world ownership/presentation/input integration; do not expose Start or attest complete world from captain-only transforms. All queued independent settings/FPS120/campaign/recovery/PC/P2 requirements retained. No new build for this documentation result.

## Current build: 75 — protected actual startup and independent views

Run 40338639501; source 17e674e20aedf048aa0cea09de1c64ff87e1d962; last observed IN_PROGRESS, no final result or new IPA yet.
https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40338639501

One P1-only batch: protected CardUtil producer gate/drain/private admission and cached MemoryCard reset; actual title/setup reuse; independent fullscreen local camera/HUD/Onion/audio selection and teardown. Local actual-source fixtures, MSVC/Clang checks,24 networking CTests,6 failure/gate regressions,5 identity/bundle checks and2 rejecting negative controls PASS. Apple/full engine and phone behavior pending. VIEW selection does not freeze guest simulation; complete shared world/engine bridge still missing. No Start/UI exposure. Keep accepted68 on both phones; no USB or installation task. P2 untouched. User reports completion; no idle CI polling.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-26T14:19:45.162331+00:00 UTC (user timezone America/New_York).

**Overall project status:** Resumed from explicit pause. Build74 remains the latest successful native package/runtime validation. This coordinated P1 source batch implements protected practice startup and independent fullscreen view selection. Apple validation is next. Online gameplay is NOT exposed; keep user-accepted Build68 on both phones. No phone/USB task.

### Pikmin 1
- Current objective: safely connect the accepted room to a disposable actual two-player area while preserving normal solo saves and independent personal settings.
- What was investigated: actual CardUtil producer/worker completion boundaries, cached MemoryCard file indices/data, direct title/setup route, camera/HUD/Onion/audio branches, legacy deterministic behavior and run teardown.
- Root cause or leading hypothesis: idle alone cannot prevent a new save job racing a root switch; old file/data/directory caches can survive admission. Existing fullscreen branches were tied to old deterministic mode, which also locks camera settings/forces30FPS elsewhere. Reuse the actual view paths without enabling that session.
- Files changed: CardUtil.h/cardutil.cpp, MemoryCard.h/memoryCard.cpp, new pc_coop_practice_start.h/.cpp, title/cardSelect hooks, pc_netplay_present.h/.cpp, pc_coop.cpp teardown, newPikiGame.cpp/gameCoreSection.cpp view branches, P1 CMake, four practice test/runner files and the existing experimental workflow.
- Source behavior: mutex-protected producer hold, nonblocking drain, explicit new private-card admission, safe pre-admission cancellation/failure retry, non-mutating readiness query, cache invalidation. Existing direct title/setup reused only after isolation, normal slot inheritance refused. Admitted practice remains process-latched; app restart required before normal solo. A future session driver must supply accepted-room intent, pump through drain/loading, timeout/cancel and show restart UI.
- View behavior: explicit player0/1 context selects own fullscreen camera/HUD/Onion and sound listener; invalid/nested/legacy ownership refused; actual co-op teardown clears view. No FPS/graphics/camera/control configuration writes. This is view selection ONLY; it does not suppress guest world simulation or attest a complete replicated world. No native Start/UI caller yet.
- Tests and results: strict MSVC actual-source admission/start/backend and view branch fixtures PASS; Clang/core-analyzer eight translation units PASS (final added race assertion subsequently MSVC compile/run PASS); 800 producer attempts, idle-window producer race, cancellation, invalid-path retry, busy-cache refusal and original bytes preserved. Actual camera/HUD/container/audio branch checks preserve ordinary solo/local split/legacy presentation. Two isolated negative controls correctly FAIL when removing producer hold or selecting the wrong audio listener.24 existing networking CTests PASS. Six new check-runner failure/timeout/gate regressions PASS. Two source-identity and three bundle tests PASS. Python AST/diff/structural workflow gate checks PASS; no full YAML parser claim.
- Confirmed working: earlier Build68 phone tests and user-reported solo baseline retained. New fixtures use controlled engine/OS/graphics leaves with real changed method bodies and real CARD backend, not a phone/GPU/full engine runtime.
- Remaining issues: game-thread room handoff/pump, actual complete world baseline and guest simulation/presentation separation, own controller/camera update mapping, world interactions, reconnect and campaign integration. Native compile/fixtures for this batch pending. No new hardware outcome claimed.

### Pikmin 2
- Current objective: preserve existing working build; stronger campaign validation/online adapter remains queued.
- What was investigated: no P2 code or phone changes in this batch.
- Root cause or leading hypothesis: no new P2 failure under investigation.
- Files changed: none.
- Tests and results: no new P2 tests/job requested.
- Confirmed working: earlier user hardware/audio report; full campaign completion unproven.
- Remaining issues: campaign coverage and later online development.

### GitHub
- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: c2d80471fa5bcc7d7a7d5001dc1a915be86a7b0a
- Latest commit: source commit recorded after this checkpoint in Exact Resume State.json.
- Commits created: scoped protected startup/view source and checks batch.
- Changes pushed: this source batch to ios-experimental, P1-only native validation requested.
- Uncommitted changes: checked and recorded after commit.
- GitHub Actions run IDs: latest completed74/run40265585036 SUCCESS; new run ID recorded after dispatch.
- Build results:74 real encrypted UIKit simulator runtime/12 room checks/full app/package PASS. New Apple checks: macOS compile/run and iPhoneOS syntax for BOTH actual-source fixtures, independent failure collection, mandatory original step outcome plus all nine receipt checks before IPA packaging. New per-check logs retained.
- Artifacts produced: no new artifact yet; verified74 IPA remains privately retained, Build68 remains phone baseline.

### Next steps
- Next Pikmin 1 task: inspect this exact native result, then continue actual room-to-engine driver and full-world/guest presentation integration. Do not enable Start using only captain transforms.
- Next Pikmin 2 task: preserve; resume broader campaign testing after P1 milestone.
- GitHub/build task: user reports new run; inspect complete logs and all new fixture receipts. No idle CI polling.
- Anything requiring user involvement: nothing until a concrete playable package is staged. Keep68; no USB/installation.

### ChatGPT continuation notes
- Important source-file locations: games/pikmin1/pc_port/netplay/pc_coop_practice_start.*, pc_netplay_present.*, games/pikmin1/src/plugPikiColin/cardutil.cpp/memoryCard.cpp/titles.cpp/cardSelect.cpp/newPikiGame.cpp and plugPikiKando/gameCoreSection.cpp.
- Relevant logs: work/practice-batch-clang.log, work/practice-checks-runner-test.log, work/practice-negative-controls.json, actual fixtures/binaries under work/practice-admission-* and work/practice-view-*;74 evidence retained.
- Unverified fixes: new Apple full app/source fixtures and actual phone behavior; guest full-world immutability and playable shared-world are NOT implemented by this view context.
- Risks and warnings: simulation advances inside newPikiGame::draw and other refresh callbacks; skipping updateAI alone is insufficient. Old lockstep mode still forces30/locks personal fields and is not enabled. Restart-only temporary routing is intentional until safe lifecycle restoration exists. New title restart guard needs a clear restart UI before exposure.
- Exact next actions: verify new run/source/package; add game-thread accepted-room ownership and continuous pumping through startup, supply scene readiness only after actual two-captain/world load, complete authoritative world/guest presentation/input adapter, then stage one concrete two-phone independent-view test. Preserve all queued research/settings/recovery/PC/P2 goals.

**END PROGRESS REPORT**

---
Earlier checkpoint history:

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

**Paused at user request:** 2026-10-26T13:39:41.923104+00:00. Stop development until resumed.

Repository C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port, branch ios-experimental.
Latest local/last fetched remote commit: c2d80471fa5bcc7d7a7d5001dc1a915be86a7b0a. No commit/push/build in this work segment.
Build74/run40265585036/sourcee896892cd0495dcf3bd064b2b7b9a6268833d291 passed; actual encrypted iOS simulator test, 12 room checks and IPA verified. Keep accepted Build68 installed on both phones. No phone/USB task. P2 untouched.

UNCOMMITTED IMPLEMENTATION, not ready for installation:
1. Actual CardUtil producer gate: closes under job-publishing mutex, drains existing work without blocking game loop, admits only the new private card, invalidates old directory/buffer pointers. Safe pre-admission cancellation, failed-path retry, non-mutating readiness query. Explicit worker idle initialization and exception-safe mutex guards.
2. MemoryCard::pcResetForCoopPractice clears old file indices, metadata and campaign byte buffer only after admitted/drained state. Personal settings untouched.
3. pc_coop_practice_start.h/.cpp wires protected requests into existing direct-title/setup route. No native UI caller is enabled. Admission precedes title exit; setup refuses a real-save fallback and inherited normal slot. After practice admission, app restart is required before normal solo.
4. pc_netplay_present practice-view context separates fullscreen local camera/HUD/container/audio selection from old deterministic netplay. Does not force FPS/camera/graphics/control settings. Actual newPikiGame.cpp/gameCoreSection.cpp branches reuse this context. No active caller yet. This is VIEW selection only, NOT guest simulation freeze/full-world replication.

VERIFICATION:
- Strict MSVC /W4 /WX compilation and actual-source admission/start/card fixture PASSED.
- Fixture tested an outstanding old job, 800 concurrent blocked producers, cancellation, invalid-path failure/retry, original-save byte preservation, actual private backend writes, stale cache reset and restart requirement.
- Diff whitespace check passed BEFORE the final view edits.
- Latest fullscreen view edits have NOT been compiled/tested yet. No Apple validation for any new work this segment. No new IPA/phone test.
- Existing card/backend tests and broader regressions need rerun once source batch is complete.

NEXT EXACT ACTIONS:
1. Inspect this uncommitted diff and saved snapshot; do not reset/reapply old installers.
2. Compile/test fullscreen context and actual camera/HUD/audio branches, including default solo/local split-screen preservation, both player identities, context teardown and legacy mode exclusion. Confirm no personal config writes/FPS cap.
3. Audit startup guards for failure/cancellation/return-to-title and rendering mutation boundaries. Actual world simulation runs inside newPikiGame::draw; skipping updateAI alone is insufficient to freeze a guest.
4. Continue game-thread room ownership/load/readiness and complete-world bridge before enabling Start Practice. Do not expose movement from incomplete captain-only state as a complete shared world.
5. Wire new admission fixture into existing Apple checks and run appropriate batch verification before source commit/push. Avoid another native build for documentation alone.

All queued objectives/research/independent personal settings/shared campaign/recovery/internet/PC/P2 requirements remain in ios/COOP_OBJECTIVE_QUEUE.md and ios/COOP_MOD_RESEARCH.md. Earlier full progress reports follow.

Uncommitted source status at pause:
```
M games/pikmin1/CMakeLists.txt
 M games/pikmin1/include/CardUtil.h
 M games/pikmin1/include/MemoryCard.h
 M games/pikmin1/pc_port/netplay/pc_netplay_present.cpp
 M games/pikmin1/pc_port/netplay/pc_netplay_present.h
 M games/pikmin1/src/plugPikiColin/cardSelect.cpp
 M games/pikmin1/src/plugPikiColin/cardutil.cpp
 M games/pikmin1/src/plugPikiColin/memoryCard.cpp
 M games/pikmin1/src/plugPikiColin/newPikiGame.cpp
 M games/pikmin1/src/plugPikiColin/titles.cpp
 M games/pikmin1/src/plugPikiKando/gameCoreSection.cpp
?? games/pikmin1/pc_port/netplay/pc_coop_practice_start.cpp
?? games/pikmin1/pc_port/netplay/pc_coop_practice_start.h
?? tests/pikmin1_practice_admission_test.py
```

Recovery snapshot: C:\Users\chazz\Documents\Open Nectar\2 - Progress and ChatGPT Handoff\Paused Work - Practice Admission and Views; includes tracked patch AND full copies of new/modified source with SHA256 manifest. These are private local backups; no game assets or credentials included.

---
Earlier checkpoint history:

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-26T13:20:09.142413+00:00 (UTC; user timezone America/New_York)

**Overall project status:** Paused at user usage limit. Build74 passed. Networking foundation is verified; actual online gameplay is not enabled. Keep accepted Build68 installed on both phones. No phone/USB or installation task now.

### Pikmin 1
- Current objective: connect the accepted room to a disposable two-player practice area without touching solo saves.
- What was investigated: Build74 full log, artifact, UIKit health and real encrypted socket execution, 12 room checks, IPA structure/resources; startup and rendering entry points.
- Root cause: Build73 incorrectly gave slow simulator installation/launch the short native execution allowance. Build74 separates setup deadlines from execution deadlines; actual health and socket tests now pass.
- Files changed this checkpoint: status/progress/handoff documentation only. Build74 source changed three runner files; game source unchanged by that batch.
- Tests and results: GitHub74 SUCCESS; health PASS; encrypted socket/session PASS; 12 room checks PASS; artifact SHA/ZIP CRC and unsigned ARM64 device IPA/platform/UUID/icons/notices verified; cleanup reports no errors. Local runner batch previously passed 38 regressions.
- Confirmed working: existing solo and Build68 connection behavior by earlier user tests. Build74 is compiler/simulator/package validation, not new phone gameplay validation.
- Remaining issues: real practice startup, host simulation and guest full-world rendering, independent views/input, actual Onion adapter, disconnect recovery, campaign integration and internet transport validation.

### Pikmin 2
- Current objective: preserve working port; return after P1 online foundation.
- What was investigated: no new P2 changes or tests this checkpoint.
- Root cause or leading hypothesis: no new P2 failure under investigation.
- Files changed: none.
- Tests and results: no P2 job in this P1-only run; earlier user reported working audio/gameplay.
- Confirmed working: earlier user hardware report, not a full campaign guarantee.
- Remaining issues: stronger campaign coverage and later online adapter.

### GitHub
- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: 5a11e7772f013bb69472a975d6ad4c4873e231f9
- Build74 source: e896892cd0495dcf3bd064b2b7b9a6268833d291
- Latest commit: documentation checkpoint recorded in Exact Resume State.json after commit.
- Commits created: documentation-only pause checkpoint, [skip ci].
- Changes pushed: documentation only; no extra build requested.
- Uncommitted changes: none before checkpoint; checked again after commit.
- GitHub Actions run IDs: 40265585036, Build74 attempt1.
- Build results: SUCCESS, including native runtime gate.
- Artifacts produced: artifact12627177472; IPA 5294015 bytes, SHA256 3179f2211e39d53341ebac28b143f25d62614bf50e9231c4694d9f88edb24ee4, executable UUID 3e5b2379-4fb7-3ac7-92b0-27381b14edbd. Retained privately in outputs/Build74-Pikmin1, not staged as the next phone update.
- Build link: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40265585036

### Next steps
- Next Pikmin 1 task: protected practice-area startup and real two-player engine bridge.
- Next Pikmin 2 task: preserve; resume broader validation after P1 milestone.
- GitHub/build task: no repeat build for documentation; batch meaningful driver changes and checks before next P1 run.
- Anything requiring user involvement: nothing now. Keep Build68; no installation or USB test requested.

### ChatGPT continuation notes
- All earlier additive objectives remain in ios/COOP_OBJECTIVE_QUEUE.md; four-mod research remains in ios/COOP_MOD_RESEARCH.md. Personal camera, graphics/FPS120, controls, audio and touch settings must remain independent. Host-agreed gameplay rules must not overwrite personal saved preferences.
- Actual source route: titles.cpp direct intent -> cardSelect.cpp direct setup -> ONEPLAYER_NewPikiGame -> gameCoreSection.cpp pc_coop_begin_run and two Navis. Native room is currently connection-only.
- Save safety: pc_card_begin_coop_practice provides process-latched isolated empty temporary card. Before invoking it, hold new CardUtil producers and drain pending work before scene teardown; idle alone is insufficient. No unlatch exists; app restart needed before ordinary solo resumes.
- Guest freeze hazard: newPikiGame.cpp::draw around2656–2706 advances world clock, Node update and game AI. Skipping only GameCoreSection::updateAI will NOT freeze guest. Audit draw-side mutations and presentation-role gates before actual replication.
- Reuse local co-op captains/cameras/squad ownership. Do not blindly enable old deterministic netplay: it forces30FPS and locks some personal camera settings; upstream catch-up also relies on drawing for simulation behavior.
- Relevant logs: work/build74-p1-full.log, work/build74-p1-artifact.zip, work/build74-package-verification.json. Earlier73 evidence retained.
- Unverified fixes: actual practice gameplay/guest world, phone74 behavior, full campaign and internet play remain unverified.
- Risks: unsafe title/card transition can race queued save work; render callbacks mutate simulation; no claim of mid-day persistence or exact host-loss recovery yet.
- Exact next actions: inspect clean head and saved state, finish startup/UI/render audits, implement protected practice admission with explicit ownership and readiness, then full-world baseline/input/camera bridge and meaningful regressions. Do not request a phone test until a concrete playable milestone exists.

**END PROGRESS REPORT**


---
Previous checkpoint history follows.

## Build74 dispatched — measured simulator phase-budget correction

Source e896892cd0495dcf3bd064b2b7b9a6268833d291; run40265585036; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40265585036; last observed IN_PROGRESS, no result/IPA yet. Three Python runner files only: separate install180s, launch90s, then health20s/native90s result waits after launch; phase receipts/accurate failed-operation classification; related cleanup60s/diagnostics45s. Actual native failure predicates/zero exit/ordered START+PASS/noFAIL and mandatory package gate unchanged. Local38 regression tests/syntax/diff PASS, including measured95s install+37s launch and strict stalled-native failure. Apple execution of revised budgets pending. No new workflow/game/test-body/P2/FPS/graphics/phone changes.

73/run40261792715 full P1 game/BOTH UIKit test apps/card/12 checks PASS, health installation killed by OUR20s combined setup/execution budget error; native code NOT RUN/no IPA. Same-run successful scene install95s establishes mismatch; exact older service-hang causes remain unproven. Keep accepted68 installed, no phone task. All additive objectives/research/personal settings retained. Actual protected practice area driver still next after native evidence. User reports result; no idle polling.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-26T03:44:52.943583+00:00

**Overall project status:**73 game and both UIKit test apps compiled; a confirmed runner timing mistake stopped health installation before native testing. Phase-separated timing fix implemented/local38 PASS; Apple validation pending.68 remains accepted phone baseline; actual co-op practice not yet exposed.

### Pikmin 1

- Current objective: Correct test setup timing, then actual disposable two-phone area with independent settings.
- What was investigated:73 full P1 and successful scene logs, artifact CRC/SHA, nested test app identities/binaries, exact install/launch timings and timeout accounting.
- Root cause or leading hypothesis: Confirmed20s health budget incorrectly included install/launch; successful installation in same run took95s. Earlier simulator-only diagnosis was too broad for73. No game compiler error.
- Files changed: tests/ios_coop_app_executor.py, ios_coop_app_executor_test.py, run_ios_coop_socket_probe.py and journals. No workflow/native/game code changed in this repair.
- Tests and results:73 scene/full game/both UIKit apps/card/12 room checks PASS; health install timed out before code, no encrypted fixture run/IPA. Repair38 host regressions/syntax/diff PASS. Real revised runner Apple runtime pending; no new phone evidence.
- Confirmed working:68 user phone baseline;70 attempt2 native helper runtime;73 actual UIKit wrapper SDK builds verified, not executed.
- Remaining issues: Real test app execution, actual area/controller/camera/guest presentation driver, shared actions/world/campaign, recovery/internet/PC and P2 adapter.

### Pikmin 2

- Current objective: Preserve working P2.
- What was investigated: No new symptom.
- Root cause or leading hypothesis: None new.
- Files changed: None in P2.
- Tests and results: No new P2 build/phone test requested.
- Confirmed working: Earlier user reports, not retested here.
- Remaining issues: Longer campaign testing and later co-op work.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; branch ios-experimental.
- Starting commit: 6d3aef0ea84d38b59d50f58066727ae53f9db89b, clean/matched fetched origin.
- Latest commit: New phase-budget source checkpoint; exact source/run saved after push.
- Commits created: Phase-specific simulator install/launch/execution timing batch [ios-build] [ios-p1-only], then dispatch journal [skip ci].
- Changes pushed: One P1-only build intended; no73 retry and no unrelated workflow/security changes.
- Uncommitted changes: None after checkpoint.
- GitHub Actions run IDs:73/run40261792715 failed; scene121375548655 PASS; P1 job121378419870 compile PASS/runtime gate FAIL. Next run pending exact lookup.
- Build results: Full game and both test apps compile PASS; test installation timed out; actual networking NOT RUN.
- Artifacts produced:73 artifact12625991403 SHA2566a644473c2ed4fb67868292f4c4ce4decb29500846561a790d8b0e6e90d560ec, CRC PASS, game/test apps+diagnostics. Nested test apps checked ARM64 iOS Simulator. NO IPA.68 remains installed/current accepted build.

### Next steps

- Next Pikmin 1 task: Verify phase timings, actual health/native test completion and package in next run; then real protected practice driver with independent views/settings.
- Next Pikmin 2 task: Preserve working app; later stronger validation/adapter.
- GitHub/build task: One grouped P1 source validation. No idle polling; user reports result.
- Anything requiring user involvement: Nothing on phones. Keep68 installed; phones may close/disconnect.

### ChatGPT continuation notes

- What another conversation needs:73 proves UIKit app compilation, not execution. It timed out INSTALLATION because our20s execution deadline included setup. Successful same-run scene installation took95s. Correct separate deadlines are now180 install/90 launch/20 health result or90 socket result after launch. This corrects evidence handling, not gameplay.
- Important source-file locations: tests/ios_coop_app_executor.py run_app/control_step/app-result.json; tests/run_ios_coop_socket_probe.py exact app-phase classification/owned lifecycle/gates. Actual socket fixture and UIKit apps unchanged.
- Relevant logs: work/build73-run.json/jobs.json/p1-full.log/scene-full.log/artifacts.json/p1-artifact.zip/failure-verification.json; work/build73-legacy/owned/app-tests.log. Accessible Build73 - Phase Budget Correction evidence folder.
- Unverified fixes: Revised runner on Apple; actual app/native networking runtime; all actual phone practice gameplay. Full product completion remains unmeasured.
- Risks and warnings: Separate setup allowance must never waive a real test failure. Missing/partial/failed native evidence still refuses IPA; no native retry. Maintain all queued personal camera/graphics/FPS120/control/touch requirements and optional per-player difficulty. Old replay forces30/locks camera and remains conditional candidate. Drain save worker before future temp-card admission/scene teardown; restart before solo after latch. Preserve apps/settings/saves/packs/P2.
- Exact next actions: Inspect next exact run/source and per-app phase receipt; require true native START/PASS/zero wrapper return and all gates. Then continue disposable real-area driver and saved research/queue, rather than more standalone foundations.

**END PROGRESS REPORT**

## 2026-10-27 — P1 co-op practice integration, before native build

User asked for continuous work until a meaningful build is submitted, larger batches, and preserving the installed P1/P2 baselines. Working tree starts at 8509f715. This batch connects the private, disposable-card practice area to the authenticated room, with two captains and separate small squads, a guest display, camera-relative input, pause/readiness, and explicit fail-closed behavior. It does not implement campaign co-op, enemies, Onions, internet, durable saves or seamless live reconnect. It has not run on either phone and its iPhone build has not yet passed.

Local checks: 25 network tests plus encrypted socket probe passed; actual host/guest capture/pool and captain visual fixtures passed; view/authority fixtures and 15 check-runner tests passed; changed game translation units passed a Windows Clang syntax pass using actual game headers. Full Apple compilation and physical behavior remain unverified. Guest may need assets already installed; the practice map uses locally owned original game material. P1 Build 68 is the previously accepted phone baseline; P2 is untouched. Practice uses process-latched disposable card storage: close and reopen P1 to return to solo. Preserve existing saves and settings.

Next: submit one P1-only native build, record its run and source revision, examine any failure logs and correct in batches. On success inspect IPA before staging. Phone test should begin only after successful packaging; first verify solo still starts, then both phones connect on the same Wi-Fi, each chooses Start Co-op Practice at title, Ready, and tries independent movement, throw, whistle, pause, and leaving. Do not claim these behaviors are verified until actually observed. Resume requires rebuilding the practice session after a disconnect for this first experiment; exact live rejoin and the full campaign remain planned.

## Build 77 dispatched

P1-only build 77, run 40579562780, source 02c3e5efa9ace37852db0d8b1d9859a653050ca6: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40579562780 . Status when dispatched: in progress; no IPA or hardware validation yet. Once the user reports completion, retrieve actual results/logs. If it passes, inspect the unsigned artifact and its identity before staging it in the user's accessible install folder. If it fails, batch the evidenced errors and preserve working P1/P2 installs. The user wants no polling while waiting and requests an audible notification when user action is needed.

## Build 77 failure and follow-up

Build 77, run 40579562780: startup passed; P1 failed before full application compilation. Actual logs show missing guest HUD methods in the view fixture, missing co-op input stubs in the extracted command fixture, and Apple's compiler rejecting ambiguous boolean precedence. Socket and room checks were skipped after the earlier failure, so their later gate errors were consequences. Fixed all three together; local view/authority, command scenarios and strict Clang checks pass. Room checks now collect independent diagnostics even after earlier failure. No IPA or device verification yet. Full log: work/build77-p1.log in the Codex workspace.
