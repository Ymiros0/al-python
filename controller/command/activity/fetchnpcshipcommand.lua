local var_0_0 = class("FetchNpcShipCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.taskId
	local var_1_2 = var_1_0.callback
	local var_1_3 = getProxy(TaskProxy)
	local var_1_4 = var_1_3:getTaskById(var_1_1)

	if not var_1_4 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("task_is_not_existence", var_1_1))

		return
	end

	if not var_1_4:isFinish() then
		pg.TipsMgr.GetInstance():ShowTips(i18n("task_submitTask_error_notFinish"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(20005, {
		id = var_1_4.id,
		choice_award = {}
	}, 20006, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = {}

			for iter_2_0, iter_2_1 in ipairs(arg_2_0.award_list) do
				table.insert(var_2_0, Drop.New({
					type = iter_2_1.type,
					id = iter_2_1.id,
					count = iter_2_1.number
				}))
			end

			var_1_4.submitTime = 1

			var_1_3:updateTask(var_1_4)
			arg_1_0:sendNotification(GAME.FETCH_NPC_SHIP_DONE, {
				items = var_2_0,
				callback = var_1_2
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("task_submitTask", arg_2_0.result))
		end
	end)
end

return var_0_0
