"""Generate an actual command/admission/start/cache-reset fixture on controlled OS leaves.

Links the real CARD/history backend. SDK mutexes are backed by std::mutex;
only the engine's forever worker/thread launch are controlled by this test.
"""
from pathlib import Path
import runpy,sys
ROOT=Path(__file__).resolve().parents[1]
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
runpy.run_path(str(ROOT/'tests/pikmin1_practice_card_test.py'),run_name='__main__')
def block(text,signature):
 a=text.index(signature);b=text.index('{',a);i=b+1;level=1
 while level:level+=(text[i]=='{')-(text[i]=='}');i+=1
 return text[a:i]
inc=ROOT/'games/pikmin1/include';pc=ROOT/'games/pikmin1/pc_port';src=ROOT/'games/pikmin1/src/plugPikiColin'
sdk=out/'Dolphin/card.h'
sdk.write_text(sdk.read_text()+'\n'+next(line for line in (inc/'Dolphin/card.h').read_text().splitlines() if line.startswith('#define CARD_COMMENT_SIZE'))+'\n')
types=out/'types.h';types.write_text(types.read_text()+'\nclass RandomAccessStream;\n#define immut const\n')
for f in ['CardUtil.h','MemoryCard.h']:(out/f).write_text((inc/f).read_text(encoding='utf-8'),encoding='utf-8')
(out/'CoreNode.h').write_text('#pragma once\nstruct CoreNode { explicit CoreNode(const char*) {} };\n',encoding='utf-8')
osdir=out/'Dolphin/OS';osdir.mkdir(exist_ok=True)
(osdir/'OSMutex.h').write_text('''#pragma once
#include <mutex>
struct OSMutex { std::mutex value; }; struct OSCond {};
inline void OSInitMutex(OSMutex*){} inline void OSInitCond(OSCond*){}
inline void OSLockMutex(OSMutex* m){m->value.lock();} inline void OSUnlockMutex(OSMutex* m){m->value.unlock();}
inline void OSSignalCond(OSCond*){}
''',encoding='utf-8')
(osdir/'OSThread.h').write_text('''#pragma once
#include <cstdint>
struct OSThread {}; enum { OS_THREAD_ATTR_DETACH=1 };
void OSCreateThread(OSThread*,void*(*)(void*),void*,void*,std::uint32_t,std::int32_t,int);
inline void OSResumeThread(OSThread*){}
''',encoding='utf-8')
util=(src/'cardutil.cpp').read_text(encoding='utf-8');mem=(src/'memoryCard.cpp').read_text(encoding='utf-8')
state=util[util.index('namespace {\nstd::atomic<bool> sCardUtilInitialized'):util.index('\n#endif',util.index('namespace {\nstd::atomic<bool> sCardUtilInitialized'))]
methods='\n'.join(block(util,signature) for signature in ['static s32 CardUtilCommand(','void CardUtilInit('])
reset=block(mem,'bool MemoryCard::pcResetForCoopPractice()')
prefix=(out/'practice-card-test.cpp').read_text().split('int main(int argc,char** argv)')[0]
test=prefix+'''
#include "CardUtil.h"
#include "MemoryCard.h"
#include "netplay/pc_coop_practice_start.h"
#include "netplay/pc_coop_switch.h"
#include "pc_coop.h"
#include <atomic>
#include <exception>
CardUtilControl CardControl; CardUtilThread CardThread;
static CARDStat cst{};u8 cardData[CARD_DATA_SIZE];
static void* CardUtilMain(void*) { return nullptr; }
static bool createdIdle=false;
void OSCreateThread(OSThread*,void*(*)(void*),void*,void*,u32,s32,int){createdIdle=CardControl.mChannel==-1;}
bool CardUtilIsCardBusy(){const std::lock_guard<std::mutex> g(CardControl.mMutex.value);return CardControl.mChannel!=-1;}
static bool pending=false;static int captains[2]={0,1};
void pc_coop_set_pending(bool v){pending=v;}bool pc_coop_pending(){return pending;}
void pc_coop_set_captain(int p,int v){captains[p]=v;}
'''+state+'\n'+methods+'\n'+reset+r'''
int main(int argc,char** argv){
 if(argc!=2)return 2;
 const auto base=fs::absolute(argv[1]);fs::create_directories(base);
 const auto normal=base/"normal",scratch=base/"scratch";fs::create_directories(normal);fs::create_directories(scratch);
 env("NECTAR_SAVE_DIR",normal.string());
 check(!CardUtilRequestCoopPractice(),"uninitialized queue rejects admission without locking invalid mutex");
 CARDInit();CARDFileInfo real{};char old[8]={'O','L','D','S','O','L','O','!'};
 check(CARDCreate(0,"Pikmin dataFile",8,&real)==0&&CARDWrite(&real,old,8,0)==0,"seed original save with real backend");
 CardUtilInit(nullptr,0,0);check(createdIdle,"actual initialization starts worker idle, not on command0");
 MemoryCard mem;mem.mSaveFileIndex=19;mem.mCardChannel=0;memset(cardData,0x5a,sizeof(cardData));
 check(!mem.pcResetForCoopPractice()&&mem.mSaveFileIndex==19&&cardData[0]==0x5a,"normal cache reset refused with every byte retained");
 char delayed[8]={'D','R','A','I','N','E','D','!'};
 check(CardUtilCommand(0,CARDCMD_Write,reinterpret_cast<void*>(static_cast<intptr_t>(real.fileNo)),delayed,0,8)==CARD_RESULT_READY,"actual producer accepts old queued job");
 check(pc_coop_practice_request_start(scratch.string().c_str()),"driver requests protected admission with old job outstanding");
 check(!pc_coop_practice_request_start(scratch.string().c_str()),"duplicate driver request rejected");
 const auto data=CardControl.mDataPtr;const auto result=CardControl.mResultCode;
 std::atomic<int> accepted{0};std::vector<std::thread> producers;
 for(int i=0;i<8;++i)producers.emplace_back([&]{for(int j=0;j<100;++j)if(CardUtilCommand(0,CARDCMD_Save,nullptr,nullptr,0,0)==CARD_RESULT_READY)++accepted;});
 for(auto& thread:producers)thread.join();
 check(accepted==0&&CardControl.mDataPtr==data&&CardControl.mResultCode==result,"800 concurrent producers cannot replace queued job or result while held");
 for(int i=0;i<8;++i)check(pc_coop_practice_poll_start()==PcCoopPracticeStart::Draining&&!pc_coop_direct_requested(),"title stays put until old worker releases buffers");
 check(!mem.pcResetForCoopPractice()&&cardData[0]==0x5a&&!pc_card_coop_practice_active(),"non-mutating cache query cannot admit private root early");
 check(pc_coop_practice_cancel_start()&&!pc_card_coop_practice_active(),"disconnect before admission cancels safely, retains real card");
 check(!pc_coop_practice_cancel_start(),"second cancellation cannot cancel an unrelated owner");
 // Finish the admitted old job using actual backend and the worker's real completion ordering.
 std::thread worker([&]{const auto rc=CARDWrite(&real,delayed,8,0);const std::lock_guard<std::mutex> g(CardControl.mMutex.value);CardControl.mResultCode=rc;CardControl.mChannel=-1;});worker.join();
 check(bytes(fs::path(pc_card_channel_dir(0))/"Pikmin dataFile")==std::string(delayed,8),"old normal job finishes against original root before transition");
 check(pc_coop_practice_request_start("relative-invalid"),"invalid scratch is staged, never trusted as a save root");
 check(pc_coop_practice_poll_start()==PcCoopPracticeStart::Failed&&!pc_card_coop_practice_active()&&!pc_coop_direct_requested(),"failed filesystem admission does not arm title or fall through to normal file");
 check(CardUtilCommand(0,CARDCMD_List,nullptr,nullptr,0,0)==CARD_RESULT_READY,"failed admission reopens normal producer gate");
 {const std::lock_guard<std::mutex> g(CardControl.mMutex.value);CardControl.mChannel=-1;CardControl.mResultCode=CARD_RESULT_READY;}
 const auto before=snapshot(normal);
 pc_coop_direct_set_slot(3);captains[0]=4;captains[1]=4;
 CardUtilDirent directory{};CardControl.mDirentList=&directory;CardControl.mDirentCount=1;
 check(pc_coop_practice_request_start(scratch.string().c_str()),"retry after refused path is explicit");
 check(CardUtilCommand(0,CARDCMD_List,nullptr,nullptr,0,0)==CARD_RESULT_BUSY&&CardControl.mChannel==-1,"closed gate rejects a racing producer even after old worker is idle");
 check(pc_coop_practice_poll_start()==PcCoopPracticeStart::Armed&&pc_card_coop_practice_active(),"actual root isolation occurs before direct-title intent");
 check(pc_coop_direct_slot()==0&&captains[0]==PC_CAPTAIN_OLIMAR&&captains[1]==PC_CAPTAIN_LOUIE&&pending,"practice cannot inherit normal slot3 or old captain selections");
 check(!CardControl.mDirentList&&CardControl.mDirentCount==0&&!CardControl.mDataPtr&&!CardControl.mFileNo,"old scene directory and worker buffer caches invalidated");
 check(pc_coop_direct_take_title()&&pc_coop_direct_take_setup(),"existing direct path is reusable once admitted");
 check(CardUtilCommand(0,CARDCMD_List,nullptr,nullptr,0,0)==CARD_RESULT_READY,"post-admission jobs can use only private card");
 check(!mem.pcResetForCoopPractice()&&mem.mSaveFileIndex==19&&cardData[0]==0x5a,"cache reset refuses even private jobs still holding buffers");
 {const std::lock_guard<std::mutex> g(CardControl.mMutex.value);CardControl.mChannel=-1;CardControl.mResultCode=CARD_RESULT_READY;}
 mem.mTempFileIndex=18;mem.mOkSectionsMask=15;mem.mValidSlots[0]=1;mem.mDidSaveFail=true;cst.length=88;
 check(pc_coop_practice_prepare_setup(mem),"actual CardSelect bridge clears caches before new area setup");
 check(mem.mCardChannel==-1&&mem.mSaveFileIndex==-1&&mem.mTempFileIndex==-1&&mem.mOkSectionsMask==0&&!mem.mValidSlots[0]&&!mem.mDidSaveFail,"all previous normal-card indices/validity cleared");
 bool zero=true;for(auto b:cardData)zero=zero&&b==0;
 check(zero&&cst.length==0,"normal campaign data buffer and metadata cleared after drain");
 CARDFileInfo temp{};check(CARDCreate(0,"Pikmin dataFile",8,&temp)==0&&CARDWrite(&temp,old,8,0)==0,"new practice writes remain functional");
 check(snapshot(normal)==before,"original save bytes unchanged after practice setup/write");
 check(!pc_coop_practice_prepare_setup(mem),"setup cannot run twice or reset live practice buffers");
 check(pc_coop_practice_restart_required()&&!CardUtilCancelCoopPractice()&&!pc_coop_practice_cancel_start(),"admitted cancellation cannot route back to real saves; restart is required");
 if(!failures)std::puts("PASS actual CardUtil admission + protected title/setup + MemoryCard reset: busy drain, 800 blocked producers, cancellation, failure/retry, cache lifetime, original bytes");
 return failures?1:0;
}
'''
(out/'practice-admission-test.cpp').write_text(test,encoding='utf-8')
print('Generated actual command/admission/start/cache-reset fixture:',out)
