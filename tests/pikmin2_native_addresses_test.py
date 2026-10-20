"""Generate focused C++ checks from the actual P2 native boundary implementations.

Compile the generated file as C++17 and run it. Game assets/Apple SDK are not needed.
The fixture provides host services; it does not validate rendering or audio playback.
"""
from pathlib import Path
import re
import sys


def block(source, signature):
    start = source.index(signature)
    pos = source.index('{', start)
    end, depth = pos + 1, 1
    while depth:
        if source[end] == '{': depth += 1
        elif source[end] == '}': depth -= 1
        end += 1
    return source[start:end]


def generate(repo):
    game = repo/'games/pikmin2'
    root = game/'pikmin2-decomp'
    read = lambda name: (root/name).read_text(encoding='utf-8')
    types = read('include/types.h')
    aliases = types[types.index('// Native addresses/opaque handles'):types.index('typedef volatile u8 vu8;')]
    align = types[types.index('#ifdef PIKI_PC_PORT\n#define ALIGN_PREV'):types.index('#define IS_ALIGNED')]
    ar = read('include/Dolphin/ar.h')
    arq = block(ar, 'struct ARQRequest {')+';'
    aram = read('include/JSystem/JKernel/JKRAram.h')
    command = block(aram, 'struct JKRAMCommand :')+';'
    sync = re.search(r'static bool orderSync\([^;]+;', aram)[0]
    post = re.search(r'void ARQPostRequest\([^;]+;', ar)[0]
    ai = read('include/Dolphin/ai.h')
    ai_prototypes = re.search(r'void AIInitDMA\([^;]+;', ai)[0]+'\n'+re.search(r'P2Address AIGetDMAStartAddr\([^;]+;', ai)[0]
    host = (game/'pc_port/dolphin_stubs/p2_os_host.cpp').read_text(encoding='utf-8')
    host_methods = '\n'.join(block(host,s) for s in ['void ARQPostRequest(ARQRequest* task', 'void AIInitDMA(', 'P2Address AIGetDMAStartAddr()'])
    start_dma = block(read('src/JSystem/JKernel/JKRAramPiece.cpp'), 'void JKRAramPiece::startDMA(')
    adapter = (game/'pikmin2-decomp-adapter/pikmin2_pc_types.h').read_text(encoding='utf-8')
    aram_offset = block(adapter,'static inline uint32_t pc_p2_aram_offset(')
    font_info = block(read('include/JSystem/JUtility/JUTFont.h'), 'struct TGlyphCacheInfo {')+';'
    font_method = block(read('src/JSystem/JUtility/JUTCacheFont.cpp'), 'void JUTCacheFont::invalidiateAllCache()')
    map_method = block(read('src/sysCommonU/mapCode.cpp'), 'inline void MapCode::Code::write(')
    heap_chart = block(read('src/JSystem/JUtility/JUTProcBar.cpp'), 'int addrToXPos(')
    norm_line = next(x.strip() for x in read('src/JSystem/J3D/J3DModelLoader.cpp').splitlines() if 'mNormNum = static_cast<u32>(((P2Address)nrm_end' in x)
    color_line = next(x.strip() for x in read('src/JSystem/J3D/J3DModelLoader.cpp').splitlines() if 'mColorNum = static_cast<u32>(((P2Address)color0_end' in x)
    return r'''
#include <cstdint>
#include <cstddef>
#include <cstdio>
#include <cassert>
#include <stdexcept>
#include <type_traits>
#include <vector>
#define PIKI_PC_PORT 1
using u8=uint8_t; using u16=uint16_t; using u32=uint32_t; using s32=int32_t;
'''+aliases+align+r'''
typedef void (*ARQCallback)(uintptr_t);
'''+arq+r'''
template<class T> struct JSULink {};
struct OSMessageQueue {};
using OSMessage=void*;
struct JKRAramBlock {};
struct JKRDecompCommand {};
'''+command+r'''
JKRAMCommand::JKRAMCommand() {}
JKRAMCommand::~JKRAMCommand() {}
'''+post+ai_prototypes+r'''
static P2Address sAiDmaAddr;
static u32 sAiDmaLength;
static uintptr_t callbackValue;
static uintptr_t cacheAddress;
static u32 cacheLength;
void DCInvalidateRange(void* p,u32 n) {cacheAddress=(uintptr_t)p;cacheLength=n;}
void DCStoreRange(void* p,u32 n) {cacheAddress=(uintptr_t)p;cacheLength=n;}
struct JKRAramPiece {
'''+sync+r'''
    static void startDMA(JKRAMCommand*);
    static void doneDMA(uintptr_t p) {callbackValue=p;}
};
#define ARAM_DIR_ARAM_TO_MRAM 1
'''+host_methods+start_dma+r'''
// Trap termination in the fixture, retaining the production boundary condition.
#define abort() throw std::out_of_range("invalid ARAM offset")
#define fprintf(...) ((void)0)
'''+aram_offset+r'''
#undef fprintf
#undef abort
struct JUTCacheFont {
'''+font_info+r'''
    void* mCacheBuffer; int mCachePageCount; u32 mPageSize;
    void* mEndPageAddr;
    TGlyphCacheInfo *mCurrPage,*mStartPage,*mEndPage;
    void invalidiateAllCache();
};
'''+font_method+r'''
struct Stream {u8 value=0; void writeByte(u8 b){value=b;}};
namespace MapCode {struct Code {u8 mContents; void write(Stream&);};}
'''+map_method+r'''
struct JKRHeap {
    static JKRHeap* root; static u32 memory; void* start;
    static JKRHeap* getRootHeap(){return root;}
    static u32 getMemorySize(){return memory;}
    void* getStartAddr(){return start;}
};
JKRHeap* JKRHeap::root=nullptr; u32 JKRHeap::memory=0;
'''+heap_chart+r'''
int main() {
    static_assert(sizeof(P2Address)==sizeof(void*) && sizeof(P2SignedAddress)==sizeof(void*),"host addresses");
    static_assert(sizeof(u32)==4 && sizeof(ARQRequest::length)==4,"serialized sizes remain32");
    static_assert(sizeof(JKRAMCommand::mSource)==sizeof(void*) && sizeof(JKRAMCommand::mDestination)==sizeof(void*),"DMA fields");
    using Order=bool(*)(int,P2Address,P2Address,u32,JKRAramBlock*);
    static_assert(std::is_same<decltype(&JKRAramPiece::orderSync),Order>::value,"DMA API width");
    const P2Address high=P2Address(0x123400000000ULL);
    for (u32 n : {1u,4u,32u,256u}) {
        for (P2Address off : {P2Address(0),P2Address(1),P2Address(31),P2Address(1000)}) {
            const P2Address addr=high+off;
            assert(ALIGN_PREV(addr,n)==(addr & ~(P2Address(n)-1)));
            assert(ALIGN_NEXT(addr,n)==((addr+n-1)&~(P2Address(n)-1)));
        }
    }
    JKRAMCommand command;
    command.mSource=high+32; command.mDestination=high+64; command.mLength=128;
    for (s32 direction : {0,1}) {
        command.mDirection=direction;
        callbackValue=0;cacheAddress=0;
        JKRAramPiece::startDMA(&command);
        assert(command.source==high+32 && command.dest==high+64 && command.length==128);
        assert(callbackValue==(uintptr_t)static_cast<ARQRequest*>(&command));
        assert(cacheAddress==(direction==1 ? high+64 : high+32) && cacheLength==128);
    }
    AIInitDMA(high+96,512);
    assert(AIGetDMAStartAddr()==high+96 && sAiDmaLength==512);
    for (uintptr_t good : {uintptr_t(0),uintptr_t(0x4000),uintptr_t(16*1024*1024),uintptr_t(UINT32_MAX)})
        assert(pc_p2_aram_offset(reinterpret_cast<void*>(good))==good);
    bool rejected=false;
    try {pc_p2_aram_offset(reinterpret_cast<void*>(high));} catch(const std::out_of_range&) {rejected=true;}
    assert(rejected);
    assert(P2SignedAddress(high+7)!=P2SignedAddress(P2Address(7))); // memory archive identities never collide
    for (int count : {0,1,3,7}) {
        std::vector<std::max_align_t> backing((128 * size_t(count ? count : 1) + sizeof(std::max_align_t) - 1) / sizeof(std::max_align_t));
        u8* base=reinterpret_cast<u8*>(backing.data());
        const u32 stride=128;
        for (int i=0;i<count;++i) reinterpret_cast<JUTCacheFont::TGlyphCacheInfo*>(base+i*stride)->mStartCode=0x5678;
        JUTCacheFont font{base,count,stride,nullptr,nullptr,nullptr,nullptr};
        font.invalidiateAllCache();
        assert(font.mEndPageAddr==(count ? base+(count-1)*stride : nullptr));
        for (int i=0;i<count;++i) {
            auto* page=reinterpret_cast<JUTCacheFont::TGlyphCacheInfo*>(base+i*stride);
            assert(page->mStartCode==0x5678);
            assert(page->mPrev==(i ? reinterpret_cast<JUTCacheFont::TGlyphCacheInfo*>(base+(i-1)*stride):nullptr));
            assert(page->mNext==(i+1<count ? reinterpret_cast<JUTCacheFont::TGlyphCacheInfo*>(base+(i+1)*stride):nullptr));
        }
    }
    for (int b=0;b<256;++b) {MapCode::Code code{u8(b)};Stream stream;code.write(stream);assert(stream.value==b);}
    JKRHeap heap{reinterpret_cast<void*>(high)}; JKRHeap::root=&heap;JKRHeap::memory=1024;
    assert(addrToXPos(reinterpret_cast<void*>(high-1),100)==0);
    assert(addrToXPos(reinterpret_cast<void*>(high+512),100)==50);
    assert(addrToXPos(reinterpret_cast<void*>(high+2048),100)==100);
    JKRHeap::memory=0;assert(addrToXPos(reinterpret_cast<void*>(high+1),100)==0);
    struct VertexData {u8* mVtxNorm;u8* mVtxColor[1];u32 mNormNum,mColorNum;};
    u8 bytes[256]{}; VertexData data{bytes,{bytes},0,0};auto* vertData=&data;
    u8* nrm_end=bytes+36;u32 nrm_size=12;u8* color0_end=bytes+28;
'''+norm_line+'\n'+color_line+r'''
    assert(data.mNormNum==4 && data.mColorNum==8);
    std::puts("PASS: actual native DMA/AI/offset/font/map/model/chart code; full-width addresses and unsigned alignment");
}
'''


if __name__ == '__main__':
    repo=Path(sys.argv[2]) if len(sys.argv)>2 else Path(__file__).resolve().parents[1]
    Path(sys.argv[1]).write_text(generate(repo),encoding='utf-8')

