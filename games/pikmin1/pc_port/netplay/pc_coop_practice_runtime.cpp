#ifdef NECTAR_DESKTOP_COOP_ROOM
#include "netplay/pc_desktop_coop.h"
#endif
#if defined(__APPLE__)
#include <TargetConditionals.h>
#endif
#include "netplay/pc_coop_practice_runtime.h"
#include "netplay/pc_coop_audio.h"
#include "netplay/pc_coop_practice_map.h"
#include "netplay/pc_coop_practice_start.h"
#include "netplay/pc_coop_practice_input.h"
#include "netplay/pc_coop_practice_status.h"
#include "netplay/pc_coop_world.h"
#include "netplay/pc_coop_visual_smoothing.h"
#include "netplay/pc_netplay_present.h"
#include "netplay/pc_input_log.h"
#include "nectar_net/practice_bootstrap.h"
#include "nectar_net/secure_random.h"
#include "GameCoreSection.h"
#include "GameStat.h"
#include "Navi.h"
#include "NaviMgr.h"
#include "PikiMgr.h"
#include "NaviState.h"
#include "MapMgr.h"
#include "PlayerState.h"
#include "FlowController.h"
#include "gameflow.h"
#include "pc_window.h"
#include "settings/pc_settings.h"
#include "Dolphin/pad.h"
#include "dolphin_stubs/pc_card_paths.h"
#include <chrono>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <thread>

#if defined(__APPLE__) && TARGET_OS_IPHONE
extern "C" void nectar_ios_open_coop_practice(void);
#endif
namespace {
namespace net=nectar::net;
std::unique_ptr<net::CoopConnection> owner;
std::unique_ptr<net::PracticeBootstrap> loading;
std::thread::id thread;
net::CoopRole role=net::CoopRole::Guest;
PcCoopPracticeInput inputs;
PcCoopVisualSmoothing smoothing;
net::ActorFrame presented;
net::NetInputFrame remote;
std::uint64_t tick=0,frame=0,applied=0,lastPublish=0,revision=0;
bool title=false,requested=false,loaded=false,confirmed=false,entered=false,stopped=false;
bool away=false,panel=false,padFiltered=false,advancing=false,sessionConfigured=false;
std::uint16_t previousButtons=0;
std::uint64_t diagnosticAt=0,diagnosticLive=0,diagnosticRepeat=0,diagnosticNeutral=0,diagnosticSamples=0,diagnosticSent=0;
// A small local-only report helps diagnose the experimental practice session.
// It contains no room code, device ID, campaign or game-data content.
void practiceReport(std::uint64_t now, net::CoopSession* s) {
    if (!s || (diagnosticAt && (now<diagnosticAt || now-diagnosticAt<1000))) return;
    diagnosticAt=now;
    // Keep separate bounded reports per app launch, preserving earlier tests.
    static char path[96]={};
    if (!path[0]) std::snprintf(path,sizeof(path),"p1-coop-practice-%llu.txt",
        static_cast<unsigned long long>(std::time(nullptr)));
    FILE* f=std::fopen(path,"ab");if(!f)return;
    if (std::fseek(f,0,SEEK_END)==0) {
        const long size=std::ftell(f);
        if (size>=0 && size<65000) {
            Navi* n=naviMgr?naviMgr->getNavi(role==net::CoopRole::Host?0:1):nullptr;
            Camera* c=n?n->controlCamera():nullptr;
            const auto finite=[](float v) {return std::isfinite(v) ? v : 0.0f;};
            net::TransportStats stats;const bool measured=owner && owner->stats(stats);
            const int rtt=measured?stats.rttMs:-1;
            std::uint64_t audioSent=0,audioPlayed=0,audioDropped=0;pc_coop_audio_counts(audioSent,audioPlayed,audioDropped);
            std::fprintf(f,"practice role=%s phase=%d away=%d tick=%llu frame=%llu applied=%llu rtt=%d queued=%d unacked=%d input_live=%llu repeat=%llu neutral=%llu samples=%llu sent=%llu camera=%d eye=%.1f,%.1f,%.1f focus=%.1f,%.1f,%.1f captain=%.1f,%.1f,%.1f host_hz=%.1f actor_age=%llu target=%llu hold=%u revision=%llu audio_sent=%llu audio_played=%llu audio_dropped=%llu audio_backend_state=%d\n",
                role==net::CoopRole::Host?"host":"guest",static_cast<int>(s->phase()),away?1:0,
                static_cast<unsigned long long>(tick),static_cast<unsigned long long>(frame),static_cast<unsigned long long>(applied),rtt,
                measured?stats.pendingReliableBytes:-1,measured?stats.unackedReliableBytes:-1,
                static_cast<unsigned long long>(diagnosticLive),static_cast<unsigned long long>(diagnosticRepeat),static_cast<unsigned long long>(diagnosticNeutral),
                static_cast<unsigned long long>(diagnosticSamples),static_cast<unsigned long long>(diagnosticSent),c?1:0,
                c?finite(c->mPosition.x):0.0f,c?finite(c->mPosition.y):0.0f,c?finite(c->mPosition.z):0.0f,
                c?finite(c->mFocus.x):0.0f,c?finite(c->mFocus.y):0.0f,c?finite(c->mFocus.z):0.0f,
                n?finite(n->mSRT.t.x):0.0f,n?finite(n->mSRT.t.y):0.0f,n?finite(n->mSRT.t.z):0.0f,inputs.rateHz(),
                static_cast<unsigned long long>(inputs.frameAge(now)),static_cast<unsigned long long>(inputs.targetTick()),s->inputHoldTicks(),
                static_cast<unsigned long long>(s->view().revision),static_cast<unsigned long long>(audioSent),
                static_cast<unsigned long long>(audioPlayed),static_cast<unsigned long long>(audioDropped),pc_coop_audio_backend_state());
        }
    }
    std::fclose(f);
}
char failure[240]={};
std::uint64_t nowMs() {
    return static_cast<std::uint64_t>(std::chrono::duration_cast<std::chrono::milliseconds>(
        std::chrono::steady_clock::now().time_since_epoch()).count());
}
bool ownThread() { return thread==std::this_thread::get_id(); }
net::CoopSession* session() { return owner ? owner->session() : nullptr; }
void showPanel() {
#if defined(__APPLE__) && TARGET_OS_IPHONE
    nectar_ios_open_coop_practice();
#elif defined(NECTAR_DESKTOP_COOP_ROOM)
    nectar_desktop_open_coop_practice();
#endif
}
void fail(const char* reason) {
    if (!failure[0]) { std::snprintf(failure,sizeof(failure),"%s",reason);std::fprintf(stderr,"[coop-practice] %s\n",reason); }
    stopped=true;advancing=false;pc_coop_audio_end();pc_coop_world_stop();
    if (loading && entered && role==net::CoopRole::Host)
        pc_coop_world_set_host_running(loading->sessionId(),loading->scene().epoch,false);
    pc_coop_practice_cancel_start(); showPanel();
}
void hold(bool run) {
    advancing=run && !stopped && !away;
    pc_coop_audio_running(session() && session()->canIssueCommands() && !stopped && !away);
    if (entered && role==net::CoopRole::Host &&
        !pc_coop_world_set_host_running(loading->sessionId(),loading->scene().epoch,advancing))
        fail("The practice world changed unexpectedly. Close P1 and reopen; your solo saves are unchanged.");
}
void enterWorld() {
    if (entered || !loaded || !loading || !loading->sessionId()) return;
    bool ok=role==net::CoopRole::Host
        ? pc_coop_world_begin_host(loading->sessionId(),loading->scene().epoch,true)
        : pc_coop_world_begin_guest(loading->sessionId(),loading->scene().epoch);
    if (!ok || !pc_netplay_present_begin_practice_view(role==net::CoopRole::Host ? 0 : 1)) {
        fail("Could not bind the two practice captains. Close P1 and reopen.");return;
    }
    entered=true;pc_coop_audio_begin(role==net::CoopRole::Host);
    if (role==net::CoopRole::Guest && !pc_coop_world_prepare_guest_visuals(loading->sessionId(),loading->scene().epoch))
        fail("Practice display resources were not ready. Close P1 and reopen.");
}
}
bool pc_coop_practice_can_enter() { return title && !owner && !pc_coop_practice_restart_required(); }
void pc_coop_practice_note_title(bool available) { title=available; }
bool pc_coop_practice_active() { return owner!=nullptr; }
bool pc_coop_practice_block_title() { return owner && (stopped || !requested); }
bool pc_coop_practice_adopt(std::unique_ptr<net::CoopConnection>& incoming) {
    if (!pc_coop_practice_can_enter() || !incoming || !incoming->connected() || !incoming->role(role)) return false;
    thread=std::this_thread::get_id(); owner=std::move(incoming);
    loading=std::make_unique<net::PracticeBootstrap>(*owner);
    std::uint64_t id=0,seed=0;
    const auto now=nowMs();
    const bool ok=role==net::CoopRole::Guest ? loading->beginGuest(now)
        : net::secureRandomBytes(reinterpret_cast<std::uint8_t*>(&id),sizeof(id)) && id &&
          net::secureRandomBytes(reinterpret_cast<std::uint8_t*>(&seed),sizeof(seed)) && loading->beginHost(id,seed,now);
    if (!ok) fail("Could not start a private practice session. Close P1 and reopen.");
    return true; // ownership was transferred even if startup failed
}
void pc_coop_practice_tick_begin() {
    if (!owner || !ownThread()) return;
    padFiltered=false;remote={}; advancing=false;
    if (stopped) return;
    const auto now=nowMs();
    net::RoomStatus status; owner->maintain(now,static_cast<std::uint64_t>(std::time(nullptr)),status);
    loading->pump(now);
    if (loading->phase()==net::PracticeLoadPhase::Failed) {
        switch (loading->failure()) {
        case net::PracticeLoadFailure::ConnectionLost: fail("The practice connection was lost. Both players must reopen P1 for this test.");break;
        case net::PracticeLoadFailure::Deadline: fail("Practice setup timed out while waiting for both phones. Reopen P1 and try again.");break;
        case net::PracticeLoadFailure::SendFailed: fail("A practice setup message could not be sent. Reopen P1 and try again.");break;
        case net::PracticeLoadFailure::SessionStartFailed: fail("The practice session could not start safely. Reopen P1 and try again.");break;
        default: fail("Practice setup stopped unexpectedly. Reopen P1 and try again.");break;
        }
        return;
    }
    if (loading->phase()==net::PracticeLoadPhase::Loading && !requested) {
        if (const char* error=pc_coop_practice_map_prepare()) { fail(error);return; }
        if (!pc_coop_practice_request_start()) { fail("Could not isolate a disposable practice save. No campaign was opened.");return; }
        requested=true;
    }
    auto* s=session();
    if (!s) return;
    if (!sessionConfigured) {
        if (role==net::CoopRole::Host && !s->configureInputContinuousMask(PcCoopPracticeInput::Continuous)) {
            fail("Could not initialize practice controls.");return;
        }
        sessionConfigured=true;
    }
    s->pump(now);
    s->setBlocked(net::CoopBlock::Settings,pc_settings_menu_is_open()!=0);
    s->setBlocked(net::CoopBlock::Background,away);
    if (s->phase()==net::CoopPhase::WaitingForPartner) { hold(false);showPanel();return; }
    if (s->view().revision!=revision) { inputs.reset();smoothing.reset();revision=s->view().revision; }
    if (role==net::CoopRole::Guest && s->actors().frame>applied) {
        const auto& actors=s->actors();
        if (!pc_coop_world_apply_guest_visuals(loading->sessionId(),loading->scene().epoch,actors)) {
            fail("A complete practice picture could not be applied. Close P1 and reopen.");return;
        }
        applied=actors.frame;inputs.observe(actors.tick,now);smoothing.push(actors,now);
        if (!confirmed) confirmed=s->confirmWorldLoaded();
    }
    if (role==net::CoopRole::Guest && applied) {
        if (s->phase()!=net::CoopPhase::Running) { smoothing.reset();smoothing.push(s->actors(),now); }
        if (smoothing.sample(now,presented) && !pc_coop_world_present_guest(presented)) {
            fail("The practice view changed unexpectedly. Close P1 and reopen.");return;
        }
    }
    // A running session dismisses the one-shot panel latch so that a later
    // interruption, including either phone backgrounding, can request ready again.
    if (s->phase()==net::CoopPhase::Running) panel=false;
    if (confirmed && !away && !panel && s->phase()!=net::CoopPhase::Running) { panel=true;showPanel(); }
    hold(s->hostShouldAdvanceWorld());
    if (advancing && role==net::CoopRole::Host) {
        ++tick;
        net::InputHealth health;
        s->consumeGuestInput(tick,remote,health,now);
        if (health==net::InputHealth::Live) ++diagnosticLive;
        else if (health==net::InputHealth::Repeated) ++diagnosticRepeat;
        else ++diagnosticNeutral;
    }
}
void pc_coop_practice_tick_end() {
    // Session creation can occur inside the world-loaded callback, after this
    // frame's tick_begin. Never publish/confirm the first world before the
    // next tick_begin configures the host input policy.
    if (!owner || !ownThread() || stopped || !entered || !session() || !sessionConfigured) return;
    auto* s=session();const auto now=nowMs();
    pc_coop_audio_tick(*s,now);
    practiceReport(now,s);
    if (role==net::CoopRole::Host && advancing) {
        // This disposable flat arena has no campaign jobs or hazards. A throw
        // beyond its wall returns that Pikmin to its owning captain only.
        Iterator it(pikiMgr);CI_LOOP(it) {
            auto* p=static_cast<Piki*>(*it);
            if (!p || !p->isAlive() || (std::fabs(p->mSRT.t.x)<850 && std::fabs(p->mSRT.t.z)<850 && p->mSRT.t.y>-100)) continue;
            Navi* n=naviMgr->getNavi(p->mPlayerId==1?1:0);
            if(n) { p->mSRT.t=n->mSRT.t;p->mLastPosition=p->mSRT.t;p->mVelocity.set(0,0,0);p->changeMode(PikiMode::FormationMode,n); }
        }
    }
    if (role==net::CoopRole::Host && (!frame || now-lastPublish>=net::CoopSession::kActorPeriodMs)) {
        std::vector<std::vector<std::uint8_t>> packets;
        if (!pc_coop_world_capture_packets(++frame,tick,net::kActorMaxPacketBytes,packets)) {
            fail("Practice actors could not be captured safely. Close P1 and reopen.");return;
        }
        if (s->publishActors(packets,now)) { lastPublish=now;if (!confirmed) confirmed=s->confirmWorldLoaded(); }
    }
    if (role==net::CoopRole::Guest && s->canIssueCommands()) {
        net::TransportStats stats; const int rtt=owner->stats(stats) ? stats.rttMs : 0;
        const auto frames=inputs.bundle(now,rtt);
        if (!frames.empty() && s->publishInput(frames,now)) { ++diagnosticSent;inputs.published(frames,now); }
    }
}
void pc_coop_practice_loaded(GameCoreSection& core) {
    if (!owner || !ownThread() || stopped || loaded) return;
    if (!core.mNavi || !core.mNavi2 || !pikiMgr || !core.mMapMgr) { fail("The practice area is incomplete.");return; }
    for (int p=0;p<2;++p) {
        Navi* n=p ? core.mNavi2 : core.mNavi;
        Vector3f at(p ? 180.0f : -180.0f,0,0);at.y=core.mMapMgr->getMinY(at.x,at.z,true);
        n->mSRT.t=at;n->mLastPosition=at;n->mVelocity.set(0,0,0);
        n->mStateMachine->transit(n,NAVISTATE_Walk);
        n->startMotion(PaniMotionInfo(PIKIANIM_Wait),PaniMotionInfo(PIKIANIM_Wait));
        if (role==net::CoopRole::Host) for (int i=0;i<12;++i) {
            auto* pik=static_cast<Piki*>(pikiMgr->birth());
            if (!pik) { fail("The practice squad could not be created.");return; }
            GameStat::workPikis.inc(i%3);pik->init(n);Vector3f pos=at;pos.x+=(i%3-1)*24.0f;pos.z+=50+(i/3)*20.0f;
            pik->Creature::init(pos);pik->initColor(i%3);pik->mPlayerId=p;
            pik->changeMode(PikiMode::FormationMode,n);
        }
    }
    // Preload locally chosen animation assets, never a path or ID supplied by
    // a network packet. Guest sampling below is read-only and cannot lazy-load.
    for (int color=0;color<3;++color) {
        auto* mgr=PikiShapeObject::_instances[color]->mAnimMgr;
        int count=0;for (auto* a=mgr->mAnimList.mChild;a;a=a->mNext) ++count;
        for (int i=0;i<count;++i) mgr->findAnim(i);
    }
    for (Navi* n : {core.mNavi,core.mNavi2}) {
        auto* mgr=n->mNaviAnimMgr.mUpperAnimator.mMgr;
        int count=0;for (auto* a=mgr->mAnimList.mChild;a;a=a->mNext) ++count;
        for (int i=0;i<count;++i) mgr->findAnim(i);
    }
    GameStat::update();
    loaded=true;enterWorld();
    if (!stopped && !loading->worldLoaded(0,nowMs())) fail("The two phones did not accept the same practice area.");
}
bool pc_coop_practice_select_stage() {
    if (!owner || !requested) return false;
    gameflow.mPlayState.Initialise();playerState->setChallengeMode();gameflow.mIsChallengeMode=TRUE;
    FOREACH_NODE(StageInfo,flowCont.mStageList.mChild,stage) {
        if (stage->mChalStageID==CHALSTAGE_Practice) {
            flowCont.mCurrentStage=stage;
            std::snprintf(flowCont.mCurrStageFilePath,sizeof(flowCont.mCurrStageFilePath),"%s",PC_COOP_PRACTICE_STAGE);
            std::snprintf(flowCont.mDoorStageFilePath,sizeof(flowCont.mDoorStageFilePath),"%s",PC_COOP_PRACTICE_STAGE);
            gameflow.mWorldClock.setTime(12.0f);
            gameflow.mNextOnePlayerSectionID=ONEPLAYER_NewPikiGame;title=false;return true;
        }
    }
    fail("Original practice-stage resources are missing.");return true;
}
void pc_coop_practice_filter_pad(PADStatus* pads) {
    if (!owner || !loaded || stopped || !ownThread() || padFiltered || !pads) return;
    padFiltered=true;
    const PADStatus physical=pads[0];
    const bool start=(physical.button&PAD_BUTTON_START) && !(previousButtons&PAD_BUTTON_START);
    previousButtons=physical.button;
    if (start) { pc_coop_practice_pause();showPanel(); }
    if (role==net::CoopRole::Guest) {
        net::NetInputFrame f;
        f.held=physical.button & ~(PAD_BUTTON_START|PAD_BUTTON_Y);
        f.stickX=physical.stickX;f.stickY=physical.stickY;
        f.cstickX=physical.substickX;f.cstickY=physical.substickY;
        f.triggerL=physical.triggerLeft;f.triggerR=physical.triggerRight;
        f.flags=(pc_window_take_bomb_press(0)?1:0)|(pc_window_take_lockon_press(0)?2:0)
            |(pc_window_take_swarm_press(0)?4:0)|(pc_window_swarm_held()?8:0);
        Navi* n=naviMgr?naviMgr->getNavi(1):nullptr;
        Camera* c=n?n->controlCamera():nullptr;
        if (c) f.controlYaw=pc_input_log_yaw_quantise(std::atan2(c->mViewXAxis.z,c->mViewXAxis.x));
        const float drag=pc_window_take_camera_drag_player(0);
        pc_window_add_camera_drag_player(1,drag);
        f.cursorDx=static_cast<std::int16_t>(std::clamp(drag*3.2f/pc_input_log::kYawTurnsToRad,-32767.0f,32767.0f));
        if (session() && session()->canIssueCommands()) { ++diagnosticSamples;inputs.sample(f,nowMs()); }
        pads[1]=physical;pads[1].button&=~(PAD_BUTTON_START|PAD_BUTTON_Y);
        pads[0]={};pads[0].err=PAD_ERR_NONE;
    } else {
        pads[0].button&=~(PAD_BUTTON_START|PAD_BUTTON_Y);
        pads[1]={};pads[1].err=PAD_ERR_NONE;
        if (advancing) {
            pads[1].button=remote.held & ~(PAD_BUTTON_START|PAD_BUTTON_Y);
            pads[1].stickX=remote.stickX;pads[1].stickY=remote.stickY;
            pads[1].substickX=remote.cstickX;pads[1].substickY=remote.cstickY;
            pads[1].triggerLeft=remote.triggerL;pads[1].triggerRight=remote.triggerR;
        }
    }
}
bool pc_coop_practice_remote_input(int p) { return owner && loaded && role==net::CoopRole::Host && p==1; }
bool pc_coop_practice_control_yaw(int p,float* sine,float* cosine) {
    if (!pc_coop_practice_remote_input(p)) return false;
    const float yaw=remote.controlYaw*pc_input_log::kYawTurnsToRad;
    *sine=std::sin(yaw);*cosine=std::cos(yaw);return true;
}
std::uint8_t pc_coop_practice_ext(int p) { return pc_coop_practice_remote_input(p)?remote.flags:0; }
std::int16_t pc_coop_practice_cursor_rotate(int p) { return pc_coop_practice_remote_input(p)?remote.cursorDx:0; }
int pc_coop_practice_local_player() { return owner && role==net::CoopRole::Guest ? 1 : 0; }
bool pc_coop_practice_can_ready() { return owner && !stopped && confirmed && session() && session()->phase()!=net::CoopPhase::WaitingForPartner; }
bool pc_coop_practice_ready() {
    if (!ownThread() || !pc_coop_practice_can_ready()) return false;
    return session()->setBlocked(net::CoopBlock::Manual,false) && session()->setReady(true);
}
void pc_coop_practice_pause() { if (owner && ownThread() && session()) { session()->setBlocked(net::CoopBlock::Manual,true);hold(false); } }
bool pc_coop_practice_leave() {
    if (!owner || !ownThread()) return false;
    pc_coop_practice_pause();
    // Only return to title while the original save routing is still active.
    // Once the temporary card has been admitted, scene/card caches cannot yet
    // be safely restored in-process, so require a full restart instead.
    pc_coop_practice_cancel_start();
    const auto start=pc_coop_practice_start_state();
    const bool safe=title && !entered && !loaded && !pc_card_coop_practice_active() &&
        (start==PcCoopPracticeStart::Idle || start==PcCoopPracticeStart::Failed);
    if (!safe) {
        owner->close();fail("Practice ended. Close P1 and reopen to return to solo. Your campaign saves and settings are unchanged.");
        std::snprintf(failure,sizeof(failure),"Practice ended. Close P1 and reopen to return to solo. Your campaign saves and settings are unchanged.");
        return false;
    }
    pc_coop_audio_end();loading.reset();owner->close();owner.reset();pc_coop_world_end_scene();
    requested=loaded=confirmed=entered=stopped=away=panel=padFiltered=advancing=sessionConfigured=false;
    tick=frame=applied=lastPublish=revision=0;previousButtons=0;failure[0]=0;inputs.reset();smoothing.reset();presented={};remote={};
    return true;
}
void pc_coop_practice_background(bool value) { if (!owner || !ownThread()) return;away=value;if (session()) session()->setBlocked(net::CoopBlock::Background,value);if(value){panel=false;hold(false);} }
void pc_coop_practice_status(char* out,std::size_t cap) {
    const char* msg="Open Online Co-op from the title screen to start practice.";
    if (failure[0]) msg=failure;
    else if (owner) {
        auto* s=session();
        if (!s || !confirmed) msg="Loading disposable practice area. Keep both phones in P1. Your campaign is untouched.";
        else if (s->phase()==net::CoopPhase::WaitingForPartner) msg="Partner disconnected. The practice world is frozen. This first test requires reopening P1 on both phones to reconnect; live rejoin is next.";
        else if (s->phase()==net::CoopPhase::Running) msg="Practice running. Each captain has 12 Pikmin. Move, throw, whistle and dismiss; Pause opens this panel. No campaign progress is saved.";
        else msg=pc_practice_wait_message(s->view(),role==net::CoopRole::Host ? 0 : 1);
    }
    if (out && cap) std::snprintf(out,cap,"%s",msg);
}

bool pc_coop_practice_hud(int player,int& formation,int& total,int& nextType) {
    if (!loaded || !session() || role!=net::CoopRole::Guest || player<0 || player>1) return false;
    formation=total=nextType=0;
    for (const auto& entry:session()->actors().pikmin) {
        const auto& p=entry.second;
        if (p.owner==player) ++total;
        if (p.leader==player && p.action==PikiMode::FormationMode) {
            ++formation;if(!nextType)nextType=6*p.color+p.maturity+1;
        }
    }
    return true;
}
