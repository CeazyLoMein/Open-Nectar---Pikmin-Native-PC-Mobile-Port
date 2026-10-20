#include "pikmin2_ios_profile.h"
#include <cstdlib>
#include <iostream>
#include <map>
#include <sstream>

static int checks = 0;
static void check(bool ok, const char* label) {
    ++checks;
    if (!ok) { std::cerr << "FAILED: " << label << '\n'; std::exit(1); }
}
// Independent reader following the game's line/key whitespace rules, so tests
// do not validate the migration using its own parser implementation.
static std::string trimmed(std::string text) {
    const auto begin = text.find_first_not_of(" \t\r");
    if (begin == std::string::npos) return {};
    return text.substr(begin, text.find_last_not_of(" \t\r") - begin + 1);
}
static std::pair<std::string, std::string> assignment(std::string line) {
    line = trimmed(line);
    if (line.empty() || line.front() == '#') return {};
    const auto equal = line.find('=');
    if (equal == std::string::npos) return {};
    auto value = line.substr(equal + 1);
    const auto comment = value.find('#');
    if (comment != std::string::npos) value.resize(comment);
    return {trimmed(line.substr(0, equal)), trimmed(value)};
}
static std::map<std::string, std::string> config(const std::string& text) {
    std::map<std::string, std::string> out;
    std::istringstream lines(text);
    std::string line;
    while (std::getline(lines, line)) {
        const auto p = assignment(line);
        if (!p.first.empty()) out[p.first] = p.second;
    }
    return out;
}
static void verifyProfile(const std::string& text) {
    const auto values = config(text);
    for (const auto& s : nectar_ios_p2::profile_detail::settings) {
        const auto found = values.find(s.key);
        check(found != values.end(), s.key);
        check(found->second == s.value, s.key);
    }
}
int main() {
    using nectar_ios_p2::apply_pikmin2_enhanced_profile;
    auto empty = apply_pikmin2_enhanced_profile("");
    check(empty.changed, "new profile is changed");
    verifyProfile(empty.text);
    check(config(empty.text).at("fpsMode") == "1", "P2 starts with requested60FPS");
    check(config(empty.text).at("iosPerformanceHud") == "1", "P2 HUD enabled for initial measurement");
    auto repeated = apply_pikmin2_enhanced_profile(empty.text);
    check(!repeated.changed && repeated.text == empty.text, "idempotent byte-for-byte");

    const std::string original =
        "# My preferences\r\n"
        "texturePack = GPV\r\n"
        "texturePackEnabled = 1\r\n"
        "fpsMode = 2\r\n"
        "mouseSensitivity = 2.75\r\n"
        "freeCamera = 1\r\n"
        "gyroEnabled = 1\r\n"
        "keyboardThrow = 123\r\n"
        "naviHealthPct = 80\r\n"
        "dayMinutes = 20\r\n"
        "pikiLimit = 200\r\n"
        "unknownCustom = future value  # keep me\r\n"
        "  renderScale\t= 0.666667  # scene resolution\r\n"
        "antialiasing = 0\r\n"
        "antialiasing = 0 # duplicate\r\n"
        "chainActions = 0\r\n"
        "chainActions = 0\r\n"
        "iosEnhancedProfile = 0\r\n"
        "iosEnhancedProfile = 0\r\n";
    const auto changed = apply_pikmin2_enhanced_profile(original);
    check(changed.changed, "existing profile changed");
    verifyProfile(changed.text);
    const auto before = config(original), after = config(changed.text);
    for (const char* key : {"mouseSensitivity", "freeCamera", "gyroEnabled", "keyboardThrow", "naviHealthPct", "dayMinutes", "pikiLimit", "unknownCustom"})
        check(before.at(key) == after.at(key), key);
    check(changed.text.find("# My preferences\r\n") == 0, "leading comment preserved");
    check(changed.text.find("unknownCustom = future value  # keep me\r\n") != std::string::npos, "unknown line byte-preserved");
    check(changed.text.find("  renderScale\t= 1.0  # scene resolution\r\n") != std::string::npos, "known inline comment/spacing preserved");
    check(changed.text.find("# Duplicate replaced by iOS profile: antialiasing = 0 # duplicate\r\n") != std::string::npos, "duplicate comment survives");
    for (std::size_t i = 0; i < changed.text.size(); ++i)
        if (changed.text[i] == '\n') check(i > 0 && changed.text[i - 1] == '\r', "CRLF consistent");

    std::map<std::string, int> counts;
    std::istringstream lines(changed.text);
    std::string line;
    while (std::getline(lines, line)) {
        const auto p = assignment(line);
        if (!p.first.empty()) ++counts[p.first];
    }
    for (const auto& s : nectar_ios_p2::profile_detail::settings) check(counts[s.key] == 1, "one active known assignment");

    check(after.at("fpsMode")=="1", "120FPS replaced by requested60 once");
    check(after.at("texturePack")==before.at("texturePack"), "existing texture choice preserved");
    std::string later = changed.text;
    const auto quick = later.find("quickGrab = 1");
    later.replace(quick, std::string("quickGrab = 1").size(), "quickGrab = 0");
    auto fps=later.find("fpsMode = 1");later.replace(fps,std::string("fpsMode = 1").size(),"fpsMode = 0");
    auto hud=later.find("iosPerformanceHud = 1");later.replace(hud,std::string("iosPerformanceHud = 1").size(),"iosPerformanceHud = 0");
    const auto preserved = apply_pikmin2_enhanced_profile(later);
    check(!preserved.changed && preserved.text == later, "later user's off value preserved");
    check(!apply_pikmin2_enhanced_profile("iosEnhancedProfile = 1 # applied\nchainActions = 0\n").changed, "marker with inline comment respected");
    check(apply_pikmin2_enhanced_profile("# iosEnhancedProfile = 1\n").changed, "commented marker ignored");
    auto newline = apply_pikmin2_enhanced_profile("custom=hello");
    check(newline.text.find("custom=hello\nrenderScale = 1.0\n") == 0, "missing final newline separated");
    auto blanks = apply_pikmin2_enhanced_profile("renderScale = \n# untouched\n");
    check(blanks.text.find("renderScale = 1.0\n# untouched\n") == 0, "empty value supported");
    auto bom = apply_pikmin2_enhanced_profile("\xEF\xBB\xBF" "renderScale = 0.5\n");
    check(bom.text.find("\xEF\xBB\xBF" "renderScale = 1.0\n") == 0, "BOM preserved and first setting upgraded");
    check(!apply_pikmin2_enhanced_profile("\xEF\xBB\xBF" "iosEnhancedProfile=1\n").changed, "BOM marker recognized");
    auto onlyBom = apply_pikmin2_enhanced_profile("\xEF\xBB\xBF");
    check(onlyBom.text.find("\xEF\xBB\xBF" "renderScale = 1.0\n") == 0, "BOM-only input supported");
    check(original.find("renderScale\t= 0.666667") != std::string::npos, "input never mutated for caller backup");
    const auto knownLast = apply_pikmin2_enhanced_profile("# header\nquickGrab = 0");
    check(knownLast.text.find("# header\nquickGrab = 1\n") == 0, "known last assignment without newline");
    verifyProfile(knownLast.text);
    const auto commented = apply_pikmin2_enhanced_profile("\t # note = preserve\ncustom = 1=2\n");
    check(commented.text.find("\t # note = preserve\ncustom = 1=2\n") == 0, "comments and equals in custom values preserved");
    std::cout << "PASS: " << checks << " profile checks\n";
}
