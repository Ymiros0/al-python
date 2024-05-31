local var_0_0 = class("UpdateTaskProgressCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.taskId
	local var_1_2 = pg.task_data_template[var_1_1]
	local var_1_3
	local var_1_4
	local var_1_5 = getProxy(TaskProxy)
	local var_1_6 = var_1_5.getTaskById(var_1_1)

	if not var_1_6:
		return

	local var_1_7 = var_1_6.getConfig("sub_type")
	local var_1_8 = False

	if var_1_7 == 2001:
		var_1_3 = Task.TASK_PROGRESS_UPDATE

		local var_1_9 = var_1_2.target_id
		local var_1_10 = var_1_2.target_num
		local var_1_11 = getProxy(FleetProxy).getData()

		for iter_1_0, iter_1_1 in pairs(var_1_11):
			if (table.contains(var_1_9, iter_1_1.id) or #var_1_9 == 0) and iter_1_1.getShipCount() == var_1_10:
				var_1_8 = True

				break

		var_1_4 = var_1_10
	elif var_1_7 == 2002:
		var_1_3 = Task.TASK_PROGRESS_UPDATE

		local var_1_12 = var_1_2.target_id
		local var_1_13 = var_1_12[1]
		local var_1_14 = var_1_12[2]
		local var_1_15 = var_1_2.target_num
		local var_1_16 = getProxy(FleetProxy).getData()
		local var_1_17 = 0

		for iter_1_2, iter_1_3 in pairs(var_1_16):
			if iter_1_3.getShipCount() == var_1_14 and var_1_13 <= iter_1_3.avgLevel():
				var_1_17 = var_1_17 + 1

		if not var_1_6.isFinish() and var_1_17 > var_1_6.progress:
			var_1_8 = True
			var_1_4 = var_1_17
	elif var_1_7 == 2003:
		var_1_3 = Task.TASK_PROGRESS_UPDATE
		var_1_8 = True
		var_1_4 = 1
	elif var_1_7 == 2010 or var_1_7 == 2011:
		var_1_3 = Task.TASK_PROGRESS_APPEND
		var_1_8 = True
		var_1_4 = 1
	elif var_1_7 == 2012:
		var_1_3 = Task.TASK_PROGRESS_UPDATE
		var_1_4 = var_1_0.progress
		var_1_8 = True

	if not var_1_8:
		return

	local var_1_18 = {
		id = var_1_1,
		mode = var_1_3,
		progress = var_1_4
	}

	pg.ConnectionMgr.GetInstance().Send(20009, {
		progressinfo = {
			var_1_18
		}
	}, 20010, function(arg_2_0)
		if arg_2_0.result == 0:
			if var_1_3 == Task.TASK_PROGRESS_UPDATE:
				var_1_6.updateProgress(var_1_4)
			elif var_1_3 == Task.TASK_PROGRESS_APPEND:
				local var_2_0 = var_1_6.progress + var_1_4

				var_1_6.updateProgress(var_2_0)

			var_1_5.updateTask(var_1_6)
			arg_1_0.sendNotification(GAME.SHARE_TASK_FINISHED))

return var_0_0
