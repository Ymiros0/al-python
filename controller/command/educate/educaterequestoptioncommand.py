local var_0_0 = class("EducateRequestOptionCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0 and var_1_0.callback

	pg.ConnectionMgr.GetInstance().Send(27045, {
		type = 1
	}, 27046, function(arg_2_0)
		if arg_2_0.result == 0:
			getProxy(EducateProxy).initRandomOpts(arg_2_0.opts)
			arg_1_0.sendNotification(GAME.EDUCATE_REQUEST_OPTION_DONE)

			if var_1_1:
				var_1_1()
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("educate request option data error. ", arg_2_0.result)))

return var_0_0
