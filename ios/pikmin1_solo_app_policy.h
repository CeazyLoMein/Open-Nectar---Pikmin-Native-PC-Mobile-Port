#pragma once
#include <string_view>
namespace nectar_ios {
inline constexpr const char* solo_bundle_id(bool update) {
    return update ? "org.opennectar.experimental.pikmin1" : "org.opennectar.experimental.pikmin1.solotest";
}
inline constexpr const char* solo_storage_name(bool update) {
    return update ? "pikmin1" : "pikmin1-solo-test";
}
inline constexpr const char* solo_card_directory(bool update) {
    // Update shares current assets/settings, never the original campaign card.
    return update ? "save-solo-test" : "save";
}
inline bool solo_bundle_matches(std::string_view actual, std::string_view expected) {
    if (actual == expected) return true;
    // Installed CFBundleIdentifier may be original.id.TEAMID (confirmed on
    // this phone). Also accept a matching team wrapper, but never arbitrary IDs.
    constexpr std::size_t teamSize=10;
    const auto validTeam=[](std::string_view team) {
        if(team.size()!=10) return false;
        for(char c:team) if(!((c>='A'&&c<='Z')||(c>='0'&&c<='9'))) return false;
        return true;
    };
    if(actual.size()==expected.size()+teamSize+1)
        return actual.substr(0,expected.size())==expected && actual[expected.size()]=='.'
            && validTeam(actual.substr(expected.size()+1));
    if (actual.size()!=expected.size()+2*(teamSize+1)) return false;
    const auto team=actual.substr(0,teamSize);
    if(!validTeam(team)) return false;
    return actual[teamSize]=='.' && actual[actual.size()-teamSize-1]=='.'
        && actual.substr(teamSize+1,expected.size())==expected
        && actual.substr(actual.size()-teamSize)==team;
}
}
