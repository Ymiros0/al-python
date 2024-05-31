local var_0_0 = class("SubmitTaskCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = arg_1_1.getType()
	local var_1_2
	local var_1_3 = {}
	local var_1_4 = getProxy(TaskProxy)
	local var_1_5 = True

	if type(var_1_0) == "number" or type(var_1_0) == "string":
		var_1_2 = var_1_0
	elif type(var_1_0) == "table":
		if var_1_0.normal_submit:
			var_1_5 = var_1_0.virtual != None and var_1_0.virtual
			var_1_2 = var_1_0.taskId
		else
			var_1_2 = var_1_0.taskId

			local var_1_6 = var_1_0.index
			local var_1_7 = var_1_4.getTaskById(var_1_2)

			assert(var_1_7.isSelectable())

			local var_1_8 = var_1_7.getConfig("award_choice")[var_1_6]

			for iter_1_0, iter_1_1 in ipairs(var_1_8):
				table.insert(var_1_3, {
					type = iter_1_1[1],
					id = iter_1_1[2],
					number = iter_1_1[3]
				})

	local var_1_9 = var_1_4.getTaskById(var_1_2)

	if not var_1_9:
		pg.TipsMgr.GetInstance().ShowTips(i18n("task_is_not_existence", var_1_2))

		if var_1_1:
			var_1_1(False)

		return

	if not var_1_9.isFinish():
		pg.TipsMgr.GetInstance().ShowTips(i18n("task_submitTask_error_notFinish"))

		if var_1_1:
			var_1_1(False)

		return

	if var_1_4.isSubmitting(var_1_2):
		return
	else
		var_1_4.addSubmittingTask(var_1_2)

	local var_1_10 = {}

	if var_1_9.IsOverflowShipExpItem() and not arg_1_0.InTaskScene():
		table.insert(var_1_10, function(arg_2_0)
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("player_expResource_mail_fullBag"),
				onYes = arg_2_0,
				def onNo:()
					var_1_4.removeSubmittingTask(var_1_2)

					if var_1_1:
						var_1_1(False)
			}))

	seriesAsync(var_1_10, function()
		pg.ConnectionMgr.GetInstance().Send(20005, {
			id = var_1_9.id,
			choice_award = var_1_3
		}, 20006, function(arg_5_0)
			var_1_4.removeSubmittingTask(var_1_2)

			if arg_5_0.result == 0:
				if var_1_9.getConfig("sub_type") == TASK_SUB_TYPE_GIVE_ITEM:
					local var_5_0 = tonumber(var_1_9.getConfig("target_id"))
					local var_5_1 = var_1_9.getConfig("target_num")

					getProxy(BagProxy).removeItemById(tonumber(var_5_0), tonumber(var_5_1))
				elif var_1_9.getConfig("sub_type") == TASK_SUB_TYPE_GIVE_VIRTUAL_ITEM:
					local var_5_2 = tonumber(var_1_9.getConfig("target_id"))
					local var_5_3 = var_1_9.getConfig("target_num")

					getProxy(ActivityProxy).removeVitemById(var_5_2, var_5_3)
				elif var_1_9.getConfig("sub_type") == TASK_SUB_TYPE_PLAYER_RES:
					local var_5_4 = tonumber(var_1_9.getConfig("target_id"))
					local var_5_5 = var_1_9.getConfig("target_num")
					local var_5_6 = getProxy(PlayerProxy)
					local var_5_7 = var_5_6.getData()

					var_5_7.consume({
						[id2res(var_5_4)] = var_5_5
					})
					var_5_6.updatePlayer(var_5_7)

				var_0_0.AddGuildLivness(var_1_9)

				local var_5_8 = PlayerConst.addTranDrop(arg_5_0.award_list, {
					taskId = var_1_9.id
				})

				if var_1_9.getConfig("type") == Task.TYPE_REFLUX:
					getProxy(RefluxProxy).addPtAfterSubTasks({
						var_1_9
					})

				if var_1_9.getConfig("type") != 8:
					var_1_4.removeTask(var_1_9)
				else
					var_1_9.submitTime = 1

					var_1_4.updateTask(var_1_9)

				if not var_1_5:
					for iter_5_0 = #var_5_8, 1, -1:
						if var_5_8[iter_5_0].type == DROP_TYPE_VITEM:
							table.remove(var_5_8, iter_5_0)

				arg_1_0.sendNotification(GAME.SUBMIT_TASK_DONE, var_5_8, {
					var_1_9.id
				})

				local var_5_9 = getProxy(ActivityProxy)
				local var_5_10 = var_5_9.getActivityByType(ActivityConst.ACTIVITY_TYPE_TASK_LIST_MONITOR)

				if var_5_10 and not var_5_10.isEnd():
					local var_5_11 = var_5_10.getConfig("config_data")[1] or {}

					if table.contains(var_5_11, var_1_9.id):
						var_5_9.monitorTaskList(var_5_10)

				if var_1_1:
					var_1_1(True)
			else
				pg.TipsMgr.GetInstance().ShowTips(errorTip("task_submitTask", arg_5_0.result))

				if var_1_1:
					var_1_1(False)))

def var_0_0.AddGuildLivness(arg_6_0):
	if arg_6_0.IsGuildAddLivnessType():
		local var_6_0 = getProxy(GuildProxy)
		local var_6_1 = var_6_0.getData()
		local var_6_2 = 0
		local var_6_3 = False

		if var_6_1 and arg_6_0.isGuildTask():
			var_6_1.setWeeklyTaskFlag(1)

			local var_6_4 = var_6_1.getWeeklyTask()

			if var_6_4:
				var_6_2 = var_6_4.GetLivenessAddition()

			var_6_3 = True
		elif arg_6_0.IsRoutineType():
			var_6_2 = pg.guildset.new_daily_task_guild_active.key_value
		elif arg_6_0.IsWeeklyType():
			var_6_2 = pg.guildset.new_weekly_task_guild_active.key_value

		if var_6_1 and var_6_2 and var_6_2 > 0:
			var_6_1.getMemberById(getProxy(PlayerProxy).getRawData().id).AddLiveness(var_6_2)

			var_6_3 = True

		if var_6_3:
			var_6_0.updateGuild(var_6_1)

def var_0_0.InTaskScene(arg_7_0):
	return getProxy(ContextProxy).getCurrentContext().mediator == TaskMediator

return var_0_0
