#include "pc_ios_mod_install.h"
#include "pc_hd_model_convert.h"

#include <algorithm>
#include <atomic>
#include <chrono>
#include <cctype>
#include <cstdio>
#include <filesystem>
#include <fstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {
namespace fs = std::filesystem;

std::string folded(std::string text)
{
    for (char& ch : text) ch = static_cast<char>(std::tolower(static_cast<unsigned char>(ch)));
    return text;
}

bool safeComponent(const std::string& name)
{
    if (name.empty() || name == "." || name == ".." || name.front() == '.'
        || name.back() == ' ' || name.back() == '.') return false;
    for (unsigned char ch : name)
        if (ch < 32 || ch == 127 || ch == '/' || ch == '\\' || ch == ':') return false;
    return true;
}

void requireDirectory(const fs::path& path)
{
    std::error_code ec;
    const auto status = fs::symlink_status(path, ec);
    if (ec && ec != std::errc::no_such_file_or_directory) throw fs::filesystem_error("Inspect import folder", path, ec);
    if (!ec && fs::exists(status)) {
        if (!fs::is_directory(status) || fs::is_symlink(status))
            throw std::runtime_error("Import path must be a real folder: " + path.u8string());
    } else {
        fs::create_directories(path);
    }
}

bool existsNoLink(const fs::path& path)
{
    std::error_code ec;
    const auto status = fs::symlink_status(path, ec);
    if (ec == std::errc::no_such_file_or_directory) return false;
    if (ec) throw fs::filesystem_error("Inspect import path", path, ec);
    if (fs::is_symlink(status)) throw std::runtime_error("Import cannot replace a symbolic link: " + path.u8string());
    return fs::exists(status);
}

// Only the normal file formats consumed by the renderer/converter count as
// usable content. This is a structural check, not a runtime rendering claim.
bool usableFile(const fs::path& file, bool models)
{
    const std::string ext = folded(file.extension().u8string());
    const std::string base = folded(file.filename().u8string());
    unsigned char header[16] = {};
    std::ifstream in(file, std::ios::binary);
    in.read(reinterpret_cast<char*>(header), sizeof(header));
    const auto n = in.gcount();
    if (models) return ext == ".nhm" && n == 16 && header[0] == 'N' && header[1] == 'H'
        && header[2] == 'M' && header[3] == '1' && (header[4] == 1 || header[4] == 2)
        && (header[12] || header[13] || header[14] || header[15]);
    if (base.compare(0, 5, "tex1_") != 0) return false;
    if (ext == ".png") {
        static const unsigned char png[] = {137, 80, 78, 71, 13, 10, 26, 10};
        return n >= 8 && std::equal(png, png + 8, header);
    }
    return ext == ".dds" && n >= 4 && header[0] == 'D' && header[1] == 'D' && header[2] == 'S' && header[3] == ' ';
}

int validateTree(const fs::path& root, bool models)
{
    int files = 0, usable = 0;
    std::vector<std::string> names;
    for (const auto& entry : fs::recursive_directory_iterator(root)) {
        const auto status = entry.symlink_status();
        if (fs::is_symlink(status) || (!fs::is_directory(status) && !fs::is_regular_file(status)))
            throw std::runtime_error("Import contains a link or unsupported file.");
        const fs::path relative = entry.path().lexically_relative(root);
        for (const auto& component : relative)
            if (!safeComponent(component.u8string())) throw std::runtime_error("Import contains an unsafe filename.");
        const std::string key = folded(relative.generic_u8string());
        names.push_back(key);
        if (fs::is_regular_file(status)) {
            ++files;
            if (usableFile(entry.path(), models)) ++usable;
        }
    }
    std::sort(names.begin(), names.end());
    if (std::adjacent_find(names.begin(), names.end()) != names.end())
        throw std::runtime_error("Import contains ambiguous filenames.");
    if (!files || !usable) throw std::runtime_error(models ? "Model pack contains no valid NHM files."
                                                            : "Texture pack contains no tex1_* PNG or DDS textures.");
    return files;
}

void copyTree(const fs::path& source, const fs::path& target)
{
    requireDirectory(target);
    for (const auto& entry : fs::recursive_directory_iterator(source)) {
        const auto status = entry.symlink_status();
        if (fs::is_symlink(status) || (!fs::is_directory(status) && !fs::is_regular_file(status)))
            throw std::runtime_error("Existing model pack contains a link or unsupported file.");
        const fs::path destination = target / entry.path().lexically_relative(source);
        if (fs::is_directory(status)) requireDirectory(destination);
        else {
            requireDirectory(destination.parent_path());
            fs::copy_file(entry.path(), destination, fs::copy_options::overwrite_existing);
        }
    }
}

struct PackMove {
    fs::path staged, installed, previous;
    bool backedUp = false, committed = false;
};

using Rename = void (*)(const fs::path&, const fs::path&);
void renamePath(const fs::path& from, const fs::path& to) { fs::rename(from, to); }

// Kept separate so rollback can be exercised with an injected rename failure.
void commitPacks(std::vector<PackMove>& moves, Rename rename = renamePath)
{
    try {
        for (auto& move : moves) {
            if (existsNoLink(move.installed)) {
                rename(move.installed, move.previous);
                move.backedUp = true;
            }
            rename(move.staged, move.installed);
            move.committed = true;
        }
    } catch (...) {
        bool recoveryFailed = false;
        for (auto it = moves.rbegin(); it != moves.rend(); ++it) {
            try {
                if (it->committed) { rename(it->installed, it->staged); it->committed = false; }
                if (it->backedUp) { rename(it->previous, it->installed); it->backedUp = false; }
            } catch (...) { recoveryFailed = true; }
        }
        if (recoveryFailed) throw std::runtime_error("Import failed and automatic rollback needs recovery. Keep the .ios-import transaction folder.");
        throw;
    }
}

fs::path makeTransaction(const fs::path& imports)
{
    static std::atomic<unsigned long> sequence {0};
    requireDirectory(imports);
    for (int attempt = 0; attempt < 20; ++attempt) {
        const auto ticks = std::chrono::high_resolution_clock::now().time_since_epoch().count();
        const fs::path path = imports / (std::to_string(ticks) + "-" + std::to_string(sequence++));
        if (fs::create_directory(path)) return path;
    }
    throw std::runtime_error("Could not create a private import folder.");
}
}

int pc_ios_mod_install(const char* source, int kind, const char* loadRoot,
                       const char* activeTexturePack, char* message,
                       unsigned long messageSize)
{
    auto say = [&](const std::string& text) {
        if (message && messageSize) std::snprintf(message, messageSize, "%s", text.c_str());
    };
    fs::path transaction;
    try {
        if (!source || !*source || !loadRoot || !*loadRoot || kind < -1 || kind > 5)
            throw std::runtime_error("Invalid import source, model type or Load folder.");
        const bool models = kind >= 0;
        const fs::path load = fs::absolute(fs::u8path(loadRoot));
        requireDirectory(load);
        const fs::path installedRoot = load / (models ? "Models" : "Textures");
        requireDirectory(installedRoot);
        transaction = makeTransaction(load / ".ios-import");
        const fs::path stagedRoot = transaction / "new";
        const fs::path previousRoot = transaction / "previous";
        requireDirectory(stagedRoot);
        requireDirectory(previousRoot);
        char detail[512] = {};
        const std::string staging = stagedRoot.u8string();
        const int imported = models
            ? pc_hd_models_convert_file_at(source, kind, staging.c_str(), detail, sizeof(detail))
            : pc_texpack_install_zip_at(source, staging.c_str(), detail, sizeof(detail));
        if (imported <= 0) throw std::runtime_error(detail[0] ? detail : "Import did not produce files.");
        std::vector<PackMove> moves;
        std::vector<std::string> names;
        int validated = 0;
        const std::string active = folded(activeTexturePack ? activeTexturePack : "");
        for (const auto& entry : fs::directory_iterator(stagedRoot)) {
            const std::string name = entry.path().filename().u8string();
            if (!safeComponent(name) || !fs::is_directory(entry.symlink_status()) || fs::is_symlink(entry.symlink_status()))
                throw std::runtime_error("Import must contain safe pack folders.");
            names.push_back(folded(name));
            PackMove move {entry.path(), installedRoot / entry.path().filename(), previousRoot / entry.path().filename()};
            const bool replacing = existsNoLink(move.installed);
            if (replacing && !fs::is_directory(move.installed)) throw std::runtime_error("A pack destination is not a folder.");
            // The renderer stores filenames, so even an atomic folder swap
            // would change files beneath its current index.
            if (!models) {
                std::error_code equivalentError;
                const bool sameActiveDirectory = replacing && safeComponent(active)
                    && fs::equivalent(move.installed, installedRoot / fs::u8path(activeTexturePack), equivalentError);
                if (folded(name) == active || sameActiveDirectory || (active == "*" && replacing))
                    throw std::runtime_error("Disable this active texture pack and restart before replacing it.");
            }
            validated += validateTree(move.staged, models);
            if (models && replacing) {
                const fs::path merged = transaction / "merged" / entry.path().filename();
                copyTree(move.installed, merged);
                copyTree(move.staged, merged);
                validateTree(merged, true);
                move.staged = merged;
            }
            moves.push_back(std::move(move));
        }
        std::sort(names.begin(), names.end());
        if (moves.empty() || validated != imported || std::adjacent_find(names.begin(), names.end()) != names.end())
            throw std::runtime_error("Import validation did not match the extracted files.");
        // A persistent map makes an interruption recoverable without guessing
        // which originals belong to this transaction. Never delete backups.
        {
            std::ofstream journal(transaction / "RECOVERY.txt");
            journal << "Original pack folders are in previous/. On interrupted import, inspect both destinations and backups before restoring.\n";
            for (const auto& move : moves)
                journal << "Destination: " << move.installed.u8string() << "\nBackup: " << move.previous.u8string() << "\n";
            journal.close();
            if (!journal) throw std::runtime_error("Could not write the import recovery record.");
        }
        commitPacks(moves);
        std::error_code ignored;
        fs::remove_all(transaction / "new", ignored);
        fs::remove_all(transaction / "merged", ignored);
        say("Installed " + std::to_string(imported) + " files. Restart the game to apply. Previous files are backed up.");
        return imported;
    } catch (const std::exception& error) {
        // Retain failed staging and any backup, including rollback failures.
        // The next attempt always uses a fresh folder and never reuses it.
        say(std::string(error.what()) + (transaction.empty() ? "" : " Import record: " + transaction.u8string()));
        return 0;
    }
}
