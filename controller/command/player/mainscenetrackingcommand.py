local var_0_0 = class("MainSceneTrackingCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.trackType
	local var_1_2 = var_1_0.arg1
	local var_1_3 = var_1_0.arg2
	local var_1_4 = var_1_0.arg3
	local var_1_5 = var_1_0.arg4

	pg.ConnectionMgr.GetInstance().Send(11029, {
		track_typ = var_1_1,
		int_arg1 = var_1_2,
		int_arg2 = var_1_3,
		int_arg3 = var_1_4,
		str_arg1 = var_1_5
	})

return var_0_0
