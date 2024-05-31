local var_0_0 = class("EducateTaskProxy")

var_0_0.TASK_ADDED = "EducateTaskProxy.TASK_ADDED"
var_0_0.TASK_REMOVED = "EducateTaskProxy.TASK_REMOVED"
var_0_0.TASK_UPDATED = "EducateTaskProxy.TASK_UPDATED"

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.binder = arg_1_1
	arg_1_0.data = {}
	arg_1_0.targetSetDays = {}

	for iter_1_0, iter_1_1 in ipairs(pg.gameset.child_target_set_date.description):
		arg_1_0.targetSetDays[iter_1_0] = EducateHelper.GetTimeFromCfg(iter_1_1)

def var_0_0.SetUp(arg_2_0, arg_2_1):
	arg_2_0.data = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_1.tasks or {}):
		arg_2_0.data[iter_2_1.id] = EducateTask.New(iter_2_1)

	arg_2_0.SetTarget(arg_2_1.targetId or 0)

	arg_2_0.finishMindTaskIds = arg_2_1.finishMindTaskIds
	arg_2_0.isGotTargetAward = arg_2_1.isGotTargetAward

def var_0_0.UpdateTargetAwardStatus(arg_3_0, arg_3_1):
	arg_3_0.isGotTargetAward = arg_3_1

def var_0_0.CanGetTargetAward(arg_4_0):
	return not arg_4_0.isGotTargetAward

def var_0_0.AddTask(arg_5_0, arg_5_1):
	local var_5_0 = EducateTask.New(arg_5_1)

	arg_5_0.data[var_5_0.id] = var_5_0

	if var_5_0.IsMind():
		EducateTipHelper.SetNewTip(EducateTipHelper.NEW_MIND_TASK)

	arg_5_0.binder.sendNotification(var_0_0.TASK_ADDED)

def var_0_0.RemoveTaskById(arg_6_0, arg_6_1):
	arg_6_0.data[arg_6_1] = None

	arg_6_0.binder.sendNotification(var_0_0.TASK_REMOVED)

def var_0_0.UpdateTask(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_0.data[arg_7_1.id]

	if var_7_0 == None:
		return

	var_7_0.progress = arg_7_1.progress

	arg_7_0.binder.sendNotification(var_0_0.TASK_UPDATED)

def var_0_0.GetTasksBySystem(arg_8_0, arg_8_1):
	local var_8_0 = {}

	for iter_8_0, iter_8_1 in pairs(arg_8_0.data):
		if iter_8_1.GetSystemType() == arg_8_1:
			table.insert(var_8_0, iter_8_1.clone())

	return var_8_0

def var_0_0.GetTaskById(arg_9_0, arg_9_1):
	return arg_9_0.data[arg_9_1] and arg_9_0.data[arg_9_1].clone() or None

def var_0_0.SetTarget(arg_10_0, arg_10_1):
	arg_10_0.targetId = arg_10_1

	if arg_10_0.targetId == 0:
		arg_10_0.targetTaskIds = {}
	else
		arg_10_0.targetTaskIds = pg.child_target_set[arg_10_0.targetId].ids

def var_0_0.GetTargetId(arg_11_0):
	return arg_11_0.targetId

def var_0_0.GetTargetSetDays(arg_12_0):
	return arg_12_0.targetSetDays

def var_0_0.CheckTargetSet(arg_13_0):
	if arg_13_0.targetId == 0:
		return True

	local var_13_0 = getProxy(EducateProxy).GetCurTime()

	for iter_13_0, iter_13_1 in pairs(arg_13_0.targetSetDays):
		if EducateHelper.IsSameDay(iter_13_1, var_13_0):
			return pg.child_target_set[arg_13_0.targetId].stage != iter_13_0

	return False

def var_0_0.GetTargetTasksForShow(arg_14_0):
	local var_14_0 = {}

	for iter_14_0, iter_14_1 in ipairs(arg_14_0.targetTaskIds):
		if arg_14_0.data[iter_14_1] and not arg_14_0.isGotTargetAward:
			table.insert(var_14_0, arg_14_0.GetTaskById(iter_14_1))
		else
			local var_14_1 = EducateTask.New({
				id = iter_14_1
			})

			var_14_1.SetRecieve()
			table.insert(var_14_0, var_14_1)

	return var_14_0

def var_0_0.GetMainTasksForShow(arg_15_0):
	local var_15_0 = {}

	for iter_15_0, iter_15_1 in ipairs(pg.child_task.all):
		if pg.child_task[iter_15_1].type_1 == EducateTask.STSTEM_TYPE_MAIN:
			if arg_15_0.data[iter_15_1]:
				table.insert(var_15_0, arg_15_0.GetTaskById(iter_15_1))
			else
				local var_15_1 = EducateTask.New({
					id = iter_15_1
				})

				if var_15_1.InTime():
					var_15_1.SetRecieve()
					table.insert(var_15_0, var_15_1)

	return var_15_0

def var_0_0.FilterByGroup(arg_16_0, arg_16_1, arg_16_2):
	local var_16_0 = {}

	for iter_16_0, iter_16_1 in ipairs(arg_16_1):
		local var_16_1 = iter_16_1.getConfig("group")

		if not var_16_0[var_16_1]:
			var_16_0[var_16_1] = {}

		table.insert(var_16_0[var_16_1], iter_16_1)

	local var_16_2 = {}

	for iter_16_2, iter_16_3 in pairs(var_16_0):
		table.sort(iter_16_3, CompareFuncs({
			function(arg_17_0)
				return arg_17_0.IsReceive() and 1 or 0,
			function(arg_18_0)
				return -arg_18_0.getConfig("order"),
			function(arg_19_0)
				return -arg_19_0.id
		}))

		if arg_16_2:
			if underscore.any(iter_16_3, function(arg_20_0)
				return not arg_20_0.IsReceive()):
				table.insert(var_16_2, iter_16_3[1])
		else
			table.insert(var_16_2, iter_16_3[1])

	table.sort(var_16_2, CompareFuncs({
		function(arg_21_0)
			return arg_21_0.IsReceive() and 1 or 0,
		function(arg_22_0)
			return arg_22_0.IsFinish() and 0 or 1,
		function(arg_23_0)
			return arg_23_0.getConfig("group"),
		function(arg_24_0)
			return -arg_24_0.id
	}))

	return var_16_2

def var_0_0.GetOtherTargetTaskProgress(arg_25_0):
	if arg_25_0.targetId == 0:
		return 0, 0

	local var_25_0 = pg.child_target_set[arg_25_0.targetId].target_progress
	local var_25_1 = pg.child_target_set[arg_25_0.targetId].ids

	return underscore.reduce(var_25_1, 0, function(arg_26_0, arg_26_1)
		return arg_26_0 + (arg_25_0.data[arg_26_1] and 0 or pg.child_task[arg_26_1].task_target_progress)), var_25_0

def var_0_0.GetMainTargetTaskProgress(arg_27_0):
	local var_27_0 = 0
	local var_27_1 = 0

	for iter_27_0, iter_27_1 in ipairs(pg.child_task.all):
		if pg.child_task[iter_27_1].type_1 == EducateTask.STSTEM_TYPE_MAIN:
			if arg_27_0.data[iter_27_1]:
				var_27_0 = var_27_0 + 1
			elif EducateTask.New({
				id = iter_27_1
			}).InTime():
				var_27_1 = var_27_1 + 1
				var_27_0 = var_27_0 + 1

	return var_27_1, var_27_0

def var_0_0.GetShowTargetTasks(arg_28_0):
	local var_28_0 = arg_28_0.FilterByGroup(arg_28_0.GetTargetTasksForShow())

	table.sort(var_28_0, CompareFuncs({
		function(arg_29_0)
			return arg_29_0.IsReceive() and 1 or 0,
		function(arg_30_0)
			return -arg_30_0.getConfig("order"),
		function(arg_31_0)
			return -arg_31_0.id
	}))

	return var_28_0

def var_0_0.GetSiteEnterAddTasks(arg_32_0, arg_32_1):
	local var_32_0 = {}

	for iter_32_0, iter_32_1 in pairs(arg_32_0.data):
		if iter_32_1.NeedAddProgressFromSiteEnter() and EducateHelper.IsMatchSubType(iter_32_1.getConfig("sub_type"), arg_32_1):
			table.insert(var_32_0, iter_32_1.clone())

	return var_32_0

def var_0_0.GetPerformAddTasks(arg_33_0, arg_33_1):
	local var_33_0 = {}

	for iter_33_0, iter_33_1 in pairs(arg_33_0.data):
		if iter_33_1.NeedAddProgressFromPerform() and EducateHelper.IsMatchSubType(iter_33_1.getConfig("sub_type"), arg_33_1):
			table.insert(var_33_0, iter_33_1.clone())

	return var_33_0

def var_0_0.OnNewWeek(arg_34_0):
	return

def var_0_0.IsShowMindTasksTip(arg_35_0):
	for iter_35_0, iter_35_1 in pairs(arg_35_0.data):
		if iter_35_1.IsMind() and iter_35_1.IsFinish():
			return True

	return False

def var_0_0.IsShowMainTasksTip(arg_36_0):
	local var_36_0 = arg_36_0.FilterByGroup(arg_36_0.GetMainTasksForShow())[1]

	return var_36_0 and not var_36_0.IsReceive() and var_36_0.IsFinish()

def var_0_0.IsShowTargetTasksTip(arg_37_0):
	for iter_37_0, iter_37_1 in pairs(arg_37_0.data):
		if iter_37_1.IsTarget() and iter_37_1.IsFinish():
			return True

	return False

def var_0_0.IsShowOtherTasksTip(arg_38_0):
	if arg_38_0.IsShowMainTasksTip():
		return True

	if arg_38_0.isGotTargetAward:
		return False

	local var_38_0, var_38_1 = arg_38_0.GetOtherTargetTaskProgress()

	if var_38_0 / var_38_1 >= 1:
		return True

	return arg_38_0.IsShowTargetTasksTip()

return var_0_0
