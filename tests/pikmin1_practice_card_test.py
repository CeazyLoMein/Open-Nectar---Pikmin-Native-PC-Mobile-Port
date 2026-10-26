"""Build actual CARD/history source against extracted SDK leaves and controlled mode dependencies."""
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
assert (ROOT/"games").is_dir(), "Run from the repository tests directory"
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True);(out/'Dolphin').mkdir(exist_ok=True);(out/'randomizer').mkdir(exist_ok=True)
def block(text,signature):
 a=text.index(signature);b=text.index('{',a);i=b+1;level=1
 while level:level+=(text[i]=='{')-(text[i]=='}');i+=1
 return text[a:i]
card=(ROOT/'games/pikmin1/pc_port/dolphin_stubs/card_stubs.cpp').read_text(encoding='utf-8')
sdk=(ROOT/'games/pikmin1/include/Dolphin/card.h').read_text(encoding='utf-8')
constants='\n'.join(line for line in sdk.splitlines() if re.match(r'#define CARD_(RESULT_|FILENAME_MAX|MAX_FILE|ICON_MAX|ENCODE_|WORKAREA_SIZE)',line))
structs=block(sdk,'struct CARDFileInfo {')+';\n'+block(sdk,'struct CARDStat {')+';\n'
exports=card[card.index('extern "C" {'):]
prototypes=re.findall(r'((?:void|BOOL|s32|u16)\s+(?:CARD\w+|__CARD\w+)\s*\([^)]*\))\s*\{',exports)
header='''#pragma once
#include <cstdint>
using s32=std::int32_t;using u32=std::uint32_t;using u16=std::uint16_t;using u8=std::uint8_t;using u64=std::uint64_t;using BOOL=int;
struct DVDDiskID;struct CARDMemoryCard;
using CARDCallback=void(*)(s32,s32);
'''+constants+'\n'+structs+'\nextern "C" {\n'+';\n'.join(prototypes)+';\n}\n'
(out/'Dolphin/card.h').write_text(header,encoding='utf-8')
(out/'types.h').write_text('#pragma once\n#include <cstdint>\nusing u32=std::uint32_t;using u64=std::uint64_t;\n',encoding='utf-8')
(out/'windows.h').write_text('''#pragma once
// Test supplies an explicit save root; executable-location discovery is unused.
#include <cstdint>
using DWORD=std::uint32_t;
inline DWORD GetModuleFileNameW(void*,wchar_t*,DWORD){return 0;}
''',encoding='utf-8')
(out/'Dolphin/dvd.h').write_text('''#pragma once
struct DVDDiskID {char gameName[4];char company[2];};
extern "C" DVDDiskID* DVDGetCurrentDiskID();
''',encoding='utf-8')
(out/'pc_speedrun.h').write_text('''#pragma once
enum{PC_SR_CAT_LOW_PIKMIN=1};bool pc_speedrun_active();const char* pc_speedrun_card_subdir();int pc_speedrun_category();
''',encoding='utf-8')
(out/'randomizer/pc_randomizer.h').write_text('#pragma once\nbool pc_randomizer_menu_pending();\n',encoding='utf-8')
ach=(ROOT/'games/pikmin1/pc_port/pc_achievements.cpp').read_text(encoding='utf-8')
achievement_methods=block(ach,'void save()')+'\n'+block(ach,'const char* pc_achievements_blocked_reason(void)')
boolgets=['piki_invincible','all_flowers','unlock_zones','no_day_advance','all_onions','infinite_day']
dependencies='\n'.join('bool pc_settings_get_'+n+'(){return false;}' for n in boolgets)
dependencies+='\nfloat pc_settings_get_carry_speed_scale(){return 1;}float pc_settings_get_navi_speed_scale(){return 1;}\n'
dependencies+='int pc_settings_get_navi_health_pct(){return 100;}int pc_settings_get_teki_health_pct(){return 100;}int pc_settings_get_piki_limit(){return 100;}bool pc_vs_active(){return false;}\n'
test=r'''
#include "Dolphin/card.h"
#include "Dolphin/dvd.h"
#include "dolphin_stubs/pc_card_paths.h"
#include "pc_day_history.h"
#include <filesystem>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <cstdio>
#include <cstring>
#include <future>
#include <thread>
#include <chrono>
namespace fs=std::filesystem;
static bool speed=false,randomized=false;
bool pc_speedrun_active(){return speed;}
const char* pc_speedrun_card_subdir(){return "all-parts";}
int pc_speedrun_category(){return 0;}
bool pc_randomizer_menu_pending(){return randomized;}
extern "C" DVDDiskID* DVDGetCurrentDiskID(){static DVDDiskID id{{'G','P','I','E'},{'0','1'}};return &id;}
std::string pc_card_save_dir();std::string pc_card_root_dir();std::string pc_card_speedrun_dir();
static_assert(sizeof(CARDStat)==0x6c,"extracted real card metadata layout");
int failures=0;void check(bool ok,const char* why){if(!ok){std::printf("FAIL %s\n",why);++failures;}}
void env(const char* key,const std::string& value){
#ifdef _WIN32
 _putenv_s(key,value.c_str());
#else
 setenv(key,value.c_str(),1);
#endif
}
std::string bytes(const fs::path& p){std::ifstream in(p,std::ios::binary);return std::string(std::istreambuf_iterator<char>(in),std::istreambuf_iterator<char>());}
std::map<std::string,std::string> snapshot(const fs::path& root){std::map<std::string,std::string> result;
 for(const auto& p:fs::recursive_directory_iterator(root))if(p.is_regular_file())result[fs::relative(p.path(),root).generic_string()]=bytes(p.path());return result;}
static int callbacks=0;static s32 callbackResult=999;
void callback(s32,s32 result){
 ++callbacks;callbackResult=result;
 auto done=std::make_shared<std::promise<void>>();auto future=done->get_future();
 std::thread other([done]{const std::lock_guard<std::recursive_mutex> guard(pc_card_io_mutex());done->set_value();});
 const bool free=future.wait_for(std::chrono::seconds(2))==std::future_status::ready;
 check(free,"callback is outside I/O lock, allowing another worker thread to acquire it");
 if(free)other.join();else other.detach();
}
constexpr const char* kFilename="pikmin_achievements.txt";constexpr int PC_ACH_COUNT=3;bool sUnlocked[PC_ACH_COUNT]={true,false,false};
'''+dependencies+achievement_methods+r'''
int main(int argc,char** argv){
 if(argc!=2)return 2;
 const auto base=fs::absolute(argv[1]);fs::create_directories(base);
 const auto normal=base/"normal",scratch=base/"scratch";fs::create_directories(normal);fs::create_directories(scratch);
 env("NECTAR_SAVE_DIR",normal.string());
 check(!pc_card_begin_coop_practice(scratch.string().c_str()),"uninitialized normal card cannot admit practice");
 CARDInit();check(!pc_card_coop_practice_active()&&fs::equivalent(pc_card_save_dir(),normal),"ordinary card routing remains baseline");
 CARDFileInfo real{};char original[8]={'S','O','L','O','D','A','T','A'};
 check(CARDCreate(0,"Pikmin dataFile",8,&real)==0&&CARDWrite(&real,original,8,0)==0,"real backend seeds normal card fixture");
 char day[8]={'D','A','Y','2',0,0,0,0};pc_days_store(0,2,day,8);
 save();const auto achievementBefore=bytes(kFilename);
 const auto before=snapshot(normal);
 env("NECTAR_SAVE_DIR",(base/"ignored-late-env").string());
 check(fs::equivalent(pc_card_save_dir(),normal),"cached normal root ignores late environment override");
 check(!pc_card_begin_coop_practice(normal.string().c_str()),"real card directory cannot be scratch base");
 check(!pc_card_begin_coop_practice(base.string().c_str()),"ancestor containing real saves cannot be scratch base");
 fs::create_directories(normal/"nested");check(!pc_card_begin_coop_practice((normal/"nested").string().c_str()),"real card descendant cannot be scratch base");
 check(!pc_card_begin_coop_practice("relative-path"),"relative scratch path refused");
 {std::ofstream out(base/"not-a-directory");out<<"file";}
 check(!pc_card_begin_coop_practice((base/"not-a-directory").string().c_str()),"non-directory scratch base refused");
 check(snapshot(normal)==before&&!pc_card_coop_practice_active(),"failed admissions preserve every original file byte");
 std::future<bool> admission;std::promise<void> entering;
 {
  const std::lock_guard<std::recursive_mutex> held(pc_card_io_mutex());
  admission=std::async(std::launch::async,[&]{entering.set_value();return pc_card_begin_coop_practice(scratch.string().c_str());});
  entering.get_future().wait();
  check(admission.wait_for(std::chrono::milliseconds(40))==std::future_status::timeout,"admission waits for in-flight card I/O boundary");
 }
 check(admission.wait_for(std::chrono::seconds(10))==std::future_status::ready&&admission.get(),"fresh card admitted after old I/O finishes");
 const auto practice=fs::path(pc_card_save_dir());
 check(pc_card_coop_practice_active()&&fs::equivalent(practice.parent_path(),scratch)&&practice!=normal,"practice is a fresh private child of approved scratch base");
 check(snapshot(practice).empty(),"no existing solo campaign copied into practice");
 check(!pc_card_begin_coop_practice(scratch.string().c_str())&&fs::path(pc_card_save_dir())==practice,"second admission cannot reset or switch card session");
 check(pc_achievements_blocked_reason()!=nullptr,"actual achievement policy blocks practice awards");
 sUnlocked[1]=true;save();check(bytes(kFilename)==achievementBefore,"actual achievement writer leaves original file unchanged in practice");
 check(CARDWrite(&real,original,8,0)==CARD_RESULT_NOFILE,"old normal-card file handle cannot write into an empty practice card");
 CARDFileInfo temp{};char payload[8]={'P','R','A','C','T','I','C','E'};
 check(CARDMountAsync(0,nullptr,nullptr,callback)==0&&callbacks==1&&callbackResult==0,"mount callback still delivered outside I/O transaction");
 check(CARDCreateAsync(0,"Pikmin dataFile",8,&temp,callback)==0&&callbacks==2,"actual asynchronous create works on private card");
 check(CARDWriteAsync(&temp,payload,8,0,callback)==0&&callbacks==3,"practice write and callback work");
 char read[8]={};check(CARDRead(&temp,read,8,0)==0&&!std::memcmp(read,payload,8),"actual practice card roundtrip");
 check(CARDWrite(&real,payload,8,0)==0,"even reused old file index now resolves only within private card");
 CARDStat stat{};check(CARDGetStatus(0,temp.fileNo,&stat)==0&&stat.length==8,"metadata stays functional");
 stat.commentAddr=2;check(CARDSetStatus(0,temp.fileNo,&stat)==0,"practice metadata update");
 check(CARDRename(0,"Pikmin dataFile","Practice renamed")==0,"practice rename");
 check(CARDOpen(0,"Practice renamed",&temp)==0&&CARDFastDelete(0,temp.fileNo)==0,"practice delete");
 check(fs::path(pc_card_channel_dir(1)).parent_path()==practice,"second card channel isolated too");
 CARDFileInfo second{};check(CARDCreate(1,"second",8,&second)==0,"second channel create");
 // Checked absolute targets before calling existing recursive CARDFormat.
 check(fs::path(pc_card_channel_dir(0)).parent_path()==practice&&practice.parent_path()==fs::canonical(scratch),"format target is beneath newly owned scratch child");
 check(CARDFormat(0)==0,"format operates on practice channel only");
 pc_days_store(0,3,payload,8);int days[3]={};check(pc_days_list(0,days,3)==1&&days[0]==3,"day history writes private card");
 pc_days_copy_slot(0,1);check(pc_days_read(1,3,read,8)&&!std::memcmp(read,payload,8),"history copy/read remain private");
 pc_days_delete_slot(0);check(pc_days_list(0,days,3)==0,"history delete remains private");
 speed=true;check(fs::path(pc_card_root_dir()).parent_path().parent_path()==practice/"speedrun","speedrun card root stays under practice");
 speed=false;randomized=true;check(fs::path(pc_card_root_dir()).parent_path()==practice/"randomizer","randomizer card root stays under practice");randomized=false;
 {std::ofstream out(fs::path(pc_card_speedrun_dir())/"records.txt");out<<"practice record";}
 std::thread delayed([&]{for(int i=0;i<100;++i){CARDFileInfo late{};if(CARDOpen(1,"second",&late)==0)CARDWrite(&late,payload,8,0);}});
 for(int i=0;i<100;++i)CARDProbe(0);delayed.join();
 check(snapshot(normal)==before,"all original normal card/metadata/history bytes remain identical after mixed delayed practice writes");
 check(pc_card_coop_practice_active()&&fs::path(pc_card_save_dir())==practice,"practice routing remains latched until process restart");
 if(!failures)std::puts("PASS actual CARD/history/achievement source: cached roots, failed admission, I/O barrier, both channels, stale handles, callbacks, rename/delete/format and original-byte preservation");
 return failures?1:0;
}
'''
(out/'practice-card-test.cpp').write_text(test,encoding='utf-8')
print('Generated actual CARD/history/achievement policy fixture:',out)
