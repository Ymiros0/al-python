local var_0_0 = class("EducateRequestCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0 and var_1_0.callback

	pg.ConnectionMgr.GetInstance().Send(27000, {
		type = 1
	}, 27001, function(arg_2_0)
		if arg_2_0.result == 0:
			getProxy(EducateProxy).initData(arg_2_0)

			if var_1_1:
				var_1_1()
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("educate request error. ", arg_2_0.result)))

return var_0_0
