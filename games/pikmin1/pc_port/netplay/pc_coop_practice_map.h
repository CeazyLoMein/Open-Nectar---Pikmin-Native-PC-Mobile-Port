#pragma once
class RandomAccessStream;
// Built-in, immutable practice terrain. Never reads a user-selected VS map,
// campaign generator, network path or downloaded content.
#define PC_COOP_PRACTICE_STAGE "stages/cooppractice.ini"
#define PC_COOP_PRACTICE_MOD "courses/cooppractice/map.mod"
const char* pc_coop_practice_map_prepare();
bool pc_coop_practice_map_path(const char* path);
RandomAccessStream* pc_coop_practice_map_open(const char* path);
