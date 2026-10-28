#include "netplay/pc_coop_practice_status.h"
#include <cstdio>
#include <cstring>
using namespace nectar::net;
int main() {
    int fail=0;CoopView v;
    auto check=[&](const char* part,int local){if(!std::strstr(pc_practice_wait_message(v,local),part)){std::printf("FAIL %s\n",part);++fail;}};
    check("Tap Ready",0);v.ready[0]=true;check("Waiting for your partner",0);
    v.blockers[1]=static_cast<unsigned char>(CoopBlock::Background);check("partner left",0);
    v.blockers[1]=static_cast<unsigned char>(CoopBlock::Settings);check("partner is in settings",0);
    v.blockers[1]=0;v.blockers[0]=static_cast<unsigned char>(CoopBlock::Settings);check("Close your settings",0);
    v.blockers[0]=static_cast<unsigned char>(CoopBlock::Manual);check("Tap Ready",0);
    v.blockers[0]=0;v.ready[1]=true;v.blockers[0]=static_cast<unsigned char>(CoopBlock::Background);check("partner left",1);
    if(!fail)std::puts("PASS practice status distinguishes partner, local readiness and blockers");return fail?1:0;
}
