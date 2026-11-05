#include "nectar_net/async_port_publisher.h"
#include "nectar_net/room.h"
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <cstdio>
#include <mutex>
#include <stdexcept>
#include <thread>
using namespace nectar::net;
using namespace std::chrono_literals;
namespace {
int failures=0;
void check(bool value,const char* why){if(!value){std::printf("FAIL %s\n",why);++failures;}}
struct Shared {
    std::mutex mutex;std::condition_variable wake;
    bool block=false,entered=false,release=false,throwDiscovery=false;
    unsigned removed=0,destroyed=0;
    Ipv4Address address{8,8,8,8};
};
class Upnp final:public IUpnpClient {
    std::shared_ptr<Shared> state;
public:
    explicit Upnp(std::shared_ptr<Shared> value):state(std::move(value)){}
    ~Upnp()override{std::lock_guard<std::mutex> l(state->mutex);++state->destroyed;state->wake.notify_all();}
    MappingError discover(std::uint32_t)override{
        std::unique_lock<std::mutex> l(state->mutex);
        state->entered=true;state->wake.notify_all();
        if(state->block)state->wake.wait(l,[&]{return state->release;});
        if(state->throwDiscovery)throw std::runtime_error("fake discovery exception");
        return MappingError::None;
    }
    MappingError addMapping(std::uint16_t,std::uint16_t,std::uint32_t,
        Ipv4Address& address,std::uint32_t& lease)override{
        address=state->address;lease=7200;return MappingError::None;
    }
    MappingError deleteMapping(std::uint16_t)override{
        std::lock_guard<std::mutex> l(state->mutex);++state->removed;state->wake.notify_all();return MappingError::None;
    }
};
PublisherBackends backend(std::shared_ptr<Shared> s){
    PublisherBackends b;b.openUpnp=[s]{return std::make_unique<Upnp>(s);};
    b.listAddresses=[] {LocalAddresses a;a.ipv4.push_back({192,168,1,2});return a;};
    b.randomBytes=[](std::uint8_t* p,std::size_t n){for(std::size_t i=0;i<n;++i)p[i]=static_cast<std::uint8_t>(i+1);return true;};
    return b;
}
bool await(AsyncPortPublisher& p,PublishResult& r,bool& failed){
    const auto until=std::chrono::steady_clock::now()+2s;
    do {if(p.take(r,failed))return true;std::this_thread::sleep_for(1ms);}while(std::chrono::steady_clock::now()<until);
    return false;
}
void completed(){
    auto shared=std::make_shared<Shared>();PublishResult result;bool failed=true;
    {
        AsyncPortPublisher p(backend(shared),50000,true);
        check(await(p,result,failed)&&!failed&&result.reachability==Reachability::Public,"background mapping publishes a route");
        check(result.endpoints.size()==2,"public route and private Wi-Fi fallback retained");
        check(!p.take(result,failed),"mailbox result consumed once");
        for(unsigned i=0;i<10000;++i)p.tick(i); // bounded coalesced work, not an unbounded queue
    }
    std::unique_lock<std::mutex> lock(shared->mutex);
    check(shared->wake.wait_for(lock,2s,[&]{return shared->destroyed==1;})&&shared->removed==1,"lease is retired exactly once on worker close");
}
void cancellation(){
    auto shared=std::make_shared<Shared>();shared->block=true;
    auto p=std::make_unique<AsyncPortPublisher>(backend(shared),50001,true);
    {
        std::unique_lock<std::mutex> l(shared->mutex);
        check(shared->wake.wait_for(l,2s,[&]{return shared->entered;}),"discovery entered controlled block");
    }
    PublishResult result;bool failed=false;check(!p->take(result,failed),"pending discovery is never reported successful");
    // Watchdog prevents a broken blocking destructor from hanging the suite.
    std::thread release([shared]{std::unique_lock<std::mutex> l(shared->mutex);shared->wake.wait_for(l,1s,[&]{return shared->release;});shared->release=true;shared->wake.notify_all();});
    const auto before=std::chrono::steady_clock::now();p.reset();
    check(std::chrono::steady_clock::now()-before<500ms,"cancel returns while router is still blocked");
    {std::lock_guard<std::mutex> l(shared->mutex);shared->release=true;shared->wake.notify_all();}
    release.join();
    std::unique_lock<std::mutex> l(shared->mutex);
    check(shared->wake.wait_for(l,2s,[&]{return shared->destroyed==1;})&&shared->removed==1,"late canceled mapping is cleaned instead of leaked");
}
void failedAndUnsupported(){
    auto shared=std::make_shared<Shared>();shared->throwDiscovery=true;
    {AsyncPortPublisher p(backend(shared),50002,true);PublishResult result;bool failed=false;
     check(await(p,result,failed)&&failed,"worker exception becomes explicit failure without escaping game thread");}
    auto cgnat=std::make_shared<Shared>();cgnat->address={100,64,0,1};
    {AsyncPortPublisher p(backend(cgnat),50003,true);PublishResult result;bool failed=false;
     check(await(p,result,failed)&&!failed&&result.reachability==Reachability::BehindCgnat,"carrier NAT is not advertised as public");
     check(result.endpoints.size()==1,"unusable mapped address excluded, Wi-Fi fallback retained");}
    RoomStatus status;
    for(auto scope:{Reachability::Public,Reachability::Ipv6Only,Reachability::BehindCgnat,Reachability::NoAutomaticMapping}){
        status.reachability=scope;
        check(hostRoomStatusText(status,true)[0]!=0,"each internet route has player-facing status");
    }
    status.checkingInternet=true;check(std::string(hostRoomStatusText(status,true)).find("Checking")!=std::string::npos,"pending status stays distinct from reachable");
    check(std::string(hostRoomStatusText(status,false)).find("same network")!=std::string::npos,"Wi-Fi mode remains explicitly local");
}
}
int main(){completed();cancellation();failedAndUnsupported();std::printf("Async router setup/cleanup: %s\n",failures?"FAIL":"PASS");return failures?1:0;}
