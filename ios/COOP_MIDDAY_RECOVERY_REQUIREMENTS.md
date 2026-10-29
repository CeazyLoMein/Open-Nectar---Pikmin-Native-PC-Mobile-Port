# Required full PC/iPhone co-op campaign recovery

Status: requirements and implementation plan, 2026-10-29. NOT implemented.

The user requires PC+PC, iPhone+iPhone and either mixed pairing, either host, independent full game views, and shared campaign continuation when changing devices. Mid-day autosave is mandatory for the finished mode. Restarting the day is not an acceptable normal recovery policy. Keep offline solo and the shared campaign distinct.

## Interruption behavior to implement and verify

| Event | Intended response |
| --- | --- |
| Incoming call or full-screen FaceTime | Hold the authoritative world on interruption; clear stale controls. Resume only after both return and agree Ready. |
| Screen locks, app backgrounds, notification/app switch | Treat as an interruption even if sockets remain connected. Preserve the live world in memory while the process lives. Do not promise indefinite background execution on iOS. |
| Guest connection drops but host lives | Host retains the exact live world, holds safely for the first recovery implementation, and offers reconnect or recover/save-and-end. Guest must load a verified fresh baseline before resuming. |
| Host network drops but process lives | Hold safely. Reconnect to the same authority/session only after validating identity and world generation. Avoid two hosts advancing diverging campaigns. |
| Either app is swipe-closed, crashes, or is killed by OS | Restore the latest fully committed mid-day checkpoint. Never depend on an exit callback or final background write. Guest reconnect alone cannot reconstruct a host world lost from memory. |
| Host battery dies or device becomes unavailable | Offer the last verified durable campaign checkpoint; a guest-side copy of accepted recovery data is a safety goal. Automatic live host migration is a separate feature, not promised by the current design. |
| PC sleep, minimize, Alt-Tab, Windows session lock | Separate loss of input focus from a healthy room; first implementation pauses and releases controls. Resume deliberately; no movement catch-up or old queued actions. |
| Switch host campaign from PC to iPhone or back | Transfer a versioned campaign snapshot, verify hash/build/schema and campaign ID/revision, retain backups and reject ambiguous newer/older conflicting histories. Personal settings/camera/cosmetic packs and credentials remain local. |

## Save implementation boundaries

Capture a coherent world at a safe authoritative tick, then serialize/write without advancing a half-captured state. A snapshot needs more than the existing visual actor frames: game clock/day, area, progression, part and Onion inventory, Pikmin ownership/lifecycle/formation, jobs and carrying targets, enemies/health/AI timers, environmental changes, generator state, RNG and story/cutscene state must be restored consistently. Never serialize raw pointers; remap stable IDs with explicit schema/version handling. Mid-scene checkpoints need a safe recovery policy so rewards and transitions cannot run twice.

Use periodic snapshots during play, with extra best-effort snapshots at safe interruptions/transitions. A provisional interval around 20-30 seconds may be evaluated, but the actual interval, CPU cost and rollback bound must be measured. Do not advertise a specific guarantee before testing. Keep multiple validated generations; commit a complete new snapshot before replacing a previous good one. Short writes, disk-full, permission errors, corrupted metadata and process termination must leave an older recoverable generation and a clear message.

Snapshot mirroring to the guest must be acknowledged and generation/hash validated before being described as available. Campaign transfer must not clone player/device identities, network secrets, signing data or private cosmetic content. Saves stay private. No cloud provider or account requirement has been selected.

## Required acceptance tests

- Fresh process save/load round trip during travel, combat, carrying, plucking, Onion use, part collection and area transition; verify counts, ownership, progression and time without duplication or missing actors.
- Interrupt host and guest separately with Home, full-screen call/FaceTime, lock, sleep, network cut, forced app close and simulated crash. Test both reconnection to a living host and cold recovery after host death.
- Kill at each snapshot capture/write/validate/commit step; corrupt/truncate the newest generation and confirm fallback. Existing normal CARD save tests do not prove this new snapshot subsystem.
- Repeat on PC and iPhone with different personal graphics/controls, then transfer the campaign both ways and mix host/guest roles.
- Verify repeated or out-of-order transfers cannot duplicate progress or silently overwrite a newer campaign. Verify solo saves/settings remain unchanged.
- Measure pauses, storage growth, heat and frame-time impact on both phones and PC before enabling autosave by default.

The immediate engineering task remains a real Windows game client compatible with the iOS practice adapter. Full campaign world replication and this save subsystem must follow before claiming the envisioned co-op mode is complete.
