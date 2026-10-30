#pragma once
#include <cstdint>
struct SVector_ {float x,y,z;};
extern "C" {
int Jac_DestroyEvent(int);int Jac_UpdateEventPosition(int,SVector_*);int Jac_CreateEvent(std::uint32_t,SVector_*);
int Jac_PlayEventAction(int,int);int Jac_StopEventAction(int,int);void Jac_InitAllEvent();
}
