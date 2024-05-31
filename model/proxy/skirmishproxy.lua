local var_0_0 = class("SkirmishProxy", import(".NetProxy"))

function var_0_0.register(arg_1_0)
	arg_1_0.data = {}

	arg_1_0:BuildSkirmishData()
end

var_0_0.SkirmishMap = 1250022

function var_0_0.BuildSkirmishData(arg_2_0)
	local var_2_0 = SkirmishVO.bindConfigTable()

	for iter_2_0, iter_2_1 in pairs(var_2_0.all) do
		local var_2_1 = var_2_0[iter_2_1]
		local var_2_2 = SkirmishVO.New(var_2_1.id)

		table.insert(arg_2_0.data, var_2_2)
	end
end

function var_0_0.TryFetchNewTask(arg_3_0)
	local var_3_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.ACTIVITY_ID_US_SKIRMISH_RE)

	if var_3_0 and not var_3_0:isEnd() then
		return updateActivityTaskStatus(var_3_0)
	end
end

function var_0_0.UpdateSkirmishProgress(arg_4_0)
	local var_4_0 = getProxy(TaskProxy)
	local var_4_1 = getProxy(ActivityProxy)
	local var_4_2 = arg_4_0.data
	local var_4_3 = var_4_1:getActivityById(ActivityConst.ACTIVITY_ID_US_SKIRMISH_RE)
	local var_4_4 = math.min(var_4_3:getDayIndex(), #var_4_2)
	local var_4_5 = false

	for iter_4_0 = #var_4_2, 1, -1 do
		local var_4_6 = var_4_2[iter_4_0]
		local var_4_7 = var_4_6:getConfig("task_id")
		local var_4_8 = var_4_0:getTaskVO(var_4_7)
		local var_4_9

		if var_4_4 < iter_4_0 then
			var_4_9 = SkirmishVO.StateInactive
		elseif var_4_8 then
			if var_4_8:isReceive() then
				var_4_9 = SkirmishVO.StateClear
				var_4_5 = var_4_5 or iter_4_0 <= var_4_4
			elseif not var_4_8:isFinish() then
				var_4_9 = SkirmishVO.StateWorking
				var_4_5 = true
			else
				var_4_9 = SkirmishVO.StateWorking
				var_4_5 = true
			end
		elseif var_4_5 then
			var_4_9 = SkirmishVO.StateClear
		else
			var_4_9 = SkirmishVO.StateActive
		end

		var_4_6:SetState(var_4_9)
	end
end

return var_0_0
