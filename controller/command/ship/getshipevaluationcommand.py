local var_0_0 = class("GetShipEvaluationCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().shipId

	pg.ConnectionMgr.GetInstance().Send(99999, {
		shipId = var_1_0
	}, 99999, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(BayProxy).getShipById(var_1_0)

			arg_1_0.sendNotification(GAME.GET_SHIP_EVALUATION_DONE, var_2_0)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("get_ship_evaluation", arg_2_0.result)))

return var_0_0
