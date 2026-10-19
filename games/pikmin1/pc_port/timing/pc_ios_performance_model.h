#ifndef PC_IOS_PERFORMANCE_MODEL_H
#define PC_IOS_PERFORMANCE_MODEL_H
#include <algorithm>
#include <array>
#include <cmath>
#include <cstddef>

struct PcIosFrameSummary {
    std::size_t count = 0;
    double fps = 0.0, meanMs = 0.0, p95Ms = 0.0, p99Ms = 0.0;
};

class PcIosFrameHistory {
public:
    void reset() { count_ = next_ = 0; haveTime_ = false; }
    bool present(double seconds) {
        if (!std::isfinite(seconds)) return false;
        if (!haveTime_) { last_ = seconds; haveTime_ = true; return false; }
        const double elapsed = seconds - last_;
        if (elapsed == 0.0) return false;
        if (elapsed < 0.0) { reset(); last_ = seconds; haveTime_ = true; return true; }
        // A suspended app does not provide useful gameplay pacing samples.
        if (elapsed > 5.0) { reset(); last_ = seconds; haveTime_ = true; return true; }
        last_ = seconds;
        values_[next_] = elapsed * 1000.0;
        next_ = (next_ + 1) % values_.size();
        if (count_ < values_.size()) ++count_;
        return false;
    }
    PcIosFrameSummary summary() const {
        PcIosFrameSummary result;
        result.count = count_;
        if (!count_) return result;
        auto ordered = values_;
        double total = 0.0;
        for (std::size_t i = 0; i < count_; ++i) total += ordered[i];
        std::sort(ordered.begin(), ordered.begin() + count_);
        result.meanMs = total / static_cast<double>(count_);
        result.fps = 1000.0 / result.meanMs;
        const auto rank = [this](double p) {
            return static_cast<std::size_t>(std::ceil(p * static_cast<double>(count_))) - 1;
        };
        result.p95Ms = ordered[rank(0.95)];
        result.p99Ms = ordered[rank(0.99)];
        return result;
    }
private:
    std::array<double, 240> values_ {};
    std::size_t count_ = 0, next_ = 0;
    double last_ = 0.0;
    bool haveTime_ = false;
};

class PcIosCpuMeter {
public:
    void reset() { haveSample_ = false; }
    bool update(double wallSeconds, double cpuSeconds, double* percent) {
        if (!std::isfinite(wallSeconds) || !std::isfinite(cpuSeconds) || cpuSeconds < 0.0) {
            reset(); return false;
        }
        bool valid = haveSample_ && wallSeconds > wall_ && cpuSeconds >= cpu_;
        if (valid && percent) *percent = 100.0 * (cpuSeconds - cpu_) / (wallSeconds - wall_);
        wall_ = wallSeconds; cpu_ = cpuSeconds; haveSample_ = true;
        return valid;
    }
private:
    double wall_ = 0.0, cpu_ = 0.0;
    bool haveSample_ = false;
};
#endif
