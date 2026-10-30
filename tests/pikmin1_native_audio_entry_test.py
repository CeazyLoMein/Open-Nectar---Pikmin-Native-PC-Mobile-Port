"""Compile the actual native JAudio entrypoint bodies against bounded fake tracks.
This catches wiring into the fallback engine instead of PIKI_USE_JAUDIO=1.
No proprietary banks, game window, device or game input are used.
"""
import re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def function(path,name):
 s=(root/path).read_text(encoding='utf-8');m=re.search(r'(?:void|BOOL) '+name+r'\([^)]*\)\s*\{',s);assert m,name
 start=m.start();i=s.index('{',m.start());end=i+1;depth=1
 while depth:
  depth+=(s[end]=='{')-(s[end]=='}');end+=1
 return s[start:end]
enums=[]
for name in ['piki_player','verysimple','piki_scene']:
 s=(root/f'games/pikmin1/include/jaudio/{name}.h').read_text(encoding='utf-8')
 enums+=re.findall(r'typedef enum \w+\s*\{.*?\}\s*\w+;',s,re.S)
player='games/pikmin1/src/jaudio/piki_player.c';system='games/pikmin1/src/jaudio/verysimple.c'
bodies='\n'.join(function(path,name) for path,names in [(player,['Jac_Orima_Walk','Jac_Orima_Formation','Jac_PlayOrimaSe','Jac_StopOrimaSe']),(system,['Jac_PauseCheck','Jac_PlaySystemSe','Jac_StopSystemSe'])] for name in names)
fixture=r"""
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <vector>
#define NECTAR_COOP_WORLD 1
#include "netplay/pc_coop_audio.h"
#define VERSION_GPIE01_01 1
#define TRUE 1
#define FALSE 0
#define STACK_PAD_VAR(x)
using u8=std::uint8_t;using u16=std::uint16_t;using vu16=volatile u16;using u32=std::uint32_t;using s32=std::int32_t;using BOOL=int;
ENUMS
struct seqp_ {int value=0;};struct CmdQueue {int port=0;};
seqp_ nativeTrack;int captured=0,localCommands=0,source=0,local=0,errors=0;bool demo=false;
struct Raw {unsigned kind;int sound;};std::vector<Raw> cues;
bool pc_audio_source_audible(){return source<0 || source==local;}
void pc_coop_audio_raw(unsigned kind,int sound,int,int){if(pc_coop_audio_call_depth()<=1){++captured;cues.push_back({kind,sound});}}
seqp_* Jam_GetTrackHandle(u32){return &nativeTrack;}
void Jal_AddCmdQueue(CmdQueue* q,seqp_*,int port){q->port=port;}
void Jam_WritePortAppDirect(seqp_*,int,u32){++localCommands;}
void Jal_SendCmdQueue_Noblock(CmdQueue*,u16){++localCommands;}
void Jac_FadeOutBgm(int,int){}
void Jac_SetBgmModeFlag(int,int,int){}
void Jam_PauseTrack(seqp_*,int){}void Jam_UnPauseTrack(seqp_*,int){}
void Jac_PauseOrimaSe(){}void Jac_UnPauseOrimaSe(){}
void Jac_PlayDemoSequenceDirect(int){}void Jac_StartDemoSound(int){}
void Jac_DemoFade(int,int,float){}void WaveScene_Set(int,int){}
void StreamSetDVDPause(int,int){}
int StreamSyncCheckBusy(int,int){return 0;}
BOOL Jac_DemoCheck(){return demo;}BOOL Jac_DemoWalkCheck(){return !demo;}
u32 Jac_GetCurrentScene(){return SCENE_Course;}
u32 GetRandom_ulimit(u32){return 0;}
int sqrtf2(int x){return static_cast<int>(std::sqrt(float(x)));}
static u32 gaya_timer=0;static seqp_* stick_seqp=nullptr;static seqp_* orima_seqp=nullptr;
static BOOL cmdqueue_reset=0,pausemode=0,container=0;static u32 countdown_count=0,sys_voldown_flag=0;
static CmdQueue system_se,system_se_stop;
BOOL InitQueue(){return TRUE;}
BOOL Jac_PauseCheck();void Jac_PlaySystemSe(s32);void Jac_StopSystemSe(s32);void Jac_PlayOrimaSe(u32);void Jac_StopOrimaSe(s32);
#if defined(_MSC_VER)
#pragma warning(push)
#pragma warning(disable:4100 4101 4244 4459)
#endif
#if defined(__clang__) || defined(__GNUC__)
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wunused-variable"
#pragma GCC diagnostic ignored "-Wunused-value"
#endif
BODIES
#if defined(_MSC_VER)
#pragma warning(pop)
#endif
#if defined(__clang__) || defined(__GNUC__)
#pragma GCC diagnostic pop
#endif
void check(bool v,const char* s){if(!v){++errors;std::printf("FAIL %s\n",s);}}
int main(){
 source=1;local=0;captured=localCommands=0;
 Jac_Orima_Walk(1,0);Jac_Orima_Formation(70,0);Jac_PlayOrimaSe(JACORIMA_PikiCalled);Jac_StopOrimaSe(JACORIMA_Gather);
 check(captured==4 && localCommands==0,"all four actual native captain paths capture BEFORE host-only ownership filtering");
 check(cues.size()==4 && cues[0].kind==10 && cues[1].kind==9 && cues[2].kind==5 && cues[3].kind==6,"actual native entrypoints use the expected cue types");
 source=1;local=1;captured=localCommands=0;Jac_PlayOrimaSe(JACORIMA_PikiCalled);Jac_Orima_Walk(1,0);
 check(captured==2 && localCommands>=2,"own original JAudio commands still reach native tracks");
 source=-1;captured=0;Jac_PlaySystemSe(JACSYS_WorkFinish);Jac_StopSystemSe(JACSYS_WorkFinish);
 check(captured==2,"actual native system cue start and stop are relayed");
 captured=0;Jac_PlayOrimaSe(JACORIMA_PlayerDown);
 check(captured==1,"nested native death jingle is not sent twice");
 captured=0;Jac_PlaySystemSe(JACSYS_Pause);check(Jac_PauseCheck() && captured==0,"native pause remains local while closing the actual JAudio pause gate");
 Jac_PlaySystemSe(JACSYS_Unpause);check(!Jac_PauseCheck() && captured==0,"native resume reopens actual JAudio pause gate");
 captured=0;Jac_PlaySystemSe(JACSYS_ContainerOK);check(captured==1,"nested native container sound is relayed once");
 std::puts(errors?"NATIVE AUDIO ENTRY FAIL":"NATIVE AUDIO ENTRY PASS");return errors?1:0;
}
"""
out=Path(sys.argv[1]);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(fixture.replace('ENUMS','\n'.join(enums)).replace('BODIES',bodies),encoding='utf-8')
