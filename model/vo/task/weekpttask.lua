﻿local var_0_0 = class("WeekPtTask", import(".Task"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.isWeekTask = true
end

function var_0_0.bindConfigTable(arg_2_0)
	return pg.weekly_task_template
end

function var_0_0.getConfig(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_0:bindConfigTable()[arg_3_0.configId]

	assert(var_3_0, arg_3_0.configId)

	if var_3_0[arg_3_1] then
		if arg_3_1 == "award_display" then
			return {
				var_3_0[arg_3_1]
			}
		else
			return var_3_0[arg_3_1]
		end
	elseif arg_3_1 == "name" or arg_3_1 == "story_id" or arg_3_1 == "story_icon" or arg_3_1 == "scene" then
		return ""
	elseif arg_3_1 == "type" then
		return 4
	elseif arg_3_1 == "level" or arg_3_1 == "visibility" then
		return 1
	elseif arg_3_1 == "priority_type" then
		return 0
	elseif arg_3_1 == "award_choice" then
		return nil
	else
		assert(false, "表 weekly_task_template 没有字段:" .. arg_3_1)
	end
end

function var_0_0.GetAward(arg_4_0)
	return arg_4_0:getConfig("award_display")[1]
end

function var_0_0.IsFinished(arg_5_0)
	return arg_5_0:isFinish()
end

return var_0_0
