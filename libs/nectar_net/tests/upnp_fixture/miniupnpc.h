#pragma once
#include <cstring>
struct UPNPDev {};
struct UPNPUrls {char* controlURL=nullptr;};
struct IGDdatas {struct {char servicetype[64]{};} first;};
constexpr int UPNP_CONNECTED_IGD=1,UPNP_PRIVATEIP_IGD=2,UPNP_DISCONNECTED_IGD=3,UPNP_UNKNOWN_DEVICE=4;
inline UPNPDev* upnpDiscoverDevices(const char* const*,int,const char*,const char*,int,int,int,int*,int){static UPNPDev d;return &d;}
inline int UPNP_GetValidIGD(UPNPDev*,UPNPUrls*,IGDdatas*,char*,int,char*,int){return UPNP_CONNECTED_IGD;}
inline void freeUPNPDevlist(UPNPDev*){}
inline void FreeUPNPUrls(UPNPUrls*){}
