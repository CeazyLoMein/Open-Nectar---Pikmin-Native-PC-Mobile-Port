#pragma once
// Practice ownership remains with its host-assigned captain even when a Pikmin
// is idle or working. Ordinary solo/local co-op keeps its existing behavior.
inline bool pc_practice_may_whistle(bool practice, int captain, int owner)
{
    return !practice || owner < 0 || owner == captain;
}
