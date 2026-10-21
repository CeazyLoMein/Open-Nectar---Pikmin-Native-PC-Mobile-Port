#include "pc_p2_audio_audit.h"
#include <atomic>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>

bool pc_host_alloc_active();
void pc_host_alloc_set(bool active);
namespace p2_audio_audit {
namespace {
constexpr unsigned kSlots = 8, kEvents = 5;
constexpr std::uint32_t kDuration = 10 * 60 * 1000;
struct Slot {
    std::atomic<unsigned> events[kEvents]{};
    std::atomic<unsigned> lastId{0}, observations{0}, silent{0};
    std::atomic<unsigned> lastDistance{0}, lastGain{0}, listener{0}, categoryMuted{0};
};
Slot slots[kSlots];
std::atomic<unsigned> banks[static_cast<unsigned>(BankResult::Count)]{};
std::atomic<unsigned> sources[32]{};
std::atomic<bool> finished{false};
const char* const names[kSlots] = {"captain", "system", "pikmin", "item", "environment", "enemy", "wind-402d", "ship-3043"};
bool enabled()
{
    if constexpr (kAutomaticallyEnabled) {
        return !finished.load(std::memory_order_relaxed);
    } else {
        static const bool optIn = std::getenv("PIKMIN_AUDIO_AUDIT") != nullptr;
        return optIn && !finished.load(std::memory_order_relaxed);
    }
}
void increment(unsigned slot, std::uint32_t id, Event kind)
{
    slots[slot].lastId.store(id, std::memory_order_relaxed);
    slots[slot].events[static_cast<unsigned>(kind)].fetch_add(1, std::memory_order_relaxed);
}
void observe(unsigned slot, std::uint32_t id, float dist, float gain, unsigned listener)
{
    auto& s=slots[slot];
    s.lastId.store(id, std::memory_order_relaxed);
    s.observations.fetch_add(1, std::memory_order_relaxed);
    if (!(gain > 0.0f)) s.silent.fetch_add(1, std::memory_order_relaxed);
    s.lastDistance.store(std::isfinite(dist) ? static_cast<unsigned>(std::clamp(dist,0.0f,1000000.0f)) : 1000001u, std::memory_order_relaxed);
    s.lastGain.store(std::isfinite(gain) ? static_cast<unsigned>(std::clamp(gain,0.0f,1.0f)*1000.0f) : 1001u, std::memory_order_relaxed);
    s.listener.store(listener, std::memory_order_relaxed);
}
int special(std::uint32_t id)
{
    if (id == 0x402d || id == 0x402e) return 6;
    if (id == 0x3043) return 7;
    return -1;
}
}
void event(std::uint32_t id, Event kind)
{
    const unsigned cat=(id>>12)&255u;
    if (!enabled() || cat>=6 || static_cast<unsigned>(kind)>=kEvents) return;
    increment(cat,id,kind);
    const int extra=special(id);
    if(extra>=0) increment(static_cast<unsigned>(extra),id,kind);
}
void distance(std::uint32_t id,float dist,float gain,unsigned listener,bool categoryMuted)
{
    const unsigned cat=(id>>12)&255u;
    if(!enabled() || cat>=6) return;
    observe(cat,id,dist,gain,listener);
    if(categoryMuted) slots[cat].categoryMuted.fetch_add(1,std::memory_order_relaxed);
    const int extra=special(id);
    if(extra>=0) observe(static_cast<unsigned>(extra),id,dist,gain,listener);
}
void bank(BankResult result)
{
    const unsigned index=static_cast<unsigned>(result);
    if(enabled() && index<static_cast<unsigned>(BankResult::Count)) banks[index].fetch_add(1,std::memory_order_relaxed);
}
void source(unsigned format)
{
    if(enabled()) sources[std::min(format,31u)].fetch_add(1,std::memory_order_relaxed);
}
void render(const std::int16_t* samples,std::size_t frames,unsigned voices,std::uint32_t now)
{
    if(!enabled()) return;
    // This function has one caller on the JAS audio queue thread. No game
    // callback writes files; cross-thread observations above use relaxed atomics.
    static bool started=false, failed=false;
    static std::uint32_t began=0, previous=0;
    static FILE* log=nullptr;
    if(failed) return;
    if(!started){started=true;began=previous=now;}
    const std::uint32_t elapsed=now-began;
    if(now-previous<5000 && elapsed<kDuration) return;
    const bool old=pc_host_alloc_active();pc_host_alloc_set(true);
    if(!log){
        // Keep the previous launch for a crash/relaunch comparison. At most
        // two files; no PCM, game content, save data or personal identifiers.
        std::remove("p2-audio-previous.txt");
        std::rename("p2-audio-report.txt","p2-audio-previous.txt");
        log=std::fopen("p2-audio-report.txt","w");
        if(log) std::fprintf(log,"P2 audio audit v1; cumulative counters; first 10 minutes only\nrequest/cull/gate apply to creature path; submitted/started to all SE\n");
        else failed=true;
    }
    if(log){
        int peak=0;
        if(samples) for(std::size_t i=0;i<frames*2;++i) peak=std::max(peak,std::abs(static_cast<int>(samples[i])));
        std::fprintf(log,"seconds=%u voices=%u output_peak=%d\n",elapsed/1000,voices,peak);
        for(unsigned i=0;i<kSlots;++i){
            auto& s=slots[i];
            std::fprintf(log,"%s id=%04x request=%u cull=%u gate=%u submitted=%u started=%u distance_checks=%u zero_gain=%u last_dist=%u last_gain_permil=%u listener=%u category_muted_checks=%u\n",names[i],s.lastId.load(),s.events[0].load(),s.events[1].load(),s.events[2].load(),s.events[3].load(),s.events[4].load(),s.observations.load(),s.silent.load(),s.lastDistance.load(),s.lastGain.load(),s.listener.load(),s.categoryMuted.load());
        }
        std::fprintf(log,"bank results [played,bank,instrument,keyregion,wavebank,wave,info,data,channel,play_failed]:");
        for(auto& count:banks)std::fprintf(log," %u",count.load());
        std::fprintf(log,"\nsource_frames:");
        for(unsigned i=0;i<32;++i){const unsigned count=sources[i].load();if(count)std::fprintf(log," %u=%u",i,count);}
        std::fprintf(log,"\n");std::fflush(log);
        if(elapsed>=kDuration){std::fclose(log);log=nullptr;finished.store(true);}
    }
    previous=now;pc_host_alloc_set(old);
}
}
