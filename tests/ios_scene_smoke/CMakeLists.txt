cmake_minimum_required(VERSION 3.24)
project(NectarSceneSmoke LANGUAGES C CXX OBJC)
if(NOT CMAKE_SYSTEM_NAME STREQUAL "iOS")
    message(FATAL_ERROR "Build this runtime probe with an Apple iOS SDK")
endif()
get_filename_component(NECTAR_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/../.." ABSOLUTE)
set(SDL_SHARED OFF CACHE BOOL "" FORCE)
set(SDL_STATIC ON CACHE BOOL "" FORCE)
set(SDL_TEST OFF CACHE BOOL "" FORCE)
set(SDL2_DISABLE_SDL2MAIN ON CACHE BOOL "" FORCE)
add_subdirectory("${NECTAR_ROOT}/games/pikmin1/third_party/SDL2-android" "${CMAKE_CURRENT_BINARY_DIR}/SDL2")
include("${NECTAR_ROOT}/ios/sdl_scene_support.cmake")
add_executable(NectarSceneSmoke MACOSX_BUNDLE main.m)
target_compile_definitions(NectarSceneSmoke PRIVATE SDL_MAIN_HANDLED=1)
target_link_libraries(NectarSceneSmoke PRIVATE SDL2-static "-framework UIKit" "-framework Foundation" "-framework QuartzCore" "-framework CoreGraphics" "-framework GameController")
set(NECTAR_IOS_BUNDLE_ID "org.opennectar.tests.scene")
set(NECTAR_IOS_LABEL "Nectar Scene Smoke")
set(NECTAR_IOS_EXECUTABLE "NectarSceneSmoke")
configure_file("${NECTAR_ROOT}/ios/Info.plist.in" "${CMAKE_CURRENT_BINARY_DIR}/Info.plist" @ONLY)
set_target_properties(NectarSceneSmoke PROPERTIES
    MACOSX_BUNDLE_INFO_PLIST "${CMAKE_CURRENT_BINARY_DIR}/Info.plist"
    XCODE_ATTRIBUTE_PRODUCT_BUNDLE_IDENTIFIER "${NECTAR_IOS_BUNDLE_ID}"
    XCODE_ATTRIBUTE_TARGETED_DEVICE_FAMILY "1"
    XCODE_ATTRIBUTE_CODE_SIGNING_ALLOWED "NO"
    XCODE_ATTRIBUTE_ENABLE_BITCODE "NO")
