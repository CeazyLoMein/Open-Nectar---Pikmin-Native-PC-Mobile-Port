"""Exercise actual gameplay update/draw guards with controlled engine leaves.

This is not an iPhone/gameplay test. The full engine and its resource adapters
still require native compilation and hardware validation before UI activation.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if not (ROOT / 'games').exists():
    ROOT = Path(r'C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port')
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)

def block(text, signature):
    start = text.index(signature); pos = text.index('{', start); depth = 1; end = pos + 1
    while depth:
        depth += (text[end] == '{') - (text[end] == '}'); end += 1
    return text[start:end]

game = (ROOT/'games/pikmin1/src/plugPikiColin/newPikiGame.cpp').read_text(encoding='utf-8')
app = (ROOT/'games/pikmin1/src/plugPikiColin/plugPiki.cpp').read_text(encoding='utf-8')
core = (ROOT/'games/pikmin1/src/plugPikiKando/gameCoreSection.cpp').read_text(encoding='utf-8')
view = (ROOT/'games/pikmin1/src/plugPikiKando/viewPiki.cpp').read_text(encoding='utf-8')
maturity = block(view, 'if (pc_coop_world_has_guest() && pikiMgr && mHappa >= Leaf && mHappa <= Flower)')
camera = (ROOT/'games/pikmin1/src/plugPikiNakata/pcamcamera.cpp').read_text(encoding='utf-8')
recenter = block(camera, 'if (pc_coop_world_may_advance() && pc_settings_get_free_camera()')
# Select the actual PC branch before balancing its braces (the source's
# inactive GameCube #else starts an alternative if with one shared close).
camera_pc = camera.replace('#else\n\t\tif (mTargetCreature && mTargetCreature->mObjType == OBJTYPE_Navi) {\n#endif', '')
rotate = block(camera_pc, 'if (pc_coop_world_may_advance() && !detMode && mTargetCreature')
record_rotate = block(camera, 'if (pc_coop_world_may_advance() && detMode && dragRoute == 1)')
mouth_start = view.index('#if defined(PIKI_PC_PORT)\n\t\tif (pc_coop_world_may_advance())')
mouth = view[mouth_start:view.index('mSRT.t = mSwallowMouthPart->mCentre;', mouth_start)+len('mSRT.t = mSwallowMouthPart->mCentre;')]
update = block(game, 'virtual void update() // _10').replace('virtual ', '', 1)
tail = game[game.index('if (!mIsInitialSetup) {\n\t\t\t// check if we should advance'):game.index('if (mNextModeState && pc_coop_world_may_advance())')]
transition = block(game, 'if (mNextModeState && pc_coop_world_may_advance())')
frame_begin = app[app.index('\tpc_render_begin_authoritative_tick();'):app.index('\n\t// Cost of the work a 60 Hz')]
messages = block(app, 'if (gameflow.mGameInterface && pc_coop_world_may_advance())')
assert app.index('pc_coop_world_may_advance()', app.index('// Begin authoritative tick')) < app.index('\n\tupdate();', app.index('// Begin authoritative tick'))
assert app.index('pc_render_end_presentation();', app.index('// Do not leak the read-only')) < app.index('\n\tgsys->waitRetrace();', app.index('// Do not leak the read-only'))
# Direct core callers must also encounter their hold guard BEFORE gameplay.
for signature, following in [('void GameCoreSection::update()', 'pcApplyPendingTutorialSkip();'), ('void GameCoreSection::updateAI()', 'pc_window_photo_mode_requested')]:
    method = block(core, signature)
    assert 'if (!pc_coop_world_may_advance())' in method
    if following in method: assert method.index('if (!pc_coop_world_may_advance())') < method.index(following)

test = r'''
#include "netplay/pc_coop_world_hooks.h"
#include "netplay/pc_netplay_present.h"
#include "timing/pc_render_phase.h"
#include <chrono>
#include <cstdio>
bool advance=true,guestContext=false;
bool pc_coop_world_may_advance(){return advance;}
bool pc_coop_world_has_guest(){return guestContext;}
bool pc_netplay_deterministic(){return false;}unsigned pc_netplay_tick(){return 0;}
static int failures=0, nodeUpdates=0, clockUpdates=0, visualClocks=0, gameplayNotes=0, aiUpdates=0, heldViews=0;
void check(bool ok,const char* why){if(!ok){std::printf("FAIL %s\n",why);++failures;}}
using u32=unsigned;using f32=float;
#define STACK_PAD_VAR(x) do{}while(false)
#define PRINT(...) do{}while(false)
enum {SYSHEAP_Movie, AYU_STACK_GROW_DOWN, MAX_DAYS=30, UPDATE_WORLD_CLOCK=1, UPDATE_AI=2};
constexpr bool TRUE=true,FALSE=false;
namespace CinePlayerFlags {constexpr unsigned NonGameMovie=1;}
enum {kPcTickWorldSim=0};
struct Clock {int mCurrentDay=2;float mTimeOfDay=8;void update(float){++clockUpdates;mTimeOfDay+=1;}};
struct Movie {bool mIsActive=false;};
struct Interface {int parsed=0;void parseMessages(){++parsed;}};
struct Flow {Movie movie;Movie*mMoviePlayer=&movie;Clock mWorldClock;Interface interface;Interface*mGameInterface=&interface;
 bool mIsUIOverlayActive=false,mIsTutorialTextActive=false,mPauseAll=false;unsigned mDemoFlags=0;}gameflow;
struct Player {bool isTutorial(){return false;}}player;Player*playerState=&player;
struct Heap {int getTopUsed(){return 0;}}heap;
struct System {bool mTogglePrint=false;bool resetPending(){return false;}Heap*getHeap(int){return &heap;}
 void resetHeap(int,int){}float getFrameTime(){return 1.0f/120.0f;}}systemState;System*gsys=&systemState;
struct Controller {int reads=0;unsigned mCurrentInput=0,mPrevInput=0,mInputPressed=0,mInputReleased=0,mInputDoublePressed=0;
 float mMainStickX=0,mMainStickY=0,mSubStickX=0,mSubStickY=0;void update(){++reads;}unsigned keyClick(unsigned key){return mInputPressed&key;}};
Controller*sP1Controller=nullptr,*sP2Controller=nullptr;unsigned sP1InputPressedRaw=0;
bool pc_coop_active(){return true;}bool pc_tick_profiler_enabled(){return false;}bool pc_settings_get_infinite_day(){return false;}
void pc_tick_profiler_record(int,double){}void pc_settings_note_gameplay_frame(){++gameplayNotes;}
void pcDiscordNoteGameplay(){}void pcWorkClockUpdate(Clock&,bool){++visualClocks;}void pcVisualClockUpdate(Clock&,bool){++visualClocks;}
struct Hud {int updates=0;void update(){++updates;}};
struct GameCoreSection {Hud hud[2];Hud*mDrawGameInfo=&hud[0],*mDrawGameInfo2=&hud[1];int setups=0;
 void pcUpdateCoopHeldView(){++heldViews;}void finalSetup(){++setups;}void updateAI(){++aiUpdates;}}core;
GameCoreSection*gamecore=&core;bool sGamecoreLive=true;
struct Node {static void update(){++nodeUpdates;}};
struct Mode {int updates=0;Mode*update(unsigned&){++updates;return this;}};
struct Menu {int updates=0;Menu*doUpdate(bool){++updates;return this;}};
struct Section:Node {
 int mMenuRepeatTimer=1;Controller controls[3];Controller*mController=&controls[0],*mPlayer2Controller=&controls[1],*mPlayer1Controller=&controls[2];
 bool mIsInitialSetup=false;Mode mode;Mode*mCurrentModeState=&mode,*mNextModeState=nullptr;Menu*mActiveMenu=nullptr;unsigned mUpdateFlags=UPDATE_AI|UPDATE_WORLD_CLOCK;
'''+update+'''
 void drawTail(){
'''+tail+'\n'+transition+'''
 }
};
enum {Leaf=0,Bud=1,Flower=2};
struct PikiMgr {int mesh[3]={};int*mLeafModel[3]={&mesh[0],&mesh[1],&mesh[2]};}pikis;
PikiMgr*pikiMgr=&pikis;
struct ViewPiki {int mHappa=Leaf;int*mHappaModel=nullptr;void syncMaturity(){
'''+maturity+'''
}};
enum {KBBTN_L=1,OBJTYPE_Navi=1};
struct Creature {int mObjType=OBJTYPE_Navi;};
struct Navi:Creature {int recentered=0,rotated=0;void pcCursorToFront(){++recentered;}void pcRotateCursor(float){++rotated;}};
bool pc_settings_get_free_camera(){return true;}
int recordedRotation=0;void pc_input_log_local_rotate_add(float){++recordedRotation;}
struct CameraControl {Creature*mTargetCreature=nullptr;bool detMode=false;int dragRoute=1;
 void recenter(Controller&controller){
'''+recenter+'''
 }
 void rotate(float cameraDrag){
'''+record_rotate+'\n'+rotate+'''
 }
};
struct Mouth {int mCentre=3;}mouth;
struct AttachedPiki {struct{int t=9;}mSRT;Mouth*mSwallowMouthPart=&mouth;void refreshPosition(){
'''+mouth+'''
}};
void beginFrame(){
'''+frame_begin+'''
}
void parseMessages(){
'''+messages+'''
}
int main(){
 Section section;Menu menu;Mode next;section.mActiveMenu=&menu;section.mNextModeState=&next;
 check(pc_coop_world_may_advance()&&pc_netplay_present_sim_side(),"ordinary play defaults to authoritative");
 advance=false;check(pc_netplay_present_begin_practice_view(1),"guest retains independently selected camera identity");
 for(int i=0;i<120;++i){
  section.mActiveMenu=(i%2)?&menu:nullptr;
  beginFrame();check(!pc_render_is_authoritative()&&!pc_netplay_present_sim_side(),"actual frame driver enters read-only phase before update");
  section.update();section.drawTail();parseMessages();pc_render_end_presentation();
 }
 check(nodeUpdates==0&&clockUpdates==0&&visualClocks==0&&aiUpdates==0&&gameplayNotes==0,"held frames do not advance world clock, Node tree, AI or gameplay work clocks");
 check(menu.updates==0&&next.updates==0&&section.mode.updates==0&&section.mNextModeState==&next&&section.mMenuRepeatTimer==1,"held input cannot trigger menu, mode, skip or queued day transition/timer");
 check(gameflow.interface.parsed==0,"held host/guest cannot process gameplay messages");
 check(heldViews==120&&section.controls[0].reads==120&&section.controls[1].reads==120&&section.controls[2].reads==120,"held frames continue collecting controls and update local view once");
 check(pc_netplay_present_local_player()==1,"render hold never changes local player identity");
 pc_render_begin_authoritative_tick();check(!pc_netplay_present_sim_side(),"legacy phase helper cannot grant guest simulation authority");
 section.mIsInitialSetup=true;section.drawTail();check(core.setups==0&&section.mIsInitialSetup,"early admitted world cannot run final setup on replica");section.mIsInitialSetup=false;
 advance=true;beginFrame();check(pc_render_is_authoritative()&&pc_netplay_present_sim_side(),"explicit host release resumes authoritative phase");
 Section initial;initial.mIsInitialSetup=true;initial.drawTail();check(core.setups==1&&!initial.mIsInitialSetup,"normal initial setup still runs once when host has authority");
 section.mActiveMenu=nullptr;section.update();section.drawTail();parseMessages();
 check(nodeUpdates==1&&clockUpdates==1&&aiUpdates==1&&gameflow.interface.parsed==1,"host release resumes exactly one normal world step and message pass");
 check(next.updates==1&&section.mNextModeState==nullptr,"host can consume its pending mode transition once");
 advance=false;beginFrame();section.update();section.drawTail();parseMessages();
 check(nodeUpdates==1&&clockUpdates==1&&aiUpdates==1&&gameflow.interface.parsed==1,"pause after running holds same world without extra gameplay steps");
 pc_render_end_presentation();pc_netplay_present_end_practice_view();advance=true;
 ViewPiki p;guestContext=true;
 for(int i=Leaf;i<=Flower;++i){p.mHappa=i;p.syncMaturity();check(p.mHappa==i&&p.mHappaModel==pikis.mLeafModel[i],"host maturity selects corresponding local leaf/bud/flower mesh without overriding host value");}
 p.mHappa=3;int*previous=p.mHappaModel;p.syncMaturity();check(p.mHappaModel==previous,"invalid maturity cannot index model array");
 p.mHappa=Leaf;guestContext=false;p.syncMaturity();check(p.mHappaModel==previous,"ordinary solo/host models are not overridden by guest presentation");
 guestContext=true;pikiMgr=nullptr;p.syncMaturity();check(p.mHappaModel==previous,"missing model manager during teardown cannot be dereferenced");
 Navi n;CameraControl camera;Controller control;control.mInputPressed=KBBTN_L;camera.mTargetCreature=&n;AttachedPiki attached;
 advance=false;camera.recenter(control);camera.rotate(1);camera.detMode=true;camera.rotate(1);attached.refreshPosition();
 check(n.recentered==0&&n.rotated==0&&recordedRotation==0&&attached.mSRT.t==9,"held camera/replay/attachment cannot write authoritative cursor, input log or replica position");
 advance=true;camera.detMode=false;camera.recenter(control);camera.rotate(1);camera.detMode=true;camera.rotate(1);attached.refreshPosition();
 check(n.recentered==1&&n.rotated==1&&recordedRotation==1&&attached.mSRT.t==3,"normal authoritative camera and mouth attachment behavior retained");
 if(!failures)std::puts("PASS actual gameplay update/draw/frame authority guards, held controls and mode/message barriers; native runtime still unverified");
 return failures?1:0;
}
'''
(out/'practice-authority-test.cpp').write_text(test, encoding='utf-8')
print('Generated actual gameplay authority fixture:', out)
