#pragma once
struct Vector3f {float x=0,y=0,z=0;Vector3f()=default;Vector3f(float a,float b,float c):x(a),y(b),z(c){}};
struct SeSystem {float listenerX=0;void calcCameraPos(const Vector3f& p,Vector3f& v){v={p.x-listenerX,p.y,p.z};}};
extern SeSystem* seSystem;
