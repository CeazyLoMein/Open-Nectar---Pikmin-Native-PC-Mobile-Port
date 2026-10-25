## Build59 attempt1 infrastructure boot failure; same-run retry queued — October25

Run40162073334/source d698f880af334690551a9bfb692521aec1551739: scene job121075548313 compiled probe successfully but simctl bootstatus for iOS27.1/Duo timed out after180s BEFORE install/launch. Artifact12586923613 SHA256358852e725dd39114978ccee7e1b235e66871a76f77c5f313f905a37649ba2d2 downloaded+verified; failure.json stage=boot. Both diagnostic simctl spawn commands also timed out45s. No native app execution/error is evidenced; P1 job121078373671 SKIPPED, no IPA. Underlying simulator stall cause unknown; do not claim new gameplay regression or verified room fix.

Authorized rerun-failed-jobs POST accepted for SAME59; API now QUEUED/conclusionnull, unchanged source. Last immediate API counter still run_attempt1; requested next attempt, verify counter on next result. No new game source or new numbered build. Existing ARC correction/guard still awaits full Apple CI. No phone/install needed; user reports the retry result. Preserve working P1/P2 and avoid idle polling. If boot repeats, investigate runner boot partial output/host status and add bounded infrastructure-only recovery without suppressing real app assertions.

## Build59 correction dispatched — exact checkpoint

Run40162073334 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40162073334), sourced698f880af334690551a9bfb692521aec1551739; last API snapshot IN_PROGRESS, no conclusion.58 failed exactly one Objective-C ARC property/getter naming error in new room UI; renamed copyButton to clipboardButton. Local actual8-property synthesized-getter compilation PASS; negative control recreates exact error. Regression check and full iPhoneOS screen compile included in59. P1 only; P2/phones unchanged. Wait actual native/socket/private-code/package result, then stage verified IPA and conduct two-phone connection-only test.57 remains last full successful native/simulator result. No phone or install needed now; user reports59 passed/failed, avoid idle polling.

## Build58 failure confirmed and corrected — October25

Run40161054040/source4f8ac135 failed P1 job121074322192 at the early iPhoneOS Objective-C++ screen check; shared scene121072507969 SUCCESS. Full log has ONE compiler error: ios/ios_coop_room.mm:127 copyButton getter follows Cocoa owned-object naming convention under ARC. Renamed property and all3 uses to clipboardButton. Audited all8 properties and14 method selectors. Added a compiler regression test extracting actual declarations and synthesizing their getters without UIKit headers: corrected screen declarations PASS on installed Clang frontend with arm64-apple-ios15.0 ARC; original owned-object naming trap produces exact diagnostic (negative control PASS). Full native screen/runtime still require next Apple build. All prior19core and identity/package tests passed in58 before this check; no new IPA produced, no phone changes, P2 untouched. Correction plus guard will be one P1-only build; next exact run entry supersedes pending state.

## Build58 — exact current checkpoint

Source 4f8ac1356f69fa1f47bbfab1ab411ab1ac4b2a76; run40161054040 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40161054040), last API snapshot IN_PROGRESS, conclusion pending. P1 only. Native Host/Join CONNECTION TEST UI + actual source/base-data fingerprints, private-code join/content-rejection probe, local-network permission and verified bundle notices. Local identity/packaging tests, strict C++ probe compile and39 app policy checks PASS. Apple/phone behavior PENDING.57 independently verified SUCCESS (native+scene+actual encrypted simulator/session), artifact/IPA checked; omitted notices corrected in58 source. No new phone install yet. User reports58 passed/failed; after native/package PASS, stage update in Documents and ask for a short two-phone same-Wi-Fi connection test. No idle polling; no phone needed now. No playable co-op campaign yet; P2 preserved.

## October25 — Build57 verified; real phone room screen implemented

Build57/run40158088407/source03cd0be0 SUCCESS: scene+P1 and actual iOS27.1 encrypted UDP/session with2captains+60Pikmin. Artifact downloaded+SHA verified, native ARM64/package identity checked. Networking notices were absent in IPA due to CMake parent/target source-property scope; fixed in new batch with strict packaged-byte verifier.

NEW pending Apple/phone validation: Advanced Settings > Data > Online Co-op: Connection Test, native UIKit Host/Join/copy/paste/leave UI, OS-random private room, source/config fingerprint and actual installed base-data streaming SHA256, local-network usage description, safe sharing/background and peer-loss handling. No campaign starts or saves/actors/settings mutate. Runtime gameplay options and full engine adapter still required before playable co-op.2identity+2packaging tests, generated real source digest, strict new C++ probe translation-unit compile,39 app policy checks PASS locally. New Apple check includes actual private-code join+content rejection, strict native UI compile and exact shipped notices verification. P2 untouched. No phone needed until next native build/package passes. See latest progress report and following exact run checkpoint.

## Build57 dispatched — exact current checkpoint

Run40158088407: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40158088407
Source 03cd0be08157613b020cb59c678271b44065a997, ios-experimental. Last API snapshot IN_PROGRESS, conclusion pending. P1 only plus shared scene and new iOS simulator real encrypted socket/session probe. No new artifact or phone runtime verified. Local19 core tests + new strict C++ probe compile +4 diagnostic-runner tests +39 app identity/storage checks PASS. P2 is not rebuilt. No phone needed. User should report passed/failed when57 completes; avoid idle polling. After reading actual Apple result, proceed with game Host/Join, actual source/content identities, accepted world loading and guest engine/camera integration. Current apps stay on working54/previous P2.

## New Apple encrypted transport batch — October24 session

Implemented distinct ios-arm64 and ios-simulator-arm64 pinned dependency builds, native matching hostprotoc, platform/SDK/pin-specific successful-cache receipts, static dependency notices, opt-in P1 encrypted transport linkage and real UDP/GatedTransport/CoopSession runtime probe. Probe checks wrong secret refusal, compatible join, both captains+60Pikmin atomic transfer, ready/pause/background/marker/disconnect flow. CLI runs only on iOS Simulator, rejects wrong-platform ARM64 and retains exact runtime/binary evidence.19 core tests, strict new C++ translation-unit compile,4 runner failure-path tests and39 app identity/storage checks PASS locally. Apple compilation/runtime PENDING next P1-only build. No game UI or live online mode yet; no phones needed. P2 source and normal P1 settings/saves preserved. See latest progress report and subsequent exact run entry.

## Build56 verified SUCCESS — 2026-10-24 America/New_York

Run40154273299, sourceb28a5d7b13037c68c76e66d730dd86fc679df59c. Both shared scene121052160673 and native P1121055004543 succeeded. Full P1 log and artifact upload metadata saved privately.18 core tests and actual P1 capture-to-receiver fixture passed in CI. Package binary was not downloaded/independently inspected in this status phase; no new phone install requested. The later researched session/pause/marker batch a5bd4690b3540b04c01d565ebcd83bea57d14e20 has19 LOCAL tests+Clang PASS but is NOT in56 and still needs Apple validation with upcoming integration. No co-op phone gameplay has been verified.

Next concrete work: build/prove encrypted iOS transport and generated source/content compatibility identities, then connect accepted Room/scene to CoopSession. Add explicit Host/Join prototype UI and guest actor/camera/audio integration using disposable campaign data. First user test will be actual two-phone connection and independent captains/views on the same Wi-Fi; shared-world actions/Onions/save/reconnect and different-network tests follow. Keep working54 and53 rollback; no phone needed now. P2 preserved.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-24 22:43 EDT

**Overall project status:** User authorized researched, fully developed co-op features. Primary-source comparison completed; feature plan saved. Implemented authenticated session/data adapter, loaded/ready gates, shared pause/interruption policy, typed partner markers and bounded actor update pacing.19 local tests and Clang PASS. No usable phone co-op mode yet. Build56 is previous actor-frame source and still running; new source saved without another immediate native run.

### Pikmin 1

- Current objective: Turn researched co-op design into a complete safe two-player session foundation, preserving normal54.
- What was investigated: Nintendo Pikmin3 leader/squad guide; Stardew developer multiplayer FAQ; Factorio latency/traffic postmortems; Mindustry developer server snapshot source; Deep Rock developer teammate/waypoint notes; Grounded shared-world notes. Findings/adaptations linked in PIKMIN1_COOP_RESEARCH_AND_FEATURES.md. Live56 metadata: shared scene successful, P1 configuring; no completed native result yet.
- Root cause or leading hypothesis: Complete actor frames alone don't define readiness, safe pause, mobile interruption or authoritative command permission. Protocol now models these explicitly. Stale queued status must never revive a timed-out phone. Previous loopback reconnect fixture tried opening a new connection before draining old closed-connection events; corrected lifecycle and verified re-auth/new-scene path. Initial new module compile missed explicit protocol header include, corrected locally before commit.
- Files changed: New libs/nectar_net/include/nectar_net/coop_session.h, src/coop_session.cpp, tests/coop_session_test.cpp; protocol.h/.cpp new types; core CMake/test list; experimental workflow Apple syntax checks; research/active-plan/status/handoff journals. NO games/pikmin1 gameplay source changed in this batch; no source flags activated.
- Tests and results:19/19 core test executables PASS with MSVC/O2/W4/WX. Clang diagnostic checks PASS including new source/test/protocol and existing actor/capture fixtures. Real authenticated gate + simulator test covers60owned actors, both-ready+loaded, host-only world advance, guest commands, independent pause reasons, background/foreground, heartbeat timeout and old queued packets, wrong ownership/epoch/sequence/payload, marker TTL/cooldown/nonfinite data, complete-update backpressure and20Hz network pacing. New source Apple/native runtime PENDING; no two-phone sockets/UI/gameplay verified.
- Confirmed working: Both phones' normal P154 launch baseline, Raye60FPS after restart; P2 working. Existing prototype actor-frame tests retained. New features confirmed only through core simulated peer tests, not real phone play.
- Remaining issues: iOS encrypted sockets/permission/session UI, generated build/content identity, scene/start-tick integration, real pause/lifecycle/input hooks, guest actors/fullscreen camera/audio, full world/Onions/workers/enemies/save/reconnect. Current confirmWorldLoaded is an adapter contract; the complete world bridge is absent. Fully fleshed design is saved; fully playable mode is not finished.

### Pikmin 2

- Current objective: Preserve working separate app while P1 prototype matures.
- What was investigated: No new P2 code this batch; future design accounts for forced shared cave travel and distinct local audio perspective.
- Root cause or leading hypothesis: No new P2 failure.
- Files changed: NONE under games/pikmin2.
- Tests and results: No new native/hardware validation requested.
- Confirmed working: User-reported P2 working on Raye's phone and prior original-phone baseline.
- Remaining issues: Longer campaign checks and P2-specific actor/cave/save adapter later.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; C:/Dev/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental; clean/fetched matching673581d9c6dda927d5a227e146e1dbc18d8f6ec9 before changes.
- Starting commit:673581d9c6dda927d5a227e146e1dbc18d8f6ec9.
- Latest commit: New research/session source exact commit written to external Exact Resume State.json after push.
- Commits created: One scoped research/session-feature source+tests+journal batch with skip-ci, preserving the in-flight56 native check.
- Changes pushed: New source batch; no extra native build immediately dispatched. Include it in the next meaningful P1 integration/validation run after56 result.
- Uncommitted changes: Only scoped listed source/workflow/docs until source commit; private evidence/helpers/assets never staged.
- GitHub Actions run IDs:56=40154273299, sourceb28a5d7b13037c68c76e66d730dd86fc679df59c. scene121052160673 SUCCESS; P1121055004543 in_progress/configuring at last check.55=40149838089 SUCCESS.
- Build results:56 pending.19 local tests/Clang PASS for NEWER source, NOT included in56. No claim native57 exists.
- Artifacts produced: No newly completed56/new-source IPA at this checkpoint.55 artifact upload metadata retained, not staged as a required update. Keep54 installed and53 backup.

### Next steps

- Next Pikmin 1 task: Actual iOS transport/build-content manifest, Room+accepted scene+new CoopSession wiring; then engine lifecycle/pause/input and guest actor/camera/audio bridge. Keep existing online flags OFF until isolated activation is deliberate. Current core is compatible-policy plumbing, not game mode UI.
- Next Pikmin 2 task: Preserve current game; later stronger cave/audio/save/system test and adapter.
- GitHub/build task: Save tested batch without redundant native run; inspect56 once completed, address real failures if any, then validate newer source together with next integration step.
- Anything requiring my involvement: None now; phones can unplug, no new IPA requested. User can report56 completion; do not consume usage polling idle.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User explicitly wants complete co-op with useful features, not merely two captains connected. New research document is the product/architecture feature contract. Accepted user constraints (together-only/one host/free same-area separation/own screens/shared stock/separate allowances/forced travel/health-led difficulty) remain. Independent offline play/cloud-host switching/host migration deferred despite Grounded supporting more.
- Important source-file locations: coop_session.h/.cpp/test: requires existing authenticated compatible GatedTransport, nonzero peer build/content digests and capability0x10000; MessageTypes67/68/69; WorldSnapshot carries prior complete actor frames. Active plan/research doc detail adapter APIs. Original FPS setting applies in gameplay constructor, user restart resolved it; no forced60 change.
- Relevant logs: PRIVATE work/coop-session-core-tests.log (final all19 PASS), coop-session-clang-checks.log, build56-result-run.json/jobs.json; research links in committed design document. No external game source/assets copied into repo.
- Unverified fixes: Actual iOS transport/UI/engine hooks and world snapshot/reconstruction remain absent. Heartbeat state API does not itself pause UIKit/game actors. Marker protocol does not draw markers yet. Caller must attest full engine readiness before confirmWorldLoaded; actor replica alone insufficient. No new native pass/phone co-op proof.
- Risks and warnings: Update pacing20Hz is networking only; user's selectable120 rendering not changed. Known reliable backlog64KiB defers whole updates; unseen transport queues require their own limits. Pause requests take network travel time. Secure rejoin identity/token and full world keyframe still to implement; tests re-authenticate the same private test gate. No accounts/security settings/paid services/other projects altered. No original saves reset; no finale spoilers.
- Exact next actions: Inspect56 when complete. Then implement actual native transport/manifest/accepted-scene glue and explicit experimental menu using disposable campaign data, wire pause/foreground and guest rendering. Add ownership-safe game actions/Onion transactions, full-world snapshots and two-network tests before release. Read PIKMIN1_COOP_RESEARCH_AND_FEATURES.md and active implementation plan first.

**END PROGRESS REPORT**

---

## Exact Build56 checkpoint — 2026-10-24 America/New_York

Source pushed: b28a5d7b13037c68c76e66d730dd86fc679df59c, branch ios-experimental. Build56 run40154273299, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40154273299. Last metadata status in_progress, conclusion pending; no native result/artifact verified yet. P1-only + shared scene validation.18 local core tests, actual engine capture-to-complete-replica fixture, compile-out and Clang PASS. Both phones keep working54; no new install requested. Raye60FPS confirmed after restart. No phone needed.55 separately verified SUCCESS. Stop idle CI polling; user will report completion. Next integration is actual authenticated iOS transport/session/scene compatibility and safe guest engine actor/camera application; current data replica alone isn't online gameplay. Full world, Onion engine transactions and snapshots remain.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-24 22:23 EDT

**Overall project status:** Both games launch on Raye's phone after P1 import-layout correction. Her P1 FPS change to60 was saved but only applied on re-entering gameplay; user confirms restart resolved30FPS. No phone needed now. Co-op55 passed native compilation; next batch implements complete captain/Pikmin frame packetization and an atomic guest-side data replica. This remains inactive engineering code, NOT online gameplay.

### Pikmin 1

- Current objective: Carry actual captured captains/squads through bounded multipart frames without applying partial/old/corrupt state.
- What was investigated:55 full P1 job121040694720 and scene job121038855551 both SUCCESS.17/17 macOS core tests and actual-engine fixture passed; artifact metadata recorded. Source frame pacing reads fpsMode in NewPikiGameSection constructor; closing settings persists selection but doesn't reconfigure current gameplay clamp. Raye live config fpsMode1, native2622x1206/1.0, AO0, VSync1; restart then user-confirmed60 works.
- Root cause or leading hypothesis: Confirmed FPS setting takes effect when gameplay reloads. For co-op, old packWorldDeltas splits a keyframe into independently decodable batches; none identifies completion of the WHOLE actor list. Replacing a guest world per batch would remove actors from other batches. New prototype frame envelope explicitly groups all parts and replaces only the complete validated replica.
- Files changed: libs/nectar_net/include/nectar_net/actor_frame.h, src/actor_frame.cpp, tests/actor_frame_test.cpp; nectar_net CMake; P1 pc_coop_world.h/.cpp actual capture-to-packets API; tests/pikmin1_coop_capture_test.py; existing experimental CI and journals. No P2 game change, normal settings/save behavior untouched.
- Tests and results: All18 core test executables PASS locally (previous17 unchanged passed; corrected new fixture rerun passed). Actual P1 capture/pool/packet-receiver fixture PASS, compile-out PASS, Clang diagnostics as errors PASS. New tests exercise1000 changing squads under loss/reordering/duplicates, timeout/non-sliding retries, stale frames/ticks/session/scene, checksums, malformed lengths/bounds, duplicate actors/captains, unknown schemas, nonfinite state and invalid owner/leader association. Two early assertions assumed a multipart frame that fit one packet and used stale test ticks; corrected fixture inputs, no runtime change to mask failures. New native Apple build pending.
- Confirmed working: User's P154 quick test baseline and Raye P154 title/music/controls launch plus restarted60FPS.55 native compilation/artifact upload only; no55 install requested. New receiver guarantees tested all-or-nothing DATA state; it does NOT write guest engine actors yet.
- Remaining issues: Actual iOS transport/session/invite UI, accepted build/content identity, guest actor creation/application/camera, host Onion-to-engine transaction bridge, enemies/jobs/items/world state and snapshot/reconnect. No claim online co-op is playable or full campaign tested.

### Pikmin 2

- Current objective: Preserve working P2 and its independent install.
- What was investigated: User confirms P2 works on Raye's phone.
- Root cause or leading hypothesis: No current P2 issue; source work remains paused.
- Files changed: NONE under games/pikmin2.
- Tests and results: No new P2 compilation/extended hardware test this batch.
- Confirmed working: User-reported normal P2 launch on Raye's phone, plus prior gameplay/audio baseline on original phone.
- Remaining issues: Longer campaign/device testing and eventual separate P2 co-op adapter.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; C:/Dev/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental; clean/fetched matching e2b9d47f5660fcd31b9bf292c16073fbc50428de at start of new co-op batch.
- Starting commit: e2b9d47f5660fcd31b9bf292c16073fbc50428de.
- Latest commit: New source/run and final docs checkpoint recorded in Exact Resume State.json after push.
- Commits created: One scoped co-op frame/adapter/tests/CI/journal batch with ios-build/ios-p1-only markers; no redundant P2 build.
- Changes pushed: New frame batch after passing local tests; exact source recorded externally once created.
- Uncommitted changes: Only scoped listed source/fixture/CI/journals until commit. No game assets/private phone logs staged.
- GitHub Actions run IDs:55=40149838089 source5bfa4fba17e9083deabeddc0033bc8a4a002ce06 SUCCESS. Next source/run recorded after push; NOT passed yet at this checkpoint.54=40145860255 SUCCESS, installed working baseline.
- Build results:55 P1+scene SUCCESS. New source Apple compilation pending; no phone install needed for plumbing-only check.
- Artifacts produced:55 P1 artifact12581478645 (5964282bytes, ZIP SHA256296fa46fa35f0498a3029c224cc2cab40cd67458759722e841cfc8c9e8b6e497); scene12581757882 (354779bytes, SHA256881ba0d61cd8f89b1f295114d6e01745fbdd08f61f179bbfc689361c70038376). Metadata/log upload verified, artifact binary NOT downloaded or independently package-verified this phase. No new55 staging/installation request.

### Next steps

- Next Pikmin 1 task: Real transport/session compatibility and accepted scene wiring, followed by bounded guest actor binding/application and each phone's own camera. Do not enable obsolete PC_ONLINE_ENABLED or independent guest simulation/save writes. Connect Onion authority to actual spawn/store and per-owner field limits, then remaining world state.
- Next Pikmin 2 task: Preserve working app; ordinary user testing optional.
- GitHub/build task: One P1-only Apple check for this batch, record exact source/run, stop idle polling. Native frame tests and actual capture fixture now in CI.
- Anything requiring my involvement: None now; both phones can disconnect. Keep54 installed. No new IPA requested until a usable prototype milestone.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Raye P1 black screen was my import path mistake, corrected and phone-confirmed. P1 data belongs in assets/dataDir; art beside assets. Both phones' selectable FPS remain30/60/120/monitor; fpsMode changes require gameplay reload in current baseline. New actor-frame module solves complete DATA transfer only, not rendering/AI/state restoration.
- Important source-file locations: actor_frame.h/.cpp (48byte NCF1 version1 envelope, session/epoch/frame/tick/whole-body size/FNV64 integrity/index/count); pc_coop_world_capture_packets validates increasing frame/tick and captures actual P1 actors before packing. Existing HostEntityRegistry/OnionAuthority remain.
- Relevant logs: PRIVATE work/build55-result-run.json/jobs.json/artifacts.json, build55-p1-full.log; actor-frame-core-tests.log (17 PASS then two faulty test assumptions), actor-frame-target-tests.log corrected PASS; actor-frame-engine-tests.log, actor-frame-clang-checks.log; raye-p1-fps-investigation.json and current-fps-settings.conf. No private evidence committed.
- Unverified fixes: No real phone-to-phone transport, session, actor application or new native56 result yet. No full-world snapshot/save or co-op gameplay. Existing solo rare bugs remain individually unverified.
- Risks and warnings: Authentication is EXTERNAL and REQUIRED: receiver only accepts bytes from authenticated HOST; FNV detects accidental corruption, is NOT a MAC. Accepted session/epoch comes from trusted scene barrier, never packet. One pending frame,128KiB/512actors/512fragments default bounds, fixed2s timeout; latest complete state retained through loss/corruption. Caller must not use stale packet output after false. Current maps include only captains/Pikmin visual schema, no targets/FSM/enemies/items/campaign. No simulation/game actor writes. Future transport should reliably deliver initial keyframes; this module supplies neither ACK/retransmit nor congestion control. Queued P1 buffers must obey engine scene-heap lifetime; owning vectors aren't proof they can outlive heap reset. Keep normals saves/settings/53/54, optional120 and AO-off baseline. No spoilers.
- Exact next actions: Inspect next Apple result once complete, then implement actual authenticated session/transport and guest actor bridge using complete frames. Continue P1_COOP_IMPLEMENTATION.md and SAVE_AND_COOP_RECOVERY_PLAN.md. No more phone setup required now.

**END PROGRESS REPORT**

---

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-24 America/New_York; recorded 2026-10-25T02:10:40.760072+00:00.

**Overall project status:** Raye now confirms BOTH games open. P1's black-screen startup was caused by this session's import layout error, now corrected on her phone and verified by a fresh user launch. No game source changed, no new IPA required. Co-op Build55 remains a separate engineering milestone.

### Pikmin 1

- Current objective: Resolve Raye's black screen after first-install asset transfer.
- What was investigated: Identified Raye's iPhone17Pro (iPhone18,1), iOS27.0.1. Read P1 Documents, three existing P1 crash reports, and a brief filtered startup log. Crash executable UUID1760960b-2d27-3a21-960f-2dcc404350c6 matches Build54, independently confirming her installed version.
- Root cause or leading hypothesis: CONFIRMED folder placement error in local import helper. It copied dataDir directly into Documents/pikmin1, while DVDOpen in pc_port/dolphin_stubs/dvd_stubs.cpp ALWAYS prefixes assets/. Jac_Start requests /dataDir/SndData; the missing expected assets/dataDir/SndData/Seqs/pikiseq.arc leaves Jac_InitEventSystem waiting for track0x20000. All three reports show Jac_InitEventSystem under Jac_Start/System::Initialise; iOS watchdog0x8BADF00D killed the unresponsive app. This is startup before drawing, distinct from the earlier in-game world-only black screen.
- Files changed: Phone only: relocated already verified disc roots into Documents/pikmin1/assets; kept art at Documents/pikmin1/art. Local work/import_raye_p1_assets.py now maps disc files to assets/* and art to art/* for future imports. Corrective helper work/repair_raye_p1_asset_layout.py used staged directory rename, refuses overwrite, and supports pre-activation rollback. Project/setup journals and accessible handoff updated. No P1 gameplay/audio/renderer source changed.
- Tests and results: Critical audio archive/bank/font hashes checked before move. ALL3529files/669952108bytes read back at CORRECT paths after activation with matching original SHA256; settings hash unchanged; saves/Load not written. Corrected importer syntax and mapping checked. User then confirmed title screen/music/touch-controls open normally.
- Confirmed working: Build54 on Raye's phone now launches normally, user-confirmed after repair. Original user's working app untouched.
- Remaining issues: Full campaign, longer performance/device-specific settings and existing rare gameplay bugs remain outside this launch check. Old Jac_InitEventSystem unbounded missing-resource wait still exists in source; no claim general startup failure handling was improved.

### Pikmin 2

- Current objective: Verify Raye's first installation; preserve existing source baseline.
- What was investigated: User's direct result after completed assets/art transfer.
- Root cause or leading hypothesis: No current P2 failure; P2 importer already used assets/* correctly.
- Files changed: None in P2 source or phone during this repair.
- Tests and results: User says P2 works on her phone; prior full2797file/1013544103byte readback transfer preserved.
- Confirmed working: User-reported normal P2 launch on Raye's phone. This is not a full campaign/audio-feature certification.
- Remaining issues: Longer gameplay/full story still unverified; P2 development remains paused while P1 co-op proceeds.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port, C:/Dev/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental; fetched origin and verified clean matching b1f020b30aa468e9d153412c853d553967281507 before journal edits.
- Starting commit: b1f020b30aa468e9d153412c853d553967281507.
- Latest commit: Documentation-only checkpoint for this repair is recorded in the external Exact Resume State.json after commit/push.
- Commits created: This repair needs only a scoped documentation commit with skip-ci; no game source change.
- Changes pushed: Updated journals/setup instructions; exact new commit recorded externally after push.
- Uncommitted changes: Only journals until documentation commit; private recordings/crash reports/assets/helpers not staged.
- GitHub Actions run IDs:55=40149838089, source5bfa4fba17e9083deabeddc0033bc8a4a002ce06. Last known in_progress from previous checkpoint, NOT refreshed during this phone repair.54=40145860255, sourcea7888f24009133fd3818355e35bfc5475c279e16, previously verified SUCCESS.
- Build results: No new build needed/triggered for relocating files.55's native result remains unverified at this checkpoint;17 local core tests+capture fixture previously passed.
- Artifacts produced: No new artifact this repair. Existing Build54 IPA unchanged;53 rollback retained.

### Next steps

- Next Pikmin 1 task: Continue co-op plan in ios/PIKMIN1_COOP_IMPLEMENTATION.md. First inspect55 once complete, then real transport/session/scene compatibility and guest actor application; bridge Onion authority to real engine accounting. Current capture is inert and is NOT playable online.
- Next Pikmin 2 task: No immediate code task; user can test ordinary gameplay when convenient.
- GitHub/build task: Save docs without extra CI; inspect55 once completion is reported, avoid idle repeated polling.
- Anything requiring my involvement: NOTHING else needed from either phone now; user explicitly told Raye can unplug. No reinstall or update for this repair.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Prior “all files verified” transfer receipt verified CONTENT but used wrong P1 parent directory. This correction supersedes the prior claim that the first P1 transfer was ready to launch. Both files and paths now verified and user-confirmed boot. P2 worked already. Preserve working apps/settings and prototype isolation.
- Important source-file locations: games/pikmin1/pc_port/dolphin_stubs/dvd_stubs.cpp DVDOpen prefixes assets/; games/pikmin1/src/sysDolphin/system.cpp Jac_Start uses /dataDir/SndData/; src/jaudio/pikiinter.c Jac_InitEventSystem waits on Jam_GetTrackHandle(0x20000). Correct install root Documents/pikmin1/assets/dataDir; control art Documents/pikmin1/art. No need to duplicate game data at both levels.
- Relevant logs: PRIVATE work/raye-p1-diagnostics contains three Oct24 crash reports205748/211009/211206 and live-p1.log; old imported ISO log.txt is historical developer output, NOT current iPhone startup evidence. work/raye-p1-layout-repair.json is definitive corrected-path verification receipt. Original transfer manifest/receipt retained for history; new repair receipt appended separately.
- Unverified fixes: No source-level startup timeout/recovery implemented. No claim online play, full campaign or all sounds tested. Fresh P1 boot with music/controls is user-confirmed.
- Risks and warnings: No unrelated files deleted, no original phone changed, no save/settings reset, no security/account changes, no proprietary assets or private reports committed. Keep120 selectable and AO-off known performance baseline. No final-boss spoilers.
- Exact next actions: Inspect55 when complete, preserve54 installed baseline and53 backup, continue co-op integration from documented active plan. Future P1 fresh imports MUST map extracted disc root under assets/, art separately beside it. Phone is no longer needed.

**END PROGRESS REPORT**

---

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF


**Date/time:** 2026-10-24 21:15 EDT

**Overall project status:** User's quick P154 check seems fine; proceed with co-op. New stable actor identity, Pikmin state codec and actual P1 read-only capture/lifetime hooks implemented and locally verified. Native engineering check: Build55 / run40149838089, source5bfa4fba17e9083deabeddc0033bc8a4a002ce06: in_progress / pending, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40149838089 Raye's two apps installed manually; both complete private asset/art transfers finished and verified. Her phone can be disconnected; runtime after import awaits feedback.

### Pikmin 1

- Current objective: Continue controlled co-op prototype while preserving54/53, existing settings and normal campaign.
- What was investigated: Actual MonoObjectMgr pool reuse/birth/kill, Creature init and stage heap teardown; old captain-only adapter and generic nectar_net records; Raye's startup folder contents and source assets.
- Root cause or leading hypothesis: Pool addresses are reused, so address-only identity can direct delayed commands at a different Pikmin. Worker/idle leader pointers change, so owner must persist independently. New registry prevents stale identity reuse, codec validates finite bounded state, hooks clear bindings before reuse/teardown. Raye's missing dataDir/art confirmed; likely first-install black-screen cause, fresh post-import launch not yet verified.
- Files changed: libs/nectar_net entity_registry.h/.cpp, pikmin_replication.h/.cpp +tests/CMake; games/pikmin1/pc_port/netplay/pc_coop_world.h/.cpp and minimal hooks; objectMgr.cpp birth/kill hooks plus already-audited missing diagnostic argument, creature.cpp init invalidation, gameCoreSection.cpp stage cleanup. P1 CMake opt-in NECTAR_COOP_WORLD; experimental workflow and tests/pikmin1_coop_capture_test.py. No renderer/input/save-setting rewrite.
- Tests and results:17 core network/accounting tests PASS with MSVC/O2/W4/WX (existing200000 decoder fuzz + simulated30-minute loss test, new20000 recycled identities and codec malformed/truncation/NaN cases). Actual capture translation unit and actual pool birth/kill methods compiled/run against controlled engine dependencies PASS: two captains/two Pikmin, retained working/idle ownership, no partial snapshot on bad state, stale pool command rejection, scene cleanup, inactive default. Feature-compiled-out fixture PASS. Clang diagnostics PASS for new source/tests and actual capture fixture. Negative control disabling lifetime invalidation causes fixture failure as intended. Build55 / run40149838089, source5bfa4fba17e9083deabeddc0033bc8a4a002ce06: in_progress / pending, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40149838089 No new live two-phone gameplay proof.
- Confirmed working: User's P154 brief smoke check fine; earlier53 graphics/keyboard/control edges. Raye P1 all3529files/34PNG/669952108bytes imported and SHA256 read-back verified, P1 preferences unchanged. Import does not itself prove launch/audio.
- Remaining issues: Live transport on iOS, host/join UI, guest actor creation/application, full-screen camera/input per phone, authoritative Onion spawn/store bridge and global field-limit reconciliation, complete world/jobs/enemy/item/campaign sync, atomic keyframes, exact-world save/reconnect/internet relay all remain. Capture is read-only, explicitly inactive unless begun; no online menu/playable campaign yet.

### Pikmin 2

- Current objective: Preserve existing source; finish Raye's requested game-file setup.
- What was investigated: Existing source manifest2768 disc assets +28 source touch PNGs, exact signed P2 app sandbox on identified iPhone17Pro.
- Root cause or leading hypothesis: Fresh installation also needed local proprietary assets, independent of co-op development.
- Files changed: NO P2 source. Added only assets/art in Raye's P2 sandbox; no save/preferences deletion/replacement. Original user's P2 phone untouched.
- Tests and results: Source hashes rechecked against prior canonical GPVE01 audit;2797files/1013544103bytes copied and read-back SHA256 verified; staging activated. No new P2 build or runtime test.
- Confirmed working: Prior user's P2 audio/gameplay; Raye's transfer is complete, launch after import unverified.
- Remaining issues: User's fresh relaunch/input/audio/pause feedback; stronger later campaign/cave/save tests before P2 co-op.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental; starting clean b5cb2b79ecdd4b9685b495a089f116902912f73a, fetched origin matched before edits.
- Starting commit:b5cb2b79ecdd4b9685b495a089f116902912f73a.
- Latest commit:5bfa4fba17e9083deabeddc0033bc8a4a002ce06 at checkpoint generation; new build source:5bfa4fba17e9083deabeddc0033bc8a4a002ce06. Final local/remote hashes saved in Exact Resume State.json after final push.
- Commits created: Scoped co-op capture/identity batch pushed at source above; documentation checkpoint afterward uses[skip ci].
- Changes pushed: Co-op capture code/test batch and current notes; one P1-only engineering build.
- Uncommitted changes: Current scoped code/journals before push; final external state records clean tree after checkpoint.
- GitHub Actions run IDs:Build55 / run40149838089, source5bfa4fba17e9083deabeddc0033bc8a4a002ce06: in_progress / pending, https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40149838089 Previous54=40145860255 SUCCESS, sourcea7888f24009133fd3818355e35bfc5475c279e16;53=40133259493;52=40131000336.
- Build results: New capture source local tests/Clang PASS; current new Apple native result pending.54 native/IPA plus user's quick check retained. No P2 CI now.
- Artifacts produced: No new prototype IPA verified yet. User can keep54; this engineering build is not a request for another phone update.54 SHA256cdf46924e6cb350eb1df571325254f55d0a479c4fab5e4e564ad950335b50ae5;53 preserved unchanged. Raye's prepared P1 copy updated to54 with53 moved to verified backup subfolder; P252 unchanged.

### Next steps

- Next Pikmin 1 task: Review one native prototype build after completion, then implement bounded reliable session/scene handshake, guest actor binding/application and full-screen per-player camera. Next bridge actual atomic Onion spawn/store and one squad/job/enemy/carried object. Existing read-only capture is not enough to play online.
- Next Pikmin 2 task: Raye reopen/basic audio/game check; retain paused source and later stronger campaign tests.
- GitHub/build task: One P1-only technical check; no idle repeated polling. No phone update/retest demanded just for invisible capture plumbing.
- Anything requiring my involvement: NONE to continue coding/CI. Both file transfers done; user already told phone can unplug and games need full close/reopen. Raye exact public iOS27.0.1 verified; no more need to ask model/version. Report only actual runtime failures when convenient.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Co-op explicitly authorized.54 very quick smoke check seems fine, not full campaign certification. Registry/Pikmin codec plus actual-engine read-only capture now exist, beyond previous Onion-only state. No live sessions started and NECTAR_ONLINE remainsOFF. Prototype capture compiled in CI via NECTAR_COOP_WORLD=ON but begins only via explicit future API; normal solo remains inactive. No original save format changed.
- Important source-file locations: ios/PIKMIN1_COOP_IMPLEMENTATION.md, SAVE_AND_COOP_RECOVERY_PLAN.md; new pc_coop_world_begin_host/pc_coop_world_capture/pc_coop_world_forget/pc_coop_world_end_scene in pc_port/netplay; HostEntityRegistry in libs/nectar_net; PikminState codec38bytes. Registry owner persists independently of current leader. Monotonic16-bit scene epochs must not wrap; transport session IDs must never be reused.
- Relevant logs: work/coop-capture-fixture, coop-capture-bin, coop-direct; coop-capture-negative.log; work/raye-p1/p2-import-progress.json and private source/transfer receipts. Public notes only metadata, no proprietary game files. New native run metadata saved in work/coop-capture-new-runs.json after push.
- Unverified fixes: Real iOS compilation of the new bridge until CI finishes; no two-iPhone actor/world synchronization/real network/reconnect/save proof. Post-import Raye game launch/audio pending. P154 rare bugs remain untested individually.
- Risks and warnings: Never serialize local addresses; guest packets must pass session/scene/lifecycle freshness and authenticated ownership checks. Capture records are NOT full AI/job/campaign or exact-scene snapshots. Do not treat each split datagram as a whole keyframe; full keyframe assembly/application must be atomic. Registry lifecycle hooks must precede pool reuse and heap reset. Read-only capture buffers currently belong to scene lifetime; future network queues require safe owned buffers across transitions. Preserve54/53/settings/AO OFF/user120 choice, avoid fourth-app requirement, no finale spoilers or security/account changes.
- Exact next actions: Record native source/run and clean Git state; inspect resulting compile after user reports completion; implement real iOS transport/handshake + guest visual/squad vertical on disposable data, then complete game authority/Onions and recovery. User/ Raye can meanwhile reopen both freshly populated apps; if still black inspect new evidence rather than re-copy blind.

**END PROGRESS REPORT**


<!-- BEFORE CAPTURE MILESTONE -->

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF


**Date/time:** 2026-10-24 20:39 EDT

**Overall project status:** P1 Build54 native compile/IPA/package verification PASS; staged for a brief optional phone regression check. New game fixes are not hardware-verified. Co-op development has started with tested shared Onion accounting; online gameplay is not yet integrated. P2 unchanged. Raye reports iPhone17Pro/public non-beta iOS; exact version/connection later when available.

### Pikmin 1

- Current objective: Preserve user-confirmed53, verify54 and continue the controlled co-op prototype.
- What was investigated: Completed Actions run40145860255, successful scene/P1 jobs, full P1 job/build logs, both artifact hashes, simulator result, ARM64 executable, bundle identity/SDK/icons and expected feature markers.
- Root cause or leading hypothesis: Preventive fixes address confirmed source hazards and carrying timing; rectangle rounding addresses numeric edge mismatches. No new evidence establishes the cause of the earlier rare black-world/stranded pair/moving-line symptoms.
- Files changed: This verification phase changes documentation only. Build54 contains prior407b7fa4 game fixes and a7888f24 co-op foundation/CI, described in PIKMIN1_COOP_IMPLEMENTATION.md. No extra game changes or build triggered.
- Tests and results: Native iPhoneOS compilation PASS; actual-method rectangle161200 cases/zero mismatches + Onion/carrying/damage/slot tests PASS;15/15 offline network tests PASS on macOS; Apple ARM64 new-fixture/authority syntax checks PASS; actual asset-free iOS27.1 simulator launch/background/resume PASS. Package digest, ZIP, ARM64/iPhoneOS, original ID, scene support, icons and ProMotion permission verified. Simulator is not the game on real hardware.
- Confirmed working: User's installed53 graphics/touch/keyboard baseline, full native resolution/1.00x with AO OFF reported120FPS.54 compiled and produced a verified IPA; not installed/tested by this phase.
- Remaining issues: Online actor/world synchronization, registry/engine bridge, camera/session UI, internet invites/relay and snapshot/reconnect still need implementation. Rare campaign issues and full-story coverage remain unverified. User does not need to reproduce every preventive bug or replay the story for this batch; a short launch/settings/input/carry/pause/resume check can detect obvious regressions while53 stays preserved.

### Pikmin 2

- Current objective: Preserve working game; later stronger stability tests and separate co-op adapter.
- What was investigated: None newly; no P2 job in54.
- Root cause or leading hypothesis: No new P2 issue diagnosed in this phase.
- Files changed: NONE under games/pikmin2.
- Tests and results: No new P2 compile/runtime. Existing52 native/IPA verification retained; earlier32 gameplay/audio user-confirmed.
- Confirmed working: User's previous installed working P2;52 package exists but is not newly phone-verified.
- Remaining issues: Raye's first solo install/assets/basic test; later cave/area/save/campaign test before P2 online.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental.
- Starting commit:4b6111091a086fa332a152e958889c6df6687f9b (clean at entry). Build54 source=a7888f24009133fd3818355e35bfc5475c279e16; fixes=407b7fa4f5479aeeb983de5c84a234d03641291e.
- Latest commit: Documentation-only verification checkpoint pending at this report creation; exact final local/remote SHA saved in friendly Exact Resume State.json after push.
- Commits created: No new game-source commit in this verification phase; documentation checkpoint only.
- Changes pushed: Documentation-only with [skip ci], no P2 rebuild or extra P1 build.
- Uncommitted changes: Only current scoped verification journals before checkpoint commit; confirm clean after push.
- GitHub Actions run IDs:54=40145860255; scene job121026926855 and P1 job121029524253 both SUCCESS. Prior53=40133259493,52=40131000336.
- Build results:54 SUCCESS. All15 offline co-op/network tests and full native P1 job passed. No hardware/co-op session result claimed.
- Artifacts produced: P1 artifact12581053357 SHA256aa0a36f05371f82349bdbf80844b83da9cbce9195ae4a90542fb47d42cbbd0bc; scene artifact12580922615 SHA2566ff701b72c9a1ad4b8dc06c9a63b1b4f49f4d0353ddcc2d7d87d1363cb98158c. Staged IPA=C:\Users\chazz\Documents\Open Nectar\1 - Install on iPhone\Pikmin 1 - Build 54 - Stability Update.ipa, 2835985bytes, SHA256cdf46924e6cb350eb1df571325254f55d0a479c4fab5e4e564ad950335b50ae5, executable UUID1760960b-2d27-3a21-960f-2dcc404350c6, original IDorg.opennectar.experimental.pikmin1, unsignedARM64/iPhoneOS SDK27.1/minimum15.0. Build53 original IPA rehashed and retained unchanged.

### Next steps

- Next Pikmin 1 task: Optional brief same-ID54 update/regression check; continue same-Wi-Fi disposable captain/squad prototype and actual engine registry/Onion bridge using the saved active plan. No full campaign/finale check demanded.
- Next Pikmin 2 task: Keep current game, no new build; Raye solo installation when ready.
- GitHub/build task:54 complete, no polling and no new build needed merely for documentation. Review any new actual failure before further fix.
- Anything requiring my involvement: Handle signing/install and brief phone feedback when convenient. Raye is using her iPhone17Pro now, so don't request immediate disconnect/use; exact public iOS version can be read when available. Her prepared P153/P252 folder remains unchanged until54 hardware feedback; nothing installed on either phone in this phase.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Co-op is explicitly authorized and underway; only the engine-free Onion authority is implemented.15 passing tests do NOT mean15 game/campaign scenarios or a real two-iPhone session passed. User asks whether rare fixes can be checked: explain automated targeted evidence plus a brief device regression check, not blind hope or a full story retest.
- Important source-file locations: ios/PIKMIN1_COOP_IMPLEMENTATION.md, ONLINE_COOP_DESIGN_NOTES.md, SAVE_AND_COOP_RECOVERY_PLAN.md; libs/nectar_net/onion_authority source/header/test; old captain adapter games/pikmin1/pc_port/netplay/pc_online_navi.cpp and pc_netplay_session.cpp. Normal online flags remainOFF until a usable integration exists.
- Relevant logs: outputs/Build54-Pikmin1/ios-build.log and ios-build-errors.md; work/build54-p1-full.log; work/build54-result-run/jobs/artifacts.json; work/build54-startup-runtime-verification.json; work/build54-verification.json. Friendly folder2 has verification/log copies.
- Unverified fixes: New54 device behavior, complete campaign, old NaN/black-world/stuck-rescue cases, all actual online gameplay/save/reconnect.
- Risks and warnings: Preserve53/settings, AO OFF and user-selectable120. No raw pointer/heap snapshot or arbitrary-tick normal-card writes. No fourth-app requirement, original save overwrite, host migration, paid relay/account changes or finale spoilers. Package backup isn't current phone-data backup. P2 remains paused.
- Exact next actions: Provide staged54/checklist → receive brief optional device result; independently advance controlled iOS transport/captain+squad vertical and registry/transaction bridge, then full host-owned world/recovery. Install Raye's P1/P2 once phone available, import private assets separately, validate her solo baseline before two-phone tests.

**END PROGRESS REPORT**


<!-- BEFORE BUILD54 VERIFICATION -->

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF


**Date/time:** 2026-10-24 20:14 EDT

**Overall project status:** User accepted P1 Build53 as the current working solo baseline and explicitly authorized beginning online co-op now. Preventive P1 upstream batch implemented and locally checked. First host Onion accounting component implemented/tested, but NOT connected to game actors or live networking. Raye install copies prepared; no installation/phone data changes performed. Pushed a7888f24009133fd3818355e35bfc5475c279e16 to ios-experimental. Build 54, run 40145860255: in_progress / pending; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40145860255

### Pikmin 1

- Current objective: Preserve working53, incorporate selected upstream campaign fixes, begin controlled online co-op development.
- What was investigated: Upstream release1.0.8 and main a6b09bfe, prior co-op/save notes, actual nectar_net and pc_netplay_session/pc_online_navi adapters. Last fetched origin matched8af39affa4c0c863ccaa1b41dd8b96538836faaa before edits.
- Root cause or leading hypothesis: Actual carrying retry used60 ticks regardless of user FPS, making intended2seconds=.5seconds at120. Several existing null/uninitialized/out-of-bounds/cache-lifetime hazards are confirmed in source. Main shared-edge rounding removes numeric rectangle gaps. These are preventive fixes; none is established as the cause of the old stranded pair, NaN/black world or motion-line symptom.
- Files changed: aiTransport.cpp retry/debug format; creatureMove.cpp collision-exhaustion null dereference; Demo.h/demoEvent.cpp/cinePlayer.cpp skipped Onion first-seed completion; SnakeAi.cpp/SnakeBody.cpp slot/array guards; dayMgr.cpp invalid-time fallback; damageEffect.cpp absent-captain guard; DrawContainer.h/drawMenuBase.cpp UI safety; drawGameInfo.cpp portrait-cache lifetime; pc_gfx.cpp rectangle edge math. New tests/pikmin1_upstream_safety_test.py. Separate libs/nectar_net/onion_authority.h/.cpp/test and CMake test registration; P1-only workflow checks.
- Tests and results: Actual-method fixture PASS for rectangle edges161200 cases/zero mismatches, first-seed skip/repeat/normal completion, missing/damaged captains, full/missing enemy mouth/target, invalid/dead carry target and retry timing30/60/120. Two negative controls restore old retry/rectangle behavior and fail as intended. Offline nectar_net15 test executables PASS with MSVC/O2/W4/WX; includes existing200000 decoder fuzz iterations,30SIMULATEDminutes with5% packet loss (live tick ratio.9982) and new10000 withdrawal/return cycles/40000 deliveries. No actual30-minute or two-phone session claimed. Preserved-display fixtures70 native-pixel checks,1820 touch/resize/layout checks, keyboard ownership PASS; scene contract26 + runner12 tests PASS. Clang warning/diagnostic checks also PASS for the actual-method fixture and new authority source/test. Apple ARM64/full game CI pending for this source.
- Confirmed working: User's installed53 sharper image, manual control edges, keyboard closed. At full2853x2007/1.00x with Ambient Occlusion OFF, user reports120FPS; keep higher quality and selectable120. New fixes are source/local-test verified only.
- Remaining issues: New source not installed/runtime tested; full story/rare cutscene/rescue/old black-world not certified. Co-op world replication, actor registry, engine transaction bridge, transport on iOS, full-screen per-player view, invites/relay, shared save/reconnect NOT implemented by the new accounting module.

### Pikmin 2

- Current objective: Preserve working game; prepare latest compiled package for Raye's solo compatibility test. P1 co-op first.
- What was investigated: Existing package hashes and bundle IDs; no new P2 source work in this batch.
- Root cause or leading hypothesis: No newly reproduced P2 bug; earlier audio/gameplay user-confirmed. Future upstream audit candidates remain queued.
- Files changed: NONE under games/pikmin2; existing P2 jobs/normal runtime unchanged.
- Tests and results: Build52 source a575ecf424008c7430da96a5082ffb7f68970dc1, run40131000336 compiled/IPA verified earlier. Copied package rehashed now; no new52 phone validation. Older32 audio/gameplay baseline preserved.
- Confirmed working: User's previous installed P2 audio/gameplay; do not equate this with testing newer52 on Raye's phone.
- Remaining issues: New phone/model/iOS details pending; assets/import + first run pending; stronger later cave/area/save/long-session test before P2 online.

### GitHub

- Repository: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port ; upstream SSunnKing same project.
- Branch: ios-experimental.
- Starting commit:8af39affa4c0c863ccaa1b41dd8b96538836faaa (clean local=origin).
- Latest commit: a7888f24009133fd3818355e35bfc5475c279e16 at report creation. Exact post-report local/remote hashes are in friendly Exact Resume State.json after push.
- Commits created:407b7fa4f5479aeeb983de5c84a234d03641291e P1 preventive batch; co-op/checkpoint commit pushed above.
- Changes pushed: Pushed a7888f24009133fd3818355e35bfc5475c279e16 to ios-experimental. Build 54, run 40145860255: in_progress / pending; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40145860255
- Uncommitted changes: Only this updated documentation checkpoint before final skip-ci commit; verify git status.
- GitHub Actions run IDs: Build 54, run 40145860255: in_progress / pending; https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40145860255 Previous53=40133259493 P1 SUCCESS,52=40131000336 P2 SUCCESS. No P2 build requested now.
- Build results: Current local tests PASS; current Apple compile/IPA/runtime not yet established.
- Artifacts produced: No new IPA from this source yet. Working P153 SHA256c483540e76cef95c002578724690fe8ebe649901b9a09906350ee0b93c5cff85; P252 SHA256fbf6b2512d91ccafc6c600ee8bddcdbbcef04a1c01ee0ea68da4c68fda40c793. Rehashed copies in Documents/Open Nectar/1 - Install on iPhone/For Raye - Start Here, with manifest and instructions. Original IPAs retained.

### Next steps

- Next Pikmin 1 task: Review one P1-only native run and verify artifact/package before an optional short carrying/Onion-skip/menu/resume hardware check. Preserve53 rollback and settings. Continue co-op actor/world vertical slice on disposable data.
- Next Pikmin 2 task: Raye solo install/asset import and basic audio/pause/resume test; no speculative P2 rebuild.
- GitHub/build task: Inspect the recorded run after completion; no idle polling.
- Anything requiring my involvement: Raye's iPhone model/iOS and connection/unlock when ready for installation; sign in/verification stays under user's control. A read-only USB inventory probe stalled and was stopped; no phone identified or modified in this phase. No need to keep the original game/phone connected for CI.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: Current user explicitly says start P1 online co-op; old notes saying online is future-only are historical/superseded. P1 ready for controlled prototype does not certify every story path. Preserve solo runtime; network flags remainOFF pending a real integration, not abandoned co-op work.
- Important source-file locations: ios/PIKMIN1_COOP_IMPLEMENTATION.md and ONLINE_COOP_DESIGN_NOTES.md; libs/nectar_net for reusable transport/identity/codecs + new OnionAuthority; games/pikmin1/pc_port/netplay/pc_netplay_session.cpp and pc_online_navi.cpp for old captain-only adapter; ios/SAVE_AND_COOP_RECOVERY_PLAN.md for exact-scene recovery target.
- Relevant logs: work/p1-upstream-safety.cpp/exe; work/p1-negative-retry.log and p1-negative-rectangle.log; work/coop-direct generated binaries; work/coop-start-actions.json and coop-start-pushed-actions.json; previous53 hardware/config evidence remains in friendly folder2.
- Unverified fixes: All new game-source behavior needs Apple build and device test; ledger isn't connected to actors or saves. No new IPA installation, full-world sync, internet service or autosave occurred.
- Risks and warnings: Do not enable old online menu and claim full co-op. Existing WorldDelta sends captain records only; other world state still needs sync. Direct networking alone cannot guarantee state-away internet/NAT traversal. Old Gekko frame/hash handle isn't a world snapshot. Normal memory-card save remains between-days; no arbitrary-tick card writes. No raw heap/pointer serialization. P1 global actor cap must be reconciled with independent per-player allowances. No finale spoilers. No full current phone-data backup claimed.
- Exact next actions: Native run → verified artifacts; Raye solo install/assets → two-phone same-Wi-Fi captain+squad vertical; stable entity registry/Onion engine bridge; host-owned Pikmin/jobs/enemies/items/obstacles + separate camera; retained-host reconnect/pause and versioned exact-world snapshots; private invites/real internet/relay tests; then stronger P2 stability and its engine adapter.

**END PROGRESS REPORT**


<!-- PRE-COOP HISTORY -->

# OPEN NECTAR iOS — CODEX TO CHATGPT MASTER HANDOFF

## Current progress report — Build53 phone baseline and upstream audit — 2026-10-24 19:48 EDT

**Overall project status:** P1 Build53 user-tested: sharper gameplay, wider manual controls, keyboard closed. Current high2853x2007/1.00x with AO OFF reports120FPS. Large43FPS dip recovered after AO Off at the same1902x1338, then user raised to full native and still reports120. User explicitly retains high quality; no graphics downgrade/code/build needed. Upstream audit completed; proposed preventive fixes NOT implemented in this audit.

### Pikmin 1

- Current objective: Preserve working53 and compare original upstream for campaign stability fixes before broader solo/co-op work.
- What was investigated: User screenshots; two read-only settings captures; published release API/web pages; fetched1.0.7/1.0.8/main source; relevant current-iOS diffs including older missing carrying timeout. Actual current/tag/main rectangle arithmetic compared locally.
- Root cause or leading hypothesis: AO is strongly isolated as main observed slowdown (not resolution alone). Moving lines remain unidentified. Missing upstream carrying/collision/Onion/enemy/menu/cache/numeric guards confirmed in source; none established as cause of reported NaN/black world or stranded pair.
- Files changed: Documentation ONLY: PIKMIN1_BUILD53_HARDWARE_RESULTS.md, UPSTREAM_1_0_8_IOS_AUDIT.md and current journals. No game source, config, phone data or workflow changed; no new CI.
- Tests and results: Standalone actual map_gx_rect comparison161200 cases: current and1.0.8 tag33910 adjacent-edge mismatches, latest main0. This proves missing numeric correction, not visible iPhone symptom. Current-renderer8 relative-quality arithmetic checks PASS.53 prior native/package/simulator checks retained; user reports targeted runtime success.
- Confirmed working: Sharper game display, farther manual control positioning, unwanted keyboard closed, current high-resolution120FPS user report with AO OFF and GPI pack still enabled. Position save/relaunch persistence and long-session heat were not separately confirmed. Following feels better;53 did not introduce new AI changes.
- Remaining issues: Full campaign, stranded-pair rescue, slow/single-file return and prior black-world/NaN remain open. Lower-resolution moving lines only revisit if they persist with AO OFF. No guarantee120 across all scenes/devices/heat conditions.

### Pikmin 2

- Current objective: Preserve installed working baseline; audit future stability candidates only.
- What was investigated: Upstream gate lifetime, interpolated transition, save/card scheduler, sample formats/buses, host readable-memory bounds and allocator differences; prior1.0.6 backlog.
- Root cause or leading hypothesis: Current source lacks several upstream defensive fixes, but user has not reported those new symptoms. New GX bounds lookup is not drop-in on Darwin (/proc/self/maps missing). Port-argument ARM64 scalar fix is already present independently; avoid blanket audio replacement.
- Files changed: NONE in game/source. Candidate list saved in shared audit.
- Tests and results: No new P2 tests/build/phone results. Prior52 native/IPA SUCCESS retained.
- Confirmed working: User's installed gameplay/audio baseline;52 package verification only, not new phone proof.
- Remaining issues: Later stronger full-campaign/cave/save test; queued fixes need targeted iOS adaptation and tests, no current P2 update requested.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; upstream SSunnKing same project.
- Branch: ios-experimental; starting clean local=origin802cd294fb9fc088da1da5233687a7674d4e3c32. Fetched upstream source/tags without merging or checking out another branch.
- Starting commit:802cd294fb9fc088da1da5233687a7674d4e3c32; current tested53 sourcec25ba6a79ed975ba5face0461805bbd330e99cee.
- Latest commit / commits created: Documentation-only audit/hardware checkpoint pending commit; final exact SHA saved in external resume JSON after push.
- Changes pushed: Only scoped journals/audit/hardware report; skip ci. No upstream fix imported and no P1/P2 build triggered.
- Uncommitted changes: Scoped documentation until checkpoint commit. Private screenshots/phone configs/fixture binaries remain outside Git.
- GitHub Actions run IDs:53=40133259493 P1+startup SUCCESS;52=40131000336 P2+startup SUCCESS. No new run for audit or AO setting.
- Build results: Latest source package53 compiled/verified; user runtime feedback establishes targeted improvements, not full story. Upstream candidates are source-reviewed only.
- Artifacts produced: No new IPA. Verified53 retained folder1, SHA256c483540e76cef95c002578724690fe8ebe649901b9a09906350ee0b93c5cff85. Public latest-release metadata, exact source refs, arithmetic fixture evidence and private graphics comparison saved under work and friendly folder2.

### Next steps

- Next Pikmin 1 task: Keep working full-native/AO-OFF configuration. Prepare a scoped preventive batch from audit: high-FPS carrying wait, collision/Onion/array/UI/cache guards and edge rounding after meaningful tests. Do not blindly merge main or claim this fixes follower/NaN issues. User's current request was comparison; adoption remains next work.
- Next Pikmin 2 task: Paused; saved later gate/interpolation/card/audio/bounds checklist.
- GitHub/build task: No run now. Batch related tested P1 backports for one later P1-only native build; preserve53 baseline and iOS platform changes.
- Anything requiring my involvement: Nothing now; phone may close/disconnect. No need repeat whole campaign or lower resolution for resolved AO slowdown. If lines recur with AO Off, brief moving-camera evidence can distinguish possible causes.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User asked retain high-resolution finding, then explicitly requested upstream releases/source comparison. Latest public release1.0.8 publishedOct22, tag6319c3e354be280ab796f2c2e2504e185ce8cf96. Main a6b09bfe5a11798b2239d6072bace2e85812f245 Oct24 has seven later commits. Audit includes missing older carry fix3dcd6f25. No code backported yet.
- Important source-file locations: Full source-specific matrix in ios/UPSTREAM_1_0_8_IOS_AUDIT.md. Hardware evidence and effective relative-resolution notes in ios/PIKMIN1_BUILD53_HARDWARE_RESULTS.md. Preserve scene/FBO/Retina/menu/touch/keyboard fork fixes.
- Relevant logs: work/upstream-latest-release-oct24.json; fetched refs; work/audit_upstream_rect_edges.py, upstream108-rect-audit.cpp/exe, check_upstream_rect.cmd; current/tag33910 vs main0 mismatches. work/build53-quality-comparison.cpp/exe8 checks. Private work/p1-build53-graphics-20261024-193524 and p1-build53-ao-off-20261024-193828; friendly folder2/Build53 - Private Graphics Comparison.
- Unverified fixes: All upstream candidates NOT implemented/native-tested here. Numeric edge fix is only a candidate for user's moving lines. Current FPS is user-reported, sustained thermal/full-story performance unverified. No new save/autosave/network feature.
- Risks and warnings: Release notes mention edge/VSync corrections that are not actually in fetched1.0.8 tag; the relevant changes are in main2b65f16a. Main also introduces large custom mission/campaign/model/menu/save changes; do not import them as a stability patch. Upstream NETPLAY.md newly declares old network code disabled/unmaintained; that is source status, not an instruction overriding our user's future co-op goal. Do not assume existing netplay is production-ready.
- Exact next actions: Use audit priorities to implement/test one P1 preventive batch when continuing development; preserve existing enhancements and profile. Leave P2/graphics config untouched. Continue separate follower/NaN investigation. Report source, CI, IPA and phone milestones distinctly.

**END PROGRESS REPORT**

---
## Earlier checkpoint history


## Current verified package — P1 Build53 SUCCESS — 2026-10-24 17:53 EDT

User reported PASS; verified directly. Run40133259493/sourcec25ba6a79ed975ba5face0461805bbd330e99cee, startup job120989318144 and P1 job120991599668 both SUCCESS. This is the requested P1-only cumulative display/control/keyboard package. No P2 job or installed-app changes. Prior in-progress notes below are historical.

### Pikmin 1

- Current objective: Phone test53 for gameplay clarity/native landscape resolution, control edge placement/persistence/hitbox, and unwanted keyboard on startup/background resume.
- What was investigated: Full successful job log; exact run/source/artifact identities; package digest/ZIP/ARM64/platform/SDK/minOS/original standard P1 identity/icons/scene manifest and compiled scene selectors; actual generic simulator initial/background/resume evidence.
- Root cause or leading hypothesis:51 corrected portrait/logical-point render budget and editor safe-frame clamping.53 includes already-committed keyboard guard: iOS ends active/shown text input during gameplay while leaving the existing randomizer editor available. Exact original keyboard trigger still unidentified; guard runtime remains a candidate until user test. Prior NaN coordinates may relate to black world but root cause NOT established.
- Files changed: No new game/source change during this result-handling turn. Source53 contains P1 pc_window.cpp guard plus51 settings/window/gl/touch corrections and actual-code regression/workflow checks. Only result journals committed now.
- Tests and results: CI1820 actual layout/editor/persistence checks and70 pixel/migration/budget checks PASS; actual keyboard helper iOS+desktop host checks PASS and Apple syntax step PASS. Existing24 surface/140 route/283 walking/105 command and campaign/storage/profile regressions PASS. Full native compile/link/package PASS. Actual generic iOS27.1/iPhone Duo scene startup and same-PID background/resume PASS; does not certify game behavior.
- Confirmed working: Exact package generated and verified. Prior installed50 user-visible gameplay and earlier audio/content baseline retained;53 installation/runtime NOT yet reported. No assertion that all navigation or full campaign works.
- Remaining issues: Slow/single-file return and reported unrescued pair UNCHANGED; black-world/NaN origin UNRESOLVED. No such fixes in53. Native resolution1.00x may cost more GPU/memory; player retains resolution/scale/FPS choices incl120.

### Pikmin 2

- Current objective: Preserve working installed app; no new test/update required for current P1 task.
- What was investigated: No new P2 source or phone evidence.52 native/IPA verification already completed.
- Root cause or leading hypothesis:52 corrected the stale P2 pixel-budget test after shared51 source; no new reported P2 gameplay defect.
- Files changed: NONE.
- Tests and results:52/run40131000336 SUCCESS; verified P2 IPA preserved.53 built P1 only.
- Confirmed working: User's existing P2 audio/gameplay baseline remains authoritative, newer52 runtime unverified.
- Remaining issues: Full campaign and optional52 display/edge hardware checks remain unverified; P2 work paused while P1 prioritized.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; local C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental. Fetched clean local=remote d49e309013e35f93c81f00daf88c582ef272c378 at start of this result turn.
- Starting/latest commit: Starting journal d49e309013e35f93c81f00daf88c582ef272c378; verified build sourcec25ba6a79ed975ba5face0461805bbd330e99cee. Result-only skip-ci commit SHA recorded in external exact resume JSON afterward.
- Commits created / changes pushed: Only successful package/test/handoff documentation; no extra build requested.
- Uncommitted changes: Only scoped journal before result commit; no private evidence, IPA or game assets staged.
- GitHub Actions run IDs:53=40133259493 SUCCESS P1+startup;52=40131000336 SUCCESS P2+startup;51=40109396851 P1+startup SUCCESS/P2 obsolete host assertion FAIL. No active build requested.
- Build results:53 native tests/compile/link/package and generic simulator PASS; real phone installation/runtime PENDING.
- Artifacts produced: P1 artifact12576271886 ZIP SHA25692d6b8da27ea1e406f210e1234e8b0d3cfee09efb2a36bcc9325076783f5aa4c. IPA2835584bytes SHA256c483540e76cef95c002578724690fe8ebe649901b9a09906350ee0b93c5cff85; executable UUID92456923-027a-3544-9d20-51a2166eed02; original org.opennectar.experimental.pikmin1 unsigned ARM64 iPhoneOS SDK27.1/min15; approved icons/landscape/ProMotion flag intact. Staged folder1/Pikmin 1 - Build 53 - Display Controls and Keyboard.ipa with verification JSON. Scene artifact12576885117 ZIP SHA2565ff42ff3b41f48dc0db82292c676452ebe5a59ac71508d7532467f2b84a80a46 verified. Older51/50/42 and P2 packages preserved.

### Next steps

- Next Pikmin 1 task: User updates existing app same account/identity without uninstall/reset; follows folder1/Pikmin 1 - Build 53 - TEST THIS.txt. Compare actual landscape dimensions/game clarity at1.00x, manual control edge/save/reload/tap, Home Screen10sec/return twice and menus for keyboard, basic input. Do not ask full campaign solely for this test.
- Next Pikmin 2 task: None now; installed app untouched.
- GitHub/build task: No new run or idle polling. On phone regression use exact53 UUID above and bounded diagnostics. Future P1 work: trace NaN origin and improve stuck/slow return with evidence and meaningful crowded/oscillation tests.
- Anything requiring my involvement: Install/test53 when ready. No USB connection or open game required now. If still blurry send gameplay and Display screenshot; report keyboard/black event separately. Do not install51 first.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User explicitly requested this P1 build because guard was previously only committed while52 P2-only ran.53 now successfully packages it with all51 display/control corrections. Only package/source/host/simulator milestones established; hardware still pending. Keep scope clear and do not conflate P2 test cleanup with P1 runtime work.
- Important source-file locations: games/pikmin1/pc_port/pc_window.cpp pc_window_update_text_input/poll_events/set_window_size; settings rebuildResolutionList; gl pc_gfx_begin_frame; touch ButtonLayout.fullBounds/layout_place/load/save; tests/pikmin1_ios_keyboard_test.py; ios_display_layout_test.py; ios_pixel_resolution_test.py. AI/NaN diagnostics remain in aiCrowd.cpp/piki.cpp/navi.cpp and private Oct24 collected navigation report.
- Relevant logs: work/build53-result-run.json, build53-result-jobs.json, build53-artifacts.json, build53-p1-full.log, build53-verification.json, build53-startup-runtime-verification.json; work/verify_stage_build53_p1.py; outputs/Build53-Pikmin1 exact IPA/checked bundle/compiler log. Friendly folder2 copies of verification/full job/simulator evidence. Private phone evidence stays local.
- Unverified fixes:53 phone sharpness/edge persistence/keyboard behavior; no AI/black-world fix implemented. Prior single rescue log cannot identify the reported pair. CPU resource report says action NONE, not a crash diagnosis.
- Risks and warnings: Preserve original installed app/settings/content and player FPS choice. No complete current phone save/assets backup; package backups do not contain phone data. Do not force-push/main merge/reset/uninstall/upload assets. No spoilers.
- Exact next actions: User tests53; capture results and update journal. For failure retrieve matching current logs without overwriting prior evidence. Continue P1 recovery/NaN research; P2 stays paused. No new CI until relevant source correction warrants it.

**END PROGRESS REPORT**

---
### Earlier checkpoints (historical)


**DISPATCHED:** P1-only Build53/run40133259493, sourcec25ba6a79ed975ba5face0461805bbd330e99cee, startup job120989318144 IN PROGRESS at last inspection. Link: https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40133259493. Contains native landscape pixels + manual control edges + keyboard ownership guard. Local keyboard iOS/desktop MSVC and Clang PASS; Apple compilation/new IPA and phone results PENDING. No new P2 job requested. No additional idle polling; user reports completion. Next retrieve logs and verify exact P1 IPA before staging. Old51 is preserved but user need not install it first. No AI/black-world fix claimed.


## Current action — P1-only package including keyboard guard — 2026-10-24 17:13 EDT

User explicitly requested packaging the pending P1 fixes now. Prepare ONE P1-only workflow run from current branch. No new P2 build is needed. Starting local/remote64f8276f95dbda7c9b660529579a24cbcbc315b1 clean and fetched.

### Pikmin 1

- Current objective: Produce a single standard P1 update containing all already-implemented display/control-placement changes plus the new keyboard guard.
- What was investigated: Confirmed P151 source contains physical landscape render budget/native migration and manual edge persistence; confirmed fb7880f6 adds pc_window_update_text_input before event polling and keyboard actual-helper host/Apple workflow checks.
- Root cause or leading hypothesis: Low portrait/logical-pixel budget and safe-frame editor clamp corrected in51. Keyboard guard defensively ends text input/shown IME outside the randomizer editor; exact UIKit trigger still unidentified. This is a candidate correction, not phone runtime proof.
- Files changed: Existing P1 pc_window.cpp keyboard guard and tests/pikmin1_ios_keyboard_test.py/workflow are already committed. This trigger changes journal only to build the current cumulative source; no fabricated additional gameplay fix.
- Tests and results: Actual P1 keyboard helper MSVC iOS/desktop PASS and Clang both variants PASS immediately before dispatch.51 actual pixel/layout/native game/IPA and shared simulator gate PASS retained. New Apple build/IPA/phone PENDING.
- Confirmed working: Prior installed50 visible game and one fresh/resume test;51 compilation and package verified, not user-installed. Prior rescue log contains one uncorrelated relocation, not confirmation of reported pair.
- Remaining issues: Slow/single-file following, reported missed two rescues, and black-world/NaN origin UNRESOLVED and unchanged in this candidate. Avoid presenting this as an all-bugs-fixed build. User FPS incl120 retained.

### Pikmin 2

- Current objective: None for this run; preserve working installed app and verified52 IPA.
- What was investigated:52 final native/tests/package and simulator metadata previously verified.
- Root cause or leading hypothesis:51 P2 test expected old699x323 budget; corrected52 actual2097x968 physical budget.
- Files changed: NONE in this run.
- Tests and results:52 successful;409 iOS/302 desktop and native/link/IPA PASS. No new P2 phone test.
- Confirmed working: User's older installed audio/gameplay baseline remains authoritative.
- Remaining issues: Full campaign and52 display/edge hardware validation pending; P2 update optional, not current priority.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental; start64f8276f95dbda7c9b660529579a24cbcbc315b1 local=remote, clean; no incoming change.
- Latest commit / commits created / changes pushed: P1-only build trigger with this journal is being committed now; exact source and run saved in dispatch checkpoint afterward.
- Uncommitted changes: Only scoped journal update before commit. Existing source/tests already committed.
- GitHub Actions run IDs / build results / artifacts: New P1-only run pending dispatch.52/run40131000336 sourcea575ecf424008c7430da96a5082ffb7f68970dc1 SUCCESS P2;51/run40109396851 source1450d21e1f60c9600c8556371e6f8f2f55cd7130 P1 and shared startup SUCCESS, P2 host test failed. Verified51 P1 and52 P2 IPA retained in folder1; new IPA not yet generated.

### Next steps

- Next Pikmin 1 task: On build completion retrieve logs and verify exact original-ID ARM64 IPA/scene/icons/digest, then stage ONE clearly named current P1 update in folder1. Ask user to test native landscape clarity, control edge/save/reload/hitbox and background/resume keyboard behavior. Do not require51 installation first: new successful package supersedes51 for this test.
- Next Pikmin 2 task: No new action/build/install now.
- GitHub/build task: Capture exact P1-only run/source/job; stop idle CI polling per user preference. User reports completion; no duplicate build.
- Anything requiring my involvement: Nothing on phone while build runs; phone/game may close/disconnect. No reset/uninstall needed. Test after new IPA verified.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User was confused because keyboard was committed but not built while a P2-only test retry ran. They now explicitly requested P1 build; package the already-tested cumulative source now, no need wait for AI/black-world work to finish. Explain unresolved issues accurately.
- Important source-file locations: P1 pc_window_update_text_input, pc_window_poll_events, pc_window_set_window_size; settings rebuildResolutionList and resolution migration; gl pc_gfx_begin_frame; touch ButtonLayout.fullBounds/manual placement/save/load; new keyboard regression/workflow.
- Relevant logs: work/p1-keyboard.cpp/exe, check_p1_keyboard.cmd, check_p1_keyboard_clang.cmd; earlier build51 and52 verification and private Oct24 phone diagnostics retained.
- Unverified fixes: Keyboard correction has only host verification until this new Apple build; all display/control/keyboard phone behavior pending. No AI/black-world correction implemented.
- Risks and warnings: Preserve installed apps/data and user-selected FPS; native1.0x costs more GPU/memory than old logical budget. No game assets/private data in Git. No force-push/main merge/reinstall/reset.
- Exact next actions: Dispatch P1-only, capture run/source, commit result-only checkpoint with skip ci; return build link and wait for user to report completion. After success verify and stage, then targeted phone test. Continue AI/NaN investigation independently when actively working, but do not claim this build includes those fixes.

---
### Previous checkpoint (historical)


## Current result and scope clarification — 2026-10-24 17:06 EDT

P1 is the active user priority. User explicitly clarified that “done” meant GitHub Build52 finished, NOT that P1 Build51 was installed. No new P1 hardware outcome should be inferred.

- P1 Build51/run40109396851/source1450d21e1f60c9600c8556371e6f8f2f55cd7130: native compilation/IPA and generic simulator startup/resume PASS. Changes ONLY correct physical landscape render resolution and manual control placement/persistence at screen edges. Verified original-ID IPA is folder1/Pikmin 1 - Build 51 - Native Pixels and Control Edges.ipa. Hardware sharpness/edge behavior pending. It does NOT include the keyboard guard, rescue/pacing changes, or black-world correction. Those problems may still occur.
- P1 keyboard guard: committed fb7880f66045035ec7cc53a945f34533a71c2c2c AFTER51 and AFTER52 source, host iOS/desktop helper tests PASS; native/IPA/phone pending, no package contains it yet. P1 stuck-pair, slow return and black-world root cause remain unresolved. Prior saved phone log had one uncorrelated rescue and later NaN captain coordinates. No claim of a complete fix.
- P2 Build52/run40131000336/sourcea575ecf424008c7430da96a5082ffb7f68970dc1: COMPLETED SUCCESS. Startup job120982491334 and P2 job120984917508 PASS. This retry changed only the test expectation after shared51 physical-resolution changes:699x323 old logical budget to2097x968 physical budget at.75.409 iOS and302 desktop actual-code checks PASS in CI, full game native/link/IPA PASS. No new P2 gameplay/audio change and no new user P2 bug report. P2 update is optional; keep working installed P2 untouched while focusing P1.
- P2 artifact12575447436 ZIP SHA256b21f25d5b14913dd4fae3eec73819c9121d5bec18c9660032ad853ae6357753e verified. Exact original-ID ARM64 iPhoneOS/SDK27.1/min15 unsigned IPA4161397bytes SHA256fbf6b2512d91ccafc6c600ee8bddcdbbcef04a1c01ee0ea68da4c68fda40c793, executable UUIDef989bd1-fc9a-37d2-92df-bc2bb62fe182. Approved icons and scene manifest/compiled selectors PASS. Staged folder1/Pikmin 2 - Build 52 - Native Pixels and Control Edges.ipa for preservation, not automatically installed.
- Scene artifact12575616448 ZIP SHA256e97a04ed04b706d54808b5c2c9a2c85cbe8d574a620961630f009d3a6a54be1b verified; actual generic simulator one-entry, landscape, foreign-event filtering and same-PID background/resume PASS. Does NOT certify either game's actual runtime.
- Repository fetched and clean local=remote fb7880f66045035ec7cc53a945f34533a71c2c2c before this result-only documentation update. This update uses skip ci; no new build. No phone modifications, private/proprietary uploads, P1 source changes or installation performed.
- Evidence: work/build52-result-run.json, build52-result-jobs.json, build52-artifacts.json, build52-p2-full.log, build52-verification.json and build52-startup-runtime-verification.json; outputs/Build52-Pikmin2; friendly verification/full-log copies in folder2.
- Exact next actions: Focus P1. Explain51 scope plainly; if user installs51, verify physical landscape Resolution/native1.0x clarity and control edge drag/save/reload. Existing keyboard/pacing/black issues stay tracked separately. Continue tracing invalid actor coordinates and recovery eligibility; next P1 fix batch should include already-committed keyboard guard with actual tests. Do not create another P2 build without new evidence. No idle CI waiting or further immediate phone-connection requirement. Preserve working installs/settings and all previous packages.

---
## Earlier investigation report (historical; current status above supersedes pending build text)


## Latest continuation — keyboard guard locally verified; P2-only52 dispatched

Build52/run40131000336/sourcea575ecf424008c7430da96a5082ffb7f68970dc1 is IN PROGRESS for P2 only after correcting the stale native-pixel fixture. No idle polling. Source parent cf4e959c;51 source1450d21e and its mixed results retained above.

After the report below was written, user provided a photo of the keyboard obscuring normal gameplay. Added P1-only pc_window_update_text_input in games/pikmin1/pc_port/pc_window.cpp, invoked before event polling: iOS stops text input/hides a shown keyboard outside the existing randomizer editor. Existing editor remains exempt, and desktop unchanged. This addresses text-input ownership defensively; the exact UIKit event that summoned the keyboard remains unidentified. Actual helper regression tests/pikmin1_ios_keyboard_test.py passes both iOS and desktop host variants. Next P1 workflow includes host variants plus Apple syntax check. Native and phone verification PENDING. This source is intentionally committed WITHOUT another build while52 runs; include in next P1 batch.51 staged IPA does NOT contain this new keyboard guard.

P1 root cause of NaN captain coordinates, black world, slow followers and missed rescues remains UNRESOLVED. No changes to movement/rescue/saving were made this turn. One fresh-launch and one background/resume check showed the world; that does not reproduce or solve prior black world. Existing evidence collected, user may close game/disconnect. No current further phone task.


**Date/time:** 2026-10-24T20:42:32.072908+00:00

**Overall project status:** Build51 completed: shared simulator startup/resume and P1 succeeded; P2 stopped on a stale host regression assertion BEFORE game compilation. P1 phone currently runs Build50 (UUID matches its CPU resource report). Latest user clips show improved but slow return and two reported stranded Pikmin. Black world with HUD remains unresolved. Phone diagnostics collected READ ONLY.

### Pikmin 1

- Current objective: Diagnose slow/single-file return, failed rescue, world-only black screen, and newly reported unwanted keyboard; preserve display/control improvements and settings.
- What was investigated: Both Oct24 clips sampled across38.47s and40.44s. Formation narrows on the cardboard crossing; some followers remain above the captain. Existing phone configuration/layout/navigation log and one CPU resource report retrieved without modifying phone files.
- Root cause or leading hypothesis: Rescue is ON (stuckFollowerRescue=1), Better Pathfinding ON, speeds100%, solo, textureGPI active,120FPS. Navigation log records ONE rescued_follower; cannot identify it as either reported stuck actor. Last recall entry has captain and target NaN coordinates. Invalid simulation coordinates could explain world-only blackness; initial source of NaN NOT found. Route budget two searches/second and conservative eligibility/safe spots may contribute to delays; not yet proven sole cause. No current crash report: CPU resource report says action taken NONE; not evidence of an OS kill. User fresh launch and one Home Screen10s/return preserved visible world; unwanted software keyboard then appeared and stayed.
- Files changed: No new P1 movement, rescue, renderer, keyboard or save source changes this turn. Previous51 native landscape pixel/control-edge changes retained. Private evidence NOT committed.
- Tests and results:51 P1 native compile/link/IPA PASS. Exact artifact digest, IPA ZIP, original standard identity/icons, ARM64 iPhoneOS SDK27.1/min15, compiled scene support/manifest verified. Generic scene simulator initial/background/resume PASS. No51 hardware test yet. Existing50 phone launch/resume visible once, not broad stability proof.
- Confirmed working: User sees game/HUD and better distant recall on50. Saved config confirms optional rescue enabled. One logged rescue occurred, without clip correlation. Earlier menu/control/audio baseline retained.
- Remaining issues: Two stranded actors NOT confirmed rescued, return pacing still poor; NaN origin/black world unresolved; unwanted keyboard screenshot during gameplay. No claim these are fixed by51. Native pixel/edge behavior requires installing51 then focused test; full story remains unverified.

### Pikmin 2

- Current objective: Restore CI validation after intended physical-pixel rendering change.
- What was investigated: Complete job120920446462 log retrieved directly. Assertion expected699x323 native render budget (logical932x430 at.75). New real code correctly derives2097x968 from physical2796x1290 at.75.
- Root cause or leading hypothesis: CONFIRMED stale regression expectation. This was a test failure before CMake/game compilation, not a newly observed compiler/linker or phone crash.
- Files changed: tests/pikmin2_ios_menus_test.py expected native pixel budget and explanatory comment only. Explicit user640x480/.75 and desktop expectations retained.
- Tests and results:409 actual iOS menu/render/input checks PASS,302 desktop checks PASS; Clang both variants with warnings-as-errors PASS. Other related test expectations searched. New Apple retry PENDING.
- Confirmed working: Previously confirmed P2 audio/gameplay baseline and50 native/IPA retained. Installed P2 untouched.
- Remaining issues: Re-run P2 native job, verify exact IPA if successful; phone native resolution/control edges/full campaign remain unverified.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port; C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental; clean matching cf4e959c5d2b9596cecaf39d8dd2409e8606e8dd at start; fetched remote before edits.
- Starting commit: cf4e959c5d2b9596cecaf39d8dd2409e8606e8dd.
- Latest commit: Build51 source1450d21e1f60c9600c8556371e6f8f2f55cd7130; upcoming P2-only test/journal commit exact SHA recorded in external checkpoint after push.
- Commits created: Scoped P2 regression/journal retry prepared; no speculative P1 fix included.
- Changes pushed: P2-only retry to be dispatched once tests/docs checked, exact source/run recorded separately. No duplicate P1 rebuild.
- Uncommitted changes: P2 fixture plus these journals until source commit. No private evidence/assets/phone files staged.
- GitHub Actions run IDs:51=40109396851 source1450d21e1f60c9600c8556371e6f8f2f55cd7130; startup120917764682 PASS; P1120920446401 PASS; P2120920446462 FAIL at host menu assertion.50=40003458275 all jobs PASS.
- Build results:51 MIXED. P2 corrected local fixture passes; new Apple compilation pending.
- Artifacts produced:51 P1 artifact12567035238; staged Pikmin 1 - Build 51 - Native Pixels and Control Edges.ipa in folder1,2835690bytes SHA2564cc90a7bacf02257c9df7b1f2c70534c7656e8f998a3ac19295ea0cfe84383fb, executable UUIDe845087d-e09e-3d8b-a89a-a9670aad56e9.51 P2 artifact12566495886 only error summary, NO IPA. Scene artifact12566192640 independently verified. Older50/42/32 IPA backups retained.

### Next steps

- Next Pikmin 1 task: Trace earliest invalid captain/actor coordinates; inspect collision/route/recall numeric boundaries. Capture bounded fresh navigation state if needed, with prior evidence preserved. Diagnose keyboard text-input ownership and close behavior. Do not call black screen fixed from one successful resume. Evaluate fair route scheduling and oscillation-aware stuck detection with actual method tests before changing rescue limits. No blind teleport or worker inclusion.
- Next Pikmin 2 task: One P2-only native retry for corrected expected physical-pixel budget. On completion retrieve full job, verify original-ID IPA, stage separately.
- GitHub/build task: Capture new run/source and then stop idle CI polling. Documentation-only updates use skip ci.
- Anything requiring my involvement: No further immediate reproduction needed; phone can close/disconnect after collection. If keyboard remains, force-close/reopen P1 as temporary workaround; do not reset/reinstall.51 update optional, contains only pixel/edge corrections, does NOT resolve AI/black/keyboard. No complete current phone-data backup made; configuration/layout evidence is not an assets/save backup.

### ChatGPT continuation notes

- What another ChatGPT conversation needs to know: User requested efficient continued work with~10min usage window. Phone connected/unlocked. First collector used denied container root; corrected to /Documents and succeeded. Do not ask user to unlock again for that path error. Installed P1 confirmed50 by UUID8b032bf3-2580-3708-886c-620a0ded22f7 in CPU report. No trap/crash report found for current world-black symptom. CPU53% average report explicitly action NONE; keep separate from44 startup trap.
- Important source-file locations: games/pikmin1/src/plugPikiKando/aiCrowd.cpp pcRecoverFollower/pcProtectFormationEdge; piki.cpp pcRescueFollowerNearCaptain/pcMoveFollowerRoute/pcSteerFollowerGoal; navi.cpp pcUpdateFollowTrail/pcTakeFollowerRouteBudget/callPikis; pc_port/pc_follow_trail.h stuck monitor; pc_follow_surface.h geometry; pc_follow_report.h bounded4 events/reason, overwrites on launch. Keyboard: SDL defaults text input active in SDL_video.c; only explicit P1 editor calls StartTextInput in settings rndTextInputOn/rndShareEnd. Root cause of unintended keyboard not established.
- Relevant logs: PRIVATE work/p1-feedback-oct24-20261024-163651, screenshots/recordings original user paths; local contact sheets work/clip-12-29-32.jpg and clip-12-30-58.jpg; work/build51-p2-full.log; build51-verification.json; build51-startup-runtime-verification.json; build51-feedback-run/jobs.json; verify_stage_build51_p1.py. Relevant copies in Documents/Open Nectar/folder2.
- Unverified fixes: No new P1 AI/black/keyboard fix implemented.51 native-resolution/edge change is compiler/package/simulator verified, hardware pending. Corrected P2 fixture locally verified, full Apple retry pending.
- Risks and warnings: No history rewrites/force push/main merge/uninstall/reset. No game assets or private phone data in Git.120FPS stays user-controlled; native1.0x costs more GPU/memory. No spoilers. Network/co-op/save redesign deferred per existing design documents.
- Exact next actions: Inspect pending P2-only run once user reports completion; don't poll idle. For P1 first fix unintended keyboard with explicit text-input ownership without breaking randomizer editor; trace NaN from earliest event with non-finite guards and timestamped actor/state diagnostics. Add crowd/oscillation regressions before pacing changes. Preserve51 package separately from current50 runtime evidence.

**END PROGRESS REPORT**
