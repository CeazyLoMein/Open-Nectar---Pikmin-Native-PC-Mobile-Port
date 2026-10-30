#pragma once
#include <cstdint>
constexpr int JACORIMA_Gather=8;
extern "C" {void Jac_StopOrimaSe(int);void Jac_PlayOrimaSe(std::uint32_t);void Jac_Orima_Formation(int,int);void Jac_Orima_Walk(int,std::uint32_t);}

void Jac_PauseOrimaSe();void Jac_UnPauseOrimaSe();
