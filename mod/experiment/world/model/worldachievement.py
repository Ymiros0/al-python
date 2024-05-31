local var_0_0 = class("WorldAchievement", import("...BaseEntity"))

var_0_0.Fields = {
	triggers = "table",
	id = "number",
	config = "table"
}

def var_0_0.Setup(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1
	arg_1_0.config = pg.world_target_data[arg_1_0.id]

	assert(arg_1_0.config, "world_target_data not exist. " .. arg_1_0.id)

	local var_1_0 = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_0.config.condition):
		local var_1_1 = WorldTrigger.New()

		var_1_1.Setup(iter_1_1[1])

		var_1_1.progress = 0
		var_1_1.maxProgress = iter_1_1[2]
		var_1_1.desc = arg_1_0.config.condition_text[iter_1_0]

		table.insert(var_1_0, var_1_1)

	arg_1_0.triggers = var_1_0

def var_0_0.NetUpdate(arg_2_0, arg_2_1):
	local var_2_0
	local var_2_1 = {}

	_.each(arg_2_1, function(arg_3_0)
		local var_3_0 = arg_2_0.GetTrigger(arg_3_0.trigger_id)

		assert(var_3_0, "can not find trigger. " .. arg_3_0.trigger_id)

		if var_3_0:
			local var_3_1 = var_3_0.IsAchieved()

			var_3_0.progress = arg_3_0.count

			if not var_3_1 and var_3_0.IsAchieved():
				if #arg_2_0.triggers > 1:
					table.insert(var_2_1, var_3_0.GetDesc())

				if arg_2_0.IsAchieved():
					var_2_0 = arg_2_0)

	return var_2_1, var_2_0

def var_0_0.GetTrigger(arg_4_0, arg_4_1):
	return _.detect(arg_4_0.triggers, function(arg_5_0)
		return arg_5_0.id == arg_4_1)

def var_0_0.GetTriggers(arg_6_0):
	return arg_6_0.triggers

def var_0_0.IsAchieved(arg_7_0):
	return _.all(arg_7_0.triggers, function(arg_8_0)
		return arg_8_0.IsAchieved())

def var_0_0.GetProgress(arg_9_0):
	if #arg_9_0.triggers > 1:
		return _.reduce(arg_9_0.triggers, 0, function(arg_10_0, arg_10_1)
			return arg_10_0 + (arg_10_1.IsAchieved() and 1 or 0))
	else
		return arg_9_0.triggers[1].GetProgress()

def var_0_0.GetMaxProgress(arg_11_0):
	if #arg_11_0.triggers > 1:
		return #arg_11_0.triggers
	else
		return arg_11_0.triggers[1].GetMaxProgress()

return var_0_0
