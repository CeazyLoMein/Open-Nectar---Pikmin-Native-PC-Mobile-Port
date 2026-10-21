#ifndef PC_FOLLOW_SURFACE_H
#define PC_FOLLOW_SURFACE_H
#include "Collision.h"
#include "MapCode.h"
#include "MapMgr.h"
#include <cmath>
inline bool pcFollowFloor(float x,float z,float reference,bool allowWater,float& y) {
    if(!mapMgr)return false;
    bool found=false;float best=1000000.0f;
    for(CollGroup* group=mapMgr->getCollGroupList(x,z,true);group;group=group->mNextCollGroup) {
        for(int i=0;i<group->mTriCount;++i){
            CollTriInfo* tri=group->mTriangleList[i];
            if(!tri || tri->mTriangle.mNormal.y<0.45f)continue;
            Vector3f p(x,reference,z);
            if(!tri->inTriClampTo(p) || p.y>reference+22.0f || p.y<reference-24.0f)continue;
            const int attr=MapCode::getAttribute(tri);
            if(attr==ATTR_Hole || (!allowWater&&attr==ATTR_Water))continue;
            const float delta=std::fabs(p.y-reference);
            if(delta<best){best=delta;y=p.y;found=true;}
        }
    }
    return found;
}
inline bool pcFollowWall(const Vector3f& a,const Vector3f& b) {
    if(!mapMgr)return true;
    Vector3f from=a,to=b;from.y+=7.0f;to.y+=7.0f;
    for(CollGroup* group=mapMgr->getCollGroupList(b.x,b.z,true);group;group=group->mNextCollGroup) {
        for(int i=0;i<group->mTriCount;++i){
            CollTriInfo* tri=group->mTriangleList[i];
            if(!tri || std::fabs(tri->mTriangle.mNormal.y)>0.45f)continue;
            const float da=tri->mTriangle.dist(from),db=tri->mTriangle.dist(to);
            if(da*db>0.0f || std::fabs(da-db)<0.001f)continue;
            const float t=da/(da-db);
            if(t<0.001f || t>1.0f)continue;
            const Vector3f hit=from+(to-from)*t;
            bool inside=true;for(int edge=0;edge<3;++edge)if(tri->mEdgePlanes[edge].dist(hit)<-2.0f)inside=false;
            if(inside)return true;
        }
    }
    return false;
}
inline bool pcFollowWalkLine(const Vector3f& a,const Vector3f& b,bool allowWater) {
    const Vector3f delta=b-a;
    const float distance=std::sqrt(delta.x*delta.x+delta.z*delta.z);
    if(distance>600.0f)return false;
    const int steps=distance>12.0f?int(std::ceil(distance/12.0f)):1;
    Vector3f previous=a;
    for(int i=1;i<=steps;++i){
        const float t=float(i)/steps;Vector3f p(a.x+delta.x*t,previous.y,a.z+delta.z*t);
        if(!pcFollowFloor(p.x,p.z,previous.y,allowWater,p.y)||pcFollowWall(previous,p))return false;
        previous=p;
    }
    return std::fabs(previous.y-b.y)<25.0f;
}
#endif
