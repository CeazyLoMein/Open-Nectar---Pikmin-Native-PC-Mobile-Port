#pragma once
#include "netplay/pc_coop_cursor_motion.h"
#include "nectar_net/input.h"
#include "nectar_net/replication.h"
#include <deque>

// Only the local aim marker is predicted. The host still owns all throws,
// whistles, actors and collision. A complete actor tick acknowledges deltas.
class PcCoopCursorPreview {
public:
    void reset() { pending.clear();held=haveActivity=false;lastActivity=0; }
    void activity(bool aimHeld,bool moved,std::uint64_t now) {
        if (haveActivity && now<lastActivity) reset();
        held=aimHeld;
        if (held || moved) {lastActivity=now;haveActivity=true;}
    }
    void published(const nectar::net::NetInputFrame& input,std::uint64_t now) {
        if (!(input.flags&32) || (!input.cursorDx&&!input.cursorDy)) return;
        if (!pending.empty() && input.tick<=pending.back().tick) return;
        if (pending.size()==32) pending.pop_front();
        pending.push_back({input.tick,now,pc_coop_cursor::decode(input.cursorDx,input.cursorDy)});
    }
    bool sample(const nectar::net::CaptainState& authoritative,std::uint64_t ackTick,
                const pc_coop_cursor::Motion& unsent,float radius,std::uint64_t now,nectar::net::Vec3& out) {
        while (!pending.empty() && (pending.front().tick<=ackTick || now<pending.front().at || now-pending.front().at>300)) pending.pop_front();
        if (!haveActivity || now<lastActivity || (!held && pending.empty() && now-lastActivity>150)) return false;
        if (!std::isfinite(radius)||radius<=0||radius>10000) return false;
        auto wanted=authoritative.cursor;
        wanted.x+=unsent.x;wanted.z+=unsent.z;
        for(const auto& entry:pending){wanted.x+=entry.delta.x;wanted.z+=entry.delta.z;}
        if (!std::isfinite(wanted.x)||!std::isfinite(wanted.y)||!std::isfinite(wanted.z)) return false;
        const float dx=wanted.x-authoritative.position.x,dz=wanted.z-authoritative.position.z;
        const float distance=std::hypot(dx,dz);
        if(distance>radius){wanted.x=authoritative.position.x+dx/distance*radius;wanted.z=authoritative.position.z+dz/distance*radius;}
        out=wanted;return true;
    }
private:
    struct Pending{std::uint64_t tick,at;pc_coop_cursor::Motion delta;};
    std::deque<Pending> pending;
    bool held=false,haveActivity=false;
    std::uint64_t lastActivity=0;
};
