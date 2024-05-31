local var_0_0 = class("CommanderHomeSelCommanderPage", import(".CommanderHomeBaseSelPage"))

def var_0_0.getUIName(arg_1_0):
	return "CommanderHomeSelCommanderPage"

def var_0_0.OnCatteryUpdate(arg_2_0, arg_2_1):
	arg_2_0.cattery = arg_2_1

	arg_2_0.Update(arg_2_0.home, arg_2_1)

def var_0_0.OnInit(arg_3_0):
	var_0_0.super.OnInit(arg_3_0)

	arg_3_0.selectedID = -1

	onButton(arg_3_0, arg_3_0.okBtn, function()
		if arg_3_0.selectedID >= 0:
			arg_3_0.emit(CommanderHomeMediator.ON_SEL_COMMANDER, arg_3_0.cattery.id, arg_3_0.selectedID), SFX_PANEL)

def var_0_0.OnSelected(arg_5_0, arg_5_1):
	if arg_5_1.commanderVO:
		local var_5_0 = arg_5_1.commanderVO.id
		local var_5_1, var_5_2 = arg_5_0.Check(var_5_0)

		if var_5_1:
			if arg_5_0.mark:
				setActive(arg_5_0.mark, False)

			if arg_5_0.selectedID == var_5_0:
				arg_5_0.selectedID = 0
				arg_5_0.mark = None

				arg_5_0.emit(CatteryDescPage.CHANGE_COMMANDER, None)
			else
				setActive(arg_5_1.mark2, True)

				arg_5_0.mark = arg_5_1.mark2
				arg_5_0.selectedID = var_5_0

				arg_5_0.emit(CatteryDescPage.CHANGE_COMMANDER, arg_5_1.commanderVO)
		else
			pg.TipsMgr.GetInstance().ShowTips(var_5_2)

def var_0_0.Check(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_0.home.GetCatteries()

	for iter_6_0, iter_6_1 in ipairs(var_6_0):
		if iter_6_1.GetCommanderId() == arg_6_1 and iter_6_1.id != arg_6_0.cattery.id:
			return False, i18n("commander_is_in_cattery")

	return True

def var_0_0.CheckIncludeSelf(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_0.home.GetCatteries()

	for iter_7_0, iter_7_1 in ipairs(var_7_0):
		if iter_7_1.GetCommanderId() == arg_7_1:
			return False

	return True

def var_0_0.OnUpdateItem(arg_8_0, arg_8_1, arg_8_2):
	var_0_0.super.OnUpdateItem(arg_8_0, arg_8_1, arg_8_2)

	local var_8_0 = arg_8_1 + 1
	local var_8_1 = arg_8_0.displays[var_8_0]
	local var_8_2 = arg_8_0.cards[arg_8_2]

	if var_8_1:
		local var_8_3 = arg_8_0.selectedID == var_8_1.id

		setActive(var_8_2.mark2, var_8_3)

		if var_8_3:
			arg_8_0.mark = var_8_2.mark2

		local var_8_4 = arg_8_0.CheckIncludeSelf(var_8_1.id)

		setActive(var_8_2._tf.Find("info/home"), not var_8_4)

def var_0_0.Update(arg_9_0, arg_9_1, arg_9_2):
	arg_9_0.Show()

	arg_9_0.home = arg_9_1
	arg_9_0.cattery = arg_9_2

	local var_9_0 = arg_9_2.GetCommanderId()

	if var_9_0 != 0:
		arg_9_0.selectedID = var_9_0

	var_0_0.super.Update(arg_9_0)

def var_0_0.Hide(arg_10_0):
	var_0_0.super.Hide(arg_10_0)

	arg_10_0.selectedID = -1
	arg_10_0.mark = None

return var_0_0
