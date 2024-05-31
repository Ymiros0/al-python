local var_0_0 = class("WeekPtTask", import(".Task"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.isWeekTask = True

def var_0_0.bindConfigTable(arg_2_0):
	return pg.weekly_task_template

def var_0_0.getConfig(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_0.bindConfigTable()[arg_3_0.configId]

	assert(var_3_0, arg_3_0.configId)

	if var_3_0[arg_3_1]:
		if arg_3_1 == "award_display":
			return {
				var_3_0[arg_3_1]
			}
		else
			return var_3_0[arg_3_1]
	elif arg_3_1 == "name" or arg_3_1 == "story_id" or arg_3_1 == "story_icon" or arg_3_1 == "scene":
		return ""
	elif arg_3_1 == "type":
		return 4
	elif arg_3_1 == "level" or arg_3_1 == "visibility":
		return 1
	elif arg_3_1 == "priority_type":
		return 0
	elif arg_3_1 == "award_choice":
		return None
	else
		assert(False, "表 weekly_task_template 没有字段." .. arg_3_1)

def var_0_0.GetAward(arg_4_0):
	return arg_4_0.getConfig("award_display")[1]

def var_0_0.IsFinished(arg_5_0):
	return arg_5_0.isFinish()

return var_0_0
