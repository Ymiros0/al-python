local var_0_0 = class("TaskOneStepSubmitOPCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().resultList

	if #var_1_0 > 0:
		local var_1_1 = {}
		local var_1_2 = {}

		for iter_1_0, iter_1_1 in ipairs(var_1_0):
			if iter_1_1.isWeekTask:
				table.insert(var_1_2, iter_1_1.id)
			else
				table.insert(var_1_1, iter_1_1)

		local var_1_3 = {}

		seriesAsync({
			function(arg_2_0)
				if #var_1_1 > 0:
					pg.m02.sendNotification(GAME.SUBMIT_TASK_ONESTEP, {
						resultList = var_1_0,
						callback = arg_2_0
					})
				else
					arg_2_0(),
			function(arg_3_0)
				if #var_1_2 > 0:
					arg_1_0.emit(TaskMediator.ON_BATCH_SUBMIT_WEEK_TASK, var_1_2, arg_3_0)
				else
					arg_3_0()
		})

return var_0_0
