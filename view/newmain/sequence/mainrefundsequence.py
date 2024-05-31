local var_0_0 = class("MainRefundSequence")

def var_0_0.Execute(arg_1_0, arg_1_1):
	local var_1_0 = getProxy(UserProxy)

	if var_1_0.data.limitServerIds and #var_1_0.data.limitServerIds > 0:
		pg.m02.sendNotification(GAME.GET_REFUND_INFO, {
			def callback:()
				arg_1_0.ShowTip(arg_1_1)
		})
	else
		arg_1_1()

def var_0_0.ShowTip(arg_3_0, arg_3_1):
	if getProxy(PlayerProxy).getRefundInfo():
		local var_3_0 = getProxy(ServerProxy)
		local var_3_1 = True

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			modal = True,
			hideClose = True,
			content = i18n("Supplement_pay1"),
			def onYes:()
				if var_3_1:
					pg.m02.sendNotification(GAME.GO_SCENE, SCENE.BACK_CHARGE)
				else
					Application.Quit(),
			def onNo:()
				pg.m02.sendNotification(GAME.LOGOUT, {
					code = 0
				}),
			yesText = i18n("Supplement_pay4"),
			noText = i18n("word_back")
		})
	else
		arg_3_1()

return var_0_0
