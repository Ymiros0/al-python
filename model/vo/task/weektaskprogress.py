local var_0_0 = class("WeekTaskProgress", import("..BaseVO"))

def var_0_0.Ctor(arg_1_0):
	return

def var_0_0.Init(arg_2_0, arg_2_1):
	arg_2_0.targets = {}
	arg_2_0.dropData = {}
	arg_2_0.index = 0
	arg_2_0.target = 0
	arg_2_0.progress = 0
	arg_2_0.drops = {}
	arg_2_0.subTasks = {}
	arg_2_0.targets = pg.gameset.weekly_target.description
	arg_2_0.dropData = pg.gameset.weekly_drop_client.description
	arg_2_0.progress = arg_2_1.pt or 0

	for iter_2_0, iter_2_1 in ipairs(arg_2_1.task):
		local var_2_0 = WeekPtTask.New(iter_2_1)

		arg_2_0.subTasks[var_2_0.id] = var_2_0

	local var_2_1 = table.indexof(arg_2_0.targets, arg_2_1.reward_lv)

	arg_2_0.UpdateTarget(var_2_1 or 0)

def var_0_0.IsMaximum(arg_3_0):
	return arg_3_0.index >= #arg_3_0.targets

def var_0_0.UpdateTarget(arg_4_0, arg_4_1):
	arg_4_0.index = arg_4_1
	arg_4_0.target = arg_4_0.targets[arg_4_1 + 1] or arg_4_0.targets[#arg_4_0.targets]
	arg_4_0.drops = arg_4_0.dropData[arg_4_1 + 1] or arg_4_0.dropData[#arg_4_0.dropData]

def var_0_0.CanUpgrade(arg_5_0):
	return arg_5_0.progress >= arg_5_0.target and not arg_5_0.IsMaximum()

def var_0_0.Upgrade(arg_6_0):
	if arg_6_0.CanUpgrade():
		local var_6_0 = arg_6_0.index + 1

		arg_6_0.UpdateTarget(var_6_0)

def var_0_0.GetDropList(arg_7_0):
	return arg_7_0.drops

def var_0_0.GetPhase(arg_8_0):
	return math.min(arg_8_0.index + 1, #arg_8_0.targets)

def var_0_0.GetTotalPhase(arg_9_0):
	return #arg_9_0.targets

def var_0_0.GetProgress(arg_10_0):
	return arg_10_0.progress

def var_0_0.GetTarget(arg_11_0):
	return arg_11_0.target

def var_0_0.UpdateProgress(arg_12_0, arg_12_1):
	arg_12_0.progress = arg_12_1

def var_0_0.AddProgress(arg_13_0, arg_13_1):
	arg_13_0.progress = arg_13_0.progress + arg_13_1

def var_0_0.GetAllPhaseDrops(arg_14_0):
	return {
		resIcon = "Props/weekly_pt",
		type = 1,
		dropList = arg_14_0.dropData,
		targets = arg_14_0.targets,
		level = arg_14_0.index,
		count = arg_14_0.progress,
		resName = i18n("week_task_pt_name")
	}

def var_0_0.ReachMaxPt(arg_15_0):
	return arg_15_0.targets[#arg_15_0.targets] <= arg_15_0.progress

def var_0_0.GetSubTasks(arg_16_0):
	return arg_16_0.subTasks

def var_0_0.RemoveSubTasks(arg_17_0, arg_17_1):
	for iter_17_0, iter_17_1 in ipairs(arg_17_1):
		arg_17_0.RemoveSubTask(iter_17_1)

def var_0_0.RemoveSubTask(arg_18_0, arg_18_1):
	arg_18_0.subTasks[arg_18_1] = None

def var_0_0.AddSubTask(arg_19_0, arg_19_1):
	arg_19_0.subTasks[arg_19_1.id] = arg_19_1

def var_0_0.UpdateSubTask(arg_20_0, arg_20_1):
	assert(arg_20_0.subTasks[arg_20_1.id], "should exist task >> " .. arg_20_1.id)

	arg_20_0.subTasks[arg_20_1.id] = arg_20_1

def var_0_0.GetSubTask(arg_21_0, arg_21_1):
	return arg_21_0.subTasks[arg_21_1]

def var_0_0.AnySubTaskCanSubmit(arg_22_0):
	if arg_22_0.ReachMaxPt():
		return False

	for iter_22_0, iter_22_1 in pairs(arg_22_0.subTasks):
		if iter_22_1.isFinish():
			return True

	return False

def var_0_0.GetCanSubmitSubTaskCnt(arg_23_0):
	if arg_23_0.ReachMaxPt():
		return 0

	local var_23_0 = 0

	for iter_23_0, iter_23_1 in pairs(arg_23_0.subTasks):
		if iter_23_1.isFinish():
			var_23_0 = var_23_0 + 1

	return var_23_0

return var_0_0
