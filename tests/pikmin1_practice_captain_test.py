"""Run actual captain visual sampling with controlled cached animation leaves."""
from pathlib import Path
import sys
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
fixture=r'''
#pragma once
#include "nectar_net/replication.h"
#include <cmath>
#include <cstddef>
struct Vec {float x=0,y=0,z=0;void set(float a,float b,float c){x=a;y=b;z=c;}void normalise(){float n=std::sqrt(x*x+y*y+z*z);x/=n;y/=n;z/=n;}Vec operator-(const Vec&o)const{return{x-o.x,y-o.y,z-o.z};}};
using Vector3f=Vec;
struct Matrix {float mMtx[4][4]{};void makeIdentity(){for(int i=0;i<4;++i)for(int j=0;j<4;++j)mMtx[i][j]=i==j?1.0f:0.0f;}void setTranslation(const Vec&v){mMtx[0][3]=v.x;mMtx[1][3]=v.y;mMtx[2][3]=v.z;}};
struct Data {int mTotalFrameCount=32;};
struct AnimInfo {AnimInfo*mChild=nullptr,*mNext=nullptr;Data*mData=nullptr;};
struct AnimMgr {AnimInfo mAnimList;};
constexpr int ANIMSTATE_Inactive=0;
struct PaniPikiAnimator {AnimMgr*mMgr=nullptr;AnimInfo*mAnimInfo=nullptr;int mCurrentAnimID=0,mCurrentKeyIndex=1,mPlayState=1,mMotionIdx=3;void*mListener=reinterpret_cast<void*>(1);float mAnimationCounter=0;};
struct Navi {struct {Vec t;}mSRT;struct{PaniPikiAnimator mUpperAnimator,mLowerAnimator;}mNaviAnimMgr;
 float mHealth=0;bool mIsCursorVisible=false;Vec mCursorWorldPos,mCursorPosition,mCursorTargetPosition;Matrix mPcCursorMtx;
 bool pcCoopVisualValidate(const nectar::net::CaptainState&)const;void pcCoopVisualApply(const nectar::net::CaptainState&);};
'''
(out/'Navi.h').write_text(fixture,encoding='utf-8');(out/'MapMgr.h').write_text('#pragma once\n')
(out/'practice-captain-test.cpp').write_text(r'''
#include "Navi.h"
#include <cstdio>
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
 std::puts(failures?"CAPTAIN VISUAL FAIL":"CAPTAIN VISUAL PASS");return failures?1:0;
}
''',encoding='utf-8')
print('Generated actual captain visual fixture',out)
