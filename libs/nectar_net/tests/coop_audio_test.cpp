#include "nectar_net/coop_audio.h"
#include <cstdio>
#include <limits>
using namespace nectar::net;
int errors = 0;
void check(bool b, const char *text)
{
    if (!b)
    {
        ++errors;
        std::printf("FAIL %s\n", text);
    }
}
int main()
{
    AudioCue cue;
    cue.kind = AudioKind::SpatialPlay;
    cue.emitter = 9;
    cue.type = 6;
    cue.sound = 2;
    cue.position = {1, 2, 3};
    std::vector<AudioCue> out;
    const auto bytes = encodeAudio({cue});
    check(bytes.size() == 25 && decodeAudio(bytes.data(), bytes.size(), out) && out.size() == 1 &&
              out[0].position.z == 3,
          "bounded spatial cue roundtrip");
    for (std::size_t n = 0; n < bytes.size(); ++n)
        check(!decodeAudio(bytes.data(), n, out), "truncation rejected atomically");
    auto bad = bytes;
    bad.push_back(0);
    check(!decodeAudio(bad.data(), bad.size(), out), "trailing bytes rejected");
    bad = bytes;
    bad[1] = 255;
    check(!decodeAudio(bad.data(), bad.size(), out), "unknown cue kind rejected");
    bad = bytes;
    bad[10] = 2;
    check(!decodeAudio(bad.data(), bad.size(), out), "non-boolean loop field rejected");
    cue.position.x = std::numeric_limits<float>::quiet_NaN();
    check(encodeAudio({cue}).empty(), "NaN rejected");
    cue.position.x = kMaxWorldCoordinate + 1;
    check(encodeAudio({cue}).empty(), "unbounded position rejected");
    cue.position.x = 0;
    cue.emitter = 0;
    check(encodeAudio({cue}).empty(), "no raw null emitter");
    cue.emitter = 1;
    cue.type = 9;
    check(encodeAudio({cue}).empty(), "unknown engine event type rejected");
    cue.type = 6;
    cue.player = 1;
    check(encodeAudio({cue}).empty(), "spatial effects cannot choose a captain");
    cue = {};
    cue.kind = AudioKind::PlayerPlay;
    cue.player = 1;
    cue.sound = 0x8005;
    check(!encodeAudio({cue}).empty(), "captain-specific original Pikmin voice ID accepted");
    cue.sound = 0x8100;
    check(encodeAudio({cue}).empty(), "invalid player command rejected");
    cue.sound = 1;
    cue.player = 2;
    check(encodeAudio({cue}).empty(), "unknown captain rejected");
    cue = {};
    std::vector<AudioCue> maximum(kAudioBatchCues, cue);
    check(!encodeAudio(maximum).empty(), "maximum packet stays below actor MTU");
    maximum.push_back(cue);
    check(encodeAudio(maximum).empty() && encodeAudio({}).empty(), "oversized and empty batches rejected");
    check(out.size() == 1 && out[0].emitter == 9, "failed decode does not mutate previous output");
    std::puts(errors ? "AUDIO CODEC FAIL" : "AUDIO CODEC PASS");
    return errors ? 1 : 0;
}
