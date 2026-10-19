"""Emit a host test using the repository's actual opaque-index method bodies.

Usage: python tests/pikmin2_container_handles_test.py OUTPUT.cpp [REPO]
Then compile OUTPUT.cpp as C++17 and run it. No Apple SDK or game data needed.
"""
from pathlib import Path
import sys


def body(source, signature):
    start = source.index(signature)
    pos = source.index('{', start)
    end, depth = pos + 1, 1
    while depth:
        if source[end] == '{':
            depth += 1
        elif source[end] == '}':
            depth -= 1
        end += 1
    return source[start:end]


def fixture(repo):
    game = repo / 'games/pikmin2/pikmin2-decomp'
    methods = []
    for file, cls, arg, next_arg in [('gameCPlate.cpp', 'CPlate', 'index', 'index'),
                                     ('creatureStick.cpp', 'Stickers', 'id', 'in')]:
        source = (game / 'src/plugProjectKandoU' / file).read_text(encoding='utf-8')
        for signature in [f'Creature* {cls}::get(void* {arg})',
                          f'void* {cls}::getNext(void* {next_arg})',
                          f'void* {cls}::getStart()', f'void* {cls}::getEnd()']:
            methods.append(body(source, signature))
    macros = (game / 'include/P2Macros.h').read_text(encoding='utf-8')
    bounds = macros.split('#define P2ASSERTBOUNDSLINE(', 1)[1].split('\n\n', 1)[0]
    return r'''
#include <cstdint>
#include <cassert>
#include <cstdio>
#include <stdexcept>
#include <vector>
#define PIKI_PC_PORT 1
#define P2ASSERTLINE(line, cond) do { if (!(cond)) throw std::out_of_range("bounds"); } while (false)
#define P2ASSERTBOUNDSLINE(''' + bounds + r'''
namespace Game {
struct Creature { int id; };
struct CPlate {
    struct Slot { Creature* mCreature; };
    Slot* mSlots; int mSlotCount;
    Creature* get(void*); void* getNext(void*); void* getStart(); void* getEnd();
};
struct Stickers {
    static int numBuffer;
    static Creature** buffer;
    Creature* get(void*); void* getNext(void*); void* getStart(); void* getEnd();
};
int Stickers::numBuffer = 0;
Creature** Stickers::buffer = nullptr;
''' + '\n'.join(methods) + r'''
}
int main() {
    using namespace Game;
    for (int count : {0, 1, 100, 110, 10000}) {
        std::vector<Creature> objects(count);
        std::vector<CPlate::Slot> slots(count);
        std::vector<Creature*> stickers(count);
        for (int i=0; i<count; ++i) {
            objects[i].id=i; slots[i].mCreature=&objects[i]; stickers[i]=&objects[i];
        }
        CPlate plate{slots.data(), count};
        Stickers attached;
        Stickers::numBuffer=count;
        Stickers::buffer=stickers.data();
        int visited=0;
        for (void* h=plate.getStart(); h!=plate.getEnd(); h=plate.getNext(h)) {
            assert(plate.get(h)==&objects[visited]);
            assert(plate.get(h)->id==visited); ++visited;
        }
        assert(visited==count);
        visited=0;
        for (void* h=attached.getStart(); h!=attached.getEnd(); h=attached.getNext(h)) {
            assert(attached.get(h)==&objects[visited]); ++visited;
        }
        assert(visited==count);
        assert(plate.getNext(reinterpret_cast<void*>(std::intptr_t(-1)))==plate.getStart());
        assert(attached.getNext(reinterpret_cast<void*>(std::intptr_t(-1)))==attached.getStart());
        const std::intptr_t high=std::intptr_t(0x100000000LL)+7;
        assert(reinterpret_cast<std::intptr_t>(plate.getNext(reinterpret_cast<void*>(high)))==high+1);
        assert(reinterpret_cast<std::intptr_t>(attached.getNext(reinterpret_cast<void*>(high)))==high+1);
        // Actual assertion must reject out-of-range and >4GiB handles before lookup.
        for (std::intptr_t bad : {std::intptr_t(-1), std::intptr_t(count), high}) {
            bool rejected=false;
            try { attached.get(reinterpret_cast<void*>(bad)); }
            catch (const std::out_of_range&) { rejected=true; }
            assert(rejected);
        }
    }
    std::puts("PASS: actual 8 container methods; 0/1/100/110/10000 slots, sentinel, >4GiB, bounds");
}
'''


if __name__ == '__main__':
    repo = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).resolve().parents[1]
    Path(sys.argv[1]).write_text(fixture(repo), encoding='utf-8')
