#include "nectar_net/enemy_replication.h"
#include "nectar_net/actor_frame.h"
#include <cstdio>
#include <limits>
using namespace nectar::net;
namespace {int failures=0,checks=0;void check(bool x,const char* s){++checks;if(!x){++failures;std::printf("FAIL %s\n",s);}}}
int main(){
 EnemyState e;e.health=e.maxHealth=150;e.position={20,3,-40};e.animation=4;e.animationFrame=12;
 auto bytes=encodeEnemyState(e);EnemyState decoded;
 check(bytes.size()==kEnemyStateBytes && decodeEnemyState(bytes.data(),bytes.size(),decoded),"enemy sample round trip");
 check(decoded.health==150&&decoded.position.z==-40&&decoded.animationFrame==12,"combat pose preserved");
 for(std::size_t n=0;n<bytes.size();++n)check(!decodeEnemyState(bytes.data(),n,decoded),"all truncations refused");
 auto trailing=bytes;trailing.push_back(0);check(!decodeEnemyState(trailing.data(),trailing.size(),decoded),"trailing bytes refused");
 for(int field=0;field<8;++field){auto bad=e;switch(field){
 case 0:bad.health=-1;break;case 1:bad.position.x=std::numeric_limits<float>::quiet_NaN();break;
 case 2:bad.scale.x=0;break;case 3:bad.scale.z=11;break;case 4:bad.type=34;break;
 case 5:bad.animation=1024;break;case 6:bad.animationFrame=-1;break;default:bad.visible=2;break;}
 check(encodeEnemyState(bad).empty(),"unsafe enemy or unknown type refused");}
 for(std::size_t at:{std::size_t(58),std::size_t(59)}){auto corrupt=bytes;corrupt[at]=255;auto before=decoded;
 check(!decodeEnemyState(corrupt.data(),corrupt.size(),decoded)&&decoded.health==before.health,"malicious type/visibility preserves accepted sample");}
 const auto id=NetEntityId{1,EntityKind::Enemy,0,40}.pack();
 check(!enemyRecord(NetEntityId{1,EntityKind::Pikmin,0,40}.pack(),e).id,"enemy cannot masquerade as Pikmin");
 CaptainState a,b;b.player=1;PikminState p;p.health=10;p.owner=p.leader=1;
 const auto pid=NetEntityId{1,EntityKind::Pikmin,0,30}.pack();
 std::vector<EntityRecord> records={captainRecord(1,a),captainRecord(1,b),pikminRecord(pid,p),enemyRecord(id,e)};
 std::vector<std::vector<std::uint8_t>> packets;ActorFrameReceiver rx;rx.begin(300,1);
 check(packActorFrame(300,1,1,1,records,160,{},packets)&&packets.size()>1,"enemy shares bounded complete world frame");
 for(std::size_t i=0;i<packets.size();++i){auto& x=packets[packets.size()-1-i];rx.receive(x.data(),x.size(),i);
 if(i+1<packets.size())check(!rx.hasFrame(),"partial enemy and squad cannot commit separately");}
 check(rx.current().enemies.size()==1&&rx.current().pikmin.size()==1,"combatants admitted atomically");
 e.health=0;e.visible=0;records.back()=enemyRecord(id,e);packets.clear();
 check(packActorFrame(300,1,2,2,records,160,{},packets),"defeat frame packs");
 for(auto& x:packets)rx.receive(x.data(),x.size(),10);
 check(rx.current().enemies.at(id).health==0&&!rx.current().enemies.at(id).visible,"death synchronized without guest AI");
 records.erase(records.begin()+2);records.pop_back();packets.clear();
 check(packActorFrame(300,1,3,3,records,160,{},packets),"retirement frame packs");
 for(auto& x:packets)rx.receive(x.data(),x.size(),20);
 check(rx.current().enemies.empty()&&rx.current().pikmin.empty(),"dead enemies and Pikmin retire together without ghosts");
 records.push_back(enemyRecord(id,e));records.push_back(enemyRecord(NetEntityId{1,EntityKind::Enemy,0,41}.pack(),e));
 check(!packActorFrame(300,1,4,4,records,1000,{},packets),"unsupported population cannot silently exceed encounter capacity");
 if(!failures)std::printf("PASS %d enemy encounter checks: combat pose, strict schemas, multipart atomicity and shared defeat/retirement\n",checks);
 return failures?1:0;
}
