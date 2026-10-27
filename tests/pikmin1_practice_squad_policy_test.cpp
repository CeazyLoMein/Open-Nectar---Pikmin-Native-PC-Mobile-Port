#include "netplay/pc_practice_squad_policy.h"
#include <cstdio>
int main()
{
    for (int captain=0;captain<2;++captain) {
        if (!pc_practice_may_whistle(true,captain,captain)) return 1;
        if (pc_practice_may_whistle(true,captain,1-captain)) return 2;
        if (!pc_practice_may_whistle(true,captain,-1)) return 3;
        if (!pc_practice_may_whistle(false,captain,1-captain)) return 4;
    }
    std::puts("PASS practice squad ownership; ordinary solo/local co-op unchanged");
    return 0;
}
