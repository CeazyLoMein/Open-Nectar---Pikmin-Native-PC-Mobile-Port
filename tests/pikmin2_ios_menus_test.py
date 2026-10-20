from pathlib import Path
import re,sys
repo=Path(__file__).resolve().parents[1]
def read(name):return (repo/name).read_text(encoding='utf-8')
def fn(s,signature):
 start=s.index(signature)
 while s.find(';',start,s.index('{',start))>=0: start=s.index(signature,start+len(signature))
 brace=s.index('{',start);depth=0
 for m in re.finditer(r'//[^\n]*|/\*[\s\S]*?\*/|"(?:\\.|[^"\\])*"|\x27(?:\\.|[^\x27\\])*\x27|[{}]',s[brace:]):
  token=m.group()
  if token=='{':depth+=1
  elif token=='}':
   depth-=1
   if depth==0:return s[start:brace+m.end()]
 raise AssertionError(signature)
gfx=read('games/pikmin2/pc_port/gl/pc_gfx.cpp');settings=read('games/pikmin2/pc_port/settings/pc_settings.cpp')
touch=read('games/pikmin2/pc_port/touch/pc_touch.cpp');option=read('games/pikmin2/pikmin2-decomp/src/plugProjectEbisawaU/ebiScreenOption.cpp')
menu=read('games/pikmin2/pikmin2-decomp/src/plugProjectOgawaU/ogMenuMgr.cpp');modal=read('games/pikmin2/pikmin2-decomp/src/plugProjectOgawaU/ogObjSMenuPauseVs.cpp')
window=read('games/pikmin2/pc_port/pc_window.cpp')
title=read('games/pikmin2/pikmin2-decomp/src/plugProjectEbisawaU/ebiScreenTitleMenu.cpp')
for signature in ['void TTitleMenu::doOpenScreen(ArgOpen* arg)','void TTitleMenu::doDraw()']:
 assert 'pc_touch_claim_game_menu();' in fn(title,signature)
assert '#if defined(__ANDROID__) || defined(__IPHONEOS__)' in fn(settings,'void pc_settings_p2_begin_frame')
assert 'sGameMenuClaimFrames <= 0' in touch[touch.index('void pc_touch_on_finger'):touch.index('static u16 sLastPadButtons')]
assert 'pcOptionSelectRow(*this, pcTap)' in fn(option,'bool TOption::doUpdateStateWait()')
assert 'pcTap.row == 6 && !pcRowChanged' in option
assert 'if (pcTap.value >= 0) mWindowCursor.mCounter = 0;' in option
assert 'pc_touch_claim_menu_confirm();' in fn(modal,'bool ObjSMenuPauseVS::menu()')
assert gfx.count('sCurrentAspectRatio = ios_native_settings_frame() ? windowAspect')==2
frame=fn(gfx,'void pc_gfx_begin_frame(void)')
assert frame.index('PcGfxHostAllocScope hostAllocScope;')<frame.index('ios_native_settings_frame(true);')
budget=frame[frame.index('SDL_Window* window ='):frame.index('        if (wantedWidth !=')]
layout=settings[settings.index('constexpr int kF1TabH'):settings.index('void f1Layout()')]+fn(settings,'void f1Layout()')
# The real renderer's centered transform is inverted by the actual F1 tap helper.
ui=fn(gfx,'void pc_gfx_ui_draw(');mapcode=ui[ui.index('    const float scale ='):ui.index('    static std::vector')]
flags=window[window.index('SDL_WINDOW_OPENGL | SDL_WINDOW_SHOWN | SDL_WINDOW_RESIZABLE'):window.index('        );',window.index('SDL_WINDOW_OPENGL | SDL_WINDOW_SHOWN | SDL_WINDOW_RESIZABLE'))]
cpp=r'''
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <vector>
#include <utility>
int checks=0;
#define CHECK(x) do { ++checks; assert(x); } while(false)
#ifndef P2_TEST_DESKTOP
#ifndef __APPLE__
#define __APPLE__ 1
#endif
#ifndef __IPHONEOS__
#define __IPHONEOS__ 1
#endif
#undef TARGET_OS_IPHONE
#define TARGET_OS_IPHONE 1
#endif
#define PIKI_PC_SETTINGS_MENU 1
#define PIKI_PC_TOUCH 1
namespace render {
using GLint=int;
int drawableW=2796,drawableH=1290,pointWidth=932,pointHeight=430;
bool sMenuOpen=false; int sGameMenuClaimFrames=0;
void pc_gfx_get_drawable_size(int* w,int* h){*w=drawableW;*h=drawableH;}
'''
cpp+=fn(settings,'int pc_settings_menu_is_open(')+'\n'+fn(touch,'bool pc_touch_menu_active(')+'\n'+fn(gfx,'static bool ios_native_settings_frame(')+'\n'
cpp+=r'''
struct SDL_Window{} fakeWindow;
SDL_Window* SDL_GL_GetCurrentWindow(){return &fakeWindow;}
void SDL_GL_GetDrawableSize(SDL_Window*,int* w,int* h){*w=drawableW;*h=drawableH;}
void SDL_GetWindowSize(SDL_Window*,int* w,int* h){*w=pointWidth;*h=pointHeight;}
bool sNativeFramebufferReady=true; int sDrawableWidth=0,sDrawableHeight=0;
int sAspectRatioMode=0,sRenderResolutionW=640,sRenderResolutionH=480;
float sCurrentAspectRatio=0,sRenderScale=.75f;
float calculate_aspect_ratio(int mode,float aspect){return mode ? 4.f/3.f : aspect;}
'''
cpp+=fn(gfx,'static void calculate_output_area(')+'\n' if 'static void calculate_output_area(' in gfx else fn(gfx,'void calculate_output_area(')+'\n'
cpp+='std::pair<int,int> renderSize(){\n'+budget+'return {wantedWidth,wantedHeight};\n}\nreturn {0,0};\n}\n'
cpp+='constexpr int PC_SET_GROUP_COUNT=9;\n'+layout+'\n'+fn(settings,'void f1TapToCanvas(')+'\n'
cpp+='std::pair<float,float> forward(float x,float y){int w=drawableW,h=drawableH,virtW=kF1CanvasW,virtH=kF1CanvasH;\n'+mapcode+'\nreturn {(ox+x*scale)/w,(oy+y*scale)/h};}\n'
cpp+='enum {SDL_WINDOW_OPENGL=1,SDL_WINDOW_SHOWN=2,SDL_WINDOW_RESIZABLE=4,SDL_WINDOW_ALLOW_HIGHDPI=8,SDL_WINDOW_FULLSCREEN=16};\nint windowFlags(){return '+flags+';\n}\n'
cpp+=r'''
void run(){
 sMenuOpen=false; ios_native_settings_frame(true);
 auto base=renderSize();
#ifdef __IPHONEOS__
 CHECK(base.first==480 && base.second==221); // explicit resolution + .75; same pre-Retina budget
 CHECK(windowFlags() & SDL_WINDOW_ALLOW_HIGHDPI);
 sRenderResolutionW=sRenderResolutionH=0; base=renderSize(); CHECK(base.first==699 && base.second==323);
 sMenuOpen=true; CHECK(!ios_native_settings_frame()); // transition waits for next frame
 ios_native_settings_frame(true); auto native=renderSize(); CHECK(native.first==2796 && native.second==1290);
 sRenderResolutionW=640;sRenderResolutionH=480;sAspectRatioMode=1;sRenderScale=.5f;
 native=renderSize();CHECK(native.first==2796 && native.second==1290);
 sMenuOpen=false; CHECK(ios_native_settings_frame()); // present retains allocated aspect
 ios_native_settings_frame(true); CHECK(!ios_native_settings_frame());
 auto restored=renderSize();CHECK(restored.first==320 && restored.second==240);
 sGameMenuClaimFrames=3;ios_native_settings_frame(true);CHECK(ios_native_settings_frame());
 sGameMenuClaimFrames=0;ios_native_settings_frame(true);CHECK(!ios_native_settings_frame());
#else
 CHECK(base.first==480 && base.second==221); CHECK(!(windowFlags() & SDL_WINDOW_ALLOW_HIGHDPI));
 sMenuOpen=true;ios_native_settings_frame(true);CHECK(!ios_native_settings_frame());
#endif
 for(auto size: {std::pair<int,int>{2796,1290},{1290,2796},{1920,1080},{0,0}}){
  drawableW=size.first;drawableH=size.second;f1Layout();
#ifdef __IPHONEOS__
  CHECK(kF1CanvasH==400 && kF1PanelX==56 && kF1PanelY==8);
#else
  CHECK(kF1CanvasH==480 && kF1CanvasW==640);
#endif
  CHECK(kF1PanelW>0 && kF1PanelH>0 && kF1Visible>0);
  // Exercise imported menu metrics too: Clang diagnoses unused constants.
  // Tab text must stop above the list, and all eight option rows must fit.
  CHECK(kF1TabY+kF1TabH<=kF1ColY);
  CHECK(16+kF1OptVisible*kF1OptH<=kF1ColH);
  if(drawableW<=0)continue;
  for(int y=kF1ColY;y<kF1ColY+kF1ColH;y+=22){
   for(int x: {kF1LeftX+8,kF1RightX+8,kF1PanelX+kF1PanelW-20}){
    auto p=forward(float(x),float(y));int a,b;f1TapToCanvas(p.first,p.second,&a,&b);
    CHECK(std::abs(a-x)<=1 && std::abs(b-y)<=1);
   }
  }
 }
}
} // render
namespace touchCase {
using u16=unsigned short;using u32=unsigned;using f32=float;
enum { BTN_BACK=0,BTN_MENU_CONFIRM=1,BTN_THROW=2,BTN_SETTINGS=3 };
int sGameMenuClaimFrames=0,sPortMenuClaimFrames=0,sMenuStickFrames=0;
unsigned sMenuWantedButtons=0;
bool sGameMenuTapPending=false;int sGameMenuTapAge=0;float sGameMenuTapX=0,sGameMenuTapY=0;
int width=1000,height=500;
void pc_gfx_get_drawable_size(int* w,int* h){*w=width;*h=height;}
'''
cpp+='struct ButtonState {float cx,cy,r;};\nconstexpr int BTN_COUNT=4;\nButtonState sButtons[BTN_COUNT]={{10,10,2},{20,10,2},{30,10,2},{40,10,2}};\nbool button_modded_off(int){return false;}\n'
for signature in ['bool menu_button_allowed(','void pc_touch_claim_game_menu(','void pc_touch_claim_menu_confirm(','bool pc_touch_menu_active(','void pc_touch_menu_uses_stick(','bool pc_touch_take_game_menu_tap(']:cpp+=fn(touch,signature)+'\n'
cpp+=fn(touch,'int button_at(')+'\n'
tracked=touch[touch.index('struct TrackedPane {'):touch.index('} // namespace',touch.index('struct TrackedPane {'))]
cpp+=tracked+'\n'
for signature in ['void pc_touch_pane_drawn(','bool pc_touch_pane_rect(','bool pc_touch_pane_hit(']:cpp+=fn(touch,signature)+'\n'
cpp+=r'''
void tick(){
'''
for name in ['sGameMenuClaimFrames','sPortMenuClaimFrames','sMenuStickFrames']:cpp+=f'if ({name}>0) --{name};\n'
cpp+=r'''
}
struct J2DPane {float x0,y0,x1,y1;};
void track(J2DPane* p){pc_touch_pane_hit(p,0,0,0);pc_touch_pane_drawn(p,p->x0,p->y0,p->x1,p->y1);}
void tap(float x,float y){sGameMenuTapPending=true;sGameMenuTapX=x/width;sGameMenuTapY=y/height;}
namespace ebi {
struct EUTPadInterface_countNum {int mMinSel=0,mMaxSel=10,*mSelIndex=nullptr,mLastIndex=0;bool mSelectionChanged=false;};
namespace Screen {
struct TOption {
 bool mEnabled=true;int mCurrMainSelection=1;EUTPadInterface_countNum mInputMainSel;
 J2DPane* mButtonPaneList[7]={};J2DPane *mPaneRumbleYes=nullptr,*mPaneRumbleNo=nullptr,*mPaneSoundType[3]={};
 J2DPane *mPaneBgmVolume[10]={},*mPaneSfxVolume[10]={},*mPaneDeflickerYes=nullptr,*mPaneDeflickerNo=nullptr;
 TOption(){mInputMainSel.mMinSel=1;mInputMainSel.mMaxSel=6;mInputMainSel.mSelIndex=&mCurrMainSelection;}
};}}
'''
cpp+=option[option.index('struct PcOptionTap {'):option.index('} // namespace',option.index('struct PcOptionTap {'))]+'\n'
cpp+=r'''
struct MenuMgr {int mElementCount=2;J2DPane **mTextBoxPanes=nullptr,**mTextBoxTakuPanes=nullptr,**mMainPanes=nullptr;
 int pcTouchTappedOption(bool,f32,f32)const;void select(int){}void killCursor(){}
};
'''
cpp+=fn(menu,'int MenuMgr::pcTouchTappedOption(')+'\n'
cpp+=r'''
struct Controller {enum {PRESS_UP=1,PRESS_DOWN=2,PRESS_A=4,PRESS_B=8,PRESS_START=16};unsigned buttons=0;unsigned getButtonDown(){return buttons;}};
struct Sys{float mDeltaTime=.033f;} system;Sys* sys=&system;
struct Sound{void setDecide(){}void setClose(){}} sound;Sound* ogSound=&sound;
struct ObjSMenuPauseVS {
 bool mMenuOpen=true;float mMenuTimer=0;int mCurrMenuSel=0,result=-1;MenuMgr* mMenuMgr;Controller controller;
 bool menu();Controller* getGamePad(){return &controller;}void blink_Menu(int){}
 void out_menu_0(){result=0;}void out_menu_1(){result=1;}void out_cancel(){result=-2;}
};
'''
cpp+=fn(modal,'bool ObjSMenuPauseVS::menu()')+'\n'
cpp+=r'''
void run(){
 CHECK(menu_button_allowed(BTN_BACK));CHECK(!menu_button_allowed(BTN_MENU_CONFIRM));CHECK(!menu_button_allowed(BTN_THROW));
 CHECK(menu_button_allowed(BTN_SETTINGS));
 pc_touch_claim_game_menu();CHECK(menu_button_allowed(BTN_MENU_CONFIRM));CHECK(menu_button_allowed(BTN_SETTINGS));
 CHECK(button_at(40,10)==BTN_SETTINGS);CHECK(button_at(20,10)==BTN_MENU_CONFIRM);CHECK(button_at(30,10)==-1);
 CHECK(!menu_button_allowed(BTN_THROW));
 for(int i=0;i<3;++i)tick();CHECK(!menu_button_allowed(BTN_MENU_CONFIRM));
 sMenuWantedButtons=1u<<BTN_THROW;CHECK(menu_button_allowed(BTN_THROW));
 pc_touch_claim_menu_confirm();CHECK(menu_button_allowed(BTN_MENU_CONFIRM)&&pc_touch_menu_active());
 for(int i=0;i<3;++i)tick();CHECK(!menu_button_allowed(BTN_MENU_CONFIRM)&&!pc_touch_menu_active());
 ebi::Screen::TOption screen;J2DPane rows[7];
 for(int i=0;i<7;++i){rows[i]={100.f,float(40+i*40),600.f,float(65+i*40)};screen.mButtonPaneList[i]=&rows[i];}
 J2DPane no{460,80,510,105},yes{400,80,450,105},mode{460,120,510,145};
 screen.mPaneRumbleNo=&no;screen.mPaneRumbleYes=&yes;screen.mPaneSoundType[2]=&mode;
 (void)pcOptionTouch(screen); // register panes before the draw
 for(int i=0;i<7;++i)track(&rows[i]);track(&no);track(&yes);track(&mode);
 tap(480,90);auto hit=pcOptionTouch(screen);CHECK(hit.row==1&&hit.value==0);CHECK(!pcOptionSelectRow(screen,hit));
 tap(480,130);hit=pcOptionTouch(screen);CHECK(hit.row==2&&hit.value==2);CHECK(pcOptionSelectRow(screen,hit));
 CHECK(screen.mCurrMainSelection==2 && screen.mInputMainSel.mLastIndex==1 && screen.mInputMainSel.mSelectionChanged);
 int value=0;ebi::EUTPadInterface_countNum count;count.mSelIndex=&value;count.mMaxSel=2;
 pcOptionSetCount(count,2);CHECK(value==2&&count.mLastIndex==0&&count.mSelectionChanged);
 count.mSelectionChanged=false;pcOptionSetCount(count,3);CHECK(value==2&&!count.mSelectionChanged);
 pcOptionSetCount(count,-1);CHECK(value==2&&!count.mSelectionChanged);
 tap(200,285);hit=pcOptionTouch(screen);CHECK(hit.row==6&&hit.value==-1);
 bool changed=pcOptionSelectRow(screen,hit);CHECK(changed && !(hit.row==6&&!changed));
 tap(200,285);hit=pcOptionTouch(screen);changed=pcOptionSelectRow(screen,hit);CHECK(!changed&&(hit.row==6&&!changed));
 screen.mEnabled=false;tap(200,90);hit=pcOptionTouch(screen);CHECK(hit.row==-1&&sGameMenuTapPending);
 sGameMenuTapPending=false;
 // A callback-owned text pane may be invisible; visible row bounds must still hit.
 J2DPane hidden{100,300,500,325},first{100,300,500,325},second{100,350,500,375};
 J2DPane* texts[2]={&hidden,nullptr};J2DPane* rowPanes[2]={&first,&second};
 MenuMgr mgr;mgr.mTextBoxTakuPanes=texts;mgr.mMainPanes=rowPanes;
 mgr.pcTouchTappedOption(false,0,0);track(&first);track(&second);
 CHECK(mgr.pcTouchTappedOption(true,.2f,.62f)==0);CHECK(mgr.pcTouchTappedOption(true,.2f,.72f)==1);
 CHECK(mgr.pcTouchTappedOption(false,.2f,.62f)==-1);
 ObjSMenuPauseVS dialog;dialog.mMenuMgr=&mgr;
 tap(200,360);CHECK(!dialog.menu()&&dialog.mCurrMenuSel==1&&dialog.result==-1);
 tap(200,360);CHECK(dialog.menu()&&dialog.result==1);
 dialog.result=-1;dialog.mCurrMenuSel=1;tap(200,310);CHECK(!dialog.menu()&&dialog.mCurrMenuSel==0&&dialog.result==-1);
 dialog.controller.buttons=Controller::PRESS_A;CHECK(dialog.menu()&&dialog.result==0);
 dialog.result=-1;dialog.controller.buttons=Controller::PRESS_B;CHECK(dialog.menu()&&dialog.result==-2);
 sTouchFrame+=3;CHECK(mgr.pcTouchTappedOption(true,.2f,.72f)==-1); // stale/hidden panes are not clickable
}
} // input
int main(){render::run();touchCase::run();std::printf("PASS: %d checks on actual Retina/menu budget, layout/tap inverse, original options and modal code\n",checks);}
'''
Path(sys.argv[1]).write_text(cpp,encoding='utf-8')
print('Generated actual-code iOS menu/render and options/modal fixture; desktop variant supported.')
