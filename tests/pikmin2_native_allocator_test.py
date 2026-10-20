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
# Emulate Apple's smaller scalar alignment on a host with a different ABI.
# Only the platform measurement is substituted; allocator control flow is real.
policy = policy.replace('alignof(std::max_align_t)', 'alignof(P2FixtureScalarMaxAlign)')
native_header = (repo/'games/pikmin2/pc_port/pc_host_alloc.h').read_text(encoding='utf-8').replace('#pragma once', '')
os_source = (repo/'games/pikmin2/pc_port/dolphin_stubs/p2_os_host.cpp').read_text(encoding='utf-8')
game_callback = re.search(r'\t\{\n\t\tPcNativeGameAllocScope gameAllocScope;.*?\n\t\}', os_source, re.S).group()
become = re.search(r'JKRHeap\* JKRHeap::becomeCurrentHeap\(\)\s*\{.*?\n\}', source, re.S).group()
sink = (repo/'games/pikmin2/pc_port/audio/jaudio_sink.cpp').read_text(encoding='utf-8')
sink_lock = re.search(r'struct SinkLock \{.*?\n\};', sink, re.S).group()
audio_host = (repo/'games/pikmin2/pc_port/audio/jaudio_host.cpp').read_text(encoding='utf-8')
assert 'PcNativeHostAllocScope hostAllocScope;' in audio_host[audio_host.index('void beginSinkOpen()'):audio_host.index('void serviceSinkOpen(')]
assert 'PcNativeHostAllocScope workerHostAllocScope;' in audio_host
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
#include <mutex>
#include <thread>
#ifdef P2_TEST_APPLE_SCALAR_ALIGNMENT
using P2FixtureScalarMaxAlign = double;
static_assert(alignof(P2FixtureScalarMaxAlign) == 8, "Apple ARM64 scalar alignment emulation");
#else
using P2FixtureScalarMaxAlign = std::max_align_t;
#endif
typedef std::size_t u32; // fixture count only; avoids host narrowing warnings
struct JKRHeap {
    static JKRHeap *sCurrentHeap, *first, *second;
    JKRHeap* becomeCurrentHeap();
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
fixture += '\n#ifndef P2_TEST_CONSOLE\n' + native_header + '\n#endif\n'
fixture += policy + '\n' + operators + '\n' + become
fixture += '\n#ifdef PIKI_PC_PORT\n' + scope + '\n' + sink_lock + '''
static_assert(pc_object_alignment(4) >= 16, "Native default new must support 16-byte objects, including iPhone ARM64");
static_assert(pc_object_alignment(-4) <= -16, "Native tail new must support 16-byte objects");
struct PcThreadArg { void* (*func)(void*); void* param; };
void* run_actual_game_callback(PcThreadArg* arg) { void* ret = nullptr;
''' + game_callback + '\nreturn ret; }\n#endif\n'
fixture += r'''
static int checks = 0;
#define CHECK(condition) do { ++checks; assert(condition); } while (false)
int main() {
    JKRHeap a, b; JKRHeap::first = &a; JKRHeap::second = &b;
    JKRHeap::sCurrentHeap = &a;
#ifdef PIKI_PC_PORT
    CHECK(!pc_game_alloc_active());
    void* nativeDefault = test_new(17);
    CHECK(nativeDefault && !JKRHeap::findFromRoot(nativeDefault)); test_delete(nativeDefault);
    CHECK(a.calls == 0);
    a.becomeCurrentHeap(); CHECK(pc_game_alloc_active());
    const int scalar = static_cast<int>(alignof(std::max_align_t));
    const int minimum = scalar > 16 ? scalar : 16;
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
            assert(!pc_game_alloc_active());
            assert(!pc_host_alloc_active());
            void* native = test_new(13);
            assert(native && !JKRHeap::findFromRoot(native)); test_delete(native);
            { PcGfxHostAllocScope child; assert(pc_host_alloc_active()); }
            assert(!pc_host_alloc_active());
            PcThreadArg arg{[](void*) -> void* {
                assert(pc_game_alloc_active()); return test_new(13);
            }, nullptr};
            void* game = run_actual_game_callback(&arg);
            assert(JKRHeap::first->owns(game)); test_delete(game);
            assert(!pc_game_alloc_active());
            {
                PcNativeHostAllocScope host;
                void* nested = run_actual_game_callback(&arg);
                assert(nested && !JKRHeap::findFromRoot(nested)); test_delete(nested);
            }
            PcThreadArg throwing{[](void*) -> void* { throw 7; }, nullptr};
            try { run_actual_game_callback(&throwing); } catch (int) {}
            assert(!pc_game_alloc_active() && !pc_host_alloc_active());
            // Explicit game heap selection must still work from a native worker.
            void* explicitHeap = test_new_array(9, JKRHeap::second, -4);
            assert(JKRHeap::second->owns(explicitHeap)); test_delete_array(explicitHeap);
        });
        worker.join(); CHECK(pc_host_alloc_active());
    }
    CHECK(!pc_host_alloc_active());
    CHECK(pc_game_alloc_active());
    // Audio's actual lock wraps synchronous SDL calls even on a game thread.
    std::recursive_mutex audioMutex;
    const int beforeAudio = a.calls;
    {
        SinkLock audio(audioMutex);
        CHECK(pc_host_alloc_active());
        { SinkLock nested(audioMutex); CHECK(pc_host_alloc_active()); }
        void* audioBuffer = test_new(32);
        CHECK(audioBuffer && !JKRHeap::findFromRoot(audioBuffer));
        test_delete(audioBuffer); CHECK(a.calls == beforeAudio);
    }
    CHECK(!pc_host_alloc_active() && pc_game_alloc_active());
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
    std::printf("PASS: %d allocator checks; game/native/audio thread ownership and scope restoration; console policy preserved\n", checks);
}
'''
out = Path(sys.argv[1]); out.write_text(fixture)
print(f'Generated actual-code allocator fixture; verified {len(boundaries)} renderer host boundaries.')
