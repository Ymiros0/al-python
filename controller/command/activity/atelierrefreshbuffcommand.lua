local var_0_0 = class("AtelierRefreshBuffCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1.body
	local var_1_1 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_ATELIER_LINK)

	assert(var_1_1)

	local var_1_2 = {}

	table.Foreach(var_1_0, function(arg_2_0, arg_2_1)
		if arg_2_1[1] == 0 then
			return
		end

		table.insert(var_1_2, {
			pos = arg_2_0,
			itemid = arg_2_1[1],
			itemnum = arg_2_1[2]
		})
	end)
	pg.ConnectionMgr.GetInstance():Send(26055, {
		act_id = var_1_1.id,
		slots = var_1_2
	}, 26056, function(arg_3_0)
		if arg_3_0.result == 0 then
			var_1_1 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_ATELIER_LINK)

			var_1_1:UpdateBuffSlots(var_1_2)
			getProxy(ActivityProxy):updateActivity(var_1_1)
			arg_1_0:sendNotification(GAME.UPDATE_ATELIER_BUFF_DONE, var_1_1)
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_3_0.result))
		end
	end)
end

return var_0_0
