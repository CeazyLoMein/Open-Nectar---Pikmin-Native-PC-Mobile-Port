#pragma once
#if NECTAR_P1_SOLO_TEST
#include <cstdio>
#include <mutex>
namespace pc_solo_test {
// No recorded content or private IDs. Bound the entire persistent journal.
// A card-write event is IO evidence, not proof of a complete reloadable save.
inline void record(const char* event, int a=0, int b=0, int c=0, int d=0) {
    static std::mutex mutex;
    const std::lock_guard<std::mutex> lock(mutex);
    FILE* f = std::fopen("p1-solo-test-events.txt", "ab");
    if (!f) return;
    if (std::fseek(f, 0, SEEK_END) == 0) {
        const long size = std::ftell(f);
        if (size >= 0 && size < 65536 - 256)
            std::fprintf(f, "%s %d %d %d %d\n", event, a, b, c, d);
    }
    std::fclose(f);
}
}
#endif
