# Experimental unsigned native iOS GAME build (not the standalone smoke app).
# Invoke via macOS Xcode -DCMAKE_SYSTEM_NAME=iOS and -DNECTAR_IOS_GAME=pikmin1 or pikmin2.
cmake_minimum_required(VERSION 3.24)
project(OpenNectarIOS LANGUAGES C CXX OBJC OBJCXX)

if(NOT CMAKE_SYSTEM_NAME STREQUAL "iOS")
    message(FATAL_ERROR "iOS SDK/Xcode is required; configure with -DCMAKE_SYSTEM_NAME=iOS")
endif()

set(NECTAR_IOS_GAME "pikmin1" CACHE STRING "Native iOS game: pikmin1 or pikmin2")
set_property(CACHE NECTAR_IOS_GAME PROPERTY STRINGS pikmin1 pikmin2)
if(NOT NECTAR_IOS_GAME STREQUAL "pikmin1" AND NOT NECTAR_IOS_GAME STREQUAL "pikmin2")
    message(FATAL_ERROR "NECTAR_IOS_GAME must be pikmin1 or pikmin2")
endif()
set(NECTAR_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/..")

# SDL2's bundled source includes its UIKit/OpenGLES backend. Statically link it
# into the game, with one intentional custom UIApplication entry point.
set(SDL_SHARED OFF CACHE BOOL "" FORCE)
set(SDL_STATIC ON CACHE BOOL "" FORCE)
set(SDL_TEST OFF CACHE BOOL "" FORCE)
set(SDL2_DISABLE_SDL2MAIN ON CACHE BOOL "" FORCE)
add_subdirectory("${NECTAR_ROOT}/games/pikmin1/third_party/SDL2-android" "${CMAKE_CURRENT_BINARY_DIR}/SDL2")

set(PIKMIN_GLES ON CACHE BOOL "" FORCE)
set(PIKMIN_TOUCH ON CACHE BOOL "" FORCE)
set(NECTAR_ONLINE OFF CACHE BOOL "" FORCE)
set(PIKMIN_BUILD_LAUNCHER OFF CACHE BOOL "" FORCE)
set(PIKMIN_BUILD_TESTS OFF CACHE BOOL "" FORCE)
set(NECTAR_BUILD_MAPMAKER OFF CACHE BOOL "" FORCE)
set(PIKMIN_ENABLE_IPO OFF CACHE BOOL "" FORCE)
set(BUILD_TESTING OFF CACHE BOOL "" FORCE)
set(PIKMIN_STATIC_RUNTIME OFF CACHE BOOL "" FORCE)

if(NECTAR_IOS_GAME STREQUAL "pikmin1")
    set(PIKMIN_GAME_VERSION "VERSION_GPIE01_01" CACHE STRING "" FORCE)
    set(PIKMIN_NATIVE_JAUDIO ON CACHE BOOL "" FORCE)
    add_subdirectory("${NECTAR_ROOT}/games/pikmin1" "${CMAKE_CURRENT_BINARY_DIR}/pikmin1")
    set(NECTAR_GAME_TARGET pikmin_pc)
    set(NECTAR_IOS_LABEL "Open Nectar Pikmin 1")
    set(NECTAR_IOS_BUNDLE_ID "org.opennectar.experimental.pikmin1")
else()
    set(PIKMIN_GAME_VERSION "VERSION_GPVE01" CACHE STRING "" FORCE)
    set(PIKMIN_NATIVE_JAUDIO OFF CACHE BOOL "" FORCE)
    add_subdirectory("${NECTAR_ROOT}/games/pikmin2" "${CMAKE_CURRENT_BINARY_DIR}/pikmin2")
    set(NECTAR_GAME_TARGET pikmin2_pc)
    set(NECTAR_IOS_LABEL "Open Nectar Pikmin 2")
    set(NECTAR_IOS_BUNDLE_ID "org.opennectar.experimental.pikmin2")
endif()

# CMake compiles the decompiled native game directly into the .app executable.
# SDL_UIKitRunApp owns UIKit's run loop and calls renamed nectar_game_main.
# Keep Objective-C++ Foundation code separate from the GameCube game target.
# The game target force-includes a header defining BOOL as int, which clashes
# with Apple's Objective-C BOOL typedef in ios_storage.mm.
target_sources(${NECTAR_GAME_TARGET} PRIVATE
    "${CMAKE_CURRENT_SOURCE_DIR}/ios_main.m")
add_library(nectar_ios_storage STATIC
    "${CMAKE_CURRENT_SOURCE_DIR}/ios_storage.mm")
set_target_properties(nectar_ios_storage PROPERTIES
    CXX_STANDARD 17 CXX_STANDARD_REQUIRED YES
    OBJCXX_STANDARD 17 OBJCXX_STANDARD_REQUIRED YES)
if(NECTAR_IOS_GAME STREQUAL "pikmin1")
    # UIKit stays isolated from the GameCube BOOL typedef / forced includes.
    target_sources(nectar_ios_storage PRIVATE
        "${CMAKE_CURRENT_SOURCE_DIR}/ios_mod_picker.mm"
        "${CMAKE_CURRENT_SOURCE_DIR}/ios_runtime_stats.mm")
    target_include_directories(nectar_ios_storage PRIVATE "${NECTAR_ROOT}/games/pikmin1/pc_port")
    target_compile_definitions(${NECTAR_GAME_TARGET} PRIVATE NECTAR_IOS_PERFORMANCE_HUD=1)
    target_compile_definitions(pikmin_legacy PRIVATE NECTAR_IOS_PERFORMANCE_HUD=1)
    set_source_files_properties("${CMAKE_CURRENT_SOURCE_DIR}/ios_mod_picker.mm"
        PROPERTIES COMPILE_FLAGS "-fobjc-arc")
    target_sources(${NECTAR_GAME_TARGET} PRIVATE
        "${CMAKE_CURRENT_SOURCE_DIR}/pc_ios_mod_bridge.cpp"
        "${CMAKE_CURRENT_SOURCE_DIR}/pc_ios_mod_install.cpp"
        "${NECTAR_ROOT}/games/pikmin1/pc_port/timing/pc_ios_performance.cpp")
    target_include_directories(${NECTAR_GAME_TARGET} PRIVATE
        "${CMAKE_CURRENT_SOURCE_DIR}"
        "${NECTAR_ROOT}/games/pikmin1/pc_port/mods")
    target_link_libraries(${NECTAR_GAME_TARGET} PRIVATE "-framework UniformTypeIdentifiers")
endif()
target_link_libraries(${NECTAR_GAME_TARGET} PRIVATE nectar_ios_storage)
target_link_libraries(${NECTAR_GAME_TARGET} PRIVATE
    "-framework UIKit"
    "-framework Foundation"
    "-framework QuartzCore"
    "-framework CoreGraphics"
    "-framework AVFoundation"
    "-framework GameController")

configure_file("${CMAKE_CURRENT_SOURCE_DIR}/Info.plist.in"
    "${CMAKE_CURRENT_BINARY_DIR}/Nectar-${NECTAR_IOS_GAME}-Info.plist" @ONLY)
set_target_properties(${NECTAR_GAME_TARGET} PROPERTIES
    MACOSX_BUNDLE TRUE
    MACOSX_BUNDLE_INFO_PLIST "${CMAKE_CURRENT_BINARY_DIR}/Nectar-${NECTAR_IOS_GAME}-Info.plist"
    XCODE_ATTRIBUTE_PRODUCT_BUNDLE_IDENTIFIER "${NECTAR_IOS_BUNDLE_ID}"
    XCODE_ATTRIBUTE_TARGETED_DEVICE_FAMILY "1"
    XCODE_ATTRIBUTE_CODE_SIGNING_ALLOWED "NO"
    XCODE_ATTRIBUTE_ENABLE_BITCODE "NO"
    OUTPUT_NAME "Nectar-${NECTAR_IOS_GAME}"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/app"
)
message(STATUS "Experimental iOS target: ${NECTAR_GAME_TARGET} (${NECTAR_IOS_GAME})")
