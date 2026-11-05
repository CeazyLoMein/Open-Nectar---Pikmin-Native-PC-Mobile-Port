// Actual production adapter, controlled router API. Not a network/router test.
#include "../src/upnp_client.cpp"
int main(){
    using namespace nectar::net;
    auto client=createUpnpClient();
    if(client->discover(1)!=MappingError::None)return 1;
    Ipv4Address address{};std::uint32_t lease=0;
    if(client->addMapping(50000,50000,7200,address,lease)!=MappingError::None || lease!=7200 || fakeAdds!=1 || std::strcmp(fakeLease,"7200"))return 2;
    fakeAddResult=725;fakeAdds=0;
    if(client->addMapping(50000,50000,7200,address,lease)!=MappingError::Refused || fakeAdds!=1 || std::strcmp(fakeLease,"7200"))return 3;
    fakeAddResult=606;
    if(client->addMapping(50000,50000,7200,address,lease)!=MappingError::NotAuthorized)return 4;
    fakeAddResult=0;fakeAddress="not-an-address";fakeDeletes=0;
    if(client->addMapping(50000,50000,7200,address,lease)!=MappingError::NetworkFailure || fakeDeletes!=1)return 5;
    std::puts("PASS actual UPnP adapter: temporary lease, permanent refusal, router denial, invalid route cleanup");return 0;
}
