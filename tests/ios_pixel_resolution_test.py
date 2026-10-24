"""Generate actual P1/P2 resolution-list/window/render-budget regression; no game assets."""
from pathlib import Path
import argparse,re,subprocess

p=argparse.ArgumentParser();p.add_argument('output',type=Path);p.add_argument('--ref');a=p.parse_args()
r=Path(__file__).resolve().parents[1]
def read(game,file):
 path=Path('games')/game/'pc_port'/file
 return subprocess.check_output(['git','show',a.ref+':'+path.as_posix()],cwd=r,text=True,encoding='utf-8') if a.ref else (r/path).read_text(encoding='utf-8')
def fn(s,signature):
 start=s.index(signature);brace=s.index('{',start);depth=0
 for m in re.finditer(r'//[^\n]*|/\*[\s\S]*?\*/|"(?:\\.|[^"\\])*"|\x27(?:\\.|[^\x27\\])*\x27|[{}]',s[brace:]):
  if m.group()=='{':depth+=1
  elif m.group()=='}':
   depth-=1
   if depth==0:return s[start:brace+m.end()]
 raise AssertionError(signature)
cpp=r'''
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <utility>
#define __IPHONEOS__ 1
int checks=0;
#define CHECK(x) do{++checks;if(!(x)){std::fprintf(stderr,"line%d: %s\n",__LINE__,#x);std::abort();}}while(false)
'''
for game in ['pikmin1','pikmin2']:
 settings=read(game,'settings/pc_settings.cpp');gfx=read(game,'gl/pc_gfx.cpp');window=read(game,'pc_window.cpp')
 cpp+='namespace '+game+' {\n'
 cpp+=r'''
struct Resolution{int w,h;bool isNative,isDerived;};
std::vector<Resolution>sResolutions;
int sDesktopW=0,sDesktopH=0,dw=2034,dh=1398,queries=0;
struct Config{int windowWidth=466,windowHeight=678,fpsMode=2;float renderScale=1;int sentinel=47;}sConfig,sPending;
struct SDL_DisplayMode{int w=466,h=678;};
int pc_window_get_display_index(){return 0;}
int SDL_GetDesktopDisplayMode(int,SDL_DisplayMode*){++queries;return 0;}
int SDL_GetNumDisplayModes(int){return 1;}
int SDL_GetDisplayMode(int,int,SDL_DisplayMode*){return 0;}
void pc_gfx_get_drawable_size(int*w,int*h){*w=dw;*h=dh;}
constexpr int PC_WINDOW_FULLSCREEN_EXCLUSIVE=1;
'''
 for signature in ['void addResolution(int w, int h, bool derived)','void rebuildResolutionList()',
                   'bool resolutionSelectable(const Resolution& r, int displayMode)',
                   'int resolutionIndexFor(int w, int h)','int defaultResolutionIndex()']:
  cpp+=fn(settings,signature)+'\n'
 start=settings.index('    int idx = sHadConfigFile ? resolutionIndexFor',settings.index('void pc_settings_init(void)'))
 end=settings.index('    sResolutionIdx = idx;',start)+len('    sResolutionIdx = idx;')
 cpp+='void migrate(){bool sHadConfigFile=true;int sResolutionIdx=-1;\n'+settings[start:end]+'\nCHECK(sResolutionIdx>=0);}\n'
 cpp+=r'''
struct SDL_Window{} fakeWindow;SDL_Window*sWindow=&fakeWindow;
int sWindowWidth=0,sWindowHeight=0,sRenderResolutionW=0,sRenderResolutionH=0;
void SDL_GetWindowSize(SDL_Window*,int*w,int*h){*w=dw/3;*h=dh/3;}
void pc_gfx_set_render_resolution(int w,int h){sRenderResolutionW=w;sRenderResolutionH=h;}
'''
 setter=fn(window,'void pc_window_set_window_size(int w, int h)');setter=setter[:setter.index('#ifdef __ANDROID__')]+'}\n';cpp+=setter
 cpp+=r'''
using GLint=int;
enum {ASPECT_AUTO,ASPECT_4_3,ASPECT_16_10,ASPECT_16_9,ASPECT_21_9};
bool menu=false;bool ios_native_settings_frame(){return menu;}
int sAspectRatioMode=0;float sCurrentAspectRatio=1,sRenderScale=1;
'''
 cpp+=fn(gfx,'float pc_gfx_get_render_scale(void)')+'\n'
 cpp+=fn(gfx,'static float calculate_aspect_ratio(int mode, float windowAspect)')+'\n'
 signature='static void calculate_output_area(int drawableWidth, int drawableHeight,\n'
 cpp+=fn(gfx,signature)+'\n'
 start=gfx.index('        // Calculate aspect ratio for this frame',gfx.index('void pc_gfx_begin_frame'))
 end=gfx.index('        if (wantedWidth !=',start)
 cpp+='std::pair<int,int> render(){int sDrawableWidth=dw,sDrawableHeight=dh;SDL_Window*window=&fakeWindow;(void)window;\n'+gfx[start:end]+'\nreturn {wantedWidth,wantedHeight};}\n'
 cpp+=r'''
void run(){
 rebuildResolutionList();
 CHECK(queries==0);CHECK(sDesktopW==dw&&sDesktopH==dh);
 CHECK(resolutionIndexFor(466,678)<0);
 for(const auto&r:sResolutions){CHECK(r.w>=r.h);CHECK(resolutionSelectable(r,PC_WINDOW_FULLSCREEN_EXCLUSIVE));}
 migrate();CHECK(sPending.windowWidth==2034&&sPending.windowHeight==1398);
 CHECK(sConfig.fpsMode==2&&sConfig.renderScale==1&&sConfig.sentinel==47);
 pc_window_set_window_size(sPending.windowWidth,sPending.windowHeight);
 CHECK(sRenderResolutionW==0&&sRenderResolutionH==0);
 CHECK(render()==std::make_pair(dw,dh));
 // Native follows a fold/rotation without a forced logical-point budget.
 for(auto size:{std::pair<int,int>{2796,1290},{2670,1878},{1365,939},{2034,1398}}){
  dw=size.first;dh=size.second;
  CHECK(render()==size);
  rebuildResolutionList();CHECK(sPending.windowWidth==dw&&sPending.windowHeight==dh);
  CHECK(sConfig.windowWidth==dw&&sConfig.windowHeight==dh);
 }
 // Lower budget and render-scale choices remain meaningful and independent.
 pc_window_set_window_size(1280,720);const auto low=render();
 CHECK(low.first<=1280&&low.second<=720&&low.first>0&&low.second>0);
 sRenderScale=.5f;const auto half=render();CHECK(std::abs(half.first*2-low.first)<=1);
 CHECK(std::abs(half.second*2-low.second)<=1);
 menu=true;CHECK(render()==std::make_pair(dw,dh));menu=false;sRenderScale=1;
 pc_window_set_window_size(dw,dh);sAspectRatioMode=1;const auto bars=render();
 CHECK(bars.first<=dw&&bars.second<=dh);
 CHECK(std::fabs(float(bars.first)/bars.second-4.f/3.f)<.002f);
 CHECK(pc_gfx_get_render_scale()==1);
}
}
'''
if a.ref:
 cpp+='void reproduce(){pikmin1::rebuildResolutionList();pikmin1::migrate();pikmin1::pc_window_set_window_size(466,678);auto size=pikmin1::render();std::printf("Old 466x678 budget -> %dx%d world on 2034x1398 drawable\\n",size.first,size.second);std::fflush(stdout); }\n'
cpp+='int main(){'+('reproduce();' if a.ref else '')+'pikmin1::run();pikmin2::run();std::printf("PASS: %d actual resolution/native pixels/migration/fold/budget checks\\n",checks);}\n'
a.output.write_text(cpp,encoding='utf-8')
print('Generated actual resolution/render-budget fixture'+(' for negative-control source '+a.ref if a.ref else ''))
