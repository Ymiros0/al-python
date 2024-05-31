local var_0_0 = class("NewBossExperimentResultStatisticsPage", import("..hpShareActBoss.NewHpShareActBossResultStatisticsPage"))

def var_0_0.GetTicketUseCount(arg_1_0):
	return 0

def var_0_0.UpdateTicket(arg_2_0, arg_2_1):
	var_0_0.super.UpdateTicket(arg_2_0, arg_2_1)

	local var_2_0 = arg_2_1.Find("playAgain/ticket/checkbox")

	triggerToggle(var_2_0, False)
	setToggleEnabled(var_2_0, False)

def var_0_0.OnPlayAgain(arg_3_0, arg_3_1):
	arg_3_0.emit(NewBattleResultMediator.REENTER_STAGE)

return var_0_0
