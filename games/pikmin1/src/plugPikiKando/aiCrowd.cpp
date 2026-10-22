#include "CPlate.h"
#include "DebugLog.h"
#include "GameStat.h"
#include "MoviePlayer.h"
#include "Navi.h"
#include "NaviMgr.h"
#include "PikiAI.h"
#include "PikiInfo.h"
#include "PikiMgr.h"
#include "PlayerState.h"
#include "ViewPiki.h"
#include "gameflow.h"
#if defined(PIKI_PC_PORT)
#include "MapCode.h"
#include "MapMgr.h"
#include "PikiState.h"
#include "pc_coop.h"
#include "netplay/pc_netplay_det.h"
#include "pc_follow_report.h"
#include "settings/pc_settings.h"
#endif
#include <stdlib.h>
#include <cmath>
#if defined(PIKI_PC_PORT)
#include "settings/pc_settings.h"
#endif

static bool newVer = true;

/**
 * @todo: Documentation
 * @note UNUSED Size: 00009C
 */
DEFINE_ERROR(20)

/**
 * @todo: Documentation
 * @note UNUSED Size: 0000F0
 */
DEFINE_PRINT("aiCrowd")

/**
 * @todo: Documentation
 */
ActCrowd::ActCrowd(Piki* piki)
    : Action(piki, true)
{
	setName("crowd");
	mPlateMgr     = nullptr;
	mCPlateSlotID = -1;
	mSelectAction = new ActBoreSelect(piki);
}

/**
 * @todo: Documentation
 */
void ActCrowd::inform(int slotID)
{
	mCPlateSlotID = slotID;
}

/**
 * @todo: Documentation
 */
void ActCrowd::startSort()
{
	mState = STATE_Sort;
	mSelectAction->stop();
}

/**
 * @todo: Documentation
 */
void ActCrowd::init(Creature* target)
{
#if defined(PIKI_PC_PORT)
    pcResetFollowerRecovery();
#endif
	mMode      = 5;
	mPrevMode        = 5;
	mNearSlotCounter = 0;
	mIsWaiting = false;
	mWasWaiting      = false;
	if (target->mObjType != OBJTYPE_Navi) {
		PRINT("target is not navi (%d)\n", target->mObjType);
	}

	Navi* navi    = static_cast<Navi*>(target);
#if defined(PIKI_PC_PORT)
    const Vector3f returnDelta=navi->mSRT.t-mPiki->mSRT.t;
    mPcReturning=returnDelta.length()>100.0f;
#endif
	mPlateMgr     = navi->mPlateMgr;
	mCPlateSlotID = mPlateMgr->getSlot(mPiki, this);
	if (mCPlateSlotID == -1) {
		PRINT("slot id is -1\n");
	} else {
		navi->incPlatePiki();
	}

	if (!mPiki->isHolding()) {
		mPiki->startMotion(PaniMotionInfo(PIKIANIM_Run), PaniMotionInfo(PIKIANIM_Run));
	}
	mPiki->unsetPastel();
	mHasRequestedNewSlot = false;
	_35              = false;
	_36              = false;
	mState           = STATE_Unk0;
	mTripLoopCounter = 0;
	mTravelDistance      = 0.0f;
	mIsTripping      = false;
	GameStat::formationPikis.inc(mPiki->mColor);
	GameStat::workPikis.dec(mPiki->mColor);
	GameStat::update();
	mHasRoute = false;
	mOdometer.start(2.0f, 20.0f);
}

/**
 * @todo: Documentation
 * @note UNUSED Size: 000054
 */
void ActCrowd::initRouteMove()
{
	mHasRoute = false;
	if (mPiki->initRouteTraceDynamic(mPiki->mNavi)) {
		PRINT("OKOK!\n");
		mHasRoute = true;
	}
	mLostChildTimer = 5.0f;
}

/**
 * @todo: Documentation
 * @note UNUSED Size: 000044
 */
void ActCrowd::exeRouteMove()
{
	if (mPiki->moveRouteTraceDynamic(1.0f) != 2) {
		PRINT("THE END\n");
		mHasRoute = false;
	}
}

/**
 * @todo: Documentation
 * @note UNUSED Size: 00006C
 */
void ActCrowd::setFormed()
{
	mState = STATE_Formed;
	if (mPiki->hasBomb() && !playerState->mDemoFlags.isFlag(DEMOFLAG_GrabFirstBomb)) {
		#if defined(PIKI_PC_PORT)
		if (mPiki->mNavi) naviMgr->setMovieNavi(mPiki->mNavi);
#endif
		playerState->mDemoFlags.setFlag(DEMOFLAG_GrabFirstBomb, mPiki);
	}
}

/**
 * @todo: Documentation
 */
void ActCrowd::procCollideMsg(Piki*, MsgCollide* msg)
{
	if (mState == STATE_Sort) {
		return;
	}

	Piki* collider = static_cast<Piki*>(msg->mEvent.mCollider);
	if (collider->mObjType == OBJTYPE_Piki) {
		if (collider->mMode == PikiMode::FormationMode && mState == STATE_Unk0) {
			ActCrowd* colliderAction = static_cast<ActCrowd*>(collider->mActiveAction->getCurrAction());
			if (colliderAction && colliderAction->mState == STATE_Formed) {
				pikiInfo->addFormationPiki();
				setFormed();
			}
		}

		_36 = true;
	}
}

/**
 * @todo: Documentation
 */
void ActCrowd::procWallMsg(Piki*, MsgWall* msg)
{
	if (mCPlateSlotID != -1) {
		mWallNormal = msg->mWallPlane->mNormal;
		_35 = true;
	}
}

/**
 * @todo: Documentation
 */
void ActCrowd::procAnimMsg(Piki* piki, MsgAnim* msg)
{
	switch (msg->mKeyEvent->mEventType) {
	case KEY_Action1:
	{
		if (mIsTripping) {
			piki->mVelocity.set(0.0f, 0.0f, 0.0f);
			piki->mTargetVelocity.set(0.0f, 0.0f, 0.0f);
		}
		break;
	}
	case KEY_LoopEnd:
	{
		if (mIsTripping) {
			mTripLoopCounter--;
			if (mTripLoopCounter <= 0) {
				piki->mPikiAnimMgr.finishMotion(piki);
			}
		}
		break;
	}
	case KEY_Finished:
	{
		if (mIsTripping) {
			mIsTripping = false;
			piki->startMotion(PaniMotionInfo(PIKIANIM_Walk), PaniMotionInfo(PIKIANIM_Walk));
		}
		break;
	}
	}
}

/**
 * @todo: Documentation
 */
void ActCrowd::cleanup()
{
#if defined(PIKI_PC_PORT)
    pcResetFollowerRecovery();
#endif
	if (mPiki->mRouteHandle) {
		routeMgr->getPathFinder('test')->releaseHandle(mPiki->mRouteHandle);
	}
	if (mCPlateSlotID != -1) {
		int count = mPiki->getCnt();
		mPiki->mNavi->decPlatePiki();
		mPlateMgr->releaseSlot(mPiki, mCPlateSlotID);
		if (count > 0 && count == mPiki->getCnt()) {
			ERROR("smart ptr err %d\n", mPiki->getCnt());
		}
	}
	pikiInfo->subFormationPiki();
	mPlateMgr     = nullptr;
	mCPlateSlotID = -1;
	GameStat::workPikis.inc(mPiki->mColor);
	GameStat::formationPikis.dec(mPiki->mColor);
	GameStat::update();
}

/**
 * @todo: Documentation
 */
#if defined(PIKI_PC_PORT)
/**
 * @brief ¿Hay agua cerca, entre el Pikmin y su capitán?
 *
 * Sondea el suelo en línea recta hacia el capitán hasta kShoreDistance: así
 * solo se paran los que ya están junto a la orilla, no los que vienen de
 * lejos.
 */
// Better Pathfinding: protect static terrain/platform edges, keep followers
// on a recent captain crossing lane, then try bounded route recovery when
// separated followers stop moving. Optional rescue is a separate final fallback.
// Moving platforms and commanded swarms retain ordinary behavior.
void ActCrowd::pcProtectFormationEdge(Vector3f& slot)
{
    mPcFollowingTrail=false;
    mPcLaneBlocked=false;
    if (!pc_settings_get_better_pathfinding() || !mPiki->mNavi || !mapMgr
        || mPiki->mNavi->mCStick.length()>0.05f || pc_netplay_deterministic() || pc_coop_active() || pc_vs_active()
        || mPiki->getStandType() == STANDTYPE_Air || mPiki->mNavi->getStandType() == STANDTYPE_Air
        || mPiki->mPlatformAdjustDelta.length()>0.5f || mPiki->mNavi->mPlatformAdjustDelta.length()>0.5f) return;
    PcFollowTrail::Point goal;
    const Vector3f position=mPiki->mSRT.t, leader=mPiki->mNavi->mSRT.t;
    // The captain deliberately dropped to lower ground. Leave the original
    // formation target untouched so followers may walk off after them.
    if (leader.y < position.y - 25.0f) return;
    const bool trail=mPiki->mNavi->mPcFollowTrail.target({position.x,position.y,position.z,false},
        {leader.x,leader.y,leader.z,false},mPiki->getStandType()!=STANDTYPE_Ground,goal);
    if (trail) slot.set(goal.x,goal.y,goal.z);
    const Vector3f here = mPiki->mSRT.t;
    const Vector3f captain = mPiki->mNavi->mSRT.t;
    auto safeStep = [&](const Vector3f& target) {
        Vector3f direction=target-here;direction.y=0.0f;
        const f32 distance=direction.normalise();
        Vector3f step=here+direction*(distance<36.0f?distance:36.0f);
        step.y=here.y+(target.y-here.y)*(distance>36.0f?36.0f/distance:1.0f);
        return mPiki->pcFollowerSegmentClear(step);
    };
    const bool redirected=!safeStep(slot);
    if (redirected) {
        const bool towardCaptain=safeStep(captain);
        slot=towardCaptain?captain:here;
        mPcLaneBlocked=!towardCaptain;
    }
    // On a recorded crossing, use the narrow lane without the normal lateral
    // circling/slot reassignment that would fan followers back over the edge.
    mPcFollowingTrail=trail||redirected;
}

void ActCrowd::pcResetFollowerRecovery()
{
    mPcFollowerProgress.reset();
    mPcStranded.reset();mPcReturnFailed=false;
    mPcFollowingTrail=false;
    mPcLaneBlocked=false;
    mPcRecoveryRoute=false;
    mPcReturning=false;
    mPcRecoveryRouteAge=0.0f;
}

bool ActCrowd::pcRecoverFollower()
{
    const f32 step=gsys->getFrameTime()>0.1f?0.1f:gsys->getFrameTime();
    if(mPcRescueCooldown>0)mPcRescueCooldown-=step>0?step:0;
    Navi* captain=mPiki->mNavi;
    if ((!pc_settings_get_better_pathfinding() && !pc_settings_get_stuck_follower_rescue()) || pc_netplay_deterministic() || pc_coop_active() || pc_vs_active()
        || !captain || captain->mCStick.length()>0.05f || !mPiki->isAlive() || mPiki->getState()!=PIKISTATE_Normal
        || mPiki->mMode!=PikiMode::FormationMode || mPiki->isHolding() || mPiki->isDamaged() || mPiki->isStickTo()
        || mPiki->getStandType()==STANDTYPE_Air || mPiki->mPlatformAdjustDelta.length()>0.5f
        || captain->mPlatformAdjustDelta.length()>0.5f || mIsTripping || playerState->inDayEnd()
        || (gameflow.mMoviePlayer && gameflow.mMoviePlayer->mIsActive)
        || (pc_settings_get_blues_only_water() && mPiki->mColor!=Blue && captain->mIsInWater)) {
        pcResetFollowerRecovery();return false;
    }
    const Vector3f here=mPiki->mSRT.t, goal=captain->mSRT.t;
    const Vector3f delta=goal-here;
    const bool separated=delta.x*delta.x+delta.z*delta.z>60.0f*60.0f || delta.y>25.0f || delta.y< -25.0f;
    if (!separated) {pcResetFollowerRecovery();return false;}
    const f32 dt=gsys->getFrameTime();
    // A legitimately parked wide formation is not stuck. Require actual
    // intended movement, a blocked lane, or separation onto another floor.
    const bool needsMove=mPcRecoveryRoute || mPiki->mTargetVelocity.length()>5.0f
        || mPcLaneBlocked || delta.y>25.0f || delta.y< -25.0f;
    if(delta.length()>160.0f || std::fabs(delta.y)>25.0f)mPcReturning=true;
    Vector3f progressGoal=goal;
    if(mPcRecoveryRoute && routeMgr && mPiki->mPathBuffers && mPiki->mCurrRoutePoint>=0 && mPiki->mCurrRoutePoint<mPiki->mNumRoutePoints){
        const int index=mPiki->mPathBuffers[mPiki->mCurrRoutePoint].mWayPointIdx;
        if(index>=0&&index<routeMgr->getNumWayPoints('test')){
            WayPoint* wp=routeMgr->getWayPoint('test',index);if(wp)progressGoal=wp->mPosition;
        }
    }
    const bool stranded=mPcStranded.update(here.x,here.y,here.z,dt,needsMove||mPcReturning,
        progressGoal.x,progressGoal.y,progressGoal.z);
    if(stranded && mPcReturnFailed && mPcRescueCooldown<=0
        && pc_settings_get_stuck_follower_rescue() && captain->pcTakeFollowerRescueBudget()){
        if(mPiki->pcRescueFollowerNearCaptain()){
            pc_follow_note("rescued_follower",here.x,here.y,here.z,mPiki->mSRT.t.x,mPiki->mSRT.t.y,mPiki->mSRT.t.z);
            pcResetFollowerRecovery();mPcRescueCooldown=12.0f;mLostChildTimer=0;return true;
        }
        mPcRescueCooldown=2.0f;
        pc_follow_note("rescue_no_safe_spot",here.x,here.y,here.z,goal.x,goal.y,goal.z);
    }
    const bool stalled=mPcFollowerProgress.stalledToward(here.x,here.y,here.z,dt,needsMove||mPcReturning,
        progressGoal.x,progressGoal.y,progressGoal.z);
    if(stalled)mPcReturning=true;
    // Separation retains ownership, but is not a reason to stop normal
    // following. Only a measured stall may acquire a new walking route.
    if (!mPcRecoveryRoute && !stalled) {
        if(mPcReturning){
            mLostChildTimer=0.0f;
            if(mIsWaiting){mIsWaiting=false;mPiki->startMotion(PaniMotionInfo(PIKIANIM_Walk),PaniMotionInfo(PIKIANIM_Walk));}
        }
        return false;
    }
    if (mPcRecoveryRoute) {
        mPcRecoveryRouteAge+=dt<0.1f?dt:0.1f;
        const Vector3f movedGoal=goal-mPcRecoveryGoal;
        if (!stalled && mPcRecoveryRouteAge<30.0f && movedGoal.length()<256.0f) {
            const int result=mPiki->pcMoveFollowerRoute();
            if (result==2) {mLostChildTimer=0.0f;return true;}
            if (result==0) {
                mPcRecoveryRoute=false;mPcFollowerProgress.reset();
                pc_follow_note("route_complete",here.x,here.y,here.z,goal.x,goal.y,goal.z);
                return false;
            }
        }
        mPcReturnFailed=true;
        mPcRecoveryRoute=false;mPcFollowerProgress.attempted();
        mPiki->pcSteerFollowerGoal(here);
        return mPcReturning;
    }
    if(!mPcReturning)return false;
    if(mPcFollowerProgress.cooldown>0.0f || !captain->pcTakeFollowerRouteBudget()){
        mPiki->pcSteerFollowerGoal(here);mLostChildTimer=0.0f;return true;
    }
    mPcFollowerProgress.attempted();
    if (!mPiki->initRouteTrace(goal,false,true)) {
        mPcReturnFailed=true;
        pc_follow_note("return_wait",here.x,here.y,here.z,goal.x,goal.y,goal.z);
        mPiki->pcSteerFollowerGoal(here);mLostChildTimer=0.0f;return true;
    }
    mPcRecoveryRoute=true;mPcRecoveryRouteAge=0.0f;mPcRecoveryGoal=goal;
    mIsWaiting=false;mLostChildTimer=0.0f;
    mPiki->startMotion(PaniMotionInfo(PIKIANIM_Run),PaniMotionInfo(PIKIANIM_Run));
    if (mPiki->pcMoveFollowerRoute()!=2) {
        mPcReturnFailed=true;
        mPcRecoveryRoute=false;
        mPiki->pcSteerFollowerGoal(here);
        pc_follow_note("route_step_blocked",here.x,here.y,here.z,goal.x,goal.y,goal.z);
    }
    return true;
}

bool ActCrowd::pcWaterAhead()
{
	const f32 kShoreDistance = 60.0f;
	const int kProbes        = 4;

	Vector3f dir = mPiki->mNavi->mSRT.t - mPiki->mSRT.t;
	dir.y        = 0.0f;
	f32 len      = dir.length();
	if (len < 0.001f) {
		return true;
	}
	dir = dir * (1.0f / len);

	for (int i = 1; i <= kProbes; i++) {
		f32 d = kShoreDistance * i / kProbes;
		if (d > len) {
			d = len;
		}
		Vector3f p      = mPiki->mSRT.t + dir * d;
		CollTriInfo* tri = mapMgr->getCurrTri(p.x, p.z, true);
		if (tri && MapCode::getAttribute(tri) == ATTR_Water) {
			return true;
		}
		if (d >= len) {
			break;
		}
	}
	return false;
}
#endif

int ActCrowd::exec()
{
	mPrevMode = mMode;
	mMode = 5;
#if defined(PIKI_PC_PORT)
    if (pcRecoverFollower()) return ACTOUT_Continue;
#endif
	if (mHasRoute) {
		exeRouteMove();
		if (mPiki->mUseAsyncPathfinding) {
			mLostChildTimer -= gsys->getFrameTime();
			if (mLostChildTimer < 0.0f) {
				mPiki->mActionState = 2;
				return ACTOUT_Fail;
			}
		}
		return ACTOUT_Continue;
	}

	if (mPiki->mNavi->isStickTo()) {
		mPiki->mActionState = 2;
		return ACTOUT_Fail;
	}

	if (mIsTripping) {
		if (mPiki->mPikiAnimMgr.getUpperAnimator().getCurrentMotionIndex() != PIKIANIM_Korobu) {
			mIsTripping = false;
			mPiki->startMotion(PaniMotionInfo(PIKIANIM_Walk), PaniMotionInfo(PIKIANIM_Walk));
		}
#if defined(PIKI_PC_PORT)
		// Frenada por fotograma de 30 Hz, repartida entre los ticks.
		mPiki->mTargetVelocity = mPiki->mTargetVelocity * powf(0.955f, 1.0f / PC_TICKS30);
#else
		mPiki->mTargetVelocity = mPiki->mTargetVelocity * 0.955f;
#endif
		return ACTOUT_Continue;
	}

#if defined(PIKI_PC_PORT)
	// Mod "Blues Only In Water": mientras el capitán está en el agua, los que
	// no son azules siguen andando hasta acercarse a la orilla y ahí se paran,
	// mirándolo, en vez de meterse. En cuanto sale vuelven a seguirlo.
	if (pc_settings_get_blues_only_water() && mPiki->mColor != Blue && mPiki->mNavi->mIsInWater
	    && (mPcWaitAshore || pcWaterAhead())) {
		mPiki->mTargetVelocity.set(0.0f, 0.0f, 0.0f);
		mPiki->mFaceDirection += 2.5f * (angDist(mPiki->mNavi->mFaceDirection, mPiki->mFaceDirection) * gsys->getFrameTime());
		if (!mPcWaitAshore) {
			mPcWaitAshore = true;
			mPiki->startMotion(PaniMotionInfo(PIKIANIM_Wait), PaniMotionInfo(PIKIANIM_Wait));
		}
		return ACTOUT_Continue;
	}
	if (mPcWaitAshore) {
		mPcWaitAshore = false;
		mPiki->startMotion(PaniMotionInfo(PIKIANIM_Walk), PaniMotionInfo(PIKIANIM_Walk));
	}
#endif

	if (mIsWaiting && !mPiki->hasBomb()) {
		int boreRes = mSelectAction->exec();
		if (boreRes != ACTOUT_Continue) {
			mIsWaiting = false;
			mPiki->startMotion(PaniMotionInfo(PIKIANIM_Walk), PaniMotionInfo(PIKIANIM_Walk));
		} else {
			if (mPiki->mPikiAnimMgr.getUpperAnimator().getCurrentMotionIndex() == PIKIANIM_Wait) {
				mIsWaiting = false;
				mPiki->startMotion(PaniMotionInfo(PIKIANIM_Walk), PaniMotionInfo(PIKIANIM_Walk));
			} else {
				return boreRes;
			}
		}
	}

	mWasWaiting = mIsWaiting;
	if (!mPiki->mNavi) {
		ERROR("piki->navi 0!\n");
	}

	bool check = false;
	if (mPiki->mNavi->mCStick.length() <= C_NAVI_PARM(mPiki->mNavi, mNeutralStickThreshold)) {
		check = true;
	}

	if (!mPlateMgr->validSlot(mCPlateSlotID)) {
		ERROR("invalid slotId!\n");
	}

	Vector3f platePos = mPlateMgr->mSlotList[mCPlateSlotID].mOffsetFromCenter + mPlateMgr->mPlateCenter;

	Vector3f effDir = static_cast<ViewPiki*>(mPiki)->mLastEffectPosition - mPiki->mSRT.t;
	f32 travelDist  = effDir.length();

	if (mPiki->hasBomb() && !playerState->mDemoFlags.isFlag(DEMOFLAG_GrabFirstBomb) && travelDist < 100.0f) {
		#if defined(PIKI_PC_PORT)
		if (mPiki->mNavi) naviMgr->setMovieNavi(mPiki->mNavi);
#endif
		playerState->mDemoFlags.setFlag(DEMOFLAG_GrabFirstBomb, mPiki);
	}

	mTravelDistance += travelDist;

	// - yellows with bombs cannot trip
	// - have to have moved a certain distance
	// - have to be moving at at least 110 units of speed
	if (!mPiki->hasBomb() && mTravelDistance >= 100.0f && mPiki->mVelocity.length() > 110.0f) {

		// idk why they did this in two rand checks, but go figure
		// approximately a 0.003% chance of tripping
		if (gsys->getRand(1.0f) >= 0.9999f && gsys->getRand(1.0f) > 0.7f
#if defined(PIKI_PC_PORT)
		    && !pc_settings_get_no_trip() // Mod "No Tripping"
		    // Una tirada por tick: a 60/120 FPS se reparte la misma probabilidad
		    // por segundo que a 30.
		    && gsys->getRand(1.0f) * PC_TICKS30 < 1.0f
#endif
		) {
			mIsTripping      = true;
			mTripLoopCounter = int((4.0f * gsys->getRand(1.0f))) + 3; // length of trip is a random number of anim loops, between 3 and 7
			mPiki->startMotion(PaniMotionInfo(PIKIANIM_Korobu, mPiki), PaniMotionInfo(PIKIANIM_Korobu));
			return ACTOUT_Continue;
		}

		mTravelDistance = 0.0f;
	}

#if defined(PIKI_PC_PORT)
	pcProtectFormationEdge(platePos);
    if (mPcFollowingTrail) {
        mPiki->pcSteerFollowerGoal(platePos);
        if (mIsWaiting) mPiki->startMotion(PaniMotionInfo(PIKIANIM_Walk),PaniMotionInfo(PIKIANIM_Walk));
        mIsWaiting=false;mLostChildTimer=0.0f;
        return ACTOUT_Continue;
    }
#endif
	Vector3f plateDir = platePos - mPiki->mSRT.t;
	f32 plateDist2D   = sqrtf(plateDir.x * plateDir.x + plateDir.z * plateDir.z);
	plateDir.normalise();

	if (plateDist2D < 60.0f && mPiki->mNavi->mIsCStickNeutral && mState != STATE_Sort) {
		if (!mIsWaiting && mPiki->mNavi->mNeutralTime - (2.0f * gsys->getRand(1.0f)) >= C_NAVI_PARM(mPiki->mNavi, mPikiImpatienceTime)) {
			mIsWaiting = true;
			return ACTOUT_Continue;
		}

		if (mState == STATE_Unk0) {
			mMode           = 0;
			Piki* minPiki   = nullptr;
			int minSlotPrio = 256;
			int minSlotID;
			Iterator iter(mPiki->mNavi->mPlateMgr);
			CI_LOOP(iter)
			{
				Piki* piki = static_cast<Piki*>(*iter);
				if (piki->mMode != PikiMode::FormationMode) {
					piki->changeMode(PikiMode::FreeMode, piki->mNavi);
				} else {
					ActCrowd* action = static_cast<ActCrowd*>(piki->mActiveAction->getCurrAction());
					if (action && piki != mPiki && action->mState == STATE_Formed) {
						int slotPrio = abs(action->mCPlateSlotID - mCPlateSlotID);
						if (slotPrio < minSlotPrio) {
							minPiki     = piki;
							minSlotPrio = slotPrio;
							minSlotID   = action->mCPlateSlotID;
						}
					}
				}
			}

			if (minPiki) {
				platePos = minPiki->mSRT.t;
			} else {
				platePos = mPiki->mNavi->mSRT.t;
			}

			STACK_PAD_VAR(1);
			mIsWaiting       = false;
			Vector3f moveDir = platePos - mPiki->mSRT.t;
			f32 moveDist     = moveDir.normalise();
			moveDist         = qdist2(platePos.x, platePos.z, mPiki->mSRT.t.x, mPiki->mSRT.t.z);
			if (moveDist <= 40.0f) {
				if (mState != STATE_Formed) {
					setFormed();
					pikiInfo->addFormationPiki();
					mOdometer.reset();
				}
			} else {
				mPiki->setSpeed(1.0f, moveDir);
				if (mWasWaiting && !mIsWaiting) {
					mPiki->startMotion(PaniMotionInfo(PIKIANIM_Walk), PaniMotionInfo(PIKIANIM_Walk));
					finishZawatuki();
				}
			}

			return ACTOUT_Continue;
		}

		mMode = 1;
		mPiki->mTargetVelocity.set(0.0f, 0.0f, 0.0f);
		Vector3f naviDir = mPiki->mNavi->mSRT.t - mPiki->mSRT.t;
		f32 diff         = atan2f(naviDir.x, naviDir.z);
		mPiki->mFaceDirection += 0.3f * angDist(diff, mPiki->mFaceDirection);
		if (!gameflow.mMoviePlayer->mIsActive && !mIsWaiting
		    && mPiki->mNavi->mNeutralTime - (2.0f * gsys->getRand(1.0f)) >= C_NAVI_PARM(mPiki->mNavi, mPikiImpatienceTime)) {
			mIsWaiting = true;
			startZawatuki();
		}
		return ACTOUT_Continue;
	}

	if (plateDist2D <= 7.0f) {
		mNearSlotCounter = 0;
	} else if (plateDist2D < 15.0f) {
		mNearSlotCounter++;
		if (mPrevMode == 2 && mPiki->mNavi->mNeutralTime > 0.1f) {
			mNearSlotCounter = 0;
		}
		if (mNearSlotCounter >= 6 * PC_TICKS30) {
			mNearSlotCounter = 6 * PC_TICKS30;
		}
	} else {
		mNearSlotCounter = 0;
	}

	if (plateDist2D <= 7.0f || (mNearSlotCounter < 6 * PC_TICKS30 && plateDist2D <= 15.0f)) {
		mMode = 2;
		mOdometer.reset();
		mPiki->mTargetVelocity.set(0.0f, 0.0f, 0.0f);
		plateDir  = mPiki->mNavi->mSRT.t - mPiki->mSRT.t;
		f32 diff  = atan2f(plateDir.x, plateDir.z);
		f32 angle = angDist(diff, mPiki->mFaceDirection);
		mPiki->mFaceDirection += 0.3f * angle;
		if (mState != STATE_Formed) {
			pikiInfo->addFormationPiki();
			setFormed();
		}

		if (!gameflow.mMoviePlayer->mIsActive && !mIsWaiting
		    && mPiki->mNavi->mNeutralTime - (5.0f * gsys->getRand(1.0f)) >= C_NAVI_PARM(mPiki->mNavi, mPikiImpatienceTime)) {
			mIsWaiting = true;
			startZawatuki();
		}
	} else if (plateDist2D < 15.0f) {
		mMode = 3;
		if (mIsWaiting && plateDist2D < 10.0f) {
			mIsWaiting = true;
		}

		mOdometer.reset();
		Vector3f vel(mPiki->mTargetVelocity);
		f32 factor = 10.0f / mPiki->mProps->mCreatureProps.mAcceleration();
		f32 speed  = mPiki->getSpeed(1.0f);
		f32 f1     = (speed / factor);
		f32 val1   = 0.5f * f1 * speed;
		f32 speed2 = mPiki->mVelocity.length();
		f32 f2     = (speed2 / factor);
		f32 val2   = 0.5f * f2 * speed2;

		if (plateDist2D < val2) {
			mPiki->mTargetVelocity.set(0.0f, 0.0f, 0.0f);
			if (!gameflow.mMoviePlayer->mIsActive && !mIsWaiting
			    && mPiki->mNavi->mNeutralTime - (5.0f * gsys->getRand(1.0f)) >= C_NAVI_PARM(mPiki->mNavi, mPikiImpatienceTime)) {
				mIsWaiting = true;
				startZawatuki();
			}
			plateDir  = mPiki->mNavi->mSRT.t - mPiki->mSRT.t;
			f32 diff  = atan2f(plateDir.x, plateDir.z);
			f32 angle = angDist(diff, mPiki->mFaceDirection);
			mPiki->mFaceDirection += 0.3f * angle;
		} else if (plateDist2D < val1) {
			f32 val3               = speed2 + 0.5f * speedy_sqrtf(speed2 * speed2 + 8.0f * factor * plateDist2D);
			mPiki->mTargetVelocity = plateDir * val3;
		} else {
			mPiki->setSpeed(1.0f, plateDir);
		}

		Vector3f pikiDir      = mPiki->mSRT.t - mPiki->mNavi->mSRT.t;
		Vector3f naviPlateDir = mPiki->mNavi->mSRT.t - mPlateMgr->mPlateOffset;
		naviPlateDir.normalise();
		if (naviPlateDir.DP(pikiDir) > 0.0f) {
			Vector3f sideDir(-pikiDir.z, 0.0f, pikiDir.x);
			if (!(mCPlateSlotID & 1)) {
				sideDir.multiply(-1.0f);
			}
			sideDir.normalise();

			if (newVer && !check) {
				sideDir.set(0.0f, 0.0f, 0.0f);
			}

			f32 prevSpeed          = mPiki->mTargetVelocity.length();
			mPiki->mTargetVelocity = mPiki->mTargetVelocity + sideDir * mPiki->getSpeed(0.5f);
			mPiki->mTargetVelocity.normalise();
			mPiki->mTargetVelocity = mPiki->mTargetVelocity * prevSpeed;
		}
	} else {
		mMode = 4;
		mPiki->setSpeed(1.0f, plateDir);

		Vector3f pikiDir      = mPiki->mSRT.t - mPiki->mNavi->mSRT.t;
		Vector3f naviPlateDir = mPiki->mNavi->mSRT.t - mPlateMgr->mPlateOffset;
		naviPlateDir.normalise();
		if (naviPlateDir.DP(pikiDir) > 0.0f) {
			Vector3f sideDir(-pikiDir.z, 0.0f, pikiDir.x);
			if (!(mCPlateSlotID & 1)) {
				sideDir.multiply(-1.0f);
			}
			sideDir.normalise();

			if (newVer && !check) {
				sideDir.set(0.0f, 0.0f, 0.0f);
			}

			f32 prevSpeed          = mPiki->mTargetVelocity.length();
			mPiki->mTargetVelocity = mPiki->mTargetVelocity + sideDir * mPiki->getSpeed(0.5f);
			mPiki->mTargetVelocity.normalise();
			mPiki->mTargetVelocity = mPiki->mTargetVelocity * prevSpeed;
		}
	}

	if (plateDist2D < C_PIKI_PARM(mPiki, mFormationSlipRange)) {
		mLostChildTimer = 0.0f;
		mHasRequestedNewSlot = false;
	} else if (plateDist2D < C_PIKI_PARM(mPiki, mFormationBreakRange)) {
		mLostChildTimer += gsys->getFrameTime();
		if (!mHasRequestedNewSlot) {
			if (mCPlateSlotID != -1) {
				mPlateMgr->releaseSlot(mPiki, mCPlateSlotID);
				mCPlateSlotID = mPlateMgr->getSlot(mPiki, this);
			}

			mHasRequestedNewSlot = true;
		}
		if (mCPlateSlotID == -1 || (mLostChildTimer > C_PIKI_PARM(mPiki, mMaxLostChildTime)
#if defined(PIKI_PC_PORT)
            && !mPcReturning
#endif
        )) {
			return ACTOUT_Fail;
		}
	} else {
#if defined(PIKI_PC_PORT)
        // The recovery dispatcher already validates solo/state eligibility.
        // Keep a distant assignment while ordinary following gets its turn;
        // never discard it merely because a route token was not needed yet.
        if (!mPcReturning) return ACTOUT_Fail;
        mLostChildTimer=0.0f;
#else
		return ACTOUT_Fail;
#endif
	}

	STACK_PAD_STRUCT(3);
	STACK_PAD_VAR(4);
	STACK_PAD_TERNARY(mPiki, 11);

	if (mWasWaiting && !mIsWaiting) {
		mPiki->startMotion(PaniMotionInfo(PIKIANIM_Walk), PaniMotionInfo(PIKIANIM_Walk));
		finishZawatuki();
	}

	return ACTOUT_Continue;
}

/**
 * @todo: Documentation
 */
void ActCrowd::startZawatuki()
{
	if (!mPiki->hasBomb()) {
		mIsWaiting = true;
		mSelectAction->init(nullptr);
	}
}

/**
 * @todo: Documentation
 */
void ActCrowd::finishZawatuki()
{
}

/**
 * @todo: Documentation
 * @note UNUSED Size: 0000C0
 */
void ActCrowd::startBoredom()
{
	switch (mBoredomMotion) {
	case 0:
	{
		startTalk();
		break;
	}
	case 2:
	{
		mPiki->startMotion(PaniMotionInfo(PIKIANIM_Akubi), PaniMotionInfo(PIKIANIM_Akubi));
		break;
	}
	case 3:
	{
		mPiki->startMotion(PaniMotionInfo(PIKIANIM_Rinbow), PaniMotionInfo(PIKIANIM_Rinbow));
		break;
	}
	}
}

/**
 * @todo: Documentation
 * @note UNUSED Size: 0000DC
 */
void ActCrowd::startTalk()
{
	Iterator iter(&mPiki->mSearchBuffer);
	iter.first();
	Creature* closest     = *iter;
	Vector3f dir          = closest->mSRT.t - mPiki->mSRT.t;
	mPiki->mFaceDirection = atan2f(dir.x, dir.z);
	mPiki->startMotion(PaniMotionInfo(PIKIANIM_Chatting), PaniMotionInfo(PIKIANIM_Chatting));
}
