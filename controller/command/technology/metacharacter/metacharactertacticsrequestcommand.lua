local var_0_0 = class("MetaCharacterTacticsRequestCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody().id

	print("63313 request tactics info")
	pg.ConnectionMgr.GetInstance():Send(63313, {
		ship_id = var_1_0
	}, 63314, function(arg_2_0)
		print("63314 requset success")

		local var_2_0 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.tasks or {}) do
			local var_2_1 = iter_2_1.skill_id

			if not var_2_0[var_2_1] then
				var_2_0[var_2_1] = {}
			end

			table.insert(var_2_0[var_2_1], {
				taskID = iter_2_1.task_id,
				finishCount = iter_2_1.finish_cnt
			})
		end

		local var_2_2 = {}

		for iter_2_2, iter_2_3 in ipairs(arg_2_0.skill_exp or {}) do
			var_2_2[iter_2_3.skill_id] = iter_2_3.exp

			print("skill", iter_2_3.skill_id, iter_2_3.exp)
		end

		local var_2_3 = {
			shipID = arg_2_0.ship_id,
			doubleExp = arg_2_0.double_exp,
			normalExp = arg_2_0.exp,
			curSkillID = arg_2_0.skill_id or 0,
			switchCount = arg_2_0.switch_cnt,
			taskInfoTable = var_2_0,
			skillExpTable = var_2_2
		}

		getProxy(MetaCharacterProxy):setMetaTacticsInfo(arg_2_0)
		arg_1_0:sendNotification(GAME.TACTICS_META_INFO_REQUEST_DONE, var_2_3)
	end)
end

return var_0_0
