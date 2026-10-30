#include "netplay/pc_coop_audio.h"
#include "SoundMgr.h"
#include "audio/pc_audio.h"
#include "audio/pc_audio_source.h"
#include "jaudio/piki_player.h"
#if PIKI_USE_JAUDIO
#include "jaudio/pikidemo.h"
#endif
#include "jaudio/pikiinter.h"
#include "jaudio/verysimple.h"
#include "nectar_net/coop_session.h"
#include <algorithm>
#include <array>
#include <deque>

namespace
{
namespace net = nectar::net;
using net::AudioCue;
using net::AudioKind;
struct Source
{
    const void *context = nullptr;
    std::uint32_t token = 0;
    std::uint8_t type = 0;
    net::Vec3 position;
    std::array<int, 16> loops;
    bool dirty = false;
    Source()
    {
        loops.fill(-1);
    }
};
struct Voice
{
    std::uint32_t token = 0;
    int handle = -1;
    net::Vec3 position;
};
std::array<Source, 16> sources;
std::array<Voice, 16> voices;
std::deque<AudioCue> pending;
std::array<std::array<int, 2>, 3> formation{};
std::array<bool,3> whistles{},flyReady{};
std::uint32_t nextToken = 0;
std::uint64_t lastFlush = 0, sent = 0, played = 0, dropped = 0;
bool active = false, host = false, running = false, resync = false, replaying = false, flushed = false;
AudioCue spatial(const Source &s, AudioKind kind, int sound = 0, bool loop = false)
{
    AudioCue c;
    c.kind = kind;
    c.emitter = s.token;
    c.type = s.type;
    c.position = s.position;
    c.sound = static_cast<std::uint16_t>(sound);
    c.loop = loop;
    return c;
}
void queue(const AudioCue &c)
{
    if (!running || replaying || !net::validAudioCue(c))
        return;
    if (pending.size() >= net::kAudioQueueCues)
    {
        pending.clear();
        resync = true;
        ++dropped;
        return;
    }
    pending.push_back(c);
}
Source *find(const void *context)
{
    for (auto &s : sources)
        if (s.context == context)
            return &s;
    return nullptr;
}
void silence()
{
    replaying = true;
    for (auto &v : voices)
    {
        if (v.handle >= 0)
            Jac_DestroyEvent(v.handle);
        v = Voice{};
    }
    {
        PcAudioSource all(-1);
        Jac_StopOrimaSe(JACORIMA_Gather);
        Jac_Orima_Formation(0, 0);
    }
    replaying = false;
}
void resetPending()
{
    pending.clear();
    pending.push_back(AudioCue{});
    for (const auto &s : sources)
        if (s.context)
            for (int sound : s.loops)
                if (sound >= 0) {
                    if(pending.size()<net::kAudioQueueCues)pending.push_back(spatial(s, AudioKind::SpatialPlay, sound, true));
                    else ++dropped;
                }
    resync = false;
}
void position(Voice &v)
{
    if (!seSystem || v.handle < 0)
        return;
    Vector3f world(v.position.x, v.position.y, v.position.z), relative;
    seSystem->calcCameraPos(world, relative);
    SVector_ pos = {relative.x, relative.y, relative.z};
    Jac_UpdateEventPosition(v.handle, &pos);
}
void apply(const AudioCue &c)
{
    if (c.kind == AudioKind::Reset)
    {
        silence();
        return;
    }
    if (c.kind >= AudioKind::SpatialPlay && c.kind <= AudioKind::SpatialRelease)
    {
        Voice *v = nullptr;
        for (auto &candidate : voices)
            if (candidate.token == c.emitter)
            {
                v = &candidate;
                break;
            }
        if (c.kind == AudioKind::SpatialPlay && !v && seSystem)
        {
            for (auto &candidate : voices)
                if (!candidate.token)
                {
                    v = &candidate;
                    break;
                }
            if (v)
            {
                Vector3f world(c.position.x, c.position.y, c.position.z), relative;
                seSystem->calcCameraPos(world, relative);
                SVector_ pos = {relative.x, relative.y, relative.z};
                v->handle = Jac_CreateEvent(c.type, &pos);
                if (v->handle >= 0)
                    v->token = c.emitter;
                else
                    v = nullptr;
            }
        }
        if (!v)
        {
            ++dropped;
            return;
        }
        v->position = c.position;
        position(*v);
        if (c.kind == AudioKind::SpatialPlay)
        {
            if (!Jac_PlayEventAction(v->handle, c.sound))
                ++dropped;
        }
        else if (c.kind == AudioKind::SpatialStop)
            Jac_StopEventAction(v->handle, c.sound);
        else if (c.kind == AudioKind::SpatialRelease)
        {
            Jac_DestroyEvent(v->handle);
            *v = Voice{};
        }
    }
    else
    {
        PcAudioSource source(c.player == 255 ? -1 : c.player);
        switch (c.kind)
        {
        case AudioKind::PlayerPlay:
            Jac_PlayOrimaSe(c.sound);
            break;
        case AudioKind::PlayerStop:
            Jac_StopOrimaSe(c.sound);
            break;
        case AudioKind::SystemPlay:
            Jac_PlaySystemSe(c.sound);
            break;
        case AudioKind::SystemStop:
            Jac_StopSystemSe(c.sound);
            break;
        case AudioKind::Formation:
            Jac_Orima_Formation(c.x, c.y);
            break;
        case AudioKind::Footstep:
            Jac_Orima_Walk(c.sound, 0);
            break;
        default:
            break;
        }
    }
    ++played;
}
} // namespace
void pc_coop_audio_begin(bool isHost)
{
    pc_coop_audio_end();
    host = isHost;
    active = true;
    nextToken = 0;
    sent = played = dropped = 0;
    // Guest AI is dormant; discard its load-time positional effects, not music.
    if (!host)
    {
        replaying = true;
        Jac_InitAllEvent();
        replaying = false;
    }
}
bool pc_coop_audio_host() {return active && host;}
bool pc_coop_audio_guest()
{
    return active && !host;
}
void pc_coop_audio_end()
{
    if (active)
    {
        if (!host)
            silence();
        // The held practice scene requires restart; freeze its effects too.
#if PIKI_USE_JAUDIO
        Jac_PlaySystemSe(JACSYS_Pause);
#else
        Jac_PauseOrimaSe();
        pc_audio_set_events_paused(true);
#endif
    }
    active = host = running = resync = replaying = flushed = false;
    lastFlush = 0;
    pending.clear();
    sources = {};
    voices = {};
    formation = {};whistles={};flyReady={};
}
void pc_coop_audio_running(bool value)
{
    if (!active || value == running)
        return;
    running = value;
    pending.clear();
    flushed = false;
    formation = {};whistles={};flyReady={};
#if PIKI_USE_JAUDIO
    // Original JAudio owns its own sequence tracks. The fallback SDL mixer
    // pause flags do not control the native DSP graph.
    Jac_PlaySystemSe(value?JACSYS_Unpause:JACSYS_Pause);
#else
    if (value)
        Jac_UnPauseOrimaSe();
    else
    {
        Jac_PauseOrimaSe();
        pc_audio_set_events_paused(true);
    }
#endif
    if (!host)
        silence();
    else if (value)
        resetPending();
}
void pc_coop_audio_spatial(const void *context, int type, int sound, bool start, bool loop, float x, float y, float z)
{
    if (!active || !host || replaying || !context || type < 1 || type > 8 || sound < 0 || sound > 511)
        return;
    auto *s = find(context);
    if (!s && start)
    {
        for (auto &candidate : sources)
            if (!candidate.context)
            {
                s = &candidate;
                break;
            }
        if (!s || nextToken == 0xffffffffu)
        {
            ++dropped;
            return;
        }
        s->context = context;
        s->token = ++nextToken;
        s->type = static_cast<std::uint8_t>(type);
    }
    if (!s)
        return;
    s->position = {x, y, z};
    if (loop && start && std::find(s->loops.begin(), s->loops.end(), sound) == s->loops.end())
        for (auto &item : s->loops)
            if (item < 0)
            {
                item = sound;
                break;
            }
    if (!start)
        for (auto &item : s->loops)
            if (item == sound)
                item = -1;
    queue(spatial(*s, start ? AudioKind::SpatialPlay : AudioKind::SpatialStop, sound, loop));
}
void pc_coop_audio_move(const void *context, float x, float y, float z)
{
    if (!active || !host || replaying)
        return;
    if (auto *s = find(context))
    {
        if (s->position.x != x || s->position.y != y || s->position.z != z)
            s->dirty = true;
        s->position = {x, y, z};
    }
}
void pc_coop_audio_release(const void *context)
{
    if (!active || !host || replaying)
        return;
    if (auto *s = find(context))
    {
        queue(spatial(*s, AudioKind::SpatialRelease));
        *s = Source{};
    }
}
void pc_coop_audio_raw(unsigned kind, int sound, int x, int y)
{
    if (!active || !host || !running || replaying || pc_coop_audio_call_depth()>1 || kind < 5 || kind > 10 || sound < 0 || sound > 0x80ff)
        return;
    AudioCue c;
    c.kind = static_cast<AudioKind>(kind);
    c.sound = static_cast<std::uint16_t>(sound);
    const int player = pc_audio_source_captain_slot();
    c.player = player < 0 ? 255 : static_cast<std::uint8_t>(player);
    c.x = static_cast<std::int8_t>(std::clamp(x, -127, 127));
    c.y = static_cast<std::int8_t>(std::clamp(y, -127, 127));
    const auto ownerSlot=c.player==255?2:c.player;
    if(ownerSlot>2)return;
    if(c.kind==AudioKind::PlayerPlay) {
        if(c.sound==0x8004 && flyReady[ownerSlot])return;
        if(c.sound==0x8004)flyReady[ownerSlot]=true;
        if(c.sound==0x8002)flyReady[ownerSlot]=false;
    }
    if((c.kind==AudioKind::PlayerPlay || c.kind==AudioKind::PlayerStop) && c.sound==JACORIMA_Gather) {
        const bool start=c.kind==AudioKind::PlayerPlay;
        if(start && whistles[ownerSlot])return;
        whistles[ownerSlot]=start;
        if(!start && c.player==255)whistles={};
    }
    if (c.kind == AudioKind::Formation)
    {
        const auto slot = c.player == 255 ? 2 : c.player;
        if (slot > 2)
            return;
        if (formation[slot][0] == c.x && formation[slot][1] == c.y)
            return;
        formation[slot] = {c.x, c.y};
    }
    queue(c);
}
void pc_coop_audio_tick(net::CoopSession &s, std::uint64_t now)
{
    if (!active || !running)
        return;
    if (!host)
    {
        const auto cues = s.takeAudio(now);
        replaying = true;
        for (const auto &c : cues)
            apply(c);
        for (auto &v : voices)
            if (v.token)
                position(v);
        replaying = false;
        return;
    }
    if (flushed && now >= lastFlush && now - lastFlush < 50)
        return;
    flushed = true;
    lastFlush = now;
    if (resync)
        resetPending();
    for (auto &source : sources)
        if (source.context && source.dirty)
        {
            queue(spatial(source, AudioKind::SpatialMove));
            source.dirty = false;
        }
    if (resync)
        resetPending();
    std::vector<AudioCue> batch;
    for (std::size_t i = 0; i < pending.size() && i < net::kAudioBatchCues; ++i)
        batch.push_back(pending[i]);
    if (!batch.empty() && s.publishAudio(batch, now))
    {
        sent += batch.size();
        for (std::size_t i = 0; i < batch.size(); ++i)
            pending.pop_front();
    }
}
void pc_coop_audio_counts(std::uint64_t &a, std::uint64_t &b, std::uint64_t &c)
{
    a = sent;
    b = played;
    c = dropped;
}

int pc_coop_audio_backend_state() {
#if PIKI_USE_JAUDIO
    return 128 | (Jac_PauseCheck()?1:0) | (Jac_DemoCheck()?2:0);
#else
    return 0;
#endif
}
