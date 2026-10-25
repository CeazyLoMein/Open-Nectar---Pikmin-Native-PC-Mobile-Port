# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** 2026-10-25T18:18:20.806019+00:00 (UTC; client date October25,2026 EDT).

**Overall project status:** Build64 fixed the native Unicode/path tests and compiled P1 successfully, but failed the later real private-room socket rejection test. This session reproduced that defect locally before fixing it and implemented/verified one related transport/lifecycle/test batch. Next P1-only native build pending; current phones unchanged.

### Pikmin 1

- Current objective: Get two-phone private rooms working, then proceed to real shared gameplay.
- What was investigated: Full64 job log and hash-verified artifact; actual GNS terminal callbacks/receive queues; compatibility and GuestJoin state machines; address discovery; delayed polling, endpoint fallback and reconnect. No guessed compiler fix:64 had no compiler error.
- Root cause: GnsTransport closed the native connection inside ClosedByPeer callback before receiving queued final reliable messages. GNS destroys unread messages when CloseConnection frees that handle. When the guest polls slowly, the final incompatibility verdict is discarded; GuestJoin receives only a disconnect, retries endpoints and eventually reports unreachable with no mismatch reason. Reproduced with a150ms raw receiver delay and100ms private-room guest polling. Fast baseline12/12 passed under unrestricted local test access; slow reproduction failed, proving timing sensitivity. Initial restricted-access baseline failure is excluded from this diagnosis.
- Batch source changes: bounded drain-before-close (max256 messages/8MiB) with existing4MiB per-message validation and message Release; queue final messages before terminal event; deliver already queued events before advancing callbacks; ignore stale Connected callbacks for retired handles; guard null native interface; honor supplied address-discovery backends with automatic mapping OFF; optional explicit room listen address (normal app defaults preserved); make the probe bind/publish only127.0.0.1; use GuestJoin terminal progress and its actual deadline rather than transient inner state.
- Regression changes: raw real-GNS final reliable payload must arrive exactly once before Disconnected; listener survives and guest reconnects; injected no-mapping discovery is honored; native co-op probe deliberately slows wrong-secret/private-room polling and verifies ALL5 incompatibility fields, reason retention, no accidental partner bans, valid join and same-room rejoin. No compatibility test disabled or expected result weakened.
- Files changed: libs/nectar_net/include/nectar_net/room.h, libs/nectar_net/src/gns_transport.cpp, libs/nectar_net/src/room.cpp, libs/nectar_net/tests/coop_socket_probe.cpp, libs/nectar_net/tests/gns_transport_test.cpp, libs/nectar_net/tests/room_test.cpp.
- Tests and results: Both deterministic pre-fix tests FAILED, then PASSED with fix. Full23/23 networking CTest suite PASS, including native socket/authentication/stress/room and actor/Onion/session tests.8 complete probe runs PASS across baseline,80ms lag/40ms jitter/2% loss,120ms lag/50ms jitter/5% loss:40 exact mismatch verdicts. Clang diagnostics/core analysis on all5 changed C++ translation units PASS after including the project's Windows CRT definition and fixing a null-interface edge. Final code rebuilt:6 directly affected CTest regressions PASS plus3 final complete baseline/impaired probes PASS (15 more mismatch verdicts). Final binary SHA256 1d4316ac20c84352d974619925efd2502639796a89f324da7ea56a5e78a2e50f.2 source-identity+3 bundle+8 runner tests PASS; diff check PASS. Windows uses pinned GNS/BCrypt; this is NOT Apple/OpenSSL or hardware proof.
- Confirmed working:64 actual Foundation NFC/NFD, real changed content/name rejection, path aliases, independent hash vector and symlink tests ALL PASS; full iPhoneOS P1 BUILD SUCCEEDED. Independent compiled-app artifact checks PASS: original app ID, permission explanation, ARM64 iPhoneOS binary, exact3 pinned notices. The new network batch awaits Apple compilation/runtime and phone retest.
- Remaining issues: Current installed62 still rejects the46 NFC/NFD names; corrected source is retained in next build. No successful actual two-phone room yet. No playable shared world/campaign, full mid-day recovery or cross-progression implemented. Approved later UX: title-menu Online Co-op Host/Join beside local Co-op and separately labelled personal Solo/shared campaign slots.

### Pikmin 2

- Current objective: Preserve the user-confirmed working port while P1 is tested.
- What was investigated: No P2 gameplay/source audit in this batch.
- Root cause or leading hypothesis: No new P2 runtime issue reported.
- Files changed: No P2 game files or workflow selection changes; shared networking source changes are validated through P1 only.
- Tests and results: No new P2 Apple build or phone runtime test claimed.
- Confirmed working: Historical working installation on both phones, per user; not retested this session.
- Remaining issues: P2 online adapter and broader campaign testing remain later work.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: 318520db3dba9c2484e88d83a20dde8c8ccbf79a
- Latest commit: Source batch commit/run recorded in next dispatch checkpoint and Exact Resume State.json.
- Commits created: One scoped transport/lifecycle/regression/journal batch is committed and pushed by this checkpoint.
- Changes pushed: P1-only [ios-build] marker; no P2 build requested and no history rewritten.
- Uncommitted changes: None after successful checkpoint commit/push.
- GitHub Actions run IDs:64/run40217032902/source f5a71297ab9c54b43157e402d6e05751a128fc35 FAILURE. Scene121240294349 PASS. P1121243384666 actual build PASS; socket gate FAIL `room code refuses a different game-data fingerprint`. Next run/source recorded at dispatch.
- Build results:64 native Unicode/hash/path regression and P1 app build PASS; real socket test FAIL. New batch local verification PASS; Apple native/network/IPA/hardware milestones PENDING.
- Artifacts produced:64 artifact12609440157 SHA2564fb0f6a71392c65f69a02a7e71166933b3b69bdb5ceb1a82160ecb23fac9c693 downloaded/verified. Contains compiled app.tar.gz and diagnostics, no completed IPA. No failed64 app installed or presented as safe-to-install.62 staged IPA and54 rollback preserved.

### Next steps

- Next Pikmin 1 task: Check next native batch result, retrieve exact logs/artifacts, verify/stage successful IPA, update BOTH existing P1 apps with same package/identity, retry T02 connection then T03 reconnect/reverse host and T04 ordinary solo.
- Next Pikmin 2 task: Keep working app unchanged; no P2 installation or build now.
- GitHub/build task: Record exact next source/run; do not poll idly. User reports build completion; retrieve evidence directly afterward.
- Anything requiring user involvement: None while building. Both phones may unplug/P1 may close. Do not reinstall game data/packs or remove either app.

### ChatGPT continuation notes

- Full64 log work/build64-p1-full.log; artifact work/build64-p1-artifact.zip; independent archive receipt work/build64-compiled-app-check.json.
- Before/after timing evidence, all test logs, Clang output and JSON results: work/build64-local-reproduction. Accessible copy beside the latest report in P1 - Build64 Network Failure and Batch Fix.
- Base-file identity problem remains proven separately: both phones3463 files/634811175bytes identical;46 Japanese filename encodings.64's Apple Foundation tests now PASS that correction; do not conflate it with this final-message/close race.
- New core bug is reproduced locally under real encrypted UDP, not merely assumed from an error label. Final reliable verdict must be consumed before freeing native handle. Bounds and privacy remain intact; no room codes, secret tokens or peer IPs printed.
- Unverified fixes: New batch Apple/OpenSSL compilation/runtime and actual phone connection are not yet verified. Windows static/runtime passes do not certify iPhone behavior or internet connectivity.
- Exact next actions: Check recorded next run; on success prepare new IPA for BOTH phones and small T02 test, retaining settings/save backups. On failure read the now-specific stage/state report before another batch.

**END PROGRESS REPORT**
