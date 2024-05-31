local var_0_0 = class("MainCheckShipNumSequence")

def var_0_0.Execute(arg_1_0, arg_1_1):
	local function var_1_0(arg_2_0)
		if arg_1_0.Check(arg_2_0):
			arg_1_1()

	pg.m02.sendNotification(GAME.GET_SHIP_CNT, {
		callback = var_1_0
	})

def var_0_0.Check(arg_3_0, arg_3_1):
	local var_3_0 = getProxy(BayProxy).getRawShipCount()
	local var_3_1 = arg_3_1 <= var_3_0

	if not var_3_1:
		originalPrint(arg_3_1, var_3_0)
		arg_3_0.ShowTip()

	return var_3_1

def var_0_0.ShowTip(arg_4_0):
	pg.MsgboxMgr.GetInstance().ShowMsgBox({
		modal = True,
		hideNo = True,
		hideClose = True,
		content = i18n("dockyard_data_loss_detected"),
		def onYes:()
			pg.m02.sendNotification(GAME.LOGOUT, {
				code = 0
			})
	})

return var_0_0
