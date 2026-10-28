#include "nectar_net/practice_visual_blend.h"
#include <cmath>
#include <utility>
namespace nectar::net {
namespace {
bool finitePosition(const Vec3& v) { return std::isfinite(v.x)&&std::isfinite(v.y)&&std::isfinite(v.z); }
bool validFrame(const ActorFrame& f) {
    for(const auto& pair:f.captains) {
        const auto bytes=encodeCaptainState(pair.second);CaptainState checked;
        if(!decodeCaptainState(bytes.data(),bytes.size(),checked)) return false;
    }
    for(const auto& pair:f.pikmin) if(!validPikminState(pair.second)) return false;
    return true;
}
bool blendable(const Vec3& a,const Vec3& b,float maxDistance) {
    if(!finitePosition(a)||!finitePosition(b)) return false;
    const double dx=double(b.x)-a.x,dy=double(b.y)-a.y,dz=double(b.z)-a.z;
    return dx*dx+dy*dy+dz*dz<=double(maxDistance)*maxDistance;
}
Vec3 lerp(Vec3 a,Vec3 b,float t) {return {a.x+(b.x-a.x)*t,a.y+(b.y-a.y)*t,a.z+(b.z-a.z)*t};}
float turn(float a,float b,float t) {
    constexpr float tau=6.2831853071795864769f;
    return a+std::remainder(b-a,tau)*t;
}
}
bool blendPracticeVisualFrame(const ActorFrame& previous,const ActorFrame& next,
                              float fraction,float maxDistance,ActorFrame& output) {
    if(!previous.frame || next.frame<=previous.frame || next.tick<previous.tick ||
       !std::isfinite(fraction)||fraction<0||fraction>1 || !std::isfinite(maxDistance)||maxDistance<=0 ||
       previous.captains.size()>2 || next.captains.size()>2 || previous.pikmin.size()>510 || next.pikmin.size()>510 ||
       !validFrame(previous) || !validFrame(next)) return false;
    ActorFrame result=next;
    for(auto& pair:result.captains) {
        auto old=previous.captains.find(pair.first);auto& v=pair.second;
        if(old==previous.captains.end() || old->second.player!=v.player ||
           !std::isfinite(old->second.faceDirection)||!std::isfinite(v.faceDirection) ||
           !blendable(old->second.position,v.position,maxDistance)) continue;
        v.position=lerp(old->second.position,v.position,fraction);
        v.faceDirection=turn(old->second.faceDirection,v.faceDirection,fraction);
    }
    for(auto& pair:result.pikmin) {
        auto old=previous.pikmin.find(pair.first);auto& v=pair.second;
        if(old==previous.pikmin.end() || old->second.color!=v.color || old->second.action!=v.action ||
           !std::isfinite(old->second.faceDirection)||!std::isfinite(v.faceDirection) ||
           !blendable(old->second.position,v.position,maxDistance)) continue;
        v.position=lerp(old->second.position,v.position,fraction);
        v.faceDirection=turn(old->second.faceDirection,v.faceDirection,fraction);
    }
    output=std::move(result);return true;
}
}
