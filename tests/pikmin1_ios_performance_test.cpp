#include "timing/pc_ios_performance.h"
#include "timing/pc_ios_performance_model.h"
#include "settings/pc_settings.h"
#include <cmath>
#include <cstdio>
#include <cstring>
#include <limits>
#include <stdexcept>

static int checks=0, enabledFlag=0, nativeCalls=0;
static PcIosRuntimeSample mock;
extern "C" int pc_settings_get_ios_performance_hud(void) {return enabledFlag;}
extern "C" void nectar_ios_runtime_sample(PcIosRuntimeSample* s) {++nativeCalls;*s=mock;}
static void check(bool ok,const char* why) {++checks;if(!ok)throw std::runtime_error(why);}
static bool near(double a,double b) {return std::fabs(a-b)<1e-6;}
int main() {
 try {
    PcIosFrameHistory frames;
    check(frames.summary().count==0,"Empty history");
    for(int i=0;i<=240;++i)frames.present(i/120.0);
    auto s=frames.summary();
    check(s.count==240 && near(s.fps,120.0),"Measured120FPS");
    check(near(s.meanMs,1000.0/120) && near(s.p99Ms,1000.0/120),"120FPSbudget8.33ms");
    frames.reset();for(int i=0;i<=60;++i)frames.present(i/60.0);
    check(near(frames.summary().fps,60.0),"Measured60notchosen120");
    frames.reset();frames.present(0);double t=0;
    for(int i=0;i<100;++i){t+=i<95?0.01:0.1;frames.present(t);}
    s=frames.summary();check(near(s.p95Ms,10) && near(s.p99Ms,100),"Tail latency exposes hitches");
    frames.present(t);check(frames.summary().count==100,"Duplicate timestamp ignored");
    frames.present(std::numeric_limits<double>::quiet_NaN());
    check(frames.summary().count==100,"NaN ignored");
    frames.present(t+6);check(frames.summary().count==0,"Background gap resets");
    frames.present(t+6+1.0/120);check(near(frames.summary().fps,120),"Resume sample independent");
    frames.present(-1);check(frames.summary().count==0,"Backward clock resets");
    frames.reset();for(int i=0;i<=1000;++i)frames.present(i/120.0);
    check(frames.summary().count==240 && near(frames.summary().fps,120),"History bounded after wrap");
    PcIosCpuMeter cpu;double percent=0;
    check(!cpu.update(0,10,&percent),"First CPU reading unavailable");
    check(cpu.update(1,11,&percent) && near(percent,100),"One core CPU100percent");
    check(cpu.update(2,13,&percent) && near(percent,200),"Two core CPU200percent");
    check(!cpu.update(3,1,&percent),"CPU counter reset guarded");
    check(!cpu.update(3,2,&percent),"Duplicate CPU wall time guarded");
    check(!cpu.update(4,std::numeric_limits<double>::infinity(),&percent),"Invalid CPU sample rejected");
    char lines[5][96] {};
    pc_ios_performance_present();
    check(!pc_ios_performance_lines(lines) && nativeCalls==0,"Off does no native sampling");
    enabledFlag=1;mock.footprintValid=1;mock.footprintBytes=512ULL*1024*1024;
    mock.availableValid=1;mock.availableBytes=0;mock.thermalState=2;mock.lowPower=1;
    check(pc_ios_performance_lines(lines) && nativeCalls==1,"On samples once");
    check(std::strstr(lines[2],"512") && std::strstr(lines[2],"spare 0"),"Zero available is real not N/A");
    check(std::strstr(lines[4],"Serious") && std::strstr(lines[4],"On"),"Thermal and LowPower reported");
    for(int i=0;i<50;++i)pc_ios_performance_present();
    pc_ios_performance_lines(lines);check(nativeCalls==1,"Native reads throttled between refreshes");
    enabledFlag=0;check(!pc_ios_performance_lines(lines),"Toggle off clears state");
    enabledFlag=1;mock.footprintValid=0;mock.availableValid=0;mock.thermalState=-1;
    pc_ios_performance_lines(lines);
    check(std::strstr(lines[2],"RAM N/A") && std::strstr(lines[2],"spare N/A"),"Unavailable data not fabricated");
    check(std::strstr(lines[4],"Unknown"),"Unknown thermal explicit");
    for(auto& line:lines)check(std::strlen(line)<sizeof(line),"Bounded HUD string");
    std::printf("PASS: %d iPhone performance history/CPU/format/disabled/throttle checks\n",checks);
    return 0;
 }catch(const std::exception& e){std::fprintf(stderr,"FAIL: %s\n",e.what());return 1;}
}
