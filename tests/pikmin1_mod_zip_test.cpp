#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
#include "pc_hd_model_convert.h"
#include <cassert>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

namespace fs=std::filesystem;
struct Entry {std::string name,data; uint16_t method=0; bool badCrc=false;};
uint32_t crc(const std::string& bytes) {
    uint32_t c=~0u;
    for(unsigned char b:bytes) {c^=b; for(int n=0;n<8;n++) c=(c>>1)^(0xedb88320u&(0u-(c&1)));}
    return ~c;
}
void put16(std::string& s,uint16_t n) {s.push_back(char(n));s.push_back(char(n>>8));}
void put32(std::string& s,uint32_t n) {put16(s,uint16_t(n));put16(s,uint16_t(n>>16));}
void zip(const fs::path& path,const std::vector<Entry>& entries) {
    std::string body,central;
    for(const auto& e:entries) {
        std::string data=e.data;
        if(e.method==8) {std::string d(1,'\1');put16(d,uint16_t(data.size()));put16(d,uint16_t(~data.size()));d+=data;data=d;}
        const auto local=uint32_t(body.size()), checksum=crc(e.data)^(e.badCrc?1:0);
        put32(body,0x04034b50);put16(body,20);put16(body,0);put16(body,e.method);put32(body,0);
        put32(body,checksum);put32(body,uint32_t(data.size()));put32(body,uint32_t(e.data.size()));
        put16(body,uint16_t(e.name.size()));put16(body,0);body+=e.name;body+=data;
        put32(central,0x02014b50);put16(central,20);put16(central,20);put16(central,0);put16(central,e.method);put32(central,0);
        put32(central,checksum);put32(central,uint32_t(data.size()));put32(central,uint32_t(e.data.size()));
        put16(central,uint16_t(e.name.size()));put16(central,0);put16(central,0);put16(central,0);put16(central,0);put32(central,0);put32(central,local);central+=e.name;
    }
    const auto offset=uint32_t(body.size());body+=central;
    put32(body,0x06054b50);put16(body,0);put16(body,0);put16(body,uint16_t(entries.size()));put16(body,uint16_t(entries.size()));
    put32(body,uint32_t(central.size()));put32(body,offset);put16(body,0);
    std::ofstream out(path,std::ios::binary);out<<body;
}
int main() {
    const fs::path root=fs::absolute("zip-test-data");fs::remove_all(root);fs::create_directory(root);
    const auto archive=root/"My Pack.zip", output=root/"staged";
    const auto archiveText=archive.u8string(),outputText=output.u8string();char message[512];
    auto extract=[&]{fs::remove_all(output);return pc_texpack_install_zip_at(archiveText.c_str(),outputText.c_str(),message,sizeof(message));};
    zip(archive,{{"nested/tex1_a.png","texture"}});assert(extract()==1);assert(fs::exists(output/"My Pack"/"nested"/"tex1_a.png"));
    zip(archive,{{"bundle/Load/Textures/Pack/tex1_a.png","texture"},{"bundle/emulator.exe","ignored"}});
    assert(extract()==1);assert(fs::exists(output/"Pack"/"tex1_a.png"));assert(!fs::exists(output/"My Pack"));
    zip(archive,{{"Load\\Textures\\Pack\\tex1_a.png","texture",8}});assert(extract()==1);assert(fs::exists(output/"Pack"/"tex1_a.png"));
    for(const char* unsafe:{"../escape","folder/../escape","/absolute","C:/drive","C:\\drive","\\\\server\\share","folder\\..\\escape","ok/Load/Textures/../escape"}) {
        zip(archive,{{unsafe,"bad"}});assert(extract()==0);assert(!fs::exists(output));
    }
    zip(archive,{{"good.txt","first"},{"bad.txt","second",99}});assert(extract()==0);
    zip(archive,{{"good.txt","first"},{"bad.txt","second",0,true}});assert(extract()==0);
    zip(archive,{{"dup.txt","a"},{"DUP.txt","b"}});assert(extract()==0);
    zip(archive,{});assert(extract()==0);
    // Destination errors must never return partial positive success.
    zip(archive,{{"good.txt","first"}});fs::remove_all(output);{std::ofstream f(output);f<<"not a folder";}
    assert(pc_texpack_install_zip_at(archiveText.c_str(),outputText.c_str(),message,sizeof(message))==0);
    assert(pc_hd_models_convert_file_at(archiveText.c_str(),99,outputText.c_str(),message,sizeof(message))==0);
    fs::remove_all(root);
    std::cout<<"PASS: actual ZIP stored/deflate extraction, Dolphin layout, backslash normalization, traversal/root/drive rejection, partial failure, CRC, duplicate, empty archive, destination error, invalid model type\n";
}
