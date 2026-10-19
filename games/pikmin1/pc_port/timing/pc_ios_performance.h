#ifndef PC_IOS_PERFORMANCE_H
#define PC_IOS_PERFORMANCE_H
#include <cstdint>

struct PcIosRuntimeSample {
    std::uint64_t footprintBytes = 0;
    std::uint64_t availableBytes = 0;
    double processCpuSeconds = 0.0;
    int footprintValid = 0;
    int availableValid = 0;
    int cpuValid = 0;
    int thermalState = -1; // NSProcessInfo: nominal=0, fair=1, serious=2, critical=3
    int lowPower = 0;
};

// Apple APIs are isolated from the game's force-included GameCube BOOL typedef.
extern "C" void nectar_ios_runtime_sample(PcIosRuntimeSample* sample);

// Main/game thread only. Disabled HUD performs no clock or native metric sampling.
void pc_ios_performance_present();
bool pc_ios_performance_lines(char lines[5][96]);
#endif
