﻿local var_0_0 = class("SenrankaguraTrainCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = getProxy(ActivityProxy):getActivityById(var_1_1)

	if not var_1_2 or var_1_2:isEnd() then
		return
	end

	pg.ConnectionMgr.GetInstance():Send(11202, {
		activity_id = var_1_1,
		cmd = var_1_0.cmd,
		arg1 = var_1_0.arg1 or 0,
		arg2 = var_1_0.arg2 or 0,
		arg3 = var_1_0.arg3 or 0,
		arg_list = var_1_0.arg_list or {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0 then
			if var_1_0.cmd == 1 then
				for iter_2_0, iter_2_1 in pairs(var_1_0.arg_list) do
					table.insert(var_1_2.data2_list, iter_2_1)
				end
			elseif var_1_0.cmd == 2 then
				var_1_2.data1_list[var_1_0.arg1] = var_1_2.data1_list[var_1_0.arg1] + 1
				var_1_2.data1 = var_1_2.data1 - var_1_0.cost

				for iter_2_2, iter_2_3 in pairs(var_1_0.arg_list) do
					table.insert(var_1_2.data2_list, iter_2_3)
				end
			end

			getProxy(ActivityProxy):updateActivity(var_1_2)

			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.award_list)

			arg_1_0:sendNotification(GAME.SENRANKAGURA_TRAIN_ACT_OP_DONE, var_2_0)
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end
	end)
end

return var_0_0
