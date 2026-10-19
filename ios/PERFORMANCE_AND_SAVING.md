# iPhone performance and saving

## Performance HUD

The new candidate adds **Settings → Display → Performance HUD → On**. Close the
settings menu to apply it. It defaults off and remembers the choice. It does not
change the selected FPS mode, scene quality or controls.

| Reading | Meaning |
| --- | --- |
| Render FPS / average ms | Frequency and interval of completed SDL render submissions, measured with a monotonic clock after swap. This is not a measurement of physical panel refresh or GPU utilisation. |
| Frame p95 / p99 | Slow-frame intervals among the most recent 240 submissions. These expose stutter hidden by an average. |
| App RAM | Process physical memory footprint, in MiB, reported by Mach task_info. |
| Spare MiB* | Apple's current advisory amount this app may allocate before its process limit. It is not total free phone RAM or a promise an HD pack will fit. |
| App CPU | Process CPU time divided by elapsed real time. 100% means one core; multiple threads can exceed100%. It is not total-device utilisation or proof the GPU has spare capacity. |
| Heat | iOS Nominal, Fair, Serious or Critical thermal state; not a temperature in degrees. |
| Low Power | Whether iOS Low Power Mode is enabled. |

Native memory/CPU/thermal readings and text refresh once per second. Frame history
uses a fixed-size buffer. Duplicate timestamps are ignored; backward clocks or a
gap over five seconds reset frame history and CPU baseline. The overlay does not
enable the much heavier per-draw developer profiler. When off, it performs no
native metric sampling or per-frame clock reads.

GPU utilisation is unavailable through this overlay. Unavailable native readings
say N/A/Unknown; zero spare memory is displayed as zero. No guessed utilisation,
temperature, supported-pack size or green "safe to install" verdict is provided.

At120FPS the frame interval is about8.33ms; at60FPS it is16.67ms. The selected mode
alone is not measured performance. Stable render pacing is encouraging, but it
does not reveal unused GPU percentage. A lightly populated early area also does
not predict later battles or a heavier texture/model pack.

### Comparing HD content

1. After a successful iOS build, enable the HUD and play a representative area for
   10-15minutes. Record FPS/p95/p99, RAM/spare and thermal state. Keep the normal FPS
   choice and other settings unchanged during the comparison.
2. Share a HUD screenshot or short reading summary. There is no universal pack-size
   rule: ZIP size, decoded RAM, renderer caches and GPU buffers differ.
3. Add one suitable mobile texture pack or model group at a time, restart as the
   importer requests, and repeat in the same area. Keep originals/backups.
4. If slow frames, memory pressure or Serious/Critical heat appear, reduce the
   workload before adding more. A60FPS option can be a useful comparison.

No external HD texture or model assets have been installed by the diagnostic work.
The new HUD still needs Apple compilation and real-device layout/reading checks.
The portable accumulator/controller has30host checks covering120/60FPS, slow tails,
ring wrap, suspension/invalid timestamps, multicore CPU, missing readings, zero
headroom, disabled cost and refresh throttling.

## How saving currently works

Source inspection found the existing normal **end-of-day save flow**, including
the memory-card/save UI and MemoryCard::saveCurrentGame. Complete that flow and
wait for the save to finish. There is no timed five-minute mid-day autosave or
save-anywhere button implemented in this iOS branch. A crash before the next
successful save can lose the current day's unsaved progress.

The native port writes GameCube-style card files into the app's writable game
folder. For ordinary P1 play the expected location in Files is:

**On My iPhone → Open Nectar Pikmin1 → pikmin1 → save → card0**

The game's settings file, pikmin_settings.conf, stores options separately from
progress. Randomizer and Speedrun use their own card subfolders. To back up existing
progress, close the game after a completed save and copy the whole save folder in
Files. Preserve app data when installing an update; keep a copy before uninstalling.
A folder copy preserves the latest saved checkpoint, not the unsaved live day.

The serializer stores PlayState and PlayerState/caches expected by the normal save
flow. It is not a snapshot of every live enemy, Pikmin action, carried object and
clock value. Calling it on a timer is not evidence that a mid-day position can be
restored correctly. No save routine, file format, existing save, or save timing was
modified during this performance change. The card layer's ordinary save path has
not yet been validated by a user save/close/relaunch/continue test in this session.

### Next saving work

1. Verify a normal end-of-day save survives closing/relaunching the iPhone app and
   Continue restores the expected day, parts and Pikmin totals.
2. Investigate a real mid-day recovery/manual-save design separately, including
   transient world state, safe snapshot points and rollback. Preserve existing slots
   and validate load behavior before enabling any periodic save feature.
3. Consider backup/recovery for normal completed checkpoints. Backups protect an
   existing save; they cannot recover unsaved minutes by themselves.

## Sources and limits

- Engine call sites: src/plugPikiColin/newPikiGame.cpp::DayOverModeState::update,
  src/plugPikiOgawa/ogSave.cpp, src/plugPikiColin/memoryCard.cpp::saveCurrentGame,
  writeCurrentGame/readCurrentGame, src/plugPikiKando/playerState.cpp::saveCard.
- Card location: pc_port/dolphin_stubs/card_stubs.cpp::saveRoot and ios/ios_storage.mm.
- [Apple app memory headroom](https://developer.apple.com/documentation/os/os_proc_available_memory)
- [Apple process/thermal state](https://developer.apple.com/documentation/foundation/processinfo)
- [Apple getrusage reference](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/getrusage.2.html)

The user reports120FPS mode feels beautiful. This is useful subjective hardware
feedback; measured render FPS, sustained temperatures/memory and HD headroom have
not been established yet. Online co-op with Raye remains the final milestone.
