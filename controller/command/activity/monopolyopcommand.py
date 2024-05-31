local var_0_0 = class("MonopolyOPCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(ActivityProxy)
	local var_1_2 = var_1_1.getActivityById(var_1_0.activity_id)

	if not var_1_2 or var_1_2.isEnd():
		return

	pg.ConnectionMgr.GetInstance().Send(11202, {
		activity_id = var_1_0.activity_id,
		cmd = var_1_0.cmd,
		arg1 = var_1_0.arg1,
		arg2 = var_1_0.arg2,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.award_list)
			local var_2_1 = var_1_0.cmd

			if var_2_1 == ActivityConst.MONOPOLY_OP_AWARD:
				var_1_2.data2_list[2] = var_1_2.data2_list[2] + 1

				var_1_1.updateActivity(var_1_2)
				arg_1_0.sendNotification(GAME.MONOPOLY_AWARD_DONE, {
					awards = var_2_0
				})
			else
				if var_2_1 == ActivityConst.MONOPOLY_OP_LAST:
					var_1_2.data2_list[3] = 1

					if #var_2_0 > 0:
						arg_1_0.sendNotification(GAME.MONOPOLY_AWARD_DONE, {
							awards = var_2_0,
							def callback:()
								return
						})

					if var_1_0.callback:
						var_1_0.callback()

				local var_2_2 = {}
				local var_2_3 = ""

				for iter_2_0, iter_2_1 in ipairs(arg_2_0.number):
					if iter_2_0 > 2:
						table.insert(var_2_2, iter_2_1)

						var_2_3 = var_2_3 .. "-" .. iter_2_1

				local var_2_4 = arg_2_0.number[1]
				local var_2_5 = arg_2_0.number[2]
				local var_2_6 = #var_2_2 > 0 and var_2_2[#var_2_2] or var_1_2.data2

				if table.contains(var_2_2, 1):
					var_1_2.data1_list[3] = var_1_2.data1_list[3] + 1

				if var_2_1 == ActivityConst.MONOPOLY_OP_THROW:
					var_1_2.data3 = var_2_4
					var_1_2.data1_list[2] = var_1_2.data1_list[2] + 1

					local var_2_7 = var_1_2.getDataConfig("reward_time")
					local var_2_8 = var_1_2.getDataConfig("effective_times") or 0
					local var_2_9

					if var_2_8 != 0:
						var_2_9 = math.min(var_1_2.data1_list[2], var_2_8)
					else
						var_2_9 = var_1_2.data1_list[2]

					if var_2_7 > 0:
						var_1_2.data2_list[1] = math.floor(var_2_9 / var_2_7)
					else
						var_1_2.data2_list[1] = 0

					var_1_1.updateActivity(var_1_2)

					if var_1_0.callback:
						var_1_0.callback(var_2_4)
				elif var_2_1 == ActivityConst.MONOPOLY_OP_MOVE:
					var_1_2.data3 = var_2_4
					var_1_2.data2 = var_2_6
					var_1_2.data4 = var_2_5

					var_1_1.updateActivity(var_1_2)

					if var_1_0.callback:
						var_1_0.callback(var_2_4, var_2_2, var_2_5)
				elif var_2_1 == ActivityConst.MONOPOLY_OP_TRIGGER:
					local var_2_10 = var_1_0.callback or function(arg_4_0, arg_4_1)
						return

					var_1_2.data3 = var_2_4
					var_1_2.data2 = var_2_6
					var_1_2.data4 = var_2_5 or 0

					var_1_1.updateActivity(var_1_2)

					if #var_2_0 > 0:
						arg_1_0.sendNotification(GAME.MONOPOLY_AWARD_DONE, {
							awards = var_2_0,
							def callback:()
								var_2_10(var_2_2, var_2_5)
						})
					else
						var_2_10(var_2_2, var_2_5)
		else
			if var_1_0.callback:
				var_1_0.callback()

			originalPrint("Monopoly Activity erro code" .. arg_2_0.result .. " cmd." .. var_1_0.cmd))

return var_0_0
