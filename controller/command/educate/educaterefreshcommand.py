local var_0_0 = class("EducateRefreshCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1

	var_1_1 = var_1_0 and var_1_0.callback

	pg.ConnectionMgr.GetInstance().Send(27047, {
		type = 1
	}, 27048, function(arg_2_0)
		if arg_2_0.result == 0:
			getProxy(EducateProxy).Refresh(function()
				arg_1_0.sendNotification(GAME.EDUCATE_REFRESH_DONE))
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("educate refresh error. ", arg_2_0.result)))

return var_0_0
