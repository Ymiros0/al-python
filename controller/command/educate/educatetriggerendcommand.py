local var_0_0 = class("EducateTriggerEndCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1

	var_1_1 = var_1_0 and var_1_0.callback

	local var_1_2 = var_1_0.id
	local var_1_3 = pg.child_ending[var_1_2].performance

	pg.ConnectionMgr.GetInstance().Send(27008, {ing_id = var_1_0.id
	}, 27009, function(arg_2_0)
		if arg_2_0.result == 0:
			getProxy(EducateProxy).AddEnding(var_1_0.id)
			pg.PerformMgr.GetInstance().PlayGroup(var_1_3, function()
				pg.PerformMgr.GetInstance().PlayOne(EducateConst.AFTER_END_PERFORM, function()
					getProxy(EducateProxy).CheckGuide("EducateScene")))
			arg_1_0.sendNotification(GAME.EDUCATE_TRIGGER_END_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("educate trigger end error. ", arg_2_0.result)))

return var_0_0
