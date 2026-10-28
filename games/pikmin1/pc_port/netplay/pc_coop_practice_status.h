#pragma once
#include "nectar_net/coop_session.h"
// Specific, non-spoiler messages for the disposable practice session. Never
// imply a campaign save or seamless rejoin is available.
inline const char* pc_practice_wait_message(const nectar::net::CoopView& view, int local) {
    using nectar::net::CoopBlock;
    const int other = local == 0 ? 1 : 0;
    const auto background=static_cast<std::uint8_t>(CoopBlock::Background);
    const auto settings=static_cast<std::uint8_t>(CoopBlock::Settings);
    const auto manual=static_cast<std::uint8_t>(CoopBlock::Manual);
    if (view.blockers[other] & background) return "Your partner left the game screen. Practice is paused until they return and both players are ready.";
    if (view.blockers[other] & settings) return "Your partner is in settings. Close settings, then both players can resume.";
    if (view.blockers[local] & settings) return "Close your settings to resume practice.";
    if (!view.ready[local] || (view.blockers[local] & manual)) return "Practice is paused. Tap Ready / Resume, then wait for your partner.";
    if (!view.ready[other] || (view.blockers[other] & manual)) return "You're ready. Waiting for your partner to tap Ready / Resume.";
    return "Practice is paused. Both players must be ready before the world continues.";
}
