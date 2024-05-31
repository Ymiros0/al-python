local var_0_0 = class("NewHpShareActBossResultStatisticsPage", import("..activityBoss.NewActivityBossResultStatisticsPage"))

def var_0_0.UpdateGrade(arg_1_0):
	local var_1_0 = "battlescore/grade_label_clear"

	LoadImageSpriteAsync(var_1_0, arg_1_0.gradeTxt, False)
	setActive(arg_1_0.gradeIcon, False)

def var_0_0.UpdateTicket(arg_2_0, arg_2_1):
	var_0_0.super.UpdateTicket(arg_2_0, arg_2_1)

	local var_2_0 = arg_2_1.Find("playAgain/ticket/checkbox")

	triggerToggle(var_2_0, True)
	setToggleEnabled(var_2_0, False)

def var_0_0.EnoughTicketCount(arg_3_0):
	local var_3_0 = arg_3_0.GetTicketItemID(arg_3_0.contextData.actId)

	return getProxy(PlayerProxy).getRawData().getResource(var_3_0) > 0

def var_0_0.OnPlayAgain(arg_4_0, arg_4_1):
	if arg_4_0.IsLastBonus():
		arg_4_0.PassMsgbox("lastBonus", {
			content = i18n("expedition_drop_use_out")
		}, arg_4_1)

		return

	if not arg_4_0.EnoughTicketCount():
		arg_4_1()
		pg.TipsMgr.GetInstance().ShowTips(i18n("stage_beginStage_error_noTicket"))

		return

	local var_4_0, var_4_1 = arg_4_0.NotEnoughOilCost()

	if var_4_0:
		arg_4_0.PassMsgbox("oil", var_4_1, arg_4_1)

		return

	if arg_4_0.NotEnoughShipBag():
		arg_4_0.PassMsgbox("shipCapacity", None, arg_4_1)

		return

	local var_4_2, var_4_3 = arg_4_0.NotEnoughEnergy()

	if var_4_2:
		arg_4_0.PassMsgbox("energy", var_4_3, arg_4_1)

		return

	arg_4_0.emit(NewBattleResultMediator.REENTER_STAGE)

return var_0_0
