// Explicit asset-free diagnostic peer. Never linked into either game.
// A profile selects the PHONE build being tested; it is not a claim that this
// program runs that engine or has its assets. Never learns identity from a rejection.
#include "nectar_net/practice_bootstrap.h"
#include "nectar_net/secure_random.h"
#include "../../../games/pikmin1/pc_port/netplay/pc_coop_practice_input.h"
#include <chrono>
#include <cmath>
#include <cstdio>
#include <ctime>
#include <fstream>
#include <iostream>
#include <iterator>
#include <thread>
#ifdef _WIN32
#include <conio.h>
#endif
using namespace nectar::net;
namespace {
std::uint64_t clockMs() {return static_cast<std::uint64_t>(std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now().time_since_epoch()).count());}
std::uint64_t unixNow() {return static_cast<std::uint64_t>(std::time(nullptr));}
const char* phaseName(CoopPhase p) {
    switch(p) {case CoopPhase::Closed:return "closed";case CoopPhase::Loading:return "loading";
    case CoopPhase::WaitingForReady:return "waiting for Ready";case CoopPhase::Running:return "running";
    case CoopPhase::Paused:return "paused";case CoopPhase::WaitingForPartner:return "partner disconnected";}return "unknown";
}
bool profile(const std::string& file,CompatibilityInfo& info) {
    std::ifstream in(file);std::string text((std::istreambuf_iterator<char>(in)),{}),hex;
    if(!in || text.size()>4096)return false;
    for(char c:text) {if(c==' '||c=='\n'||c=='\r'||c=='\t')continue;hex+=c;}
    if(hex.size()!=kCompatibilityInfoBytes*2)return false;
    auto digit=[](char c)->int{if(c>='0'&&c<='9')return c-'0';if(c>='a'&&c<='f')return c-'a'+10;if(c>='A'&&c<='F')return c-'A'+10;return -1;};
    std::vector<std::uint8_t> bytes;
    for(std::size_t i=0;i<hex.size();i+=2){int a=digit(hex[i]),b=digit(hex[i+1]);if(a<0||b<0)return false;bytes.push_back(static_cast<std::uint8_t>(a*16+b));}
    if(!decodeCompatibilityInfo(bytes.data(),bytes.size(),info) || info.game!=1 || info.region!=1)return false;
    bool build=false,content=false;for(auto x:info.build)build|=x!=0;for(auto x:info.content)content|=x!=0;
    return build&&content&&(info.capabilities&0x30000)==0x30000&&(info.requiredCapabilities&0x30000)==0x30000;
}
// No actual game world: fixture ready means only the known two-captain test
// model/receiver is initialized. Phone practice still uses its real loading gate.
struct Peer {
    CoopConnection connection;
    PracticeBootstrap bootstrap{connection};
    CoopRole role=CoopRole::Guest;
    PcCoopPracticeInput input;
    bool failed=false,configured=false,attested=false,confirmed=false,firstReady=false,march=false,paused=false,away=false;
    std::uint64_t tick=0,frame=0,applied=0,lastPublish=0,lastStep=0,revision=0,moves=0;
    CaptainState captains[2];
    Peer(){captains[0].player=0;captains[0].position.x=-180;captains[1].player=1;captains[1].position.x=180;}
    bool start(CoopRole value,std::uint64_t now) {
        role=value;lastStep=now;
        if(value==CoopRole::Guest)return bootstrap.beginGuest(now);
        std::uint64_t id=0,seed=0;
        return secureRandomBytes(reinterpret_cast<std::uint8_t*>(&id),sizeof(id))&&id&&
            secureRandomBytes(reinterpret_cast<std::uint8_t*>(&seed),sizeof(seed))&&bootstrap.beginHost(id,seed,now);
    }
    void pump(std::uint64_t now) {
        if(failed)return;
        RoomStatus status;connection.maintain(now,unixNow(),status);bootstrap.pump(now);
        if(bootstrap.phase()==PracticeLoadPhase::Failed){failed=true;return;}
        if(bootstrap.phase()==PracticeLoadPhase::Loading&&!attested){
            attested=true;if(!bootstrap.worldLoaded(0,now)){failed=true;return;}
        }
        auto* s=connection.session();if(!s)return;
        if(!configured){if(role==CoopRole::Host&&!s->configureInputContinuousMask(PcCoopPracticeInput::Continuous)){failed=true;return;}configured=true;}
        s->pump(now);
        if(s->view().revision!=revision){revision=s->view().revision;input.reset();}
        if(role==CoopRole::Guest&&s->actors().frame>applied){applied=s->actors().frame;input.observe(s->actors().tick,now);if(!confirmed)confirmed=s->confirmWorldLoaded();}
        if(role==CoopRole::Host){
            // Fixed 30 Hz fixture, one step per pump: never catch up after sleep.
            if(now-lastStep>=33){lastStep=now;if(s->hostShouldAdvanceWorld()){
                NetInputFrame f;InputHealth health;++tick;s->consumeGuestInput(tick,f,health);
                if(f.stickX||f.stickY)++moves;
                captains[1].velocity={float(f.stickX)*1.5f,0,float(f.stickY)*1.5f};
                captains[1].position.x=std::clamp(captains[1].position.x+captains[1].velocity.x/30,-700.0f,700.0f);
                captains[1].position.z=std::clamp(captains[1].position.z+captains[1].velocity.z/30,-700.0f,700.0f);
            }}
            if(!frame||now-lastPublish>=CoopSession::kActorPeriodMs){
                std::vector<EntityRecord> records{captainRecord(static_cast<std::uint16_t>(bootstrap.scene().epoch),captains[0]),captainRecord(static_cast<std::uint16_t>(bootstrap.scene().epoch),captains[1])};
                for(std::uint32_t i=0;i<24;++i){PikminState p;p.owner=p.leader=static_cast<std::uint8_t>(i/12);p.color=static_cast<std::uint8_t>(i%3);p.health=10;
                    p.position=captains[p.owner].position;p.position.x+=float(int(i%3)-1)*24;p.position.z+=50+float((i%12)/3)*20;
                    records.push_back(pikminRecord(NetEntityId{static_cast<std::uint16_t>(bootstrap.scene().epoch),EntityKind::Pikmin,0,i+10}.pack(),p));}
                std::vector<std::vector<std::uint8_t>> packets;
                if(!packActorFrame(bootstrap.sessionId(),static_cast<std::uint16_t>(bootstrap.scene().epoch),frame+1,tick,records,kActorMaxPacketBytes,{},packets)){failed=true;return;}
                if(s->publishActors(packets,now)){++frame;lastPublish=now;if(!confirmed)confirmed=s->confirmWorldLoaded();}
            }
        }else if(s->canIssueCommands()){
            NetInputFrame f;
            if(march){switch((now/2000)%4){case 0:f.stickX=60;break;case 1:f.stickY=60;break;case 2:f.stickX=-60;break;default:f.stickY=-60;}}
            input.sample(f,now);TransportStats stats;int rtt=connection.stats(stats)?stats.rttMs:0;
            const auto bundle=input.bundle(now,rtt);if(!bundle.empty()&&s->publishInput(bundle,now))input.published(bundle,now);
        }
        if(confirmed&&!firstReady){firstReady=s->setReady(true);}
    }
    void command(char key){
        if(key=='m'){march=!march;std::puts(march?"PC guest walking pattern ON":"PC guest walking pattern OFF");return;}
        auto* s=connection.session();if(!s)return;
        if(key=='p'){paused=!paused;s->setBlocked(CoopBlock::Manual,paused);}
        if(key=='b'){away=!away;s->setBlocked(CoopBlock::Background,away);}
        if(key=='r')s->setReady(true);
    }
};
bool selfTest(){
    CompatibilityInfo id;id.game=1;id.region=1;id.build.fill(42);id.content.fill(73);id.capabilities=id.requiredCapabilities=0x30000;
    auto host=std::make_unique<HostRoom>(defaultTransportFactory(),PublisherBackends{});
    RoomConfig cfg;cfg.compatibility=id;cfg.automaticPortMapping=false;cfg.includeLanEndpoint=false;cfg.listenAddress="127.0.0.1";
    RoomStatus status;bool opened=false;
    for(std::uint16_t port=40070;port<40080&&!opened;++port){cfg.localPort=port;DirectEndpoint e;e.address={127,0,0,1};e.port=port;cfg.manualEndpoints={e};opened=host->open(cfg,unixNow(),status)==RoomError::None;}
    if(!opened)return false;
    auto guest=std::make_unique<GuestJoin>();if(guest->start(status.code,id,1,unixNow(),clockMs())!=JoinFailure::None)return false;
    Peer h,g;auto end=clockMs()+10000;bool joined=false;
    while(clockMs()<end){TransportEvent e;while(host->transport()->poll(e)){}bool has=false;guest->poll(clockMs(),e,has);
        if(host->transport()->state()==TransportState::Connected&&guest->transport()&&guest->transport()->state()==TransportState::Connected){joined=true;break;}
        std::this_thread::sleep_for(std::chrono::milliseconds(2));}
    if(!joined||!h.connection.adoptHost(host)||!h.start(CoopRole::Host,clockMs()))return false;
    // The phone may enter practice well before the PC transfers room ownership.
    const auto delayed=clockMs()+350;
    while(clockMs()<delayed){h.pump(clockMs());TransportEvent e;bool has=false;
        if(guest->poll(clockMs(),e,has)!=JoinProgress::Connected)return false;
        if(has&&e.type==TransportEventType::Message&&!g.connection.bufferBeforeHandoff(std::move(e)))return false;
        std::this_thread::sleep_for(std::chrono::milliseconds(2));}
    if(!g.connection.adoptGuest(guest)||!g.start(CoopRole::Guest,clockMs()))return false;
    auto until=[&](auto done){const auto limit=clockMs()+7000;do{const auto n=clockMs();h.pump(n);g.pump(n);if(h.failed||g.failed)return false;if(done())return true;std::this_thread::sleep_for(std::chrono::milliseconds(2));}while(clockMs()<limit);return false;};
    if(!until([&]{return h.connection.session()&&g.connection.session()&&h.connection.session()->hostShouldAdvanceWorld()&&g.connection.session()->canIssueCommands();}))return false;
    std::puts("PASS authenticated room, staggered bootstrap, baseline and ready");
    g.march=true;
    if(!until([&]{return h.moves>=5&&g.connection.session()->actors().pikmin.size()==24;}))return false;
    std::puts("PASS guest input reaches fixture host; 24 test Pikmin reach guest");
    g.command('p');if(!until([&]{return h.connection.session()->phase()==CoopPhase::Paused;}))return false;
    const auto held=h.tick;for(int i=0;i<100;++i){h.pump(clockMs());g.pump(clockMs());std::this_thread::sleep_for(std::chrono::milliseconds(2));}if(h.tick!=held)return false;
    g.command('p');if(!until([&]{return h.tick>held;}))return false;
    std::puts("PASS pause freezes fixture ticks and resume works");
    g.command('b');if(!until([&]{return h.connection.session()->phase()==CoopPhase::Paused&&!h.connection.session()->view().ready[1];}))return false;
    g.command('b');if(!until([&]{return h.connection.session()->phase()==CoopPhase::WaitingForReady;}))return false;
    g.command('r');if(!until([&]{return h.connection.session()->hostShouldAdvanceWorld();}))return false;
    std::puts("PASS interruption requires explicit Ready before continuing");
    g.connection.close();if(!until([&]{return h.connection.session()->phase()==CoopPhase::WaitingForPartner;}))return false;
    const auto stopped=h.tick;h.pump(clockMs()+100);if(h.tick!=stopped)return false;
    std::puts("PASS disconnect holds fixture world");return true;
}
}
int main(int argc,char** argv){
    std::setvbuf(stdout,nullptr,_IONBF,0);
    if(argc==2&&std::string(argv[1])=="--self-test"){bool ok=selfTest();std::puts(ok?"COMPANION SELF TEST PASS":"COMPANION SELF TEST FAIL");return ok?0:1;}
    if(argc==3&&std::string(argv[1])=="--validate-profile"){CompatibilityInfo id;bool ok=profile(argv[2],id);std::puts(ok?"PROFILE PASS":"PROFILE FAIL");return ok?0:2;}
    if(argc!=3||(std::string(argv[1])!="--host"&&std::string(argv[1])!="--join")){std::puts("Usage: nectar_practice_companion --host|--join profile.identity\nDiagnostic fixture only: no campaign, AI, graphics or save files.");return 2;}
    CompatibilityInfo id;if(!profile(argv[2],id)){std::puts("Profile invalid. Use a prepared profile matching the installed P1 build.");return 2;}
    Peer peer;std::unique_ptr<HostRoom> host;std::unique_ptr<GuestJoin> guest;RoomStatus status;
    const bool hosting=std::string(argv[1])=="--host";
    std::puts("P1 PC TEST PARTNER - diagnostic scene only, no campaign saves.\nUse the SAME Wi-Fi/LAN as your phone. Close this helper to disconnect.\nKeys: M toggle PC guest walking, P pause/unpause, B simulate away/back, R Ready, Q quit.");
    if(hosting){host=std::make_unique<HostRoom>();RoomConfig cfg;cfg.compatibility=id;cfg.automaticPortMapping=false;
        if(host->open(cfg,unixNow(),status)!=RoomError::None){std::puts("Could not host. Check the PC network and firewall.");return 1;}
        // Invite displayed locally by explicit host action; never printed by self-test.
        std::puts("Copy this PRIVATE code to your phone (do not share screenshots publicly):");std::puts(status.code.c_str());
    }else{std::puts("Paste the phone's complete private room code, then press Enter:");std::string code;std::getline(std::cin,code);
        if(code.size()>4096){std::puts("Code too long.");return 2;}guest=std::make_unique<GuestJoin>();
        auto error=guest->start(code,id,1,unixNow(),clockMs());std::fill(code.begin(),code.end(),'\0');
        if(error!=JoinFailure::None){std::printf("Join failed: %s\n",joinFailureString(error));return 1;}}
    bool adopted=false;auto started=clockMs(),lastReport=started;
    while(clockMs()-started<600000){const auto now=clockMs();
#ifdef _WIN32
        if(_kbhit()){const int key=_getch();if(key=='q'||key=='Q')break;peer.command(static_cast<char>(key>='A'&&key<='Z'?key+32:key));}
#endif
        if(!adopted){TransportEvent e;
            if(host){while(host->transport()->state()!=TransportState::Connected&&host->transport()->poll(e)){}if(host->transport()->state()==TransportState::Connected)adopted=peer.connection.adoptHost(host);}
            else{bool has=false;auto progress=guest->poll(now,e,has);if(has&&e.type==TransportEventType::Message&&!peer.connection.bufferBeforeHandoff(std::move(e))){std::puts("Could not retain early practice message.");return 1;}
                if(progress==JoinProgress::Failed){std::printf("Join failed: %s (%s). Check the chosen PHONE build profile.\n",joinFailureString(guest->failure()),compatibilityFieldString(guest->incompatibility()));return 1;}
                if(progress==JoinProgress::Connected)adopted=peer.connection.adoptGuest(guest);}
            if(adopted){if(!peer.start(hosting?CoopRole::Host:CoopRole::Guest,now)){std::puts("Could not begin diagnostic practice.");return 1;}std::puts("Connected. On the phone tap Start Co-op Practice, then Ready / Resume when available.");}
        }else peer.pump(now);
        if(peer.failed){std::puts("Practice loading failed or timed out. Close/reopen phone P1 and retry; no campaign saved.");return 1;}
        if(now-lastReport>=1000){lastReport=now;auto* s=peer.connection.session();if(s){TransportStats stats;peer.connection.stats(stats);
            std::printf("%s | delay %d ms | fixture tick %llu | received picture %llu | input ticks %llu\n",phaseName(s->phase()),stats.rttMs,static_cast<unsigned long long>(peer.tick),static_cast<unsigned long long>(s->actors().frame),static_cast<unsigned long long>(s->receivedGuestInputTick()));
            if(s->phase()==CoopPhase::WaitingForPartner){std::puts("Partner disconnected; world held. Reopen phone P1 and restart this helper for another test.");return 0;}
        }else if(!adopted)std::puts("Waiting for connection...");}
        std::this_thread::sleep_for(std::chrono::milliseconds(2));
    }
    std::puts("PC test partner closed (10-minute safety limit or Quit). No campaign was saved.");return 0;
}
