#ifndef PC_FOLLOW_TRAIL_H
#define PC_FOLLOW_TRAIL_H

// Bounded recent grounded footsteps. No entity pointers, heap allocations,
// save data, teleports or path requests. Coordinates are world-space units.
struct PcFollowTrail {
    struct Point { float x=0,y=0,z=0; bool platform=false; };
    static constexpr int capacity=64;
    Point points[capacity];
    int count=0;
    void clear() { count=0; }
    void record(Point p) {
        if (count) {
            const Point& last=points[count-1];
            const float dx=p.x-last.x,dy=p.y-last.y,dz=p.z-last.z;
            if (dx*dx+dz*dz>96.0f*96.0f || dy>40.0f || dy< -40.0f) clear();
            else if (dx*dx+dy*dy+dz*dz<12.0f*12.0f) {
                // Keep a platform edge marker until the next spaced sample.
                points[count-1].platform = last.platform || p.platform;
                return;
            }
        }
        if (count==capacity) { for(int i=1;i<count;++i) points[i-1]=points[i]; --count; }
        points[count++]=p;
    }
    bool target(Point here, Point captain, bool onPlatform, Point& out) const {
        if (count<2) return false;
        int nearest=-1; float best=60.0f*60.0f;
        for(int i=0;i<count;++i) {
            const Point& p=points[i];
            const float dy=p.y-here.y,dx=p.x-here.x,dz=p.z-here.z;
            if(dy>24.0f || dy< -24.0f) continue; // never use a trail on another floor
            const float d=dx*dx+dz*dz;
            if(d<best) {best=d;nearest=i;}
        }
        if(nearest<0) return false;
        bool crossing=onPlatform;
        // Retain the narrow lane through the exit, not throughout the area.
        for(int i=nearest>3?nearest-3:0;i<count;++i) crossing=crossing||points[i].platform;
        if(!crossing) return false;
        out=points[nearest];
        const float dx=out.x-here.x,dz=out.z-here.z;
        if(dx*dx+dz*dz<18.0f*18.0f) out=nearest+1<count?points[nearest+1]:captain;
        // A sharp ramp edge / floor mismatch must be handled by a route.
        return out.y-here.y<=24.0f && out.y-here.y>=-24.0f;
    }
};

struct PcFollowerProgress {
    float x=0,y=0,z=0,elapsed=0,cooldown=0;
    bool seeded=false;
    void reset() {seeded=false;elapsed=0;cooldown=0;}
    bool stalled(float px,float py,float pz,float dt,bool needsMove) {
        if(dt<0)dt=0;
        if(dt>.1f)dt=.1f; // background/pause time is not failed movement
        if(cooldown>0)cooldown-=dt;
        if(!seeded || !needsMove) {x=px;y=py;z=pz;elapsed=0;seeded=true;return false;}
        float dx=px-x,dy=py-y,dz=pz-z;
        if(dx*dx+dy*dy+dz*dz>=8.0f*8.0f) {x=px;y=py;z=pz;elapsed=0;return false;}
        elapsed+=dt;
        return elapsed>=1.25f && cooldown<=0;
    }
    void attempted() {elapsed=0;cooldown=2.0f;seeded=false;}
};
#endif
