local var_0_0 = class("CatteryOpAnimPage", import("....base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "CatteryOPAnimUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.homeExpAnim = CatteryAddHomeExpAnim.New(arg_2_0.findTF("bg/single"))
	arg_2_0.homeAndCommanderAnim = CattertAddHomeExpAndCommanderExpAnim.New(arg_2_0.findTF("bg/both"))

def var_0_0.OnInit(arg_3_0):
	return

def var_0_0.AddPlan(arg_4_0, arg_4_1):
	arg_4_0.RemoveTimer()
	arg_4_0.Show()

	local var_4_0, var_4_1, var_4_2, var_4_3 = arg_4_0.ParseData(arg_4_1)
	local var_4_4

	if #var_4_0 > 0:
		var_4_4 = arg_4_0.homeAndCommanderAnim
	else
		var_4_4 = arg_4_0.homeExpAnim

	if arg_4_0.player:
		arg_4_0.player.Clear()

		if arg_4_0.player != var_4_4:
			arg_4_0.player.Hide()

	arg_4_0.doAnim = True

	var_4_4.Action(var_4_0, var_4_1, var_4_2, var_4_3, function()
		arg_4_0.doAnim = False

		if arg_4_0.exited:
			return

		arg_4_0.timer = Timer.New(function()
			var_4_4.Hide()
			arg_4_0.Hide(), 0.5, 1)

		arg_4_0.timer.Start())

	arg_4_0.player = var_4_4

def var_0_0.ParseData(arg_7_0, arg_7_1):
	local var_7_0 = False
	local var_7_1 = False

	for iter_7_0, iter_7_1 in ipairs(arg_7_1.awards):
		if iter_7_1.id == Item.COMMANDER_QUICKLY_TOOL_ID:
			var_7_0 = True

		if iter_7_1.id == PlayerConst.ResDormMoney:
			var_7_1 = True

	return arg_7_1.commanderExps, arg_7_1.homeExp, var_7_0, var_7_1

def var_0_0.RemoveTimer(arg_8_0):
	if arg_8_0.timer:
		arg_8_0.timer.Stop()

		arg_8_0.timer = None

def var_0_0.OnDestroy(arg_9_0):
	arg_9_0.RemoveTimer()

	arg_9_0.doAnim = None

	arg_9_0.homeExpAnim.Dispose()
	arg_9_0.homeAndCommanderAnim.Dispose()

	arg_9_0.exited = True

return var_0_0
