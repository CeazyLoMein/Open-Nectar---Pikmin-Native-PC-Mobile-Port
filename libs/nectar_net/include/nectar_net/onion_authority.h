#pragma once

#include "nectar_net/world.h"
#include <array>
#include <cstdint>
#include <map>
#include <vector>

namespace nectar::net {

// Host-thread-only campaign accounting. The engine adapter must preflight the
// corresponding spawn/store operation and commit both at the same safe tick.
// Working/idle Pikmin retain their owner and count toward that player's limit.
// This component does not simulate Pikmin, move actors, or write campaign saves.
class OnionAuthority {
public:
    static constexpr std::size_t kColors = 5; // P1 uses 3, P2 can use 5.
    static constexpr std::uint32_t kMaxPerPlayer = 1000;
    enum class Operation : std::uint8_t { Withdraw = 1, Store = 2 };
    enum class Status : std::uint8_t {
        Applied, InvalidSession, WrongPlayer, OutOfOrder, ReusedSequence,
        InvalidCommand, InsufficientStock, PlayerLimit, InvalidEntity
    };
    struct Command {
        std::uint16_t sceneEpoch = 0;
        std::uint8_t player = 0;
        std::uint64_t sequence = 0; // contiguous per authenticated player, starts at 1
        Operation operation = Operation::Withdraw;
        std::uint8_t color = 0;
        // Host-assigned entity IDs, never trusted just because a guest sent them.
        // The engine adapter must resolve IDs against its authoritative registry.
        std::vector<std::uint64_t> entities;
    };
    struct Reply {
        Status status = Status::InvalidCommand;
        std::uint64_t revision = 0;
        // A cached acknowledgement must NEVER execute engine side effects again.
        bool replayed = false;
    };
    struct FieldPikmin { std::uint8_t player = 0, color = 0; };

    OnionAuthority(std::uint16_t epoch, std::uint8_t colors,
                   const std::array<std::uint32_t, kColors>& stored,
                   const std::array<std::uint32_t, 2>& perPlayerLimit);
    bool valid() const { return mValid; }
    // Session/peer authentication happens in the transport; never take the
    // authenticatedPlayer argument from the packet's untrusted player field.
    Reply apply(std::uint8_t authenticatedPlayer, const Command& command);
    // Engine-only death notification: releases allowance without adding to Onion.
    bool retire(std::uint64_t entity);
    std::uint32_t stored(std::uint8_t color) const;
    std::uint32_t fieldCount(std::uint8_t player) const;
    const std::map<std::uint64_t, FieldPikmin>& field() const { return mField; }
    std::uint64_t revision() const { return mRevision; }
private:
    struct LastRequest { Command command; Reply reply; bool valid = false; };
    bool validId(std::uint64_t entity) const;
    static bool equal(const Command& a, const Command& b);
    bool mValid = false;
    std::uint16_t mEpoch;
    std::uint8_t mColors;
    std::array<std::uint32_t, kColors> mStored;
    std::array<std::uint32_t, 2> mLimits, mCounts{};
    std::array<LastRequest, 2> mLast{};
    std::map<std::uint64_t, FieldPikmin> mField;
    std::uint64_t mRevision = 0;
};

} // namespace nectar::net
