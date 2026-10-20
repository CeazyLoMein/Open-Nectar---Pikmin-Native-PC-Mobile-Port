"""Check actual iOS target wiring and extract the real reset routine for execution.
No Apple SDK or game assets are needed; Objective-C++ compilation remains a CI check.
"""
from pathlib import Path
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("output", type=Path)
parser.add_argument("--cmake", default="cmake")
parser.add_argument("--generator")
args = parser.parse_args()
repo = Path(__file__).resolve().parents[1]
out = args.output.resolve()
out.mkdir(parents=True, exist_ok=True)
cmake = (repo/"ios/CMakeLists.txt").read_text(encoding="utf-8")
start = cmake.index('if(NECTAR_IOS_GAME STREQUAL "pikmin1")', cmake.index('add_library(nectar_ios_storage'))
block = cmake[start:cmake.index("\ntarget_link_libraries(${NECTAR_GAME_TARGET} PRIVATE nectar_ios_storage)", start)]
head = 'cmake_minimum_required(VERSION 3.24)\nproject(P2Wiring LANGUAGES CXX)\nset(NECTAR_ROOT "@ROOT@")\nset(CMAKE_CURRENT_SOURCE_DIR "${NECTAR_ROOT}/ios")\nset(NECTAR_GAME_TARGET fixture_game)\nadd_library(fixture_game STATIC "${CMAKE_CURRENT_LIST_DIR}/dummy.cpp")\nadd_library(pikmin_legacy STATIC "${CMAKE_CURRENT_LIST_DIR}/dummy.cpp")\nadd_library(pikmin2_legacy STATIC "${CMAKE_CURRENT_LIST_DIR}/dummy.cpp")\nadd_library(nectar_ios_storage STATIC "${CMAKE_CURRENT_LIST_DIR}/dummy.cpp")\nif(NECTAR_IOS_GAME STREQUAL "pikmin2")\n target_sources(fixture_game PRIVATE "${NECTAR_ROOT}/games/pikmin2/pc_port/mods/pc_hd_model_convert.cpp")\nendif()\n'
tail = '\nget_target_property(src fixture_game SOURCES)\nget_target_property(storage nectar_ios_storage SOURCES)\nforeach(f IN LISTS src storage)\n if(NOT f MATCHES "dummy[.]cpp$")\n  set_source_files_properties("${f}" PROPERTIES HEADER_FILE_ONLY TRUE)\n endif()\nendforeach()\nget_target_property(defs nectar_ios_storage COMPILE_DEFINITIONS)\nif(NECTAR_IOS_GAME STREQUAL "pikmin2")\n if(NOT "NECTAR_IOS_P2_FEATURES=1" IN_LIST defs)\n  message(FATAL_ERROR "P2 native callback routing missing")\n endif()\n if("${NECTAR_ROOT}/games/pikmin2/pc_port/mods/pc_hd_model_convert.cpp" IN_LIST src)\n  message(FATAL_ERROR "Duplicate old converter remains")\n endif()\n if(NOT "${NECTAR_ROOT}/games/pikmin1/pc_port/mods/pc_hd_model_convert.cpp" IN_LIST src)\n  message(FATAL_ERROR "Hardened staged converter missing")\n endif()\nendif()\nforeach(f pc_ios_mod_bridge.cpp pc_ios_mod_install.cpp)\n if(NOT "${NECTAR_ROOT}/ios/${f}" IN_LIST src)\n  message(FATAL_ERROR "Missing import source ${f}")\n endif()\nendforeach()\nforeach(f ios_mod_picker.mm ios_runtime_stats.mm)\n if(NOT "${NECTAR_ROOT}/ios/${f}" IN_LIST storage)\n  message(FATAL_ERROR "Missing native source ${f}")\n endif()\nendforeach()\nget_target_property(game_defs fixture_game COMPILE_DEFINITIONS)\nif(NOT "NECTAR_IOS_PERFORMANCE_HUD=1" IN_LIST game_defs)\n message(FATAL_ERROR "HUD definition missing")\nendif()\nmessage(STATUS "PASS: ${NECTAR_IOS_GAME} native feature wiring")\n'
(out/"dummy.cpp").write_text("int dummy;\n", encoding="utf-8")
(out/"CMakeLists.txt").write_text(head.replace("@ROOT@", repo.as_posix()) + block + tail, encoding="utf-8")
for game in ("pikmin1", "pikmin2"):
    command = [args.cmake, "-S", str(out), "-B", str(out/("build-" + game)), "-DNECTAR_IOS_GAME=" + game]
    if args.generator:
        command += ["-G", args.generator]
    subprocess.run(command, check=True)

settings = (repo/"games/pikmin2/pc_port/settings/pc_settings.cpp").read_text(encoding="utf-8")
start = settings.index("void resetToDefaults() {")
reset = settings[start:settings.index("\n}", start) + 2]
fixture = r'''
#include <cassert>
#include <cstdio>
struct Config {
    int iosEnhancedProfile = 0, iosPerformanceHud = 0, fpsMode = 0;
    void applyDefaults() { iosEnhancedProfile=0; iosPerformanceHud=0; fpsMode=0; }
};
Config sConfig, sPending, saved;
bool sVideoConfirmActive=true;
int applies=0;
void applyVideo() { ++applies; }
void applyControls(const Config&) { ++applies; }
void applyGraphics(const Config&) { ++applies; }
void saveConfig() { saved=sConfig; }
'''
fixture += reset
fixture += r'''
int main() {
    for (int marker : {0, 1, 7}) {
        sConfig.iosEnhancedProfile=marker;
        sConfig.iosPerformanceHud=1;
        sConfig.fpsMode=2;
        sVideoConfirmActive=true;
        resetToDefaults();
        assert(sConfig.iosEnhancedProfile==marker);
        assert(sPending.iosEnhancedProfile==marker && saved.iosEnhancedProfile==marker);
        assert(sConfig.iosPerformanceHud==0 && sConfig.fpsMode==0);
        assert(sPending.fpsMode==0 && saved.fpsMode==0);
        assert(!sVideoConfirmActive);
    }
    assert(applies==9);
    std::puts("PASS: actual P2 reset preserves migration history and resets user settings");
}
'''
fixture = "#include <initializer_list>\n" + fixture
(out/"reset-test.cpp").write_text(fixture, encoding="utf-8")

# Compile the actual settings-to-import boundary against the real public APIs.
# Replacing GL's include guard only avoids needing a graphics SDK in this unit
# fixture; the texture-pack header and declarations are used without alteration.
texpack = (repo/"games/pikmin2/pc_port/gl/pc_texpack.cpp").read_text(encoding="utf-8")
def body(source, signature):
    start = source.index(signature + "\n{") if signature + "\n{" in source else source.index(signature + " {")
    return source[start:source.index("\n}", start) + 2]
action = body(settings, "void texturePacksRowAction(int row, const std::vector<std::string>& packs)")
fixture = r'''
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#define __IPHONEOS__ 1
#define PIKMIN_PC_OPENGL_H
using GLuint = unsigned int;
#include "gl/pc_texpack.h"
#include "pc_ios_mod_bridge.h"
static bool sEnabled=false;
static std::string sSelectedPack;
struct Config { int texturePackEnabled=0; std::string texturePack; };
static Config sConfig,sPending;
static bool sTexturePackPickerActive=false,sTexturePackRestartPrompt=false;
static const int kTexturePackInstallRow=0;
static bool acceptImport=true,noticeError=false;
static int imports=0,saves=0,openedKind=99;
static std::string capturedPack,notice;
static void saveConfig() { ++saves; }
static void texturePackNotice(bool error,const char* text) { noticeError=error; notice=text; }
bool pc_ios_mod_import_open(int kind,const char* active) {
    ++imports; openedKind=kind; capturedPack=active; return acceptImport;
}
'''
fixture += body(texpack, "bool pc_texpack_enabled(void)") + "\n"
fixture += body(texpack, "const std::string& pc_texpack_selected_pack(void)") + "\n" + action
fixture += r'''
static int checks=0;
static void check(bool value) { ++checks; assert(value); }
int main() {
    const std::vector<std::string> packs={"GPV","GPVE01"};
    // Disabled renderer must not protect a merely configured or pending pack.
    sConfig.texturePack="GPV";sConfig.texturePackEnabled=1;
    sPending=sConfig;
    texturePacksRowAction(0,packs);
    check(imports==1 && capturedPack.empty() && openedKind==-1);
    check(sTexturePackPickerActive);
    // Renderer selection is independent of settings changed since startup.
    sTexturePackPickerActive=false;sEnabled=true;sSelectedPack="GPV";
    sConfig.texturePack="GPVE01";sPending=sConfig;
    texturePacksRowAction(0,packs);
    check(imports==2 && capturedPack=="GPV");
    check(sTexturePackPickerActive);
    sTexturePackPickerActive=false;sConfig.texturePackEnabled=0;
    sConfig.texturePack.clear();sPending=sConfig;
    texturePacksRowAction(0,packs);
    check(imports==3 && capturedPack=="GPV");
    check(sEnabled && sSelectedPack=="GPV");
    // All-indexed mode protects all existing pack folders, until restart.
    sTexturePackPickerActive=false;sSelectedPack.clear();
    texturePacksRowAction(0,packs);
    check(imports==4 && capturedPack=="*");
    sTexturePackPickerActive=false;sEnabled=false;
    texturePacksRowAction(0,packs);
    check(imports==5 && capturedPack.empty());
    // Reentry and activation during installation must not interrupt the worker.
    texturePacksRowAction(0,packs);
    check(imports==5);
    texturePacksRowAction(1,packs);
    check(saves==0 && sConfig.texturePack.empty() && !sTexturePackRestartPrompt);
    check(noticeError);
    sTexturePackPickerActive=false;acceptImport=false;
    texturePacksRowAction(0,packs);
    check(imports==6 && !sTexturePackPickerActive);
    check(noticeError && notice=="An import is already running.");
    // Choosing and disabling a pack changes config, not the current index.
    texturePacksRowAction(1,packs);
    check(saves==1 && sConfig.texturePack=="GPV" && sPending.texturePack=="GPV");
    check(sConfig.texturePackEnabled && sPending.texturePackEnabled && sTexturePackRestartPrompt);
    sTexturePackRestartPrompt=false;sEnabled=true;sSelectedPack="GPV";
    texturePacksRowAction(1,packs);
    check(saves==2 && sConfig.texturePack.empty() && sPending.texturePack.empty());
    check(!sConfig.texturePackEnabled && !sPending.texturePackEnabled);
    check(sEnabled && sSelectedPack=="GPV" && !sTexturePackRestartPrompt);
    texturePacksRowAction(-1,packs);texturePacksRowAction(99,packs);
    check(saves==2 && imports==6);
    std::printf("PASS: %d actual P2 texture-action/API/active-pack checks\n",checks);
}
'''
(out/"texture-import-action-test.cpp").write_text(fixture, encoding="utf-8")
