#include "netplay/pc_coop_practice_map.h"
#include "nectar_mapcore/compile.h"
#include "Stream.h"
#include "system.h"
#include <cstring>
#include <string>
#include <vector>

namespace {
std::vector<unsigned char> terrain, stage;
std::string failure;
bool readBase(const std::string& path, std::vector<unsigned char>& output)
{
    // The compiler chooses these immutable original asset paths locally.
    RandomAccessStream* stream = gsys->openFile(path.c_str(), true);
    if (!stream) return false;
    const int size = stream->getPending();
    if (size <= 0 || size > 64 * 1024 * 1024) { stream->close(); return false; }
    output.resize(static_cast<std::size_t>(size));
    stream->read(output.data(), size); stream->close(); return true;
}
}

const char* pc_coop_practice_map_prepare()
{
    if (!terrain.empty() && !stage.empty()) return nullptr;
    nectar::MapData map{};
    map.name = "Co-op practice";
    map.baseStage = "stages/chal0.ini";
    map.sourceMod = "courses/practice/practice.mod";
    map.minX = map.minZ = -900; map.maxX = map.maxZ = 900;
    map.wallHeight = 300; map.cell = 150;
    map.routeStep = 150; map.routeMargin = 70;
    map.sunDir[0] = -0.3f; map.sunDir[1] = -1; map.sunDir[2] = -0.2f;
    map.bases[0].x = -180; map.bases[1].x = 180;
    // No generators, enemies, Onions, ship parts, water or campaign objects.
    // The first gameplay milestone exercises captains and their own squads.
    nectar::CompiledMap output;
    if (!nectar::compileMap(map, readBase, PC_COOP_PRACTICE_MOD, output, failure)
        || output.mod.empty() || output.ini.empty()) {
        if (failure.empty()) failure = "Practice terrain could not be prepared.";
        return failure.c_str();
    }
    terrain.swap(output.mod); stage.swap(output.ini);
    return nullptr;
}

bool pc_coop_practice_map_path(const char* path)
{
    return path && (std::strcmp(path, PC_COOP_PRACTICE_STAGE) == 0
        || std::strcmp(path, PC_COOP_PRACTICE_MOD) == 0
        || std::strncmp(path, "stages/cooppractice/", 20) == 0);
}
RandomAccessStream* pc_coop_practice_map_open(const char* path)
{
    if (!pc_coop_practice_map_path(path) || pc_coop_practice_map_prepare()) return nullptr;
    if (std::strcmp(path, PC_COOP_PRACTICE_STAGE) == 0) return new RamStream(stage.data(), static_cast<int>(stage.size()));
    if (std::strcmp(path, PC_COOP_PRACTICE_MOD) == 0) return new RamStream(terrain.data(), static_cast<int>(terrain.size()));
    return nullptr; // Explicitly suppress every generator under this private stage.
}
