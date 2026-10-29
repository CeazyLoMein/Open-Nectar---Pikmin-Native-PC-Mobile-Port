"""Run the actual native Ready/focus functions with controlled Win32 leaves."""
from pathlib import Path
import sys
r=Path(__file__).resolve().parents[1]
s=(r/'games/pikmin1/pc_port/netplay/pc_desktop_coop.cpp').read_text(encoding='utf-8')
def function(signature):
 a=s.index(signature);b=s.index('{',a);i=b+1;depth=1
 while depth:depth+=(s[i]=='{')-(s[i]=='}');i+=1
 return s[a:i]
window=(r/'games/pikmin1/pc_port/pc_window.cpp').read_text(encoding='utf-8')
assert 'pc_coop_practice_background(event.window.event == SDL_WINDOWEVENT_FOCUS_LOST)' not in window
assert '    updateFocus();' in s
code=r"""
#include <cstdio>
#include <cstdlib>
using HWND=int;constexpr int SW_HIDE=0,GA_ROOTOWNER=1;
HWND game=1,room=2,panel=3,current=3,rootOwner=3;
bool readyRequested=false,blocked=true,ready=false,loaded=true,denyFocus=false,minimized=false,visible=true;
int attempts=0,checks=0;
HWND GetForegroundWindow(){return current;} HWND GetAncestor(HWND,int){return rootOwner;}
void SetForegroundWindow(HWND h){if(!denyFocus)current=h;}
void SetFocus(HWND){}void ShowWindow(HWND,int){visible=false;}
bool IsIconic(HWND){return minimized;}
void pc_coop_practice_background(bool value){blocked=value;if(value)ready=false;}
bool pc_coop_practice_can_ready(){return loaded;}
bool pc_coop_practice_ready(){++attempts;if(blocked||!loaded)return false;ready=true;return true;}
FUNCTIONS
void check(bool yes,const char*why){++checks;if(!yes){std::fprintf(stderr,"FAIL %s\n",why);std::exit(1);}}
int main(){
 updateFocus();check(!blocked,"practice panel belongs to game");
 current=room;updateFocus();check(!blocked,"room belongs to game");
 current=game;updateFocus();check(!blocked,"game active");
 current=4;rootOwner=game;updateFocus();check(!blocked,"owned control active");
 rootOwner=4;updateFocus();check(blocked,"external app really blocks");
 current=panel;rootOwner=panel;loaded=false;visible=true;resume();check(!readyRequested&&visible,"loading cannot accept ready");
 loaded=true;blocked=true;ready=false;resume();check(readyRequested&&!visible&&!ready,"click queues readiness before focus messages");
 updateFocus();check(ready&&!blocked&&!readyRequested&&attempts==1,"guest native ready commits after focus settled");
 current=panel;ready=false;denyFocus=true;resume();updateFocus();check(readyRequested&&!ready&&!blocked,"denied focus does not lose request or claim ready");
 denyFocus=false;current=game;updateFocus();check(ready&&!readyRequested,"delayed focus transfer completes ready");
 current=panel;ready=false;denyFocus=true;resume();current=4;rootOwner=4;updateFocus();check(blocked&&!readyRequested,"external switch cancels queued ready");
 current=game;denyFocus=false;updateFocus();check(!blocked&&!ready,"return from external app requires new ready");
 minimized=true;updateFocus();check(blocked,"minimized game blocks");minimized=false;
 current=0;updateFocus();check(blocked,"no foreground blocks");
 std::printf("%d actual desktop Ready/focus checks passed\n",checks);
}
""".replace('FUNCTIONS',function('void resume()')+'\n'+function('void updateFocus()'))
Path(sys.argv[1]).write_text(code,encoding='utf-8')
