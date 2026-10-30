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
#include <set>
#include "nectar_net/pikmin_replication.h"
struct Vec{float x=0,y=0,z=0;};
struct Creature{virtual ~Creature()=default;struct{Vec t,r;}mSRT;Vec mVelocity,mLastPosition;
 float mFaceDirection=0,mHealth=100;bool alive=true,canRemove=true;
 virtual bool isAlive(){return alive;}bool removable(){return canRemove;}};

class Graphics{};
struct Animator{int mCurrentAnimID=0;float mAnimationCounter=0;};
struct Animations{Animator upper,lower;Animator&getUpperAnimator(){return upper;}Animator&getLowerAnimator(){return lower;}};
struct Navi:Creature{int mNaviID=0;Vec mCursorWorldPos;bool mIsCursorVisible=true;Animations mNaviAnimMgr;
 void pcCoopWhistleCapture(nectar::net::CaptainState&s){s.whistleActive=1;s.whistleRadius=80.0f+static_cast<float>(mNaviID);}
 bool pcCoopVisualValidate(const nectar::net::CaptainState&s)const{return s.upperAnimation<90&&s.lowerAnimation<90&&s.upperFrame<=64&&s.lowerFrame<=64;}
 void pcCoopVisualApply(const nectar::net::CaptainState&s){mHealth=s.health;mCursorWorldPos={s.cursor.x,s.cursor.y,s.cursor.z};}};
class Piki:public Creature{public:Navi*mNavi=nullptr;std::uint16_t mColor=0,mMode=0;int mHappa=0,mPlayerId=0;Animations mPikiAnimMgr;};
class ViewPiki:public Piki{public:bool ready=true;int applied=0,drawn=0;nectar::net::PikminState last;
 bool pcCoopVisualReady()const{return ready;}
 bool pcCoopVisualValidate(const nectar::net::PikminState&s)const{return ready&&nectar::net::validPikminState(s)&&s.color<3&&s.upperAnimation<90&&s.lowerAnimation<90&&s.upperFrame<=64&&s.lowerFrame<=64;}
 void pcCoopVisualApply(const nectar::net::PikminState&s){++applied;last=s;}
 void pcCoopVisualDraw(Graphics&){++drawn;}};
struct ObjectMgr{std::vector<Creature*>objects;};
struct MonoObjectMgr:ObjectMgr{int mNumObjects=0,mMaxElements=1;Creature*objectStorage[4]={};Creature**mObjectList=objectStorage;int statusStorage[4]={-1,-1,-1,-1};int*mEntryStatus=statusStorage;
 int getEmptyIndex(){for(int i=0;i<mMaxElements;++i)if(mEntryStatus[i]==-1)return i;return -1;}
 int getIndex(Creature*p){for(int i=0;i<mMaxElements;++i)if(mObjectList[i]==p)return i;return -1;}
 Creature*birth();void kill(Creature*);};
struct NaviMgr:MonoObjectMgr{};struct PikiMgr:MonoObjectMgr{
 bool pcCoopVisualSlots(std::vector<ViewPiki*>&);bool pcCoopVisualSlotsValid(const std::vector<ViewPiki*>&)const;};
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
visual=(ROOT/'games/pikmin1/pc_port/netplay/pc_coop_pikmin_visuals.cpp').read_text(encoding='utf-8')
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
test+=method(visual,'bool PikiMgr::pcCoopVisualSlots(')+'\n'+method(visual,'bool PikiMgr::pcCoopVisualSlotsValid(')+'\n'
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
 p0.mPikiAnimMgr.upper.mCurrentAnimID=23;p0.mPikiAnimMgr.upper.mAnimationCounter=12.5f;
 p0.mPikiAnimMgr.lower.mCurrentAnimID=2;p0.mPikiAnimMgr.lower.mAnimationCounter=7.75f;
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
 check(guest.current().captains.begin()->second.whistleActive==1 && guest.current().captains.begin()->second.whistleRadius==80,"host whistle radius travels through actual capture and packet decoding");
 check(guest.current().captains.size()==2&&guest.current().pikmin.size()==2,"actual engine capture reaches guest replica intact");
 const auto beforePackets=packets;
 check(!pc_coop_world_capture_packets(1,51,100,packets)&&packets==beforePackets,"capture packet sequence cannot repeat");
 check(!pc_coop_world_capture_packets(2,49,100,packets)&&packets==beforePackets,"capture tick cannot rewind");
 check(!pc_coop_world_capture_packets(2,51,48,packets)&&packets==beforePackets,"packetization failure never emits partial engine capture");
 check(pc_coop_world_capture_packets(2,51,100,packets),"failed packetization doesn't consume frame sequence");

 const auto original=pc_coop_world_actor_id(&p0,EntityKind::Pikmin);
 check(original&&!pc_coop_world_actor_id(&p0,EntityKind::Enemy),"actual actors have typed IDs");
 auto s=read(records,original);check(s.position.x==40&&s.owner==0&&s.leader==0,"capture actual transform and association");
 check(s.upperAnimation==23&&s.lowerAnimation==2&&s.upperFrame==12.5f&&s.lowerFrame==7.75f,"actual host capture preserves both independent animation IDs and counters");
 p0.mPikiAnimMgr.upper.mCurrentAnimID=-1;check(!pc_coop_world_capture(records),"host cannot publish uninitialized animation ID");p0.mPikiAnimMgr.upper.mCurrentAnimID=23;
 p0.mPikiAnimMgr.lower.mAnimationCounter=std::numeric_limits<float>::quiet_NaN();check(!pc_coop_world_capture(records),"host cannot publish invalid final pose counter");p0.mPikiAnimMgr.lower.mAnimationCounter=7.75f;
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

 // Authority is explicit and session-scoped, not inferred from render FPS.
 check(pc_coop_world_may_advance()&&!pc_coop_world_has_guest(),"scene teardown restores ordinary authority");
 check(pc_coop_world_begin_host(110,3)&&!pc_coop_world_may_advance(),"admitted host begins held before readiness");
 check(!pc_coop_world_set_host_running(999,3,true)&&!pc_coop_world_set_host_running(110,4,true)&&!pc_coop_world_may_advance(),"wrong accepted context cannot release host");
 check(pc_coop_world_set_host_running(110,3,true)&&pc_coop_world_may_advance(),"matching ready driver releases actual host context");
 check(pc_coop_world_set_host_running(110,3,false)&&!pc_coop_world_may_advance(),"pause or disconnect holds host without ending scene");
 navis.objects={&n0};check(!pc_coop_world_set_host_running(110,3,true)&&!pc_coop_world_may_advance(),"missing live captain cannot resume host");navis.objects={&n0,&n1};
 pc_coop_world_end_scene();check(!pc_coop_world_set_host_running(110,3,true)&&pc_coop_world_may_advance(),"old callback cannot revive ended host");

 // Guest engine application: real adapter TU, no copied transform implementation.
 check(!pc_coop_world_guest_active(),"guest is inactive in ordinary gameplay");
 navis.objects={&n0};
 check(!pc_coop_world_begin_guest(101,3),"guest scene requires both actual local presentation captains");
 navis.objects={&n0,&n1};
 check(pc_coop_world_begin_guest(101,3)&&pc_coop_world_guest_active()&&pc_coop_world_active(),"explicit guest scene binds both captain lifetimes");
 check(!pc_coop_world_begin_host(102,1)&&!pc_coop_world_capture(records),"guest cannot become host or capture authoritative world");
 check(pc_coop_world_has_guest()&&!pc_coop_world_may_advance()&&!pc_coop_world_set_host_running(101,3,true),"guest cannot acquire host advancement even with matching session context");
 ActorFrame view;view.frame=1;view.tick=100;
 CaptainState ca,cb;ca.player=0;cb.player=1;ca.position={100,20,30};cb.position={200,21,31};
 ca.velocity={1,2,3};cb.velocity={4,5,6};ca.faceDirection=1;cb.faceDirection=2;
 const auto id0=NetEntityId{3,EntityKind::Captain,0,40}.pack();
 const auto id1=NetEntityId{3,EntityKind::Captain,0,41}.pack();
 view.captains[id0]=ca;view.captains[id1]=cb;
 const float oldNaviX=n0.mSRT.t.x;
 check(!pc_coop_world_apply_guest_captains(999,3,view)&&n0.mSRT.t.x==oldNaviX,"wrong trusted session rejected with no writes");
 check(!pc_coop_world_apply_guest_captains(101,2,view),"wrong scene context refused");
 auto invalidView=view;invalidView.captains[id1].position.y=std::numeric_limits<float>::quiet_NaN();
 check(!pc_coop_world_apply_guest_captains(101,3,invalidView)&&n0.mSRT.t.x==oldNaviX,"bad SECOND actor cannot partially move first captain");
 invalidView=view;invalidView.captains[id1].player=0;
 check(!pc_coop_world_apply_guest_captains(101,3,invalidView),"duplicate remote player cannot alias captain");
 invalidView=view;invalidView.captains.erase(id1);
 check(!pc_coop_world_apply_guest_captains(101,3,invalidView),"partial remote captain set cannot apply");
 check(pc_coop_world_apply_guest_captains(101,3,view)&&n0.mSRT.t.x==100&&n1.mSRT.t.x==200&&
       n1.mVelocity.z==6&&n1.mFaceDirection==2&&n1.mSRT.r.y==2&&n1.mLastPosition.x==200,
       "both actual guest captains receive host transforms, velocity, facing and coherent previous-position");
 check(!pc_coop_world_apply_guest_captains(101,3,view),"same guest frame cannot apply twice");
 view.frame=2;view.tick=99;check(!pc_coop_world_apply_guest_captains(101,3,view),"authoritative clock cannot rewind");
 view.tick=101;invalidView=view;invalidView.captains.erase(id1);
 invalidView.captains[NetEntityId{3,EntityKind::Captain,0,42}.pack()]=cb;
 check(!pc_coop_world_apply_guest_captains(101,3,invalidView),"remote actor ID cannot silently change mid-scene");
 invalidView=view;invalidView.captains.erase(id1);
 invalidView.captains[NetEntityId{2,EntityKind::Captain,0,41}.pack()]=cb;
 check(!pc_coop_world_apply_guest_captains(101,3,invalidView),"previous-scene actor ID refused");
 Navi replacementNavi;replacementNavi.mNaviID=1;navis.objects={&n0,&replacementNavi};
 check(!pc_coop_world_apply_guest_captains(101,3,view),"replaced local captain not overwritten");
 navis.objects={&n0,&n1};pc_coop_world_forget(&n1);
 check(!pc_coop_world_guest_active()&&!pc_coop_world_apply_guest_captains(101,3,view),"same-address pool reuse invalidates entire guest binding");
 check(pc_coop_world_has_guest()&&!pc_coop_world_may_advance(),"invalidated guest binding stays held rather than silently falling back to solo");
 pc_coop_world_end_scene();
 check(!pc_coop_world_active()&&!pc_coop_world_apply_guest_captains(101,3,view),"stage exit clears guest references before game heap reset");
 check(!pc_coop_world_begin_guest(101,3)&&pc_coop_world_begin_guest(101,4),"guest new scene requires higher accepted epoch");
 pc_coop_world_end_scene();

 // Whole-squad guest adapter: IDs bind explicit local objects, never manager order.
 p0.mColor=0;p1.mColor=2;p0.mMode=77;p1.mMode=88;
 p0.mNavi=&n0;p1.mNavi=&n1;pikis.objects={&p0,&p1};navis.objects={&n0,&n1};
 check(pc_coop_world_begin_guest(105,7),"new accepted guest cohort context");
 const auto pId0=NetEntityId{7,EntityKind::Pikmin,0,110}.pack();
 const auto pId1=NetEntityId{7,EntityKind::Pikmin,0,111}.pack();
 const auto cId0=NetEntityId{7,EntityKind::Captain,0,112}.pack();
 const auto cId1=NetEntityId{7,EntityKind::Captain,0,113}.pack();
 std::vector<PcCoopGuestPikminBinding> bindings={{pId1,&p1},{pId0,&p0}};
 check(!pc_coop_world_bind_guest_pikmin(999,7,bindings)&&!pc_coop_world_bind_guest_pikmin(105,6,bindings),"wrong accepted session/epoch cannot bind squad");
 auto wrongBindings=bindings;wrongBindings.pop_back();
 check(!pc_coop_world_bind_guest_pikmin(105,7,wrongBindings),"missing live local Pikmin cannot silently disappear");
 wrongBindings=bindings;wrongBindings[1].local=&p1;
 check(!pc_coop_world_bind_guest_pikmin(105,7,wrongBindings),"same local pool actor cannot represent two host Pikmin");
 wrongBindings=bindings;wrongBindings[1].id=pId1;
 check(!pc_coop_world_bind_guest_pikmin(105,7,wrongBindings),"duplicate host identity cannot alias local actors");
 Piki foreign;wrongBindings=bindings;wrongBindings[1].local=&foreign;
 check(!pc_coop_world_bind_guest_pikmin(105,7,wrongBindings),"foreign pointer outside live manager rejected before dereference");
 wrongBindings=bindings;wrongBindings[1].id=cId0;
 check(!pc_coop_world_bind_guest_pikmin(105,7,wrongBindings),"captain ID cannot bind a Pikmin");
 wrongBindings=bindings;wrongBindings[1].id=NetEntityId{6,EntityKind::Pikmin,0,110}.pack();
 check(!pc_coop_world_bind_guest_pikmin(105,7,wrongBindings),"previous-scene ID cannot bind a current Pikmin");
 wrongBindings.assign(511,{pId0,&p0});
 check(!pc_coop_world_bind_guest_pikmin(105,7,wrongBindings),"oversized cohort rejected before engine mutation");
 navis.objects={&n0,&replacementNavi};check(!pc_coop_world_bind_guest_pikmin(105,7,bindings),"changed local captain prevents squad binding");navis.objects={&n0,&n1};
 check(pc_coop_world_bind_guest_pikmin(105,7,bindings)&&!pc_coop_world_bind_guest_pikmin(105,7,bindings),"explicit complete cohort accepted once after failed attempts");
 ActorFrame squad;squad.frame=1;squad.tick=100;squad.captains[cId0]=ca;squad.captains[cId1]=cb;
 PikminState ps0,ps1;ps0.position={10,11,12};ps0.velocity={1,2,3};ps0.faceDirection=0.7f;ps0.health=60;ps0.owner=0;ps0.leader=1;ps0.color=0;ps0.maturity=2;ps0.action=9;
 ps1.position={20,21,22};ps1.velocity={4,5,6};ps1.faceDirection=0.8f;ps1.health=80;ps1.owner=1;ps1.leader=255;ps1.color=2;ps1.maturity=1;ps1.action=3;
 squad.pikmin[pId0]=ps0;squad.pikmin[pId1]=ps1;
 PikminState diagnostic;diagnostic.position.x=555;
 check(!pc_coop_world_guest_pikmin_state(pId0,diagnostic)&&diagnostic.position.x==555,"unapplied diagnostic getter leaves output intact");
 const auto unchangedX=p0.mSRT.t.x;
 check(!pc_coop_world_apply_guest_captains(105,7,squad)&&p0.mSRT.t.x==unchangedX,"captain-only path cannot consume a bound squad's frame");
 check(pc_coop_world_apply_guest_actors(105,7,squad),"whole captain+squad frame applied through actual engine adapter");
 check(p0.mSRT.t.x==10&&p1.mSRT.t.x==20&&p0.mVelocity.z==3&&p1.mVelocity.z==6&&p0.mLastPosition.x==10&&p0.mSRT.r.y==0.7f,
       "explicit IDs map correctly despite reversed binding order and coherent velocity/facing/previous positions");
 check(p0.mHealth==60&&p1.mHealth==80&&p0.mHappa==2&&p1.mHappa==1&&p0.mNavi==&n1&&!p1.mNavi,"actual health, maturity and local leader association updated");
 check(p0.mMode==77&&p1.mMode==88&&pc_coop_world_guest_pikmin_state(pId0,diagnostic)&&diagnostic.owner==0&&diagnostic.action==9,
       "host owner/job metadata retained without starting or overwriting guest AI actions");
 check(!pc_coop_world_apply_guest_actors(105,7,squad),"whole actor frame cannot apply twice");
 auto snapshot=[&]{return std::vector<float>{n0.mSRT.t.x,n1.mSRT.t.x,p0.mSRT.t.x,p1.mSRT.t.x,p0.mVelocity.z,p1.mVelocity.z,
    p0.mHealth,p1.mHealth,float(p0.mHappa),float(p1.mHappa),p0.mFaceDirection,p1.mFaceDirection};};
 auto expectRejected=[&](const ActorFrame& badFrame,const char* reason){
  const auto before=snapshot();Navi* leader0=p0.mNavi;Navi* leader1=p1.mNavi;
  check(!pc_coop_world_apply_guest_actors(105,7,badFrame)&&snapshot()==before&&p0.mNavi==leader0&&p1.mNavi==leader1,reason);
  PikminState last;check(pc_coop_world_guest_pikmin_state(pId0,last)&&last.position.x==10&&last.owner==0,"rejected complete frame keeps previous host metadata");
 };
 squad.frame=2;squad.tick=101;squad.captains[cId0].position.x=999;squad.pikmin[pId0].position.x=333;
 auto badSquad=squad;badSquad.pikmin[pId1].health=std::numeric_limits<float>::quiet_NaN();expectRejected(badSquad,"invalid LAST Pikmin vetoes ALL captain and Pikmin writes");
 badSquad=squad;badSquad.pikmin[pId1].color=4;expectRejected(badSquad,"P2-only color rejected by actual P1 adapter");
 badSquad=squad;badSquad.pikmin[pId1].color=1;expectRejected(badSquad,"unprepared color conversion cannot corrupt local model identity");
 badSquad=squad;badSquad.pikmin[pId1].maturity=3;expectRejected(badSquad,"invalid maturity rejects entire actor frame");
 badSquad=squad;badSquad.pikmin[pId1].owner=2;expectRejected(badSquad,"invalid owner rejects entire actor frame");
 badSquad=squad;badSquad.pikmin[pId1].leader=2;expectRejected(badSquad,"invalid leader cannot select an absent captain");
 badSquad=squad;badSquad.pikmin[pId1].health=-1;expectRejected(badSquad,"negative health rejects entire actor frame");
 badSquad=squad;badSquad.pikmin.erase(pId1);expectRejected(badSquad,"missing/dead remote actor requires explicit lifecycle adapter, no partial survivors");
 badSquad=squad;badSquad.pikmin[NetEntityId{7,EntityKind::Pikmin,0,114}.pack()]=ps1;expectRejected(badSquad,"new remote birth cannot be guessed onto an existing pool actor");
 badSquad=squad;badSquad.pikmin.erase(pId1);badSquad.pikmin[NetEntityId{7,EntityKind::Pikmin,1,111}.pack()]=ps1;expectRejected(badSquad,"recycled host identity cannot silently reuse guest binding");
 badSquad=squad;badSquad.tick=99;expectRejected(badSquad,"whole squad clock cannot rewind");
 badSquad=squad;badSquad.captains[cId1].position.x=std::numeric_limits<float>::infinity();expectRejected(badSquad,"invalid captain also vetoes squad updates");
 p1.mColor=1;expectRejected(squad,"local color/model changed outside admitted baseline");p1.mColor=2;
 pikis.objects={&p0,&p0};expectRejected(squad,"duplicate manager pointer cannot impersonate complete cohort");pikis.objects={&p0,&p1};
 Piki unexpected;pikis.objects.push_back(&unexpected);expectRejected(squad,"unbound live guest actor cannot be left as a ghost");pikis.objects.pop_back();
 pikis.objects={&p0};expectRejected(squad,"lost local bound actor rejects whole frame");pikis.objects={&p0,&p1};
 check(pc_coop_world_apply_guest_actors(105,7,squad)&&p0.mSRT.t.x==333&&n0.mSRT.t.x==999,"invalid attempted frames do not consume valid sequence");
 pc_coop_world_forget(&p0);
 check(!pc_coop_world_guest_active()&&!pc_coop_world_apply_guest_actors(105,7,squad)&&!pc_coop_world_guest_pikmin_state(pId0,diagnostic),"same-address Pikmin pool reuse invalidates whole guest cohort and metadata");
 pc_coop_world_end_scene();check(!pc_coop_world_apply_guest_actors(105,7,squad),"scene exit drops all squad pointers");
 pikis.objects.clear();check(pc_coop_world_begin_guest(105,8)&&pc_coop_world_bind_guest_pikmin(105,8,{}),"explicit empty-squad baseline is valid");
 ActorFrame empty;empty.frame=1;empty.tick=1;empty.captains[NetEntityId{8,EntityKind::Captain,0,1}.pack()]=ca;empty.captains[NetEntityId{8,EntityKind::Captain,0,2}.pack()]=cb;
 check(pc_coop_world_apply_guest_actors(105,8,empty),"empty complete squad still atomically updates both captains");pc_coop_world_end_scene();
 // 300 actors through real multipart encoding/receiver, not a hand-waved count.
 std::vector<Piki> many(300);std::vector<PcCoopGuestPikminBinding> manyBindings;std::vector<EntityRecord> manyRecords;
 ActorFrame manyFrame;manyFrame.frame=1;manyFrame.tick=50;
 for(int i=0;i<2;++i){const auto id=NetEntityId{9,EntityKind::Captain,0,static_cast<std::uint32_t>(i+1)}.pack();const auto value=i?cb:ca;
  manyFrame.captains[id]=value;auto r=captainRecord(9,value);r.id=id;manyRecords.push_back(r);}
 for(std::size_t i=0;i<many.size();++i){many[i].mColor=static_cast<std::uint16_t>(i%3);pikis.objects.push_back(&many[i]);
  const auto id=NetEntityId{9,EntityKind::Pikmin,0,static_cast<std::uint32_t>(i+10)}.pack();manyBindings.push_back({id,&many[i]});
  PikminState value;value.color=static_cast<std::uint8_t>(i%3);value.position.x=static_cast<float>(i);value.health=100;
  value.owner=static_cast<std::uint8_t>(i%2);value.leader=value.owner;manyFrame.pikmin[id]=value;manyRecords.push_back(pikminRecord(id,value));}
 check(pc_coop_world_begin_guest(106,9)&&pc_coop_world_bind_guest_pikmin(106,9,manyBindings),"large explicit cohort binds stable real adapter identities");
 std::vector<std::vector<std::uint8_t>> fragments;check(packActorFrame(106,9,1,50,manyRecords,1200,{},fragments)&&fragments.size()>1,"300-Pikmin full actor frame packetized under network budget");
 ActorFrameReceiver assembled;check(assembled.begin(106,9),"accepted receiver context for large squad");
 for(std::size_t i=fragments.size();i>0;--i){assembled.receive(fragments[i-1].data(),fragments[i-1].size(),0);
  if(i>1)check(!pc_coop_world_apply_guest_actors(106,9,assembled.current())&&many[299].mSRT.t.x==0,"partial reordered fragments never move any engine actor");}
 check(assembled.current().pikmin.size()==300&&pc_coop_world_apply_guest_actors(106,9,assembled.current())&&many[299].mSRT.t.x==299&&many[299].mNavi==&n1,"complete reordered network frame reaches all 300 actual guest Pikmin bindings");
 pc_coop_world_end_scene();pikis.objects.clear();

 // Dynamic visual population: real world adapter + actual dormant-pool admission.
 PikiMgr displayPool;ViewPiki d0,d1,d2;displayPool.mMaxElements=3;
 displayPool.mObjectList[0]=&d0;displayPool.mObjectList[1]=&d1;displayPool.mObjectList[2]=&d2;
 pikiMgr=&displayPool;navis.objects={&n0,&n1};Graphics gfx;
 check(pc_coop_world_begin_guest(107,10),"dynamic guest context admitted");
 check(!pc_coop_world_prepare_guest_visuals(999,10),"foreign context cannot claim dormant visual pool");
 displayPool.mNumObjects=1;check(!pc_coop_world_prepare_guest_visuals(107,10),"live jobs/Pikmin cannot be silently abandoned by display admission");displayPool.mNumObjects=0;
 displayPool.mEntryStatus[0]=-2;check(!pc_coop_world_prepare_guest_visuals(107,10),"pending destruction is not a safe dormant slot");displayPool.mEntryStatus[0]=-1;
 d2.ready=false;check(!pc_coop_world_prepare_guest_visuals(107,10),"missing display resources refuse admission");d2.ready=true;
 check(pc_coop_world_prepare_guest_visuals(107,10)&&!pc_coop_world_prepare_guest_visuals(107,10),"dormant visual pool can be owned only once");
 check(pc_coop_world_draw_guest_pikmin(gfx)&&d0.drawn==0&&d1.drawn==0,"empty admitted display suppresses stale normal population before baseline");
 ActorFrame dynamic;dynamic.frame=1;dynamic.tick=100;
 const auto dc0=NetEntityId{10,EntityKind::Captain,0,1}.pack(),dc1=NetEntityId{10,EntityKind::Captain,0,2}.pack();
 const auto dp0=NetEntityId{10,EntityKind::Pikmin,0,10}.pack(),dp1=NetEntityId{10,EntityKind::Pikmin,0,11}.pack(),dp2=NetEntityId{10,EntityKind::Pikmin,0,12}.pack();
 dynamic.captains[dc0]=ca;dynamic.captains[dc1]=cb;
 PikminState visual0;visual0.color=0;visual0.owner=0;visual0.upperAnimation=23;visual0.upperFrame=8.5f;
 PikminState visual1=visual0;visual1.color=2;visual1.owner=1;visual1.maturity=2;visual1.lowerAnimation=2;visual1.lowerFrame=4;
 dynamic.pikmin[dp0]=visual0;dynamic.pikmin[dp1]=visual1;
 check(pc_coop_world_apply_guest_visuals(107,10,dynamic)&&d0.applied==1&&d1.applied==1&&d0.last.upperFrame==8.5f&&d1.last.lowerFrame==4,"complete host population samples apply to actual guest model slots");
 check(displayPool.mNumObjects==0&&displayPool.mEntryStatus[0]==-1&&displayPool.mEntryStatus[1]==-1,"display never registers live actors or consumes real Pikmin allowance");
 check(!pc_coop_world_bind_guest_pikmin(107,10,{})&&!pc_coop_world_apply_guest_captains(107,10,dynamic),"fixed/partial adapter cannot take over visual population mode");
 pc_coop_world_draw_guest_pikmin(gfx);check(d0.drawn==1&&d1.drawn==1&&d2.drawn==0,"exactly current authoritative population is displayed");
 dynamic.frame=2;dynamic.tick=101;auto invalidDynamic=dynamic;invalidDynamic.pikmin[dp1].upperAnimation=99;invalidDynamic.captains[dc0].position.x=9999;
 const auto beforeCapt=n0.mSRT.t.x;
 check(!pc_coop_world_apply_guest_visuals(107,10,invalidDynamic)&&d0.applied==1&&d1.applied==1&&n0.mSRT.t.x==beforeCapt,"bad final asset pose never partially updates first model or either captain");
 invalidDynamic=dynamic;invalidDynamic.pikmin[NetEntityId{10,EntityKind::Pikmin,0,13}.pack()]=visual0;invalidDynamic.pikmin[dp2]=visual0;
 check(!pc_coop_world_apply_guest_visuals(107,10,invalidDynamic),"complete population above local capacity is refused without truncation");
 invalidDynamic=dynamic;invalidDynamic.pikmin[NetEntityId{9,EntityKind::Pikmin,0,20}.pack()]=visual0;
 check(!pc_coop_world_apply_guest_visuals(107,10,invalidDynamic),"old-scene population identity refused");
 dynamic.pikmin.erase(dp0);dynamic.pikmin[dp2]=visual0;dynamic.pikmin[dp1].color=1;
 check(pc_coop_world_apply_guest_visuals(107,10,dynamic)&&d0.applied==2&&d1.applied==2&&d1.last.color==1,"death/birth replacement and color conversion are one atomic visual transaction");
 check(!pc_coop_world_guest_pikmin_state(dp0,diagnostic)&&pc_coop_world_guest_pikmin_state(dp2,diagnostic)&&diagnostic.upperFrame==8.5f,"removed identity disappears and new identity has only its host state");
 dynamic.frame=3;dynamic.tick=102;dynamic.pikmin.clear();check(pc_coop_world_apply_guest_visuals(107,10,dynamic),"complete empty population removes every guest visual without gameplay kill");
 pc_coop_world_draw_guest_pikmin(gfx);check(d0.drawn==1&&d1.drawn==1&&!pc_coop_world_guest_pikmin_state(dp1,diagnostic),"empty snapshot leaves no ghost model or metadata");
 dynamic.frame=4;dynamic.tick=103;dynamic.pikmin[dp0]=visual0;pc_coop_world_forget(&d2);
 check(!pc_coop_world_guest_active()&&!pc_coop_world_may_advance()&&!pc_coop_world_apply_guest_visuals(107,10,dynamic)&&pc_coop_world_draw_guest_pikmin(gfx),"even dormant slot reuse invalidates ownership, holds guest and suppresses normal fallback");
 pc_coop_world_end_scene();check(!pc_coop_world_draw_guest_pikmin(gfx),"scene teardown restores ordinary manager draw ownership");


 // Presentation redraws cannot consume a host sequence or change game metadata.
 pikiMgr=&displayPool;navis.objects={&n0,&n1};d0.applied=d1.applied=d2.applied=0;
 check(pc_coop_world_begin_guest(109,20)&&pc_coop_world_prepare_guest_visuals(109,20),"smoothing display context");
 ActorFrame smooth;smooth.frame=1;smooth.tick=100;
 auto sc0=NetEntityId{20,EntityKind::Captain,0,1}.pack(),sc1=NetEntityId{20,EntityKind::Captain,0,2}.pack();
 auto sp0=NetEntityId{20,EntityKind::Pikmin,0,3}.pack(),sp1=NetEntityId{20,EntityKind::Pikmin,0,4}.pack();
 smooth.captains[sc0]=ca;smooth.captains[sc1]=cb;smooth.pikmin[sp0]=visual0;smooth.pikmin[sp1]=visual1;
 check(!pc_coop_world_present_guest(smooth),"cannot present before accepted baseline");
 check(pc_coop_world_apply_guest_visuals(109,20,smooth),"baseline before smoothing");
 auto shown=smooth;shown.captains[sc0].position.x=12;shown.pikmin[sp0].position.x=24;shown.captains[sc0].cursor={18,0,12};
 shown.pikmin[sp0].owner=1;shown.pikmin[sp0].health=0;shown.pikmin[sp0].color=2;shown.captains[sc0].health=0;
 check(pc_coop_world_present_guest(shown)&&n0.mSRT.t.x==12&&d0.last.position.x==24,"actual display applies intermediate transforms");
 check(n0.mCursorWorldPos.x==18&&n0.mCursorWorldPos.z==12,"actual display applies interpolated cursor instead of latest packet cursor");
 check(n0.mHealth==ca.health&&d0.last.owner==visual0.owner&&d0.last.health==visual0.health&&d0.last.color==visual0.color,"smoothing cannot overwrite accepted captain health or Pikmin metadata");
 check(pc_coop_world_guest_pikmin_state(sp0,diagnostic)&&diagnostic.position.x==visual0.position.x,"smoothing does not overwrite host diagnostic state");
 auto expectPresentationRejected=[&](const ActorFrame& badFrame,const char*why){
  int count=d0.applied;float x=n0.mSRT.t.x;check(!pc_coop_world_present_guest(badFrame)&&d0.applied==count&&n0.mSRT.t.x==x,why);
 };
 auto badShown=shown;badShown.frame=2;expectPresentationRejected(badShown,"unadmitted future frame refused");
 badShown=shown;badShown.tick=99;expectPresentationRejected(badShown,"presentation tick rewind refused");
 badShown=shown;badShown.pikmin.erase(sp1);expectPresentationRejected(badShown,"missing population refused atomically");
 badShown=shown;badShown.pikmin[sp1].upperAnimation=89;expectPresentationRejected(badShown,"presentation cannot switch accepted animation clip");
 badShown=shown;badShown.pikmin[sp1].upperFrame=1000;expectPresentationRejected(badShown,"bad final pose does not partially update any actor");
 smooth.frame=2;smooth.tick=101;
 check(pc_coop_world_apply_guest_visuals(109,20,smooth),"presentation redraws did not consume the next authoritative frame");
 expectPresentationRejected(shown,"old population sequence refused after new frame");
 pc_coop_world_forget(&d2);expectPresentationRejected(smooth,"recycled dormant pool refuses redraw");
 pc_coop_world_end_scene();check(!pc_coop_world_present_guest(smooth),"scene teardown clears display redraw access");

 // New session after rejoin: both idle actors keep their original owner.
 pikiMgr=&pikis;navis.objects={&n0,&n1};pikis.objects={&p0,&p1};
 p0.mNavi=nullptr;p1.mNavi=nullptr;p0.mPlayerId=0;p1.mPlayerId=1;
 check(pc_coop_world_begin_host(111,11,true)&&pc_coop_world_capture(records),"practice host captures idle followers for new session");
 check(read(records,pc_coop_world_actor_id(&p0,EntityKind::Pikmin)).owner==0 &&
       read(records,pc_coop_world_actor_id(&p1,EntityKind::Pikmin)).owner==1,"idle squads retain owners after host registry reconstruction");
 p1.mPlayerId=0;check(!pc_coop_world_capture(records),"unexpected owner change fails whole practice capture");
 pc_coop_world_end_scene();
 pc_coop_world_stop();check(!pc_coop_world_may_advance(),"startup failure freezes even before adapter binding");pc_coop_world_end_scene();check(pc_coop_world_may_advance(),"scene teardown clears emergency hold");

 if(!bad)std::puts("PASS actual P1 capture and pool hooks: default inert, ownership, recycled actors, finite/atomic snapshot, whole guest squad, 300-Pikmin packet apply and stage lifetime");
 return bad?1:0;
}
'''
(out/'capture-test.cpp').write_text(test,encoding='utf-8')
(out/'disabled-test.cpp').write_text('#include "netplay/pc_coop_world_hooks.h"\nint main(){pc_coop_world_forget(nullptr);pc_coop_world_end_scene();return (!pc_coop_world_may_advance()||pc_coop_world_has_guest())?1:0;}\n',encoding='utf-8')
print('Generated actual capture/pool regression fixture and compile-out check:',out)
