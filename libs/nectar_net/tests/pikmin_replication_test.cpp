#include "nectar_net/pikmin_replication.h"
#include <cstdio>
#include <limits>
#include <cstring>
using namespace nectar::net;
int bad = 0;
void check(bool ok, const char* what) { if (!ok) { std::printf("FAIL %s\n", what); ++bad; } }
int main()
{
    PikminState s;s.position={1,2,3};s.velocity={4,5,6};s.health=100;s.owner=1;s.leader=0;s.color=2;s.maturity=2;s.action=9;
    auto bytes=encodePikminState(s);PikminState out;
    check(bytes.size()==38 && bytes[0]==0x3f && bytes[1]==0x80, "fixed network byte order, no native padding");
    check(decodePikminState(bytes.data(),bytes.size(),out) && out.position.z==3 && out.owner==1
          && out.leader==0 && out.health==100 && out.action==9, "fields round trip");
    for(std::size_t n=0;n<bytes.size();++n) check(!decodePikminState(bytes.data(),n,out), "every truncation rejected");
    auto extra=bytes;extra.push_back(0);check(!decodePikminState(extra.data(),extra.size(),out),"trailing byte rejected");
    check(!decodePikminState(nullptr,38,out),"null input rejected");
    const auto id=NetEntityId{5,EntityKind::Pikmin,0,1}.pack();
    auto record=pikminRecord(id,s);check(record.id==id && record.schema==1 && record.data==bytes,"record contains stable ID and schema");
    check(!pikminRecord(NetEntityId{5,EntityKind::Enemy,0,1}.pack(),s).id,"wrong entity kind rejected");
    for(const float f:{std::numeric_limits<float>::quiet_NaN(),std::numeric_limits<float>::infinity(),100001.0f}) {
        auto invalid=s;invalid.position.x=f;check(encodePikminState(invalid).empty(),"bad host position refused");
        auto wire=bytes;std::uint32_t bits=0;std::memcpy(&bits,&f,4);
        for(int n=0;n<4;++n) wire[static_cast<std::size_t>(n)]=static_cast<std::uint8_t>(bits>>(24-8*n));
        const auto before=out.position.x;check(!decodePikminState(wire.data(),wire.size(),out)&&out.position.x==before,"invalid input doesn't partially overwrite state");
    }
    for(int field=0;field<5;++field) {auto invalid=s;
        if(field==0)invalid.owner=2;if(field==1)invalid.leader=2;if(field==2)invalid.color=5;
        if(field==3)invalid.maturity=3;if(field==4)invalid.action=256;
        check(encodePikminState(invalid).empty(),"unknown metadata refused");}
    s.owner=255;s.leader=255;check(!encodePikminState(s).empty(),"unclaimed/idle is explicit");
    s.health=-1;check(encodePikminState(s).empty(),"negative health refused");
    if(!bad)std::puts("PASS Pikmin wire state: endian/size, IDs, metadata, malformed/truncated/NaN and atomic decoding");
    return bad?1:0;
}
