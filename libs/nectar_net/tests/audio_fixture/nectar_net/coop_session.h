#pragma once
#include "nectar_net/coop_audio.h"
namespace nectar::net {
// Narrow engine-adapter test double only. Real role/sequence/revision delivery is
// independently exercised by coop_session_test over the actual authenticated link.
class CoopSession {
public:
 std::vector<AudioCue> in,out;bool blocked=false;
 bool publishAudio(const std::vector<AudioCue>& cues,std::uint64_t) {
  if(blocked || encodeAudio(cues).empty())return false;
  out.insert(out.end(),cues.begin(),cues.end());return true;
 }
 std::vector<AudioCue> takeAudio(std::uint64_t){auto cues=in;in.clear();return cues;}
};
}
