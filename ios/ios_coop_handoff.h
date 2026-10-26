#pragma once
#include <memory>
namespace nectar { namespace net { class CoopConnection; } }
// Future practice driver only; call on UIKit/main thread at its accepted start
// boundary, after it has arranged disposable scene loading. No active Start
// button calls this yet. Empty output required. On failure the room stays open.
// Success stops old UI polling, MOVES live room ownership to output, and closes
// only its screen. Caller becomes sole owner/poller and must pump while paused.
bool nectar_ios_coop_room_take_connection(std::unique_ptr<nectar::net::CoopConnection>& output);
