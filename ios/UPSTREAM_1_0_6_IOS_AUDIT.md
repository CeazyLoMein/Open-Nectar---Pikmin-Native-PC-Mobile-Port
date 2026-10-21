# Upstream 1.0.5 / 1.0.6 audit for the native iOS branch

Inspected upstream main70c5c938862bef15a1434b2df3f5d4fa7a26e446 (release1.0.6, October20), tags1.0.5/1.0.6, and source diffs. No merge/rebase performed. Original iOS working branch began before several Android/desktop release fixes; a similar symptom is not proof our independently fixed iOS implementation is identical.

| Change | iOS decision and evidence |
|---|---|
| P1 deterministic RNG float range (4906449d / bc4e195a) | Adopted the exact current upstream pc_sim_rng.h/.cpp/test.cpp. Deterministic draws are15-bit, whereas Darwin RAND_MAX is31-bit. Ordinary solo libc RNG behavior remains unchanged. Local upstream test PASS with a Windows mode seam; CI links the actual deterministic-mode implementation on macOS. Important foundation for later co-op, not a shipped online feature. |
| P1 Windows DPI / Linux controller / desktop packaging | Platform-specific; not copied over iOS Retina/SDL framebuffer/native menu fixes. |
| P1/P2 launcher crash-report workflow (70c5c938/0db7e4e2) | Desktop/Android launcher integration is not an iOS recovery implementation. Existing native crash reports/USB retrieval remain; no crash handler or launch/relaunch code copied blindly. |
| P1 settings/controller tidying described by release notes | Reviewed against our readable mobile settings/touch changes. No whole-file replacement. Existing choice values and touch-layout keys preserved; new aiming options scoped explicitly to P1. |
| P2 Begin crash (5b1fcced) | Specifically Android bionic pthread cancellation/SIGUSR2 cleanup. Not copied to Darwin; our prior iOS startup/allocator fixes and positive phone test remain the baseline. |
| P2 audio / ARAM (eb499721 and related current audio source) | Upstream keeps PSM_FACTORY_HEAP_SIZE9MiB within emulated16MiB ARAM; ours still expands it4x. Upstream has subframe audio rendering and drop diagnostics absent from ours. These are separate from our verified scalar-layout, dry-mixer and opening-category mute fixes. Queue a tested P2 batch; do not replace working audio wholesale or claim the remaining differences currently cause audible failures. |
| P2 empty radar (2e2046ce) | Relevant renderer ordering: flush pending immediate primitive before depth/color/alpha state changes. Queue for P2 phase; compare against retained iOS native-presentation patch. |
| P2 wrong ship textures after cave exit (24424f96) | Relevant reused heap-address GXCopyTex cache; upstream32-byte fingerprint invalidates stale copies. Queue for repeated cave-entry/exit tests. |
| P2 dialogue/explorer kit IDs (35e77144) | Relevant data-layout fixes: preserve u8 texture-map index while byte-swapping .btp entries; encode u64 message tags big-endian. Queue against iOS adapter/64-bit fixes with real fixtures. |
| P2 animation/audio end repeats (127ac574), cursor flicker (97504665),60FPS constants (4794f647) | Potentially relevant at our60FPS setting. Queue functional comparisons/30vs60 tests across combat, timers, menus, effects and cave transitions. Do not treat newer desktop code as hardware-verified here. |

P2 receives no new source changes or CI run in this P1 batch. Shared P2 menu fixtures still pass188 iOS /198 desktop checks. Reassess newer upstream commits before the later P2 batch.

Primary sources: [official1.0.6 release](https://github.com/SSunnKing/Open-Nectar---Pikmin-Native-PC-Mobile-Port/releases/tag/1.0.6), the fetched commit diffs above. No APKs, game assets or unrelated downloads installed.
