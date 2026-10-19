#include "pc_ios_mod_install.cpp"
#include <iostream>
#include <cassert>
#include <cstring>

namespace fs = std::filesystem;
namespace {
std::string mode;
int extractionCount = 1;
void write(const fs::path& path, const std::string& bytes) {
    fs::create_directories(path.parent_path());
    std::ofstream out(path, std::ios::binary); out << bytes;
}
std::string read(const fs::path& path) {
    std::ifstream in(path, std::ios::binary); return {std::istreambuf_iterator<char>(in), {}};
}
std::string png(const char* note) { return std::string("\211PNG\r\n\032\n",8) + note; }
std::string nhm() { return std::string("NHM1\1\0\0\0\1\0\0\0\1\0\0\0",16); }
int renameCall = 0, failAt = 0;
void failRename(const fs::path& a, const fs::path& b) {
    if (++renameCall == failAt) throw std::runtime_error("Injected disk failure");
    fs::rename(a,b);
}
}
int pc_texpack_install_zip_at(const char*, const char* root, char* message, unsigned long) {
    if (mode == "failed") { write(fs::path(root)/"Pack"/"tex1_bad.png",png("partial")); std::snprintf(message,128,"%s","Extraction failed"); return 0; }
    if (mode == "unsafe") { write(fs::path(root)/".hidden"/"tex1_a.png",png("new")); return 1; }
    if (mode == "empty") { write(fs::path(root)/"Pack"/"readme.txt","not a texture"); return 1; }
    write(fs::path(root)/"Pack"/"tex1_a.png",png(mode.c_str())); return extractionCount;
}
int pc_hd_models_convert_file_at(const char*, int kind, const char* root, char*, unsigned long) {
    write(fs::path(root)/"BulborbHD"/(kind == 4 ? "bulborb.nhm" : "bulborb_dwarf.nhm"),nhm()); return 1;
}
int main() {
    const fs::path root = fs::absolute("transaction-test-data");
    fs::remove_all(root); fs::create_directories(root);
    const std::string load=(root/"Load").u8string(); char message[1024]={};
    auto install=[&](int kind=-1,const char* active=""){return pc_ios_mod_install("fixture.zip",kind,load.c_str(),active,message,sizeof(message));};
    mode="old"; assert(install()==1);
    const auto texture=root/"Load"/"Textures"/"Pack"/"tex1_a.png";
    mode="new"; assert(install(-1,"pack")==0); assert(read(texture)==png("old"));
    assert(install(-1,"*")==0); assert(read(texture)==png("old"));
    assert(install()==1); assert(read(texture)==png("new"));
    bool backupFound=false;
    for(const auto& e:fs::recursive_directory_iterator(root/"Load"/".ios-import"))
        if(e.is_regular_file() && e.path().filename()=="tex1_a.png" && read(e.path())==png("old")) backupFound=true;
    assert(backupFound);
    mode="failed"; assert(install()==0); assert(read(texture)==png("new"));
    mode="empty"; assert(install()==0); assert(read(texture)==png("new"));
    mode="unsafe"; assert(install()==0); assert(!fs::exists(root/"Load"/"Textures"/".hidden"));
    mode="count mismatch"; extractionCount=2; assert(install()==0); extractionCount=1;
    assert(install(4)==1); assert(install(5)==1);
    const auto models=root/"Load"/"Models"/"BulborbHD";
    assert(read(models/"bulborb.nhm")==nhm() && read(models/"bulborb_dwarf.nhm")==nhm());
    assert(install(6)==0);
    // Failure after backing up two originals and installing one new folder:
    // the reverse transaction must restore both original trees exactly.
    const auto rollback=root/"rollback";
    write(rollback/"live"/"A"/"old","A"); write(rollback/"live"/"B"/"old","B");
    write(rollback/"stage"/"A"/"new","a"); write(rollback/"stage"/"B"/"new","b");
    fs::create_directories(rollback/"previous");
    std::vector<PackMove> moves={ {rollback/"stage"/"A",rollback/"live"/"A",rollback/"previous"/"A"},
                                  {rollback/"stage"/"B",rollback/"live"/"B",rollback/"previous"/"B"} };
    renameCall=0; failAt=4; bool threw=false;
    try {commitPacks(moves,failRename);} catch (...) {threw=true;}
    assert(threw && read(rollback/"live"/"A"/"old")=="A" && read(rollback/"live"/"B"/"old")=="B");
    assert(!fs::exists(rollback/"live"/"A"/"new") && !fs::exists(rollback/"live"/"B"/"new"));
    fs::remove_all(root);
    std::cout<<"PASS: install, active-pack protection, backup, partial extraction, invalid content, unsafe folder, file-count validation, model sibling merge, rollback\n";
}
