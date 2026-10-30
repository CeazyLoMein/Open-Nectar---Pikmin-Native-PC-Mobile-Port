"""Run actual guest whistle presentation and captain input consumers with controlled engine seams."""
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
def body(text,signature):
 at=text.index(signature);start=text.index('{',at);end=start+1;depth=1
 while depth:
  if text[end]=='{':depth+=1
  elif text[end]=='}':depth-=1
  end+=1
 return text[at:end]
visual=(root/'games/pikmin1/pc_port/netplay/pc_coop_captain_visuals.cpp').read_text(encoding='utf-8')
nav=(root/'games/pikmin1/src/plugPikiKando/navi.cpp').read_text(encoding='utf-8')
settings=(root/'games/pikmin1/pc_port/settings/pc_settings.cpp').read_text(encoding='utf-8')
runtime=(root/'games/pikmin1/pc_port/netplay/pc_coop_practice_runtime.cpp').read_text(encoding='utf-8')
parts=[body(visual,s) for s in ['void Navi::pcCoopWhistleCapture(', 'bool Navi::pcCoopWhistleRadius(', 'void Navi::pcCoopWhistleEffects(']]
parts += [body(nav,s) for s in ['void Navi::renderCircle(', 'static bool pcTouchAim(', 'void Navi::pcUpdateRecallAll(']]
parts += [body(runtime,s) for s in ['bool pc_coop_practice_cursor_delta(', 'float pc_coop_practice_remote_speed(']]
parts += [body(settings,s) for s in ['int pc_settings_get_recall_all(', 'float pc_settings_get_piki_speed_scale(', 'const char* disabledReason(']]
particles=(root/'games/pikmin1/src/plugPikiYamashita/particleManager.cpp').read_text(encoding='utf-8')
parts += [body(particles,'void zen::particleManager::updateCoopWhistles('),body(runtime,'bool pc_coop_practice_guest_effects_running(')]
assert 'ptclGen->mPcCoopWhistleVisual=false' in particles
pg=(root/'games/pikmin1/src/plugPikiYamashita/particleGenerator.cpp').read_text(encoding='utf-8')
assert 'if (!(mPcCoopWhistleVisual && pc_coop_practice_guest_effects_running())) return false' in pg
fx=(root/'games/pikmin1/src/plugPikiYamashita/effectMgr.cpp').read_text(encoding='utf-8')
assert 'gen->mPcCoopWhistleVisual=effID==EFF_Navi_Whistle1 || effID==EFF_Navi_Whistle2' in fx
assert '|| effID==EFF_Navi_Whistle3 || effID==EFF_Navi_WhistleCursor' in fx
render=(root/'games/pikmin1/src/plugPikiColin/newPikiGame.cpp').read_text(encoding='utf-8')
assert 'else if (isDVDNormal && gamecore->mRenderPass==0 && pc_coop_practice_guest_effects_running())' in render
assert 'effectMgr->updateCoopWhistles();' in render
# Keep the actual input bridge and cursor application seams in this gate too.
assert 'f.flags|=PcCoopPracticeInput::AimHeld' in runtime
assert 'pc_window_get_mouse_cursor_delta_x(),dy=pc_window_get_mouse_cursor_delta_y()' in runtime
assert 'f.naviSpeedPct=' in runtime and 'pc_touch_take_recall_request() || recall' in runtime
assert 'pc_coop_practice_remote_speed(mNaviID)' in nav
assert 'pc_coop_practice_control_yaw(mNaviID,&aimSin,&aimCos)' in nav
assert '!remoteCursor) pc_window_clear_mouse_cursor_delta()' in nav
assert 'pc_practice_may_whistle(pc_coop_practice_active(),mNaviID,piki->mPlayerId)' in nav
code=r'''
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <utility>
#include "nectar_net/replication.h"
#include "nectar_net/input.h"
#include "netplay/pc_coop_practice_input.h"
#include "netplay/pc_practice_squad_policy.h"
#define PIKI_PC_PORT 1
#define PIKI_PC_TOUCH 1
#define NECTAR_COOP_WORLD 1
using f32=float;
constexpr float TAU=6.28318530718f;
struct Vector3f{float x=0,y=0,z=0;Vector3f()=default;Vector3f(float a,float b,float c):x(a),y(b),z(c){}Vector3f operator+(const Vector3f&b)const{return {x+b.x,y+b.y,z+b.z};}};
struct Graphics{};
struct Map{float getMinY(float,float,bool){return 5;}}map;Map*mapMgr=&map;
bool guest=true,validGuest=true,host=false,heldAim=false,keyboardRecall=false,touchRecall=false,enabled=true;
int localPlayer=1;nectar::net::NetInputFrame remote;
bool pc_coop_world_has_guest(){return guest;}
bool pc_coop_world_guest_active(){return guest&&validGuest;}
bool pc_coop_practice_remote_input(int p){return host&&p==1;}
int pc_coop_practice_local_player(){return localPlayer;}
unsigned char pc_coop_practice_ext(int){return remote.flags;}
bool pc_touch_aim_active(){return heldAim;}
bool det=false,hard=false,speedrun=false,coop=true,vsMode=false,practice=true;
bool pc_netplay_deterministic(){return det;}
bool pc_coop_practice_active(){return practice;}
bool pc_hardmode_active(){return hard;}bool pc_speedrun_active(){return speedrun;}
bool pc_coop_active(){return coop;}bool pc_vs_active(){return vsMode;}
struct Config{int recallAll=1,pikiSpeedPct=100;}sConfig;
enum{SRC_MAIN,SRC_ADV,SRC_RECENTER,SRC_GFX,SRC_MODS,SRC_DATA,ROW_RESOLUTION=100,PC_WINDOW_FULLSCREEN_BORDERLESS=2,PC_CONTROL_CLASSIC=0};
struct GroupRow{int src,idx;};bool hardLocked(const GroupRow&){return false;}
struct Pending{int displayMode=0,controlMode=0;bool gyroEnabled=false,colourGrading=false,lockOn=false;}sPending;
bool pc_gyro_available(){return false;}bool online_guest(){return false;}
bool pc_window_take_recall_press(){return std::exchange(keyboardRecall,false);}
bool pc_touch_take_recall_request(){return std::exchange(touchRecall,false);}
int pc_settings_get_recall_all();
struct Movie{bool mIsActive=false;}movie;
struct Player{bool ended=false;bool inDayEnd(){return ended;}}player;Player*playerState=&player;
struct Gameflow{Movie*mMoviePlayer=&movie;}gameflow;
struct EffectParm{explicit EffectParm(const Vector3f&) {}};
namespace KandoEffect{enum{NaviWhistle0=1,NaviWhistle1=2,NaviFue0=7,NaviFue1=8};}
int casts[9]={},kills[9]={};
struct UtEffectMgr{static void cast(int id,const EffectParm&){++casts[id];}void kill(int id){++kills[id];}}effects;
UtEffectMgr*utEffectMgr=&effects;
enum{NAVISTATE_Gather=2};
struct NaviGatherState{bool mWhistleEffectsStopped=false;}gatherState;
struct Machine{int id=0;int getCurrID(void*){return id;}}machine;
struct Navi{
 int mNaviID=0;Machine*mStateMachine=&machine;
 struct{Vector3f t;}mSRT;
 struct{float mWhistleExpandTime=.5f,mWhistleMinRadius=20,mWhistleMaxRadius=180;}parms;
 float mWhistleTimer=0,mWhistleRadiusFrac=0,mWhistleCircleRadius=0;int mWhistleCircleMode=0;
 Vector3f mCursorWorldPos,mWhistleFxPosArr[32];
 bool mPcCoopWhistleActive=false,mPcCoopWhistleShown=false;float mPcCoopWhistleRadius=0;
 NaviGatherState*getCurrState(){return &gatherState;}
 void pcCoopWhistleCapture(nectar::net::CaptainState&);
 bool pcCoopWhistleRadius(float&)const;void pcCoopWhistleEffects();void renderCircle(Graphics&);
 int recalls=0;void callPikis(float,bool all){if(all)++recalls;}void pcUpdateRecallAll();
};
#define C_NAVI_PARM(n,p) ((n)->parms.p)
#define NAVI_PARM(p) parms.p
#define NAVI_WHISTLE_MAX_RADIUS(n) ((n)->parms.mWhistleMaxRadius)
#if defined(_MSC_VER)
#pragma warning(push)
#pragma warning(disable:4100)
#endif
#if defined(__clang__) || defined(__GNUC__)
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunused-parameter"
#endif
namespace nectar::net{enum class CoopRole{Host,Guest};}
namespace net=nectar::net;
bool owner=true,loaded=true,stopped=false,away=false,sessionRunning=true;
net::CoopRole role=net::CoopRole::Guest;
struct Session{bool canIssueCommands(){return sessionRunning;}}fakeSession;
Session*session(){return &fakeSession;}
bool pc_coop_practice_guest_effects_running();
struct System{float frame=.5f;float getFrameTime(){return frame;}}systemMock;System*gsys=&systemMock;
namespace zen {
struct zenList{zenList*mNext=nullptr;};
struct particleGenerator:zenList{bool mPcCoopWhistleVisual=false,finished=false;int calls=0;float step=0;bool update(float dt){++calls;step=dt;return finished;}};
struct List{zenList sentinel;zenList*first=&sentinel;int merges=0;zenList*getOrigin(){return &sentinel;}zenList*getTopList(){return first;}void merge(List*){++merges;}};
struct particleManager{List mActiveGenList,mInactiveGenList,_20;float _98=30;int recycled=0;void pmPutPtclGen(zenList*){++recycled;}void updateCoopWhistles();};
}
BODIES
#if defined(_MSC_VER)
#pragma warning(pop)
#endif
#if defined(__clang__) || defined(__GNUC__)
#pragma GCC diagnostic pop
#endif
int failures=0,checks=0;
void check(bool v,const char*why){++checks;if(!v){++failures;std::printf("FAIL %s\n",why);}}
bool near(float a,float b){return std::fabs(a-b)<.001f;}
int main(){
 Navi a,b;b.mNaviID=1;Graphics gfx;nectar::net::CaptainState s;
 machine.id=NAVISTATE_Gather;a.mWhistleCircleMode=1;a.mWhistleTimer=.25f;a.pcCoopWhistleCapture(s);
 check(s.whistleActive==1&&near(s.whistleRadius,100),"actual host whistle charge captures current radius");
 gatherState.mWhistleEffectsStopped=true;a.pcCoopWhistleCapture(s);check(!s.whistleActive,"native effect-stop state does not keep guest effect alive");gatherState.mWhistleEffectsStopped=false;
 machine.id=0;a.pcCoopWhistleCapture(s);check(!s.whistleActive&&s.whistleRadius==0,"leaving whistle state publishes stop");
 a.mPcCoopWhistleActive=b.mPcCoopWhistleActive=true;a.mPcCoopWhistleRadius=80;b.mPcCoopWhistleRadius=130;
 a.parms.mWhistleMaxRadius=9999;a.mCursorWorldPos={10,0,20};b.mCursorWorldPos={300,0,400};
 a.renderCircle(gfx);b.renderCircle(gfx);
 check(casts[1]==1&&casts[2]==1&&casts[7]==1&&casts[8]==1,"both original captain whistle and ring effects start independently");
 check(near(a.mWhistleCircleRadius,80)&&near(b.mWhistleCircleRadius,130),"guest settings cannot change host-authoritative ring size");
 check(near(a.mWhistleFxPosArr[0].y,5)&&!near(a.mWhistleFxPosArr[0].x,b.mWhistleFxPosArr[0].x),"native rings use each cursor and terrain height");
 for(int i=0;i<20;++i){a.renderCircle(gfx);b.renderCircle(gfx);}
 check(casts[1]==1&&casts[2]==1&&casts[7]==1&&casts[8]==1,"rendering does not allocate effects every frame");
 a.mPcCoopWhistleActive=false;a.renderCircle(gfx);a.renderCircle(gfx);
 check(kills[1]==1&&kills[7]==1&&kills[2]==0,"release kills only that captain effects once");
 validGuest=false;b.renderCircle(gfx);check(kills[2]==1&&kills[8]==1,"invalidated guest stops its presentation effects");
 guest=false;int old=casts[1]+casts[2];a.mPcCoopWhistleActive=true;a.renderCircle(gfx);check(casts[1]+casts[2]==old,"ordinary host/solo rendering does not enter guest effect path");
 heldAim=true;host=false;check(!pcTouchAim(&a)&&pcTouchAim(&b),"guest touch aim belongs to local captain one, not hardcoded zero");
 host=true;localPlayer=0;heldAim=false;remote.flags=16|32;remote.cursorDx=24;remote.cursorDy=-12;
 check(pcTouchAim(&b)&&!pcTouchAim(&a),"desktop host uses authenticated guest aim-held state");
 float x=0,y=0;check(pc_coop_practice_cursor_delta(1,&x,&y)&&near(x,6)&&near(y,-3),"actual host consumer decodes both quarter-pixel cursor axes");
 check(!pc_coop_practice_cursor_delta(0,&x,&y),"remote cursor never replaces host controls");
 remote.flags=0;pc_coop_practice_cursor_delta(1,&x,&y);check(!pcTouchAim(&b)&&x==0&&y==0,"release clears aim without stale displacement");
 remote.naviSpeedPct=250;check(near(pc_coop_practice_remote_speed(1),2.5f),"guest captain chooses independent speed");
 remote.naviSpeedPct=100;check(near(pc_coop_practice_remote_speed(1),1)&&near(pc_coop_practice_remote_speed(0),1),"return to100 applies without inheriting host settings");
 sConfig.recallAll=0;remote.flags=64;b.pcUpdateRecallAll();check(b.recalls==1,"guest-enabled recall request does not require host local cheat toggle");
 remote.flags=0;b.pcUpdateRecallAll();check(b.recalls==1,"remote recall does not repeat without edge");
 check(pc_practice_may_whistle(true,1,1)&&!pc_practice_may_whistle(true,1,0),"recall follows existing host squad ownership, cannot take partner workers");
 keyboardRecall=true;sConfig.recallAll=1;a.pcUpdateRecallAll();check(a.recalls==1,"host own Recall All still works");
 practice=true;localPlayer=0;sConfig.pikiSpeedPct=200;
 check(near(pc_settings_get_piki_speed_scale(),2)&&!disabledReason({SRC_MODS,43}),"host may set shared Pikmin walking speed in practice");
 localPlayer=1;check(disabledReason({SRC_MODS,43})&&near(pc_settings_get_piki_speed_scale(),1),"guest Pikmin speed row explains host control instead of silently changing nothing");
 check(!disabledReason({SRC_MODS,42})&&pc_settings_get_recall_all()==1,"both players may enable their own practice recall button");
 for(bool* blocked:{&hard,&speedrun,&vsMode,&det}){*blocked=true;check(pc_settings_get_recall_all()==0&&near(pc_settings_get_piki_speed_scale(),1)&&disabledReason({SRC_MODS,42}),"restricted modes retain original cheat safety gates");*blocked=false;}
 practice=false;check(pc_settings_get_recall_all()==0&&near(pc_settings_get_piki_speed_scale(),1)&&disabledReason({SRC_MODS,42}),"unrelated local multiplayer stays restricted");
 zen::particleManager pm;zen::particleGenerator allowed,other,finished;
 allowed.mPcCoopWhistleVisual=finished.mPcCoopWhistleVisual=true;finished.finished=true;
 pm.mActiveGenList.first=&allowed;allowed.mNext=&other;other.mNext=&finished;finished.mNext=&pm.mActiveGenList.sentinel;
 sessionRunning=false;pm.updateCoopWhistles();check(!allowed.calls&&!other.calls,"paused guest does not advance whistle particles");
 sessionRunning=true;pm.updateCoopWhistles();check(allowed.calls==1&&finished.calls==1&&other.calls==0,"actual native manager advances only tagged whistle generators, not unrelated callbacks");
 check(pm.recycled==1&&near(allowed.step,1),"native whitelist path recycles ended effects and bounds interruption time step");
 role=net::CoopRole::Host;pm.updateCoopWhistles();check(allowed.calls==1,"whistle presentation path never double-updates host effects");
 role=net::CoopRole::Guest;away=true;pm.updateCoopWhistles();check(allowed.calls==1,"background interruption freezes guest effect clock");
 std::printf("%s %d actual practice feedback checks\n",failures?"FAIL":"PASS",checks);return failures?1:0;
}
'''
out=Path(sys.argv[1]);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(code.replace('BODIES','\n'.join(parts)),encoding='utf-8')
