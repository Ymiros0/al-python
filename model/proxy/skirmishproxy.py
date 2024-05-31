local var_0_0 = class("SkirmishProxy", import(".NetProxy"))

def var_0_0.register(arg_1_0):
	arg_1_0.data = {}

	arg_1_0.BuildSkirmishData()

var_0_0.SkirmishMap = 1250022

def var_0_0.BuildSkirmishData(arg_2_0):
	local var_2_0 = SkirmishVO.bindConfigTable()

	for iter_2_0, iter_2_1 in pairs(var_2_0.all):
		local var_2_1 = var_2_0[iter_2_1]
		local var_2_2 = SkirmishVO.New(var_2_1.id)

		table.insert(arg_2_0.data, var_2_2)

def var_0_0.TryFetchNewTask(arg_3_0):
	local var_3_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.ACTIVITY_ID_US_SKIRMISH_RE)

	if var_3_0 and not var_3_0.isEnd():
		return updateActivityTaskStatus(var_3_0)

def var_0_0.UpdateSkirmishProgress(arg_4_0):
	local var_4_0 = getProxy(TaskProxy)
	local var_4_1 = getProxy(ActivityProxy)
	local var_4_2 = arg_4_0.data
	local var_4_3 = var_4_1.getActivityById(ActivityConst.ACTIVITY_ID_US_SKIRMISH_RE)
	local var_4_4 = math.min(var_4_3.getDayIndex(), #var_4_2)
	local var_4_5 = False

	for iter_4_0 = #var_4_2, 1, -1:
		local var_4_6 = var_4_2[iter_4_0]
		local var_4_7 = var_4_6.getConfig("task_id")
		local var_4_8 = var_4_0.getTaskVO(var_4_7)
		local var_4_9

		if var_4_4 < iter_4_0:
			var_4_9 = SkirmishVO.StateInactive
		elif var_4_8:
			if var_4_8.isReceive():
				var_4_9 = SkirmishVO.StateClear
				var_4_5 = var_4_5 or iter_4_0 <= var_4_4
			elif not var_4_8.isFinish():
				var_4_9 = SkirmishVO.StateWorking
				var_4_5 = True
			else
				var_4_9 = SkirmishVO.StateWorking
				var_4_5 = True
		elif var_4_5:
			var_4_9 = SkirmishVO.StateClear
		else
			var_4_9 = SkirmishVO.StateActive

		var_4_6.SetState(var_4_9)

return var_0_0
