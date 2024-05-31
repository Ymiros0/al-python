local var_0_0 = class("LanternRiddlesController")

def var_0_0.Ctor(arg_1_0):
	arg_1_0.model = LanternRiddlesModel.New(arg_1_0)
	arg_1_0.view = LanternRiddlesView.New(arg_1_0)

def var_0_0.SetCallBack(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4):
	arg_2_0.exitCallback = arg_2_1
	arg_2_0.onHome = arg_2_2
	arg_2_0.onSuccess = arg_2_3
	arg_2_0.onSaveData = arg_2_4

def var_0_0.SetUp(arg_3_0, arg_3_1):
	arg_3_0.model.UpdateData(arg_3_1)

	local var_3_0 = arg_3_0.model.GetQuestiones()

	arg_3_0.view.UpdateDay(arg_3_0.model.finishCount)
	arg_3_0.view.InitLanternRiddles(var_3_0)

def var_0_0.SelectAnswer(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = False

	if arg_4_0.model.IsRight(arg_4_1, arg_4_2):
		var_4_0 = True

		arg_4_0.model.UpdateRightAnswerFlag(arg_4_1)

		if arg_4_0.onSuccess:
			arg_4_0.onSuccess()

		arg_4_0.view.UpdateDay(arg_4_0.model.finishCount)

		if arg_4_0.model.unlockCount <= 0:
			arg_4_0.view.RefreshLanterRiddles(arg_4_0.model.questiones)
	else
		arg_4_0.model.UpdateWrongAnswerFlag(arg_4_1, arg_4_2)

	if arg_4_0.onSaveData:
		arg_4_0.onSaveData()

	local var_4_1 = arg_4_0.model.GetQuestion(arg_4_1)

	arg_4_0.view.OnUpdateAnswer(var_4_1, arg_4_2, var_4_0)

def var_0_0.GetLockTime(arg_5_0):
	return arg_5_0.model.GetLockTime()

def var_0_0.ExitGame(arg_6_0):
	if arg_6_0.exitCallback:
		arg_6_0.exitCallback()

def var_0_0.ExitGameAndGoHome(arg_7_0):
	if arg_7_0.onHome:
		arg_7_0.onHome()

def var_0_0.GetSaveData(arg_8_0):
	local var_8_0 = {}

	for iter_8_0, iter_8_1 in ipairs(arg_8_0.model.questiones):
		table.insert(var_8_0, iter_8_1.nextTime)

	table.insert(var_8_0, arg_8_0.model.lockTime)

	local var_8_1 = arg_8_0.model.finishCount

	for iter_8_2, iter_8_3 in ipairs(arg_8_0.model.finishList):
		if var_8_1 > 0:
			table.insert(var_8_0, iter_8_3)

			var_8_1 = var_8_1 - 1

	return var_8_0

def var_0_0.Dispose(arg_9_0):
	arg_9_0.model.Dispose()
	arg_9_0.view.Dispose()

return var_0_0
