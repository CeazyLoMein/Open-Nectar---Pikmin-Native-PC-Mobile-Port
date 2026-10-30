#pragma once
#include <cstdint>
// A top-level JAudio command may invoke another (for example captain-down
// also triggers a system jingle). Send the original command once; guest native
// playback performs the same nested work locally.
inline unsigned& pc_coop_audio_call_depth(){static unsigned depth=0;return depth;}
class PcCoopAudioCall {
public:
    PcCoopAudioCall(){++pc_coop_audio_call_depth();}
    ~PcCoopAudioCall(){--pc_coop_audio_call_depth();}
    PcCoopAudioCall(const PcCoopAudioCall&)=delete;
    PcCoopAudioCall& operator=(const PcCoopAudioCall&)=delete;
};
#if defined(NECTAR_COOP_WORLD)
namespace nectar
{
namespace net
{
class CoopSession;
}
} // namespace nectar
void pc_coop_audio_begin(bool host);
void pc_coop_audio_end();
bool pc_coop_audio_guest();
bool pc_coop_audio_host();
void pc_coop_audio_running(bool running);
void pc_coop_audio_tick(nectar::net::CoopSession &, std::uint64_t now);
void pc_coop_audio_spatial(const void *context, int type, int sound, bool start, bool loop, float x, float y, float z);
void pc_coop_audio_move(const void *context, float x, float y, float z);
void pc_coop_audio_release(const void *context);
// 5/6 player start/stop;7/8 system;9 formation;10 footstep. Native IDs only.
void pc_coop_audio_raw(unsigned kind, int sound, int x = 0, int y = 0);
int pc_coop_audio_backend_state();
void pc_coop_audio_counts(std::uint64_t &sent, std::uint64_t &played, std::uint64_t &dropped);
#else
inline bool pc_coop_audio_host() {return false;}
inline bool pc_coop_audio_guest()
{
    return false;
}
inline void pc_coop_audio_spatial(const void *, int, int, bool, bool, float, float, float)
{
}
inline void pc_coop_audio_move(const void *, float, float, float)
{
}
inline void pc_coop_audio_release(const void *)
{
}
inline void pc_coop_audio_raw(unsigned, int, int = 0, int = 0)
{
}
#endif
