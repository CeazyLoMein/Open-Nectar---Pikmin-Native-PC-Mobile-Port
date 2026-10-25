#include "nectar_net/actor_frame.h"
#include "nectar_net/byte_io.h"
#include <algorithm>
#include <array>
#include <limits>

namespace nectar::net {
namespace {
constexpr std::uint32_t kMagic=0x4e434631; // NCF1, versioned prototype actor frame
constexpr std::size_t kHardBytes=1024*1024, kHardFragments=2048;
bool validLimits(const ActorFrameLimits& l) {
    return l.maxFrameBytes>=3 && l.maxFrameBytes<=kHardBytes && l.maxRecords>0 && l.maxRecords<=4096
        && l.maxFragments>0 && l.maxFragments<=kHardFragments && l.timeoutMs>0 && l.timeoutMs<=60000;
}
// Detect accidental cross-frame corruption; NOT authentication or a MAC.
std::uint64_t checksum(const std::vector<std::uint8_t>& data) {
    std::uint64_t h=14695981039346656037ULL;
    for(auto b:data) { h^=b; h*=1099511628211ULL; }
    return h;
}
bool actors(const std::vector<EntityRecord>& records, std::uint16_t epoch, ActorFrame& frame) {
    ActorFrame pending;
    std::array<bool,2> players{};
    std::map<std::uint64_t,bool> ids;
    for(const auto& r:records) {
        NetEntityId id;
        if(!NetEntityId::unpack(r.id,id) || id.sceneEpoch!=epoch || !ids.emplace(r.id,true).second) return false;
        if(id.kind==EntityKind::Captain && r.schema==kCaptainSchema) {
            CaptainState s;
            if(!decodeCaptainState(r.data.data(),r.data.size(),s) || players[s.player]) return false;
            players[s.player]=true; pending.captains.emplace(r.id,s);
        } else if(id.kind==EntityKind::Pikmin && r.schema==kPikminSchema) {
            PikminState s;
            if(!decodePikminState(r.data.data(),r.data.size(),s)) return false;
            pending.pikmin.emplace(r.id,s);
        } else return false; // add other entity schemas explicitly in a later milestone
    }
    if(!players[0]) return false;
    for(const auto& p:pending.pikmin) {
        const auto& s=p.second;
        if(s.leader!=255 && !players[s.leader]) return false;
        if(s.owner!=255 && !players[s.owner]) return false;
    }
    frame=std::move(pending); return true;
}
struct Header {
    std::uint64_t session=0,frame=0,tick=0,hash=0;
    std::uint32_t bytes=0;
    std::uint16_t epoch=0,index=0,parts=0;
};
bool readHeader(const std::uint8_t* data,std::size_t size,const ActorFrameLimits& limits,Header& h) {
    if(!data || size<=kActorFragmentHeaderBytes || size>kActorMaxPacketBytes) return false;
    ByteReader r(data,size); std::uint32_t magic=0; std::uint8_t version=0,flags=0;
    if(!r.readU32(magic)||!r.readU8(version)||!r.readU8(flags)||!r.readU16(h.epoch)
       ||!r.readU64(h.session)||!r.readU64(h.frame)||!r.readU64(h.tick)||!r.readU32(h.bytes)
       ||!r.readU64(h.hash)||!r.readU16(h.index)||!r.readU16(h.parts)) return false;
    if(magic!=kMagic || version!=1 || flags!=kWorldDeltaKeyframe || !h.session || !h.epoch || !h.frame
       || h.bytes<3 || h.bytes>limits.maxFrameBytes || !h.parts || h.parts>limits.maxFragments
       || h.parts>h.bytes || h.index>=h.parts) return false;
    const std::size_t stride=(h.bytes+h.parts-1)/h.parts;
    const std::size_t offset=stride*h.index;
    // Refuse impossible/noncanonical part counts before any allocation.
    if(stride>kActorMaxPacketBytes-kActorFragmentHeaderBytes || stride*(h.parts-1)>=h.bytes || offset>=h.bytes) return false;
    return r.remaining()==std::min(stride,static_cast<std::size_t>(h.bytes)-offset);
}
} // namespace

bool packActorFrame(std::uint64_t session,std::uint16_t epoch,std::uint64_t frame,
                    std::uint64_t tick,const std::vector<EntityRecord>& records,
                    std::size_t budget,const ActorFrameLimits& limits,
                    std::vector<std::vector<std::uint8_t>>& packets) {
    if(!session || !epoch || !frame || !validLimits(limits) || budget<=kActorFragmentHeaderBytes
       || budget>kActorMaxPacketBytes || records.size()>limits.maxRecords) return false;
    std::size_t bytes=3;
    for(const auto& r:records) {
        if(r.data.size()>1024 || bytes+11+r.data.size()>limits.maxFrameBytes) return false;
        bytes+=11+r.data.size();
    }
    ActorFrame validated;
    if(!actors(records,epoch,validated)) return false;
    const auto body=encodeWorldDelta(kWorldDeltaKeyframe,records);
    if(body.empty() || body.size()!=bytes) return false;
    const auto capacity=budget-kActorFragmentHeaderBytes;
    const std::size_t parts=(bytes+capacity-1)/capacity;
    if(parts>limits.maxFragments) return false;
    const auto stride=(bytes+parts-1)/parts;
    // Extremely small budgets can produce redundant parts after balancing.
    // Use exact fixed capacity chunks instead by refusing noncanonical geometry.
    if(stride*(parts-1)>=bytes) return false;
    const auto hash=checksum(body);
    std::vector<std::vector<std::uint8_t>> result;
    result.reserve(parts);
    for(std::size_t i=0;i<parts;++i) {
        const auto offset=i*stride;
        const auto count=std::min(stride,bytes-offset);
        ByteWriter w(kActorFragmentHeaderBytes+count);
        w.writeU32(kMagic);w.writeU8(1);w.writeU8(kWorldDeltaKeyframe);w.writeU16(epoch);
        w.writeU64(session);w.writeU64(frame);w.writeU64(tick);w.writeU32(static_cast<std::uint32_t>(bytes));
        w.writeU64(hash);w.writeU16(static_cast<std::uint16_t>(i));w.writeU16(static_cast<std::uint16_t>(parts));
        w.writeBytes(body.data()+offset,count);
        if(!w.ok()) return false;
        result.push_back(w.bytes());
    }
    packets.swap(result);return true;
}

bool ActorFrameReceiver::begin(std::uint64_t session,std::uint16_t epoch) {
    if(!session || !epoch || !validLimits(mLimits)) return false;
    end();mSession=session;mEpoch=epoch;return true;
}
void ActorFrameReceiver::end() {mSession=0;mEpoch=0;mSeenFrame=0;mCurrent=ActorFrame{};mPending=Pending{};}
void ActorFrameReceiver::expire(std::uint64_t now) {
    if(mPending.frame && (now<mPending.started || now-mPending.started>=mLimits.timeoutMs)) mPending=Pending{};
}
ActorFrameReceiver::Result ActorFrameReceiver::receive(const std::uint8_t* data,std::size_t size,std::uint64_t now) {
    if(!mSession) return Result::Rejected;
    expire(now);
    Header h;
    if(!readHeader(data,size,mLimits,h)) return Result::Rejected;
    if(h.session!=mSession || h.epoch!=mEpoch || h.frame<mSeenFrame || h.frame<=mCurrent.frame || h.tick<mCurrent.tick) return Result::Ignored;
    if(h.frame==mSeenFrame && !mPending.frame) return Result::Ignored; // expired/rejected frame cannot restart
    if(h.frame>mSeenFrame) {
        Pending pending;pending.frame=h.frame;pending.tick=h.tick;pending.checksum=h.hash;
        pending.started=now;pending.bytes=h.bytes;pending.parts=h.parts;
        pending.body.resize(h.bytes);pending.seen.resize(h.parts);
        mPending=std::move(pending);mSeenFrame=h.frame;
    }
    auto& p=mPending;
    if(h.tick!=p.tick || h.bytes!=p.bytes || h.parts!=p.parts || h.hash!=p.checksum) return Result::Rejected;
    const std::size_t stride=(h.bytes+h.parts-1)/h.parts;
    const auto offset=stride*h.index;
    const auto count=size-kActorFragmentHeaderBytes;
    const auto* begin=data+kActorFragmentHeaderBytes;
    if(p.seen[h.index]) {
        if(!std::equal(begin,begin+count,p.body.begin()+offset)) return Result::Rejected;
        return Result::Buffered;
    }
    std::copy(begin,begin+count,p.body.begin()+offset);p.seen[h.index]=1;++p.received;
    if(p.received<p.parts) return Result::Buffered;
    std::uint8_t flags=0;std::vector<EntityRecord> records;ActorFrame decoded;
    const bool valid=checksum(p.body)==p.checksum
        && decodeWorldDelta(p.body.data(),p.body.size(),mEpoch,{mLimits.maxRecords,1024},flags,records)
        && flags==kWorldDeltaKeyframe && actors(records,mEpoch,decoded);
    if(!valid) {mPending=Pending{};return Result::Rejected;}
    decoded.frame=p.frame;decoded.tick=p.tick;
    mCurrent=std::move(decoded);mPending=Pending{};return Result::Committed;
}
} // namespace nectar::net
