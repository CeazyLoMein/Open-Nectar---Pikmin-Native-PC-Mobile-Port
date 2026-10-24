"""Exercise P1 actual keyboard-ownership guard; no SDL/phone required."""
from pathlib import Path
import sys
r=Path(__file__).resolve().parents[1]
s=(r/'games/pikmin1/pc_port/pc_window.cpp').read_text(encoding='utf-8')
a=s.index('static void pc_window_update_text_input()');b=s.index('\nvoid pc_window_poll_events',a)
assert 'pc_window_update_text_input();' in s[b:s.index('SDL_PollEvent',b)]
cpp=r'''
#include <cassert>
#include <cstdio>
#ifndef TEST_DESKTOP
#define __IPHONEOS__ 1
#endif
#define PIKI_PC_PORT 1
#define PIKI_PC_SETTINGS_MENU 1
bool active=false,shown=false,editor=false;int stops=0;void*sWindow=nullptr;
bool SDL_IsTextInputActive(){return active;}bool SDL_IsScreenKeyboardShown(void*){return shown;}
bool pc_randomizer_intro_active(){return editor;}
void SDL_StopTextInput(){active=shown=false;++stops;}
FUNCTION
int main(){
#ifdef __IPHONEOS__
 active=true;pc_window_update_text_input();assert(!active&&stops==1);
 pc_window_update_text_input();assert(stops==1);
 shown=true;pc_window_update_text_input();assert(!shown&&stops==2);
 editor=true;active=shown=true;pc_window_update_text_input();assert(active&&shown&&stops==2);
 editor=false;pc_window_update_text_input();assert(!active&&!shown&&stops==3);
 active=shown=true;pc_window_update_text_input();assert(!active&&!shown&&stops==4);
#else
 active=shown=true;pc_window_update_text_input();assert(active&&shown&&stops==0);
#endif
 std::puts("PASS actual P1 keyboard ownership: startup, stale IME, editor preservation/exit, resumed gameplay, desktop");
}
'''
Path(sys.argv[1]).write_text(cpp.replace('FUNCTION',s[a:b]),encoding='utf-8')
