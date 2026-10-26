#include "netplay/pc_coop_practice_start.h"
#include "netplay/pc_coop_switch.h"
#include "pc_coop.h"
#include "CardUtil.h"
#include "MemoryCard.h"
#include "dolphin_stubs/pc_card_paths.h"

namespace {
PcCoopPracticeStart sPracticeStart = PcCoopPracticeStart::Idle;
}

PcCoopPracticeStart pc_coop_practice_start_state() { return sPracticeStart; }

bool pc_coop_practice_request_start(const char* scratchDirectory)
{
	if ((sPracticeStart != PcCoopPracticeStart::Idle && sPracticeStart != PcCoopPracticeStart::Failed)
	    || pc_coop_direct_requested() || pc_coop_direct_active() || pc_card_coop_practice_active()) return false;
	if (!CardUtilRequestCoopPractice(scratchDirectory)) return false;
	sPracticeStart = PcCoopPracticeStart::Draining;
	return true;
}

PcCoopPracticeStart pc_coop_practice_poll_start()
{
	if (sPracticeStart != PcCoopPracticeStart::Draining) return sPracticeStart;
	const PcCardPracticeAdmission admission = CardUtilPollCoopPractice();
	if (admission == PcCardPracticeAdmission::Ready && pc_card_coop_practice_active()) {
		// Fresh disposable area only. Never inherit the old online direct-slot
		// preference, import a normal campaign, or touch saved personal settings.
		pc_coop_direct_set_slot(0);
		pc_coop_set_captain(0, PC_CAPTAIN_OLIMAR);
		pc_coop_set_captain(1, PC_CAPTAIN_LOUIE);
		pc_coop_set_pending(true);
		pc_coop_direct_request();
		sPracticeStart = PcCoopPracticeStart::Armed;
	} else if (admission != PcCardPracticeAdmission::Draining) {
		sPracticeStart = PcCoopPracticeStart::Failed;
	}
	return sPracticeStart;
}

bool pc_coop_practice_cancel_start()
{
	if (sPracticeStart == PcCoopPracticeStart::Draining && CardUtilCancelCoopPractice()) {
		sPracticeStart = PcCoopPracticeStart::Idle;
		return true;
	}
	// Admission is irreversible within the process. Do not resume solo even
	// when the room disconnects in the small title -> setup transition window.
	if (sPracticeStart == PcCoopPracticeStart::Armed || sPracticeStart == PcCoopPracticeStart::Loading) {
		sPracticeStart = PcCoopPracticeStart::RestartRequired;
	}
	return false;
}

bool pc_coop_practice_prepare_setup(MemoryCard& card)
{
	if (sPracticeStart != PcCoopPracticeStart::Armed || !pc_card_coop_practice_active()
	    || pc_coop_direct_slot() != 0 || !card.pcResetForCoopPractice()) {
		if (pc_card_coop_practice_active()) sPracticeStart = PcCoopPracticeStart::RestartRequired;
		return false;
	}
	sPracticeStart = PcCoopPracticeStart::Loading;
	return true;
}

bool pc_coop_practice_restart_required()
{
	return sPracticeStart == PcCoopPracticeStart::Loading
	    || sPracticeStart == PcCoopPracticeStart::RestartRequired;
}
