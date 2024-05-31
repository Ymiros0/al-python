local var_0_0 = class("ActivityTaskProxy", import(".NetProxy"))

function var_0_0.register(arg_1_0)
	arg_1_0.actTasks = {}
	arg_1_0.autoSubmitTasks = {}
end

function var_0_0.initActList(arg_2_0, arg_2_1, arg_2_2)
	if not arg_2_2 then
		return {}
	end

	local var_2_0 = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_2) do
		local var_2_1 = arg_2_0:createTask(arg_2_1, iter_2_1)

		table.insert(var_2_0, var_2_1)
	end

	table.insert(arg_2_0.actTasks, {
		actId = arg_2_1,
		tasks = var_2_0
	})
	arg_2_0:checkAutoSubmit()
end

function var_0_0.updateActList(arg_3_0, arg_3_1, arg_3_2)
	for iter_3_0, iter_3_1 in ipairs(arg_3_2) do
		for iter_3_2 = 1, #arg_3_0.actTasks do
			if arg_3_0.actTasks[iter_3_2].actId == arg_3_1 then
				for iter_3_3, iter_3_4 in ipairs(arg_3_0.actTasks[iter_3_2].tasks) do
					if iter_3_4.id == iter_3_1.id then
						iter_3_4:updateProgress(iter_3_1.progress)
					end
				end
			end
		end
	end

	arg_3_0:checkAutoSubmit()
end

function var_0_0.addActList(arg_4_0, arg_4_1, arg_4_2)
	for iter_4_0, iter_4_1 in ipairs(arg_4_2) do
		for iter_4_2 = 1, #arg_4_0.actTasks do
			if arg_4_0.actTasks[iter_4_2].actId == arg_4_1 then
				local var_4_0 = arg_4_0.actTasks[iter_4_2].tasks

				for iter_4_3 = #var_4_0, 1, -1 do
					if var_4_0[iter_4_3].id == iter_4_1.id then
						table.remove(var_4_0, iter_4_3)
					end
				end

				local var_4_1 = arg_4_0:createTask(arg_4_1, iter_4_1)

				table.insert(var_4_0, var_4_1)
			end
		end
	end

	arg_4_0:checkAutoSubmit()
end

function var_0_0.checkAutoSubmit(arg_5_0)
	if not arg_5_0.actTasks or #arg_5_0.actTasks == 0 then
		return
	end

	for iter_5_0 = 1, #arg_5_0.actTasks do
		local var_5_0 = arg_5_0.actTasks[iter_5_0].actId
		local var_5_1 = arg_5_0.actTasks[iter_5_0].tasks
		local var_5_2 = {}

		for iter_5_1, iter_5_2 in ipairs(var_5_1) do
			if iter_5_2.autoCommit and iter_5_2:isFinish() then
				if not table.contains(arg_5_0.autoSubmitTasks, iter_5_2.id) then
					table.insert(var_5_2, iter_5_2.id)
					table.insert(arg_5_0.autoSubmitTasks, iter_5_2.id)
				else
					warning("task_id" .. iter_5_2.id .. "已经存在于提交列表中，无需重复提交")
				end
			end
		end

		if #var_5_2 > 0 then
			arg_5_0:sendNotification(GAME.AVATAR_FRAME_AWARD, {
				act_id = var_5_0,
				task_ids = var_5_2
			})
		end
	end
end

function var_0_0.removeActList(arg_6_0, arg_6_1, arg_6_2)
	for iter_6_0, iter_6_1 in ipairs(arg_6_2) do
		for iter_6_2 = 1, #arg_6_0.actTasks do
			if arg_6_0.actTasks[iter_6_2].actId == arg_6_1 then
				local var_6_0 = arg_6_0.actTasks[iter_6_2].tasks

				for iter_6_3 = #var_6_0, 1, -1 do
					if var_6_0[iter_6_3].id == iter_6_1.id then
						if not var_6_0[iter_6_3]:isRepeated() then
							var_6_0[iter_6_3]:updateProgress(0)
						end

						if not var_6_0[iter_6_3]:isCircle() then
							table.remove(var_6_0, iter_6_3)
						end
					end
				end
			end
		end
	end
end

function var_0_0.getTaskById(arg_7_0, arg_7_1)
	for iter_7_0, iter_7_1 in ipairs(arg_7_0.actTasks) do
		if iter_7_1.actId == arg_7_1 then
			return Clone(iter_7_1.tasks)
		end
	end

	return {}
end

function var_0_0.getFinishTasksByActId(arg_8_0, arg_8_1)
	local var_8_0 = getProxy(ActivityProxy):getActivityById(arg_8_1)

	if not var_8_0 then
		return {}
	end

	local var_8_1 = var_8_0:GetFinishedTaskIds()

	return _.map(var_8_1, function(arg_9_0)
		local var_9_0 = ActivityTask.New(arg_8_1, {
			id = arg_9_0
		})

		var_9_0:setOver()

		return var_9_0
	end)
end

function var_0_0.checkTasksFinish(arg_10_0, arg_10_1, arg_10_2)
	local var_10_0 = {}

	for iter_10_0, iter_10_1 in ipairs(arg_10_0:getFinishTasksByActId(arg_10_1)) do
		var_10_0[iter_10_1.id] = true
	end

	return underscore.all(arg_10_2, function(arg_11_0)
		return var_10_0[arg_11_0.id]
	end)
end

function var_0_0.getTaskVOsByActId(arg_12_0, arg_12_1)
	local var_12_0 = arg_12_0:getTaskById(arg_12_1)

	table.insertto(var_12_0, arg_12_0:getFinishTasksByActId(arg_12_1))

	return var_12_0
end

function var_0_0.getActTaskTip(arg_13_0, arg_13_1)
	local var_13_0 = {}

	for iter_13_0, iter_13_1 in ipairs(arg_13_0.actTasks) do
		if iter_13_1.actId == arg_13_1 then
			var_13_0 = iter_13_1.tasks
		end
	end

	local var_13_1 = 0

	for iter_13_2, iter_13_3 in ipairs(var_13_0) do
		if not iter_13_3:isCircle() and not iter_13_3:isOver() and iter_13_3:isFinish() and not iter_13_3.autoCommit then
			var_13_1 = var_13_1 + 1
		end
	end

	return var_13_1 > 0
end

function var_0_0.createTask(arg_14_0, arg_14_1, arg_14_2)
	return (ActivityTask.New(arg_14_1, arg_14_2))
end

function var_0_0.getFinishTasks(arg_15_0)
	local var_15_0 = getProxy(ActivityProxy):GetTaskActivities()
	local var_15_1 = {}

	_.each(_.map(var_15_0, function(arg_16_0)
		return arg_15_0:getFinishTasksByActId(arg_16_0.id)
	end), function(arg_17_0)
		table.insertto(var_15_1, arg_17_0)
	end)

	return var_15_1
end

return var_0_0
