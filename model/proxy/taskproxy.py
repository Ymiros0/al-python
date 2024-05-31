local var_0_0 = class("TaskProxy", import(".NetProxy"))

var_0_0.TASK_ADDED = "task added"
var_0_0.TASK_UPDATED = "task updated"
var_0_0.TASK_REMOVED = "task removed"
var_0_0.TASK_FINISH = "task finish"
var_0_0.TASK_PROGRESS_UPDATE = "task TASK_PROGRESS_UPDATE"
var_0_0.WEEK_TASK_UPDATED = "week task updated"
var_0_0.WEEK_TASKS_ADDED = "week tasks added"
var_0_0.WEEK_TASKS_DELETED = "week task deleted"
var_0_0.WEEK_TASK_RESET = "week task refresh"
mingshiTriggerId = 1
mingshiActivityId = 21
changdaoActivityId = 10006
changdaoTaskStartId = 5031

def var_0_0.register(arg_1_0):
	arg_1_0.on(20001, function(arg_2_0)
		arg_1_0.data = {}
		arg_1_0.finishData = {}
		arg_1_0.tmpInfo = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.info):
			local var_2_0 = Task.New(iter_2_1)

			if var_2_0.getConfigTable() != None:
				var_2_0.display("loaded")

				if var_2_0.getTaskStatus() != 2:
					arg_1_0.data[var_2_0.id] = var_2_0
				else
					arg_1_0.finishData[var_2_0.id] = var_2_0
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("task_notfound_error") .. tostring(iter_2_1.id))
				Debugger.LogWarning("Missing Task Config, id ." .. tostring(iter_2_1.id))

		getProxy(TechnologyProxy).updateBlueprintStates())
	arg_1_0.on(20002, function(arg_3_0)
		for iter_3_0, iter_3_1 in ipairs(arg_3_0.info):
			local var_3_0 = arg_1_0.data[iter_3_1.id]

			if var_3_0 != None:
				local var_3_1 = var_3_0.isFinish()

				var_3_0.progress = iter_3_1.progress

				arg_1_0.updateTask(var_3_0)

				if not var_3_1:
					arg_1_0.sendNotification(var_0_0.TASK_PROGRESS_UPDATE, var_3_0.clone())

		arg_1_0.sendNotification(GAME.TASK_PROGRESS_UPDATE))
	arg_1_0.on(20003, function(arg_4_0)
		for iter_4_0, iter_4_1 in ipairs(arg_4_0.info):
			local var_4_0 = Task.New(iter_4_1)

			arg_1_0.addTask(var_4_0))
	arg_1_0.on(20004, function(arg_5_0)
		for iter_5_0, iter_5_1 in ipairs(arg_5_0.id_list):
			arg_1_0.removeTaskById(iter_5_1))
	arg_1_0.on(20015, function(arg_6_0)
		local var_6_0 = arg_6_0.time

		arg_1_0.sendNotification(GAME.ZERO_HOUR))

	arg_1_0.taskTriggers = {}
	arg_1_0.weekTaskProgressInfo = WeekTaskProgress.New()

	arg_1_0.on(20101, function(arg_7_0)
		arg_1_0.weekTaskProgressInfo.Init(arg_7_0.info)
		arg_1_0.sendNotification(var_0_0.WEEK_TASK_RESET))
	arg_1_0.on(20102, function(arg_8_0)
		for iter_8_0, iter_8_1 in ipairs(arg_8_0.task):
			print("update sub task ", iter_8_1)

			local var_8_0 = WeekPtTask.New(iter_8_1)

			arg_1_0.weekTaskProgressInfo.UpdateSubTask(var_8_0)
			arg_1_0.sendNotification(var_0_0.WEEK_TASK_UPDATED, {
				id = var_8_0.id
			}))
	arg_1_0.on(20103, function(arg_9_0)
		for iter_9_0, iter_9_1 in ipairs(arg_9_0.id):
			print("add sub task ", iter_9_1)

			local var_9_0 = WeekPtTask.New({
				progress = 0,
				id = iter_9_1
			})

			arg_1_0.weekTaskProgressInfo.AddSubTask(var_9_0)

		arg_1_0.sendNotification(var_0_0.WEEK_TASKS_ADDED))
	arg_1_0.on(20104, function(arg_10_0)
		for iter_10_0, iter_10_1 in ipairs(arg_10_0.id):
			print("remove sub task ", iter_10_1)
			arg_1_0.weekTaskProgressInfo.RemoveSubTask(iter_10_1)

		arg_1_0.sendNotification(var_0_0.WEEK_TASKS_DELETED))
	arg_1_0.on(20105, function(arg_11_0)
		local var_11_0 = arg_11_0.pt

		arg_1_0.weekTaskProgressInfo.UpdateProgress(var_11_0))

	arg_1_0.submittingTask = {}

def var_0_0.GetWeekTaskProgressInfo(arg_12_0):
	return arg_12_0.weekTaskProgressInfo

def var_0_0.getTasksForBluePrint(arg_13_0):
	local var_13_0 = {}

	for iter_13_0, iter_13_1 in pairs(arg_13_0.data or {}):
		var_13_0[iter_13_1.id] = iter_13_1

	for iter_13_2, iter_13_3 in pairs(arg_13_0.finishData):
		var_13_0[iter_13_3.id] = iter_13_3

	return var_13_0

def var_0_0.addTmpTask(arg_14_0, arg_14_1):
	arg_14_0.tmpInfo[arg_14_1.id] = arg_14_1

def var_0_0.checkTmpTask(arg_15_0, arg_15_1):
	if arg_15_0.tmpInfo[arg_15_1]:
		arg_15_0.addTask(arg_15_0.tmpInfo[arg_15_1])

		arg_15_0.tmpInfo[arg_15_1] = None

def var_0_0.addTask(arg_16_0, arg_16_1):
	assert(isa(arg_16_1, Task), "should be an instance of Task")

	if arg_16_0.data[arg_16_1.id]:
		arg_16_0.addTmpTask(arg_16_1)

		return

	if arg_16_1.getConfigTable() == None:
		pg.TipsMgr.GetInstance().ShowTips(i18n("task_notfound_error") .. tostring(arg_16_1.id))
		Debugger.LogWarning("Missing Task Config, id ." .. tostring(arg_16_1.id))

		return

	arg_16_0.data[arg_16_1.id] = arg_16_1.clone()

	arg_16_0.data[arg_16_1.id].display("added")
	arg_16_0.data[arg_16_1.id].onAdded()
	arg_16_0.facade.sendNotification(var_0_0.TASK_ADDED, arg_16_1.clone())
	arg_16_0.checkAutoSubmitTask(arg_16_1)

def var_0_0.updateTask(arg_17_0, arg_17_1):
	assert(isa(arg_17_1, Task), "should be an instance of Task")

	local var_17_0 = arg_17_0.data[arg_17_1.id]

	assert(var_17_0 != None, "task should exist")

	arg_17_0.data[arg_17_1.id] = arg_17_1.clone()
	arg_17_0.data[arg_17_1.id].acceptTime = var_17_0.acceptTime

	arg_17_0.data[arg_17_1.id].display("updated")
	arg_17_0.facade.sendNotification(var_0_0.TASK_UPDATED, arg_17_1.clone())
	arg_17_0.checkAutoSubmitTask(arg_17_1)

def var_0_0.getTasks(arg_18_0):
	local var_18_0 = {}

	for iter_18_0, iter_18_1 in pairs(arg_18_0.data):
		table.insert(var_18_0, iter_18_1)

	return Clone(var_18_0)

def var_0_0.getTaskById(arg_19_0, arg_19_1):
	if arg_19_0.data[arg_19_1]:
		return arg_19_0.data[arg_19_1].clone()

def var_0_0.getFinishTaskById(arg_20_0, arg_20_1):
	if arg_20_0.finishData[arg_20_1]:
		return arg_20_0.finishData[arg_20_1].clone()

def var_0_0.getTaskVO(arg_21_0, arg_21_1):
	return arg_21_0.getTaskById(arg_21_1) or arg_21_0.getFinishTaskById(arg_21_1)

def var_0_0.getCanReceiveCount(arg_22_0):
	local var_22_0 = 0

	for iter_22_0, iter_22_1 in pairs(arg_22_0.data):
		if iter_22_1.ShowOnTaskScene() and iter_22_1.isFinish() and iter_22_1.isReceive() == False:
			var_22_0 = var_22_0 + 1

			local var_22_1 = iter_22_1.getConfig("award_display")

			for iter_22_2, iter_22_3 in ipairs(var_22_1):
				local var_22_2, var_22_3, var_22_4 = unpack(iter_22_3)

				if not LOCK_UR_SHIP and var_22_2 == DROP_TYPE_VITEM and Item.getConfigData(var_22_3).virtual_type == 20:
					local var_22_5 = pg.gameset.urpt_chapter_max.description[1]
					local var_22_6 = not LOCK_UR_SHIP and getProxy(BagProxy).GetLimitCntById(var_22_5) or 0
					local var_22_7 = not LOCK_UR_SHIP and pg.gameset.urpt_chapter_max.description[2] or 0

					if var_22_6 + var_22_4 - var_22_7 > 0:
						var_22_0 = var_22_0 - 1

	local var_22_8 = arg_22_0.GetWeekTaskProgressInfo()

	if var_22_8.CanUpgrade():
		var_22_0 = var_22_0 + 1

	return var_22_0 + var_22_8.GetCanSubmitSubTaskCnt()

def var_0_0.getNotFinishCount(arg_23_0, arg_23_1):
	local var_23_0 = arg_23_1 or 3
	local var_23_1 = 0

	for iter_23_0, iter_23_1 in pairs(arg_23_0.data):
		if iter_23_1.GetRealType() == var_23_0 and iter_23_1.isFinish() == False:
			var_23_1 = var_23_1 + 1

	return var_23_1

def var_0_0.removeTask(arg_24_0, arg_24_1):
	assert(isa(arg_24_1, Task), "should be an instance of Task")
	arg_24_0.removeTaskById(arg_24_1.id)

def var_0_0.removeTaskById(arg_25_0, arg_25_1):
	local var_25_0 = arg_25_0.data[arg_25_1]

	if var_25_0 == None:
		return

	arg_25_0.finishData[arg_25_1] = arg_25_0.data[arg_25_1].clone()
	arg_25_0.finishData[arg_25_1].submitTime = pg.TimeMgr.GetInstance().GetServerTime()
	arg_25_0.data[arg_25_1] = None

	arg_25_0.facade.sendNotification(var_0_0.TASK_REMOVED, var_25_0)
	arg_25_0.checkTmpTask(arg_25_1)

def var_0_0.getmingshiTaskID(arg_26_0, arg_26_1):
	local var_26_0 = pg.task_data_trigger[mingshiTriggerId]

	if arg_26_1 >= var_26_0.count:
		local var_26_1 = var_26_0.task_id

		if var_26_1 and not arg_26_0.getTaskVO(var_26_1):
			return var_26_1

	return 0

def var_0_0.dealMingshiTouchFlag(arg_27_0, arg_27_1):
	local var_27_0 = getProxy(ActivityProxy).getActivityById(mingshiActivityId)

	if not var_27_0 or var_27_0.isEnd():
		return

	local var_27_1 = var_27_0.getConfig("config_id")
	local var_27_2 = var_27_0.getConfig("config_data")[1]

	pg.MsgboxMgr.GetInstance().ShowMsgBox({
		hideNo = True,
		content = i18n("mingshi_task_tip_" .. arg_27_1)
	})

	local var_27_3 = arg_27_0.getTaskById(var_27_2)

	if var_27_3 and var_27_3.getTaskStatus() < 1:
		if not arg_27_0.mingshiTouchList:
			arg_27_0.mingshiTouchList = {}

		for iter_27_0, iter_27_1 in pairs(arg_27_0.mingshiTouchList):
			if iter_27_1 == arg_27_1:
				return

		for iter_27_2, iter_27_3 in pairs(var_27_0.data1_list):
			if iter_27_3 == arg_27_1:
				return

		table.insert(arg_27_0.mingshiTouchList, arg_27_1)
		arg_27_0.sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 2,
			activity_id = mingshiActivityId,
			arg1 = arg_27_1
		})

def var_0_0.mingshiTouchFlagEnabled(arg_28_0):
	local var_28_0 = getProxy(ActivityProxy).getActivityById(mingshiActivityId)

	if not var_28_0 or var_28_0.isEnd():
		return

	local var_28_1 = tonumber(var_28_0.getConfig("config_id"))
	local var_28_2 = tonumber(var_28_0.getConfig("config_data")[1])
	local var_28_3 = arg_28_0.getTaskById(var_28_2)

	if var_28_3 and var_28_3.getTaskStatus() < 1:
		return True

	if arg_28_0.getTaskVO(var_28_1):
		return False

	return True

def var_0_0.getAcademyTask(arg_29_0, arg_29_1):
	local var_29_0 = getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_TASK_LIST)
	local var_29_1 = _.detect(var_29_0, function(arg_30_0)
		local var_30_0 = arg_30_0.getTaskShip()

		return var_30_0 and var_30_0.groupId == arg_29_1)

	if var_29_1 and not var_29_1.isEnd():
		return getActivityTask(var_29_1, True)

def var_0_0.isFinishPrevTasks(arg_31_0, arg_31_1):
	local var_31_0 = Task.New({
		id = arg_31_1
	}).getConfig("open_need")

	if var_31_0 and type(var_31_0) == "table" and #var_31_0 > 0:
		return _.all(var_31_0, function(arg_32_0)
			local var_32_0 = arg_31_0.getTaskById(arg_32_0) or arg_31_0.getFinishTaskById(arg_32_0)

			return var_32_0 and var_32_0.isReceive())

	return True

def var_0_0.isReceiveTasks(arg_33_0, arg_33_1):
	return _.all(arg_33_1, function(arg_34_0)
		local var_34_0 = arg_33_0.getFinishTaskById(arg_34_0)

		return var_34_0 and var_34_0.isReceive())

def var_0_0.pushAutoSubmitTask(arg_35_0):
	for iter_35_0, iter_35_1 in pairs(arg_35_0.data):
		arg_35_0.checkAutoSubmitTask(iter_35_1)

def var_0_0.checkAutoSubmitTask(arg_36_0, arg_36_1):
	if arg_36_1.getConfig("auto_commit") == 1 and arg_36_1.isFinish():
		arg_36_0.sendNotification(GAME.SUBMIT_TASK, arg_36_1.id)

def var_0_0.addSubmittingTask(arg_37_0, arg_37_1):
	arg_37_0.submittingTask[arg_37_1] = True

def var_0_0.removeSubmittingTask(arg_38_0, arg_38_1):
	arg_38_0.submittingTask[arg_38_1] = None

def var_0_0.isSubmitting(arg_39_0, arg_39_1):
	return arg_39_0.submittingTask[arg_39_1]

def var_0_0.triggerClientTasks(arg_40_0):
	local var_40_0 = {}

	for iter_40_0, iter_40_1 in pairs(arg_40_0.data):
		if iter_40_1.isClientTrigger():
			table.insert(var_40_0, iter_40_1)

	return var_40_0

def var_0_0.GetBackYardInterActionTaskList(arg_41_0):
	local var_41_0 = {}

	for iter_41_0, iter_41_1 in pairs(arg_41_0.data):
		if iter_41_1.IsBackYardInterActionType():
			table.insert(var_41_0, iter_41_1)

	return var_41_0

def var_0_0.GetFlagShipInterActionTaskList(arg_42_0):
	local var_42_0 = {}

	for iter_42_0, iter_42_1 in pairs(arg_42_0.data):
		if iter_42_1.IsFlagShipInterActionType():
			table.insert(var_42_0, iter_42_1)

	return var_42_0

return var_0_0
