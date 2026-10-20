"""Exercise actual JKR new/delete bodies without replacing the test CRT allocator.

Generate native and original-console fixtures; compile both as C++14. The fake
heap records routing/alignment and returns aligned real storage, while malloc
fallbacks and scope nesting/thread-local state run normally.
"""
from pathlib import Path
import re
import sys

repo = Path(__file__).resolve().parents[1]
source = (repo/'games/pikmin2/pikmin2-decomp/src/JSystem/JKernel/JKRHeap.cpp').read_text(encoding='utf-8')
gfx = (repo/'games/pikmin2/pc_port/gl/pc_gfx.cpp').read_text(encoding='utf-8')
begin = source.index('#define JKR_NEW_SIZE_T size_t')
end = source.index('\n#endif', begin) + len('\n#endif')
policy = '#ifndef P2_TEST_CONSOLE\n#define PIKI_PC_PORT 1\n#endif\n#ifdef PIKI_PC_PORT\n' + source[begin:end]
begin = source.index('void* operator new(JKR_NEW_SIZE_T byteCount)')
end = source.index('\nJKRHeap::TState::TState(', begin)
operators = source[begin:end]
assert len(re.findall(r'void\* operator new(?:\[\])?\(', operators)) == 6
operators = operators.replace('operator new[]', 'test_new_array').replace('operator new', 'test_new')
operators = operators.replace('operator delete[]', 'test_delete_array').replace('operator delete', 'test_delete')
scope = re.search(r'struct PcGfxHostAllocScope \{.*?\n\};', gfx, re.S).group()
boundaries = ['pc_gfx_init', 'pc_gfx_begin_frame', 'pc_gfx_flush_batch',
              'pc_gfx_overlay_texture_create', 'pc_gfx_overlay_texture_destroy',
              'pc_gfx_overlay_begin', 'pc_gfx_overlay_sprite', 'pc_gfx_overlay_end',
              'pc_gfx_dim_full_target', 'pc_gfx_ui_draw', 'pc_gfx_blur_gx_rect']
for name in boundaries:
    entry = re.search(r'(?:void|unsigned) ' + name + r'\([^;{]*\)\s*\{([^{}]*)', gfx).group(1)
    # Ignore comments; require host allocation before any executable statement,
    # including early returns and the driver's first lazy shader compilation.
    entry = re.sub(r'//[^\n]*|/\*.*?\*/', '', entry, flags=re.S).strip()
    assert entry.startswith('PcGfxHostAllocScope hostAllocScope;'), name

fixture = r'''
#include <cassert>
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <initializer_list>
#include <thread>
typedef std::size_t u32; // fixture count only; avoids host narrowing warnings
struct JKRHeap {
    static JKRHeap *sCurrentHeap, *first, *second;
    alignas(64) unsigned char bytes[4096];
    std::size_t cursor = 3;
    int lastAlign = 0, calls = 0, frees = 0;
    void* do_alloc(std::size_t size, int alignment) {
        lastAlign = alignment; ++calls;
        const auto a = static_cast<std::uintptr_t>(alignment < 0 ? -alignment : alignment);
        const auto minAlign = a < 4 ? 4 : a;
        const auto start = reinterpret_cast<std::uintptr_t>(bytes) + cursor;
        const auto aligned = (start + minAlign - 1) & ~(minAlign - 1);
        cursor = aligned - reinterpret_cast<std::uintptr_t>(bytes) + (size ? size : 1);
        assert(cursor < sizeof(bytes));
        return reinterpret_cast<void*>(aligned);
    }
    bool owns(void* p) const {
        auto a = reinterpret_cast<std::uintptr_t>(p);
        auto b = reinterpret_cast<std::uintptr_t>(bytes);
        return a >= b && a < b + sizeof(bytes);
    }
    static JKRHeap* findFromRoot(void* p) {
        return first->owns(p) ? first : (second->owns(p) ? second : nullptr);
    }
    static void free(void* p, JKRHeap*) {
        JKRHeap* heap = findFromRoot(p); assert(heap); ++heap->frees;
    }
};
JKRHeap *JKRHeap::sCurrentHeap = nullptr, *JKRHeap::first = nullptr, *JKRHeap::second = nullptr;
'''
fixture += policy + '\n' + operators + '\n#ifdef PIKI_PC_PORT\n' + scope + '\n#endif\n'
fixture += r'''
static int checks = 0;
#define CHECK(condition) do { ++checks; assert(condition); } while (false)
int main() {
    JKRHeap a, b; JKRHeap::first = &a; JKRHeap::second = &b;
    JKRHeap::sCurrentHeap = &a;
#ifdef PIKI_PC_PORT
    const int minimum = static_cast<int>(alignof(std::max_align_t));
#if defined(__APPLE__) && defined(__aarch64__)
    static_assert(alignof(std::max_align_t) >= 16, "Apple ARM64 fundamental alignment");
#endif
#else
    const int minimum = 4;
#endif
    for (std::size_t size : {std::size_t(0), std::size_t(1), std::size_t(13), std::size_t(32)}) {
        for (int form = 0; form != 2; ++form) {
            a.cursor = 3;
            void* p = form ? test_new_array(size) : test_new(size);
            CHECK(a.lastAlign == minimum);
            CHECK(a.owns(p)); CHECK(reinterpret_cast<std::uintptr_t>(p) % minimum == 0);
            if (size) static_cast<unsigned char*>(p)[size-1] = 42;
            const int freed = a.frees;
            if (form) test_delete_array(p); else test_delete(p);
            CHECK(a.frees == freed + 1);
        }
        for (int alignment : {-64, -32, -16, -8, -4, -1, 0, 1, 4, 8, 16, 32, 64}) {
            const int magnitude = alignment < 0 ? -alignment : alignment;
            const int expected = (alignment < 0 ? -1 : 1) * (magnitude < minimum ? minimum : magnitude);
            for (int form = 0; form != 6; ++form) {
                a.cursor = b.cursor = 3;
                void* p = nullptr;
                switch (form) {
                case 0: p = test_new(size, alignment); break;
                case 1: p = test_new_array(size, alignment); break;
                case 2: p = test_new(size, &b, alignment); break;
                case 3: p = test_new_array(size, &b, alignment); break;
                case 4: p = test_new(size, nullptr, alignment); break;
                case 5: p = test_new_array(size, nullptr, alignment); break;
                }
                auto& heap = (form == 2 || form == 3) ? b : a;
#ifdef PIKI_PC_PORT
                CHECK(heap.lastAlign == expected);
#else
                (void)expected; CHECK(heap.lastAlign == alignment);
#endif
                CHECK(heap.owns(p));
                const int actual = heap.lastAlign < 0 ? -heap.lastAlign : heap.lastAlign;
                CHECK(reinterpret_cast<std::uintptr_t>(p) % (actual < 4 ? 4 : actual) == 0);
                if (size) static_cast<unsigned char*>(p)[size-1] = 17;
                const int freed = heap.frees;
                if (form % 2) test_delete_array(p); else test_delete(p);
                CHECK(heap.frees == freed + 1);
            }
        }
    }
#ifdef PIKI_PC_PORT
    CHECK(!pc_host_alloc_active());
    const int before = a.calls;
    {
        PcGfxHostAllocScope outer;
        CHECK(pc_host_alloc_active());
        { PcGfxHostAllocScope inner; CHECK(pc_host_alloc_active()); }
        CHECK(pc_host_alloc_active());
        try { PcGfxHostAllocScope inner; throw 7; } catch (int) {}
        CHECK(pc_host_alloc_active());
        for (std::size_t size : {std::size_t(0), std::size_t(1), std::size_t(31)}) {
            for (int form = 0; form != 6; ++form) {
                void* p = nullptr;
                switch (form) {
                case 0: p = test_new(size); break;
                case 1: p = test_new_array(size); break;
                case 2: p = test_new(size, 4); break;
                case 3: p = test_new_array(size, -4); break;
                case 4: p = test_new(size, nullptr, 4); break;
                case 5: p = test_new_array(size, nullptr, -4); break;
                }
                CHECK(p && !JKRHeap::findFromRoot(p));
                CHECK(reinterpret_cast<std::uintptr_t>(p) % minimum == 0);
                CHECK(a.calls == before);
                if (form % 2) test_delete_array(p); else test_delete(p);
            }
        }
        b.cursor = 3;
        void* explicitHeap = test_new(7, &b, -4);
        CHECK(b.owns(explicitHeap) && b.lastAlign == -minimum);
        test_delete(explicitHeap);
        // Thread-local host routing must not leak from this main-thread scope.
        std::thread worker([] {
            assert(!pc_host_alloc_active());
            { PcGfxHostAllocScope child; assert(pc_host_alloc_active()); }
            assert(!pc_host_alloc_active());
        });
        worker.join(); CHECK(pc_host_alloc_active());
    }
    CHECK(!pc_host_alloc_active());
    JKRHeap::sCurrentHeap = nullptr;
    void* fallback = test_new(9);
    CHECK(fallback && !JKRHeap::findFromRoot(fallback));
    test_delete(fallback);
    test_delete(nullptr); test_delete_array(nullptr);
    // Validate sized deletes reach the same original heap, regardless of scope.
    a.cursor = 3; JKRHeap::sCurrentHeap = &a;
    void* p = test_new(13);
    { PcGfxHostAllocScope host; const int freed = a.frees; test_delete(p, std::size_t(13)); CHECK(a.frees == freed+1); }
#endif
    std::printf("PASS: %d checks on actual JKR allocation/deallocation bodies; native scope nesting/thread isolation; original console policy preserved\n", checks);
}
'''
out = Path(sys.argv[1]); out.write_text(fixture)
print(f'Generated actual-code allocator fixture; verified {len(boundaries)} renderer host boundaries.')
