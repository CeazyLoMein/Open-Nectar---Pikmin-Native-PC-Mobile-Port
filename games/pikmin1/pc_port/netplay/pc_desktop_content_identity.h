#pragma once
// Windows equivalent of ios/ios_coop_content_identity.h: same NFC names,
// literal UTF-16 ordering, domain and big-endian length/size encodings.
#ifndef NOMINMAX
#define NOMINMAX
#endif
#include <windows.h>
#include "netplay/pc_netplay_sha256.h"
#include <array>
#include <filesystem>
#include <fstream>
#include <map>
namespace nectar_desktop {
inline bool contentIdentity(const std::filesystem::path& root,std::array<std::uint8_t,32>& output) {
    namespace fs=std::filesystem;
    try {
        const auto regular=[](const fs::path& p){DWORD a=GetFileAttributesW(p.c_str());return a!=INVALID_FILE_ATTRIBUTES&&!(a&FILE_ATTRIBUTE_REPARSE_POINT);};
        if(!fs::is_directory(root)||!regular(root))return false;
        std::map<std::wstring,fs::path> files;
        for(const auto& entry:fs::recursive_directory_iterator(root)) {
            if(!regular(entry.path()))return false;
            if(entry.is_directory())continue;
            if(!entry.is_regular_file())return false;
            const auto name=entry.path().lexically_relative(root).generic_wstring();
            int n=NormalizeString(NormalizationC,name.data(),static_cast<int>(name.size()),nullptr,0);if(n<=0)return false;
            std::wstring normalized(static_cast<std::size_t>(n),0);
            n=NormalizeString(NormalizationC,name.data(),static_cast<int>(name.size()),normalized.data(),n);if(n<=0)return false;normalized.resize(n);
            if(!files.emplace(normalized,entry.path()).second||files.size()>100000)return false;
        }
        if(files.empty())return false;
        pc_netplay_sha::Sha256 tree;const char domain[]="NECTAR-P1-DATA-v2";tree.update(domain,sizeof(domain));std::uint64_t total=0;
        for(const auto& item:files) {
            const auto& name=item.first;const auto& path=item.second;
            const int n=WideCharToMultiByte(CP_UTF8,WC_ERR_INVALID_CHARS,name.data(),static_cast<int>(name.size()),nullptr,0,nullptr,nullptr);
            if(n<=0||n>16384)return false;std::string key(static_cast<std::size_t>(n),0);
            if(WideCharToMultiByte(CP_UTF8,WC_ERR_INVALID_CHARS,name.data(),static_cast<int>(name.size()),key.data(),n,nullptr,nullptr)!=n)return false;
            const auto size=fs::file_size(path);const auto time=fs::last_write_time(path);
            if(size>8ULL*1024*1024*1024-total)return false;total+=size;
            std::ifstream in(path,std::ios::binary);if(!in)return false;
            pc_netplay_sha::Sha256 file;std::uint64_t count=0;char chunk[65536];
            while(in){in.read(chunk,sizeof(chunk));const auto got=in.gcount();if(got>0){file.update(chunk,static_cast<std::size_t>(got));count+=got;}if(count>size)return false;}
            if(!in.eof()||count!=size||fs::file_size(path)!=size||fs::last_write_time(path)!=time)return false;
            std::uint8_t hash[32],length[4],bytes[8];file.final(hash);
            for(unsigned i=0;i<4;++i)length[i]=static_cast<std::uint8_t>(static_cast<unsigned>(n)>>(24-i*8));
            for(unsigned i=0;i<8;++i)bytes[i]=static_cast<std::uint8_t>(size>>(56-i*8));
            tree.update(length,4);tree.update(key.data(),key.size());tree.update(bytes,8);tree.update(hash,32);
        }
        tree.final(output.data());return true;
    }catch(...){return false;}
}
}
