cmake_minimum_required(VERSION 3.16)

if(CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
    project(nectar_net VERSION 0.1.0 LANGUAGES CXX)
    include(CTest)
    set(_NECTAR_NET_TESTS_DEFAULT ON)
else()
    set(_NECTAR_NET_TESTS_DEFAULT OFF)
endif()

add_library(nectar_net STATIC
    src/byte_io.cpp
    src/clock.cpp
    src/compatibility.cpp
    src/connection_code.cpp
    src/gated_transport.cpp
    src/input.cpp
    src/join_gate.cpp
    src/net_platform.cpp
    src/port_mapping.cpp
    src/port_publisher.cpp
    src/protocol.cpp
    src/recording.cpp
    src/replication.cpp
    src/room.cpp
    src/scene.cpp
    src/secure_random.cpp
    src/sim_network.cpp
    src/upnp_client.cpp
    src/coop_session.cpp
    src/coop_connection.cpp
    src/practice_bootstrap.cpp
    src/practice_visual_blend.cpp
    src/actor_frame.cpp
    src/entity_registry.cpp
    src/pikmin_replication.cpp
    src/onion_authority.cpp
    src/world.cpp
    src/secure_memory.cpp
)

target_compile_features(nectar_net PUBLIC cxx_std_17)
target_include_directories(nectar_net PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

if(WIN32)
    target_link_libraries(nectar_net PUBLIC bcrypt iphlpapi ws2_32)
endif()

if(MSVC)
    target_compile_options(nectar_net PRIVATE /W4 /WX)
else()
    target_compile_options(nectar_net PRIVATE -Wall -Wextra -Wpedantic -Werror)
endif()

option(NECTAR_NET_BUILD_TESTS "Build nectar_net unit tests" ${_NECTAR_NET_TESTS_DEFAULT})
option(NECTAR_NET_ENABLE_GNS "Build the GameNetworkingSockets direct encrypted transport" OFF)
option(NECTAR_NET_ENABLE_UPNP "Map the host port with UPnP IGD through miniupnpc" ${NECTAR_NET_ENABLE_GNS})

if(NECTAR_NET_ENABLE_UPNP)
    # Built by scripts/netplay-deps.sh next to GNS.
    find_package(miniupnpc CONFIG REQUIRED)
    target_link_libraries(nectar_net PRIVATE miniupnpc::miniupnpc)
    target_compile_definitions(nectar_net PRIVATE NECTAR_NET_HAS_UPNP=1)
endif()

if(NECTAR_NET_ENABLE_GNS)
    # Built by scripts/netplay-deps.sh; pass its prefix in CMAKE_PREFIX_PATH.
    # GNS links OpenSSL::Crypto (BCrypt on Windows) but its config does not
    # look it up, so do it here and keep the link fully static.
    if(NOT WIN32)
        set(OPENSSL_USE_STATIC_LIBS ON)
        find_package(OpenSSL REQUIRED COMPONENTS Crypto)
    endif()
    find_package(Threads REQUIRED)
    find_package(GameNetworkingSockets CONFIG REQUIRED)
    target_sources(nectar_net PRIVATE src/gns_transport.cpp)
    target_link_libraries(nectar_net PUBLIC GameNetworkingSockets::static)
    if(ANDROID)
        # GNS logs through __android_log_write but its export omits liblog.
        target_link_libraries(nectar_net PUBLIC log)
    endif()
    target_compile_definitions(nectar_net PUBLIC NECTAR_NET_HAS_GNS=1)
endif()

if(NECTAR_NET_BUILD_TESTS AND NOT ANDROID)
    enable_testing()
    # Each tests/<name>.cpp becomes nectar_net_<name>, warning-clean and run by ctest.
    function(nectar_net_add_test name)
        add_executable(nectar_net_${name} tests/${name}.cpp)
        target_link_libraries(nectar_net_${name} PRIVATE nectar_net)
        if(MSVC)
            target_compile_options(nectar_net_${name} PRIVATE /W4 /WX)
        else()
            target_compile_options(nectar_net_${name} PRIVATE -Wall -Wextra -Wpedantic -Werror)
        endif()
        add_test(NAME nectar_net_${name} COMMAND nectar_net_${name})
    endfunction()

    foreach(name protocol_test connection_code_test join_gate_test gated_transport_test compatibility_test
                 decoder_fuzz_test port_mapping_test port_publisher_test room_test input_test clock_test world_scene_test soak_test replication_test onion_authority_test entity_registry_test pikmin_replication_test actor_frame_test coop_session_test coop_connection_test practice_input_test practice_visual_blend_test reliable_queue_delay_test coop_audio_test)
        nectar_net_add_test(${name})
    endforeach()
    nectar_net_add_test(coop_audio_engine_test)
    target_sources(nectar_net_coop_audio_engine_test PRIVATE ../../games/pikmin1/pc_port/netplay/pc_coop_audio.cpp)
    target_include_directories(nectar_net_coop_audio_engine_test BEFORE PRIVATE tests/audio_fixture ../../games/pikmin1/pc_port)
    target_compile_definitions(nectar_net_coop_audio_engine_test PRIVATE PIKI_PC_PORT=1 NECTAR_COOP_WORLD=1)
    if(NECTAR_NET_ENABLE_GNS)
        foreach(name gns_transport_test gated_gns_test gns_stress_test room_gns_test)
            nectar_net_add_test(${name})
        endforeach()
        # Two-process cross-platform check; run by hand, not by ctest.
        add_executable(nectar_net_interop_peer tests/interop_peer.cpp)
        target_link_libraries(nectar_net_interop_peer PRIVATE nectar_net)
        # Real-router port mapping check; run by hand, not by ctest.
        add_executable(nectar_net_publish_probe tests/publish_probe.cpp)
        target_link_libraries(nectar_net_publish_probe PRIVATE nectar_net)
    endif()
endif()

# Asset-free CLI probe, runnable in the iOS simulator through simctl spawn.
# It uses the same GNS, join gate and session code as the future game adapter.
option(NECTAR_NET_BUILD_COOP_SOCKET_PROBE "Build a real encrypted co-op connection probe" OFF)
if(NECTAR_NET_BUILD_COOP_SOCKET_PROBE)
    if(NOT NECTAR_NET_ENABLE_GNS)
        message(FATAL_ERROR "The real socket probe requires NECTAR_NET_ENABLE_GNS")
    endif()
    add_executable(nectar_net_coop_socket_probe tests/coop_socket_probe.cpp)
    set_target_properties(nectar_net_coop_socket_probe PROPERTIES MACOSX_BUNDLE FALSE)
    target_link_libraries(nectar_net_coop_socket_probe PRIVATE nectar_net)
    if(MSVC)
        target_compile_options(nectar_net_coop_socket_probe PRIVATE /W4 /WX)
    else()
        target_compile_options(nectar_net_coop_socket_probe PRIVATE -Wall -Wextra -Wpedantic -Werror)
    endif()
endif()

# Manual asset-free phone companion. No engine or campaign writes.
option(NECTAR_NET_BUILD_PRACTICE_COMPANION "Build the standalone P1 diagnostic partner" OFF)
if(NECTAR_NET_BUILD_PRACTICE_COMPANION)
    if(NOT NECTAR_NET_ENABLE_GNS)
        message(FATAL_ERROR "The practice companion needs GNS")
    endif()
    add_executable(nectar_practice_companion tools/practice_companion.cpp)
    target_link_libraries(nectar_practice_companion PRIVATE nectar_net)
    if(MSVC)
        target_compile_options(nectar_practice_companion PRIVATE /W4 /WX)
    else()
        target_compile_options(nectar_practice_companion PRIVATE -Wall -Wextra -Wpedantic -Werror)
    endif()
    if(NECTAR_NET_BUILD_TESTS)
        add_test(NAME nectar_practice_companion_self_test COMMAND nectar_practice_companion --self-test)
        set_tests_properties(nectar_practice_companion_self_test PROPERTIES TIMEOUT 60)
    endif()
endif()
