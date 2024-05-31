local var_0_0 = class("EducateGetPlansCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1

	var_1_1 = var_1_0 and var_1_0.callback

	pg.ConnectionMgr.GetInstance().Send(27012, {
		plans = var_1_0.plans
	}, 27013, function(arg_2_0)
		if arg_2_0.result == 0:
			getProxy(EducateProxy).GetPlanProxy().SetGridData(arg_2_0.plans)
			arg_1_0.sendNotification(GAME.EDUCATE_EXECUTE_PLANS, {
				isSkip = var_1_0.isSkip
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("educate get plans error. ", arg_2_0.result)))

return var_0_0
