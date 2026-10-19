#ifndef NECTAR_PIKMIN1_IOS_PROFILE_H
#define NECTAR_PIKMIN1_IOS_PROFILE_H

#include <array>
#include <string>
#include <string_view>

namespace nectar_ios {

struct ProfileResult {
    std::string text;
    bool changed;
};

namespace profile_detail {
struct Setting { const char* key; const char* value; };
inline constexpr std::array<Setting, 16> settings {{
    {"renderScale", "1.0"}, {"antialiasing", "1"},
    {"anisotropy", "4"}, {"bloom", "1"},
    {"chainActions", "1"}, {"holdToPluck", "1"},
    {"betterPathfinding", "1"}, {"idleCounter", "1"},
    {"instantWhistle", "1"}, {"quickGrab", "1"},
    {"noTrip", "1"}, {"throwCancelB", "1"},
    {"throwWhileMoving", "1"}, {"lockOn", "1"},
    {"charge", "1"}, {"iosEnhancedProfile", "1"}
}};

inline std::string_view trim(std::string_view text) {
    const auto first = text.find_first_not_of(" \t\r");
    if (first == std::string_view::npos) return {};
    const auto last = text.find_last_not_of(" \t\r");
    return text.substr(first, last - first + 1);
}

struct ParsedLine {
    std::string_view key;
    std::string_view value;
    std::size_t valueBegin = 0;
    std::size_t valueEnd = 0;
};

inline ParsedLine parse(std::string_view line) {
    if (!line.empty() && line.back() == '\r') line.remove_suffix(1);
    const auto eq = line.find('=');
    if (eq == std::string_view::npos) return {};
    const auto key = trim(line.substr(0, eq));
    if (key.empty() || key.front() == '#') return {};
    auto end = line.find('#', eq + 1);
    if (end == std::string_view::npos) end = line.size();
    auto begin = eq + 1;
    while (begin < end && (line[begin] == ' ' || line[begin] == '\t')) ++begin;
    auto valueEnd = end;
    while (valueEnd > begin && (line[valueEnd - 1] == ' ' || line[valueEnd - 1] == '\t')) --valueEnd;
    return {key, line.substr(begin, valueEnd - begin), begin, valueEnd};
}
} // namespace profile_detail

// Text-only, one-time upgrade. Unknown keys and existing comments survive.
// The caller owns filesystem backup and atomic replacement. The game must
// also serialize iosEnhancedProfile, or use a durable separate marker: its
// regular config writer otherwise drops unknown keys on the next menu save.
inline ProfileResult apply_pikmin1_enhanced_profile(const std::string& original) {
    using namespace profile_detail;
    const bool bom = original.compare(0, 3, "\xEF\xBB\xBF") == 0;
    const std::size_t start = bom ? 3 : 0;
    for (std::size_t pos = start; pos < original.size();) {
        const auto nl = original.find('\n', pos);
        const auto end = nl == std::string::npos ? original.size() : nl;
        auto body = std::string_view(original).substr(pos, end - pos);
        if (!body.empty() && body.back() == '\r') body.remove_suffix(1);
        const auto parsed = parse(body);
        if (parsed.key == "iosEnhancedProfile" && parsed.value == "1")
            return {original, false};
        if (nl == std::string::npos) break;
        pos = nl + 1;
    }

    const auto firstNl = original.find('\n');
    const std::string eol = firstNl != std::string::npos && firstNl > 0 && original[firstNl - 1] == '\r'
        ? "\r\n" : "\n";
    std::array<bool, settings.size()> seen {};
    std::string result = bom ? original.substr(0, 3) : std::string();
    for (std::size_t pos = start; pos < original.size();) {
        const auto nl = original.find('\n', pos);
        const auto end = nl == std::string::npos ? original.size() : nl;
        auto body = std::string_view(original).substr(pos, end - pos);
        const bool cr = !body.empty() && body.back() == '\r';
        if (cr) body.remove_suffix(1);
        const auto parsed = parse(body);
        std::size_t index = settings.size();
        for (std::size_t i = 0; i < settings.size(); ++i)
            if (parsed.key == settings[i].key) { index = i; break; }
        if (index == settings.size()) {
            result.append(body.data(), body.size());
        } else if (seen[index]) {
            // Preserve the old text as a comment, never as a later override.
            result += "# Duplicate replaced by iOS profile: ";
            result.append(body.data(), body.size());
        } else {
            seen[index] = true;
            result.append(body.data(), parsed.valueBegin);
            result += settings[index].value;
            result.append(body.data() + parsed.valueEnd, body.size() - parsed.valueEnd);
        }
        if (cr) result += '\r';
        if (nl == std::string::npos) break;
        result += '\n';
        pos = nl + 1;
    }
    for (std::size_t i = 0; i < settings.size(); ++i) {
        if (seen[i]) continue;
        if (!result.empty() && result.back() != '\n' && result.size() != start) result += eol;
        result += settings[i].key;
        result += " = ";
        result += settings[i].value;
        result += eol;
    }
    return {result, result != original};
}

} // namespace nectar_ios
#endif
