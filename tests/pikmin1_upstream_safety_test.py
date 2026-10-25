"""Compile actual small P1 methods with controlled engine dependencies.

Pass --ref <git-ref> for a negative control against an older source revision.
This does not replace a full Apple build or real campaign tests.
"""
from pathlib import Path
import argparse
import subprocess

ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument('output', type=Path)
p.add_argument('--ref')
args = p.parse_args()
def source(path):
    path = 'games/pikmin1/' + path
    if args.ref:
        return subprocess.check_output(['git', 'show', args.ref + ':' + path], cwd=ROOT).decode('utf-8')
    return (ROOT/path).read_text(encoding='utf-8')
def method(path, signature):
    text = source(path)
    a = text.index(signature)
    b = text.index('{', a)
    i, depth = b+1, 1
    while depth:
        depth += (text[i] == '{') - (text[i] == '}')
        i += 1
    return text[a:i]

cpp = r'''#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using f32=float;
int failures=0;
void check(bool ok,const char* why){if(!ok){std::printf("FAIL: %s\n",why);++failures;}}
namespace rect {
using GLint=int;using GLsizei=int;float sx=1,sy=1;bool sHudWide=false;
int hud_virtual_height(){return 480;}
void gx_rect_params(float&a,float&b,float&c,float&d){a=sx;b=sy;c=.25f;d=.25f;}
'''
cpp += method('pc_port/gl/pc_gfx.cpp', 'static void map_gx_rect(')
cpp += r'''
void test(){int bad=0,cases=0;
 for(auto size:{std::pair<int,int>{1426,1002},{1902,1338},{2853,2007},{1920,1200},{2034,1398}}){
  sx=float(size.first)/640;sy=float(size.second)/480;
  for(int x=0;x<600;++x)for(int w=1;w<32;++w){
   int ax,ay,aw,ah,bx,by,bw,bh;map_gx_rect(float(x),0,float(w),480,ax,ay,aw,ah);
   map_gx_rect(float(x+w),0,1,480,bx,by,bw,bh);bad+=(ax+aw!=bx);++cases;}
  for(int y=0;y<440;++y)for(int h=1;h<32;++h){
   int ax,ay,aw,ah,bx,by,bw,bh;map_gx_rect(0,float(y),640,float(h),ax,ay,aw,ah);
   map_gx_rect(0,float(y+h),640,1,bx,by,bw,bh);bad+=(by+bh!=ay);++cases;}
 }
 std::printf("Rectangle shared-edge cases=%d mismatches=%d\n",cases,bad);check(bad==0,"adjacent rectangles meet");
}}
namespace onion {
enum{OBJTYPE_Goal=1};struct Creature{int mObjType=0;};
struct GoalAI{enum{GOAL_BootInit=1,GOAL_BootEmit=2};};
struct GoalItem:Creature{struct{void*mStateMachine=nullptr;}mSAICtx;int mOnionColour=0,state=0,emits=0;};
struct StateMachine{int getCurrID(GoalItem*g){return g->state;}void start(GoalItem*g,int state){g->state=state;++g->emits;}} machine;
#define C_SAI(g) (&machine)
struct PlayerState{bool boot=false;bool hasBootContainer(int){return boot;}} player;
PlayerState*playerState=&player;
struct DemoEventMgr{void finishOnionBootAfterSkip(Creature*);};
'''
# Older revisions have no method: retain this negative-control boundary explicitly.
try:
    cpp += method('src/plugPikiKando/demoEvent.cpp', 'void DemoEventMgr::finishOnionBootAfterSkip(')
except ValueError:
    cpp += 'void DemoEventMgr::finishOnionBootAfterSkip(Creature*){}\n'
cpp += r'''
void test(){DemoEventMgr mgr;Creature other;GoalItem g;g.mObjType=OBJTYPE_Goal;g.state=GoalAI::GOAL_BootInit;
 mgr.finishOnionBootAfterSkip(nullptr);mgr.finishOnionBootAfterSkip(&other);mgr.finishOnionBootAfterSkip(&g);
 check(g.emits==0,"no machine, no seed");g.mSAICtx.mStateMachine=&machine;mgr.finishOnionBootAfterSkip(&g);
 check(g.emits==0,"undiscovered onion remains unchanged");player.boot=true;mgr.finishOnionBootAfterSkip(&g);
 check(g.emits==1&&g.state==GoalAI::GOAL_BootEmit,"skipping boot emits first seed");
 mgr.finishOnionBootAfterSkip(&g);check(g.emits==1,"repeat skip does not duplicate seed");
 g.state=3;mgr.finishOnionBootAfterSkip(&g);check(g.emits==1,"normal completed boot unchanged");
}}
namespace damage {
struct Navi{bool hurt=false;bool orimaDamaged(){return hurt;}} captain;
struct Manager{Navi*value=nullptr;Navi*getNavi(int){return value;}} manager;
Manager*naviMgr=nullptr;struct{bool mIsUIOverlayActive=false;}gameflow;
struct Sys{float getFrameTime(){return .25f;}}sys;Sys*gsys=&sys;
namespace zen{int gHudNaviIndex=0;struct DamageEffect{float mDamageAlpha=0;bool update();};}
'''
cpp += method('src/plugPikiYamashita/damageEffect.cpp', 'bool zen::DamageEffect::update()')
cpp += r'''
void test(){zen::DamageEffect fx;fx.update();check(fx.mDamageAlpha==0,"no captain manager is safe");
 naviMgr=&manager;fx.update();check(fx.mDamageAlpha==0,"missing HUD captain is safe");
 manager.value=&captain;captain.hurt=true;fx.update();check(fx.mDamageAlpha==1.75f,"damage flash retained");
 gameflow.mIsUIOverlayActive=true;fx.update();check(fx.mDamageAlpha==1.75f,"overlay retains damage state");}}
namespace slots {
struct CollPart{int children=0;CollPart*getChildAt(int n){check(n>=0&&n<2,"slot index in range");++children;return this;}} fixtureMouth;
struct Creature{int hits=0;template<class T>void stimulate(const T&){++hits;}} target;
struct CollInfo{CollPart*value=&fixtureMouth;CollPart*getSphere(int){return value;}} info;
struct Actor{CollInfo*mCollInfo=&info;Creature*value=&target;Creature*getTargetCreature(){return value;}}actor;
struct InteractSwallow{InteractSwallow(Actor*,CollPart*,int){}};
struct NsMathI{static int getRand(int){return 0;}};
struct SnakeAi{Actor*mSnake=&actor;int mMaxSlotCount=2,mOccupiedSlotCount=0;bool used[2]={false,false};
 bool getMouthCollPart(int n){return used[n];}void setMouthCollPart(int n){used[n]=true;}void pikiStickMouth();};
'''
cpp += method('src/plugPikiNishimura/SnakeAi.cpp', 'void SnakeAi::pikiStickMouth()').replace("'slot'", '0')
cpp += r'''
void test(){SnakeAi ai;ai.used[0]=ai.used[1]=true;ai.pikiStickMouth();check(target.hits==0,"full mouth refuses target");
 ai.used[0]=false;ai.pikiStickMouth();check(target.hits==1&&ai.mOccupiedSlotCount==1,"available slot still works");
 SnakeAi missing;info.value=nullptr;missing.pikiStickMouth();check(missing.mOccupiedSlotCount==0,"missing mouth consumes no slot");
 info.value=&fixtureMouth;actor.value=nullptr;missing.pikiStickMouth();check(missing.mOccupiedSlotCount==0,"missing target consumes no slot");}}
namespace retry {
int tickScale=1;
#define PC_TICKS30 tickScale
// Actual decision prefix includes invalid/dead-pellet checks and retry state changes.
struct Vector3f{float x=0,y=0,z=0;Vector3f()=default;Vector3f(float a,float b,float c):x(a),y(b),z(c){}
 Vector3f operator-(const Vector3f&o)const{return{x-o.x,y-o.y,z-o.z};}
 float normalise(){float len=std::sqrt(x*x+y*y+z*z);if(len){x/=len;y/=len;z/=len;}return len;}};
float speedy_sqrtf(float f){return std::sqrt(f);}
struct PikiEmotion{enum{Sad=1};};struct Piki{struct{Vector3f t;}mSRT;int mEmotion=0;};
struct Pellet{bool alive=true;int next=1,queries=0;bool isAlive(){return alive;}
 Vector3f getSlotGlobalPos(int,float){return{50,0,0};}float getCentreSize(){return 0;}
 int getNearestFreeSlotIndex(Vector3f){++queries;return next;}} fixturePellet;
struct Handle{Pellet*value=&fixturePellet;Pellet*getPtr(){return value;}};
struct ActTransport{Handle mPellet;Piki piki;Piki*mPiki=&piki;int mSlotIndex=0,mStateProgress=0,mState=99;
 float mWaitTimer=0;enum{STATE_Go=1};bool gotoLiftPos();};
'''
text = method('src/plugPikiKando/aiTransport.cpp', 'bool ActTransport::gotoLiftPos()')
text = text[:text.index('\n\tif (horizontalDist > 6.0f)')]
cpp += text + '\n (void)verticalDist;(void)distToCentre;return true;\n}\n'
cpp += r'''
void test(){for(int hz:{30,60,120}){tickScale=hz/30;fixturePellet=Pellet{};ActTransport a;
 for(int n=0;n<2*hz-1;++n)check(a.gotoLiftPos(),"wait before slot retry");
 check(fixturePellet.queries==0,"no premature high-FPS retry");check(a.gotoLiftPos(),"retry to next slot succeeds");
 check(fixturePellet.queries==1&&a.mStateProgress==0&&a.mState==ActTransport::STATE_Go,"retry occurs at two seconds");}
 ActTransport invalid;invalid.mSlotIndex=-1;check(!invalid.gotoLiftPos(),"invalid slot refused");
 invalid.mSlotIndex=0;invalid.mPellet.value=nullptr;check(!invalid.gotoLiftPos(),"missing pellet refused");
 invalid.mPellet.value=&fixturePellet;fixturePellet.alive=false;check(!invalid.gotoLiftPos(),"dead pellet refused");fixturePellet.alive=true;
 for(int next:{-1,0}){ActTransport a;a.mStateProgress=2*120-1;fixturePellet.next=next;
 check(!a.gotoLiftPos()&&a.piki.mEmotion==PikiEmotion::Sad,"full or unchanged slot refuses retry");}}}
int main(){rect::test();onion::test();damage::test();slots::test();retry::test();
 if(!failures)std::puts("PASS actual P1 rectangle, onion skip, damage, mouth slot and carrying retry methods");return failures?1:0;}
'''
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(cpp,encoding='utf-8')
print('Generated actual-method upstream regression fixture:',args.output)
