local var_0_0 = class("BlackWhiteGridOPCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.activityId
	local var_1_3 = var_1_0.cmd
	local var_1_4 = var_1_0.score

	if var_1_4 < 0:
		return

	local var_1_5 = getProxy(ActivityProxy)
	local var_1_6 = var_1_5.getActivityById(var_1_2)

	if not var_1_6 or var_1_6.isEnd():
		return

	pg.ConnectionMgr.GetInstance().Send(11202, {
		cmd = 1,
		activity_id = var_1_2,
		arg1 = var_1_1,
		arg2 = var_1_4,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.award_list)

			if not table.contains(var_1_6.data1_list, var_1_1):
				table.insert(var_1_6.data1_list, var_1_1)

			local var_2_1 = table.indexof(var_1_6.data1_list, var_1_1)

			assert(var_2_1)

			var_1_6.data2_list[var_2_1] = var_1_4

			var_1_5.updateActivity(var_1_6)
			arg_1_0.sendNotification(GAME.BLACK_WHITE_GRID_OP_DONE, {
				awards = var_2_0
			})
		else
			originalPrint(arg_2_0.result))

return var_0_0
