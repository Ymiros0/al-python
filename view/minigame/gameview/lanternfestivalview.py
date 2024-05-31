local var_0_0 = class("LanternFestivalView", import("..BaseMiniGameView"))

def var_0_0.getUIName(arg_1_0):
	return "LanternFestivalUI"

def var_0_0.didEnter(arg_2_0):
	arg_2_0.controller = LanternRiddlesController.New()

	arg_2_0.controller.view.SetUI(arg_2_0._tf)

	local function var_2_0()
		arg_2_0.emit(var_0_0.ON_BACK)

	local function var_2_1()
		arg_2_0.emit(var_0_0.ON_HOME)

	local function var_2_2()
		if arg_2_0.GetMGHubData().count > 0:
			arg_2_0.SendSuccess(0)

	local function var_2_3()
		local var_6_0 = arg_2_0.controller.GetSaveData()

		arg_2_0.StoreDataToServer(var_6_0)

	arg_2_0.controller.SetCallBack(var_2_0, var_2_1, var_2_2, var_2_3)

	local var_2_4 = arg_2_0.PackData()

	arg_2_0.controller.SetUp(var_2_4)

def var_0_0.PackData(arg_7_0):
	local var_7_0 = 15
	local var_7_1 = arg_7_0.GetMGHubData()
	local var_7_2 = arg_7_0.GetMGData().GetRuntimeData("elements")
	local var_7_3
	local var_7_4

	if var_7_2 and #var_7_2 > 0:
		var_7_3 = _.slice(var_7_2, 1, var_7_0)
		var_7_4 = _.slice(var_7_2, var_7_0 + 1, var_7_1.usedtime)
	else
		var_7_3 = {}

		for iter_7_0 = 1, var_7_0:
			table.insert(var_7_3, 0)

		var_7_4 = {}

	return {
		finishCount = var_7_1.usedtime,
		unlockCount = var_7_1.count,
		nextTimes = var_7_3,
		finishList = var_7_4
	}

def var_0_0.OnGetAwardDone(arg_8_0, arg_8_1):
	if arg_8_1.cmd == MiniGameOPCommand.CMD_COMPLETE:
		local var_8_0 = arg_8_0.GetMGHubData()
		local var_8_1 = var_8_0.ultimate
		local var_8_2 = var_8_0.usedtime
		local var_8_3 = var_8_0.getConfig("reward_need")

		if var_8_1 == 0 and var_8_3 <= var_8_2:
			pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
				hubid = var_8_0.id,
				cmd = MiniGameOPCommand.CMD_ULTIMATE,
				args1 = {}
			})

def var_0_0.willExit(arg_9_0):
	arg_9_0.controller.Dispose()

return var_0_0
