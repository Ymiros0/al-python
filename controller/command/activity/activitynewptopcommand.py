local var_0_0 = class("ActivityNewPtOPCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.callback
	local var_1_2 = getProxy(ActivityProxy)
	local var_1_3 = var_1_2.getActivityById(var_1_0.activity_id)

	if not var_1_3 or var_1_3.isEnd():
		return

	pg.ConnectionMgr.GetInstance().Send(11202, {
		activity_id = var_1_0.activity_id,
		cmd = var_1_0.cmd or 0,
		arg1 = var_1_0.arg1 or 0,
		arg2 = var_1_0.arg2 or 0,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = {}

			if var_1_0.cmd == 1:
				var_2_0 = PlayerConst.addTranDrop(arg_2_0.award_list)
				var_1_3 = var_1_2.getActivityById(var_1_0.activity_id)

				table.insert(var_1_3.data1_list, var_1_0.arg1)

				if var_1_3.getConfig("type") == ActivityConst.ACTIVITY_TYPE_PIZZA_PT and var_1_0.arg2 and var_1_0.arg2 > 0:
					table.insert(var_1_3.data2_list, var_1_0.arg2)
			elif var_1_0.cmd == 2:
				var_1_3.data3 = arg_2_0.number[1]
			elif var_1_0.cmd == 3:
				var_2_0 = PlayerConst.addTranDrop(arg_2_0.award_list)
				var_1_3 = var_1_2.getActivityById(var_1_0.activity_id)

				if var_1_0.arg1 and var_1_0.arg1 > 0:
					table.insert(var_1_3.data2_list, var_1_0.arg1)

				local var_2_1 = var_1_0.oldBuffId or 0

				for iter_2_0, iter_2_1 in ipairs(var_1_3.data3_list):
					if iter_2_1 == var_2_1:
						var_1_3.data3_list[iter_2_0] = var_1_0.arg2
			elif var_1_0.cmd == 4:
				var_2_0 = PlayerConst.addTranDrop(arg_2_0.award_list)
				var_1_3 = var_1_2.getActivityById(var_1_0.activity_id)

				local var_2_2 = var_1_3.getDataConfig("target")

				for iter_2_2, iter_2_3 in ipairs(var_2_2):
					if iter_2_3 <= var_1_0.arg1:
						if not table.contains(var_1_3.data1_list, iter_2_3):
							table.insert(var_1_3.data1_list, iter_2_3)
					else
						break
			elif var_1_0.cmd == 5:
				local var_2_3 = arg_2_0.number[1]

				var_1_3.data1 = var_1_3.data1 + var_2_3

				local var_2_4 = getProxy(PlayerProxy)
				local var_2_5 = var_2_4.getRawData()

				var_2_5.consume({
					[id2res(var_1_0.arg1)] = var_2_3
				})
				var_2_4.updatePlayer(var_2_5)

			var_1_2.updateActivity(var_1_3)
			arg_1_0.sendNotification(GAME.ACT_NEW_PT_DONE, {
				awards = var_2_0,
				callback = var_1_1
			})
		else
			originalPrint(errorTip("", arg_2_0.result)))

return var_0_0
