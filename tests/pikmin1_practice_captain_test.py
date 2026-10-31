"""Run actual captain visual sampling with controlled cached animation leaves."""
from pathlib import Path
import sys
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
fixture=r'''
#pragma once
#include "nectar_net/replication.h"
#include <cmath>
#include <cstddef>
#include "NaviState.h"
#include "NaviMgr.h"
struct Vec {float x=0,y=0,z=0;void set(float a,float b,float c){x=a;y=b;z=c;}void normalise(){float n=std::sqrt(x*x+y*y+z*z);x/=n;y/=n;z/=n;}Vec operator-(const Vec&o)const{return{x-o.x,y-o.y,z-o.z};}};
using Vector3f=Vec;
struct Matrix {float mMtx[4][4]{};void makeIdentity(){for(int i=0;i<4;++i)for(int j=0;j<4;++j)mMtx[i][j]=i==j?1.0f:0.0f;}void setTranslation(const Vec&v){mMtx[0][3]=v.x;mMtx[1][3]=v.y;mMtx[2][3]=v.z;}};
struct Data {int mTotalFrameCount=32;};
struct AnimInfo {AnimInfo*mChild=nullptr,*mNext=nullptr;Data*mData=nullptr;};
struct AnimMgr {AnimInfo mAnimList;};
constexpr int ANIMSTATE_Inactive=0;
struct PaniPikiAnimator {AnimMgr*mMgr=nullptr;AnimInfo*mAnimInfo=nullptr;int mCurrentAnimID=0,mCurrentKeyIndex=1,mPlayState=1,mMotionIdx=3;void*mListener=reinterpret_cast<void*>(1);float mAnimationCounter=0;};
struct Navi {struct {Vec t;}mSRT;struct{PaniPikiAnimator mUpperAnimator,mLowerAnimator;}mNaviAnimMgr;
 int mNaviID=0;NaviMachine machine;NaviMachine*mStateMachine=&machine;NaviGatherState gatherState;
 NaviProp props;int mWhistleCircleMode=0;float mWhistleTimer=0,mWhistleRadiusFrac=0;
 bool mPcCoopWhistleActive=false,mPcCoopWhistleShown=false;float mPcCoopWhistleRadius=0;
 NaviGatherState*getCurrState(){return &gatherState;}
 void pcCoopWhistleCapture(nectar::net::CaptainState&);bool pcCoopWhistleRadius(float&)const;void pcCoopWhistleEffects();
 float mHealth=0;bool mIsCursorVisible=false;Vec mCursorWorldPos,mCursorPosition,mCursorTargetPosition;Matrix mPcCursorMtx;
 bool pcCoopVisualValidate(const nectar::net::CaptainState&)const;void pcCoopVisualApply(const nectar::net::CaptainState&);};
'''
(out/'NaviState.h').write_text("""#pragma once
enum {NAVISTATE_Gather=2};
struct NaviMachine {int id=0;int getCurrID(void*) {return id;}};
struct NaviGatherState {bool mWhistleEffectsStopped=false;};
""",encoding='utf-8')
(out/'NaviMgr.h').write_text("""#pragma once
struct NaviProp {float mWhistleExpandTime=.5f,mWhistleMinRadius=20,mWhistleMaxRadius=180;};
#define C_NAVI_PARM(n,p) ((n)->props.p)
#define NAVI_WHISTLE_MAX_RADIUS(n) ((n)->props.mWhistleMaxRadius)
""",encoding='utf-8')
(out/'UtEffect.h').write_text("""#pragma once
#include "Navi.h"
struct EffectParm {explicit EffectParm(const Vector3f&) {}};
namespace KandoEffect {enum {NaviWhistle0=1,NaviWhistle1=2,NaviFue0=7,NaviFue1=8};}
inline int emitted[9]={},killed[9]={};
struct UtEffectMgr {static void cast(int id,const EffectParm&) {++emitted[id];}static void kill(int id) {++killed[id];}};
inline UtEffectMgr effectSeam;
inline UtEffectMgr*utEffectMgr=&effectSeam;
""",encoding='utf-8')
(out/'Navi.h').write_text(fixture,encoding='utf-8');(out/'MapMgr.h').write_text('#pragma once\n')
(out/'practice-captain-test.cpp').write_text(r'''
#include "Navi.h"
#include <cstdio>
#include "UtEffect.h"
bool guest=false;
bool pc_coop_world_has_guest(){return guest;}
bool pc_coop_world_guest_active(){return guest;}
int failures=0;void check(bool ok,const char*m){if(!ok){++failures;std::printf("FAIL %s\n",m);}}
int main(){
 Data data;AnimInfo loaded,missing;loaded.mData=&data;loaded.mNext=&missing;AnimMgr manager;manager.mAnimList.mChild=&loaded;
 Navi n;n.mNaviAnimMgr.mUpperAnimator.mMgr=n.mNaviAnimMgr.mLowerAnimator.mMgr=&manager;
 nectar::net::CaptainState s;s.health=75;s.cursor={12,1,20};s.upperFrame=32;s.lowerFrame=3;s.cursorVisible=1;
 check(n.pcCoopVisualValidate(s),"locally cached captain samples accepted");
 auto bad=s;bad.lowerAnimation=1;check(!n.pcCoopVisualValidate(bad),"unloaded lower channel rejected without lazy asset IO");
 bad=s;bad.upperFrame=33;check(!n.pcCoopVisualValidate(bad),"out-of-resource frame refused");
 bad=s;bad.upperAnimation=1024;check(!n.pcCoopVisualValidate(bad),"animation index bounded");
 n.mSRT.t={2,0,5};n.pcCoopVisualApply(s);
 check(n.mHealth==75&&n.mIsCursorVisible&&n.mCursorPosition.x==10&&n.mCursorPosition.z==15,"host health/cursor applied to local actor");
 check(n.mNaviAnimMgr.mUpperAnimator.mAnimationCounter==31&&n.mNaviAnimMgr.mLowerAnimator.mAnimationCounter==3,"end marker clamped and two poses retained");
 check(!n.mNaviAnimMgr.mUpperAnimator.mListener&&n.mNaviAnimMgr.mLowerAnimator.mPlayState==0&&n.mNaviAnimMgr.mUpperAnimator.mMotionIdx==-1,"guest samples cannot emit gameplay animation events");
 check(n.mPcCursorMtx.mMtx[0][3]==12&&n.mPcCursorMtx.mMtx[2][3]==20,"cursor presentation matrix rebuilt");
 s.cursor={2,0,5};n.pcCoopVisualApply(s);check(std::isfinite(n.mPcCursorMtx.mMtx[0][0]),"zero cursor vector cannot produce NaN");
 n.machine.id=NAVISTATE_Gather;n.mWhistleCircleMode=1;n.mWhistleTimer=.25f;
 n.pcCoopWhistleCapture(s);check(s.whistleActive==1&&s.whistleRadius==100,"actual host capture uses current whistle radius");
 n.gatherState.mWhistleEffectsStopped=true;n.pcCoopWhistleCapture(s);check(!s.whistleActive,"finished native whistle publishes stop");
 n.gatherState.mWhistleEffectsStopped=false;n.machine.id=0;n.pcCoopWhistleCapture(s);check(!s.whistleActive&&s.whistleRadius==0,"leaving gather cannot leave guest ring active");
 guest=true;s.whistleActive=1;s.whistleRadius=85;n.pcCoopVisualApply(s);
 check(n.mPcCoopWhistleActive&&n.mPcCoopWhistleRadius==85,"whole actual adapter applies wire whistle fields alongside animation and cursor");
 float radius=0;check(n.pcCoopWhistleRadius(radius)&&radius==85,"guest rendering receives authoritative radius");
 n.pcCoopWhistleEffects();n.pcCoopWhistleEffects();check(emitted[1]==1&&emitted[7]==1,"same guest state cannot repeatedly allocate whistle effects");
 Navi partner;partner.mNaviID=1;partner.mNaviAnimMgr.mUpperAnimator.mMgr=partner.mNaviAnimMgr.mLowerAnimator.mMgr=&manager;
 partner.pcCoopVisualApply(s);partner.pcCoopWhistleEffects();check(emitted[2]==1&&emitted[8]==1,"second captain uses independent original effect slots");
 s.whistleActive=0;n.pcCoopVisualApply(s);n.pcCoopWhistleEffects();n.pcCoopWhistleEffects();
 check(killed[1]==1&&killed[7]==1&&killed[2]==0&&killed[8]==0,"release kills own guest effects once without muting partner visuals");
 guest=false;radius=999;check(!n.pcCoopWhistleRadius(radius)&&radius==999,"solo and host retain original render radius path");
 std::puts(failures?"CAPTAIN VISUAL FAIL":"CAPTAIN VISUAL PASS");return failures?1:0;
}
''',encoding='utf-8')
print('Generated actual captain visual fixture',out)
