#include "nectar_net/actor_frame.h"
#include "nectar_net/byte_io.h"
#include <algorithm>
#include <cstdio>
#include <limits>
#include <random>

using namespace nectar::net;
namespace {
int failures=0;
void check(bool ok,const char* why){if(!ok){std::printf("FAIL %s\n",why);++failures;}}
using Packets=std::vector<std::vector<std::uint8_t>>;
using Result=ActorFrameReceiver::Result;
std::vector<EntityRecord> squad(std::uint16_t epoch,std::size_t count) {
    CaptainState a,b;b.player=1;
    std::vector<EntityRecord> records={captainRecord(epoch,a),captainRecord(epoch,b)};
    for(std::size_t i=0;i<count;++i) {
        PikminState p;p.position.x=static_cast<float>(i);p.owner=static_cast<std::uint8_t>(i%2);p.leader=p.owner;
        p.color=static_cast<std::uint8_t>(i%3);
        NetEntityId id;id.sceneEpoch=epoch;id.kind=EntityKind::Pikmin;id.counter=static_cast<std::uint32_t>(i+10);
        records.push_back(pikminRecord(id.pack(),p));
    }
    return records;
}
Packets pack(std::uint64_t frame,std::uint64_t tick,std::size_t count=60) {
    Packets p;check(packActorFrame(100,1,frame,tick,squad(1,count),1000,{},p),"valid host frame packs");return p;
}
Result feed(ActorFrameReceiver& receiver,const std::vector<std::uint8_t>& p,std::uint64_t time=0) {
    return receiver.receive(p.data(),p.size(),time);
}
void all(ActorFrameReceiver& receiver,const Packets& p,std::uint64_t time=0) {for(const auto& b:p)feed(receiver,b,time);}
// Construct a complete but semantically bad frame with matching integrity hash.
// Its checksum isn't a security boundary: the decoder must validate its actors.
std::vector<std::uint8_t> unchecked(const std::vector<EntityRecord>& records,std::uint64_t frame) {
    auto body=encodeWorldDelta(kWorldDeltaKeyframe,records);std::uint64_t h=14695981039346656037ULL;
    for(auto b:body){h^=b;h*=1099511628211ULL;}
    ByteWriter w(1200);w.writeU32(0x4e434631);w.writeU8(1);w.writeU8(kWorldDeltaKeyframe);w.writeU16(1);
    w.writeU64(100);w.writeU64(frame);w.writeU64(frame*10+100);w.writeU32(static_cast<std::uint32_t>(body.size()));
    w.writeU64(h);w.writeU16(0);w.writeU16(1);w.writeBytes(body.data(),body.size());return w.bytes();
}
}
int main(){
 ActorFrameReceiver receiver;auto first=pack(1,10);
 check(feed(receiver,first[0])==Result::Rejected,"inactive receiver never accepts a world");
 check(!receiver.begin(0,1)&&!receiver.begin(100,0)&&receiver.begin(100,1),"explicit valid context required");
 check(first.size()>1,"normal squad requires multiple network packets");
 for(auto it=first.rbegin();it!=first.rend();++it){
  auto result=feed(receiver,*it,100);
  if(it+1!=first.rend())check(result==Result::Buffered&&!receiver.hasFrame(),"reordered partial squad never publishes");
  else check(result==Result::Committed,"last missing fragment atomically commits");
 }
 check(receiver.current().frame==1&&receiver.current().tick==10&&receiver.current().pikmin.size()==60,"complete captain/squad replica");
 const auto id=NetEntityId{1,EntityKind::Pikmin,0,69}.pack();
 check(receiver.current().pikmin.at(id).position.x==59&&receiver.current().pikmin.at(id).owner==1,"actual transforms and per-player ownership survive wire");
 check(feed(receiver,first[0])==Result::Ignored,"old complete frame cannot replay");
 auto second=pack(2,20,20);
 check(feed(receiver,second[0],200)==Result::Buffered,"replacement begins without deleting old actors");
 check(feed(receiver,second[0],201)==Result::Buffered&&receiver.current().pikmin.size()==60,"duplicate fragment doesn't count twice");
 auto conflict=second[0];conflict.back()^=1;
 check(feed(receiver,conflict,202)==Result::Rejected,"conflicting duplicate refused");
 check(receiver.current().frame==1,"corrupt packet never replaces visible state");
 for(std::size_t i=1;i<second.size();++i)feed(receiver,second[i],203);
 check(receiver.current().frame==2&&receiver.current().pikmin.size()==20,"despawn occurs only once whole replacement arrives");
 auto third=pack(3,30),fourth=pack(4,40,40);
 feed(receiver,third[0],300);feed(receiver,fourth[0],301);all(receiver,third,302);
 check(receiver.current().frame==2,"older unfinished frame cannot supersede newer assembly");
 all(receiver,fourth,303);check(receiver.current().frame==4&&receiver.current().pikmin.size()==40,"newer full frame supersedes incomplete older one");
 auto five=pack(5,50);feed(receiver,five[0],1000);feed(receiver,five[0],2999);receiver.expire(3000);
 check(!receiver.assembling()&&receiver.current().frame==4,"fixed timeout discards assembly but keeps last good world");
 check(feed(receiver,five[0],3001)==Result::Ignored,"late fragments cannot restart expired frame");
 auto six=pack(6,60);six.back().back()^=1;all(receiver,six,3100);
 check(receiver.current().frame==4&&!receiver.assembling(),"whole-frame integrity failure keeps last good world");
 auto seven=pack(7,70);auto bad=seven[0];bad[15]^=1;
 check(feed(receiver,bad,3200)==Result::Ignored,"other session refused before allocation");
 bad=seven[0];bad[7]=2;check(feed(receiver,bad,3200)==Result::Ignored,"other scene refused");
 bad=seven[0];bad[4]=2;check(feed(receiver,bad,3200)==Result::Rejected,"unknown wire version refused");
 bad=seven[0];bad[5]=0;check(feed(receiver,bad,3200)==Result::Rejected,"delta cannot masquerade as complete actor frame");
 bad=seven[0];bad[32]=255;check(feed(receiver,bad,3200)==Result::Rejected,"oversized frame refused before allocation");
 bad=seven[0];bad[46]=255;check(feed(receiver,bad,3200)==Result::Rejected,"unbounded fragment count refused");
 check(receiver.current().frame==4,"malformed headers cannot mutate published state");
 all(receiver,seven,3300);check(receiver.current().frame==7,"valid later frame recovers after loss/corruption");
 Packets old=seven;auto invalid=squad(1,1);invalid.push_back(invalid[0]);
 check(!packActorFrame(100,1,8,80,invalid,1000,{},old)&&old==seven,"duplicate entity rejects entire host batch without changing output");
 invalid=squad(1,1);invalid[1].id=NetEntityId{1,EntityKind::Captain,0,100}.pack();invalid[1].data=invalid[0].data;
 check(!packActorFrame(100,1,8,80,invalid,1000,{},old),"duplicate captain player rejected");
 check(feed(receiver,unchecked(invalid,8),3400)==Result::Rejected&&receiver.current().frame==7,"guest validates semantics even with a matching hash");
 invalid=squad(1,1);invalid.back().schema=3;
 check(feed(receiver,unchecked(invalid,9),3400)==Result::Rejected,"unknown actor schema never publishes");
 invalid=squad(1,1);PikminState ps;ps.position.x=std::numeric_limits<float>::quiet_NaN();
 invalid.back().data=encodePikminState(ps);
 check(feed(receiver,unchecked(invalid,10),3400)==Result::Rejected,"guest rejects nonfinite transform");
 invalid=squad(1,1);invalid.erase(invalid.begin()+1);ps=PikminState{};ps.owner=1;ps.leader=1;
 invalid.back().data=encodePikminState(ps);
 check(feed(receiver,unchecked(invalid,11),3400)==Result::Rejected,"owner/leader must refer to an included captain");
 auto empty=squad(1,0);Packets noPikis;
 check(packActorFrame(100,1,12,120,empty,1200,{},noPikis),"zero Pikmin with captains is valid");
 all(receiver,noPikis,3500);check(receiver.current().frame==12&&receiver.current().pikmin.empty(),"complete empty squad removes previous Pikmin");
 auto pastTick=pack(13,119);check(feed(receiver,pastTick[0])==Result::Ignored,"simulation tick cannot rewind despite a newer frame number");
 ActorFrameLimits tiny;tiny.maxFrameBytes=64;
 check(!packActorFrame(100,1,1,1,squad(1,60),1000,tiny,old),"oversized captures fail rather than silently dropping actors");
 tiny=ActorFrameLimits{};tiny.maxFragments=1;
 check(!packActorFrame(100,1,1,1,squad(1,60),1000,tiny,old),"fragment limit fails atomically");
 for(auto budget:{std::size_t(48),std::size_t(1201)})check(!packActorFrame(100,1,1,1,empty,budget,{},old),"bad packet budget refused");
 for(std::size_t n=0;n<seven[0].size();++n)check(receiver.receive(seven[0].data(),n,4000)!=Result::Committed,"truncated fragment cannot publish");
 auto trailing=seven[0];trailing.push_back(0);check(feed(receiver,trailing,4000)==Result::Rejected,"trailing fragment bytes refused");
 receiver.end();check(!receiver.hasFrame()&&!receiver.assembling()&&feed(receiver,seven[0])==Result::Rejected,"leave clears both world and pending bytes");
 check(receiver.begin(100,2)&&feed(receiver,seven[0])==Result::Ignored,"old scene data cannot enter new accepted scene");
 std::mt19937 rng(45);receiver.begin(100,1);
 for(std::uint64_t frame=1;frame<=1000;++frame){
  const std::size_t count=rng()%101;auto packets=pack(frame,frame,count);
  std::shuffle(packets.begin(),packets.end(),rng);
  const bool lose=(frame%5)==0;const auto previous=receiver.current().frame;
  for(std::size_t i=0;i<packets.size();++i){if(lose&&i+1==packets.size())continue;feed(receiver,packets[i],frame*10);if(i%2==0)feed(receiver,packets[i],frame*10);}
  check(lose?receiver.current().frame==previous:receiver.current().frame==frame,"1000-frame reordered/duplicate/loss simulation remains atomic");
  if(!lose)check(receiver.current().pikmin.size()==count,"all actors replaced together with no ghosts");
 }
 if(!failures)std::puts("PASS actor frames: bounded multipart assembly, atomic replicas, loss/reorder/retry/corruption, schema/scene/session guards, expiry and1000 changing squads");
 return failures?1:0;
}
