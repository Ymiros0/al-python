local var_0_0 = class("EducateAddTaskProgressCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1

	var_1_1 = var_1_0 and var_1_0.callback

	pg.ConnectionMgr.GetInstance().Send(27037, {
		type_1 = var_1_0.system,
		progresses = var_1_0.progresses
	}, 27038, function(arg_2_0)
		if arg_2_0.result == 0:
			-- block empty
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("educate add task progress error. ", arg_2_0.result)))

return var_0_0
