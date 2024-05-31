local var_0_0 = class("MergeTaskOneStepAwardCommand", pm.SimpleCommand)

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

		local function var_1_4(arg_2_0)
			for iter_2_0, iter_2_1 in ipairs(arg_2_0):
				table.insert(var_1_3, iter_2_1)

		seriesAsync({
			function(arg_3_0)
				if #var_1_1 <= 0:
					arg_3_0()

					return

				arg_1_0.sendNotification(GAME.SUBMIT_TASK_ONESTEP, {
					dontSendMsg = True,
					resultList = var_1_1,
					def callback:(arg_4_0)
						var_1_4(arg_4_0)
						arg_3_0()
				}),
			function(arg_5_0)
				if #var_1_2 <= 0:
					arg_5_0()

					return

				arg_1_0.sendNotification(GAME.BATCH_SUBMIT_WEEK_TASK, {
					dontSendMsg = True,
					ids = var_1_2,
					def callback:(arg_6_0)
						var_1_4(arg_6_0)
						arg_5_0()
				})
		}, function()
			local var_7_0 = _.map(var_1_1, function(arg_8_0)
				return arg_8_0.id)

			arg_1_0.sendNotification(GAME.MERGE_TASK_ONE_STEP_AWARD_DONE, {
				awards = var_1_3,
				taskIds = var_7_0
			}))

return var_0_0
