#pragma once
#include "nectar_net/input.h"
#include <algorithm>
#include <cmath>
#include <limits>
#include <map>

// Guest input targets the host's measured simulation clock, never this phone's
// display FPS. Bounded six-tick bundles preserve taps between network sends.
class PcCoopPracticeInput {
public:
    static constexpr std::uint8_t Continuous = 8; // P1 Swarm, other ext bits are edges
    void reset() { *this = PcCoopPracticeInput{}; }
    void observe(std::uint64_t tick, std::uint64_t now) {
        if (haveFrame && tick > frameTick && now > frameAt && now - frameAt <= 500) {
            const double sample = double(tick - frameTick) * 1000.0 / double(now - frameAt);
            if (sample >= 15 && sample <= 240) {
                rate = haveRate ? rate * 0.75 + sample * 0.25 : sample;
                haveRate = true;
            }
        }
        if (!haveFrame || (tick >= frameTick && now >= frameAt)) {
            frameTick = tick; frameAt = now; haveFrame = true;
        }
    }
    void sample(const nectar::net::NetInputFrame& value) {
        latest = value;
        taps |= value.held;
        edges |= value.flags & ~Continuous;
        rotation = std::clamp(rotation + int(value.cursorDx), -32767, 32767);
    }
    std::vector<nectar::net::NetInputFrame> bundle(std::uint64_t now, int rtt) const {
        if (!haveFrame || now < frameAt || now - frameAt > 1000 ||
            (haveSent && (now < sentAt || now - sentAt < 33)) ||
            frameTick > std::numeric_limits<std::uint64_t>::max() - 64) return {};
        // A snapshot was already in flight before it reached this phone; an
        // input must also travel back. Estimate both halves of the RTT.
        const double delay = double(now - frameAt) + std::clamp(rtt, 0, 1000) + 16.0;
        std::uint64_t target = frameTick + std::min<std::uint64_t>(30, std::max<std::uint64_t>(2, static_cast<std::uint64_t>(std::ceil(delay * rate / 1000.0))));
        if (haveSent) target = std::max(target, sentTick + 1);
        if (target > frameTick + 30) return {};
        std::vector<nectar::net::NetInputFrame> frames;
        const auto count = std::min<std::uint64_t>(nectar::net::kMaxInputFrames, target + 1);
        frames.reserve(static_cast<std::size_t>(count));
        for (std::uint64_t n = 0; n < count; ++n) {
            auto value = latest; value.tick = target - n;
            const auto old = history.find(value.tick);
            if (old != history.end()) { frames.push_back(old->second); continue; }
            value.held |= taps; value.pressed = value.released = 0;
            value.flags &= Continuous;
            value.cursorDx = 0;
            if (n == 0) { value.flags |= edges; value.cursorDx = static_cast<std::int16_t>(rotation); }
            frames.push_back(value);
        }
        return frames;
    }
    void published(const std::vector<nectar::net::NetInputFrame>& frames, std::uint64_t now) {
        if (frames.empty()) return;
        sentAt = now; sentTick = frames.front().tick; haveSent = true;
        for (const auto& value : frames) history[value.tick] = value;
        while (history.size() > 12) history.erase(history.begin());
        taps = 0; edges = 0; rotation = 0;
    }
private:
    nectar::net::NetInputFrame latest;
    std::uint64_t frameTick = 0, frameAt = 0, sentAt = 0, sentTick = 0;
    double rate = 120;
    bool haveFrame = false, haveRate = false, haveSent = false;
    std::uint16_t taps = 0;
    std::uint8_t edges = 0;
    int rotation = 0;
    std::map<std::uint64_t, nectar::net::NetInputFrame> history;
};
