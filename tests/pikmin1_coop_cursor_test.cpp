#include "netplay/pc_coop_cursor_motion.h"
#include "netplay/pc_coop_cursor_preview.h"
#include "netplay/pc_coop_practice_input.h"
#include <cstdio>
#include <cstdlib>
#include <limits>
using namespace nectar::net;
int checks=0;
void check(bool yes,const char* why){++checks;if(!yes){std::fprintf(stderr,"FAIL %s\n",why);std::exit(1);}}
bool near(float a,float b,float epsilon=.033f){return std::fabs(a-b)<epsilon;}
int main(){
    for(int degrees=0;degrees<360;degrees+=15)for(float handedness:{-1.0f,1.0f}) {
        const float angle=static_cast<float>(degrees)*.01745329252f;
        const pc_coop_cursor::Motion right{std::cos(angle)*3,7,std::sin(angle)*3};
        const pc_coop_cursor::Motion back{-std::sin(angle)*handedness*2,-5,std::cos(angle)*handedness*2};
        for(const auto& delta:{Vec3{8,0,0},Vec3{-8,0,0},Vec3{0,0,12},Vec3{0,0,-12},Vec3{3.3f,0,-2.7f}}) {
            const auto solo=pc_coop_cursor::project(delta.x,delta.z,right,back);
            const auto online=pc_coop_cursor::decode(pc_coop_cursor::encode(solo.x),pc_coop_cursor::encode(solo.z));
            check(near(solo.x,online.x)&&near(solo.z,online.z),"online uses exact solo camera basis including reflected and tilted axes");
            const float dx=delta.x*.5f,dz=delta.z*.5f;
            check(near(solo.x,std::cos(angle)*dx+std::sin(angle)*handedness*dz,.001f)
               &&near(solo.z,std::sin(angle)*dx-std::cos(angle)*handedness*dz,.001f),"right/left and down/up preserve original solo projection signs and sensitivity");
        }
    }
    check(pc_coop_cursor::encode(std::numeric_limits<float>::quiet_NaN())==0,"invalid raw delta cannot enter integer conversion");
    check(pc_coop_cursor::encode(100000)==32767&&pc_coop_cursor::encode(-100000)==-32767,"wire delta is bounded");
    for(int actor:{0,1})for(int keyboard:{0,1})for(bool remote:{false,true})for(bool deterministic:{false,true})
        check(pc_coop_cursor::localMouse(deterministic,remote,actor,keyboard)==(!remote&&!deterministic&&actor==keyboard),"only actual local keyboard owner may read PC absolute cursor/gyro/camera state");
    CaptainState truth;truth.player=1;truth.position={0,0,0};truth.cursor={10,5,20};truth.health=75;
    PcCoopCursorPreview preview;Vec3 shown;
    preview.activity(true,true,1000);
    check(preview.sample(truth,100,{6,0,-3},200,1000,shown)&&near(shown.x,16)&&near(shown.z,17),"own free-aim marker responds before input send or actor round trip");
    NetInputFrame f;f.tick=110;f.flags=16|32;f.cursorDx=96;f.cursorDy=-48;
    preview.published(f,1005);preview.published(f,1006);
    check(preview.sample(truth,109,{},200,1010,shown)&&near(shown.x,16)&&near(shown.z,17),"publication does not double predicted motion; duplicate tick ignored");
    truth.cursor={16,5,17};
    check(preview.sample(truth,110,{},200,1040,shown)&&near(shown.x,16)&&near(shown.z,17),"complete host tick acknowledges motion without applying it twice");
    check(truth.health==75&&truth.position.x==0&&truth.cursor.x==16,"preview does not write host actor health/position/cursor");
    preview.activity(true,true,1041);
    check(preview.sample(truth,110,{-2,0,1},200,1041,shown)&&near(shown.x,14)&&near(shown.z,18),"a new unsent drag stacks on acknowledged truth once");
    check(preview.sample(truth,110,{5000,0,5000},100,1042,shown)&&std::hypot(shown.x,shown.z)<=100.001f,"visual prediction stays inside actual cursor reach");
    const auto previous=shown;
    check(!preview.sample(truth,110,{std::numeric_limits<float>::quiet_NaN(),0,0},100,1043,shown)&&shown.x==previous.x,"invalid preview input cannot corrupt presented cursor");
    preview.activity(false,false,1044);
    check(!preview.sample(truth,110,{},200,1300,shown),"release returns to normal presentation after bounded settling interval");
    preview.activity(true,true,1400);f.tick=120;preview.published(f,1400);preview.activity(false,false,1401);
    check(!preview.sample(truth,110,{},200,1801,shown),"old unacknowledged drag expires after interruption");
    preview.activity(true,true,1900);preview.reset();
    check(!preview.sample(truth,110,{8,0,8},200,1901,shown),"pause/phase reset drops all marker prediction");
    PcCoopPracticeInput input;input.observe(10,1000);f.tick=0;f.flags=16|32;f.cursorDx=32;f.cursorDy=-16;
    input.sample(f,1000);input.sample(f,1001);
    auto unsent=input.pendingCursorWorld(1001);
    check(near(unsent.x,4)&&near(unsent.z,-2),"preview reads exact quantized unsent accumulator used by network bundle");
    auto bundle=input.bundle(1010,0);input.published(bundle,1010);
    check(input.pendingCursorWorld(1010).x==0&&input.pendingCursorWorld(1010).z==0,"publishing clears unsent preview accumulator");
    std::printf("%d cursor projection/ownership/preview checks passed\n",checks);
}
