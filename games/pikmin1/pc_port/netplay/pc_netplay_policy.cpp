#include "netplay/pc_coop_practice_runtime.h"
// Netplay sim-visibility policy. Engine-free.

#include "netplay/pc_netplay_policy.h"
#include "netplay/pc_netplay_det.h"

bool pc_netplay_sim_visible(bool frustumResult)
{
	if (pc_netplay_deterministic() || pc_coop_practice_remote_input(1)) {
		return true;
	}
	return frustumResult;
}

float pc_netplay_sim_aspect(float liveAspect)
{
	if (pc_netplay_deterministic()) {
		return 16.0f / 9.0f;
	}
	return liveAspect;
}

float pc_netplay_sim_lod_distance(float liveDistance)
{
	if (pc_netplay_deterministic() || pc_coop_practice_remote_input(1)) {
		return 0.0f;
	}
	return liveDistance;
}
