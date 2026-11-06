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
    preview.reset();preview.activity(true,true,2000);
    truth.position={100,0,200};truth.cursor={115,5,220};
    for(int delta=-100;delta<=100;delta+=10){
        Vec3 displayed{100.0f+delta,0,200.0f-delta};
        check(preview.sample(truth,150,{3,0,-2},200,2001,shown,&displayed),"moving captain supports local aim preview");
        check(near(shown.x-displayed.x,18)&&near(shown.z-displayed.z,18),"pending aim stays attached to displayed captain, not newer unsmoothed position");
    }
    const auto kept=shown;Vec3 badPosition{std::numeric_limits<float>::quiet_NaN(),0,0};
    check(!preview.sample(truth,150,{},200,2002,shown,&badPosition)&&near(shown.x,kept.x),"invalid displayed position leaves cursor output unchanged");
    check(truth.position.x==100&&truth.cursor.x==115,"moving preview never changes authoritative state");
    for(int degrees=0;degrees<360;degrees+=30){
        const float angle=degrees*.01745329252f;
        pc_coop_cursor::Motion right{std::cos(angle),0,std::sin(angle)};
        for(float side:{-1.0f,1.0f}){
            const pc_coop_cursor::Motion offset{right.x*100*side,0,right.z*100*side};
            const pc_coop_cursor::Motion step{right.x*10*side,0,right.z*10*side};
            const auto turn=pc_coop_cursor::edgeTurn(offset,step,right,100);
            check(near(turn.drag,-side*.1f/3.2f,.0001f),"guest edge camera uses solo turn sign at every view angle");
            const float c=std::cos(turn.drag*3.2f),sn=std::sin(turn.drag*3.2f);
            check(near(offset.x+turn.delta.x,offset.x*c+offset.z*sn)
                &&near(offset.z+turn.delta.z,offset.z*c-offset.x*sn),"encoded cursor displacement includes same rotation as solo camera");
            check(near(std::hypot(offset.x+turn.delta.x,offset.z+turn.delta.z),100),"edge turning keeps final cursor at radial reach");
        }
    }
    auto inside=pc_coop_cursor::edgeTurn({10,0,10},{2,0,3},{1,0,0},100);
    check(inside.drag==0&&inside.delta.x==2&&inside.delta.z==3,"ordinary interior mouse aim stays unchanged");
    auto vertical=pc_coop_cursor::edgeTurn({0,0,100},{0,0,10},{1,0,0},100);
    check(vertical.drag==0,"vertical edge movement does not invent horizontal camera turn");
    auto invalid=pc_coop_cursor::edgeTurn({100,0,0},{10,0,0},{1,0,0},0);
    check(invalid.drag==0&&invalid.delta.x==10,"invalid reach cannot rotate camera or divide by zero");
    {
        PcCoopCursorPreview aimPreview;nectar::net::CaptainState assisted;assisted.lockedEnemy=1;
        nectar::net::Vec3 aimOut;aimPreview.activity(false,true,1000);
        check(!aimPreview.sample(assisted,0,{1,0,1},300,1000,aimOut),"local preview cannot fight host soft assist target");
        aimPreview.activity(true,true,1000);
        check(aimPreview.sample(assisted,0,{1,0,1},300,1000,aimOut),"explicit free aim retains instant local response while assistance releases");
    }
    std::printf("%d cursor projection/ownership/preview checks passed\n",checks);
}
