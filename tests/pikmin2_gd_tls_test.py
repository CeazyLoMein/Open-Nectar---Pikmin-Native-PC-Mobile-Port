"""Extract real GD TLS declarations/storage into a mixed C/C++ link/thread smoke test."""
from pathlib import Path
import re
import sys

repo=Path(__file__).resolve().parents[1]
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
headers=[repo/'games/pikmin2/pikmin2-decomp/include/Dolphin/gd.h',repo/'games/pikmin2/include/Dolphin/gd.h']
for i,path in enumerate(headers):
    text=path.read_text()
    structure=re.search(r'typedef struct GDCurrentDL \{.*?\} GDCurrentDL;',text,re.S).group()
    begin=text.index('#ifdef PIKI_PC_PORT',text.index('///////////// GD DECLARATIONS'))
    end=text.index('extern GDOverflowCallback overflowcb;',begin)
    declaration=text[begin:end]
    write=re.search(r'static inline void __GDWrite\(u8 data\)\s*\{.*?\n\}',text,re.S).group()
    (out/f'gd-{i}.h').write_text('#include <stddef.h>\n#include <stdint.h>\n#define PIKI_PC_PORT 1\ntypedef uint8_t u8; typedef int32_t s32;\n'+structure+'\n#ifdef __cplusplus\nextern "C" {\n#endif\n'+declaration+write+'\n#ifdef __cplusplus\n}\n#endif\n')
source=(repo/'games/pikmin2/pikmin2-decomp/src/Dolphin/gd/GDBase.c').read_text()
begin=source.index('#ifdef PIKI_PC_PORT');end=source.index('#endif',begin)+len('#endif')
(out/'gd-storage.c').write_text('#include "gd-0.h"\n'+source[begin:end]+'''
void* gd_c_slot(void) { return &__GDCurrentDL; }
GDCurrentDL* gd_c_get(void) { return __GDCurrentDL; }
void gd_c_set(GDCurrentDL* p) { __GDCurrentDL=p; }
''')
(out/'gd-mirror.cpp').write_text('#include "gd-1.h"\nextern "C" void* gd_cpp_mirror_slot() { return &__GDCurrentDL; }\n')
(out/'gd-main.cpp').write_text('''#include "gd-0.h"
#include <atomic>
#include <cassert>
#include <cstdio>
#include <thread>
extern "C" void* gd_c_slot();
extern "C" GDCurrentDL* gd_c_get();
extern "C" void gd_c_set(GDCurrentDL*);
extern "C" void* gd_cpp_mirror_slot();
int main() {
    assert(__GDCurrentDL==nullptr);
    u8 mainBytes[4]={}; GDCurrentDL mainDL={mainBytes,4,mainBytes,mainBytes+4};
    __GDCurrentDL=&mainDL;
    assert(gd_c_get()==&mainDL);
    void* mainSlot=&__GDCurrentDL;
    std::atomic<int> ready{0}; std::atomic<bool> release{false};
    void* slots[2]={};
    auto worker=[&](int index) {
        assert(__GDCurrentDL==nullptr);
        u8 bytes[4]={}; GDCurrentDL dl={bytes,4,bytes,bytes+4};
        gd_c_set(&dl); assert(__GDCurrentDL==&dl);
        slots[index]=&__GDCurrentDL;
        assert(gd_c_slot()==slots[index]);
        assert(gd_cpp_mirror_slot()==slots[index]);
        __GDWrite(static_cast<u8>(index+10));
        assert(bytes[0]==index+10 && dl.data==bytes+1);
        ready.fetch_add(1);
        while(!release.load()) std::this_thread::yield();
        assert(__GDCurrentDL==&dl && gd_c_get()==&dl);
    };
    std::thread a(worker,0),b(worker,1);
    while(ready.load()!=2) std::this_thread::yield();
    assert(slots[0]!=slots[1] && slots[0]!=mainSlot && slots[1]!=mainSlot);
    assert(__GDCurrentDL==&mainDL && gd_c_get()==&mainDL);
    release.store(true); a.join(); b.join();
    __GDWrite(42); assert(mainBytes[0]==42);
    std::puts("PASS: actual GD C storage and both C++ header declarations link; three threads retain independent display-list pointers");
}
''')
print('Generated mixed C/C++ TLS fixture from both actual GD headers and GDBase.c.')
