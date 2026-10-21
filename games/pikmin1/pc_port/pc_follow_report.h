#ifndef PC_FOLLOW_REPORT_H
#define PC_FOLLOW_REPORT_H
#include <cstdio>
#include <cstring>
// Small on-device evidence log: first four events/reason, at most128 lines/run.
// Game coordinates only; no account, device ID or proprietary assets.
inline void pc_follow_note(const char* reason,float x,float y,float z,float gx,float gy,float gz,int detail=0) {
    struct Count {const char* reason=nullptr;int count=0;};
    static Count counts[32];static int lines=0;static FILE* file=nullptr;
    if(lines>=128)return;
    int slot=0;for(;slot<32;++slot)if(!counts[slot].reason||!std::strcmp(counts[slot].reason,reason))break;
    if(slot==32||counts[slot].count>=4)return;
    counts[slot].reason=reason;++counts[slot].count;
    if(!file){file=std::fopen("p1-navigation-report.txt","w");if(file)std::fputs("P1 navigation v2; bounded per-run report\n",file);}
    if(file){std::fprintf(file,"%s from=%.1f,%.1f,%.1f goal=%.1f,%.1f,%.1f detail=%d\n",reason,x,y,z,gx,gy,gz,detail);std::fflush(file);++lines;}
}
#endif
