#pragma once
#ifdef __cplusplus
extern "C" {
#endif
// Presents an explicit connection-only test. Does not start/mutate a campaign.
void nectar_ios_open_coop_room(void);
// True only while the opaque native connection screen covers the game.
int nectar_ios_coop_room_is_open(void);
#ifdef __cplusplus
}
#endif
