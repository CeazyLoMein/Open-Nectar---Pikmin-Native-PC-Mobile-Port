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
HEADER
struct Vector3f {float x=0,y=0,z=0;Vector3f()=default;Vector3f(float a,float b,float c):x(a),y(b),z(c){}
Vector3f operator-(Vector3f p)const{return {x-p.x,y-p.y,z-p.z};}float length()const{return std::sqrt(x*x+y*y+z*z);}float normalise(){float d=length();if(d>0){x/=d;y/=d;z/=d;}return d;}void set(float a,float b,float c){x=a;y=b;z=c;}};
enum {STANDTYPE_Ground,STANDTYPE_TekiPlatform,STANDTYPE_Platform,STANDTYPE_Air,PIKISTATE_Normal=20,PIKISTATE_Drown,Red=0,Blue=2};
namespace PikiMode {enum {FormationMode,CarryMode,AttackMode,FreeMode};}
enum {PIKIANIM_Run,PIKIANIM_Walk};int PaniMotionInfo(int x){return x;}
bool better=true,det=false,coop=false,vs=false,blues=true;
bool pc_settings_get_better_pathfinding(){return better;}bool pc_netplay_deterministic(){return det;}bool pc_coop_active(){return coop;}bool pc_vs_active(){return vs;}bool pc_settings_get_blues_only_water(){return blues;}
struct System {float dt=1.f/60.f;float getFrameTime(){return dt;}}sys;System*gsys=&sys;
struct Movie {bool mIsActive=false;}movie;struct Game {Movie*mMoviePlayer=&movie;}gameflow;
struct State {bool end=false;bool inDayEnd(){return end;}}state;State*playerState=&state;
struct Navi {struct {Vector3f t;}mSRT;Vector3f mPlatformAdjustDelta;bool alive=true,stick=false,mIsCStickNeutral=true,mIsInWater=false;int stand=STANDTYPE_Ground;
bool isAlive(){return alive;}bool isStickTo(){return stick;}int getStandType(){return stand;}
PcFollowTrail mPcFollowTrail;float mPcFollowRouteCooldown=0;void pcUpdateFollowTrail();bool pcTakeFollowerRouteBudget();};
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
WayPoint*getWayPoint(int,int index){return index==0?&first:index==1?&last:nullptr;}
}route;Route*routeMgr=&route;
struct Sphere {Sphere(Vector3f,float){}}; struct Tube {Tube(Vector3f,Vector3f,float,float){}bool collide(Sphere&,Vector3f&,float&){return false;}};

struct Piki {struct {Vector3f t;}mSRT;Vector3f mPlatformAdjustDelta,mTargetVelocity;Navi*mNavi=nullptr;
bool alive=true,holding=false,damaged=false,stick=false;int state=PIKISTATE_Normal,mMode=PikiMode::FormationMode,mColor=Red,stand=STANDTYPE_Ground;
bool isAlive(){return alive;}int getState(){return state;}bool isHolding(){return holding;}bool isDamaged(){return damaged;}bool isStickTo(){return stick;}int getStandType(){return stand;}
Buffer buffer[8]={};Buffer*mPathBuffers=buffer;int mRouteHandle=0;bool mUseAsyncPathfinding=false,mIsRetryPathfind=false;
int mNumRoutePoints=0,mRouteSourceIndex=-1,mRouteDestinationIndex=-1,mCurrRoutePoint=-1,sharedCalls=0,moves=0,moveResult=2;
Vector3f mRouteStartPos,mRouteGoalPos,mSplineControlPts[4];
bool initRouteTrace(const Vector3f&,bool,bool=false);
int findRoute(int,int,bool,bool){++sharedCalls;return 2;}
Vector3f crGetPoint(int){return {};}float crGetRadius(int){return 1;}bool crPointOpen(int){return true;}void crMakeRefs(){}
int pcMoveFollowerRoute();void setSpeed(float,Vector3f d){mTargetVelocity={d.x*100,d.y*100,d.z*100};++moves;}void startMotion(int,int){}
};
struct ActCrowd {Piki*mPiki;PcFollowerProgress mPcFollowerProgress;bool mPcFollowingTrail=false,mPcLaneBlocked=false,mPcRecoveryRoute=false,mIsTripping=false,mIsWaiting=false;
float mPcRecoveryRouteAge=0,mLostChildTimer=0;Vector3f mPcRecoveryGoal;
void pcResetFollowerRecovery();bool pcRecoverFollower();};
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
for(int i=0;i<7;++i)n.pcUpdateFollowTrail();check(n.pcTakeFollowerRouteBudget(),"captain budget replenishes in simulation time");
Piki k;k.mNavi=&n;n.mSRT.t={200,0,0};route.first.mPosition={0,0,0};route.last.mPosition={200,0,0};route.last.mIndex=1;
check(k.initRouteTrace(n.mSRT.t,false,true)&&pf.calls==1&&k.sharedCalls==0&&!k.mUseAsyncPathfinding&&!pf.ignoredClosed,"recovery uses synchronous direct route and respects gates");
route.missingStart=true;check(!k.initRouteTrace(n.mSRT.t,false,true),"missing start waypoint safe failure");route.missingStart=false;
route.missingEnd=true;check(!k.initRouteTrace(n.mSRT.t,false,true),"missing destination safe failure");route.missingEnd=false;
route.last.mIsOpen=false;check(!k.initRouteTrace(n.mSRT.t,false,true),"closed endpoint rejected");route.last.mIsOpen=true;
route.last.mPosition.y=100;check(!k.initRouteTrace(n.mSRT.t,false,true),"waypoint on another floor rejected");route.last.mPosition.y=0;
route.first.mPosition.x=190;check(!k.initRouteTrace(n.mSRT.t,false,true),"far route entry rejected");route.first.mPosition.x=0;
route.last.mIndex=99;check(!k.initRouteTrace(n.mSRT.t,false,true),"invalid endpoint index rejected before search");route.last.mIndex=1;
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
wait(a);check(!a.mPcRecoveryRoute,"directly below captain does not count as safely reunited");n.mSRT.t={200,0,0};
for(int mode:{PikiMode::CarryMode,PikiMode::AttackMode,PikiMode::FreeMode}){a.pcResetFollowerRecovery();k.mMode=mode;calls=pf.calls;check(!wait(a)&&pf.calls==calls,"working/attacking/idle Pikmin untouched");}k.mMode=PikiMode::FormationMode;
for(bool*flag:{&k.holding,&k.damaged,&k.stick,&a.mIsTripping,&state.end,&movie.mIsActive,&det,&coop,&vs}){a.pcResetFollowerRecovery();*flag=true;calls=pf.calls;check(!wait(a)&&pf.calls==calls,"special states never trigger recovery route");*flag=false;}
a.pcResetFollowerRecovery();k.mTargetVelocity={0,0,0};calls=pf.calls;check(!wait(a)&&pf.calls==calls,"wide parked formation is not mistaken for a stuck follower");k.mTargetVelocity={50,0,0};
k.state=PIKISTATE_Drown;check(!wait(a),"drowning Pikmin never rescued by route cheat");k.state=PIKISTATE_Normal;
n.mIsInWater=true;check(!wait(a),"red follower waits ashore");n.mIsInWater=false;
better=false;calls=pf.calls;check(!wait(a)&&calls==pf.calls,"original behavior available with Better Pathfinding off");better=true;
a.pcResetFollowerRecovery();n.mPcFollowRouteCooldown=0;pf.blocked=true;before=pf.calls;wait(a,240);check(pf.calls-before<=2,"failed searches back off per follower");pf.blocked=false;
check(near(k.mSRT.t.x,0)&&near(k.mSRT.t.y,0),"no recovery path teleports Pikmin");
std::printf("%d P1 crossing/route recovery scenarios; %d failures\n",checks,failures);return failures?1:0;
}
"""
cpp=cpp.replace('HEADER',(root/'games/pikmin1/pc_port/pc_follow_trail.h').read_text(encoding='utf-8'))
funcs=[fn(nav,'void Navi::pcUpdateFollowTrail('),fn(nav,'bool Navi::pcTakeFollowerRouteBudget('),fn(piki,'bool Piki::initRouteTrace('),fn(piki,'int Piki::pcMoveFollowerRoute('),fn(crowd,'void ActCrowd::pcResetFollowerRecovery('),fn(crowd,'bool ActCrowd::pcRecoverFollower(')]
Path(sys.argv[1]).write_text(cpp.replace('FUNCTIONS','\n'.join(funcs)),encoding='utf-8');print('Generated actual crossing, route setup and follower recovery fixture')
