#include "pc_ios_performance.h"
#include "pc_ios_performance_model.h"
#include "settings/pc_settings.h"
#include <chrono>
#include <cstdio>
#include <cstring>

namespace {
PcIosFrameHistory sFrames;
PcIosCpuMeter sCpu;
bool sWasEnabled = false, sHaveRefresh = false;
double sRefreshTime = 0.0;
char sLines[5][96] = {};
double nowSeconds() {
    return std::chrono::duration<double>(std::chrono::steady_clock::now().time_since_epoch()).count();
}
bool enabled() {
    if (!pc_settings_get_ios_performance_hud()) {
        if (sWasEnabled) {
            sFrames.reset(); sCpu.reset(); sHaveRefresh = false; sWasEnabled = false;
        }
        return false;
    }
    sWasEnabled = true;
    return true;
}
}

void pc_ios_performance_present() {
    if (enabled() && sFrames.present(nowSeconds())) {
        sCpu.reset(); sHaveRefresh = false;
    }
}

bool pc_ios_performance_lines(char lines[5][96]) {
    if (!enabled()) return false;
    const double now = nowSeconds();
    if (!sHaveRefresh || now - sRefreshTime >= 1.0) {
        sHaveRefresh = true;
        sRefreshTime = now;
        const auto frames = sFrames.summary();
        if (frames.count) {
            std::snprintf(sLines[0], sizeof(sLines[0]), "Render %.1f FPS | average %.2f ms", frames.fps, frames.meanMs);
            std::snprintf(sLines[1], sizeof(sLines[1]), "Frame p95 %.2f | p99 %.2f ms", frames.p95Ms, frames.p99Ms);
        } else {
            std::snprintf(sLines[0], sizeof(sLines[0]), "Render FPS: collecting samples");
            std::snprintf(sLines[1], sizeof(sLines[1]), "Frame time: collecting samples");
        }
        PcIosRuntimeSample sample {};
        nectar_ios_runtime_sample(&sample);
        char used[24] = "N/A", available[24] = "N/A";
        constexpr double mib = 1024.0 * 1024.0;
        if (sample.footprintValid) std::snprintf(used, sizeof(used), "%.0f", sample.footprintBytes / mib);
        if (sample.availableValid) std::snprintf(available, sizeof(available), "%.0f", sample.availableBytes / mib);
        std::snprintf(sLines[2], sizeof(sLines[2]), "App RAM %s MiB | spare %s MiB*", used, available);
        double cpuPercent = 0.0;
        if (sample.cpuValid && sCpu.update(now, sample.processCpuSeconds, &cpuPercent))
            std::snprintf(sLines[3], sizeof(sLines[3]), "App CPU %.0f%% (1 core = 100%%)", cpuPercent);
        else {
            if (!sample.cpuValid) sCpu.reset();
            std::snprintf(sLines[3], sizeof(sLines[3]), "App CPU: collecting / unavailable");
        }
        static const char* const states[] = { "Nominal", "Fair", "Serious", "Critical" };
        const char* thermal = sample.thermalState >= 0 && sample.thermalState <= 3 ? states[sample.thermalState] : "Unknown";
        std::snprintf(sLines[4], sizeof(sLines[4]), "Heat %s | Low Power %s", thermal, sample.lowPower ? "On" : "Off");
    }
    std::memcpy(lines, sLines, sizeof(sLines));
    return true;
}
