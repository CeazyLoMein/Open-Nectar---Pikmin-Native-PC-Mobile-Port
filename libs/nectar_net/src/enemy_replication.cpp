#include "nectar_net/enemy_replication.h"
#include "nectar_net/byte_io.h"
#include <cmath>
#include <cstring>
namespace nectar::net {
namespace {
bool bounded(float f,float n){return std::isfinite(f)&&std::fabs(f)<=n;}
std::uint32_t bits(float f){std::uint32_t n;std::memcpy(&n,&f,4);return n;}
float value(std::uint32_t n){float f;std::memcpy(&f,&n,4);return f;}
}
bool validEnemyState(const EnemyState& s){
    return s.type==kPracticeEnemyType && s.visible<2 && s.animation<1024
      && bounded(s.position.x,kMaxWorldCoordinate)&&bounded(s.position.y,kMaxWorldCoordinate)&&bounded(s.position.z,kMaxWorldCoordinate)
      && bounded(s.velocity.x,kMaxSpeed)&&bounded(s.velocity.y,kMaxSpeed)&&bounded(s.velocity.z,kMaxSpeed)
      && bounded(s.scale.x,10)&&bounded(s.scale.y,10)&&bounded(s.scale.z,10)&&s.scale.x>0&&s.scale.y>0&&s.scale.z>0
      && bounded(s.faceDirection,1000)&&bounded(s.tilt,1000)&&bounded(s.health,1000000)&&s.health>=0
      && bounded(s.animationFrame,1000000)&&s.animationFrame>=0
      && bounded(s.maxHealth,1000000)&&s.maxHealth>0&&s.health<=s.maxHealth;
}
std::vector<std::uint8_t> encodeEnemyState(const EnemyState& s){
    if(!validEnemyState(s))return {};
    ByteWriter w(kEnemyStateBytes);
    for(float f:{s.position.x,s.position.y,s.position.z,s.velocity.x,s.velocity.y,s.velocity.z,
                 s.scale.x,s.scale.y,s.scale.z,s.faceDirection,s.health,s.tilt,s.animationFrame,s.maxHealth})w.writeU32(bits(f));
    w.writeU16(s.animation);w.writeU8(s.type);w.writeU8(s.visible);
    return w.ok()?w.bytes():std::vector<std::uint8_t>{};
}
bool decodeEnemyState(const std::uint8_t* data,std::size_t size,EnemyState& output){
    if(!data||size!=kEnemyStateBytes)return false;
    ByteReader r(data,size);float f[14];for(float& n:f){std::uint32_t b=0;if(!r.readU32(b))return false;n=value(b);}
    EnemyState s;s.position={f[0],f[1],f[2]};s.velocity={f[3],f[4],f[5]};s.scale={f[6],f[7],f[8]};
    s.faceDirection=f[9];s.health=f[10];s.tilt=f[11];s.animationFrame=f[12];s.maxHealth=f[13];
    if(!r.readU16(s.animation)||!r.readU8(s.type)||!r.readU8(s.visible)||!validEnemyState(s))return false;
    output=s;return true;
}
EntityRecord enemyRecord(std::uint64_t value,const EnemyState& s){
    NetEntityId id;if(!NetEntityId::unpack(value,id)||id.kind!=EntityKind::Enemy)return {};
    auto data=encodeEnemyState(s);if(data.empty())return {};return {value,kEnemySchema,std::move(data)};
}
} // namespace nectar::net
