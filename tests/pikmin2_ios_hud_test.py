"""Extract actual P2 HUD/renderer routing; no assets or graphics context needed."""
from pathlib import Path
import sys
repo=Path(__file__).resolve().parents[1]
gfx=(repo/'games/pikmin2/pc_port/gl/pc_gfx.cpp').read_text(encoding='utf-8')
settings=(repo/'games/pikmin2/pc_port/settings/pc_settings.cpp').read_text(encoding='utf-8')
os=(repo/'games/pikmin2/pc_port/dolphin_stubs/p2_os_host.cpp').read_text(encoding='utf-8')
def function(source,signature):
 start=source.index(signature);return source[start:source.index('\n}',start)+2]
ui=function(gfx,'void pc_gfx_ui_draw(')
route=ui[:ui.index('    if (fontI8')].replace('void pc_gfx_ui_draw(', 'void routeUI(')
route+='    (void)fontI8; (void)fontW; (void)fontH; lastW=w; lastH=h;\n}\n'
restore=ui[ui.index('    if (displayOverlay && glBindFramebuffer_ptr && sNativeFramebufferReady)'):ui.rindex('\n}')]
hud=function(settings,'void pc_settings_draw_ios_performance(void)')
vi=function(os,'void VIWaitForRetrace()')
assert vi.index('pc_settings_p2_flush();')<vi.index('pc_gfx_present();')<vi.index('pc_touch_draw();')<vi.index('pc_settings_draw_ios_performance();')<vi.index('SDL_GL_SwapWindow(window);')
assert 'ROW_IOS_PERFORMANCE_HUD' in settings and 'sPending.iosPerformanceHud = !sPending.iosPerformanceHud' in settings
prefix=r'''
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <vector>
using GLint=int;
struct PcUiVertex {};
constexpr int GL_FRAMEBUFFER=1;
static bool host=false;
struct PcGfxHostAllocScope { bool previous=host; PcGfxHostAllocScope(){host=true;} ~PcGfxHostAllocScope(){host=previous;} };
static bool sNativeFramebufferReady=true,sNativeWrittenThisFrame=false,programReady=true;
static int sRenderWidth=640,sRenderHeight=296,sDrawableWidth=2796,sDrawableHeight=1290;
static unsigned sNativeFramebuffer=17,lastFbo=0;
static int lastW=0,lastH=0,binds=0,viewportW=0,viewportH=0;
static void bindFramebuffer(int,unsigned fbo){assert(host);lastFbo=fbo;++binds;}
static auto glBindFramebuffer_ptr=bindFramebuffer;
static unsigned pc_gfx_display_framebuffer(){return 43;}
static bool ensure_ui_program(){return programReady;}
static void pc_gfx_note_gl_state_change(){}
static void invalidate_gl_pipeline_guards(){}
static void glViewport(int,int,int w,int h){viewportW=w;viewportH=h;}
'''
prefix+=route+'\nvoid restoreUI(bool displayOverlay) {\n'+restore+'\n}\n'
prefix+=r'''
#define __IPHONEOS__ 1
#define PC_SETTINGS_HOST_ALLOC() PcGfxHostAllocScope scope
static bool sMenuOpen=false,captain=false,hudEnabled=true;
struct Colour {int r,g,b,a;Colour(int R,int G,int B,int A):r(R),g(G),b(B),a(A){}};
struct RectArea {int x0,y0,x1,y1;RectArea(int a,int b,int c,int d):x0(a),y0(b),x1(c),y1(d){}};
struct Matrix4f {int mMtx=0;};
static int panelAlpha=0,linesDrawn=0,fontWidth=0,flushes=0,virtualW=866,virtualH=400;
static bool displayFlush=false;
static RectArea observedPanel(0,0,0,0);
struct DGXGraphics {
 void setOrthogonal(int,const RectArea&){}
 void setColour(Colour c,bool){panelAlpha=c.a;}
 void setAuxColour(Colour){}
 void useTexture(void*,int){}
 void fillRectangle(const RectArea& r){observedPanel=r;}
};
static DGXGraphics graphics;
struct System {DGXGraphics* mDGXGfx;};
static System systemObj{&graphics};static System* gsys=&systemObj;
static bool pc_captain_select_active(){return captain;}
static bool pc_ios_performance_lines(char lines[5][96]) {
 if(!hudEnabled)return false;
 for(int i=0;i<5;++i)std::snprintf(lines[i],96,"Render60.0FPS average16.67ms row%d",i);
 return true;
}
static int font=1;static int* sFont=&font;
static void ensureFont(){}
static void ngScreen(int* w,int* h){*w=virtualW;*h=virtualH;}
struct PcSettingsP2DFrame {PcSettingsP2DFrame(int,int){}};
constexpr int GX_TEXMAP0=0;
static int pc_p2_text_width(const char* s,int fw){return static_cast<int>(std::strlen(s)*fw*0.78f);}
static void pc_p2_text(int,int,const char*,Colour main,Colour shadow,int fw){
 assert(main.a==255 && shadow.a==255);++linesDrawn;fontWidth=fw;
}
static void pc_settings_p2_flush(bool display){assert(host);++flushes;displayFlush=display;}
'''
prefix+=hud
prefix+=r'''
static int checks=0;
static void check(bool ok){++checks;assert(ok);}
int main(){
 PcUiVertex v;
 routeUI(&v,1,866,400,nullptr,0,0,true);
 check(lastFbo==43 && lastW==2796 && lastH==1290 && !sNativeWrittenThisFrame);
 check(!host);
 {PcGfxHostAllocScope scope;restoreUI(true);}
 check(lastFbo==17 && viewportW==640 && viewportH==296);
 routeUI(&v,1,866,400,nullptr,0,0,false);
 check(lastFbo==17 && lastW==640 && lastH==296 && sNativeWrittenThisFrame);
 sNativeFramebufferReady=false;sNativeWrittenThisFrame=false;lastFbo=99;binds=0;
 routeUI(&v,1,866,400,nullptr,0,0,false);
 check(binds==0 && lastFbo==99 && lastW==2796 && sNativeWrittenThisFrame);
 routeUI(&v,1,866,400,nullptr,0,0,true);
 check(binds==1 && lastFbo==43);
 const int before=binds;sDrawableWidth=0;
 routeUI(&v,1,866,400,nullptr,0,0,true);check(binds==before);
 sDrawableWidth=2796;programReady=false;
 routeUI(&v,1,866,400,nullptr,0,0,true);check(binds==before);
 programReady=true;sNativeFramebufferReady=true;
 pc_settings_draw_ios_performance();
 check(linesDrawn==5 && fontWidth>=10 && panelAlpha>=240);
 check(flushes==1 && displayFlush && !host);
 check(observedPanel.x0>=0 && observedPanel.y0>=0 && observedPanel.x1<=virtualW && observedPanel.y1<=virtualH);
 hudEnabled=false;pc_settings_draw_ios_performance();check(flushes==1 && linesDrawn==5);
 hudEnabled=true;sMenuOpen=true;pc_settings_draw_ios_performance();check(flushes==1);
 sMenuOpen=false;captain=true;pc_settings_draw_ios_performance();check(flushes==1);
 captain=false;gsys=nullptr;pc_settings_draw_ios_performance();check(flushes==1);
 gsys=&systemObj;virtualW=533;pc_settings_draw_ios_performance();
 check(linesDrawn==10 && observedPanel.x1<=virtualW);
 std::printf("PASS: %d actual HUD routing/readability/disabled/native-framebuffer checks\n",checks);
}
'''
Path(sys.argv[1]).write_text(prefix,encoding='utf-8')
print('Generated actual HUD/renderer fixture; native display ordering and toggle verified.')
