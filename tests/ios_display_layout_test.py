"""Exercise actual P1/P2 menu, touch layout and editor code across changing windows."""
from pathlib import Path
import plistlib,re,sys
repo=Path(__file__).resolve().parents[1]
def fn(s,signature):
 start=s.index(signature);brace=s.index('{',start);depth=0
 for m in re.finditer(r'//[^\n]*|/\*[\s\S]*?\*/|"(?:\\.|[^"\\])*"|\x27(?:\\.|[^\x27\\])*\x27|[{}]',s[brace:]):
  if m.group()=='{':depth+=1
  elif m.group()=='}':
   depth-=1
   if depth==0:return s[start:brace+m.end()]
 raise AssertionError(signature)
plist=plistlib.loads((repo/'ios/Info.plist.in').read_bytes())
assert plist['CADisableMinimumFrameDurationOnPhone'] is True
assert set(plist['UISupportedInterfaceOrientations'])=={'UIInterfaceOrientationLandscapeLeft','UIInterfaceOrientationLandscapeRight'}
cpp=r'''
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#define __IPHONEOS__ 1
'''
cpp+='#include "'+(repo/'games/pikmin2/pc_port/pc_mobile_layout.h').as_posix()+'"\n'
cpp+=r'''
PcMobileInsets testInsets;
PcMobileInsets pc_mobile_safe_insets(){return testInsets;}
int checks=0;
#define CHECK(x) do {++checks; if(!(x)){std::fprintf(stderr,"failed line %d: %s\n",__LINE__,#x);std::abort();}}while(false)
bool near(float a,float b){return std::fabs(a-b)<.01f;}
'''
for game in ['pikmin1','pikmin2']:
 port=repo/'games'/game/'pc_port'
 touch=(port/'touch/pc_touch.cpp').read_text(encoding='utf-8')
 settings=(port/'settings/pc_settings.cpp').read_text(encoding='utf-8')
 assert '120 FPS (experimental)' in settings
 assert 'else if (key == "fpsMode")' in settings
 cpp+='namespace '+game+' {\n'
 # Import the real button specifications and persisted layout units.
 cpp+='using u16=unsigned short;\n'
 for name in sorted(set(re.findall(r'PAD_\w+',touch[touch.index('const ButtonSpec kButtons'):touch.index('constexpr float kStickRadius')]))):
  cpp+='constexpr u16 '+name+'=0;\n'
 cpp+=touch[touch.index('enum ButtonId {'):touch.index('// ── Disposición personalizable')]
 cpp+=touch[touch.index('struct ButtonLayout {'):touch.index('bool sLayoutLoaded')]
 cpp+=r'''
constexpr int TOOL_COUNT=4,kGridCells=16,PC_SET_GROUP_COUNT=9;
int sLayoutW=0,sLayoutH=0; bool sLayoutDirty=true,sEditGrid=false;
int sEditDragFinger=-1,sEditToolFinger=-1,sEditDragButton=-1,sEditToolPressed=-1;
struct ButtonState {long long finger=-1;bool tapLatch=false;float cx=0,cy=0,r=0;};
ButtonState sButtons[BTN_COUNT];
struct Stick {int finger=-1;float dx=0,dy=0,radius=0;}sStick;
struct Finger {int finger=-1;}sRightGesture[2],sSwipes[6],sMenuDrag;
using GestureFinger=Finger;using SwipeFinger=Finger;
struct Group {bool dragging=false;}sGroupDrag;
float sPinchDistance=-1;bool sGameMenuTapPending=false;
u16 sQueuedGameButtons=0,sPreviousMenuButtons=0,sSwipeButtons=0;
int sSwipeHoldFrames=0,sColorTapFinger=-1;
struct Tool {float cx=0,cy=0,r=0;}sTools[TOOL_COUNT];
PcMobileFrame sSafeFrame {0,0,1,1,1};
void layout_load(){}
int drawableW=0,drawableH=0;
void pc_gfx_get_drawable_size(int* w,int* h){*w=drawableW;*h=drawableH;}
'''
 for sig in ['void cancel_geometry_touches()','void layout(int w, int h)','void layout_place(int i, float px, float py)']:
  cpp+=fn(touch,sig)+'\n'
 # Import live renderer size queries so resize-before-begin_frame is tested too.
 gfx=(port/'gl/pc_gfx.cpp').read_text(encoding='utf-8')
 cpp+='namespace drawable {\nstruct SDL_Window{} fakeWindow;\nSDL_Window* SDL_GL_GetCurrentWindow(){return &fakeWindow;}\nvoid SDL_GL_GetDrawableSize(SDL_Window*,int* w,int* h){*w=drawableW;*h=drawableH;}\nint sDrawableWidth=1,sDrawableHeight=1;\n'
 cpp+=fn(gfx,'void pc_gfx_get_drawable_size(int* width, int* height)')+'\n}\n'
 window=(port/'pc_window.cpp').read_text(encoding='utf-8')
 setter=fn(window,'void pc_window_set_window_size(int w, int h)')
 setter=setter[:setter.index('#ifdef __ANDROID__')]+'}\n'
 cpp+='namespace windowCase {\nint fakeWindow=1;int* sWindow=&fakeWindow;int sWindowWidth=1,sWindowHeight=1,rw=0,rh=0;\nvoid pc_gfx_set_render_resolution(int w,int h){rw=w;rh=h;}\nvoid SDL_GetWindowSize(int*,int* w,int* h){*w=drawableW/3;*h=drawableH/3;}\n'
 cpp+=setter+'}\n'
 cpp+=settings[settings.index('constexpr int kF1TabH'):settings.index('void f1Layout()')]+fn(settings,'void f1Layout()')+'\n'
 cpp+=r'''
void run(){
 (void)kStickDead; (void)kLayerAlpha;
 for(int i=0;i<BTN_COUNT;++i)sLayout[i]={kButtons[i].cx,kButtons[i].cy,kButtons[i].fromRight,1};
 for(auto size: {std::pair<int,int>{2796,1290},{2670,1878},{2034,1398},{1920,1080},{1136,640},{600,600}}){
  for(int rotation=0;rotation<2;++rotation){
   testInsets=rotation ? PcMobileInsets{.02f,.01f,.06f,.04f} : PcMobileInsets{.06f,.01f,.02f,.04f};
   drawableW=size.first;drawableH=size.second;
   sButtons[BTN_THROW].finger=7;sStick.finger=8;sStick.dx=12;sRightGesture[0].finger=9;
   const bool hadLayout=sLayoutW>0;
   layout(drawableW,drawableH);
   if(hadLayout)CHECK(sButtons[BTN_THROW].finger==-1&&sStick.finger==-1&&sStick.dx==0&&sRightGesture[0].finger==-1);
   for(int i=0;i<BTN_COUNT;++i){
    const auto& b=sButtons[i];
    CHECK(b.cx-b.r>=sSafeFrame.x-.01f&&b.cx+b.r<=sSafeFrame.x+sSafeFrame.w+.01f);
    CHECK(b.cy-b.r>=sSafeFrame.y-.01f&&b.cy+b.r<=sSafeFrame.y+sSafeFrame.h+.01f);
    CHECK(near(sLayout[i].cx,kButtons[i].cx)&&near(sLayout[i].cy,kButtons[i].cy));
   }
   // Editing and reflow share one inverse; changing displays never saves new coordinates.
   const auto before=sLayout[BTN_THROW];
   const float x=sSafeFrame.x+sSafeFrame.w*.7f,y=sSafeFrame.y+sSafeFrame.h*.6f;
   layout_place(BTN_THROW,x,y);sLayoutDirty=true;layout(drawableW,drawableH);
   CHECK(near(sButtons[BTN_THROW].cx,x)&&near(sButtons[BTN_THROW].cy,y));
   const auto edited=sLayout[BTN_THROW];layout(drawableW*2,drawableH*2);
   CHECK(near(sButtons[BTN_THROW].cx,x*2)&&near(sButtons[BTN_THROW].cy,y*2));
   CHECK(near(sLayout[BTN_THROW].cx,edited.cx)&&near(sLayout[BTN_THROW].cy,edited.cy));
   sLayout[BTN_THROW]=before;sLayoutDirty=true;layout(drawableW,drawableH);
   // No dimension change: ordinary held controls must remain held.
   sButtons[BTN_THROW].finger=10;layout(drawableW,drawableH);CHECK(sButtons[BTN_THROW].finger==10);
   windowCase::pc_window_set_window_size(640,480);
   CHECK(windowCase::rw==640&&windowCase::rh==480);
   CHECK(windowCase::sWindowWidth==drawableW/3&&windowCase::sWindowHeight==drawableH/3);
   int w,h;drawable::pc_gfx_get_drawable_size(&w,&h);CHECK(w==drawableW&&h==drawableH);
   f1Layout();
   CHECK(kF1PanelW>=580&&kF1PanelH>280&&kF1Visible>0);
   CHECK(kF1TabY+kF1TabH<=kF1ColY&&16+kF1OptVisible*kF1OptH<=kF1ColH);
   CHECK(kF1TabW>0&&kF1RightW>0);
   CHECK(std::fabs(float(kF1CanvasW)/kF1CanvasH-float(drawableW)/drawableH)<.002f);
   const auto sf=pc_mobile_frame(float(kF1CanvasW),float(kF1CanvasH),testInsets);
   CHECK(kF1PanelX>=sf.x&&kF1PanelY>=sf.y);
   CHECK(kF1PanelX+kF1PanelW<=sf.x+sf.w&&kF1PanelY+kF1PanelH<=sf.y+sf.h);
  }
 }
 // A stationary-size safe-area change must update layout and release old touches.
 const float old=sButtons[BTN_PAUSE].cx;testInsets.left=.12f;sButtons[BTN_PAUSE].finger=11;
 layout(drawableW,drawableH);CHECK(sButtons[BTN_PAUSE].cx>old&&sButtons[BTN_PAUSE].finger==-1);
 // Grid snapping at the safe edges stays visible and round-trips.
 sEditGrid=true;layout_place(BTN_THROW,-100,-100);const float x=sButtons[BTN_THROW].cx,y=sButtons[BTN_THROW].cy;
 sLayoutDirty=true;layout(drawableW,drawableH);CHECK(near(sButtons[BTN_THROW].cx,x)&&near(sButtons[BTN_THROW].cy,y));
}
}
'''
cpp+='int main(){pikmin1::run();pikmin2::run();std::printf("PASS: %d actual-code display, safe touch, editor, resize and saved-layout checks; landscape/120 FPS metadata valid\\n",checks);}\n'
Path(sys.argv[1]).write_text(cpp,encoding='utf-8')
print('Generated actual P1/P2 adaptive display integration fixture.')
