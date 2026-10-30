#pragma once
#include "nectar_net/actor_frame.h"
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <deque>

// Presentation only, AFTER authenticated complete frames pass engine validation.
// Time is local monotonic milliseconds, independent of either player's FPS.
// Latest population/ownership stays authoritative; only common visual transforms
// and compatible animation poses are blended. Never advances guest simulation.
class PcCoopVisualSmoothing {
public:
    static constexpr std::uint64_t DelayMs = 75;
    void reset() { history.clear(); }
    bool push(const nectar::net::ActorFrame& frame, std::uint64_t now) {
        if (!frame.frame || (!history.empty() &&
            (frame.frame <= history.back().frame.frame || now < history.back().at))) return false;
        if (history.size() == 8) history.pop_front();
        history.push_back({frame, now});
        return true;
    }
    bool sample(std::uint64_t now, nectar::net::ActorFrame& out) const {
        if (history.empty()) return false;
        out = history.back().frame; // authoritative identity, health, ownership, population
        const auto target = now >= DelayMs ? now - DelayMs : 0;
        const Entry* left = &history.front();
        const Entry* right = left;
        for (const auto& entry : history) {
            right = &entry;
            if (entry.at >= target) break;
            left = &entry;
        }
        if (target >= history.back().at) left = right = &history.back();
        const float alpha = right->at > left->at
            ? std::clamp(float(target > left->at ? target-left->at : 0) / float(right->at-left->at),0.0f,1.0f) : 0;
        blend(out.captains, left->frame.captains, right->frame.captains, alpha);
        blend(out.pikmin, left->frame.pikmin, right->frame.pikmin, alpha);
        for(auto& entry:out.captains) {
            const auto a=left->frame.captains.find(entry.first),b=right->frame.captains.find(entry.first);
            if(a==left->frame.captains.end() || b==right->frame.captains.end())continue;
            const auto& x=a->second.cursor;const auto& y=b->second.cursor;
            const float dx=x.x-y.x,dy=x.y-y.y,dz=x.z-y.z;
            if(dx*dx+dy*dy+dz*dz<=400.0f*400.0f)entry.second.cursor=mix(x,y,alpha);
        }
        return true;
    }
private:
    struct Entry { nectar::net::ActorFrame frame; std::uint64_t at; };
    std::deque<Entry> history;
    static float mix(float a,float b,float t) { return a+(b-a)*t; }
    static nectar::net::Vec3 mix(const nectar::net::Vec3& a,const nectar::net::Vec3& b,float t) {
        return {mix(a.x,b.x,t),mix(a.y,b.y,t),mix(a.z,b.z,t)};
    }
    template<class Map>
    static void blend(Map& shown,const Map& old,const Map& next,float t) {
        for (auto& entry : shown) {
            auto a=old.find(entry.first),b=next.find(entry.first);
            if (a==old.end() || b==next.end()) continue; // birth/replacement never borrows another pose
            const auto& x=a->second;const auto& y=b->second;auto& result=entry.second;
            const float dx=x.position.x-y.position.x,dy=x.position.y-y.position.y,dz=x.position.z-y.position.z;
            const float lx=result.position.x-y.position.x,ly=result.position.y-y.position.y,lz=result.position.z-y.position.z;
            if (dx*dx+dy*dy+dz*dz > 400.0f*400.0f || lx*lx+ly*ly+lz*lz > 400.0f*400.0f) continue; // teleport/rescue: snap to current truth
            result.position=mix(x.position,y.position,t);
            result.velocity=mix(x.velocity,y.velocity,t);
            constexpr float circle=6.28318530718f;
            result.faceDirection=std::remainder(x.faceDirection+std::remainder(y.faceDirection-x.faceDirection,circle)*t,circle);
            // No interpolating across clip changes/loops: those require engine
            // asset lengths, and rolling an animation backward creates artifacts.
            if (result.upperAnimation==x.upperAnimation && result.upperAnimation==y.upperAnimation && y.upperFrame>=x.upperFrame)
                result.upperFrame=mix(x.upperFrame,y.upperFrame,t);
            if (result.lowerAnimation==x.lowerAnimation && result.lowerAnimation==y.lowerAnimation && y.lowerFrame>=x.lowerFrame)
                result.lowerFrame=mix(x.lowerFrame,y.lowerFrame,t);
        }
    }
};
