#pragma once
extern "C" {void Jac_PlaySystemSe(int);void Jac_StopSystemSe(int);}

constexpr int JACSYS_Pause=3,JACSYS_Unpause=15;
extern "C" int Jac_PauseCheck();
