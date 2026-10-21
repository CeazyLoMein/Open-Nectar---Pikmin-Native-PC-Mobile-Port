"""Execute actual P1 walking-speed and settings functions with engine seams."""
from pathlib import Path
import re,sys
root=Path(__file__).resolve().parents[1]
def read(p):return (root/p).read_text(encoding='utf-8')
def fn(s,sig):
 at=s.index(sig);start=s.index('{',at);depth=1;i=start+1
 while depth:
  if s[i]=='{':depth+=1
  if s[i]=='}':depth-=1
  i+=1
 return s[at:i]
s=read('games/pikmin1/pc_port/settings/pc_settings.cpp');p=read('games/pikmin1/src/plugPikiKando/piki.cpp')
constants=s[s.index('constexpr int kSpeedPcts[]'):s.index('void speedPctLabel(')]
getter=fn(s,'float pc_settings_get_piki_speed_scale(')
funcs=[fn(p,sig) for sig in ['void Piki::setSpeed(f32 speedRatio)','f32 Piki::getSpeed(f32 speedRatio)','void Piki::setSpeed(f32 speedRatio, immut Vector3f& direction)','void Piki::setSpeed(f32 speedRatio, f32 angle)']]
parse=re.search(r'else if \(key == "pikiSpeedPct"\) ([^\n]+)',s)[1]
save=re.search(r'out << "pikiSpeedPct[^\n]+',s)[0]
change=fn(s,'else if (row == 43)')[len('else '):]
value=re.search(r'case 43: ([^\n]+) break;',s)[1]
config=read('games/pikmin1/pc_port/settings/pc_settings.h')
assert 'float pc_settings_get_piki_speed_scale(void)' in config
assert s.count('pikiSpeedPct = 100;')==2,'default and Reset must both retain original speed'
assert 'X(pikiSpeedPct)' not in s,'solo-only getter must not alter locked netplay schema'
assert '#if !PIKI_P2_HOST\n    { SRC_MODS, 43, "Pikmin Speed"' in s
cpp=r"""
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <sstream>
#define PIKI_PC_PORT 1
#define immut const
using f32=float;
enum {Leaf,Bud,Flower};
bool hard=false,speedrun=false,coop=false,vs=false,det=false;
bool pc_hardmode_active(){return hard;}bool pc_speedrun_active(){return speedrun;}bool pc_coop_active(){return coop;}
bool pc_vs_active(){return vs;}bool pc_netplay_deterministic(){return det;}
struct Config {int pikiSpeedPct=100;}sConfig,sPending;
CONSTANTS
GETTER
struct Vector3f {f32 x=0,y=0,z=0;void set(f32 a,f32 b,f32 c){x=a;y=b;z=c;}};
Vector3f operator*(f32 s,const Vector3f&d){return {s*d.x,s*d.y,s*d.z};}
struct Parms {float mMaxLeafMoveSpeed(){return 100;}float mMaxBudMoveSpeed(){return 150;}float mMaxFlowerMoveSpeed(){return 200;}float mMinMoveSpeed(){return 20;}};
struct Props {Parms mPikiParms;}props;
struct Manager {Props*mPikiParms=&props;}manager;Manager*pikiMgr=&manager;
struct AIConstant {bool scale=true;bool mDoScaleHappaMoveSpeed(){return scale;}}AICONST;
struct Piki {int mHappa=Leaf;float mMoveSpeed=0;Vector3f mTargetVelocity;
void setSpeed(f32);float getSpeed(f32);void setSpeed(f32,const Vector3f&);void setSpeed(f32,f32);};
FUNCTIONS
void parseSpeed(const std::string&val){PARSE}
std::string saveSpeed(){std::ostringstream out;SAVE return out.str();}
STEP
void changeSpeed(int row,bool left,bool right){CHANGE}
std::string valueSpeed(){char value[64];size_t n=sizeof(value);VALUE return value;}
int checks=0,failures=0;void check(bool ok,const char*label){++checks;if(!ok){++failures;std::printf("FAIL %s\n",label);}}
bool near(float a,float b){return std::fabs(a-b)<.001f;}
int main(){
 check(sConfig.pikiSpeedPct==100,"default original speed");
 for(int pct:kSpeedPcts){
  sConfig.pikiSpeedPct=pct;Piki p;
  const float factor=
#if PIKI_P2_HOST
   1.f;
#else
   pct/100.f;
#endif
  for(int stage:{Leaf,Bud,Flower})for(float ratio:{0.f,.5f,1.f}){
   p.mHappa=stage;float maximum=stage==Leaf?100.f:stage==Bud?150.f:200.f;
   float expected=((maximum-20)*ratio+20)*factor;
   check(near(p.getSpeed(ratio),expected),"query scaled once after maturity interpolation");
   p.setSpeed(ratio);check(near(p.mMoveSpeed,expected),"scalar entry scaled once");
   Vector3f d{.6f,0,.8f};p.setSpeed(ratio,d);check(near(p.mMoveSpeed,expected)&&near(p.mTargetVelocity.x,expected*.6f)&&near(p.mTargetVelocity.z,expected*.8f),"direction entry consistent with query");
   p.setSpeed(ratio,0.f);check(near(p.mMoveSpeed,expected)&&near(p.mTargetVelocity.x,expected)&&near(p.mTargetVelocity.z,0),"angle entry consistent with query");
  }
 }
 sConfig.pikiSpeedPct=200;for(bool*flag:{&hard,&speedrun,&coop,&vs,&det}){*flag=true;check(near(pc_settings_get_piki_speed_scale(),1),"non-solo context keeps stock speed");*flag=false;}
 for(const char*text:{"0","-100","999","125","garbage"}){parseSpeed(text);check(sConfig.pikiSpeedPct==100,"invalid config falls back original");}
 for(int pct:kSpeedPcts){parseSpeed(std::to_string(pct));check(sConfig.pikiSpeedPct==pct,"supported config roundtrip");check(saveSpeed()=="pikiSpeedPct = "+std::to_string(pct)+"\n","persist exact percentage");}
 sPending.pikiSpeedPct=100;changeSpeed(43,false,true);check(sPending.pikiSpeedPct==150,"right increments");changeSpeed(43,true,false);check(sPending.pikiSpeedPct==100,"left decrements");changeSpeed(43,true,false);check(sPending.pikiSpeedPct==500,"left wraps");
 changeSpeed(43,false,true);check(sPending.pikiSpeedPct==100,"right wraps");changeSpeed(42,false,true);check(sPending.pikiSpeedPct==100,"other row untouched");
 sPending.pikiSpeedPct=200;check(valueSpeed()=="200%","menu displays actual percent");
 std::printf("%d P1 walking speed/config scenarios; %d failures\n",checks,failures);return failures?1:0;
}
"""
for k,v in {'CONSTANTS':constants,'GETTER':getter,'FUNCTIONS':'\n'.join(funcs),'PARSE':parse,'SAVE':save,'STEP':fn(s,'int stepPct('),'CHANGE':change,'VALUE':value}.items():cpp=cpp.replace(k,v)
Path(sys.argv[1]).write_text(cpp,encoding='utf-8');print('Generated real P1 speed and config scenarios')
