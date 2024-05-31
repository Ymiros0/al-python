local var_0_0 = class("BeginStageCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().system

	pg.ConnectionMgr.GetInstance().Send(40005, {
		system = var_1_0
	}, 40006, function(arg_2_0)
		if arg_2_0.result == 0:
			-- block empty
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("stage_beginStage", arg_2_0.result)))

return var_0_0
