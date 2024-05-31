local var_0_0 = class("CastleActivityCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = getProxy(ActivityProxy)
	local var_1_3 = var_1_2:getActivityById(var_1_1)

	if not var_1_3 or var_1_3:isEnd() then
		return
	end

	pg.ConnectionMgr.GetInstance():Send(11202, {
		activity_id = var_1_1,
		cmd = var_1_0.cmd,
		arg1 = var_1_0.arg1 or 0,
		arg2 = var_1_0.arg2 or 0,
		arg3 = var_1_0.arg3 or 0,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0 then
			if var_1_0.cmd == 1 then
				var_1_3.data1 = arg_2_0.number[2]

				if arg_2_0.number[1] <= 50 then
					var_1_3.data2 = var_1_3.data2 - 1
				end

				var_1_2:updateActivity(var_1_3)
				arg_1_0:sendNotification(GAME.CASTLE_DICE_OP_DONE, arg_2_0)
			elseif var_1_0.cmd == 2 then
				warning(#arg_2_0.number)

				var_1_3.data1 = arg_2_0.number[1]

				var_1_2:updateActivity(var_1_3)
				arg_1_0:sendNotification(GAME.CASTLE_STORY_OP_DONE, arg_2_0)
			elseif var_1_0.cmd == 3 then
				arg_1_0:sendNotification(GAME.CASTLE_FIRST_STORY_OP_DONE)
			end
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end
	end)
end

return var_0_0
