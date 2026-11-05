#pragma once
#include <cstring>
#include <cstdio>
constexpr int UPNPCOMMAND_SUCCESS=0;
inline int fakeAddResult=0,fakeAdds=0,fakeDeletes=0;
inline const char* fakeAddress="8.8.8.8";
inline char fakeLease[32]{};
inline int UPNP_AddPortMapping(const char*,const char*,const char*,const char*,const char*,const char*,const char*,const char*,const char* lease){++fakeAdds;std::snprintf(fakeLease,sizeof(fakeLease),"%s",lease);return fakeAddResult;}
inline int UPNP_GetExternalIPAddress(const char*,const char*,char* address){std::snprintf(address,40,"%s",fakeAddress);return 0;}
inline int UPNP_DeletePortMapping(const char*,const char*,const char*,const char*,const char*){++fakeDeletes;return 0;}
