"""Generate offline fixtures for the actual P2 software DSP, without game assets."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def generate(output):
    output.mkdir(parents=True, exist_ok=True)
    (output / "jaudio").mkdir(exist_ok=True)
    header = (ROOT / "games/pikmin2/include/jaudio/dspinterface.h").read_text()
    start = header.index("struct DSPMixerChannel {")
    end = header.index("///////////////////////////////////////////////////////////////////////////////", start)
    (output / "jaudio/dspinterface.h").write_text(
        '#pragma once\n#include "types.h"\ntypedef u16 DSPBOOL;\n'
        '#define DSP_TRUE 1\n#define DSP_FALSE 0\n' + header[start:end])
    (output / "types.h").write_text(
        '#pragma once\n#include <cstdint>\n'
        'using s8=std::int8_t; using u8=std::uint8_t; '
        'using s16=std::int16_t; using u16=std::uint16_t; '
        'using s32=std::int32_t; using u32=std::uint32_t; '
        'using s64=std::int64_t; using u64=std::uint64_t;\n')
    (output / "test.cpp").write_text(TEST)
    (output / "audit-test.cpp").write_text(AUDIT_TEST)
    (output / "host.cpp").write_text("static thread_local bool host=false;\nbool pc_host_alloc_active(){return host;}\nvoid pc_host_alloc_set(bool v){host=v;}\n")
    print("Generated actual P2 DSP route regression")

TEST = r'''
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include "jaudio/dspinterface.h"
#include "audio/pc_dsp_host.h"
static thread_local bool host=false;
bool pc_host_alloc_active(){return host;}
void pc_host_alloc_set(bool v){host=v;}
static int failures=0,checks=0;
void check(bool ok,const char* name){++checks;if(!ok){++failures;std::printf("FAIL: %s\n",name);}}
DSPchannel_ channel(bool automatic,u8 pan,u8 rear,u8 fx){
 DSPchannel_ c{};c.enabled=1;c.useConstantSample=1;c.constantSample=12000;c.resamplingRatio=0x1000;
 c.useDolbyVolume=automatic;c.dolbyVoicePosition=static_cast<u16>((pan<<8)|rear);
 c.dolbyReverbFactor=static_cast<s16>((fx<<8)|(fx<<1));c.dolbyVolumeCurrent=0x4000;c.dolbyVolumeTarget=0x4000;
 return c;
}
int level(DSPchannel_ c,int side){s16 out[160]{};pc_dsp_host_render_frame(&c,1,out,80);int sum=0;for(int i=0;i<80;++i)sum+=std::abs(static_cast<int>(out[i*2+side]));return sum/80;}
int main(){pc_dsp_host_init();pc_dsp_host_set_pitch_unity(0x1000);pc_dsp_host_set_mixer_level(1);
 for(u8 pan: {u8(0),u8(64),u8(127)})for(u8 rear:{u8(0),u8(64),u8(127)}){
  auto dry=channel(true,pan,rear,0),wet=channel(true,pan,rear,127);
  int dl=level(dry,0),dr=level(dry,1),wl=level(wet,0),wr=level(wet,1);
  check(dl+dr>100,"direct voice survives at every camera quadrant with zero reverb");
  check(std::abs(dl-wl)<=1&&std::abs(dr-wr)<=1,"reverb send does not control direct positional gain");
  if(pan==0)check(dr==0&&dl>0,"hard left remains left");
  if(pan==127)check(dl==0&&dr>0,"hard right remains right");
 }
 auto rearLeft=channel(false,0,0,0);rearLeft.mixChannels[0]={0x0F40,0x4000,0x4000,0};
 check(level(rearLeft,0)>100&&level(rearLeft,1)==0,"rear-left bus 0x0F40 reaches stereo left");
 auto rearRight=channel(false,0,0,0);rearRight.mixChannels[0]={0x0CA0,0x4000,0x4000,0};
 check(level(rearRight,1)>100&&level(rearRight,0)==0,"rear-right bus 0x0CA0 reaches stereo right");
 auto mute=channel(true,64,127,0);mute.dolbyVolumeCurrent=0;mute.dolbyVolumeTarget=0;
 check(level(mute,0)==0&&level(mute,1)==0,"zero engine gain remains silent");
 auto far=channel(true,64,64,0),near=far;far.dolbyVolumeCurrent=far.dolbyVolumeTarget=0x0800;
 check(level(far,0)<level(near,0)/4,"lower engine distance gain stays quieter");
 pc_dsp_host_shutdown();std::printf("%d audio route checks; %d failures\n",checks,failures);return failures?1:0;}
'''

AUDIT_TEST = r'''
#include "audio/pc_p2_audio_audit.h"
#include <cstdio>
#include <fstream>
#include <iterator>
#include <string>
#include <thread>
#include <vector>
static thread_local bool host=false;
bool pc_host_alloc_active(){return host;}
void pc_host_alloc_set(bool v){host=v;}
static int checks=0,failures=0;
void check(bool ok,const char* message){++checks;if(!ok){++failures;std::printf("FAIL: %s\n",message);}}
std::string read(const char* name){std::ifstream f(name);return std::string(std::istreambuf_iterator<char>(f),{});}
int main(){
 using namespace p2_audio_audit;
 {std::ofstream previous("p2-audio-report.txt");previous<<"previous launch";}
 std::vector<std::thread> workers;
 for(int i=0;i<4;++i)workers.emplace_back([]{for(int j=0;j<1000;++j)event(0x2802,Event::CreatureRequest);});
 for(auto& t:workers)t.join();
 event(0x2802,Event::Submitted);event(0x2802,Event::Started);
 event(0x402d,Event::Submitted);distance(0x402d,0,0,0);
 event(0x3043,Event::Submitted);distance(0x3043,3000,0,1);
 bank(BankResult::MissingData);source(9);
 std::int16_t samples[160]{};samples[0]=1234;
 render(samples,80,3,0);
 check(read("p2-audio-report.txt")=="previous launch","no file writes before five seconds");
 render(samples,80,3,5000);
 const auto log=read("p2-audio-report.txt");
 check(log.find("request=4000")!=std::string::npos,"concurrent category requests preserved");
 check(log.find("wind-402d id=402d")!=std::string::npos,"wind tracked separately from other environment sounds");
 check(log.find("ship-3043 id=3043")!=std::string::npos,"ship tracked separately");
 check(log.find("last_dist=3000 last_gain_permil=0 listener=1")!=std::string::npos,"distance, volume and Louie listener recorded");
 check(log.find("source_frames: 9=1")!=std::string::npos,"DSP source formats recorded");
 check(log.find("output_peak=1234")!=std::string::npos,"output peak recorded without audio dump");
 check(read("p2-audio-previous.txt")=="previous launch","previous launch log retained");
 check(!host,"host allocation override restored");
 for(unsigned now=10000;now<=600000;now+=5000)render(samples,80,3,now);
 const auto final=read("p2-audio-report.txt");
 event(0x2802,Event::CreatureRequest);render(samples,80,3,605000);
 check(read("p2-audio-report.txt")==final,"report stops after ten minutes");
 check(final.size()<512*1024,"report bounded below 512 KiB");
 std::printf("%d audio audit checks; %d failures\n",checks,failures);return failures?1:0;
}
'''

if __name__ == "__main__":
    generate(Path(sys.argv[1]))
