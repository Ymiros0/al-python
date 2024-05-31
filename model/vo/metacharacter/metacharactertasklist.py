local var_0_0 = class("MetaCharacterTaskList", import("..BaseVO"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_0.id
	arg_1_0.skillId = arg_1_0.getConfig("skill_ID")
	arg_1_0.taskList = {}

	local var_1_0 = arg_1_0.getConfig("skill_levelup_task")
	local var_1_1

	for iter_1_0, iter_1_1 in ipairs(var_1_0):
		local var_1_2 = MetaCharacterTask.New({
			taskId = iter_1_1[1],
			star = iter_1_1[2],
			level = iter_1_1[3],
			skillId = arg_1_0.skillId,
			prev = var_1_1,
			indexofList = iter_1_0
		})

		table.insert(arg_1_0.taskList, var_1_2)

		var_1_1 = var_1_2

def var_0_0.bindConfigTable(arg_2_0):
	return pg.ship_meta_skilltask

def var_0_0.getTaskList(arg_3_0):
	return arg_3_0.taskList

def var_0_0.getSkillId(arg_4_0):
	return arg_4_0.skillId

def var_0_0.getTaskByTaskId(arg_5_0, arg_5_1):
	return _.detect(arg_5_0.taskList, function(arg_6_0)
		return arg_5_1 == arg_6_0.id)

return var_0_0
