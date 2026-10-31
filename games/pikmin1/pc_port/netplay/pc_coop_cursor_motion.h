#pragma once
#include <algorithm>
#include <cmath>
#include <cstdint>

// One projection for solo and online: use the actual control camera's axes,
// including its handedness. SDL/touch deltas are distances, not velocities.
namespace pc_coop_cursor {
struct Motion { float x=0,y=0,z=0; };
constexpr float WireScale=16.0f;
inline Motion project(float dx,float dy,const Motion& right,const Motion& back) {
    const float r=std::hypot(right.x,right.z),b=std::hypot(back.x,back.z);
    if (!std::isfinite(dx)||!std::isfinite(dy)||!std::isfinite(r)||!std::isfinite(b)) return {};
    const float rx=r>.0001f?right.x/r:0,rz=r>.0001f?right.z/r:0;
    const float bx=b>.0001f?back.x/b:0,bz=b>.0001f?back.z/b:0;
    return {(rx*dx-bx*dy)*.5f,0,(rz*dx-bz*dy)*.5f};
}
inline std::int16_t encode(float value) {
    return std::isfinite(value)?static_cast<std::int16_t>(std::lround(std::clamp(value*WireScale,-32767.0f,32767.0f))):0;
}
inline Motion decode(std::int16_t x,std::int16_t z) { return {x/WireScale,0,z/WireScale}; }
inline bool localMouse(bool deterministic,bool remote,int captain,int keyboardOwner) {
    return !deterministic && !remote && captain==keyboardOwner;
}
}
