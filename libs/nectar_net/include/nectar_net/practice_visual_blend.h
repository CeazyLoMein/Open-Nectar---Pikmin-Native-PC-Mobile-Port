#pragma once
#include "nectar_net/actor_frame.h"
namespace nectar::net {
// Presentation-only candidate: input must be two fully authenticated,
// validated frames from the SAME accepted session/scene. Never use its output
// as host simulation, input authority, collision, save, or reconnect state.
// Actors born/removed in the new frame take effect immediately; discontinuous
// movement snaps. On invalid arguments, output is left untouched.
bool blendPracticeVisualFrame(const ActorFrame& previous, const ActorFrame& next,
                              float fraction, float maxBlendDistance, ActorFrame& output);
}
