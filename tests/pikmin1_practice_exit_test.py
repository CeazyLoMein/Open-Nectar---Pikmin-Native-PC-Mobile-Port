"""Exercise actual practice exit body with fake card/scene resources."""
import sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
s=(root/'games/pikmin1/pc_port/netplay/pc_coop_practice_runtime.cpp').read_text(encoding='utf-8')
start=s.index('bool pc_coop_practice_leave() {');i=s.index('{',start);depth=1;j=i+1
while depth:
 depth+=(s[j]=='{')-(s[j]=='}');j+=1
body=s[i:j]
fixture=r"""
#include "netplay/pc_coop_visual_smoothing.h"
#include <cstdio>
#include <memory>
#include <cstdint>
struct Connection {bool closed=false;void close(){closed=true;}};
struct Loading {};
struct Inputs {void reset(){}};
struct Remote {int x=0;};
enum class PcCoopPracticeStart {Idle,Draining,Armed,Loading,Failed,RestartRequired};
std::unique_ptr<Connection> owner;std::unique_ptr<Loading> loading;
bool title,requested,loaded,confirmed,entered,stopped,away,panel,padFiltered,advancing,sessionConfigured;
std::uint64_t tick,frame,applied,lastPublish,revision;std::uint16_t previousButtons;char failure[240];Inputs inputs;Remote remote;
PcCoopVisualSmoothing smoothing;nectar::net::ActorFrame presented;
PcCoopPracticeStart startState;bool cardActive,threadOK;int worldEnds,cancels,pauses;
bool ownThread(){return threadOK;}void pc_coop_practice_pause(){++pauses;}
bool pc_coop_practice_cancel_start(){++cancels;if(startState==PcCoopPracticeStart::Draining){startState=PcCoopPracticeStart::Idle;return true;}return false;}
PcCoopPracticeStart pc_coop_practice_start_state(){return startState;}bool pc_card_coop_practice_active(){return cardActive;}
void pc_coop_world_end_scene(){++worldEnds;}void fail(const char*){stopped=true;}
bool pc_coop_practice_leave() BODY
int errors=0,checks=0;void check(bool v,const char* s){++checks;if(!v){std::printf("FAIL %s\\n",s);++errors;}}
void setup(PcCoopPracticeStart s,bool card,bool onTitle,bool haveEntered){owner=std::make_unique<Connection>();loading=std::make_unique<Loading>();startState=s;cardActive=card;title=onTitle;entered=haveEntered;loaded=haveEntered;threadOK=true;worldEnds=cancels=pauses=0;failure[0]=0;
 smoothing.reset();nectar::net::ActorFrame sample;sample.frame=7;sample.tick=50;
 smoothing.push(sample,1000);presented=sample;
}
bool buffered(){nectar::net::ActorFrame value;return smoothing.sample(1100,value);}
int main(){
 setup(PcCoopPracticeStart::Idle,false,true,false);check(pc_coop_practice_leave()&&!owner&&!loading&&worldEnds==1,"idle title returns safely");
 check(!buffered()&&presented.frame==0&&presented.tick==0,"safe leave clears real smoothing history and presentation");
 setup(PcCoopPracticeStart::Draining,false,true,false);check(pc_coop_practice_leave()&&!owner&&startState==PcCoopPracticeStart::Idle&&worldEnds==1,"pending admission cancels before returning");
 check(!buffered()&&presented.frame==0,"canceled admission clears old presentation");
 setup(PcCoopPracticeStart::Armed,true,true,false);check(!pc_coop_practice_leave()&&owner&&owner->closed&&worldEnds==0,"admitted scratch card requires restart");
 check(buffered()&&presented.frame==7,"late restart does not tear down live display resources");
 setup(PcCoopPracticeStart::Loading,true,false,true);check(!pc_coop_practice_leave()&&owner&&owner->closed&&worldEnds==0,"live scene does not expose solo card");
 check(buffered()&&presented.frame==7,"held live scene retains its display until restart");
 setup(PcCoopPracticeStart::Idle,false,true,false);threadOK=false;check(!pc_coop_practice_leave()&&owner&&!owner->closed&&cancels==0,"wrong thread makes no changes");
 check(buffered()&&presented.frame==7,"wrong thread cannot erase presentation state");
 if(!errors)std::printf("PASS %d actual practice exit checks: early menu return, late restart, card protection and real smoothing cleanup\n",checks);return errors?1:0;
}
"""
out=Path(sys.argv[1]);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(fixture.replace('BODY',body),encoding='utf-8')
