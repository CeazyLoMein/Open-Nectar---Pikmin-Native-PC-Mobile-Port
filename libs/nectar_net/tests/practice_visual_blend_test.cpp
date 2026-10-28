#include "nectar_net/practice_visual_blend.h"
#include <cmath>
#include <cstdio>
#include <limits>
using namespace nectar::net;
int main(){
 int errors=0;auto check=[&](bool b,const char* s){if(!b){std::printf("FAIL %s\n",s);++errors;}};
 ActorFrame a,b,out;a.frame=1;a.tick=10;b.frame=2;b.tick=16;
 CaptainState c;c.position.x=0;c.faceDirection=3.10f;c.player=0;a.captains.emplace(11,c);c.position.x=100;c.faceDirection=-3.10f;b.captains.emplace(11,c);
 PikminState p;p.position.x=0;p.action=4;a.pikmin.emplace(21,p);p.position.x=40;b.pikmin.emplace(21,p);
 p.position.x=9;b.pikmin.emplace(22,p);a.pikmin.emplace(23,p);
 check(blendPracticeVisualFrame(a,b,0.5f,200,out),"valid pair blends");
 check(out.captains.at(11).position.x==50 && std::fabs(out.captains.at(11).faceDirection)>3.0f,"captain moves halfway via shortest turn");
 check(out.pikmin.at(21).position.x==20 && out.pikmin.count(22)==1 && out.pikmin.count(23)==0,"Pikmin movement, births and removals");
 check(a.captains.at(11).position.x==0 && b.captains.at(11).position.x==100,"source authority unchanged");
 check(blendPracticeVisualFrame(a,b,0.5f,20,out)&&out.captains.at(11).position.x==100,"teleport snaps");
 b.pikmin.at(21).action=7;check(blendPracticeVisualFrame(a,b,0.5f,200,out)&&out.pikmin.at(21).position.x==40,"changed action snaps");
 auto untouched=out;check(!blendPracticeVisualFrame(a,b,std::numeric_limits<float>::quiet_NaN(),200,out)&&out.frame==untouched.frame&&out.pikmin.at(21).position.x==untouched.pikmin.at(21).position.x,"invalid fraction leaves output untouched");
 b.pikmin.at(21).position.x=std::numeric_limits<float>::quiet_NaN();
 check(!blendPracticeVisualFrame(a,b,0.5f,200,out)&&out.pikmin.at(21).position.x==untouched.pikmin.at(21).position.x,"invalid actor rejects entire visual output");
 b.pikmin.at(21).position.x=40;
 b.tick=9;check(!blendPracticeVisualFrame(a,b,0.5f,200,out),"stale host tick rejected");
 if(!errors)std::puts("PASS visual-only blending, identity, discontinuities and atomic refusal");
 return errors?1:0;
}
