#include "../../../games/pikmin1/pc_port/netplay/pc_coop_practice_input.h"
#include <cstdio>
#include <limits>
using namespace nectar::net;
int failures=0;
void check(bool ok,const char* msg){if(!ok){++failures;std::printf("FAIL %s\n",msg);}}
int main(){
    PcCoopPracticeInput clock;
    NetInputFrame physical;physical.held=0x100;physical.flags=0x0c;physical.cursorDx=90;physical.controlYaw=50000;
    clock.sample(physical,1000);check(clock.bundle(1000,0).empty(),"no commands before actual host clock");
    clock.observe(100,1000);clock.observe(106,1050); // actual host120, irrespective of guest60
    auto first=clock.bundle(1050,12);
    check(!first.empty()&&first[0].tick==110,"input targets measured host120, with network lead");
    check(first.size()==6&&first[0].controlYaw==50000&&first[0].flags==12&&first[0].cursorDx==90,"camera and accumulated action survive bundle");
    for(std::size_t i=1;i<first.size();++i)check((first[i].flags&4)==0&&first[i].cursorDx==0,"new edge issued once");
    clock.published(first,1050);
    check(clock.bundle(1060,12).empty(),"does not transmit at phone render rate");
    physical.flags=8;physical.cursorDx=0;clock.sample(physical,1084);clock.observe(110,1084);
    const auto second=clock.bundle(1084,12);
    bool repaired=false;for(const auto& f:second)if(f.tick==110&&f.flags==12&&f.cursorDx==90)repaired=true;
    check(repaired,"next redundant bundle preserves old edge if first datagram lost");
    InputPolicy policy;policy.continuousFlags=8;InputReceiver receiver(policy);
    receiver.receive(second,108);int edges=0;
    for(std::uint64_t tick=108;tick<121;++tick){InputHealth health;const auto applied=receiver.consume(tick,health);if(applied.flags&4)++edges;if(tick==114)check((applied.flags&8)!=0,"swarm survives short gap");}
    check(edges==1,"receiver never repeats recovered charge");
    check(clock.bundle(2200,12).empty(),"stale host clock neutralizes publication");
    clock.reset();check(clock.bundle(2200,0).empty(),"pause revision discards old actions and clock");
    // Simulate a host at 125 Hz and a guest sending every 33ms, with
    // snapshots and inputs each spending one-way delay on the wire.
    for(int lag:{6,15,30,50}) {
        struct Msg {int arrive;std::vector<NetInputFrame> frames;};
        struct Snapshot {int arrive;std::uint64_t tick;};
        PcCoopPracticeInput g;InputReceiver h;NetInputFrame moving;moving.stickX=80;
        std::vector<Msg> messages;std::vector<Snapshot> snapshots;
        std::uint64_t tick=0;int neutral=0,rejected=0;
        for(int ms=0;ms<10000;++ms) {
            if(ms%8==0) {
                ++tick;if(ms%48==0)snapshots.push_back({ms+lag,tick});
                if(ms>1000) {InputHealth health;const auto input=h.consume(tick,health);if(!input.stickX)++neutral;}
            }
            for(auto it=snapshots.begin();it!=snapshots.end();) {
                if(it->arrive<=ms){g.observe(it->tick,ms);it=snapshots.erase(it);}else ++it;
            }
            g.sample(moving,static_cast<std::uint64_t>(ms));
            if(ms%33==0) {const auto frames=g.bundle(ms,lag*2);if(!frames.empty()){messages.push_back({ms+lag,frames});g.published(frames,ms);}}
            for(auto it=messages.begin();it!=messages.end();) {
                if(it->arrive<=ms){if(it->frames.front().tick>=tick)h.receive(it->frames,tick);else ++rejected;it=messages.erase(it);}else ++it;
            }
        }
        check(neutral<20 && rejected<10,"held movement survives two-way snapshot/input delay at 125Hz");
    }
    for(unsigned fps:{30u,60u,120u}){
        clock.reset();clock.observe(100,1000);clock.observe(100+fps/2,1500);clock.sample(physical,1500);
        const auto b=clock.bundle(1500,0);
        const auto lead=b[0].tick-(100+fps/2);
        check(lead==2,"30/60/120 host rate inferred without changing display settings");
    }
    // A tap made during a prolonged unsent queue must not fire after recovery.
    PcCoopPracticeInput delayed;NetInputFrame tap;tap.held=1;tap.flags=4;tap.cursorDx=50;
    delayed.observe(100,1000);delayed.sample(tap,1000);
    NetInputFrame released;delayed.sample(released,1010);delayed.observe(150,1500);
    auto recovered=delayed.bundle(1500,0);
    check(!recovered.empty() && recovered[0].held==0 && recovered[0].flags==0 && recovered[0].cursorDx==0,
          "old tap and camera drag expire before a stalled link recovers");
    delayed.sample(tap,1510);auto fresh=delayed.bundle(1510,0);
    check(!fresh.empty() && fresh[0].held==1 && fresh[0].flags==4 && fresh[0].cursorDx==50,
          "fresh tap remains usable after stale actions expire");
    PcCoopPracticeInput stagger;stagger.observe(100,1000);
    NetInputFrame a;a.flags=1;stagger.sample(a,1000);
    NetInputFrame b;b.flags=2;stagger.sample(b,1290);
    stagger.observe(140,1310);auto staggered=stagger.bundle(1310,0);
    check(!staggered.empty() && (staggered[0].flags&1)==0 && (staggered[0].flags&2)!=0,
          "expiring an older action does not discard a newer different action");
    clock.reset();clock.observe(std::numeric_limits<std::uint64_t>::max()-10,1);
    check(clock.bundle(1,0).empty(),"tick overflow fails closed");
    std::puts(failures?"PRACTICE INPUT FAIL":"PRACTICE INPUT PASS");return failures?1:0;
}
