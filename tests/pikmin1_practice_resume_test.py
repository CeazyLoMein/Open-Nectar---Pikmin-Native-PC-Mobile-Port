"""Exercise actual practice panel latch across interruptions."""
from pathlib import Path
import sys
s=(Path(__file__).resolve().parents[1]/'games/pikmin1/pc_port/netplay/pc_coop_practice_runtime.cpp').read_text()
a=s.index('    if (s->phase()==net::CoopPhase::Running) panel=false;')
b=s.index('\n    hold(s->hostShouldAdvanceWorld());',a)
actual=s[a:b]
code=r"""
#include <cstdio>
namespace net {enum class CoopPhase {Loading,WaitingForReady,Running,Paused,WaitingForPartner};}
struct Session{net::CoopPhase value;net::CoopPhase phase(){return value;}};
bool panel=false,confirmed=false,away=false;int shown=0;void showPanel(){++shown;}
void update(Session* s){ ACTUAL }
int errors=0;void check(bool b,const char*m){if(!b){std::printf("FAIL %s\n",m);++errors;}}
int main(){Session s{net::CoopPhase::Loading};update(&s);check(shown==0,"unconfirmed never offers ready");
confirmed=true;update(&s);check(shown==1&&panel,"initial ready shown");update(&s);check(shown==1,"waiting does not reopen repeatedly");
s.value=net::CoopPhase::Running;update(&s);check(!panel,"running rearms future prompt");
away=true;s.value=net::CoopPhase::Paused;update(&s);check(shown==1&&!panel,"background does not show modal");
away=false;update(&s);check(shown==2&&panel,"return from background reopens ready");update(&s);check(shown==2,"prompt shown once");
s.value=net::CoopPhase::Running;update(&s);s.value=net::CoopPhase::Paused;update(&s);check(shown==3,"partner interruption also reopens ready");
if(!errors)std::puts("PASS actual practice panel latch: initial ready, background return, partner pause");return errors?1:0;}
""".replace('ACTUAL',actual)
out=Path(sys.argv[1]);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(code,encoding='utf-8')
