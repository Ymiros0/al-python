local var_0_0 = class("ActivityMemoryOPCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.actId
	local var_1_3 = getProxy(ActivityProxy)
	local var_1_4 = getProxy(ActivityProxy):getActivityById(var_1_2)
	local var_1_5 = var_1_0.awardCallback

	if not var_1_4 or var_1_4:isEnd() then
		return
	end

	if not table.contains(var_1_4.data1_list, var_1_1) then
		return
	end

	if table.contains(var_1_4.data2_list, var_1_1) then
		return
	end

	pg.ConnectionMgr.GetInstance():Send(11202, {
		cmd = 2,
		arg2 = 0,
		activity_id = var_1_2,
		arg1 = var_1_1,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0 then
			table.insert(var_1_4.data2_list, var_1_1)
			var_1_3:updateActivity(var_1_4)
			arg_1_0:sendNotification(GAME.MEMORYBOOK_UNLOCK_DONE, var_1_1)

			if arg_2_0.award_list then
				if var_1_5 then
					var_1_5(PlayerConst.addTranDrop(arg_2_0.award_list))
				else
					arg_1_0:sendNotification(GAME.MEMORYBOOK_UNLOCK_AWARD_DONE, {
						awards = PlayerConst.addTranDrop(arg_2_0.award_list)
					})
				end
			end
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end
	end)
end

return var_0_0
