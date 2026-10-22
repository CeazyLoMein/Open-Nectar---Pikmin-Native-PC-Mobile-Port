"""Execute actual P1 crossing/recovery/setup methods; no game assets required."""
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
def fn(s,sig):
 a=s.index(sig);b=s.index('{',a);n=1;i=b+1
 while n:
  if s[i]=='{':n+=1
  if s[i]=='}':n-=1
  i+=1
 return s[a:i]
nav=(root/'games/pikmin1/src/plugPikiKando/navi.cpp').read_text(encoding='utf-8')
crowd=(root/'games/pikmin1/src/plugPikiKando/aiCrowd.cpp').read_text(encoding='utf-8')
piki=(root/'games/pikmin1/src/plugPikiKando/piki.cpp').read_text(encoding='utf-8')
assert '#include "PikiState.h"' in crowd and '#include "pc_coop.h"' in crowd and '#include "netplay/pc_netplay_det.h"' in crowd
assert 'pcUpdateFollowTrail();' in fn(nav,'void Navi::update(')
assert 'if (pcRecoverFollower()) return ACTOUT_Continue;' in fn(crowd,'int ActCrowd::exec(')
assert 'if (mPcFollowingTrail)' in fn(crowd,'int ActCrowd::exec(')
for sig in ['void ActCrowd::init(','void ActCrowd::cleanup(']:assert 'pcResetFollowerRecovery();' in fn(crowd,sig)
cpp=r"""
#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>
#define PIKI_PC_PORT 1
#define immut const
#define PRINT(...) ((void)0)
using f32=float;
REPORT_HEADER
HEADER
struct Vector3f {float x=0,y=0,z=0;Vector3f()=default;Vector3f(float a,float b,float c):x(a),y(b),z(c){}
Vector3f operator+(Vector3f p)const{return {x+p.x,y+p.y,z+p.z};}Vector3f operator*(float a)const{return {x*a,y*a,z*a};}Vector3f operator-(Vector3f p)const{return {x-p.x,y-p.y,z-p.z};}float length()const{return std::sqrt(x*x+y*y+z*z);}float normalise(){float d=length();if(d>0){x/=d;y/=d;z/=d;}return d;}void set(float a,float b,float c){x=a;y=b;z=c;}};
enum {STANDTYPE_Ground,STANDTYPE_TekiPlatform,STANDTYPE_Platform,STANDTYPE_Air,PIKISTATE_Normal=20,PIKISTATE_Drown,Red=0,Blue=2};
namespace PikiMode {enum {FormationMode,CarryMode,AttackMode,FreeMode};}
enum {PIKIANIM_Run,PIKIANIM_Walk};int PaniMotionInfo(int x){return x;}
bool rescueEnabled=false;bool pc_settings_get_stuck_follower_rescue(){return rescueEnabled;}
bool better=true,det=false,coop=false,vs=false,blues=true;float pikiScale=1;float pc_settings_get_piki_speed_scale(){return pikiScale;}
bool pc_settings_get_better_pathfinding(){return better;}bool pc_netplay_deterministic(){return det;}bool pc_coop_active(){return coop;}bool pc_vs_active(){return vs;}bool pc_settings_get_blues_only_water(){return blues;}
struct System {float dt=1.f/60.f;float getFrameTime(){return dt;}}sys;System*gsys=&sys;
struct Movie {bool mIsActive=false;}movie;struct Game {Movie*mMoviePlayer=&movie;}gameflow;
struct State {bool end=false;bool inDayEnd(){return end;}}state;State*playerState=&state;
struct Creature {struct {Vector3f t;}mSRT;Vector3f mLastPosition;bool alive=true,visibility=true,teki=false;bool isAlive(){return alive;}bool isVisible(){return visibility;}bool isTeki(){return teki;}void resetPosition(const Vector3f&p){mSRT.t=p;mLastPosition=p;}};
struct Teki:Creature {Teki(){teki=true;}int mTekiType=0;};enum {TEKI_Palm=7,TEKI_Pearl=13,TEKI_Rocpe=14};
struct CollTriInfo {int attr=0;};enum{ATTR_Water=5,ATTR_Hole=6};struct MapCode{static int getAttribute(CollTriInfo*t){return t->attr;}};CollTriInfo dryFloor;
struct ObjectMgr {std::vector<Creature*> items;};
struct Iterator {ObjectMgr*m;unsigned at=0;Iterator(ObjectMgr*p):m(p){}void first(){at=0;}bool isDone(){return at>=m->items.size();}void next(){++at;}Creature*operator*(){return m->items[at];}};
#define CI_LOOP(i) for(i.first();!i.isDone();i.next())
ObjectMgr pikiStore;ObjectMgr*pikiMgr=&pikiStore,*tekiMgr=nullptr,*bossMgr=nullptr;
struct Navi:Creature {Vector3f mCStick;CollTriInfo*mGroundTriangle=&dryFloor;void*mRope=nullptr;Vector3f mPlatformAdjustDelta;bool stick=false,mIsCStickNeutral=true,mIsInWater=false;int stand=STANDTYPE_Ground;
bool isAlive(){return alive;}bool isStickTo(){return stick;}int getStandType(){return stand;}
PcFollowTrail mPcFollowTrail;float mPcFollowerRescueCooldown=0,mPcFollowRouteCooldown=0;bool pcTakeFollowerRescueBudget();void pcUpdateFollowTrail();bool pcTakeFollowerRouteBudget();};
struct WayPoint {Vector3f mPosition;bool mIsOpen=true,water=false;int mIndex=0;bool inWater(){return water;}};
namespace PathFinderMode {enum {AvoidWater=1};}
struct Buffer {int mWayPointIdx=0;};
struct PathFinder {static int mode;bool available=true,blocked=false,wet=false;int calls=0,releases=0;bool ignoredClosed=true;
static void setMode(int x){mode=x;}static void clearMode(){mode=0;}
void releaseHandle(int){++releases;}
int findSync(Buffer*b,int a,int z,bool closed){++calls;ignoredClosed=closed;b[0].mWayPointIdx=a;b[1].mWayPointIdx=z;return blocked||((mode&1)&&wet)?0:2;}}pf;int PathFinder::mode=0;
struct Route {WayPoint first,last;bool missingStart=false,missingEnd=false,noFinder=false;int count=2;
PathFinder*getPathFinder(int){return noFinder?nullptr:&pf;}int getNumWayPoints(int){return count;}
void findNearestEdgeAvoidOff(WayPoint**a,WayPoint**b,int,Vector3f,bool,bool,bool){*a=missingStart?nullptr:&first;*b=nullptr;}
WayPoint*findNearestWayPoint(int,Vector3f p,bool dry){WayPoint*w=p.x>100?&last:&first;if((w==&first&&missingStart)||(w==&last&&missingEnd)||(dry&&w->water))return nullptr;return w;}
WayPoint*getWayPoint(int,int index){return index==0?(missingStart?nullptr:&first):index==1?(missingEnd?nullptr:&last):nullptr;}
}route;Route*routeMgr=&route;
struct Sphere {Sphere(Vector3f,float){}}; struct Tube {Tube(Vector3f,Vector3f,float,float){}bool collide(Sphere&,Vector3f&,float&){return false;}};

struct Piki:Creature {Vector3f mPlatformAdjustDelta,mTargetVelocity;Navi*mNavi=nullptr;
bool holding=false,damaged=false,stick=false;bool mIsCallable=true;void*mRope=nullptr;CollTriInfo*mGroundTriangle=&dryFloor,*mPreviousTriangle=nullptr,*mPikiPlatformTriangle=nullptr;Vector3f mShadowPos,mEffectPos,mLastAnimPosition;bool isBuried(){return false;}void resetPosition(const Vector3f&);int state=PIKISTATE_Normal,mMode=PikiMode::FormationMode,mColor=Red,stand=STANDTYPE_Ground;
bool isAlive(){return alive;}int getState(){return state;}bool isHolding(){return holding;}bool isDamaged(){return damaged;}bool isStickTo(){return stick;}int getStandType(){return stand;}
Buffer buffer[8]={};Buffer*mPathBuffers=buffer;int mRouteHandle=0;bool mUseAsyncPathfinding=false,mIsRetryPathfind=false;
int mNumRoutePoints=0,mRouteSourceIndex=-1,mRouteDestinationIndex=-1,mCurrRoutePoint=-1,sharedCalls=0,moves=0,moveResult=2;
Vector3f mRouteStartPos,mRouteGoalPos,mSplineControlPts[4];
bool initRouteTrace(const Vector3f&,bool,bool=false);
int findRoute(int,int,bool,bool){++sharedCalls;return 2;}
Vector3f crGetPoint(int){return {};}float crGetRadius(int){return 1;}bool crPointOpen(int){return true;}void crMakeRefs(){}
float mMoveSpeed=0;Vector3f mVelocity;float getSpeed(float){return 100*pikiScale;}
bool pcRescueFollowerNearCaptain();bool pcFollowerSegmentClear(const Vector3f&g);bool pcBuildFollowerRoute(const Vector3f&);void pcSteerFollowerGoal(const Vector3f&);
int pcMoveFollowerRoute();void setSpeed(float,Vector3f d){mTargetVelocity={d.x*100,d.y*100,d.z*100};++moves;}void startMotion(int,int){}
};
struct TestPlate {void releaseSlot(void*,int){}int getSlot(void*,void*){return 0;}}testPlate;
struct TestParms {float mFormationSlipRange=600,mFormationBreakRange=1000,mMaxLostChildTime=10;}testParms;
#define C_PIKI_PARM(p,v) testParms.v
enum {ACTOUT_Fail=1};
struct ActCrowd {int mCPlateSlotID=0;bool mHasRequestedNewSlot=false;TestPlate*mPlateMgr=&testPlate;bool testFormationRetention(float);Piki*mPiki;PcStuckFollowerMonitor mPcStranded;bool mPcReturnFailed=false;float mPcRescueCooldown=0;PcFollowerProgress mPcFollowerProgress;bool mPcFollowingTrail=false,mPcLaneBlocked=false,mPcRecoveryRoute=false,mPcReturning=false,mIsTripping=false,mIsWaiting=false;
float mPcRecoveryRouteAge=0,mLostChildTimer=0;Vector3f mPcRecoveryGoal;
void pcResetFollowerRecovery();bool pcRecoverFollower();};
bool surfaceBlocked=false,localStepBlocked=false;int blockedEntry=-1;
bool pcFollowWalkLine(const Vector3f&a,const Vector3f&b,bool){
 if(surfaceBlocked || (localStepBlocked && b.x>1 && b.x<100))return false;if(std::fabs(a.y-b.y)>40)return false;
 if(blockedEntry>=0&&nearbyint(b.x)==blockedEntry)return false;
 return true;
}
bool mapAvailable=true;bool*mapMgr=&mapAvailable;bool landingAvailable=true;
bool pcFollowRescueSpot(const Vector3f&,const Vector3f&candidate,Vector3f&out){out=candidate;return landingAvailable;}
FUNCTIONS
int checks=0,failures=0;void check(bool c,const char*n){++checks;if(!c){++failures;std::printf("FAIL %s\n",n);}}
bool near(float a,float b){return std::fabs(a-b)<.001f;}
bool wait(ActCrowd&a,int ticks=100){bool result=false;for(int i=0;i<ticks;++i){a.mPiki->mNavi->pcUpdateFollowTrail();result=a.pcRecoverFollower()||result;}return result;}
int main(){
PcFollowTrail t;PcFollowTrail::Point p;
t.record({0,50,0,true});t.record({12,50,0,true});t.record({24,50,0,true});
check(t.target({0,50,0,false},{24,50,0,false},true,p)&&near(p.x,12),"platform follower takes next captain footstep");
check(!t.target({12,0,0,false},{24,50,0,false},true,p),"below-platform Pikmin cannot use trail above it");
check(!t.target({500,50,0,false},{24,50,0,false},true,p),"distant follower not pulled across missing trail");
t.clear();t.record({0,0,0,true});t.record({12,0,0,true});t.record({12,0,12,true});t.record({12,0,24,true});
check(t.target({0,0,0,false},{12,0,24,false},true,p)&&near(p.x,12)&&near(p.z,0),"corner follows first leg rather than diagonal to captain");
t.clear();t.record({0,0,0,false});t.record({12,0,0,false});check(!t.target({0,0,0,false},{12,0,0,false},false,p),"ordinary ground retains wide formation");
t.record({500,0,0,true});check(t.count==1,"captain relocation breaks stale path");
t.record({512,100,0,true});check(t.count==1,"large height jump breaks trail");
t.clear();for(int i=0;i<200;++i)t.record({float(i*12),0,0,true});check(t.count==64&&near(t.points[0].x,136*12),"trail storage remains bounded");
for(int fps:{30,60,120}){PcFollowerProgress monitor;bool fired=false;for(int i=0;i<fps;++i)fired=monitor.stalled(0,0,0,1.f/fps,true)||fired;check(!fired,"no early stuck detection at any frame rate");for(int i=0;i<fps;++i)fired=monitor.stalled(0,0,0,1.f/fps,true)||fired;check(fired,"stuck detection uses seconds at30/60/120FPS");}
PcFollowerProgress prog;bool stuck=false;for(int i=0;i<100;++i)stuck=prog.stalled(0,0,0,1.f/60,true)||stuck;check(stuck,"stationary separated follower detected");
prog.reset();stuck=false;for(int i=0;i<200;++i)stuck=prog.stalled(float(i),0,0,1.f/60,true)||stuck;check(!stuck,"healthy walking follower never classified stuck");
prog.reset();for(int i=0;i<10;++i)prog.stalled(0,0,0,0.016f,false);check(!prog.stalled(0,0,0,20,true),"background time alone cannot trigger recovery");
Navi n;n.mSRT.t={0,0,0};n.stand=STANDTYPE_Platform;n.pcUpdateFollowTrail();n.mSRT.t={12,0,0};n.pcUpdateFollowTrail();check(n.mPcFollowTrail.count==2,"grounded platform samples recorded");
n.stand=STANDTYPE_Air;n.pcUpdateFollowTrail();check(n.mPcFollowTrail.count==0,"airborne captain clears trail");n.stand=STANDTYPE_Ground;
for(bool*flag:{&det,&coop,&vs}){*flag=true;n.pcUpdateFollowTrail();check(n.mPcFollowTrail.count==0,"no unsynchronized trail in multiplayer");*flag=false;}
n.mPcFollowRouteCooldown=0;check(n.pcTakeFollowerRouteBudget()&&!n.pcTakeFollowerRouteBudget(),"route token prevents squad search burst");
for(int i=0;i<32;++i)n.pcUpdateFollowTrail();check(n.pcTakeFollowerRouteBudget(),"captain budget replenishes in simulation time");
Piki k;k.mNavi=&n;n.mSRT.t={200,0,0};route.first.mPosition={0,0,0};route.last.mPosition={200,0,0};route.last.mIndex=1;
check(k.initRouteTrace(n.mSRT.t,false,true)&&pf.calls==1&&k.sharedCalls==0&&!k.mUseAsyncPathfinding&&!pf.ignoredClosed,"recovery uses synchronous direct route and respects gates");
route.missingStart=true;route.missingEnd=true;check(!k.initRouteTrace(n.mSRT.t,false,true),"no waypoint safe failure");route.missingStart=false;route.missingEnd=false;
surfaceBlocked=true;check(!k.initRouteTrace(n.mSRT.t,false,true),"no reachable destination safe failure");surfaceBlocked=false;
route.last.mIsOpen=false;route.missingStart=true;check(!k.initRouteTrace(n.mSRT.t,false,true),"no open route endpoints safe failure");route.last.mIsOpen=true;route.missingStart=false;
route.last.mPosition.y=100;route.missingStart=true;check(!k.initRouteTrace(n.mSRT.t,false,true),"waypoint on another floor rejected");route.last.mPosition.y=0;route.missingStart=false;
route.first.mPosition.x=190;surfaceBlocked=true;check(!k.initRouteTrace(n.mSRT.t,false,true),"near but unreachable route entry rejected");surfaceBlocked=false;route.first.mPosition.x=0;

route.noFinder=true;check(!k.initRouteTrace(n.mSRT.t,false,true),"missing path finder safe failure");route.noFinder=false;
k.mPathBuffers=nullptr;check(!k.initRouteTrace(n.mSRT.t,false,true),"missing route buffer safe failure");k.mPathBuffers=k.buffer;
pf.wet=true;check(!k.initRouteTrace(n.mSRT.t,false,true),"red recovery route excludes water");k.mColor=Blue;check(k.initRouteTrace(n.mSRT.t,false,true),"blue recovery may use water");pf.wet=false;k.mColor=Red;check(PathFinder::mode==0,"global pathfinder mode restored after failure/success");
pf.blocked=true;check(!k.initRouteTrace(n.mSRT.t,false,true),"disconnected/blocked route fails without teleport");pf.blocked=false;
check(k.initRouteTrace(n.mSRT.t,false,true)&&k.pcMoveFollowerRoute()==2&&std::isfinite(k.mTargetVelocity.x),"coincident start waypoint skipped without NaN");
route.last.mIsOpen=false;check(k.pcMoveFollowerRoute()==1,"gate closing during route stops movement");route.last.mIsOpen=true;
route.last.water=true;check(k.pcMoveFollowerRoute()==1,"route rechecks water before walking");route.last.water=false;
k.mPathBuffers[k.mCurrRoutePoint].mWayPointIdx=99;check(k.pcMoveFollowerRoute()==1,"invalid live route waypoint rejected");k.initRouteTrace(n.mSRT.t,false,true);
k.mCurrRoutePoint=1;k.mSRT.t={200,-80,0};check(k.pcMoveFollowerRoute()==1,"below destination cannot finish route on wrong floor");k.mSRT.t={0,0,0};

ActCrowd a{};a.mPiki=&k;k.mTargetVelocity={50,0,0};n.mPcFollowRouteCooldown=0;int before=pf.calls;check(wait(a)&&a.mPcRecoveryRoute&&pf.calls>before,"stationary follower starts walking valid route");
int calls=pf.calls;check(a.pcRecoverFollower()&&pf.calls==calls,"active route follows without searching each frame");
n.mSRT.t={0,100,0};k.mSRT.t={0,0,0};a.pcResetFollowerRecovery();pf.calls=0;n.mPcFollowRouteCooldown=0;
wait(a);check(a.mPcReturning,"directly below captain retains return ownership");n.mSRT.t={200,0,0};
for(int mode:{PikiMode::CarryMode,PikiMode::AttackMode,PikiMode::FreeMode}){a.pcResetFollowerRecovery();k.mMode=mode;calls=pf.calls;check(!wait(a)&&pf.calls==calls,"working/attacking/idle Pikmin untouched");}k.mMode=PikiMode::FormationMode;
for(bool*flag:{&k.holding,&k.damaged,&k.stick,&a.mIsTripping,&state.end,&movie.mIsActive,&det,&coop,&vs}){a.pcResetFollowerRecovery();*flag=true;calls=pf.calls;check(!wait(a)&&pf.calls==calls,"special states never trigger recovery route");*flag=false;}
a.pcResetFollowerRecovery();n.mSRT.t={80,0,0};k.mTargetVelocity={0,0,0};calls=pf.calls;check(!wait(a)&&pf.calls==calls,"wide parked formation is not mistaken for a stuck follower");k.mTargetVelocity={50,0,0};n.mSRT.t={200,0,0};
k.state=PIKISTATE_Drown;check(!wait(a),"drowning Pikmin never rescued by route cheat");k.state=PIKISTATE_Normal;
n.mIsInWater=true;check(!wait(a),"red follower waits ashore");n.mIsInWater=false;
better=false;calls=pf.calls;check(!wait(a)&&calls==pf.calls,"original behavior available with Better Pathfinding off");better=true;
a.pcResetFollowerRecovery();n.mPcFollowRouteCooldown=0;pf.blocked=true;before=pf.calls;wait(a,240);check(pf.calls-before<=12,"failed searches back off per follower");pf.blocked=false;
check(near(k.mSRT.t.x,0)&&near(k.mSRT.t.y,0),"no recovery path teleports Pikmin");

PcFollowerProgress circle;bool circlingStuck=false;for(int i=0;i<180;++i){float angle=i*.2f;circlingStuck=circle.stalledToward(100*std::cos(angle),0,100*std::sin(angle),1.f/60,true,0,0,0)||circlingStuck;}check(circlingStuck,"circling is not progress toward destination");
PcFollowerProgress closer;bool healthyStuck=false;for(int i=0;i<180;++i)healthyStuck=closer.stalledToward(float(i),0,0,1.f/60,true,300,0,0)||healthyStuck;check(!healthyStuck,"actual progress toward goal does not trigger recovery");
for(int fps:{30,60,120})for(float scale:{1.f,2.f,5.f}){sys.dt=1.f/fps;pikiScale=scale;k.mSRT.t={0,0,0};k.mVelocity={1000,0,0};k.pcSteerFollowerGoal({12,0,0});check(k.mTargetVelocity.length()*sys.dt<=6.01f,"short following target cannot be overshot at500percent");check(k.mVelocity.length()<=100.01f,"crossing brakes inherited horizontal speed");}sys.dt=1.f/60;pikiScale=1;
a.pcResetFollowerRecovery();n.mSRT.t={1000,0,0};k.mSRT.t={0,0,0};surfaceBlocked=true;n.mPcFollowRouteCooldown=0;wait(a,300);check(a.mPcReturning,"failed long recall preserves return intent");check(k.mTargetVelocity.length()==0,"failed recall waits instead of pushing directly into cliff");surfaceBlocked=false;

surfaceBlocked=false;k.mRouteHandle=73;int released=pf.releases;
check(k.initRouteTrace({200,0,0},false,true)&&k.mRouteHandle==0&&pf.releases==released+1,"old async handle released once before follower route rebuild");
a.pcResetFollowerRecovery();n.mSRT.t={200,0,0};n.mPcFollowRouteCooldown=0;localStepBlocked=true;
wait(a);check(a.mPcReturning&&!a.mPcRecoveryRoute,"blocked first route step retains return ownership after measured stall");
check(k.mTargetVelocity.length()==0,"blocked first step brakes instead of falling into stock movement");localStepBlocked=false;

// Normal following must not acquire route tokens merely for distance or
// a deliberate downward step. Simulate continuous progress at each frame rate.
for(int fps:{30,60,120}){
 sys.dt=1.f/fps;ActCrowd healthy{};healthy.mPiki=&k;bool tookOver=false;
 n.mPcFollowRouteCooldown=0;before=pf.calls;
 for(int j=0;j<fps*5;++j){k.mSRT.t={j*60.f/fps,50,0};n.mSRT.t={k.mSRT.t.x+200,0,0};k.mTargetVelocity={60,0,0};n.pcUpdateFollowTrail();tookOver=healthy.pcRecoverFollower()||tookOver;}
 check(!tookOver&&pf.calls==before,"healthy descending follower never joins global route-search queue");
 check(k.mTargetVelocity.x>0,"distance/height alone cannot brake healthy movement");
}
sys.dt=1.f/60;k.mSRT.t={0,0,0};n.mSRT.t={200,0,0};k.mTargetVelocity={50,0,0};
ActCrowd grace{};grace.mPiki=&k;before=pf.calls;check(!wait(grace,60)&&pf.calls==before,"stationary separation gets normal-follow grace before route takeover");
// Route completion is success even if the captain moved farther afterward.
ActCrowd finished{};finished.mPiki=&k;finished.mPcReturning=true;finished.mPcRecoveryRoute=true;
n.mSRT.t={400,0,0};finished.mPcRecoveryGoal=n.mSRT.t;k.mSRT.t={200,0,0};k.mRouteGoalPos=k.mSRT.t;k.mNumRoutePoints=2;k.mCurrRoutePoint=2;
check(!finished.pcRecoverFollower()&&!finished.mPcRecoveryRoute&&!finished.mPcReturnFailed,"completed route immediately hands back normal following without marking failure");
ActCrowd ownership{};ownership.mPiki=&k;ownership.mPcReturning=true;
check(ownership.testFormationRetention(1200),"distant return assignment survives normal-follow handoff");
ownership.mLostChildTimer=20;check(ownership.testFormationRetention(800),"return intent protects assignment while observing movement");
ownership.mCPlateSlotID=-1;check(!ownership.testFormationRetention(800),"invalid formation slot still rejects safely");
ownership.mCPlateSlotID=0;ownership.mPcReturning=false;check(!ownership.testFormationRetention(1200),"original non-recovery formation break preserved");
k.mSRT.t={0,0,0};n.mSRT.t={200,0,0};

// Conservative classifier: moving captain alone is not Pikmin progress, while
// an actor walking toward each sampled goal is not stranded.
for(int fps:{30,60,120}){
 PcStuckFollowerMonitor stalledMonitor;bool early=false;
 for(int j=0;j<int(fps*7.5f);++j)early=stalledMonitor.update(0,0,0,1.f/fps,true,300,0,0)||early;
 check(!early,"automatic rescue never triggers before eight seconds");
 bool ready=false;for(int j=0;j<fps;++j)ready=stalledMonitor.update(0,0,0,1.f/fps,true,300+float(j),0,0)||ready;
 check(ready,"stuck detector survives moving captain and failed-search retries");
 PcStuckFollowerMonitor healthy;bool falselyStuck=false;
 for(int j=0;j<fps*12;++j)falselyStuck=healthy.update(j*60.f/fps,0,0,1.f/fps,true,400+j*60.f/fps,0,0)||falselyStuck;
 check(!falselyStuck,"walking follower behind moving captain never rescued just for distance");
 PcStuckFollowerMonitor spinning;bool circleReady=false;
 for(int j=0;j<fps*9;++j){float angle=j*3.f/fps;circleReady=spinning.update(100*std::cos(angle),0,100*std::sin(angle),1.f/fps,true,0,0,0)||circleReady;}
 check(circleReady,"circling without getting nearer counts as a sustained stall");
 PcStuckFollowerMonitor parked;for(int j=0;j<fps*12;++j)parked.update(0,0,0,1.f/fps,false,300,0,0);
 check(parked.seconds==0,"parked formations do not accumulate rescue time");
}
PcStuckFollowerMonitor pauseMonitor;check(!pauseMonitor.update(0,0,0,60,true,300,0,0),"pause/background delta cannot instantly cause a rescue");
rescueEnabled=true;better=true;pf.blocked=true;surfaceBlocked=true;landingAvailable=true;
n.mSRT.t={300,0,0};n.mCStick={0,0,0};n.mIsCStickNeutral=false;n.mGroundTriangle=&dryFloor;n.mPcFollowRouteCooldown=0;n.mPcFollowerRescueCooldown=0;
k.mSRT.t={0,0,0};k.mTargetVelocity={50,0,0};pikiStore.items={&k};ActCrowd rescue{};rescue.mPiki=&k;
wait(rescue,420);check(near(k.mSRT.t.x,0)&&rescue.mPcReturnFailed,"failed route at seven seconds has not teleported a follower");
wait(rescue,100);check((k.mSRT.t-n.mSRT.t).length()<60,"stuck owned follower rescued after eight seconds despite stock non-neutral separation flag");
check(k.mMode==PikiMode::FormationMode&&k.mNavi==&n,"rescue preserves squad ownership and action bookkeeping");
check(near(k.mLastPosition.x,k.mSRT.t.x)&&near(k.mShadowPos.x,k.mSRT.t.x)&&near(k.mEffectPos.x,k.mSRT.t.x),"actual resetPosition synchronizes collision/shadow/effect positions");
check(rescue.mPcRescueCooldown>0,"successful rescue starts per-follower cooldown");
k.mSRT.t={0,0,0};wait(rescue,420);check(near(k.mSRT.t.x,0),"immediately repeated separation cannot produce teleport loop");
for(int mode:{PikiMode::CarryMode,PikiMode::AttackMode,PikiMode::FreeMode}){
 ActCrowd worker{};worker.mPiki=&k;k.mMode=mode;k.mSRT.t={0,0,0};wait(worker,600);
 check(near(k.mSRT.t.x,0)&&!worker.mPcReturnFailed,"workers fighters and intentionally idle Pikmin never automatically rescued");
}k.mMode=PikiMode::FormationMode;
landingAvailable=false;k.mSRT.t={0,0,0};ActCrowd unsafe{};unsafe.mPiki=&k;wait(unsafe,650);
check(near(k.mSRT.t.x,0),"no safe landing means wait rather than force teleport");landingAvailable=true;
for(bool*flag:{&k.holding,&k.damaged,&k.stick}){*flag=true;check(!k.pcRescueFollowerNearCaptain(),"rescue method independently excludes held damaged or attached followers");*flag=false;}
k.mRope=&k;check(!k.pcRescueFollowerNearCaptain(),"rope/onion transition cannot be rescued");k.mRope=nullptr;
k.mIsCallable=false;check(!k.pcRescueFollowerNearCaptain(),"uncallable transition not bypassed by rescue");k.mIsCallable=true;
k.stand=STANDTYPE_Air;check(!k.pcRescueFollowerNearCaptain(),"thrown/falling follower never rescued mid-air");k.stand=STANDTYPE_Ground;
n.stand=STANDTYPE_Air;check(!k.pcRescueFollowerNearCaptain(),"airborne captain cannot define a landing");n.stand=STANDTYPE_Ground;
dryFloor.attr=ATTR_Water;check(!k.pcRescueFollowerNearCaptain(),"swimming captain cannot teleport reds into water");dryFloor.attr=ATTR_Hole;check(!k.pcRescueFollowerNearCaptain(),"captain over hole is not a landing");dryFloor.attr=0;
ObjectMgr enemies;Creature enemy;enemy.mSRT.t=n.mSRT.t;enemies.items={&enemy};tekiMgr=&enemies;check(!k.pcRescueFollowerNearCaptain(),"nearby hostile blocks rescue into combat");
enemy.mSRT.t={0,0,0};check(!k.pcRescueFollowerNearCaptain(),"active combat at origin not escaped through rescue");
Teki flower;flower.mTekiType=TEKI_Palm;flower.mSRT.t=n.mSRT.t;enemies.items={&flower};check(k.pcRescueFollowerNearCaptain(),"harmless pellet posy does not falsely block safe rescue");tekiMgr=nullptr;
Piki crowded;crowded.mSRT.t={322,0,0};pikiStore.items={&k,&crowded};k.mSRT.t={0,0,0};check(k.pcRescueFollowerNearCaptain()&&(k.mSRT.t-crowded.mSRT.t).length()>=12,"rescue selects an unoccupied spot rather than stacking into a peer");
rescueEnabled=false;k.mSRT.t={0,0,0};check(!k.pcRescueFollowerNearCaptain(),"rescue is opt-in and can be disabled");
n.mCStick={1,0,0};ActCrowd commanded{};commanded.mPiki=&k;check(!wait(commanded,600),"actual swarm input retains player control and cancels rescue observation");n.mCStick={0,0,0};
std::printf("%d P1 crossing/route recovery scenarios; %d failures\n",checks,failures);return failures?1:0;
}
"""
cpp=cpp.replace('REPORT_HEADER',(root/'games/pikmin1/pc_port/pc_follow_report.h').read_text(encoding='utf-8'))
cpp=cpp.replace('HEADER',(root/'games/pikmin1/pc_port/pc_follow_trail.h').read_text(encoding='utf-8'))
funcs=[fn(nav,'void Navi::pcUpdateFollowTrail('),fn(nav,'bool Navi::pcTakeFollowerRouteBudget('),fn(nav,'bool Navi::pcTakeFollowerRescueBudget('),fn(piki,'bool Piki::initRouteTrace('),fn(piki,'void Piki::resetPosition('),fn(piki,'bool Piki::pcRescueFollowerNearCaptain('),fn(piki,'bool Piki::pcFollowerSegmentClear('),fn(piki,'void Piki::pcSteerFollowerGoal('),fn(piki,'bool Piki::pcBuildFollowerRoute('),fn(piki,'int Piki::pcMoveFollowerRoute('),fn(crowd,'void ActCrowd::pcResetFollowerRecovery('),fn(crowd,'bool ActCrowd::pcRecoverFollower(')]
exec_body=fn(crowd,'int ActCrowd::exec(')
start=exec_body.index('\tif (plateDist2D < C_PIKI_PARM(mPiki, mFormationSlipRange))')
end=exec_body.index('\n\tSTACK_PAD_STRUCT(3);',start)
retention=exec_body[start:end].replace('return ACTOUT_Fail;','return false;')
funcs.append('bool ActCrowd::testFormationRetention(float plateDist2D){'+retention+'return true;}')
Path(sys.argv[1]).write_text(cpp.replace('FUNCTIONS','\n'.join(funcs)),encoding='utf-8');print('Generated actual crossing, route setup and follower recovery fixture')
