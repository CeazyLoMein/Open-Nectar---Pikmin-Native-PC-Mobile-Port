#include "Navi.h"
#include "MapMgr.h"
#include "nectar_net/replication.h"
#include <algorithm>
namespace {
AnimInfo* sampleAsset(AnimMgr* manager, unsigned id) {
    if (!manager || id>=1024) return nullptr;
    auto* info=static_cast<AnimInfo*>(manager->mAnimList.mChild);
    for (unsigned i=0; info && i<id; ++i) info=static_cast<AnimInfo*>(info->mNext);
    return info && info->mData && info->mData->mTotalFrameCount>0 ? info : nullptr;
}
bool validSample(const PaniPikiAnimator& a,unsigned id,float frame) {
    auto* info=sampleAsset(a.mMgr,id);
    return info && frame<=info->mData->mTotalFrameCount;
}
void sample(PaniPikiAnimator& a,unsigned id,float frame) {
    a.mAnimInfo=sampleAsset(a.mMgr,id); a.mCurrentAnimID=id;
    a.mAnimationCounter=std::min(frame,float(a.mAnimInfo->mData->mTotalFrameCount-1));
    a.mListener=nullptr; a.mCurrentKeyIndex=-1; a.mPlayState=ANIMSTATE_Inactive; a.mMotionIdx=-1;
}
}
bool Navi::pcCoopVisualValidate(const nectar::net::CaptainState& s) const {
    return validSample(mNaviAnimMgr.mUpperAnimator,s.upperAnimation,s.upperFrame)
        && validSample(mNaviAnimMgr.mLowerAnimator,s.lowerAnimation,s.lowerFrame);
}
void Navi::pcCoopVisualApply(const nectar::net::CaptainState& s) {
    sample(mNaviAnimMgr.mUpperAnimator,s.upperAnimation,s.upperFrame);
    sample(mNaviAnimMgr.mLowerAnimator,s.lowerAnimation,s.lowerFrame);
    mHealth=s.health; mIsCursorVisible=s.cursorVisible;
    mCursorWorldPos.set(s.cursor.x,s.cursor.y,s.cursor.z);
    mCursorPosition=mCursorWorldPos-mSRT.t; mCursorTargetPosition=mCursorPosition;
    // The first scene is flat. Build a pure presentation cursor basis; never
    // run guest targeting, terrain mutation, locks or whistle gameplay.
    Vector3f forward=mCursorPosition; forward.y=0;
    if (forward.x*forward.x+forward.z*forward.z<0.000001f) forward.set(0,0,1); else forward.normalise();
    mPcCursorMtx.makeIdentity();
    mPcCursorMtx.mMtx[0][0]=forward.z; mPcCursorMtx.mMtx[2][0]=-forward.x;
    mPcCursorMtx.mMtx[0][2]=forward.x; mPcCursorMtx.mMtx[2][2]=forward.z;
    mPcCursorMtx.setTranslation(mCursorWorldPos);
}
