"""Exercise the real layered floor/wall walkability helpers numerically."""
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
header=(root/'games/pikmin1/pc_port/pc_follow_surface.h').read_text(encoding='utf-8')
for include in ['#include "Collision.h"','#include "MapCode.h"','#include "MapMgr.h"']:header=header.replace(include,'')
cpp=r"""
#include <cmath>
#include <cstdio>
#include <vector>
struct Vector3f {float x=0,y=0,z=0;Vector3f()=default;Vector3f(float a,float b,float c):x(a),y(b),z(c){}
Vector3f operator+(Vector3f b)const{return {x+b.x,y+b.y,z+b.z};}Vector3f operator-(Vector3f b)const{return {x-b.x,y-b.y,z-b.z};}Vector3f operator*(float v)const{return {x*v,y*v,z*v};}};
struct Plane {Vector3f mNormal{0,1,0};float mOffset=0;float dist(const Vector3f&p)const{return p.x*mNormal.x+p.y*mNormal.y+p.z*mNormal.z-mOffset;}};
enum {ATTR_Solid,ATTR_Water=5,ATTR_Hole=6};
struct CollTriInfo {Plane mTriangle,mEdgePlanes[3];float minX=-1000,maxX=1000,minZ=-1000,maxZ=1000;int attr=ATTR_Solid;
bool inTriClampTo(Vector3f&p){p.y=(mTriangle.mOffset-p.x*mTriangle.mNormal.x-p.z*mTriangle.mNormal.z)/mTriangle.mNormal.y;return p.x>=minX&&p.x<=maxX&&p.z>=minZ&&p.z<=maxZ;}};
struct CollGroup {CollTriInfo**mTriangleList=nullptr;int mTriCount=0;CollGroup*mNextCollGroup=nullptr;};
struct Map {CollGroup group;std::vector<CollTriInfo*>triangles;int queries=0;CollGroup*getCollGroupList(float,float,bool){++queries;group.mTriangleList=triangles.data();group.mTriCount=int(triangles.size());return &group;}}map;Map*mapMgr=&map;
struct MapCode {static int getAttribute(CollTriInfo*t){return t->attr;}};
HEADER
int checks=0,failures=0;void check(bool c,const char*n){++checks;if(!c){++failures;std::printf("FAIL %s\n",n);}}
int main(){
CollTriInfo low,high;high.mTriangle.mOffset=80;
map.triangles={&low};check(pcFollowWalkLine({0,0,0},{100,0,0},false),"flat walkable surface");
map.triangles={&low,&high};check(pcFollowWalkLine({0,0,0},{100,0,0},false),"underpass uses actor floor rather than highest overhead platform");
check(pcFollowWalkLine({0,80,0},{100,80,0},false),"platform top uses its own layer");
check(!pcFollowWalkLine({0,0,0},{100,80,0},false),"cannot magically climb to overhead layer");
CollTriInfo left,right;left.maxX=45;right.minX=45;right.mTriangle.mOffset=100;map.triangles={&left,&right};
check(!pcFollowWalkLine({0,0,0},{100,100,0},false),"upward cliff blocks direct waypoint entry");
right.mTriangle.mOffset=-100;check(!pcFollowWalkLine({0,0,0},{100,-100,0},false),"downward cliff not accepted as walking shortcut");
CollTriInfo ramp;ramp.mTriangle.mNormal={-.2f,1,0};map.triangles={&ramp};
check(pcFollowWalkLine({0,0,0},{100,20,0},false),"continuous ramp between heights is walkable");
map.triangles={&low};low.attr=ATTR_Water;check(!pcFollowWalkLine({0,0,0},{100,0,0},false),"red/yellow reject watery entry");check(pcFollowWalkLine({0,0,0},{100,0,0},true),"blue may use water");
low.attr=ATTR_Hole;check(!pcFollowWalkLine({0,0,0},{100,0,0},true),"hole floor never walkable");low.attr=ATTR_Solid;
CollTriInfo wall;wall.mTriangle.mNormal={1,0,0};wall.mTriangle.mOffset=50;wall.mEdgePlanes[0]={{0,1,0},0};wall.mEdgePlanes[1]={{0,-1,0},-30};wall.mEdgePlanes[2]={{0,0,1},-20};map.triangles={&low,&wall};
check(!pcFollowWalkLine({0,0,0},{100,0,0},false),"vertical wall blocks same-height shortcut");
check(pcFollowWalkLine({0,40,0},{100,40,0},false)==false,"unsupported walk above wall is not invented");
map.triangles={&low};map.queries=0;check(pcFollowWalkLine({0,0,0},{600,0,0},false),"long reachable entry allowed beyond prior180-unit cutoff");check(map.queries<=100,"walk query cost bounded to50 steps");
check(!pcFollowWalkLine({0,0,0},{601,0,0},false),"entry range bounded");
map.triangles.clear();check(!pcFollowWalkLine({0,0,0},{10,0,0},false),"no ground rejects route");
mapMgr=nullptr;check(!pcFollowWalkLine({0,0,0},{10,0,0},false),"missing map safe failure");
std::printf("%d P1 layered-surface/wall route-entry scenarios; %d failures\n",checks,failures);return failures?1:0;
}
"""
Path(sys.argv[1]).write_text(cpp.replace('HEADER',header),encoding='utf-8');print('Generated real layered floor/wall route-entry fixture')
