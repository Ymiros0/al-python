local var_0_0 = class("GameRoomPileGameView", import("..BaseMiniGameView"))

def var_0_0.getUIName(arg_1_0):
	return "GameRoomPileGameUI"

def var_0_0.init(arg_2_0):
	arg_2_0.backBtn = arg_2_0.findTF("overview/back")

local var_0_1 = 7

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0.backBtn, function()
		arg_3_0.emit(var_0_0.ON_BACK), SFX_PANEL)

	arg_3_0.controller = PileGameController.New()

	arg_3_0.controller.view.SetUI(arg_3_0._go)

	local var_3_0 = arg_3_0.PackData()

	arg_3_0.controller.SetUp(var_3_0, function(arg_5_0, arg_5_1)
		if arg_5_1 < arg_5_0:
			arg_3_0.StoreDataToServer({
				arg_5_0
			})

		local var_5_0 = arg_3_0.GetMGHubData()

		arg_3_0.SendSuccess(arg_5_0))
	arg_3_0.controller.setGameStartCallback(function(arg_6_0)
		arg_3_0.openCoinLayer(arg_6_0))

def var_0_0.PackData(arg_7_0):
	local var_7_0 = arg_7_0.GetMGData().GetRuntimeData("elements")
	local var_7_1 = var_7_0 and var_7_0[1] or 0

	if arg_7_0.getGameRoomData():
		arg_7_0.gameHelpTip = arg_7_0.getGameRoomData().game_help

	return {
		highestScore = var_7_1,
		screen = Vector2(arg_7_0._tf.rect.width, arg_7_0._tf.rect.height),
		tip = arg_7_0.gameHelpTip
	}

def var_0_0.OnGetAwardDone(arg_8_0, arg_8_1):
	return

def var_0_0.onBackPressed(arg_9_0):
	if arg_9_0.controller.onBackPressed():
		return

	arg_9_0.emit(var_0_0.ON_BACK)

def var_0_0.willExit(arg_10_0):
	arg_10_0.controller.Dispose()

return var_0_0
