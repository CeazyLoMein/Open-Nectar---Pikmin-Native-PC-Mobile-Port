"""Regression for the real opening mute, cleanup and six category distance curves."""
from pathlib import Path
import re
import sys
ROOT=Path(__file__).resolve().parents[1]
def function(source,signature):
 start=source.index(signature);brace=source.index('{',start);depth=1;end=brace+1
 while depth:
  if source[end]=='{':depth+=1
  if source[end]=='}':depth-=1
  end+=1
 return source[start:end]
demo=(ROOT/'games/pikmin2/pikmin2-decomp/src/utilityU/PSMainSide_Demo.cpp').read_text()
game=(ROOT/'games/pikmin2/pikmin2-decomp/src/plugProjectHikinoU/PSGame.cpp').read_text()
calc=(ROOT/'games/pikmin2/pikmin2-decomp/src/JSystem/JAudio/JAL/JALCalc.cpp').read_text()
table=(ROOT/'games/pikmin2/pikmin2-decomp/include/PSGame/SoundTable.h').read_text()
start=table.index('struct SePerspInfo');end=table.index('struct CategoryMgr')
struct=table[start:end]
cleanup=function(demo,'static void pcRestoreOpeningSeCategories(')
onend=function(demo,'void Demo::onDemoEnd()')
assert 'pcRestoreOpeningSeCategories(mCurrentDemoName);' in onend
top=function(demo,'void Demo::onDemoTop()')
opening=function(top,'if (!strcmp(name, "x01_gamestart"))')
types=r'''
#include <cmath>
#include <cstdio>
#include <cstring>
using f32=float;using u8=unsigned char;
#define P2ASSERTLINE(line, condition) do { if(!(condition)) return; } while(0)
#define JUT_PANICLINE(line, msg) return 0.0f
namespace JAIGlobalParameter {
f32 getParamMaxVolumeDistance(){return 10.0f;}
f32 getParamMinDistanceVolume(){return 0.0f;}
}
namespace JALCalc { CALC }
namespace PSGame { namespace SoundTable {
STRUCT
struct CategoryMgr {
 enum {SoundCat0_Navi,SoundCat1_System,SoundCat2_Piki,SoundCat3_Item,SoundCat4_Env,SoundCat5_Enemy,SoundCat_COUNT};
 SePerspInfo* mPerspInfo[6];void initiate(u8);
 CategoryMgr(){for(u8 i=0;i<6;++i){mPerspInfo[i]=new SePerspInfo;initiate(i);}}
 ~CategoryMgr(){for(auto* p:mPerspInfo)delete p;}
};
}}
namespace PSSystem {
template<class T>struct SingletonBase {static T* value;static T* getInstance(){return value;}};
template<class T>T* SingletonBase<T>::value=nullptr;
PSGame::SoundTable::SePerspInfo* getSoundCategoryInfo(PSGame::SoundTable::CategoryMgr* mgr,u8 i){return mgr->mPerspInfo[i];}
}
namespace PSGame {
INIT
SET
DIST
}
CLEANUP
int checks=0,failed=0;
void check(bool ok,const char* msg){++checks;if(!ok){++failed;std::printf("FAIL %s\n",msg);}}
int main(){
 PSGame::SoundTable::CategoryMgr categoryStore;
 PSSystem::SingletonBase<PSGame::SoundTable::CategoryMgr>::value=&categoryStore;
 const char* name="x01_gamestart";
 OPENING
 check(categoryStore.mPerspInfo[2]->getDistVol(88,0)==0,"opening mutes Pikmin");
 check(categoryStore.mPerspInfo[5]->getDistVol(201,0)==0,"opening mutes nearby enemy");
 pcRestoreOpeningSeCategories("other_demo");
 check(categoryStore.mPerspInfo[2]->mDisabled&&categoryStore.mPerspInfo[5]->mDisabled,"unrelated cleanup does not change policy");
 pcRestoreOpeningSeCategories(nullptr);
 check(categoryStore.mPerspInfo[2]->mDisabled&&categoryStore.mPerspInfo[5]->mDisabled,"null no-op");
 // Simulate completing/skipping WITHOUT the opening onMessageEnd callback.
 pcRestoreOpeningSeCategories(name);
 for(int c=0;c<6;++c){
  auto* p=categoryStore.mPerspInfo[c];
  check(!p->mDisabled,"all categories usable");
  check(p->getDistVol(88,0)>0,"nearby audible gain");
  check(p->getDistVol(201,0)>0,"enemy-range audible gain");
  check(p->getDistVol(1500,0)<p->getDistVol(88,0),"distance still attenuates");
  check(p->getDistVol(6000,0)==0,"distant source still culled by gain");
 }
 pcRestoreOpeningSeCategories(name);
 check(!categoryStore.mPerspInfo[2]->mDisabled&&!categoryStore.mPerspInfo[5]->mDisabled,"repeat cleanup safe");
 categoryStore.mPerspInfo[0]->mDisabled=true;pcRestoreOpeningSeCategories(name);
 check(categoryStore.mPerspInfo[0]->mDisabled,"unrelated category mute preserved");
 std::printf("%d P2 actual opening-mute/cleanup/distance checks; %d failures\n",checks,failed);
 return failed?1:0;
}
'''
for key,value in {'CALC':function(calc,'f32 linearTransform('),'STRUCT':struct,
 'INIT':function(game,'void SoundTable::CategoryMgr::initiate('),
 'SET':function(game,'void SoundTable::SePerspInfo::set('),
 'DIST':function(game,'f32 SoundTable::SePerspInfo::getDistVol('),
 'CLEANUP':cleanup,'OPENING':opening}.items():types=types.replace(key,value)
out=Path(sys.argv[1]);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(types,encoding='utf-8')
print('Generated actual opening category mute/exit cleanup/distance regression')
