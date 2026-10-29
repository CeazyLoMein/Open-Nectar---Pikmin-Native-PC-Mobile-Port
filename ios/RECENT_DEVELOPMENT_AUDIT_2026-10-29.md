# Open Nectar P1 review of recent development

Date: 2026-10-29, 09:04 EDT
Reviewed branch: ios-experimental, source HEAD 37a0e779 (matches fetched origin).

## Verdict and scope
No confirmed new destructive change or critical regression was identified in the reviewed recent changes. This is a bounded source/test audit, not proof that solo or co-op works on real phones. Reviewed changes from Build 78 source 0cc12367 through current HEAD, with particular attention to post-Build81 changes: saves, practice startup/ownership/input, iOS lifecycle/menu changes, network simulation, shared Onion foundations and seed landing. P2 source was unchanged in the post-Build81 range.

## Independent verification
- Build84 run 40773579467 completed SUCCESS at 4a886468d3c3a263d477fe1702cae290fed2cf83; both scene-startup and build (pikmin1) succeeded. This audit did not download or verify its IPA contents.
- Rebuilt current local networking targets and reran all 27 tests: 27/27 passed, including real encrypted local socket and stress checks. This is Windows/local networking evidence.
- Regenerated the save fixture from current source, compiled the extracted actual DoSave/DoList with actual CARD/history backend, and ran in a new GUID-named scratch directory: all 14 modeled recovery scenarios passed. No real player saves or phones were accessed. Engine/platform fixtures and injected failures are not real crash or power-loss tests.
- Independently compiled/reran the upstream-derived seed decision tests: passed. Checked System::pcTicksPer30Hz mapping against the integration call.
- Menu presentation source contract passed. It checks source structure; it does not operate the real iOS UI or verify visual appearance.
- Existing iOS workflow requires room, practice and encrypted socket runtime receipts before packaging; the recent changes did not remove those gates.

## Material limitations and priorities
1. The last user-reported two-phone gameplay had guest black view/stutter and interruption freezing. Later build success does not establish those symptoms are resolved. Two-phone practice remains the next decisive acceptance test.
2. Most recent changes are bounded hardening, diagnostics, tests or design notes. Shared Onion authority and visual smoothing have tests but are not connected to campaign gameplay. Cutscene synchronization, campaign save/rejoin and cross-progression remain unfinished. Do not count these as delivered features.
3. Production dependencies still disable ICE/WebRTC and current GNS transport uses direct IP sockets. Reliable internet play across arbitrary home/mobile networks has not been established. Isolated ICE library compilation is not an internet test.
4. Stale-input expiry deliberately drops actions older than 300ms. Rapid repeated taps can still coalesce before publication; this is documented and needs explicit throw/whistle/charge interaction testing before campaign use.
5. Save preservation is narrowly defensive: an uncertain sole temporary save is retained and an I/O error is returned. This can require manual recovery; it is not automatic repair, mid-day saving or power-loss durability. The whole save subsystem was not rewritten.
6. Current HEAD has post-Build84 stale held-input, seed and save changes that have only local verification. They must receive one batched iOS validation before recommending installation of that newer source.

## Next actions
Check and stage Build84 package if needed as a fallback. For continuing development, validate the accumulated post84 source in one P1 build, then use both phones to test guest view/movement, staggered entry, pause/resume and background/disconnect. Capture local practice diagnostics for any failure. Prioritize these observed failures over more unintegrated feature foundations. Preserve the user-accepted installed solo baseline and settings. P2 remains outside this audit's development scope.

Audit made no gameplay changes and installed nothing. No new iOS build was triggered for the audit itself.
