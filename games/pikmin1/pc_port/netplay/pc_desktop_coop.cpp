// Full Windows game frontend for the SAME retained-room/practice engine as iOS.
// No diagnostic identity profiles, relaunch into legacy online, or foreign saves.
#ifndef NOMINMAX
#define NOMINMAX
#endif
#include <windows.h>
#include "netplay/pc_desktop_coop.h"
#include "netplay/pc_desktop_content_identity.h"
#include "netplay/pc_coop_practice_bridge.h"
#include "nectar_net/coop_connection.h"
#include "nectar_coop_build_identity.h"
#include <chrono>
#include <ctime>
#include <future>
#include <string>
using namespace nectar::net;
namespace {
HWND room=nullptr,panel=nullptr,codeBox=nullptr,roomStatus=nullptr,practiceStatus=nullptr,game=nullptr;
std::unique_ptr<HostRoom> host;std::unique_ptr<GuestJoin> guest;
std::unique_ptr<CoopConnection> handoff;
CompatibilityInfo identity;bool checked=false,hashing=false;
std::future<bool> hashJob;std::array<std::uint8_t,32> content{};
std::uint64_t lastStatus=0;
std::uint64_t nowMs(){return static_cast<std::uint64_t>(std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now().time_since_epoch()).count());}
void status(const char* text){if(roomStatus)SetWindowTextA(roomStatus,text);}
void stop(){if(handoff)handoff->close();if(guest)guest->cancel();if(host)host->close();guest.reset();host.reset();if(codeBox)SetWindowTextA(codeBox,"");}
void resume(){
    if(game){SetForegroundWindow(game);SetFocus(game);}
    if(GetForegroundWindow()==game){pc_coop_practice_background(false);if(pc_coop_practice_ready())ShowWindow(panel,SW_HIDE);}
}
void action(int id){
    if(id==7){ShowWindow(room,SW_HIDE);if(game)SetForegroundWindow(game);return;}
    if(id==8){stop();status("Room closed. Host or join again.");return;}
    if(id==10){resume();return;}
    if(id==11){ShowWindow(panel,SW_HIDE);if(game)SetForegroundWindow(game);return;}
    if(id==12){if(pc_coop_practice_leave())ShowWindow(panel,SW_HIDE);return;}
    if(!checked){status("Wait for the base game-data check to finish.");return;}
    if(id==1){
        if(host||guest)return;host=std::make_unique<HostRoom>();RoomConfig c;c.compatibility=identity;c.automaticPortMapping=false;
        RoomStatus s;if(host->open(c,static_cast<std::uint64_t>(std::time(nullptr)),s)!=RoomError::None){stop();status("Could not host. Check home network and private firewall permission.");return;}
        SetWindowTextA(codeBox,s.code.c_str());status("Room open. Copy code to your partner. Both games need the SAME new PC/iPhone update.");
    }else if(id==2){
        if(host||guest)return;char value[4097]={};if(GetWindowTextLengthA(codeBox)>4096){status("Code too long.");return;}
        GetWindowTextA(codeBox,value,sizeof(value));guest=std::make_unique<GuestJoin>();
        if(guest->start(value,identity,1,static_cast<std::uint64_t>(std::time(nullptr)),nowMs())!=JoinFailure::None){stop();status("Invalid or expired room code.");}
        SecureZeroMemory(value,sizeof(value));
    }else if(id==3){SendMessageW(codeBox,EM_SETSEL,0,-1);SendMessageW(codeBox,WM_COPY,0,0);
    }else if(id==4){if(!host&&!guest){SetFocus(codeBox);SendMessageW(codeBox,WM_PASTE,0,0);}
    }else if(id==5){
        if(!pc_coop_practice_can_enter()){status("Return to the title screen first. Ending admitted practice may require reopening P1.");return;}
        auto connection=std::move(handoff);bool ok=host?connection->adoptHost(host):connection->adoptGuest(guest);
        if(!ok){handoff=std::move(connection);status("Connect both devices before starting practice.");return;}
        handoff=std::make_unique<CoopConnection>();
        // The SAME owner carries early authenticated scene messages across handoff.
        if(pc_coop_practice_adopt(connection)){ShowWindow(room,SW_HIDE);if(game)SetForegroundWindow(game);}else{connection->close();status("Could not start practice safely.");}
    }
}
LRESULT CALLBACK procedure(HWND window,UINT msg,WPARAM w,LPARAM l){
    if(msg==WM_COMMAND){action(LOWORD(w));return 0;}
    if(msg==WM_CLOSE){if(window==room)ShowWindow(room,SW_HIDE);else ShowWindow(panel,SW_HIDE);if(game)SetForegroundWindow(game);return 0;}
    return DefWindowProcW(window,msg,w,l);
}
HWND createWindow(bool practice){
    WNDCLASSW c{};c.lpfnWndProc=procedure;c.hInstance=GetModuleHandleW(nullptr);c.lpszClassName=L"NectarFullGameCoop";
    c.hCursor=LoadCursorW(nullptr,MAKEINTRESOURCEW(32512));c.hbrBackground=reinterpret_cast<HBRUSH>(COLOR_WINDOW+1);RegisterClassW(&c);
    return CreateWindowW(c.lpszClassName,practice?L"Pikmin 1 - Online practice":L"Pikmin 1 - Online Co-op",WS_OVERLAPPED|WS_CAPTION|WS_SYSMENU|WS_MINIMIZEBOX,CW_USEDEFAULT,CW_USEDEFAULT,760,420,game,nullptr,c.hInstance,nullptr);
}
HWND label(HWND parent,const char* text,int y,int height){return CreateWindowA("STATIC",text,WS_CHILD|WS_VISIBLE,20,y,700,height,parent,nullptr,nullptr,nullptr);}
void button(HWND parent,const char* text,int x,int y,int id,int width=160){CreateWindowA("BUTTON",text,WS_CHILD|WS_VISIBLE|WS_TABSTOP,x,y,width,38,parent,reinterpret_cast<HMENU>(static_cast<INT_PTR>(id)),nullptr,nullptr);}
}
// These ABI entry names are shared with existing title hooks, despite the old
// iOS prefix. This module is Windows-only and does not link UIKit.
extern "C" void nectar_ios_open_coop_room(){
    if(!handoff)handoff=std::make_unique<CoopConnection>();
    if(!game)game=GetForegroundWindow();
    if(!room){
        room=createWindow(false);label(room,"Same-LAN PC / iPhone practice. Each device renders the full game. Campaign play and recovery are still being developed.",15,45);
        roomStatus=label(room,"Checking immutable base game data...",65,60);
        codeBox=CreateWindowA("EDIT","",WS_CHILD|WS_VISIBLE|WS_BORDER|ES_MULTILINE|ES_AUTOVSCROLL|WS_TABSTOP,20,130,700,65,room,nullptr,nullptr,nullptr);
        SendMessageW(codeBox,EM_SETLIMITTEXT,4096,0);
        button(room,"Host Room",20,210,1);button(room,"Join Room",200,210,2);button(room,"Copy Code",380,210,3);button(room,"Paste Code",560,210,4);
        button(room,"Start Co-op Practice",20,270,5,220);button(room,"Leave Room",260,270,8,200);button(room,"Return to Game",480,270,7,240);
        label(room,"Personal graphics and controls stay local. Use matching new builds. No campaign progress is saved by practice.",330,45);
        hashing=true;const auto root=std::filesystem::current_path()/"dataDir";
        hashJob=std::async(std::launch::async,[root]{return nectar_desktop::contentIdentity(root,content);});
    }
    ShowWindow(room,SW_SHOW);SetForegroundWindow(room);
}
extern "C" int nectar_ios_coop_room_is_open(){return room&&IsWindowVisible(room);}
extern "C" void nectar_desktop_open_coop_practice(){
    if(!panel){panel=createWindow(true);label(panel,"Online Co-op - Practice",20,30);practiceStatus=label(panel,"Loading...",65,120);
        button(panel,"Ready / Resume",20,230,10,220);button(panel,"View Practice Area",260,230,11,220);button(panel,"End Practice",500,230,12,220);
        label(panel,"Ending practice after save isolation requires closing and reopening P1. Solo saves remain separate.",300,55);}
    ShowWindow(panel,SW_SHOW);SetForegroundWindow(panel);
}
extern "C" void nectar_desktop_coop_pump(){
    MSG msg;while(PeekMessageW(&msg,nullptr,0,0,PM_REMOVE)){TranslateMessage(&msg);DispatchMessageW(&msg);}
    if(hashing&&hashJob.wait_for(std::chrono::seconds(0))==std::future_status::ready){
        checked=hashJob.get();hashing=false;
        if(checked){identity.game=1;identity.region=1;identity.build=nectar_ios::coop_build_identity;identity.content=content;identity.capabilities=identity.requiredCapabilities=0x30000;status("Ready. Host a private room or paste a code from the matching game update.");}
        else status("Base data verification failed. Launch from the prepared game folder with its original dataDir.");
    }
    const auto now=nowMs();
    if(host){RoomStatus s;host->maintain(now,static_cast<std::uint64_t>(std::time(nullptr)),s);TransportEvent e;
        for(int n=0;n<64&&host->transport()->poll(e);++n){if(e.type==TransportEventType::Message){if(!handoff->bufferBeforeHandoff(std::move(e))){stop();status("Too many early messages. Retry the room.");break;}}}}
    if(guest){TransportEvent e;bool has=false;const auto progress=guest->poll(now,e,has);
        if(has&&e.type==TransportEventType::Message&&!handoff->bufferBeforeHandoff(std::move(e))){stop();status("Early practice message could not be retained.");}
        else if(progress==JoinProgress::Failed){std::string text="Join failed: "+std::string(joinFailureString(guest->failure()))+" ("+compatibilityFieldString(guest->incompatibility())+"). Use the same new build and base game version.";stop();status(text.c_str());}}
    if(now-lastStatus>=200){lastStatus=now;
        auto* link=host?host->transport():guest?guest->transport():nullptr;
        if(link&&link->state()==TransportState::Connected)status("Connected. Start Co-op Practice on both devices, then Ready / Resume. You do not need simultaneous clicks.");
        if(panel){char value[600];pc_coop_practice_status(value,sizeof(value));SetWindowTextA(practiceStatus,value);}
    }
}
