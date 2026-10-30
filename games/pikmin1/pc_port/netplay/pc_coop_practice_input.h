#pragma once
#include "nectar_net/input.h"
#include <algorithm>
#include <array>
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
        if (haveFrame && (tick < frameTick || now < frameAt)) return;
        if (!haveRateAnchor) { rateTick=tick;rateAt=now;haveRateAnchor=true; }
        // Measuring consecutive arrivals aliases a 20 Hz stream against a
        // 30/60/120 Hz client. Short bursts look impossibly fast and used to be
        // rejected, while slow gaps biased the learned host clock downward.
        if (now >= rateAt && now-rateAt >= 250) {
            if (tick>rateTick && now-rateAt<=1000) {
                const double measured=double(tick-rateTick)*1000.0/double(now-rateAt);
                if (measured>=15 && measured<=1000) { rate=haveRate?rate*.5+measured*.5:measured;haveRate=true; }
            }
            rateTick=tick;rateAt=now;
        }
        frameTick=tick;frameAt=now;haveFrame=true;
    }
    double rateHz() const { return rate; }
    std::uint64_t targetTick() const { return sentTick; }
    std::uint64_t frameAge(std::uint64_t now) const { return haveFrame && now>=frameAt?now-frameAt:0; }
    // Short transient actions cannot be replayed seconds after a network stall.
    // Continuous movement/held state always comes from the latest sample.
    static constexpr std::uint64_t TransientLifetimeMs = 300;
    void sample(const nectar::net::NetInputFrame& value, std::uint64_t now) {
        latest = value; sampleAt = now; haveSample = true;
        for (unsigned bit = 0; bit < 16; ++bit) {
            const auto mask = static_cast<std::uint16_t>(1u << bit);
            if ((taps & mask) && (now < tapAt[bit] || now - tapAt[bit] > TransientLifetimeMs)) taps &= ~mask;
            if (value.held & mask) { taps |= mask; tapAt[bit] = now; }
        }
        for (unsigned bit = 0; bit < 8; ++bit) {
            const auto mask = static_cast<std::uint8_t>(1u << bit);
            if ((edges & mask) && (now < edgeAt[bit] || now - edgeAt[bit] > TransientLifetimeMs)) edges &= ~mask;
            if ((value.flags & ~Continuous) & mask) { edges |= mask; edgeAt[bit] = now; }
        }
        if (haveRotation && (now < rotationAt || now - rotationAt > TransientLifetimeMs)) {
            rotation = 0; haveRotation = false;
        }
        if (value.cursorDx) {
            if (!haveRotation) { rotationAt = now; haveRotation = true; }
            rotation = std::clamp(rotation + int(value.cursorDx), -32767, 32767);
        }
    }
    std::vector<nectar::net::NetInputFrame> bundle(std::uint64_t now, int rtt) const {
        if (!haveFrame || !haveSample || now < sampleAt || now - sampleAt > TransientLifetimeMs ||
            now < frameAt || now - frameAt > 1000 ||
            (haveSent && (now < sentAt || now - sentAt < 33)) ||
            frameTick > std::numeric_limits<std::uint64_t>::max() - 64) return {};
        // A snapshot was already in flight before it reached this phone; an
        // input must also travel back. Estimate both halves of the RTT.
        const double delay = double(now - frameAt) + std::clamp(rtt, 0, 1000) + 50.0;
        std::uint64_t target = frameTick + std::min<std::uint64_t>(30, std::max<std::uint64_t>(2, static_cast<std::uint64_t>(std::ceil(delay * rate / 1000.0))));
        if (haveSent) target = std::max(target, sentTick + 1);
        if (target > frameTick + 30) return {};
        std::uint16_t freshTaps = 0;
        std::uint8_t freshEdges = 0;
        for (unsigned bit = 0; bit < 16; ++bit)
            if ((taps & (1u << bit)) && now >= tapAt[bit] && now - tapAt[bit] <= TransientLifetimeMs)
                freshTaps |= static_cast<std::uint16_t>(1u << bit);
        for (unsigned bit = 0; bit < 8; ++bit)
            if ((edges & (1u << bit)) && now >= edgeAt[bit] && now - edgeAt[bit] <= TransientLifetimeMs)
                freshEdges |= static_cast<std::uint8_t>(1u << bit);
        const bool freshRotation = haveRotation && now >= rotationAt && now - rotationAt <= TransientLifetimeMs;
        std::vector<nectar::net::NetInputFrame> frames;
        const auto count = std::min<std::uint64_t>(nectar::net::kMaxInputFrames, target + 1);
        frames.reserve(static_cast<std::size_t>(count));
        for (std::uint64_t n = 0; n < count; ++n) {
            auto value = latest; value.tick = target - n;
            const auto old = history.find(value.tick);
            if (old != history.end()) { frames.push_back(old->second); continue; }
            value.held |= freshTaps;
            value.pressed = value.released = 0;
            value.flags &= Continuous;
            value.cursorDx = 0;
            if (n == 0) {
                value.flags |= freshEdges;
                if (freshRotation) value.cursorDx = static_cast<std::int16_t>(rotation);
            }
            frames.push_back(value);
        }
        return frames;
    }
    void published(const std::vector<nectar::net::NetInputFrame>& frames, std::uint64_t now) {
        if (frames.empty()) return;
        sentAt = now; sentTick = frames.front().tick; haveSent = true;
        for (const auto& value : frames) history[value.tick] = value;
        while (history.size() > 12) history.erase(history.begin());
        taps = 0; edges = 0; rotation = 0; haveRotation = false;
    }
private:
    nectar::net::NetInputFrame latest;
    std::uint64_t frameTick = 0, frameAt = 0, sentAt = 0, sentTick = 0, rotationAt = 0, sampleAt = 0, rateTick=0, rateAt=0;
    double rate = 120;
    bool haveFrame = false, haveRate = false, haveSent = false, haveRotation = false, haveSample = false, haveRateAnchor=false;
    std::array<std::uint64_t, 16> tapAt{};
    std::array<std::uint64_t, 8> edgeAt{};
    std::uint16_t taps = 0;
    std::uint8_t edges = 0;
    int rotation = 0;
    std::map<std::uint64_t, nectar::net::NetInputFrame> history;
};
