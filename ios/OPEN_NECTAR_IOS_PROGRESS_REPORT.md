# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** October25,2026 20:09 EDT.

**Overall project status:**69 native/simulator/package verified PASS. Next coordinated retained-connection/area-agreement batch implemented, local tests PASS, Apple pending.68 remains installed accepted baseline; actual two-phone area not exposed yet.

### Pikmin 1

- Current objective: Disposable same-area two-captain prototype with separate screens and protected solo data.
- What was investigated:69 actual run/jobs/artifact/probe/package; native UI discarded early messages and closed links on Done; room/session ownership; both-loaded scene protocol; cached card save root.
- Root cause or leading hypothesis: No new failure. Prevented a startup race where early scene/status bytes arrived before other phone left its native UI. Also confirmed static cached saveRoot means late environment override is insufficient practice-save isolation.
- Files changed: New coop_connection.h/.cpp, practice_bootstrap.h/.cpp, coop_connection_test.cpp; new ios/ios_coop_handoff.h; ios_coop_room.mm, coop_session.h/.cpp, actual coop_socket_probe.cpp, core CMake and experimental P1 checks; journal/checklist.
- Tests and results:69 actual Apple full game/captain adapter/12 required gates/simulator input and pause/mismatch/rejoin/package PASS; artifact/IPA SHA/CRC/device resources verified. New batch all24 CTest (incl real GNS stress) PASS, actual Windows encrypted loopback early-message/area/load/input/peer-close PASS, Clang6 units PASS,10 ARC getters+negative control and2 identity tests PASS, diff check PASS. New native full UI/handoff/bootstrap runtime pending next build.
- Confirmed working:68 phone connection/menu/Rejoin/Done bundle and improved heat by user report.69 source native helper tests passed;69 phone not installed/retested. New owner/bootstrap logic works in local fixture/Windows socket scope, not an actual loaded game area.
- Remaining issues: Actual practice engine/start UI not activated; need safe temporary card context before direct boot, actual scene+actors, guest simulation suppression, correct controller/camera yaw and fullscreen HUD/audio, pause/background/exit restoration. Shared actions/Onion/save slots/recovery/internet remain later.

### Pikmin 2

- Current objective: Preserve working P2.
- What was investigated: No new P2 symptom/audit.
- Root cause or leading hypothesis: No new issue.
- Files changed: No P2 source/phone files; shared network library extended but P2 not activated.
- Tests and results: No new P2 native/device test requested; next run P1 only.
- Confirmed working: Earlier user-reported P2, not retested here.
- Remaining issues: Broader campaign testing/future co-op adapter.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port.
- Branch: ios-experimental.
- Starting commit: de9e26884f9ed7c206b2f1d10e33e60942df3d84; fetched local/remote matched before batch.
- Latest commit: New handoff/area source checkpoint recorded in Exact Resume State.json after push.
- Commits created: Retain accepted room and coordinate practice loading with bounded handoff queue [ios-build] [ios-p1-only].
- Changes pushed: Source/tests/docs; one native P1 validation intended. Exact source/run appended at dispatch.
- Uncommitted changes: None after checkpoint.
- GitHub Actions run IDs:69/run40243925821 SUCCESS; scene121321406659/P1121323818559 SUCCESS. Next run pending dispatch lookup;68/run40232707062 phone-accepted baseline.
- Build results:69 full Apple/native/simulator/package PASS; new batch LOCAL PASS, Apple/phones pending.
- Artifacts produced:69 artifact12618896083 SHA2564b37b417051db8935829ed94d522eda119cab5923b5c3c81f6a5d72e5b0a510c; IPA5288997bytes SHA25696d9464924c0d3b36e4dbea5ad4588447d34b7df7bdeb9bb339465b909048710, UUIDf2958444-a438-3617-a8e2-57308563ddf7, unsigned deviceARM64/standard identity/icons/notices. Saved privately at C:\Users\chazz\Documents\Codex\2026-10-19\got-it-you-want-codex-to\outputs\Build69-Pikmin1\Nectar-pikmin1-unsigned.ipa, receipt work/build69-package-verification.json. No cleanup warning69; no69 installation request.68 install folder remains current.

### Next steps

- Next Pikmin 1 task: Actual disposable practice engine driver and save isolation, scene loading/actors and ready, controller+own camera yaw, guest non-simulating fullscreen presentation and safe pause/background/exit. New startup code must not be exposed alone as playable co-op.
- Next Pikmin 2 task: Preserve working app.
- GitHub/build task: One combined Apple build validates current native detach+queue/bootstrap/session/socket/core batch. User reports result; no idle polling.
- Anything requiring user involvement: Nothing now. Keep68 installed. No USB/game-open or repeated connection test requested until complete practice package is staged.

### ChatGPT continuation notes

- What another conversation needs:69 verified engineering build, not new phone baseline.68 accepted limited phone tests/heat improvement. New retained-link/early-message/area-agreement source is implemented but actual engine scene/camera/controller driver remains. Normal Done still closes room; only future explicit take_connection seam moves it.
- Important source locations: ios/ios_coop_room.mm rememberEvent/detachConnection and ios_coop_handoff.h; libs/nectar_net/coop_connection.* owning room/session + bounded queue; practice_bootstrap.* two-load/60s/start protocol; CoopSession.mBuffered private friend queue then normal single event pump. Actual captain guest adapter from69 pc_coop_world.cpp remains.
- Relevant logs: work/build69-run.json/jobs.json/artifacts.json/package-verification.json; outputs/Build69-Pikmin1/socket-session.log/result.json; full job log; work/local-net-win/core-build/Testing/Temporary/LastTest.log. Accessible current reports and69 evidence mirrored.
- Unverified fixes: New actual UIKit detach/queue and native bootstrap Apple compilation/runtime; native UI detach execution not tested on phone. No real practice area/camera/controller yet.
- Risks and warnings: Future engine owner must take native connection on main thread, keep sole event pump through pause/loading, attest actual loaded scene and full baseline, use unique session IDs, never continue alone after load failure. card_stubs.cpp static cached saveRoot ignores late NECTAR_SAVE_DIR change; explicit no-I/O/temporary card context and handle cleanup/restoration are prerequisites. Keep existing save/settings/packs/P2/FPS120 choices unchanged. No heat change beyond accepted68; no online internet/full campaign claims.
- Exact next actions: Inspect next native result, fix grouped actual errors if needed; then implement explicit practice-save context and title/card-select/GameCore driver. GameCore camera/HUD/input and guest sim guards required before T10 phone test. Never simply enable old netplay/direct boot or modify normal card files.

**END PROGRESS REPORT**
