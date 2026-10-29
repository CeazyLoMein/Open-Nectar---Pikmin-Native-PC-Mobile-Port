#include "netplay/pc_desktop_content_identity.h"
#include <iostream>
namespace fs=std::filesystem;
int main(int argc,char** argv){
 if(argc!=2)return 2;const fs::path root=fs::absolute(fs::u8path(argv[1]));if(!fs::create_directory(root)){std::cerr<<"Need a new isolated fixture directory\n";return 2;}
 auto put=[](const fs::path& p,const std::string& name,const std::string& raw){fs::create_directories(p);std::ofstream f(p/fs::u8path(name),std::ios::binary);f.write(raw.data(),raw.size());return bool(f);};
 std::array<std::uint8_t,32> a{},b{},c{};const std::string raw("\0\xff\1\3",4);
 if(nectar_desktop::contentIdentity(root,a))return 1;
 if(!put(root/"golden","name.bin",raw)||!nectar_desktop::contentIdentity(root/"golden",a))return 1;
 if(pc_netplay_sha::hex(a.data(),a.size())!="7bc95658ff552dbfcda6c9e58176dfea2ee419791264f3e5f57bece4ab5987d4")return 1;
 if(!put(root/"nfc","caf\xc3\xa9.bin",raw)||!put(root/"nfd","cafe\xcc\x81.bin",raw))return 1;
 if(!nectar_desktop::contentIdentity(root/"nfc",b)||!nectar_desktop::contentIdentity(root/"nfd",c)||b!=c)return 1;
 if(!put(root/"nfd","cafe\xcc\x81.bin","changed")||!nectar_desktop::contentIdentity(root/"nfd",c)||b==c)return 1;
 if(nectar_desktop::contentIdentity(root/"missing",a))return 1;
 std::cout<<"PASS Windows native content identity: native iOS golden, NFC/NFD, changed bytes, empty/missing roots\n";return 0;
}
