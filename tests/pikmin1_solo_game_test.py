"""Generate a host fixture around the real test-only preset and profile helpers."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
global_header = (ROOT/'games/pikmin1/include/GlobalGameOptions.h').read_text()
pellet_header = (ROOT/'games/pikmin1/include/Pellet.h').read_text()
enums = '\n'.join(re.search(r'enum '+name+r'\s*\{.*?\};',source,re.S)[0]
                  for name,source in [('StageID',global_header),('PikiColor',global_header),
                                      ('PikiHappa',global_header),('UfoPartIndex',pellet_header),('UfoPartID',pellet_header)])
demo_header=(ROOT/'games/pikmin1/include/Demo.h').read_text()
enums += '\n#define MAX_UFO_PARTS 30\n' + re.search(r'enum EDemoFlags\s*\{.*?\};',demo_header,re.S)[0]
card = (ROOT/'games/pikmin1/src/plugPikiColin/cardSelect.cpp').read_text(encoding='utf-8')
assert card.count('pc_solo_test_prepare_new_campaign(')==2
core = (ROOT/'games/pikmin1/src/plugPikiKando/gameCoreSection.cpp').read_text(encoding='utf-8')
assert 'pc_solo_test_prepare_new_campaign(' not in core
code = r'''
#include <cstdio>
#include <fstream>
#include <string>
#include <numeric>
#include "PROFILE"
ENUMS
enum { PARTVIS_Uncollected, PARTVIS_Visible, PARTVIS_Invisible };
struct PlayerState {
 struct Flags { unsigned long long bits=0; bool isFlag(int n)const{return (bits & (1ull<<n))!=0;}
  void setFlagOnly(int n){bits|=1ull<<n;} } mDemoFlags;
 bool isTutorial() const {return mIsTutorialMode;}
 bool hasUfoParts(unsigned) const {return mUfoParts && mUfoParts[UFO_MainEngine].mPartVisType!=0;}
 struct Part { int mPartVisType=0; } parts[UFO_COUNT];
 int mTotalParts=UFO_COUNT; Part* mUfoParts=parts;
 int mCurrParts=0,mRequiredUfoPartCount=0,mShipUpgradeLevel=0,mShipEffectPartFlag=8;
 bool mIsTutorialMode=true;
 int mStagePartsCollected[STAGE_COUNT]{};
 int mContainerFlag=0,mDisplayPikiFlag=0;
 int mLivingPikiNum=0,mTotalBornPikiNum=0,mTotalPluckedPikiCount=0;
 int mPartsCollectedByDay[30]{};
 void setContainer(int c) { mContainerFlag |= 1<<c; }
 void setBootContainer(int c) { mContainerFlag |= 1<<(c+3); }
 void setDisplayPikiCount(int c) { mDisplayPikiFlag |= 1<<c; }
};
struct PikiInfMgr { int mPikiCounts[PikiColorCount][PikiHappaCount]{}; };
struct TestPlayState { unsigned flags=0; void openStage(int id){flags|=1u<<id;} };
#include "pc_solo_test_game.h"
int checks=0,failed=0;
void check(bool ok,const char* name){++checks;if(!ok){++failed;std::printf("FAIL %s\n",name);}}
int main(){
 auto profile=nectar_ios::apply_pikmin1_solo_test_profile("");
 check(profile.changed,"fresh test profile");
 for(const char* s : {"unlockZones = 1", "allOnions = 1", "fpsMode = 1", "iosPerformanceHud = 1"})
  check(profile.text.find(s)!=std::string::npos,s);
 const std::string custom="iosPerformanceHud = 0\nfpsMode = 1\ntexturePack = GPI\n";
 auto kept=nectar_ios::apply_pikmin1_solo_test_profile(custom);
 check(!kept.changed&&kept.text==custom,"existing custom test settings preserved");
#if NECTAR_P1_SOLO_TEST
 TestPlayState play;pc_solo_test_unlock_areas(play);
#if NECTAR_P1_SOLO_UPDATE
 check(play.flags==15,"update unlocks four earlier areas, finale left closed");
#else
 check(play.flags==31,"separate test has five selectable areas");
#endif
 std::remove("p1-solo-test-events.txt");
 for(int slot=0;slot<3;++slot){
  PlayerState p;PikiInfMgr b;
  pc_solo_test_prepare_new_campaign(p,b,slot);
#if NECTAR_P1_SOLO_UPDATE
  const bool finale=false;
#else
  const bool finale=slot==1;
#endif
  check(p.mCurrParts==(finale?29:1),"part count");
  check(p.mRequiredUfoPartCount==(finale?25:1),"required count");
  check(p.mUfoParts[UFO_SecretSafe].mPartVisType==0,"Secret Safe remains real pickup");
  check(p.mUfoParts[UFO_MainEngine].mPartVisType==(finale?PARTVIS_Visible:PARTVIS_Invisible),"engine preset");
  int acquired=0;for(auto& part:p.parts)acquired+=part.mPartVisType!=0;
  check(acquired==p.mCurrParts,"part flags agree with count");
  check(std::accumulate(p.mStagePartsCollected,p.mStagePartsCollected+STAGE_COUNT,0)==p.mCurrParts,"area totals agree");
  check(p.mStagePartsCollected[STAGE_Last]==0,"final area remains uncompleted");
  check(!p.mIsTutorialMode&&p.mContainerFlag==63&&p.mDisplayPikiFlag==7,"all Onions ready");
  for(int c=0;c<PikiColorCount;++c)
   check(b.mPikiCounts[c][Leaf]==100&&b.mPikiCounts[c][Bud]==0&&b.mPikiCounts[c][Flower]==0,"bank inventory");
  check(p.mTotalBornPikiNum==300&&p.mPartsCollectedByDay[0]==p.mCurrParts,"summary");
  check(p.mDemoFlags.isFlag(DEMOFLAG_ApproachEngine)&&p.mDemoFlags.isFlag(DEMOFLAG_CollectEngine),"engine tutorial already completed");
  check(!pc_solo_test_repair_tutorial(p),"tutorial repair idempotent");
 }
 PlayerState loaded;loaded.mIsTutorialMode=false;loaded.mUfoParts[UFO_MainEngine].mPartVisType=PARTVIS_Invisible;
 loaded.mCurrParts=2;loaded.mLivingPikiNum=243;loaded.mStagePartsCollected[0]=2;
 check(pc_solo_test_repair_tutorial(loaded),"old test card tutorial flags repaired");
 check(loaded.mCurrParts==2&&loaded.mLivingPikiNum==243&&loaded.mStagePartsCollected[0]==2,"loaded progress not reset");
 check(!loaded.mDemoFlags.isFlag(DEMOFLAG_UfoPartDiscoveryOffset+UFO_SecretSafe),"later discoveries remain untouched");
 PlayerState tutorial;check(!pc_solo_test_repair_tutorial(tutorial)&&tutorial.mDemoFlags.bits==0,"real tutorial untouched");
 PlayerState noEngine;noEngine.mIsTutorialMode=false;check(!pc_solo_test_repair_tutorial(noEngine),"missing engine untouched");
 PlayerState invalid;PikiInfMgr b;invalid.mTotalParts=1;
 pc_solo_test_prepare_new_campaign(invalid,b,1);
 check(invalid.mCurrParts==0&&b.mPikiCounts[Red][Leaf]==0,"invalid registry untouched");
 invalid.mTotalParts=UFO_COUNT;invalid.mUfoParts=nullptr;
 pc_solo_test_prepare_new_campaign(invalid,b,1);
 check(invalid.mCurrParts==0,"missing registry untouched");
 std::ifstream f("p1-solo-test-events.txt");std::string first;std::getline(f,first);f.close();
 check(first.find("preset_new_file_slot_parts 0 1")!=std::string::npos,"setup labelled separately");
 for(int i=0;i<5000;++i)pc_solo_test::record("bounded",i);
 std::ifstream size("p1-solo-test-events.txt",std::ios::binary|std::ios::ate);
 check(size.tellg()<=65536,"persistent log bounded");size.close();
 std::remove("p1-solo-test-events.txt");
#else
 PlayerState p;PikiInfMgr b;
 check(p.mCurrParts==0&&p.mContainerFlag==0&&b.mPikiCounts[Red][Leaf]==0,"standard build has no preset");
#endif
 std::printf("%d P1 test preset/profile checks; %d failures\n",checks,failed);
 return failed?1:0;
}
'''.replace('ENUMS',enums).replace('PROFILE',(ROOT/'ios/pikmin1_solo_test_profile.h').as_posix())
out=Path(sys.argv[1]);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(code,encoding='utf-8')
print('Generated P1 actual preset/profile fixture; no game assets needed')
