#include "pc_ios_mod_bridge.h"
#include "pc_ios_mod_install.h"
#include <cstdio>
#include <exception>
#include <mutex>
#include <string>
#include <thread>
#if PIKI_P2_HOST
#include "pc_host_alloc.h"
#define PC_IOS_IMPORT_HOST() PcNativeHostAllocScope importHostScope
#else
#define PC_IOS_IMPORT_HOST() ((void)0)
#endif

extern "C" void nectar_ios_open_mod_picker(int kind);
extern "C" void nectar_ios_cleanup_mod_import(const char* path);

namespace {
std::mutex sMutex;
bool sBusy = false;
bool sReady = false;
bool sPicked = false;
bool sOk = false;
bool sCancelled = false;
int sKind = -1;
std::string sActivePack;
std::string sMessage;

void finish(bool ok, bool cancelled, const std::string& message) {
    PC_IOS_IMPORT_HOST();
    std::lock_guard<std::mutex> guard(sMutex);
    sOk = ok;
    sCancelled = cancelled;
    sMessage = message;
    sReady = true;
}
}

bool pc_ios_mod_import_open(int kind, const char* activeTexturePack) {
    PC_IOS_IMPORT_HOST();
    {
        std::lock_guard<std::mutex> guard(sMutex);
        if (sBusy || kind < -1 || kind > 5) return false;
#if PIKI_P2_HOST
        if (kind != -1) return false; // P1 character-model rows do not apply to P2.
#endif
        sBusy = true;
        sReady = sPicked = false;
        sKind = kind;
        sActivePack = activeTexturePack ? activeTexturePack : "";
    }
    nectar_ios_open_mod_picker(kind);
    return true;
}

extern "C" void nectar_ios_mod_picker_result(int kind, const char* path, const char* error) {
    PC_IOS_IMPORT_HOST();
    std::string active;
    {
        std::lock_guard<std::mutex> guard(sMutex);
        if (!sBusy || sPicked || kind != sKind) return;
        sPicked = true;
        active = sActivePack;
    }
    if (!path || !*path) {
        finish(false, !error || !*error, error && *error ? error : "Import cancelled.");
        return;
    }
    const std::string copiedPath(path);
    try {
        std::thread([copiedPath, active, kind] {
            PC_IOS_IMPORT_HOST();
            char message[512] = {};
            int count = 0;
            try {
                count = pc_ios_mod_install(copiedPath.c_str(), kind, "Load", active.c_str(), message, sizeof(message));
            } catch (const std::exception&) {
                std::snprintf(message, sizeof(message), "Import failed. Existing packs were preserved.");
            } catch (...) {
                std::snprintf(message, sizeof(message), "Import failed unexpectedly.");
            }
            nectar_ios_cleanup_mod_import(copiedPath.c_str());
            finish(count > 0, false, message[0] ? message : "The ZIP did not contain a supported pack.");
        }).detach();
    } catch (...) {
        nectar_ios_cleanup_mod_import(copiedPath.c_str());
        finish(false, false, "Could not start the import. Please try again.");
    }
}

bool pc_ios_mod_import_poll(bool* ok, bool* cancelled, char* message, std::size_t size) {
    PC_IOS_IMPORT_HOST();
    std::lock_guard<std::mutex> guard(sMutex);
    if (!sReady) return false;
    if (ok) *ok = sOk;
    if (cancelled) *cancelled = sCancelled;
    if (message && size) std::snprintf(message, size, "%s", sMessage.c_str());
    sBusy = sReady = false;
    sMessage.clear();
    return true;
}
