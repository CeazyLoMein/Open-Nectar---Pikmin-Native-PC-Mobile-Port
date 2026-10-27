"""Compile actual view-context code and changed camera/HUD/audio branches.

Controlled engine/graphics leaves record selection; this is not GPU rendering
or a complete guest-world/simulation validation.
"""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
pc=ROOT/'games/pikmin1/pc_port'
def block(text,signature):
 a=text.index(signature);b=text.index('{',a);i=b+1;level=1
 while level:level+=(text[i]=='{')-(text[i]=='}');i+=1
 return text[a:i]
(out/'Matrix4f.h').write_text('''#pragma once
class Matrix4f { public: float mMtx[4][4]{}; void makeIdentity(){for(int i=0;i<4;++i)for(int j=0;j<4;++j)mMtx[i][j]=i==j?1.0f:0.0f;} };
''')
(out/'Camera.h').write_text('''#pragma once
#include "Matrix4f.h"
class Camera { public: float mFov=60,mNear=100,mFar=10000,mAspectRatio=1;
 Matrix4f mPerspectiveMatrix,mProjectionMatrix,mLookAtMtx,mInverseLookAtMtx;
 int updates=0;void update(float aspect,float fov,float nearClip,float farClip){mAspectRatio=aspect;mFov=fov;mNear=nearClip;mFar=farClip;++updates;}
};
''')
(out/'Graphics.h').write_text('''#pragma once
#include "Camera.h"
class Graphics { public: Camera* mCamera=nullptr;int mScreenWidth=1200,mScreenHeight=800;void setCamera(Camera* c){mCamera=c;}void setViewport(int){}void setScissor(int){} };
''')
core=(ROOT/'games/pikmin1/src/plugPikiKando/gameCoreSection.cpp').read_text(encoding='utf-8')
game=(ROOT/'games/pikmin1/src/plugPikiColin/newPikiGame.cpp').read_text(encoding='utf-8')
methods='\n'.join(block(core,sig) for sig in ['Camera* GameCoreSection::getViewCamera(int view)','void GameCoreSection::drawGameInfoHud(Graphics& gfx)','void GameCoreSection::drawContainerWindows(Graphics& gfx)'])
audio=core[core.index('\n#if defined(PIKI_PC_PORT)\n\t// Online audio is local output'):core.index('\n\tgsys->mTimer->stop("se updt");',core.index('// Online audio is local output'))]
end_run=block((pc/'pc_coop.cpp').read_text(encoding='utf-8'),'void pc_coop_end_run(void)')
view_declarations=game[game.index('\t\tconst bool localSingleView ='):game.index('\n\t\tfor (int view = 0; view < mSplitViews;',game.index('\t\tconst bool localSingleView ='))]
camera=block(game,'if (localSingleView && pc_netplay_present_local_view_pass())')
test='''#include "Graphics.h"
#include "netplay/pc_netplay_present.h"
#include "timing/pc_render_phase.h"
#include <cstdio>
#include <cstdlib>
#include <cmath>
static bool deterministic=false,merge=true,firstPerson=false,worldAdvance=true;
bool pc_coop_world_may_advance(){return worldAdvance;}
bool hasGuest=false;bool pc_coop_world_has_guest(){return hasGuest;}
bool pc_netplay_deterministic(){return deterministic;}unsigned pc_netplay_tick(){return 0;}
void pc_netplay_present_restore_all_shapes(){}
static int failures=0;
void check(bool ok,const char* why){if(!ok){std::printf("FAIL %s\\n",why);++failures;}}
void envPlayer(const char* value){
#ifdef _WIN32
 _putenv_s("PIKMIN_NETPLAY_LOCAL_PLAYER",value);
#else
 setenv("PIKMIN_NETPLAY_LOCAL_PLAYER",value,1);
#endif
}
using f32=float;
#define AREA_FULL_SCREEN(gfx) 0
struct Vector3f{float x=0,y=0,z=0; Vector3f operator+(Vector3f b)const{return {x+b.x,y+b.y,z+b.z};}Vector3f operator*(float s)const{return {x*s,y*s,z*s};}};
struct Navi{Camera* mNaviCamera=nullptr;struct {Vector3f t;}mSRT;bool isAlive(){return true;}};
namespace zen {
struct GameInfo {};
struct DrawGameInfo {int full=0,player=0,shared=0,updates=0;GameInfo data;GameInfo* info(){return &data;}void update(){++updates;}void draw(Graphics&){++full;}void drawPlayer(Graphics&){++player;}void drawShared(Graphics&){++shared;}};
struct DrawContainer {int full=0;void draw(Graphics&){++full;}};
}
zen::DrawContainer box[2];zen::DrawContainer* containerWindow=&box[0];zen::DrawContainer* containerWindow2=&box[1];
struct Movie{bool mIsActive=false;void getLookAtPos(Vector3f& p){p={99,0,0};}}movie;
struct {Movie* mMoviePlayer=&movie;unsigned mDemoFlags=0;}gameflow;
struct CinePlayerFlags{enum{NonGameMovie=1};};
bool pc_settings_get_coop_merge_camera(){return merge;}int pc_settings_get_coop_split(){return 0;}
bool pc_first_person_active(){return firstPerson;}bool pc_coop_p2_tinted(){return false;}
void pc_coop_p2_tint(unsigned char* r,unsigned char* g,unsigned char* b){*r=*g=*b=255;}
float pc_gfx_get_window_aspect_ratio(){return 1.5f;}void pc_gfx_set_view_aspect_override(float){}
void pc_gfx_set_out_tint(float,float,float){}void pc_gfx_clear_out_tint(){}void pc_gfx_clear_view_subrect(){}void pc_gfx_set_hud_virtual_size(int,int){}
static int camleadCalls=0;Camera* pc_netplay_camlead_view(int,Camera* c){++camleadCalls;return c;}
struct Sound{int calls=0;Vector3f listener;void update(Graphics&,Vector3f p){++calls;listener=p;}}sound;Sound* seSystem=&sound;
struct PcamCameraManager {int updates=0;void update(){++updates;}};
PcamCameraManager managers[2];PcamCameraManager*cameraMgr=&managers[0],*sCameraMgrP1=nullptr;
struct System {float getFrameTime(){return 1.0f/120.0f;}}systemState;System*gsys=&systemState;
struct GameCoreSection {
 bool split=true;Navi* mNavi=nullptr;Navi* mNavi2=nullptr;Camera* mGameCamera2=nullptr;Camera mViewCam[2];
 zen::DrawGameInfo* mDrawGameInfo=nullptr;zen::DrawGameInfo* mDrawGameInfo2=nullptr;int mRenderPass=0,subrects=0;
 PcamCameraManager*mCameraMgr2=&managers[1];int splitUpdates=0;
 void fillHudInfo(zen::GameInfo*,Navi*){}
 void setActiveView(int);void pcUpdateCoopHeldView();void updateDynamicSplit(float){++splitUpdates;}
 bool isSplitScreen(){return split;}void setViewSubrect(int){++subrects;}void drawDownedLabel(Graphics&,Navi*,float){}
 Camera* getViewCamera(int);void drawGameInfoHud(Graphics&);void drawContainerWindows(Graphics&);void audio(Graphics&);
};
'''+methods+'\n'+block(core,'void GameCoreSection::setActiveView(int view)')+'\n'+block(core,'void GameCoreSection::pcUpdateCoopHeldView()')+'\nstatic bool sActive=true,sVsActive=true;\n'+end_run+'''
void GameCoreSection::audio(Graphics& gfx){bool advanceState=pc_render_is_authoritative();if(mRenderPass!=0)advanceState=false;
'''+audio+'''
}
bool sGamecoreLive=true;GameCoreSection* gamecore=nullptr;void* memcardWindow=nullptr;
struct Renderer {int mSplitViews=0;float mCameraFarClip=9000;void drawViews(Graphics& gfx){
'''+view_declarations+'''
 for(int view=0;view<mSplitViews;++view){if(sGamecoreLive&&gamecore)gamecore->mRenderPass=view;
'''+camera+'''
 }
}};
void resetOutputs(zen::DrawGameInfo* hud){for(int i=0;i<2;++i){hud[i]={};box[i]={};}sound={};camleadCalls=0;}
int main(){
 Camera cameras[2];Navi navis[2];zen::DrawGameInfo hud[2];Graphics gfx;Renderer renderer;GameCoreSection core;
 for(int i=0;i<2;++i){navis[i].mNaviCamera=&cameras[i];navis[i].mSRT.t={float(i*80),0,0};}
 core.mNavi=&navis[0];core.mNavi2=&navis[1];core.mGameCamera2=&cameras[1];core.mDrawGameInfo=&hud[0];core.mDrawGameInfo2=&hud[1];gamecore=&core;
 envPlayer("0");pc_netplay_present_reset_local_player();pc_render_begin_authoritative_tick();
 check(!pc_netplay_present_single_view()&&!pc_netplay_present_local_view_pass(),"normal play has no single-view override");
 check(!pc_netplay_present_begin_practice_view(-1)&&!pc_netplay_present_begin_practice_view(2),"invalid player identity leaves view inactive");
 check(core.getViewCamera(0)==&core.mViewCam[0]&&core.getViewCamera(1)==&core.mViewCam[1],"normal merged camera selection preserved");
 core.drawGameInfoHud(gfx);core.drawContainerWindows(gfx);core.audio(gfx);renderer.drawViews(gfx);
 check(hud[0].player==1&&hud[1].player==1&&hud[0].shared==1&&box[0].full==1&&box[1].full==1&&renderer.mSplitViews==2,"normal split-screen HUD and containers retain both players");
 check(sound.calls==1&&sound.listener.x==40,"normal split-screen audio keeps midpoint listener");
 for(int local=0;local<2;++local){
  resetOutputs(hud);merge=true;firstPerson=local==1;gfx.mCamera=nullptr;
  check(pc_netplay_present_begin_practice_view(local),"explicit practice view starts without legacy session");
  check(!pc_netplay_present_begin_practice_view(1-local)&&pc_netplay_present_local_player()==local,"nested request cannot replace active player");
  check(pc_netplay_present_single_view()&&pc_netplay_present_local_view_pass()&&!pc_netplay_present_two_pass_active()&&pc_netplay_present_sim_side(),"view selection does not enable lockstep or claim guest simulation is frozen");
  check(pc_netplay_present_local_player()==local,"authenticated role overrides old opposite launch preference");
  check(core.getViewCamera(local)==&cameras[local],"local own camera wins over saved merged-camera preference");
  renderer.drawViews(gfx);core.drawGameInfoHud(gfx);core.drawContainerWindows(gfx);core.audio(gfx);
  check(renderer.mSplitViews==1&&gfx.mCamera==&cameras[local]&&cameras[local].mAspectRatio==1.5f,"actual camera branch uses one full-screen local view");
  check(cameras[local].mNear==(firstPerson?3.0f:100.0f)&&camleadCalls==0,"personal clip mode preserved; legacy camlead not entered");
  check(hud[local].full==1&&hud[1-local].full==0&&box[local].full==1&&box[1-local].full==0,"only own HUD and Onion window drawn");
  check(sound.calls==1&&sound.listener.x==float(local*80),"sound listener follows own captain, not distant other player");
  check(merge&&firstPerson==(local==1)&&!deterministic,"view entry never overwrites personal merge/first-person settings or simulation mode");
  worldAdvance=false;pc_render_begin_presentation(1.0);int ownUpdates=managers[local].updates,otherUpdates=managers[1-local].updates;
  hasGuest=true;core.pcUpdateCoopHeldView();check(hud[0].updates==1 && hud[1].updates==1,"held guest HUD refreshes both replicated displays");hasGuest=false;
  check(managers[local].updates==ownUpdates+1&&managers[1-local].updates==otherUpdates&&cameraMgr==&managers[0]&&sCameraMgrP1==nullptr,"held world advances only local camera and restores legacy singleton");
  check(!pc_netplay_present_sim_side()&&pc_netplay_present_local_player()==local,"camera motion never releases held world or changes identity");
  pc_render_end_presentation();worldAdvance=true;
  movie.mIsActive=true;core.audio(gfx);check(sound.calls==2&&sound.listener.x==99,"movie audio still uses movie position");movie.mIsActive=false;
  pc_netplay_present_end_practice_view();check(!pc_netplay_present_single_view()&&pc_netplay_present_local_player()==0,"view exit restores prior player choice and normal local mode");
 }
 check(pc_netplay_present_begin_practice_view(1),"new view can begin after explicit teardown");pc_coop_end_run();
 check(!pc_netplay_present_single_view()&&!sActive&&!sVsActive,"actual game-run teardown clears local view and co-op flags");
 deterministic=true;pc_render_begin_authoritative_tick();
 check(!pc_netplay_present_begin_practice_view(1),"legacy deterministic session cannot acquire second view owner");
 resetOutputs(hud);check(pc_netplay_present_two_pass_active()&&!pc_netplay_present_local_view_pass(),"legacy authoritative pass still suppresses local-only output");
 check(core.getViewCamera(0)==&core.mViewCam[0],"legacy authoritative merged-camera selection remains unchanged");
 core.mRenderPass=0;core.drawGameInfoHud(gfx);core.drawContainerWindows(gfx);core.audio(gfx);check(hud[0].full==0&&box[0].full==0&&sound.calls==0,"legacy sim pass draws no HUD/Onion/audio");
 pc_render_begin_presentation(1.0);core.drawGameInfoHud(gfx);core.drawContainerWindows(gfx);core.audio(gfx);renderer.drawViews(gfx);
 check(hud[0].full==1&&box[0].full==1&&sound.calls==1&&camleadCalls==1,"legacy presentation retains local HUD/audio/camera-lead path");
 pc_render_end_presentation();deterministic=false;core.split=false;resetOutputs(hud);core.drawGameInfoHud(gfx);core.drawContainerWindows(gfx);
 check(hud[0].full==1&&box[0].full==1&&hud[1].full==0&&box[1].full==0,"ordinary solo output preserved after context teardown");
 gamecore=nullptr;sGamecoreLive=false;renderer.drawViews(gfx);check(renderer.mSplitViews==1,"missing world never selects a local captain camera");
 if(!failures)std::puts("PASS actual independent view context and camera/HUD/Onion/audio branches; solo/local split/legacy pass behavior retained");
 return failures?1:0;
}
'''
(out/'practice-view-test.cpp').write_text(test,encoding='utf-8')
print('Generated actual practice-view/camera/HUD/audio branch fixture:',out)
