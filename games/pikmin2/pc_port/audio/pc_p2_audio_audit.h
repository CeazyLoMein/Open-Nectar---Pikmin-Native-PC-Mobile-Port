#pragma once
#include <cstddef>
#include <cstdint>

// Fixed-size counters only; game/audio call sites never open files or allocate.
// The iOS queue thread writes one bounded text report every five seconds.
namespace p2_audio_audit {
enum class Event { CreatureRequest, Culled, SceneBlocked, Submitted, Started };
enum class BankResult { Played, MissingBank, MissingInstrument, NoKeyRegion,
                        MissingWaveBank, MissingWave, MissingInfo, MissingData, NoChannel, PlayFailed, Count };
void event(std::uint32_t sound, Event kind);
void distance(std::uint32_t sound, float dist, float gain, unsigned listener);
void bank(BankResult result);
void source(unsigned format);
void render(const std::int16_t* samples, std::size_t frames, unsigned voices, std::uint32_t milliseconds);
}
