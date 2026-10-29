#include "netplay/pc_coop_visual_smoothing.h"
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace nectar::net;
int checks=0;
void check(bool yes,const char* why){++checks;if(!yes){std::fprintf(stderr,"FAIL %s\n",why);std::exit(1);}}
bool near(float a,float b){return std::fabs(a-b)<0.001f;}
ActorFrame frame(std::uint64_t id,float x){
    ActorFrame f;f.frame=id;f.tick=id*11;CaptainState c;c.player=0;c.position={x,0,0};c.velocity={1000,0,0};c.upperFrame=x/10;f.captains[1]=c;
    c.player=1;f.captains[2]=c;PikminState p;p.position={x,0,0};p.owner=0;p.upperFrame=x/10;f.pikmin[3]=p;return f;
}
int main(){
    PcCoopVisualSmoothing s;ActorFrame out;
    check(!s.sample(0,out),"no frame before admission");
    auto a=frame(1,0),b=frame(2,50),c=frame(3,100);
    check(s.push(a,1000)&&s.push(b,1050)&&s.push(c,1100),"monotonic frames admitted");
    check(!s.push(b,1101)&&!s.push(frame(4,101),999),"duplicate/old frame or backwards arrival refused");
    check(s.sample(1150,out)&&near(out.captains[1].position.x,75)&&near(out.pikmin[3].position.x,75),"captains and Pikmin blend between 20Hz frames");
    check(out.frame==3&&out.tick==33,"display never invents authoritative sequence or tick");
    check(near(out.captains[1].upperFrame,7.5f),"compatible animation pose interpolates");
    check(s.sample(900,out)&&near(out.captains[1].position.x,0),"startup holds first pose");
    check(s.sample(9000,out)&&near(out.captains[1].position.x,100),"long stall holds last pose without extrapolation");
    for(int fps:{30,60,120,240}){
        s.reset();
        for(int i=0;i<8;++i)check(s.push(frame(i+1,float(i*5)),1000+i*50),"frame buffer admits");
        float before=-1;
        for(int i=0;i<fps/5;++i){
            const auto now=1100+static_cast<std::uint64_t>(i*1000/fps);
            check(s.sample(now,out),"sample at personal display rate");
            check(out.captains[1].position.x>=before,"no backwards jitter at any display rate");before=out.captains[1].position.x;
        }
    }
    s.reset();s.push(a,1000);b.pikmin.erase(3);b.pikmin[4]=PikminState{};b.pikmin[4].position.x=300;b.pikmin[4].owner=1;s.push(b,1050);s.sample(1075,out);
    check(!out.pikmin.count(3)&&out.pikmin.count(4)&&near(out.pikmin[4].position.x,300)&&out.pikmin[4].owner==1,"latest births/deaths/ownership apply immediately without identity borrowing");
    s.reset();a=frame(1,0);b=frame(2,50);b.pikmin[3].owner=1;b.pikmin[3].action=9;b.pikmin[3].health=7;s.push(a,1000);s.push(b,1050);s.sample(1100,out);
    check(out.pikmin[3].owner==1&&out.pikmin[3].action==9&&out.pikmin[3].health==7,"gameplay metadata is latest truth while pose blends");
    s.reset();a=frame(1,0);b=frame(2,1000);s.push(a,1000);s.push(b,1050);s.sample(1100,out);check(near(out.captains[1].position.x,1000),"teleport does not sweep across map");
    s.reset();a=frame(1,0);b=frame(2,50);c=frame(3,1000);s.push(a,1000);s.push(b,1050);s.push(c,1100);s.sample(1100,out);check(near(out.captains[1].position.x,1000),"latest teleport overrides an older interpolation interval");
    s.reset();a=frame(1,0);b=frame(2,50);a.captains[1].faceDirection=6.2f;b.captains[1].faceDirection=0.1f;s.push(a,1000);s.push(b,1050);s.sample(1100,out);
    check(std::fabs(out.captains[1].faceDirection)<0.15f,"angle takes short path around wrap");
    s.reset();a=frame(1,0);b=frame(2,50);a.captains[1].upperFrame=29;b.captains[1].upperFrame=1;s.push(a,1000);s.push(b,1050);s.sample(1100,out);check(near(out.captains[1].upperFrame,1),"animation loop does not rewind through clip");
    s.reset();a=frame(1,0);b=frame(2,50);b.captains[1].upperAnimation=2;s.push(a,1000);s.push(b,1050);s.sample(1100,out);check(out.captains[1].upperAnimation==2&&near(out.captains[1].upperFrame,5),"clip change retains valid latest pose");
    s.reset();s.push(c,1200);s.sample(1210,out);check(near(out.captains[1].position.x,1000),"pause/revision reset stops pending motion");
    s.reset();s.push(frame(1,0),1000);s.push(frame(2,60),1060);s.push(frame(3,180),1180);s.sample(1195,out);
    check(near(out.captains[1].position.x,120),"dropped snapshot blends over real arrival interval");
    s.reset();s.push(frame(1,0),1000);s.push(frame(2,10),1000);s.sample(1075,out);
    check(near(out.captains[1].position.x,10),"same-time burst never divides by zero");
    for(int i=3;i<=20;++i)s.push(frame(i,float(i)),1000+50*i);
    s.sample(0,out);check(near(out.captains[1].position.x,13),"history evicts oldest frames at its fixed eight-frame bound");
    std::printf("%d guest presentation checks passed\n",checks);
}
