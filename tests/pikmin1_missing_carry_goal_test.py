"""Execute actual carry-goal selection and its null-goal routing guard."""
from pathlib import Path
import sys
r=Path(__file__).resolve().parents[1]
s=(r/'games/pikmin1/src/plugPikiKando/aiTransport.cpp').read_text(encoding='utf-8')
def block(signature):
 a=s.index(signature);b=s.index('{',a);i=b+1;depth=1
 while depth:depth+=(s[i]=='{')-(s[i]=='}');i+=1
 return s[a:i]
lift=s[s.index('void ActTransport::doLift()'):s.index('int ActTransport::exec()')]
start=lift.index('\t\t\tdecideGoal(pel);');end=lift.index('\t\t\t// this isn',start)
guard=lift[start:end]
code=r"""
#include <cstdio>
#include <cstdlib>
#include <vector>
#define PIKI_PC_PORT 1
#define TRUE 1
#define PRINT(...) ((void)0)
#define PRINT_KANDO(...) ((void)0)
#define STACK_PAD_VAR(x) ((void)0)
#define ERROR(...) std::abort()
using f32=float;
enum{Blue=0,Red=1,Yellow=2,PikiColorCount=3,PELTYPE_UfoPart=0};
struct Goal{};
struct Creature{virtual~Creature()=default;virtual bool isPiki(){return false;}std::vector<Creature*> attached;};
struct Navi{int mNaviID=0;};struct Piki:Creature{int mColor=0,mPlayerId=0;Navi*mNavi=nullptr;bool isPiki()override{return true;}};
struct Config{int type=1;int mPelletType(){return type;}};
struct Pellet:Creature{Config config;Config*mConfig=&config;Goal*mTargetGoal=nullptr;};
struct Stickers{std::vector<Creature*>*items;explicit Stickers(Creature*c):items(&c->attached){}};
struct Iterator{std::vector<Creature*>*items;std::size_t index=0;explicit Iterator(Stickers*s):items(s->items){}Creature*operator*(){return (*items)[index];}};
#define CI_LOOP(it) for(it.index=0;it.index<it.items->size();++it.index)
struct Ptr{Pellet*mPtr=nullptr;Pellet*getPtr(){return mPtr;}void clear(){mPtr=nullptr;}};
struct Flow{int mIsVersusMode=0;}flowCont;bool pc_vs_active(){return false;}
struct System{float getRand(float){return 0.5f;}}systemValue;System*gsys=&systemValue;
struct Items{Goal*goals[2][3]{};Goal*ships[2]{};int lastOwner=-1;Goal*pcGetContainer(int color,int owner){lastOwner=owner;return goals[owner][color];}Goal*pcGetUfo(int owner){return ships[owner];}}items;Items*itemMgr=&items;
struct ActTransport{Ptr mPellet;Piki*mPiki=nullptr;Goal*mGoal=nullptr;bool reachedRouting=false;void decideGoal(Creature*);void liftGuard(){Pellet*pel=mPellet.getPtr();GUARD reachedRouting=true;}};
FUNCTION
int checks=0;void check(bool yes,const char*why){++checks;if(!yes){std::fprintf(stderr,"FAIL %s\n",why);std::exit(1);}}
int main(){
 Pellet cargo;Piki carrier;carrier.mColor=Red;carrier.mPlayerId=1;cargo.attached={&carrier};ActTransport action;action.mPiki=&carrier;action.mPellet.mPtr=&cargo;
 action.decideGoal(&cargo);check(!action.mGoal&&!cargo.mTargetGoal,"absent Onion is a failed job, not panic");
 action.liftGuard();check(!action.reachedRouting&&!action.mPellet.mPtr,"actual lift guard drops job before route dereference");
 Goal ownerGoal;items.goals[1][Red]=&ownerGoal;action.mPellet.mPtr=&cargo;action.decideGoal(&cargo);check(action.mGoal==&ownerGoal&&cargo.mTargetGoal==&ownerGoal&&items.lastOwner==1,"existing owner/color goal unchanged");
 action.liftGuard();check(action.reachedRouting,"valid goal proceeds to normal routing");
 cargo.config.type=PELTYPE_UfoPart;action.decideGoal(&cargo);check(!action.mGoal&&!cargo.mTargetGoal,"missing ship is safe too");
 Goal ship;items.ships[1]=&ship;action.decideGoal(&cargo);check(action.mGoal==&ship&&cargo.mTargetGoal==&ship,"existing ship goal unchanged");
 action.mPellet.mPtr=nullptr;action.decideGoal(&cargo);check(!action.mGoal,"vanished cargo does not reuse old destination or dereference null");
 action.mPellet.mPtr=&cargo;action.decideGoal(nullptr);check(!action.mGoal,"absent cargo reference is safe");
 std::printf("%d actual carry-goal/route guard checks passed\n",checks);
}
""".replace('GUARD',guard).replace('FUNCTION',block('void ActTransport::decideGoal('))
Path(sys.argv[1]).write_text(code,encoding='utf-8')
