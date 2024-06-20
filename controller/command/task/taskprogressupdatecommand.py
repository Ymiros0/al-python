local var_0_0 = class("TaskProgressUpdateCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	arg_1_0.CheckAndSubmitVoteTask()

def var_0_0.CheckAndSubmitVoteTask(arg_2_0, arg_2_1):
	local var_2_0 = getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_VOTE)

	for iter_2_0, iter_2_1 in pairs(var_2_0):
		if not iter_2_1.isEnd():
			local var_2_1 = arg_2_0.GetCanSubmitVoteTaskList(iter_2_1)

			arg_2_0.SubmitTaskList(var_2_1)

def var_0_0.GetCanSubmitVoteTaskList(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.getConfig("config_id")
	local var_3_1 = pg.activity_vote[var_3_0]

	assert(var_3_1, arg_3_1.id .. "-" .. var_3_0)

	local var_3_2 = _.flatten(var_3_1.task_period)
	local var_3_3 = {}

	for iter_3_0, iter_3_1 in ipairs(var_3_2):
		local var_3_4 = getProxy(TaskProxy).getTaskById(iter_3_1)

		if var_3_4 and var_3_4.isFinish() and not var_3_4.isReceive():
			table.insert(var_3_3, var_3_4)

	return var_3_3

def var_0_0.SubmitTaskList(arg_4_0, arg_4_1):
	if #arg_4_1 <= 0:
		return

	for iter_4_0, iter_4_1 in pairs(arg_4_1):
		arg_4_0.sendNotification(GAME.SUBMIT_TASK, iter_4_1.id)

return var_0_0