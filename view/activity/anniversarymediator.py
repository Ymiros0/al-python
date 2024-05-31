local var_0_0 = class("AnniversaryMediator", import("..base.ContextMediator"))

var_0_0.ON_SUBMIT_TASK = "AnniversaryMediator.ON_SUBMIT_TASK"
var_0_0.TO_TASK = "AnniversaryMediator.TO_TASK"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.TO_TASK, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.TASK_GO, {
			taskVO = arg_2_1
		}))
	arg_1_0.bind(var_0_0.ON_SUBMIT_TASK, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.SUBMIT_TASK, arg_3_1))

	local var_1_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.ANNIVERSARY_TASK_LIST_ID)

	arg_1_0.viewComponent.setActivity(var_1_0)
	arg_1_0.acceptTask(var_1_0)

	local var_1_1 = arg_1_0.getTaskByIds()

	arg_1_0.viewComponent.setTaskList(var_1_1)

def var_0_0.acceptTask(arg_4_0, arg_4_1):
	local var_4_0 = getProxy(TaskProxy)
	local var_4_1 = arg_4_1.getConfig("config_data")
	local var_4_2 = pg.TimeMgr.GetInstance()
	local var_4_3 = var_4_2.DiffDay(arg_4_1.data1, var_4_2.GetServerTime()) + 1
	local var_4_4 = math.clamp(var_4_3, 1, #var_4_1)
	local var_4_5 = arg_4_1.data3

	if var_4_5 == 0 or var_4_5 < var_4_4 and _.all(_.flatten({
		var_4_1[var_4_5]
	}), function(arg_5_0)
		return var_4_0.getFinishTaskById(arg_5_0) != None):
		arg_4_0.sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 1,
			activity_id = arg_4_1.id
		})

def var_0_0.getTaskByIds(arg_6_0):
	local var_6_0 = {}
	local var_6_1 = getProxy(TaskProxy)
	local var_6_2 = var_6_1.getData()

	for iter_6_0, iter_6_1 in pairs(var_6_2):
		var_6_0[iter_6_1.id] = iter_6_1

	local var_6_3 = var_6_1.finishData

	for iter_6_2, iter_6_3 in pairs(var_6_3):
		var_6_0[iter_6_3.id] = iter_6_3

	return var_6_0

def var_0_0.listNotificationInterests(arg_7_0):
	return {
		TaskProxy.TASK_ADDED,
		TaskProxy.TASK_UPDATED,
		TaskProxy.TASK_REMOVED,
		TaskProxy.TASK_FINISH,
		GAME.SUBMIT_TASK_DONE,
		ActivityProxy.ACTIVITY_UPDATED
	}

def var_0_0.handleNotification(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1.getName()
	local var_8_1 = arg_8_1.getBody()

	if var_8_0 == TaskProxy.TASK_ADDED or var_8_0 == TaskProxy.TASK_UPDATED or var_8_0 == TaskProxy.TASK_REMOVED or var_8_0 == TaskProxy.TASK_FINISH:
		local var_8_2 = arg_8_0.getTaskByIds()

		arg_8_0.viewComponent.setTaskList(var_8_2)
	elif var_8_0 == GAME.SUBMIT_TASK_DONE:
		local var_8_3 = getProxy(ActivityProxy).getActivityById(ActivityConst.ANNIVERSARY_TASK_LIST_ID)

		if arg_8_0.viewComponent.dateIndex and arg_8_0.viewComponent.dateIndex == var_8_3.data3:
			arg_8_0.viewComponent.updateTaskGroupDesc(var_8_3.data3)

		arg_8_0.viewComponent.updateBottomTaskGroup(var_8_3.data3)
		arg_8_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_8_1)
		arg_8_0.acceptTask(var_8_3)
	elif var_8_0 == ActivityProxy.ACTIVITY_UPDATED and var_8_1.id == ActivityConst.ANNIVERSARY_TASK_LIST_ID:
		arg_8_0.viewComponent.setActivity(var_8_1)
		arg_8_0.viewComponent.updateTaskGroups()
		arg_8_0.viewComponent.moveToTaskGroup(arg_8_0.viewComponent.date, None, True)

return var_0_0
