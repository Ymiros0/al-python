﻿local var_0_0 = class("ActivityCrusingOPCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.callback
	local var_1_2 = getProxy(ActivityProxy)
	local var_1_3 = var_1_2:getActivityById(var_1_0.activity_id)

	if not var_1_3 or var_1_3:isEnd() then
		return
	end

	pg.ConnectionMgr.GetInstance():Send(11202, {
		activity_id = var_1_0.activity_id,
		cmd = var_1_0.cmd or 0,
		arg1 = var_1_0.arg1 or 0,
		arg2 = var_1_0.arg2 or 0,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = {}

			if var_1_0.cmd == 1 then
				-- block empty
			elseif var_1_0.cmd == 2 then
				var_2_0 = PlayerConst.addTranDrop(arg_2_0.award_list)

				table.insert(var_1_3.data1_list, var_1_0.arg1)
			elseif var_1_0.cmd == 3 then
				var_2_0 = PlayerConst.addTranDrop(arg_2_0.award_list)

				table.insert(var_1_3.data2_list, var_1_0.arg1)
			elseif var_1_0.cmd == 4 then
				var_2_0 = PlayerConst.addTranDrop(arg_2_0.award_list)
				var_1_3.data1_list = {}

				for iter_2_0, iter_2_1 in ipairs(pg.battlepass_event_pt[var_1_3.id].target) do
					if iter_2_1 <= var_1_3.data1 then
						table.insert(var_1_3.data1_list, iter_2_1)
					else
						break
					end
				end

				if var_1_3.data2 == 1 then
					var_1_3.data2_list = underscore.rest(var_1_3.data1_list, 1)
				end
			end

			var_1_2:updateActivity(var_1_3)
			arg_1_0:sendNotification(GAME.CRUSING_CMD_DONE, {
				awards = var_2_0,
				callback = var_1_1
			})
		else
			originalPrint(errorTip("", arg_2_0.result))
		end
	end)
end

return var_0_0
