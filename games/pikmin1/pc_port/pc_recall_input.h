#pragma once
#include <cstdint>

// One command per press. Menu/focus loss cancels it and an unconsumed press
// expires, so a paused world cannot receive an old command on resume.
struct PcRecallInput {
    bool down = false;
    bool pending = false;
    bool awaitRelease = false;
    std::uint64_t pressedAt = 0;
    void sample(bool held, bool allowed, std::uint64_t now) {
        if (!allowed || awaitRelease) pending = false;
        else if (held && !down) { pending = true; pressedAt = now; }
        if (!held) awaitRelease = false;
        down = held;
    }
    void cancel() { pending = false; awaitRelease = true; }
    bool take(std::uint64_t now) {
        const bool result = pending && now >= pressedAt && now - pressedAt <= 250;
        pending = false;
        return result;
    }
};
