"""Compile fixtures extracted from the actual title labels and opaque-room pause."""
import argparse
import subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def block(text,needle):
 a=text.index(needle);a=text.index('{',a);depth=1;b=a+1
 while depth:
  depth += (text[b]=='{')-(text[b]=='}');b+=1
 return text[a:b]
def generate(output):
 title=(ROOT/'games/pikmin1/src/plugPikiOgawa/ogTitle.cpp').read_text(encoding='utf-8')
 labels=block(title,'void zen::ogScrTitleMgr::pcInsertCoopItem')
 a=title.index('#if defined(NECTAR_IOS_COOP_ROOM) || defined(NECTAR_DESKTOP_COOP_ROOM)\n        static const int kPcRowToAction')
 b=title.index('\n\t\tif (mCurrentSelection >= 0',a)
 mapping=title[a:b]
 system=(ROOT/'games/pikmin1/src/sysDolphin/system.cpp').read_text(encoding='utf-8')
 pause=block(system,'if (nectar_ios_coop_room_is_open())')
 fixture=r'''
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <chrono>
#include <thread>
#include "pc_frame_scheduler.h"
#define immut const
// Enforce the Apple SDK API restriction even when the local SDK permits sprintf.
#define sprintf NECTAR_UNBOUNDED_SPRINTF_IS_FORBIDDEN
struct P2DTextBox {char* text;char* getString(){return text;}void setString(char* s){text=s;}};
struct Screen {
 std::map<std::string,P2DTextBox> boxes;
 void* search(const std::string& tag,bool){auto p=boxes.find(tag);return p==boxes.end()?nullptr:&p->second;}
};
struct P2DPaneLibrary {static std::string makeTag(const char* s){return s;}};
struct DrawMenu {Screen screen;Screen* getScreenPtr(){return &screen;}};
namespace zen {struct ogScrTitleMgr {void pcInsertCoopItem(DrawMenu*);};}
void zen::ogScrTitleMgr::pcInsertCoopItem(DrawMenu* menu) LABELS
int failures=0;
void check(bool yes,const char* label){if(!yes){std::printf("FAIL %s\n",label);++failures;}}
int remaining=0,polls=0,audio=0;bool closeRequested=false;
struct PADStatus {int unused=0;};
int nectar_ios_coop_room_is_open(){return remaining>0;}
void Jac_Gsync(){++audio;}
void pc_window_poll_events(PADStatus*){++polls;--remaining;}
bool pc_window_should_close(){return closeRequested;}
unsigned OSGetTick(){return 42;}
int main(){
 static char start[]="Start",options[]="Options",challenge[]="Challenge Mode",copy[]="clone";
 zen::ogScrTitleMgr manager;
 for(bool unlocked:{false,true}) {
  DrawMenu menu;
#if defined(NECTAR_IOS_COOP_ROOM) || defined(NECTAR_DESKTOP_COOP_ROOM)
  const int count=unlocked?8:7;
  const char* expected[]={"Start","Co-op","Online Co-op","VS","Options","Speedrun","Randomizer","Challenge Mode"};
#else
  const int count=unlocked?7:6;
  const char* expected[]={"Start","Co-op","VS","Options","Speedrun","Randomizer","Challenge Mode"};
#endif
  for(const char* family:{"he%02d","hm%02d"})for(int i=0;i<count;++i){
   char key[8];std::snprintf(key,sizeof(key),family,i);
   menu.screen.boxes[key].text=i==0?start:i==1?options:i==2&&unlocked?challenge:copy;
  }
  manager.pcInsertCoopItem(&menu);
  for(const char* family:{"he%02d","hm%02d"})for(int i=0;i<count;++i){
   char key[8];std::snprintf(key,sizeof(key),family,i);
   check(std::strcmp(menu.screen.boxes[key].text,expected[i])==0,"actual title labels/order retain local modes and challenge");
  }
 }
 MAPPING
 check(kPcRowToAction[0]==0 && kPcRowToAction[1]==2,"solo/local coop actions preserved");
#if defined(NECTAR_IOS_COOP_ROOM) || defined(NECTAR_DESKTOP_COOP_ROOM)
 check(kPcRowToAction[2]==7 && kPcRowToAction[3]==3 && kPcRowToAction[4]==4,"online vs options action mapping");
#else
 check(kPcRowToAction[2]==3 && kPcRowToAction[3]==4,"desktop VS/options unchanged");
#endif
 for(int clamp:{0,1,2})for(int covered:{0,3})for(bool quit:{false,true}){
  int mFrameRate=clamp;unsigned mPrevTick=0;int gameTicks=0;
  PcFrameScheduler frameScheduler;frameScheduler.reset(0,clamp);
  remaining=covered;polls=audio=0;closeRequested=quit;
  for(int i=0;i<4;++i){
#if defined(NECTAR_IOS_COOP_ROOM) || defined(NECTAR_DESKTOP_COOP_ROOM)
   if(nectar_ios_coop_room_is_open()) PAUSE
#endif
   ++gameTicks;
  }
#if defined(NECTAR_IOS_COOP_ROOM) || defined(NECTAR_DESKTOP_COOP_ROOM)
  if(covered){
   check(gameTicks==(quit?0:1) && polls==(quit?1:3) && audio==polls,"opaque UI pumps events/audio, skips hidden game ticks/draws, honors quit");
   if(!quit){
    check(mPrevTick==42,"paused wall time reset");
    check(frameScheduler.discardedTicks()==0,"no paused catch-up backlog");
   }
  }else check(gameTicks==4&&polls==0,"visible gameplay untouched");
#else
  check(gameTicks==4&&polls==0,"non-iOS loop untouched");
  (void)mPrevTick;
#endif
  check(mFrameRate==clamp,"player FPS/clamp unchanged including120");
 }
 std::printf("actual title/modal source checks: %s\n",failures?"FAILED":"PASS");
 return failures?1:0;
}
'''
 fixture=fixture.replace('LABELS',labels).replace('MAPPING',mapping).replace('PAUSE',pause)
 output.parent.mkdir(parents=True,exist_ok=True);output.write_text(fixture,encoding='utf-8')
 print('Generated actual iOS/desktop title-row and opaque-room pause fixture')
def compile_and_run(output, compiler, sdk_root=None):
 source=ROOT/'games/pikmin1/pc_port/timing/pc_frame_scheduler.cpp'
 include=source.parent
 msvc=Path(compiler).name.lower() in ('cl','cl.exe')
 failures=[]
 for mode in ('desktop','native','desktop-coop'):
  build=output.parent/('room-ux-'+mode);build.mkdir(parents=True,exist_ok=True)
  binary=build/('test.exe' if msvc else 'test')
  if msvc:
   command=[compiler,'/nologo','/std:c++17','/EHsc','/W4','/WX','/D_CRT_SECURE_NO_WARNINGS',
            '/I'+str(include)]
   if mode=='native':command+=['/DNECTAR_IOS_COOP_ROOM=1']
   if mode=='desktop-coop':command+=['/DNECTAR_DESKTOP_COOP_ROOM=1']
   command += [str(output),str(source),'/Fe:'+str(binary)]
  else:
   command=[compiler,'-std=c++17','-Wall','-Wextra','-Werror','-I'+str(include)]
   if sdk_root:command += ['-isysroot',str(sdk_root)]
   if mode=='native':command += ['-DNECTAR_IOS_COOP_ROOM=1']
   if mode=='desktop-coop':command += ['-DNECTAR_DESKTOP_COOP_ROOM=1']
   command += [str(output),str(source),'-o',str(binary)]
  print('Compiling actual room UX fixture: '+mode,flush=True)
  try:
   subprocess.run(command,cwd=build,check=True,timeout=120)
   subprocess.run([str(binary)],cwd=build,check=True,timeout=30)
  except (subprocess.CalledProcessError,subprocess.TimeoutExpired,OSError) as error:
   print('FAIL room UX mode '+mode+': '+str(error),flush=True);failures.append(mode)
 if failures:raise RuntimeError('Room UX fixture failures: '+', '.join(failures))

if __name__=='__main__':
 parser=argparse.ArgumentParser()
 parser.add_argument('output',type=Path)
 parser.add_argument('--compiler')
 parser.add_argument('--sdk-root',type=Path)
 args=parser.parse_args()
 output=args.output.resolve();generate(output)
 if args.compiler:compile_and_run(output,args.compiler,args.sdk_root)
