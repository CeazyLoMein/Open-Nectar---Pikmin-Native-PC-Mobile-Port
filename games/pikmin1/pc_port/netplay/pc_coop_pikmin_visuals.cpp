// Host-driven guest Pikmin presentation. Reuse already-created dormant model
// slots; never register live actors, execute AI/animation events or replay death.
#include "PikiMgr.h"
#include "Graphics.h"
#include "Shape.h"
#include "Material.h"
#include "netplay/pc_coop_world_hooks.h"
#include "nectar_net/pikmin_replication.h"
#include <algorithm>
#include <set>

namespace {
// Unlike AnimMgr::findAnim, this cannot lazily load an asset from packet data.
// Required animation assets must already be loaded during trusted scene setup.
AnimInfo* loadedAnimation(AnimMgr* manager, unsigned index)
{
    if (!manager || index >= 1024) return nullptr;
    AnimInfo* info = static_cast<AnimInfo*>(manager->mAnimList.mChild);
    for (unsigned i = 0; info && i < index; ++i) info = static_cast<AnimInfo*>(info->mNext);
    return info && info->mData && info->mData->mTotalFrameCount > 0 ? info : nullptr;
}
bool visualSample(AnimMgr* manager, unsigned index, float frame)
{
    AnimInfo* info = loadedAnimation(manager, index);
    // The engine can publish the exact end marker. Draw its last valid frame.
    return info && frame <= static_cast<float>(info->mData->mTotalFrameCount);
}
void applySample(PaniPikiAnimator& animator, AnimInfo* info, unsigned index, float frame)
{
    animator.mListener = nullptr;
    animator.mCurrentKeyIndex = -1;
    animator.mPlayState = ANIMSTATE_Inactive;
    animator.mMotionIdx = -1; // raw animation sample, never a gameplay motion/FSM
    animator.mCurrentAnimID = static_cast<int>(index);
    animator.mAnimInfo = info;
    animator.mAnimationCounter = std::min(frame, static_cast<float>(info->mData->mTotalFrameCount - 1));
}
}

bool PikiMgr::pcCoopVisualSlots(std::vector<ViewPiki*>& output)
{
    if (!pc_coop_world_has_guest() || mNumObjects != 0 || mMaxElements <= 0 || mMaxElements > 510
        || !mEntryStatus || !mObjectList) return false;
    std::vector<ViewPiki*> pending;
    std::set<ViewPiki*> unique;
    pending.reserve(static_cast<std::size_t>(mMaxElements));
    for (int i = 0; i < mMaxElements; ++i) {
        if (mEntryStatus[i] != -1 || !mObjectList[i]) return false;
        // PikiMgr::createObject always constructs ViewPiki, not arbitrary actors.
        ViewPiki* model = static_cast<ViewPiki*>(mObjectList[i]);
        if (!unique.insert(model).second || !model->pcCoopVisualReady()) return false;
        pending.push_back(model);
    }
    output.swap(pending);
    return true;
}

bool PikiMgr::pcCoopVisualSlotsValid(const std::vector<ViewPiki*>& slots) const
{
    if (!pc_coop_world_has_guest() || mNumObjects != 0 || mMaxElements <= 0
        || slots.size() != static_cast<std::size_t>(mMaxElements) || !mEntryStatus || !mObjectList) return false;
    for (int i = 0; i < mMaxElements; ++i) {
        if (mEntryStatus[i] != -1 || mObjectList[i] != slots[static_cast<std::size_t>(i)]) return false;
    }
    return true;
}

bool ViewPiki::pcCoopVisualReady() const
{
    if (!pikiMgr || !mPikiAnimMgr.mUpperAnimator.mContext || !mPikiAnimMgr.mLowerAnimator.mContext) return false;
    for (int i = 0; i < 3; ++i) {
        const auto* shape = PikiShapeObject::_instances[i];
        if (!shape || !shape->mShape || !shape->mShape->mMaterialList || !shape->mAnimMgr || shape->mShape->mJointCount <= 6
            || !pikiMgr->mLeafModel[i]) return false;
    }
    return true;
}

bool ViewPiki::pcCoopVisualValidate(const nectar::net::PikminState& value) const
{
    if (!nectar::net::validPikminState(value) || value.color >= 3 || !pcCoopVisualReady()) return false;
    AnimMgr* animations = PikiShapeObject::_instances[value.color]->mAnimMgr;
    return visualSample(animations, value.upperAnimation, value.upperFrame)
        && visualSample(animations, value.lowerAnimation, value.lowerFrame);
}

void ViewPiki::pcCoopVisualApply(const nectar::net::PikminState& value)
{
    // Caller validates EVERY sample and reserves ALL maps before this commit.
    // No normal initColor/changeShape/setFlower: those can apply gameplay rules.
    mPikiShape = PikiShapeObject::_instances[value.color];
    mPikiAnimMgr.changeContext(&mPikiShape->mAnimatorB, &mPikiShape->mAnimatorA);
    applySample(mPikiAnimMgr.mUpperAnimator, loadedAnimation(mPikiShape->mAnimMgr, value.upperAnimation), value.upperAnimation, value.upperFrame);
    applySample(mPikiAnimMgr.mLowerAnimator, loadedAnimation(mPikiShape->mAnimMgr, value.lowerAnimation), value.lowerAnimation, value.lowerFrame);
    mSRT.t.set(value.position.x, value.position.y, value.position.z);
    mSRT.r.set(0.0f, value.faceDirection, 0.0f);
    mSRT.s.set(1.0f, 1.0f, 1.0f);
    mLastPosition = mSRT.t;
    mColor = value.color; mHappa = value.maturity;
    mHappaModel = pikiMgr->mLeafModel[value.maturity];
    mCurrentColour = pikiColors[value.color];
}

void ViewPiki::pcCoopVisualDraw(Graphics& gfx)
{
    if (!gfx.mCamera || !mPikiShape || !gfx.mCamera->isPointVisible(mSRT.t, 40.0f)) return;
    // No mMode/FSM/collision/attachment/look/effect updates. Host pose samples
    // are installed before each shared-shape draw; render rate never advances them.
    Matrix4f world, view;
    world.makeSRT(mSRT.s, mSRT.r, mSRT.t);
    gfx.mCamera->mLookAtMtx.multiplyTo(world, view);
    mPikiAnimMgr.updateContext();
    mPikiShape->mShape->updateAnim(gfx, view, nullptr, nullptr);
    mPikiShape->mShape->mMaterialList->setColour(mCurrentColour);
    const GXColor white = {255, 255, 255, 255};
    if (!pc_hd_model_draw_skinned(gfx, mPikiShape->mShape, hdPikiModel(), white))
        mPikiShape->mShape->drawshape(gfx, *gfx.mCamera, nullptr);
    gfx.useMatrix(mPikiShape->mShape->getAnimMatrix(6), 0);
    if (!pc_hd_model_draw_rigid(gfx, mPikiShape->mShape->getAnimMatrix(6), hdHappaModel(), white))
        mHappaModel->drawshape(gfx, *gfx.mCamera, nullptr);
}
