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
struct EdgeTurn { Motion delta; float drag=0; };
// Solo Free Camera turns when mouse aim pushes past the radial limit. Guest
// actors do not run Navi::makeVelocity, so route that presentation intent here.
// Send the matching clamped+rotated cursor displacement through existing input;
// never mutate guest actors or let a local camera change host authority.
inline EdgeTurn edgeTurn(const Motion& offset,const Motion& delta,const Motion& right,float radius) {
    EdgeTurn out{delta,0};
    const float length=std::hypot(right.x,right.z);
    if(!std::isfinite(radius)||radius<=0||!std::isfinite(length)||length<.0001f)return out;
    const float x=offset.x+delta.x,z=offset.z+delta.z,distance=std::hypot(x,z);
    if(!std::isfinite(x)||!std::isfinite(z)||!std::isfinite(distance)||distance<=radius)return out;
    const float bx=x*radius/distance,bz=z*radius/distance;
    const float lateral=((x-bx)*right.x+(z-bz)*right.z)/length;
    out.drag=std::clamp(-(lateral/radius)/3.2f,-1.0f,1.0f);
    if(!out.drag)return out;
    const float angle=out.drag*3.2f,c=std::cos(angle),sn=std::sin(angle);
    out.delta={bx*c+bz*sn-offset.x,delta.y,bz*c-bx*sn-offset.z};
    return out;
}
inline std::int16_t encode(float value) {
    return std::isfinite(value)?static_cast<std::int16_t>(std::lround(std::clamp(value*WireScale,-32767.0f,32767.0f))):0;
}
inline Motion decode(std::int16_t x,std::int16_t z) { return {x/WireScale,0,z/WireScale}; }
inline bool localMouse(bool deterministic,bool remote,int captain,int keyboardOwner) {
    return !deterministic && !remote && captain==keyboardOwner;
}
}
