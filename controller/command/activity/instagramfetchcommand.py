local var_0_0 = class("InstagramFetchCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(ActivityProxy)
	local var_1_2 = var_1_1.getActivityById(var_1_0.activity_id)

	pg.ConnectionMgr.GetInstance().Send(11202, {
		cmd = 6,
		activity_id = var_1_0.activity_id,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = var_1_2.data1_list
			local var_2_1 = math.floor(#arg_2_0.number)

			for iter_2_0 = 1, var_2_1:
				var_1_2.data1_list[iter_2_0] = arg_2_0.number[iter_2_0]

			var_1_1.RegisterRequestTime(var_1_0.activity_id, pg.TimeMgr.GetInstance().GetServerTime())
			var_1_1.updateActivity(var_1_2)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
