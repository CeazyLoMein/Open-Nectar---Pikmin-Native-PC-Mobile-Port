"""Generate isolated tests of the actual P1 save/list recovery stages."""
from pathlib import Path
import runpy,sys
root=Path(__file__).resolve().parents[1]; out=Path(sys.argv[1]); out.mkdir(parents=True,exist_ok=True)
sys.argv=['pikmin1_practice_admission_test.py',str(out)]
runpy.run_path(str(root/'tests/pikmin1_practice_admission_test.py'),run_name='__main__')
def block(text,sig):
 a=text.index(sig); b=text.index('{',a); i=b+1; level=1
 while level:
  level += (text[i]=='{')-(text[i]=='}');i+=1
 return text[a:i]
sdk=(root/'games/pikmin1/include/Dolphin/card.h').read_text(encoding='utf-8')
h=out/'Dolphin/card.h';s=h.read_text(encoding='utf-8')
for prefix in ('#define CARD_READ_SIZE','#define CARD_STAT_SPEED_END','#define CARD_STAT_ICON_NONE','#define CARD_STAT_ANIM_BOUNCE','#define CARD_STAT_ANIM_MASK','#define CARD_STAT_ICON_MASK','#define CARD_STAT_SPEED_MASK','#define TRUNC(','#define OFFSET(','#define CARDGetIcon'):
 s+='\n'+'\n'.join(line for line in sdk.splitlines() if line.startswith(prefix))
h.write_text(s+'\n',encoding='utf-8')
source=(root/'games/pikmin1/src/plugPikiColin/cardutil.cpp').read_text(encoding='utf-8')
listing=block(source,'static s32 DoList(');saving=block(source,'static s32 DoSave(')
for name in ('CARDCreate','CARDWrite','CARDSetStatus','CARDFastDelete','CARDRename'):
 saving=saving.replace(name+'(', 'Fail'+name+'(')
prefix=(out/'practice-card-test.cpp').read_text(encoding='utf-8').split('int main(int argc,char** argv)')[0]
prefix=prefix.replace('static bool speed=false,randomized=false;', 'static bool testSpeed=false,randomized=false;').replace('return speed;', 'return testSpeed;')
test=prefix+'''\n#include "CardUtil.h"
#include <algorithm>
#define ALIGN_NEXT(x,n) (((x)+(n)-1)&~((n)-1))
inline void DCFlushRange(void*,u32){}
void CardUtilLockDirectory(){} void CardUtilUnlockDirectory(){}
CardUtilControl CardControl{};
s32* CardUtilByteNotUsed(){return &CardControl.mByteNotUsed;}
s32* CardUtilFilesNotUsed(){return &CardControl.mFilesNotUsed;}
static int fault=0;
s32 FailCARDCreate(s32 c,const char* n,u32 z,CARDFileInfo* i){return fault==1?CARD_RESULT_IOERROR:CARDCreate(c,n,z,i);}
s32 FailCARDWrite(CARDFileInfo* i,void* d,s32 n,s32 o){
 if(fault==2)return CARD_RESULT_IOERROR;
 if(fault==6){if(CARDWrite(i,d,n/2,o)<0)return CARD_RESULT_FATAL_ERROR;return CARD_RESULT_IOERROR;}
 return CARDWrite(i,d,n,o);
}
s32 FailCARDSetStatus(s32 c,s32 n,CARDStat* s){
 if(fault==3)return CARD_RESULT_IOERROR;
 if(fault==7){if(CARDSetStatus(c,n,s)<0)return CARD_RESULT_FATAL_ERROR;return CARD_RESULT_IOERROR;}
 return CARDSetStatus(c,n,s);
}
s32 FailCARDFastDelete(s32 c,s32 n){
 if(fault==4)return CARD_RESULT_IOERROR;
 if(fault==8){if(CARDFastDelete(c,n)<0)return CARD_RESULT_FATAL_ERROR;return CARD_RESULT_IOERROR;}
 return CARDFastDelete(c,n);
}
s32 FailCARDRename(s32 c,const char* a,const char* b){
 if(fault==5)return CARD_RESULT_IOERROR;
 if(fault==9){if(CARDRename(c,a,b)<0)return CARD_RESULT_FATAL_ERROR;return CARD_RESULT_IOERROR;}
 return CARDRename(c,a,b);
}
'''+listing+'\n'+saving+'''\nint main(int argc,char** argv){
 if(argc!=2)return 2;const auto base=fs::absolute(argv[1]);fs::create_directories(base);env("NECTAR_SAVE_DIR",base.string());CARDInit();
 for(int stage=0;stage<=9;++stage){
  const std::string name="Save"+std::to_string(stage);CARDFileInfo file{};std::vector<char> old(512,'A'),now(512,'B');
  check(CARDCreate(0,name.c_str(),512,&file)==0 && CARDWrite(&file,old.data(),512,0)==0,"seed original fixture");
  CARDStat stat{};check(CARDGetStatus(0,file.fileNo,&stat)==0,"read original metadata");stat.commentAddr=0;stat.length=512;
  fault=stage;const auto saved=DoSave(0,&stat,now.data());fault=0;
  check((stage==0 && saved>=0)||(stage!=0 && saved<0),"save reaches the selected injected failure");
  std::vector<CardUtilDirent> entries(CARD_MAX_FILE);check(DoList(0,entries.data())>=0,"actual startup listing recovers interrupted temp");
  CARDFileInfo current{};check(CARDOpen(0,name.c_str(),&current)==0,"original or completed save remains accessible");
  std::vector<char> observed(512);check(CARDRead(&current,observed.data(),512,0)==0,"recovered save can be read");
  check(observed==((stage==0||stage==5||stage==8||stage==9)?now:old),"recovered bytes match a complete old or new file");
  CardControl.mDirentList=nullptr;CardControl.mDirentCount=0;
 }
 std::puts(failures?"SAVE RECOVERY FIXTURE FAIL":"SAVE RECOVERY FIXTURE PASS");return failures?1:0;
}
'''
(out/'save-recovery-test.cpp').write_text(test,encoding='utf-8')
