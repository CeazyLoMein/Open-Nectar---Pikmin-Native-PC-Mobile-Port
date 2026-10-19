#include "pc_ios_mod_bridge.h"
#include <atomic>
#include <chrono>
#include <cstdio>
#include <cstring>
#include <stdexcept>
#include <string>
#include <thread>

extern "C" void nectar_ios_mod_picker_result(int, const char*, const char*);
static int opened = 99;
static std::atomic<int> cleaned {0};
static std::atomic<int> calls {0};
static std::atomic<bool> entered {false}, releaseWorker {false};
static std::string activeSeen;
static int mode = 0;
extern "C" void nectar_ios_open_mod_picker(int kind) { opened = kind; }
extern "C" void nectar_ios_cleanup_mod_import(const char*) { ++cleaned; }
int pc_ios_mod_install(const char* source, int kind, const char* root, const char* active,
                       char* message, unsigned long size) {
    if (std::string(source) != "owned.zip" || std::string(root) != "Load" || kind != -1)
        throw std::runtime_error("Unexpected worker arguments");
    activeSeen = active;
    ++calls;
    entered = true;
    while (!releaseWorker) std::this_thread::sleep_for(std::chrono::milliseconds(1));
    if (mode == 1) throw std::runtime_error("Mock failure");
    std::snprintf(message, size, "Installed test pack");
    return 3;
}
static int checks = 0;
static void check(bool result, const char* what) {
    ++checks;
    if (!result) throw std::runtime_error(what);
}
static bool awaitResult(bool& ok, bool& cancelled, char* message, std::size_t size) {
    const auto end = std::chrono::steady_clock::now() + std::chrono::seconds(3);
    do {
        if (pc_ios_mod_import_poll(&ok, &cancelled, message, size)) return true;
        std::this_thread::sleep_for(std::chrono::milliseconds(1));
    } while (std::chrono::steady_clock::now() < end);
    return false;
}
int main() {
    try {
        bool ok = true, cancelled = false;
        char message[512] = {};
        check(!pc_ios_mod_import_poll(&ok, &cancelled, message, sizeof(message)), "No premature result");
        check(!pc_ios_mod_import_open(6, ""), "Invalid kind refused");
        check(pc_ios_mod_import_open(2, ""), "Model picker opened");
        check(opened == 2, "Model row forwarded");
        check(!pc_ios_mod_import_open(-1, ""), "Concurrent picker refused");
        nectar_ios_mod_picker_result(1, nullptr, nullptr);
        check(!pc_ios_mod_import_poll(&ok, &cancelled, message, sizeof(message)), "Wrong callback ignored");
        nectar_ios_mod_picker_result(2, nullptr, nullptr);
        check(pc_ios_mod_import_poll(&ok, &cancelled, message, sizeof(message)) && !ok && cancelled, "Cancel consumed");
        check(calls == 0 && cleaned == 0, "Cancel never installs or deletes source");
        check(pc_ios_mod_import_open(-1, "*"), "Picker reusable");
        nectar_ios_mod_picker_result(-1, nullptr, "Files unavailable");
        check(pc_ios_mod_import_poll(&ok, &cancelled, message, sizeof(message)) && !ok && !cancelled, "Picker error consumed");
        check(std::string(message) == "Files unavailable", "Picker error preserved");
        check(pc_ios_mod_import_open(-1, "GPI"), "Texture picker opened");
        nectar_ios_mod_picker_result(-1, "owned.zip", nullptr);
        check(!pc_ios_mod_import_open(-1, ""), "Busy until worker result consumed");
        nectar_ios_mod_picker_result(-1, "owned.zip", nullptr);
        releaseWorker = true;
        check(awaitResult(ok, cancelled, message, sizeof(message)) && ok && !cancelled, "Worker completed");
        check(calls == 1 && cleaned == 1 && activeSeen == "GPI", "One install, owned cleanup, active selection");
        check(!pc_ios_mod_import_poll(&ok, &cancelled, message, sizeof(message)), "Result consumed once");
        mode = 1;
        check(pc_ios_mod_import_open(-1, "*"), "Picker reopens after success");
        nectar_ios_mod_picker_result(-1, "owned.zip", nullptr);
        check(awaitResult(ok, cancelled, message, sizeof(message)) && !ok && !cancelled, "Worker exception reported");
        check(cleaned == 2 && calls == 2 && activeSeen == "*", "Failure cleans owned copy");
        std::printf("PASS: %d bridge checks\n", checks);
        return 0;
    } catch (const std::exception& error) {
        std::fprintf(stderr, "FAIL: %s\n", error.what());
        return 1;
    }
}
