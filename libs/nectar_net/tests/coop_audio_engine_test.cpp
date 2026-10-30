#include "SoundMgr.h"
#include "audio/pc_audio_source.h"
#include "jaudio/pikiinter.h"
#include "nectar_net/coop_session.h"
#include "netplay/pc_coop_audio.h"
#include <cmath>
#include <cstdio>
using namespace nectar::net;
SeSystem engine;
SeSystem *seSystem = &engine;
int local = 0, errors = 0, activeVoices = 0, spatialPlays = 0, stops = 0, playerPlays = 0, steps = 0, formations = 0,
    systemPlays = 0, initializations = 0;
float lastRelativeX = 0;
bool practice = true, eventsPaused = false;
void pc_audio_set_events_paused(bool p)
{
    eventsPaused = p;
}
void Jac_PauseOrimaSe()
{
    eventsPaused = true;
}
void Jac_UnPauseOrimaSe()
{
    eventsPaused = false;
}
void check(bool b, const char *s)
{
    if (!b)
    {
        ++errors;
        std::printf("FAIL %s\n", s);
    }
}
bool pc_netplay_session_active()
{
    return false;
}
bool pc_coop_practice_active()
{
    return practice;
}
extern "C"
{
    int pc_netplay_present_two_pass_active()
    {
        return 0;
    }
    int pc_netplay_present_single_view()
    {
        return practice ? 1 : 0;
    }
    int pc_netplay_present_local_player()
    {
        return local;
    }
    int Jac_DestroyEvent(int)
    {
        --activeVoices;
        return 1;
    }
    int Jac_UpdateEventPosition(int, SVector_ *p)
    {
        lastRelativeX = p->x;
        return 1;
    }
    int Jac_CreateEvent(std::uint32_t, SVector_ *p)
    {
        lastRelativeX = p->x;
        return activeVoices++;
    }
    int Jac_PlayEventAction(int, int)
    {
        ++spatialPlays;
        return 1;
    }
    int Jac_StopEventAction(int, int)
    {
        ++stops;
        return 1;
    }
    void Jac_InitAllEvent()
    {
        activeVoices = 0;
        ++initializations;
    }
    void Jac_StopOrimaSe(int)
    {
    }
    void Jac_PlayOrimaSe(std::uint32_t)
    {
        if (pc_audio_source_audible())
            ++playerPlays;
    }
    void Jac_Orima_Formation(int x, int y)
    {
        if (pc_audio_source_audible() && (x || y))
            ++formations;
    }
    void Jac_Orima_Walk(int, std::uint32_t)
    {
        if (pc_audio_source_audible())
            ++steps;
    }
    void Jac_PlaySystemSe(int)
    {
        ++systemPlays;
    }
    void Jac_StopSystemSe(int)
    {
    }
}
int main()
{
    CoopSession session;
    int context = 0;
    pc_coop_audio_begin(true);
    pc_coop_audio_running(true);
    pc_coop_audio_spatial(&context, 6, 2, true, true, 100, 20, 30);
    {
        PcAudioSource other(1);
        check(!pc_audio_source_audible(), "host locally mutes other captain");
        pc_coop_audio_raw(5, 0x8005);
        pc_coop_audio_raw(10, 1);
        pc_coop_audio_raw(9, 0, 60, 0);
    }
    {
        PcAudioSource own(0);
        pc_coop_audio_raw(5, 6);
    }
    pc_coop_audio_tick(session, 1000);
    auto first = session.out;
    check(first.size() == 6 && first[0].kind == AudioKind::Reset, "initial reset and all live sounds batched once");
    const auto token = first.size() > 1 ? first[1].emitter : 0;
    check(token != 0 && first[1].position.x == 100, "only opaque token and WORLD position are emitted");
    session.out.clear();
    pc_coop_audio_move(&context, 150, 20, 30);
    pc_coop_audio_tick(session, 1050);
    check(session.out.size() == 1 && session.out[0].kind == AudioKind::SpatialMove && session.out[0].emitter == token,
          "emitter movement coalesces into one update");
    auto movement = session.out;
    session.out.clear();
    pc_coop_audio_running(false);
    pc_coop_audio_raw(5, 1);
    pc_coop_audio_tick(session, 1100);
    check(session.out.empty() && eventsPaused, "pause queues no fresh sounds and freezes host effects");
    pc_coop_audio_running(true);
    pc_coop_audio_tick(session, 1150);
    check(!eventsPaused && session.out.size() == 2 && session.out[1].loop,
          "resume restores active loop but does not repeat old throw or voice");
    pc_coop_audio_end();
    local = 1;
    pc_coop_audio_begin(false);
    pc_coop_audio_running(true);
    check(pc_coop_audio_guest() && initializations == 1, "guest starts with isolated positional audio");
    engine.listenerX = 25;
    session.in = first;
    pc_coop_audio_tick(session, 1200);
    check(spatialPlays == 1 && std::fabs(lastRelativeX - 75) < .01f,
          "guest computes position against its OWN listener");
    check(playerPlays == 1 && steps == 1 && formations == 1,
          "guest hears its own captain even though host filtered that captain locally");
    session.in = movement;
    pc_coop_audio_tick(session, 1250);
    check(std::fabs(lastRelativeX - 125) < .01f, "moving emitter updates distance and panning");
    engine.listenerX = 40;
    pc_coop_audio_tick(session, 1260);
    check(std::fabs(lastRelativeX - 110) < .01f, "moving guest listener updates sounds without new host packet");
    check(spatialPlays == 1 && playerPlays == 1, "render updates never replay one-shots");
    AudioCue stop;
    stop.kind = AudioKind::SpatialStop;
    stop.type = 6;
    stop.emitter = token;
    stop.sound = 2;
    session.in = {stop};
    pc_coop_audio_tick(session, 1300);
    check(stops == 1, "stop action reaches backend");
    stop.kind = AudioKind::SpatialRelease;
    session.in = {stop};
    pc_coop_audio_tick(session, 1350);
    check(activeVoices == 0, "release frees guest event handle");
    session.in = {first[1]};
    pc_coop_audio_tick(session, 1400);
    check(activeVoices == 1, "loop restarted for cleanup test");
    pc_coop_audio_running(false);
    check(activeVoices == 0, "pause destroys all guest loop handles");
    pc_coop_audio_running(true);
    session.in = {first[1]};
    pc_coop_audio_tick(session, 1450);
    pc_coop_audio_end();
    check(activeVoices == 0 && !pc_coop_audio_guest(), "ending session clears playback and identity");
    // A failed/slow sender cannot allocate an unbounded event queue or strand an old loop.
    pc_coop_audio_begin(true);
    pc_coop_audio_running(true);
    session.out.clear();
    session.blocked = true;
    for (int n = 0; n < 1000; ++n)
        pc_coop_audio_raw(5, 1);
    session.blocked = false;
    pc_coop_audio_tick(session, 2000);
    std::uint64_t sent = 0, played = 0, dropped = 0;
    pc_coop_audio_counts(sent, played, dropped);
    check(dropped > 0 && session.out.size() == 1 && session.out[0].kind == AudioKind::Reset,
          "overflow fails silent with bounded reset, no stale sound storm");
    pc_coop_audio_end();
    pc_coop_audio_begin(true);pc_coop_audio_running(true);session.out.clear();
    for(int n=0;n<1000;++n)pc_coop_audio_raw(5,8);
    pc_coop_audio_tick(session,3000);
    check(session.out.size()==2 && session.out[1].sound==8,"held whistle coalesces instead of filling network queue at high FPS");
    pc_coop_audio_end();
    pc_coop_audio_begin(true);pc_coop_audio_running(true);session.out.clear();
    {PcCoopAudioCall outer;pc_coop_audio_raw(5,12);{PcCoopAudioCall nested;pc_coop_audio_raw(7,40);}}
    pc_coop_audio_tick(session,4000);
    check(session.out.size()==2 && session.out[1].kind==AudioKind::PlayerPlay,"nested native command relays once, avoiding duplicate jingle playback");
    pc_coop_audio_end();
    practice = false;
    {
        PcAudioSource other(1);
        check(pc_audio_source_audible(), "solo keeps original sound ownership");
    }
    std::puts(errors ? "AUDIO ENGINE FAIL" : "AUDIO ENGINE PASS");
    return errors ? 1 : 0;
}
