#ifndef _P2PORT_DOLPHIN_MTX_H
#define _P2PORT_DOLPHIN_MTX_H
// Explicitly load the canonical lowercase header. On case-insensitive
// Apple filesystems "Dolphin/mtx.h" can resolve back to this Mtx.h alias,
// leaving GameCube matrix types undefined.
#include "../../pikmin2-decomp/include/Dolphin/mtx.h"
#endif
