"""Execute the real non-touch Recall All consumer and input latch on the host."""
from pathlib import Path
import sys

root=Path(__file__).resolve().parents[1]
source=(root/'games/pikmin1/src/plugPikiKando/navi.cpp').read_text(encoding='utf-8')
start=source.index('void Navi::pcUpdateRecallAll(')
brace=source.index('{',start);depth=1;end=brace+1
while depth:
    if source[end]=='{':depth+=1
    elif source[end]=='}':depth-=1
    end+=1
function=source[start:end]
code=r"""
#include <cstdint>
#include <cstdio>
#include <cstdlib>
INPUT_HEADER
#define PIKI_PC_PORT 1
#define PIKI_PC_TOUCH 0
PcRecallInput input;
std::uint64_t now=0;
bool enabled=true;
bool pc_window_take_recall_press(){return input.take(now);}
int pc_settings_get_recall_all(){return enabled;}
struct Movie{bool mIsActive=false;}movie;
struct Gameflow{Movie*mMoviePlayer=&movie;}gameflow;
struct Player{bool ended=false;bool inDayEnd(){return ended;}}player;
Player*playerState=&player;
struct Navi{int mNaviID=0,calls=0;bool global=false;
    void pcUpdateRecallAll();
    void callPikis(float,bool all){++calls;global=all;}};
FUNCTION
int checks=0;
void check(bool value,const char*why){++checks;if(!value){std::fprintf(stderr,"FAIL: %s\n",why);std::exit(1);}}
int main(){
    input.sample(true,true,0);check(input.take(0),"fresh press");check(!input.take(0),"one shot");
    input.sample(true,true,10);check(!input.take(10),"hold does not repeat");
    input.sample(false,true,20);input.sample(true,true,21);check(input.take(21),"release and repress");
    input.sample(false,true,30);input.sample(true,true,31);check(!input.take(282),"stale press expires");
    input.sample(false,true,300);input.sample(true,false,301);input.sample(true,true,302);check(!input.take(302),"menu-held key cannot activate on close");
    input.sample(false,true,303);input.sample(true,true,304);input.cancel();check(!input.take(304),"focus loss cancels");
    input.sample(true,true,305);check(!input.take(305),"focus return with held key cannot recall");
    input.sample(false,true,306);input.sample(true,true,307);check(input.take(307),"fresh post-focus press works");
    input.sample(false,true,400);input.sample(true,true,401);input.sample(true,false,402);check(!input.take(402),"disabled/menu sampling cancels pending input");
    input.sample(false,true,500);input.sample(true,true,501);check(!input.take(400),"backwards clock rejected");
    input.sample(false,true,0);input.sample(true,true,0);check(input.take(250),"exact expiry boundary");
    Navi captain;
    auto press=[](){input.sample(false,true,now);input.sample(true,true,now);};
    now=1000;press();captain.pcUpdateRecallAll();check(captain.calls==1&&captain.global,"desktop build can recall globally");
    captain.pcUpdateRecallAll();check(captain.calls==1,"consumer cannot replay press");
    enabled=false;press();captain.pcUpdateRecallAll();enabled=true;captain.pcUpdateRecallAll();check(captain.calls==1,"disabled cheat drops input");
    movie.mIsActive=true;press();captain.pcUpdateRecallAll();movie.mIsActive=false;captain.pcUpdateRecallAll();check(captain.calls==1,"cutscene drops input");
    player.ended=true;press();captain.pcUpdateRecallAll();player.ended=false;captain.pcUpdateRecallAll();check(captain.calls==1,"day end drops input");
    playerState=nullptr;press();captain.pcUpdateRecallAll();playerState=&player;captain.pcUpdateRecallAll();check(captain.calls==1,"absent campaign drops input");
    Navi other;other.mNaviID=1;press();other.pcUpdateRecallAll();check(other.calls==0,"second captain cannot consume solo recall");captain.pcUpdateRecallAll();check(captain.calls==2,"command belongs to captain zero");
    std::printf("%d non-touch Recall All command/input checks passed\n",checks);
}
""".replace('INPUT_HEADER',(root/'games/pikmin1/pc_port/pc_recall_input.h').read_text(encoding='utf-8').replace('#pragma once',''))
code=code.replace('FUNCTION',function)
Path(sys.argv[1]).write_text(code,encoding='utf-8')
print('Generated actual non-touch Recall All/input checks')
