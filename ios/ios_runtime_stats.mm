#import <Foundation/Foundation.h>
#include <mach/mach.h>
#include <os/proc.h>
#include <sys/resource.h>
#include "timing/pc_ios_performance.h"

extern "C" void nectar_ios_runtime_sample(PcIosRuntimeSample* sample) {
    if (!sample) return;
    @autoreleasepool {
        *sample = PcIosRuntimeSample {};
        task_vm_info_data_t info {};
        mach_msg_type_number_t count = TASK_VM_INFO_COUNT;
        if (task_info(mach_task_self(), TASK_VM_INFO, reinterpret_cast<task_info_t>(&info), &count) == KERN_SUCCESS) {
            sample->footprintBytes = info.phys_footprint;
            sample->footprintValid = 1;
        }
        sample->availableBytes = os_proc_available_memory();
        sample->availableValid = 1; // Zero is meaningful; it is not an unavailable reading.
        struct rusage usage {};
        if (getrusage(RUSAGE_SELF, &usage) == 0) {
            sample->processCpuSeconds = usage.ru_utime.tv_sec + usage.ru_utime.tv_usec / 1000000.0
                                      + usage.ru_stime.tv_sec + usage.ru_stime.tv_usec / 1000000.0;
            sample->cpuValid = 1;
        }
        NSProcessInfo* process = NSProcessInfo.processInfo;
        sample->thermalState = static_cast<int>(process.thermalState);
        sample->lowPower = process.lowPowerModeEnabled ? 1 : 0;
    }
}
