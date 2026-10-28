"""Compile actual practice/story start-movie branch with controlled state."""
from pathlib import Path
import sys
s=(Path(__file__).resolve().parents[1]/'games/pikmin1/src/plugPikiColin/newPikiGame.cpp').read_text()
a=s.index('if (playerState->isTutorial() && !pc_coop_practice_active())');b=s.index('\n\t\tgsys->setFade(1.0f);',a)
actual=s[a:b]
code=r"""
#include <cstdio>
using u32=unsigned;
enum {DEMOID_OlimarWakeUp=1,DEMOID_Landing=2,CAF_AllVisibleMask=7,STAGE_COUNT=5};
struct Movie {int started=0;void startMovie(int id,int,void*,void*,void*,int,bool){started=id;}} movie;
struct Gameflow {Movie*mMoviePlayer=&movie;} gameflow;
struct Stage {u32 mStageID=0;} stage;
struct Flow {Stage*mCurrentStage=&stage;} flowCont;
struct Player {bool tutorial=false;bool isTutorial(){return tutorial;}} player;Player*playerState=&player;
bool practice=false,versus=false,skip=false;
bool pc_coop_practice_active(){return practice;}bool pc_vs_active(){return versus;}bool pc_tutorial_skip_pending(){return skip;}
void start(){ ACTUAL }
int errors=0;void check(bool b,const char* label){if(!b){std::printf("FAIL %s\n",label);++errors;}}
int main(){for(bool t:{false,true}){player.tutorial=t;practice=true;movie.started=0;start();check(movie.started==0,"practice never starts story movie");}
practice=false;player.tutorial=true;movie.started=0;start();check(movie.started==DEMOID_OlimarWakeUp,"story tutorial still starts");
player.tutorial=false;movie.started=0;start();check(movie.started==DEMOID_Landing,"story landing still starts");
versus=true;movie.started=0;start();check(movie.started==0,"versus remains without landing");
if(!errors)std::puts("PASS practice suppresses movies while story and versus retain their paths");return errors?1:0;}
""".replace('ACTUAL',actual)
code=code.replace('#include <cstdio>','#include <cstdio>\n#include <initializer_list>')
out=Path(sys.argv[1]);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(code,encoding='utf-8')
