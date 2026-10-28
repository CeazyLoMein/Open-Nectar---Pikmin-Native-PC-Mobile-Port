#include "nectar_net/onion_authority.h"
#include <limits>
#include <set>

namespace nectar::net {

OnionAuthority::OnionAuthority(std::uint16_t epoch, std::uint8_t colors,
                             const std::array<std::uint32_t, kColors>& stored,
                             const std::array<std::uint32_t, 2>& perPlayerLimit)
    : mEpoch(epoch), mColors(colors), mStored(stored), mLimits(perPlayerLimit)
{
    mValid = epoch != 0 && colors > 0 && colors <= kColors;
    for (const auto limit : mLimits) mValid = mValid && limit > 0 && limit <= kMaxPerPlayer;
    for (std::size_t c = colors; c < kColors; ++c) mValid = mValid && stored[c] == 0;
}

bool OnionAuthority::validId(std::uint64_t entity) const
{
    NetEntityId id;
    return NetEntityId::unpack(entity, id) && id.sceneEpoch == mEpoch && id.kind == EntityKind::Pikmin;
}

bool OnionAuthority::equal(const Command& a, const Command& b)
{
    return a.sceneEpoch == b.sceneEpoch && a.player == b.player && a.sequence == b.sequence
        && a.operation == b.operation && a.color == b.color && a.entities == b.entities;
}

OnionAuthority::Reply OnionAuthority::apply(std::uint8_t authenticatedPlayer, const Command& c)
{
    auto refused = [this](Status status) { return Reply{status, mRevision}; };
    if (!mValid || c.sceneEpoch != mEpoch) return refused(Status::InvalidSession);
    if (authenticatedPlayer >= 2 || c.player != authenticatedPlayer) return refused(Status::WrongPlayer);
    auto& last = mLast[authenticatedPlayer];
    if (last.valid && c.sequence == last.command.sequence) {
        if (!equal(c, last.command)) return refused(Status::ReusedSequence);
        Reply cached = last.reply;
        cached.replayed = true;
        return cached;
    }
    const auto previous = last.valid ? last.command.sequence : 0;
    if (c.sequence == 0 || c.sequence - 1 != previous) return refused(Status::OutOfOrder);
    // Bound before making a cached copy; malformed/oversized packets consume no memory or sequence.
    if (c.color >= mColors || c.entities.empty() || c.entities.size() > kMaxPerPlayer
        || (c.operation != Operation::Withdraw && c.operation != Operation::Store))
        return refused(Status::InvalidCommand);
    Status status = Status::Applied;
    std::set<std::uint64_t> unique;
    for (const auto id : c.entities) {
        if (!validId(id) || !unique.insert(id).second) { status = Status::InvalidEntity; break; }
        const auto it = mField.find(id);
        if (c.operation == Operation::Withdraw) {
            if (it != mField.end()) { status = Status::InvalidEntity; break; }
        } else if (it == mField.end() || it->second.player != c.player || it->second.color != c.color) {
            status = Status::InvalidEntity; break;
        }
    }
    const auto count = static_cast<std::uint32_t>(c.entities.size());
    if (status == Status::Applied && c.operation == Operation::Withdraw) {
        if (count > mStored[c.color]) status = Status::InsufficientStock;
        else if (count > mLimits[c.player] - mCounts[c.player]) status = Status::PlayerLimit;
    } else if (status == Status::Applied
               && count > std::numeric_limits<std::uint32_t>::max() - mStored[c.color]) {
        status = Status::InvalidCommand;
    }
    // Allocate/cache before changing balances. Failed semantic requests are also
    // remembered, so retrying after the world changes cannot change their result.
    LastRequest next;
    next.command = c;
    next.valid = true;
    if (status == Status::Applied) {
        if (c.operation == Operation::Withdraw) {
            // Stage allocation in a copy: allocation failure cannot leave a partial withdrawal.
            auto field = mField;
            for (const auto id : c.entities) field.emplace(id, FieldPikmin{c.player, c.color});
            mField.swap(field);
            mStored[c.color] -= count;
            mCounts[c.player] += count;
        } else {
            for (const auto id : c.entities) mField.erase(id);
            mStored[c.color] += count;
            mCounts[c.player] -= count;
        }
        ++mRevision;
    }
    next.reply = {status, mRevision};
    last = std::move(next);
    return last.reply;
}

bool OnionAuthority::retire(std::uint64_t entity)
{
    const auto it = mField.find(entity);
    if (!mValid || it == mField.end()) return false;
    --mCounts[it->second.player];
    mField.erase(it);
    ++mRevision;
    return true;
}

std::uint32_t OnionAuthority::stored(std::uint8_t color) const
{
    return color < mColors && color < kColors ? mStored[color] : 0;
}

std::uint32_t OnionAuthority::fieldCount(std::uint8_t player) const
{
    return player < 2 ? mCounts[player] : 0;
}

} // namespace nectar::net
