local var_0_0 = class("MetaCharacterTask")

var_0_0.STATE_EMPTY = 1
var_0_0.STATE_START = 2
var_0_0.STATE_FINISHED = 3
var_0_0.STATE_SUBMITED = 4

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.taskId = arg_1_1.taskId
	arg_1_0.star = arg_1_1.star
	arg_1_0.level = arg_1_1.level
	arg_1_0.skillId = arg_1_1.skillId
	arg_1_0.isLearned = false
	arg_1_0.prevTask = arg_1_1.prev
	arg_1_0.indexOfTaskList = arg_1_1.indexofList
end

function var_0_0.setIsLearned(arg_2_0)
	arg_2_0.isLearned = true
end

function var_0_0.isLearnedTask(arg_3_0)
	return arg_3_0.isLearned
end

function var_0_0.CanFetch(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:getConfig("star")
	local var_4_1 = arg_4_1.level

	return var_4_0 >= arg_4_0.star and var_4_1 >= arg_4_0.level
end

function var_0_0.GetTask(arg_5_0)
	if arg_5_0:isLearnedTask() then
		return Task.New({
			submitTime = 1,
			id = arg_5_0.taskId
		})
	else
		return getProxy(TaskProxy):getTaskById(arg_5_0.taskId) or Task.New({
			id = arg_5_0.taskId
		})
	end
end

function var_0_0.GetDesc(arg_6_0)
	local var_6_0 = pg.skill_data_template[arg_6_0.skillId]

	if arg_6_0.isLearned then
		return i18n("meta_learn_skill", var_6_0.name)
	else
		return i18n1(var_6_0.name .. "Lv+1")
	end
end

function var_0_0.GetState(arg_7_0)
	local var_7_0 = getProxy(TaskProxy):getTaskVO(arg_7_0.taskId)

	if not var_7_0 then
		if arg_7_0:isLearnedTask() then
			return MetaCharacterTask.STATE_SUBMITED
		else
			return MetaCharacterTask.STATE_EMPTY
		end
	else
		local var_7_1 = var_7_0:isFinish()
		local var_7_2 = var_7_0:isReceive()

		if var_7_1 and var_7_2 then
			return MetaCharacterTask.STATE_SUBMITED
		elseif var_7_1 and not var_7_2 then
			return MetaCharacterTask.STATE_FINISHED
		else
			return MetaCharacterTask.STATE_START
		end
	end
end

return var_0_0
