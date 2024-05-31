local var_0_0 = class("ColoringClearCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.activityId
	local var_1_2 = var_1_0.id

	pg.ConnectionMgr.GetInstance().Send(26006, {
		act_id = var_1_1,
		id = var_1_2
	}, 26007, function(arg_2_0)
		if arg_2_0.result == 0:
			getProxy(ColoringProxy).getColorGroup(var_1_2).clearFill()
			arg_1_0.sendNotification(GAME.COLORING_CLEAR_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("coloring_clear", arg_2_0.result)))

return var_0_0
