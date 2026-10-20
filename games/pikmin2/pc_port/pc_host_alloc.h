#pragma once

// The global C++ allocator follows a JKR heap only on game-owned threads.
// Native SDL/Apple worker threads default to the process heap instead.
bool pc_host_alloc_active();
void pc_host_alloc_set(bool active);
bool pc_game_alloc_active();
void pc_game_alloc_set(bool active);

struct PcNativeHostAllocScope {
    bool previous = pc_host_alloc_active();
    PcNativeHostAllocScope() { pc_host_alloc_set(true); }
    ~PcNativeHostAllocScope() { pc_host_alloc_set(previous); }
    PcNativeHostAllocScope(const PcNativeHostAllocScope&) = delete;
    PcNativeHostAllocScope& operator=(const PcNativeHostAllocScope&) = delete;
};

struct PcNativeGameAllocScope {
    bool previous = pc_game_alloc_active();
    PcNativeGameAllocScope() { pc_game_alloc_set(true); }
    ~PcNativeGameAllocScope() { pc_game_alloc_set(previous); }
    PcNativeGameAllocScope(const PcNativeGameAllocScope&) = delete;
    PcNativeGameAllocScope& operator=(const PcNativeGameAllocScope&) = delete;
};
