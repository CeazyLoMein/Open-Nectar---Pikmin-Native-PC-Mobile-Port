## Build63 native regression failure; path handling and diagnostic follow-up — October25

63/run40215584390/source405ab5ef8432e427366056fc82e607c67c8dfbc6 completed FAILURE. Scene startup job121235891954 SUCCESS. P1 job121238470144 failed Check native Host Join screen and generated build identity: the actual new Foundation test COMPILED, then exited with exactly `FAIL: hash valid fixture`. No compiler/linker error was present; full P1 build/IPA did not run. The original test did not identify which valid fixture or which rejection branch. Exact branch/cause therefore remains UNCONFIRMED; do not record a proven macOS-alias cause from this log alone.

Implemented a scoped follow-up: stable rejection-stage enum (no room-code/private-data logging), labelled fixture progress/failure, explicit intended reasons for empty-tree/symlink rejection, consistent standardization of BOTH root and enumerated paths for scope checks, raw enumerated filesystem paths retained for reads, and native /var-versus-/private/var alias coverage. Apple documents that Foundation standardization/resolution can remove /private (https://developer.apple.com/documentation/foundation/nsurl/standardizingpath?language=objc); alias handling is a supported hardening hypothesis, not a verified diagnosis of63. NFC identity keys and strict byte/name/case/symlink/alias-collision checks remain. Local2 build-identity+3 bundle+8 runner tests PASS; diff check PASS. Actual Foundation/iOS compilation/runtime awaits next P1-only build. Native regression was not disabled or bypassed.

Both-phone audit remains proven:3463 files/634811175bytes identical;46 Japanese NFC/NFD names caused62 false content rejection. No phone files changed.63 produced no installable IPA; current installed62 still needs corrected build on BOTH phones, then repeat T02. T03/T04 remain untested. Both phones can stay disconnected/closed while CI runs. P2 unchanged. Main-menu Online Co-op and separate Solo/shared slots are approved future work after connection passes, not implemented by this follow-up. Full63 job log saved privately in work/build63-p1-full.log and accessible handoff folder. Next source/run follows; avoid idle CI polling.

## User-approved upcoming UX — main menu Online Co-op and separate campaigns

After connection validation, add title-menu Online Co-op > Host/Join beside existing local Co-op, with personal offline Solo and a separately labelled shared campaign (numbered slots acceptable). Existing indexed slot/day-history code supports this direction, but multiplayer campaign identity/slot binding and write protection still need implementation/testing. Preserve occupied slots, whole-card backup and solo progress; joining targets the host's campaign, not the guest's solo slot. Detailed approved plan in PIKMIN1_COOP_IMPLEMENTATION.md and COOP_CROSS_PROGRESSION_AND_RECOVERY.md. No menu/save/runtime changes now; Build63/source405ab5ef/run40215584390 remains the pending identity-fix validation. No extra native build triggered. T02 false mismatch on62 still awaits corrected build/retest. P2 unchanged.

## Build63 dispatched — Unicode filename identity fix

Source 405ab5ef8432e427366056fc82e607c67c8dfbc6; run40215584390 (https://github.com/CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port/actions/runs/40215584390); last observed in_progress, no conclusion or new IPA yet. Both phone base-data audits complete; all3463 files/634811175bytes match,46 Japanese filename encodings caused62's false rejection. NFC source fix plus actual native Foundation regression queued.13 local regressions PASS and corrected independent full-data digest matches. T02 FAILED62; wait for verified63 then update BOTH and repeat room test. Both phones may disconnect now; no game data/settings/save/pack writes. P2 unchanged. No idle polling requested; user reports build result.

# OPEN NECTAR iOS — CODEX PROGRESS REPORT

**Date/time:** October25,2026; real-phone Build62 join failure investigated.

**Overall project status:** Both Build62 installations user-reported ready. First private-room join rejected with different game data. Confirmed identity-check bug; source fix implemented and local checks passed. Next P1-only native build pending. No phone files modified.

### Pikmin 1

- Current objective: Fix false game-data mismatch, then repeat T02 room connection.
- What was investigated: Read-only inventories and complete per-file SHA256 of assets/dataDir on both USB phones; actual contentIdentity implementation.
- Root cause: Both phones contain3463 base files/634811175bytes, all contents and sizes identical.46 Japanese filenames are NFC on Raye's phone versus NFD on yours. Build62 hashes literal UTF8 filename bytes; visually equivalent filenames therefore produce different tree hashes. This is proven from both actual phone inventories, not an assumed texture-pack difference.
- Files changed: ios/ios_coop_content_identity.h (shared actual hash function, canonical NFC identity keys mapped to original filesystem paths, ambiguous alias rejection, domainv2); ios/ios_coop_room.mm (use helper); tests/ios_coop_content_identity_test.mm; experimental workflow (compile/run actual Foundation hash tests on macOS before full iPhoneOS UI compilation). Existing file size/content hashes, case distinctions, symlink rejection and source build gates retained.
- Tests and results: Both phone manifests match canonical source file bytes exactly. Legacy digests differ; corrected independent NFC recomputation matches at 26719287a52022d2ced07b74edb4c7a990c310e8554a63e91deec87652bfb8ba. Local2 build-identity+3 bundle+8 network-runner tests PASS; diff check PASS. New actual Foundation test covers direct NFC/NFD equivalence, real trees, creation order, changed contents/names, independent golden hash, extra files and symlink rejection. Apple native execution/compilation pending CI; no claim of hardware fix yet.
- Confirmed working: Historical solo baselines; both62 installs user-reported. Both pre-update backups retained. No successful new phone connection yet.
- Remaining issues: T02 FAILED on62; full playable co-op, gameplay-state integration, durable mid-day saves and cross-device progress remain future work. User may disconnect both phones now; all reading finished.

### Pikmin 2

- Current objective: Preserve working port while P1 networking is validated.
- What was investigated: Nothing new in P2 for this fix.
- Root cause or leading hypothesis: No new P2 issue reported.
- Files changed: None in P2; experimental build will select P1 only.
- Tests and results: No new P2 run requested.
- Confirmed working: Prior user-reported working P2 on both phones; not retested this turn.
- Remaining issues: Future P2 co-op and wider campaign validation.

### GitHub

- Repository: CeazyLoMein/Open-Nectar---Pikmin-Native-PC-Mobile-Port
- Branch: ios-experimental
- Starting commit: 59480c3b44e6d332ca43a3fb39882910a3a1ec03
- Latest source commit: 405ab5ef8432e427366056fc82e607c67c8dfbc6; Build63/run40215584390 in progress. Later documentation-only commit recorded in Exact Resume State.json.
- Commits created: Next source commit contains only identity fix, native regression and journal/checklist updates.
- Changes pushed: Scoped source/test/workflow/report commit pushed; Build63 selected P1 only.
- Uncommitted changes: None after documented source/dispatch commits.
- GitHub Actions run IDs: Previous62/run40210863029/source b8abc62ecddd146f411d136c0ab9f6095ee9d858 SUCCESS; phone join FAILED. Next native run not yet assigned at this checkpoint.
- Build results: New source not yet compiled on Apple; no native success claimed.
- Artifacts produced: No new IPA yet. Existing verified62 and known-working54 rollback retained.

### Next steps

- Next Pikmin 1 task: Native compile/run actual hash regression and full P1 package validation; stage verified new IPA only after success.
- Next Pikmin 2 task: Keep working installation unchanged.
- GitHub/build task: Push one scoped P1-only [ios-build] commit; record exact source/run, no idle CI polling.
- Anything requiring user involvement: Nothing while building. Both phones can unplug/P1 can close. After verified package, update BOTH with the same new IPA and repeat T02 before T03/T04.

### ChatGPT continuation notes

- Both actual phone inventories prove identical base data; no recopy, cleanup, pack deletion or arbitrary compatibility bypass needed.
- Important source-file locations: ios/ios_coop_content_identity.h and ios/ios_coop_room.mm; tests/ios_coop_content_identity_test.mm; .github/workflows/ios-native-experimental.yml.
- Relevant logs: Private work/build62-your-content-audit.json, build62-raye-content-audit.json, build62-content-mismatch-root-cause.json. These contain game-file paths/hashes only and remain outside public Git. Room codes/credentials never collected or logged.
- Unverified fixes: Native NFC implementation and actual two-phone join await next build and hardware test.
- Risks and warnings: New identity domain/build must match on both phones; one62 plus one new build cannot join. No live gameplay networking is implemented by this change.
- Exact next actions: Check next native run; on success verify/stage IPA, preserve backups and request same-Wi-Fi Host/Join retest. Record T02 failure on62 and keep future runtime tasks untested.

**END PROGRESS REPORT**
