local var_0_0 = class("ActivityStoreDataCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.callback
	local var_1_2 = var_1_0.activity_id
	local var_1_3 = getProxy(ActivityProxy):getActivityById(var_1_0.activity_id)

	if not var_1_3 or var_1_3:isEnd() then
		return
	end

	local var_1_4 = var_1_0.intValue or 0
	local var_1_5 = var_1_0.strValue or ""

	pg.ConnectionMgr.GetInstance():Send(26160, {
		act_id = var_1_2,
		int_value = var_1_4,
		str_value = var_1_5
	}, 26161, function(arg_2_0)
		if arg_2_0.result == 0 then
			var_1_3.data1 = var_1_4
			var_1_3.str_data1 = var_1_5

			getProxy(ActivityProxy):updateActivity(var_1_3)

			if var_1_1 then
				var_1_1()
			end
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end
	end)
end

return var_0_0
