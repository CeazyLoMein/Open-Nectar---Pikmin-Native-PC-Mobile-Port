"""Host scenarios executing the actual P1 charge, release, recall and ledge code."""
from pathlib import Path
import re,sys,subprocess
ROOT=Path(__file__).resolve().parents[1]
if not (ROOT/'games').exists(): ROOT=Path(r'C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port')
old_ref=sys.argv[2] if len(sys.argv)>2 else None
def read(p):
 if old_ref:return subprocess.check_output(['git','show',old_ref+':'+p],cwd=ROOT).decode('utf-8')
 return (ROOT/p).read_text(encoding='utf-8')
def extract(s,signature,default=''):
 at=s.find(signature)
 if at<0:
  assert default,signature
  return default
 start=s.index('{',at);level=1;i=start+1
 while level:
  if s[i]=='{':level+=1
  if s[i]=='}':level-=1
  i+=1
 return s[at:i]
nav=read('games/pikmin1/src/plugPikiKando/navi.cpp')
# Extracted behavior tests supply engine types below. Check the owning source's
# real dependency too, so that seam cannot hide a missing compiler declaration.
if 'KeyConfig::' in nav:
 assert '#include "KeyConfig.h"' in nav, 'navi.cpp must include its KeyConfig dependency'
piki=read('games/pikmin1/src/plugPikiKando/piki.cpp')
crowd=read('games/pikmin1/src/plugPikiKando/aiCrowd.cpp')
settings=read('games/pikmin1/pc_port/settings/pc_settings.cpp')
touch=read('games/pikmin1/pc_port/touch/pc_touch.cpp')
pieces=[extract(piki,'void Piki::pcChargeAt('),
 extract(nav,'void Navi::pcReleaseLockOn(', 'void Navi::pcReleaseLockOn() {}'),
 extract(nav,'static bool pcGroundChargeTarget(', '[[maybe_unused]] static bool pcGroundChargeTarget(Creature*) {return true;}'),
 extract(nav,'void Navi::pcUpdateLockOn('),
 extract(nav,'void Navi::pcPinCursorToLock('),
 extract(crowd,'void ActCrowd::pcProtectFormationEdge(', 'void ActCrowd::pcProtectFormationEdge(Vector3f&) {}'),
 extract(settings,'int pc_settings_get_recall_all(', 'int pc_settings_get_recall_all() {return 0;}')]
pieces.append(extract(settings,'int pc_settings_get_stuck_follower_rescue('))
assert settings.count('stuckFollowerRescue = 0;')==2, 'default and Reset must both be off'
assert 'X(stuckFollowerRescue)' not in settings, 'solo rescue must not alter locked netplay schema'
assert '#if !PIKI_P2_HOST\n    { SRC_MODS, 44, "Rescue Stuck Followers"' in settings
parse=re.search(r'else if \(key == "stuckFollowerRescue"\) ([^\n]+)',settings)[1]
save=re.search(r'out << "stuckFollowerRescue[^\n]+',settings)[0]
change=extract(settings,'else if (row == 44)')[len('else '):]
value=re.search(r'case 44: ([^\n]+)break;',settings)[1]
pieces += ['void parseRescue(const std::string&val){'+parse+'}',
           'std::string saveRescue(){std::ostringstream out;'+save+'return out.str();}',
           'void changeRescue(int row,bool left,bool right){'+change+'}',
           'std::string valueRescue(){char value[64];size_t n=sizeof(value);'+value+'return value;}']
call=extract(nav,'void Navi::callPikis(')
call_decl=re.search(r'void callPikis\([^;]+;',read('games/pikmin1/include/Navi.h'))[0]
if 'pcUpdateRecallAll' in nav:
 assert 'bool recallAll = false' in call_decl, 'ordinary whistle must default to local range'
 pieces += [extract(touch,'static void pcTouchRequestRecall('),
            extract(touch,'static void pcTouchAgeRecallRequest('),
            extract(touch,'bool pc_touch_take_recall_request('),
            extract(nav,'void Navi::pcUpdateRecallAll(')]
call_prefix=call[call.index('{')+1:call.index('\tVector3f unused =')]

eligibility=re.search(r'if \((callable &&.*?dist < radius)\) \{',call,re.S)[1]
distance=call[call.index('\t\tVector3f sep ='):call.index('\n\t\tint state =')].replace('continue;','return false;')
pieces += [extract(touch,'static void pcTouchButtonCursorDrag(', 'static void pcTouchButtonCursorDrag(int button,float dx,float dy) {if(button==BTN_THROW||button==BTN_WHISTLE)pc_window_add_cursor_delta(dx,dy);}'),extract(touch,'bool pc_touch_aim_active(', 'bool pc_touch_aim_active() {return false;}')]
pieces.append('bool Navi::eligible(Piki* piki,float dist,float radius) {\n'
 'const int state=piki->getState();\nbool callable=piki->mNavi==this || !piki->mNavi || piki->mMode!=PikiMode::FormationMode;\nreturn '+eligibility+';\n}')
pieces.append('bool Navi::inRange(Piki* piki,float radius,bool recallAll) {(void)recallAll;\n'+call_prefix+distance+'\nreturn true;}')
code=r'''
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#define PIKI_PC_PORT 1
FOLLOW_HEADER
#define PIKI_PC_TOUCH 1
using f32=float;
void pc_follow_note(const char*,float,float,float,float,float,float,int=0){}
struct Vector3f {float x=0,y=0,z=0; Vector3f()=default;Vector3f(float a,float b,float c):x(a),y(b),z(c){}
 Vector3f operator+(Vector3f b)const{return {x+b.x,y+b.y,z+b.z};}
 Vector3f operator-(Vector3f b)const{return {x-b.x,y-b.y,z-b.z};}
 Vector3f operator*(float b)const{return {x*b,y*b,z*b};}
 void set(float a,float b,float c){x=a;y=b;z=c;}float length()const{return std::sqrt(x*x+y*y+z*z);}float normalise(){float l=length();if(l>0){x/=l;y/=l;z/=l;}return l;}
};
float speedy_sqrtf(float f){return std::sqrt(f);}
enum {TEKI_Shell=10,TEKI_Pearl=13,TEKI_Rocpe=14};
enum {PIKISTATE_Normal,PIKISTATE_Emotion,PIKISTATE_Nukare,PIKISTATE_Swallowed,PIKISTATE_Drown,PIKISTATE_Absorb,PIKISTATE_LookAt,PIKISTATE_Pressed};
enum {STANDTYPE_Ground,STANDTYPE_TekiPlatform,STANDTYPE_Platform,STANDTYPE_Air};
namespace PikiMode {enum {FreeMode,FormationMode,AttackMode};}
namespace PikiAction {enum {Crowd,Attack};}
struct Creature {Vector3f mPlatformAdjustDelta;struct {Vector3f t;}mSRT; bool alive=true;bool teki=true,boss=false;int mObjType=1;
 bool isTeki(){return teki;}bool isBoss(){return boss;}Vector3f getCentre(){return mSRT.t;}};
struct Teki:Creature {int mTekiType=0;};
struct Navi;
struct Child {Creature* target=nullptr;void initialise(Creature*t){target=t;}};
struct Action {int mCurrActionIdx=PikiAction::Crowd;Child mChildActions[2];int abandoned=0;void abandon(void*){++abandoned;}};
struct Piki:Creature {Navi*mNavi=nullptr;int mMode=PikiMode::FormationMode;Action action;Action*mActiveAction=&action;
 bool callable=true,buried=false,kinoko=false;int state=PIKISTATE_Normal,stand=STANDTYPE_Ground;
 bool mIsCallable=true;bool isKinoko(){return kinoko;}bool isBuried(){return buried;}bool isAlive(){return alive;}
 int getState(){return state;}int getStandType(){return stand;}void pcChargeAt(Creature*);bool pcFollowerSegmentClear(const Vector3f&);
};
struct Controller {bool whistle=false;bool keyDown(int){return whistle;}};
struct KeyConfig {struct {int mBind=1;}mSetCursorKey;static KeyConfig*_instance;};KeyConfig keyConfig;KeyConfig*KeyConfig::_instance=&keyConfig;
struct Navi:Creature {PcFollowTrail mPcFollowTrail;Controller controller;Controller*mKontroller=&controller;int mNaviID=0,stand=STANDTYPE_Ground;
 Creature*mPcLockTarget=nullptr,*mPcLockIgnore=nullptr;float mPcChargeTime=0,mCursorNaviDist=0,mCursorMaxRadius=200;
 Vector3f mCStick,mPcAimOffset,mPcPinnedOffset,mCursorPosition,mCursorTargetPosition,mCursorWorldPos;bool mIsCStickNeutral=true;
 void pcReleaseLockOn();void pcUpdateLockOn();void pcPinCursorToLock();void pcPinCursorFirstPerson(){}int getStandType(){return stand;}
 bool eligible(Piki*,float,float);bool inRange(Piki*,float,bool=false);
 void pcUpdateRecallAll();int recalls=0;bool recalledAll=false;
 CALL_DECL

};
void Navi::callPikis(float,bool all){++recalls;recalledAll=all;}
struct Movie {bool mIsActive=false;}movie;
struct Gameflow {Movie*mMoviePlayer=&movie;}gameflow;
struct PlayerState {bool end=false;bool inDayEnd(){return end;}} player;PlayerState*playerState=&player;
struct System {float getFrameTime(){return 1.f/60;}} hostSystem;System*gsys=&hostSystem;
int lockMode=1,chargeOn=1,better=1;bool lockPress=false,chargePress=false,det=false,coop=false,vs=false,speedrun=false,hard=false;
bool pc_netplay_deterministic(){return det;}bool pc_netplay_ext_trace(){return false;}
uint8_t pc_netplay_ext_bits(int){return 0;}unsigned pc_netplay_tick(){return 0;}
namespace pc_input_log {enum {kExtLockOn=1,kExtCharge=2};}
bool pc_window_take_lockon_press(int){bool b=lockPress;lockPress=false;return b;}
bool pc_window_take_swarm_press(int){bool b=chargePress;chargePress=false;return b;}
int pc_settings_get_lock_on(){return lockMode;}int pc_settings_get_charge(){return chargeOn;}
int pc_settings_get_better_pathfinding(){return better;}void pc_settings_note_lock_on(int){}
bool touchAim=false;bool pcTouchAim(const Navi*n){return touchAim&&!det&&n->mNaviID==0;}
bool pc_coop_active(){return coop;}bool pc_vs_active(){return vs;}bool pc_speedrun_active(){return speedrun;}bool pc_hardmode_active(){return hard;}
struct Config {int recallAll=0,stuckFollowerRescue=0;}sConfig,sPending;
std::vector<Creature*> targets;
template<class F>bool pcForEachLockable(F f){for(auto*t:targets)if(t->alive&&f(t))return true;return false;}
float pc_lock_target_radius(Creature*){return 10;}
float pcLockDistXZ(Creature*c,Vector3f p){Vector3f d=c->mSRT.t-p;d.y=0;return d.length();}
std::vector<Piki*> pikis;auto*pikiMgr=&pikis;
struct Iterator {std::vector<Piki*>&items;unsigned index=0;Iterator(std::vector<Piki*>*p):items(*p){}Piki*operator*(){return items[index];}};
#define CI_LOOP(i) for((i).index=0;(i).index<(i).items.size();++(i).index)
#define NAVI_PARM(p) this->p
struct Map {bool hole=false,drop=false;int queries=0;
 void*getCurrTri(float x,float,bool){++queries;return hole&&x>8?nullptr:this;}
 float getMinY(float x,float,bool){++queries;return drop&&x>8?0.0f:50.0f;}
} map;Map*mapMgr=&map;
bool Piki::pcFollowerSegmentClear(const Vector3f& to){for(int i=1;i<=2;++i){float x=mSRT.t.x+(to.x-mSRT.t.x)*i*.5f;float z=mSRT.t.z+(to.z-mSRT.t.z)*i*.5f;if(!mapMgr->getCurrTri(x,z,true))return false;float h=mapMgr->getMinY(x,z,true);if(h<mSRT.t.y-30||h>mSRT.t.y+30)return false;}return true;}

struct ActCrowd {Piki*mPiki;bool mPcFollowingTrail=false,mPcLaneBlocked=false;void pcProtectFormationEdge(Vector3f&);};
enum {BTN_THROW,BTN_WHISTLE,BTN_AIM,BTN_CHARGE,BTN_RECALL_ALL,BTN_COUNT};
struct Button {long long finger=-1;}sButtons[BTN_COUNT];
int sLayoutH=1290,sGameMenuClaimFrames=0,sPortMenuClaimFrames=0;bool sEditMode=false;int sRecallRequestFrames=0;
float cursorDx=0,cursorDy=0;void pc_window_add_cursor_delta(float x,float y){cursorDx+=x;cursorDy+=y;}
FUNCTIONS
int checks=0,failures=0;void check(bool ok,const char*n){++checks;if(!ok){++failures;std::printf("FAIL: %s\n",n);}}
bool near(float a,float b){return std::fabs(a-b)<0.001f;}
int main(){
 Navi n;Piki p;p.mNavi=&n;Teki foe;foe.mSRT.t={80,0,0};targets={&foe};pikis={&p};
 p.pcChargeAt(&foe);
 check(p.mMode==PikiMode::AttackMode,"charge sets true attack mode");
 check(p.mActiveAction->mCurrActionIdx==PikiAction::Attack&&p.action.mChildActions[1].target==&foe,"charge keeps chosen target");
 check(n.eligible(&p,0,100),"charged attacker remains whistle eligible");
 int old=p.action.abandoned;player.end=true;p.pcChargeAt(&foe);check(p.action.abandoned==old,"day end charge rejected");player.end=false;
 p.pcChargeAt(nullptr);check(p.action.abandoned==old,"null target rejected");
 // Manual release from a target beyond the normal cursor radius.
 n.mPcLockTarget=&foe;n.mPcAimOffset={30,0,40};n.mCursorPosition={500,0,0};n.mPcPinnedOffset=n.mCursorPosition;n.mPcChargeTime=2;
 lockPress=true;n.pcUpdateLockOn();
 check(!n.mPcLockTarget&&near(n.mCursorPosition.x,30)&&near(n.mCursorPosition.z,40),"manual unlock restores free aim");
 check(near(n.mCursorTargetPosition.x,30)&&near(n.mPcPinnedOffset.z,40)&&near(n.mCursorNaviDist,50),"all cursor state restored together");
 check(n.mPcChargeTime==0,"unlock cancels remaining charge");
 touchAim=true;n.mPcLockTarget=&foe;n.mPcAimOffset={12,0,15};n.pcUpdateLockOn();
 check(!n.mPcLockTarget&&near(n.mCursorPosition.x,12),"dedicated aim releases target");
 lockMode=2;n.pcUpdateLockOn();check(!n.mPcLockTarget,"dedicated aim blocks auto reacquire while held");touchAim=false;lockMode=1;
 n.mCursorPosition={30,0,40};n.mCursorPosition.x+=5;check(near(n.mCursorPosition.x,35),"free cursor can move immediately");
 n.mPcLockTarget=&foe;n.mPcAimOffset={500,0,0};n.pcReleaseLockOn();check(near(n.mCursorPosition.length(),200),"released cursor clamped to legal radius");
 n.mPcLockTarget=&foe;n.mPcAimOffset={20,0,0};n.mCursorPosition={500,0,0};foe.alive=false;n.pcUpdateLockOn();
 check(!n.mPcLockTarget&&near(n.mCursorPosition.x,20),"dead target release restores manual aim");foe.alive=true;
 n.mPcLockTarget=&foe;n.mPcAimOffset={25,0,0};lockMode=0;n.pcUpdateLockOn();check(!n.mPcLockTarget&&near(n.mCursorPosition.x,25),"setting off releases cursor");lockMode=1;
 n.mPcLockTarget=&foe;n.controller.whistle=true;n.mPcChargeTime=2;chargePress=true;p.mMode=PikiMode::FormationMode;p.action.mCurrActionIdx=PikiAction::Crowd;n.pcUpdateLockOn();
 check(n.mPcChargeTime==0&&p.mMode==PikiMode::FormationMode,"whistle wins over new and ongoing charge");n.controller.whistle=false;
 for(int type:{TEKI_Shell,TEKI_Pearl,TEKI_Rocpe}){foe.mTekiType=type;n.mPcLockTarget=&foe;chargePress=true;n.pcUpdateLockOn();check(n.mPcChargeTime==0&&p.mMode==PikiMode::FormationMode,"raised clam target does not ground-charge");}
 foe.mTekiType=0;p.mSRT.t={70,0,0};n.mPcLockTarget=&foe;chargePress=true;n.pcUpdateLockOn();check(p.mMode==PikiMode::AttackMode,"ordinary enemy still charges");
 p.mMode=PikiMode::FreeMode;p.mSRT.t={10000,0,0};n.mCursorWorldPos={0,0,0};
 sConfig.recallAll=1; check(!n.inRange(&p,100,false),"normal whistle retains range");check(n.inRange(&p,100,true),"recall reaches distant Pikmin");
 p.mMode=PikiMode::FormationMode;check(!n.eligible(&p,0,100),"already following Pikmin not reset repeatedly");p.mMode=PikiMode::AttackMode;
 p.buried=true;check(!n.eligible(&p,0,100),"recall never plucks buried Pikmin");p.buried=false;
 p.kinoko=true;check(!n.eligible(&p,0,100),"recall excludes transformed Pikmin");p.kinoko=false;
 p.alive=false;check(!n.eligible(&p,0,100),"recall never revives");p.alive=true;
 for(int state:{PIKISTATE_Nukare,PIKISTATE_Swallowed,PIKISTATE_Drown,PIKISTATE_Absorb,PIKISTATE_LookAt,PIKISTATE_Pressed}){p.state=state;check(!n.eligible(&p,0,100),"recall preserves unavailable-state guard");}p.state=PIKISTATE_Normal;
 // Soft assist: approach acquires, aim-away and walk-away release it.
 n.mPcLockTarget=nullptr;n.mPcLockIgnore=nullptr;n.mSRT.t={0,0,0};foe.mSRT.t={80,0,0};n.mCursorPosition={80,0,0};lockMode=3;
 n.pcUpdateLockOn();check(n.mPcLockTarget==&foe,"soft assist acquires nearby target");
 n.mPcAimOffset={60,0,0};n.mCursorPosition=n.mPcPinnedOffset;n.pcPinCursorToLock();
 check(n.mCursorPosition.x>60&&n.mCursorPosition.x<80,"soft assist nudges rather than pins cursor");
 n.mPcAimOffset={150,0,0};n.pcUpdateLockOn();check(!n.mPcLockTarget&&near(n.mCursorPosition.x,150),"aiming away releases soft target");
 n.mPcLockTarget=&foe;n.mPcAimOffset={80,0,0};n.mSRT.t={-200,0,0};n.pcUpdateLockOn();check(!n.mPcLockTarget,"walking away releases soft target");
 n.mSRT.t={0,0,0};n.mPcLockTarget=&foe;n.mCursorPosition={80,0,0};n.mPcAimOffset={80,0,0};lockPress=true;n.pcUpdateLockOn();
 check(!n.mPcLockTarget&&n.mPcLockIgnore==&foe,"manual dismissal suppresses immediate soft reacquire");
 lockMode=1;n.mPcLockTarget=&foe;n.mPcAimOffset={30,0,0};n.mPcPinnedOffset=n.mCursorPosition;n.pcPinCursorToLock();check(near(n.mCursorPosition.x,80),"manual hard lock still pins correctly");
 lockMode=1;
 check(pc_settings_get_stuck_follower_rescue()==0,"rescue off by default");
 sConfig.stuckFollowerRescue=1;
#if PIKI_P2_HOST
 check(pc_settings_get_stuck_follower_rescue()==0,"P2 bridge cannot activate P1 rescue");
#else
 check(pc_settings_get_stuck_follower_rescue()==1,"rescue enabled for solo P1");
#endif
 for(bool*flag:{&det,&coop,&vs,&speedrun,&hard}){*flag=true;check(pc_settings_get_stuck_follower_rescue()==0,"rescue disabled in locked contexts");*flag=false;}
 for(const char*text:{"0","1","-1","9","garbage"}){parseRescue(text);int expected=std::atoi(text)?1:0;check(sConfig.stuckFollowerRescue==expected,"rescue parses boolean");check(saveRescue()=="stuckFollowerRescue = "+std::to_string(expected)+"\n","rescue setting persists");}
 check(valueRescue()=="Off (original)","rescue menu initially off");changeRescue(44,false,true);check(sPending.stuckFollowerRescue==1&&valueRescue()=="On","rescue row can turn on");
 changeRescue(42,true,false);check(sPending.stuckFollowerRescue==1,"recall row cannot change rescue");changeRescue(44,true,false);check(!sPending.stuckFollowerRescue,"rescue row can turn off");
 sConfig.stuckFollowerRescue=0;
 sConfig.recallAll=1;check(pc_settings_get_recall_all()==1,"recall can be enabled solo");
 for(bool*flag:{&det,&coop,&vs,&speedrun,&hard}){*flag=true;check(pc_settings_get_recall_all()==0,"recall disabled in competitive/multiplayer contexts");*flag=false;}
 sConfig.recallAll=0;check(pc_settings_get_recall_all()==0,"recall disabled by default/off");
 n.mSRT.t={-30,50,0};p.mSRT.t={0,50,0};ActCrowd a{&p};Vector3f slot(50,50,0);
 map.drop=true;map.queries=0;a.pcProtectFormationEdge(slot);check(near(slot.x,-30),"unsafe following slot redirects toward captain");check(map.queries<=8,"ledge lookahead has bounded query cost");
 map.drop=false;slot={50,50,0};a.pcProtectFormationEdge(slot);check(near(slot.x,50),"flat terrain unchanged");
 map.hole=true;slot={50,50,0};a.pcProtectFormationEdge(slot);check(near(slot.x,-30),"missing ground treated as edge");map.hole=false;map.drop=true;
 better=0;slot={50,50,0};a.pcProtectFormationEdge(slot);check(near(slot.x,50),"ledge guard follows existing setting");better=1;
 p.stand=STANDTYPE_Platform;a.pcProtectFormationEdge(slot);check(near(slot.x,-30),"platform edge is guarded too");slot={50,50,0};p.stand=STANDTYPE_Ground;
 n.mSRT.t.y=0;a.pcProtectFormationEdge(slot);check(near(slot.x,50),"intentional descent preserved");n.mSRT.t.y=50;
 n.mPcFollowTrail.clear();n.mPcFollowTrail.record({0,50,0,true});n.mPcFollowTrail.record({12,50,0,true});
 n.mSRT.t={40,0,0};p.stand=STANDTYPE_Platform;slot={50,0,0};map.queries=0;a.pcProtectFormationEdge(slot);
 check(near(slot.x,50)&&near(slot.y,0)&&!a.mPcFollowingTrail&&!a.mPcLaneBlocked,"captain drop keeps original lower formation target despite stale platform trail");
 check(map.queries==0,"intentional descent does not stop for edge reassessment");
 n.mPcFollowTrail.clear();n.mSRT.t={-30,50,0};p.stand=STANDTYPE_Ground;slot={50,50,0};
 n.mCStick={1,0,0};n.mIsCStickNeutral=false;a.pcProtectFormationEdge(slot);check(near(slot.x,50),"explicit swarm behavior unchanged");
 pcTouchButtonCursorDrag(BTN_AIM,30,15);check(near(cursorDx,10)&&near(cursorDy,5),"dedicated aim DPI-normalized delta");
 cursorDx=cursorDy=0;pcTouchButtonCursorDrag(BTN_THROW,30,15);check(near(cursorDx,30)&&near(cursorDy,15),"throw drag behavior preserved");
 cursorDx=cursorDy=0;pcTouchButtonCursorDrag(BTN_CHARGE,30,15);check(cursorDx==0&&cursorDy==0,"charge button never moves cursor");
 sGameMenuClaimFrames=1;pcTouchButtonCursorDrag(BTN_AIM,30,15);check(cursorDx==0&&cursorDy==0,"game menus suppress aim");sGameMenuClaimFrames=0;
 sPortMenuClaimFrames=1;pcTouchButtonCursorDrag(BTN_AIM,30,15);check(cursorDx==0&&cursorDy==0,"advanced menus suppress aim");sPortMenuClaimFrames=0;
 sButtons[BTN_AIM].finger=2;check(pc_touch_aim_active(),"dedicated aim owns only its finger");
 sEditMode=true;check(!pc_touch_aim_active(),"layout editing cannot steer gameplay");sEditMode=false;
 sButtons[BTN_AIM].finger=-1;check(!pc_touch_aim_active(),"releasing aim ends override");

 sConfig.recallAll=1;n.mNaviID=0;player.end=false;movie.mIsActive=false;
 p.mSRT.t={1000,0,0};n.mCursorWorldPos={0,0,0};
 check(!n.inRange(&p,100),"enabled global option leaves normal whistle range local");
 check(n.inRange(&p,100,true),"explicit Recall All reaches distant worker");
 sConfig.recallAll=0;check(!n.inRange(&p,100,true),"disabled cheat cannot expand even explicit request");sConfig.recallAll=1;
 n.callPikis(100);check(!n.recalledAll,"actual API defaults ordinary whistle to local");
 pcTouchRequestRecall(BTN_WHISTLE);check(!pc_touch_take_recall_request(),"ordinary whistle button never queues global recall");
 pcTouchRequestRecall(BTN_AIM);check(!pc_touch_take_recall_request(),"aim button never queues global recall");
 int calls=n.recalls;pcTouchRequestRecall(BTN_RECALL_ALL);n.pcUpdateRecallAll();
 check(n.recalls==calls+1&&n.recalledAll,"separate button invokes explicit global recall");
 n.pcUpdateRecallAll();check(n.recalls==calls+1,"holding/rechecking does not repeat global recall");
 sGameMenuClaimFrames=3;pcTouchRequestRecall(BTN_RECALL_ALL);check(!pc_touch_take_recall_request(),"game menu cannot queue recall");sGameMenuClaimFrames=0;
 sPortMenuClaimFrames=3;pcTouchRequestRecall(BTN_RECALL_ALL);check(!pc_touch_take_recall_request(),"advanced menu cannot queue recall");sPortMenuClaimFrames=0;
 sEditMode=true;pcTouchRequestRecall(BTN_RECALL_ALL);check(!pc_touch_take_recall_request(),"layout editor cannot queue recall");sEditMode=false;
 sConfig.recallAll=0;pcTouchRequestRecall(BTN_RECALL_ALL);check(!pc_touch_take_recall_request(),"disabled cheat cannot queue recall");sConfig.recallAll=1;
 pcTouchRequestRecall(BTN_RECALL_ALL);pcTouchAgeRecallRequest();check(pc_touch_take_recall_request(),"quick tap survives one input merge");
 pcTouchRequestRecall(BTN_RECALL_ALL);pcTouchAgeRecallRequest();pcTouchAgeRecallRequest();check(!pc_touch_take_recall_request(),"unconsumed request expires rather than firing later");
 pcTouchRequestRecall(BTN_RECALL_ALL);sGameMenuClaimFrames=3;pcTouchAgeRecallRequest();sGameMenuClaimFrames=0;check(!pc_touch_take_recall_request(),"opening menu cancels pending request");
 calls=n.recalls;movie.mIsActive=true;pcTouchRequestRecall(BTN_RECALL_ALL);n.pcUpdateRecallAll();movie.mIsActive=false;n.pcUpdateRecallAll();check(n.recalls==calls,"cutscene drops recall instead of deferring it");
 player.end=true;pcTouchRequestRecall(BTN_RECALL_ALL);n.pcUpdateRecallAll();player.end=false;n.pcUpdateRecallAll();check(n.recalls==calls,"day end drops pending recall");
 for(bool*flag:{&det,&coop,&vs,&speedrun,&hard}){*flag=true;pcTouchRequestRecall(BTN_RECALL_ALL);n.pcUpdateRecallAll();check(n.recalls==calls,"recall command disabled outside permitted solo context");*flag=false;}
 std::printf("%d P1 command/recall/cursor/edge scenarios; %d failures\n",checks,failures);return failures?1:0;
}
'''.replace('FUNCTIONS','\n\n'.join(pieces)).replace('CALL_DECL',call_decl).replace('FOLLOW_HEADER',read('games/pikmin1/pc_port/pc_follow_trail.h'))
out=Path(sys.argv[1]);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(code,encoding='utf-8')
print('Generated real P1 command scenarios'+(' from '+old_ref if old_ref else ''))
