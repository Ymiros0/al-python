local var_0_0 = class("ValentineQteGameView", import("..BaseMiniGameView"))

def var_0_0.getUIName(arg_1_0):
	return "ValentineQteGamePage"

def var_0_0.init(arg_2_0):
	arg_2_0.gameView = ValentineQteGamePage.New(arg_2_0._tf)

def var_0_0.didEnter(arg_3_0):
	local var_3_0 = arg_3_0.GetMGHubData().usedtime == 0

	arg_3_0.gameView.SetUp(function()
		if arg_3_0.GetMGHubData().count > 0:
			arg_3_0.SendSuccess(0), function()
		if arg_3_0.gameView:
			arg_3_0.gameView = None

		arg_3_0.emit(var_0_0.ON_BACK), var_3_0)

def var_0_0.onBackPressed(arg_6_0):
	if arg_6_0.gameView and arg_6_0.gameView.onBackPressed():
		return

	var_0_0.super.onBackPressed(arg_6_0)

def var_0_0.willExit(arg_7_0):
	if arg_7_0.gameView:
		arg_7_0.gameView.Destroy()

		arg_7_0.gameView = None

return var_0_0
