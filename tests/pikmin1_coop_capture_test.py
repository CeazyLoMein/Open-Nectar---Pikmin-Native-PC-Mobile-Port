# Actual P1 capture translation unit with controlled engine dependencies.
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
common=r'''
#pragma once
#include <vector>
#include <cstddef>
#include <cstdint>
struct Vec{float x=0,y=0,z=0;};
struct Creature{virtual ~Creature()=default;struct{Vec t;}mSRT;Vec mVelocity;
 float mFaceDirection=0,mHealth=100;bool alive=true,canRemove=true;
 virtual bool isAlive(){return alive;}bool removable(){return canRemove;}};
struct Navi:Creature{int mNaviID=0;};
struct Piki:Creature{Navi*mNavi=nullptr;std::uint16_t mColor=0,mMode=0;int mHappa=0;};
struct ObjectMgr{std::vector<Creature*>objects;};
struct MonoObjectMgr:ObjectMgr{int mNumObjects=0,mMaxElements=1;Creature*mObjectList[4]={};int mEntryStatus[4]={-1,-1,-1,-1};
 int getEmptyIndex(){for(int i=0;i<mMaxElements;++i)if(mEntryStatus[i]==-1)return i;return -1;}
 int getIndex(Creature*p){for(int i=0;i<mMaxElements;++i)if(mObjectList[i]==p)return i;return -1;}
 Creature*birth();void kill(Creature*);};
struct NaviMgr:MonoObjectMgr{};struct PikiMgr:MonoObjectMgr{};
extern NaviMgr*naviMgr;extern PikiMgr*pikiMgr;
struct Iterator{ObjectMgr*m;std::size_t i=0;explicit Iterator(ObjectMgr*p):m(p){}Creature*operator*(){return m->objects[i];}};
#define CI_LOOP(it) for((it).i=0;(it).i<(it).m->objects.size();++(it).i)
#define PRINT(...) do{}while(false)
'''
(out/'engine_fixture.h').write_text(common,encoding='utf-8')
for name in ['Navi.h','NaviMgr.h','Piki.h','PikiMgr.h']:(out/name).write_text('#include "engine_fixture.h"\n',encoding='utf-8')
def method(text,signature):
 a=text.index(signature);b=text.index('{',a);i=b+1;depth=1
 while depth:
  depth+=(text[i]=='{')-(text[i]=='}');i+=1
 return text[a:i]
obj=(ROOT/'games/pikmin1/src/plugPikiKando/objectMgr.cpp').read_text(encoding='utf-8')
creature=(ROOT/'games/pikmin1/src/plugPikiKando/creature.cpp').read_text(encoding='utf-8')
stage=(ROOT/'games/pikmin1/src/plugPikiKando/gameCoreSection.cpp').read_text(encoding='utf-8')
init=method(creature,'void Creature::init()');exit=method(stage,'void GameCoreSection::exitStage()')
assert init.index('pc_coop_world_forget(this)')<init.index('mSearchBuffer.invalidate')
assert exit.index('pc_coop_world_end_scene()')<exit.index('naviMgr      = nullptr')<exit.index('memStat->reset()')
assert 'NECTAR_COOP_WORLD=1' in (ROOT/'games/pikmin1/CMakeLists.txt').read_text(encoding='utf-8')
test=r'''
#include "engine_fixture.h"
#include "netplay/pc_coop_world.h"
#include "nectar_net/pikmin_replication.h"
#include <cstdio>
#include <limits>
NaviMgr*naviMgr=nullptr;PikiMgr*pikiMgr=nullptr;
int bad=0;void check(bool ok,const char*why){if(!ok){std::printf("FAIL %s\n",why);++bad;}}
'''
test+=method(obj,'Creature* MonoObjectMgr::birth()')+'\n'+method(obj,'void MonoObjectMgr::kill(')+'\n'
test+=r'''
using namespace nectar::net;
PikminState read(const std::vector<EntityRecord>&r,std::uint64_t id){PikminState s;bool found=false;
 for(const auto&v:r)if(v.id==id)found=decodePikminState(v.data.data(),v.data.size(),s);
 check(found,"valid Pikmin record for actor");return s;}
int main(){
 std::vector<EntityRecord> records;
 check(!pc_coop_world_active()&&!pc_coop_world_begin_host(100,1)&&!pc_coop_world_capture(records),"normal/incomplete world stays inactive");
 pc_coop_world_forget(nullptr);pc_coop_world_end_scene();
 NaviMgr navis;PikiMgr pikis;Navi n0,n1;n1.mNaviID=1;Piki p0,p1;p0.mNavi=&n0;p1.mNavi=&n1;p1.mColor=2;p0.mSRT.t.x=40;
 naviMgr=&navis;pikiMgr=&pikis;navis.objects={&n0,&n1};pikis.objects={&p0,&p1};
 check(!pc_coop_world_begin_host(0,1)&&!pc_coop_world_begin_host(100,0),"invalid session/epoch refused");
 check(pc_coop_world_begin_host(100,1)&&!pc_coop_world_begin_host(100,1),"explicit host begin once");
 check(pc_coop_world_capture(records)&&records.size()==4,"two captains and two Pikmin captured");

 std::vector<std::vector<std::uint8_t>> packets;
 check(pc_coop_world_capture_packets(1,50,100,packets)&&packets.size()>1,"actual engine capture produces bounded owned multipart packets");
 ActorFrameReceiver guest;check(guest.begin(100,1),"guest accepted matching session scene");
 for(auto it=packets.rbegin();it!=packets.rend();++it){
  const auto result=guest.receive(it->data(),it->size(),0);
  if(it+1!=packets.rend())check(result==ActorFrameReceiver::Result::Buffered&&!guest.hasFrame(),"actual engine squad invisible until all packets arrive");
 }
 check(guest.current().captains.size()==2&&guest.current().pikmin.size()==2,"actual engine capture reaches guest replica intact");
 const auto beforePackets=packets;
 check(!pc_coop_world_capture_packets(1,51,100,packets)&&packets==beforePackets,"capture packet sequence cannot repeat");
 check(!pc_coop_world_capture_packets(2,49,100,packets)&&packets==beforePackets,"capture tick cannot rewind");
 check(!pc_coop_world_capture_packets(2,51,48,packets)&&packets==beforePackets,"packetization failure never emits partial engine capture");
 check(pc_coop_world_capture_packets(2,51,100,packets),"failed packetization doesn't consume frame sequence");

 const auto original=pc_coop_world_actor_id(&p0,EntityKind::Pikmin);
 check(original&&!pc_coop_world_actor_id(&p0,EntityKind::Enemy),"actual actors have typed IDs");
 auto s=read(records,original);check(s.position.x==40&&s.owner==0&&s.leader==0,"capture actual transform and association");
 p0.mNavi=nullptr;p0.mMode=9;
 check(pc_coop_world_capture(records),"worker capture");s=read(records,original);
 check(s.owner==0&&s.leader==255&&s.action==9,"worker retains ownership despite absent leader");
 check(pc_coop_world_set_owner(original,1)&&pc_coop_world_capture(records),"explicit host reassignment");
 p0.mMode=0;p0.mNavi=&n0;check(pc_coop_world_capture(records),"idle capture");
 check(read(records,original).owner==1,"idle/leader change cannot silently steal ownership");
 check(!pc_coop_world_set_owner(original,2)&&!pc_coop_world_set_owner(pc_coop_world_actor_id(&n0,EntityKind::Captain),1),"invalid owner/kind refused");
 MonoObjectMgr pool;pool.mObjectList[0]=&p0;pool.mEntryStatus[0]=0;pool.mNumObjects=1;
 pool.kill(&p0);check(!pc_coop_world_actor_id(&p0,EntityKind::Pikmin),"actual pool kill invalidates identity");
 check(pool.birth()==&p0&&pc_coop_world_capture(records),"actual pool birth reuses local address");
 const auto replacement=pc_coop_world_actor_id(&p0,EntityKind::Pikmin);
 check(replacement&&replacement!=original&&!pc_coop_world_set_owner(original,1),"stale command cannot target replacement Pikmin");
 const auto oldRecords=records;const auto oldPosition=p0.mSRT.t.x;
 p0.mSRT.t.x=std::numeric_limits<float>::quiet_NaN();
 check(!pc_coop_world_capture(records)&&records.size()==oldRecords.size()&&records[0].data==oldRecords[0].data,"invalid transform never publishes partial world");
 p0.mSRT.t.x=oldPosition;p0.mHappa=-1;check(!pc_coop_world_capture(records),"invalid maturity refused");p0.mHappa=0;
 p0.mColor=4;check(!pc_coop_world_capture(records),"P1 rejects P2-only colors");p0.mColor=0;
 p0.alive=false;check(pc_coop_world_capture(records)&&records.size()==3&&!pc_coop_world_actor_id(&p0,EntityKind::Pikmin),"dead actor removed from complete record list");p0.alive=true;
 navis.objects={&n0,&n0};check(!pc_coop_world_capture(records),"duplicate captain refused");navis.objects={&n0,&n1};
 check(p0.mHealth==100&&p0.mSRT.t.x==oldPosition&&p0.mMode==0,"capture does not mutate gameplay");
 pc_coop_world_end_scene();check(!pc_coop_world_active()&&!pc_coop_world_capture(records),"scene end clears capture before heap reset");
 check(!pc_coop_world_begin_host(100,1)&&pc_coop_world_begin_host(100,2)&&pc_coop_world_capture(records),"new scene requires a higher epoch");
 check(pc_coop_world_actor_id(&p0,EntityKind::Pikmin)!=replacement,"previous scene identity cannot alias next scene");
 pc_coop_world_end_scene();
 if(!bad)std::puts("PASS actual P1 capture and pool hooks: default inert, ownership, recycled actors, finite/atomic snapshot and stage lifetime");
 return bad?1:0;
}
'''
(out/'capture-test.cpp').write_text(test,encoding='utf-8')
(out/'disabled-test.cpp').write_text('#include "netplay/pc_coop_world_hooks.h"\nint main(){pc_coop_world_forget(nullptr);pc_coop_world_end_scene();}\n',encoding='utf-8')
print('Generated actual capture/pool regression fixture and compile-out check:',out)
