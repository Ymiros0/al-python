local var_0_0 = class("Challenge2InitialRequestCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().mode
	local var_1_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_CHALLENGE)
	local var_1_2 = getProxy(FleetProxy).getActivityFleets()[var_1_1.id]
	local var_1_3 = {
		[var_1_0 + 1] = var_1_2[var_1_0 + 1],
		[var_1_0 + 11] = var_1_2[var_1_0 + 11]
	}
	local var_1_4 = {}

	for iter_1_0, iter_1_1 in pairs(var_1_3):
		if iter_1_1:
			local var_1_5 = {}

			_.each(iter_1_1.vanguardShips, function(arg_2_0)
				var_1_5[#var_1_5 + 1] = arg_2_0)
			_.each(iter_1_1.mainShips, function(arg_3_0)
				var_1_5[#var_1_5 + 1] = arg_3_0)
			_.each(iter_1_1.subShips, function(arg_4_0)
				var_1_5[#var_1_5 + 1] = arg_4_0)

			local var_1_6 = {}

			for iter_1_2, iter_1_3 in pairs(iter_1_1.commanderIds):
				table.insert(var_1_6, {
					pos = iter_1_2,
					id = iter_1_3
				})

			local var_1_7 = {
				id = iter_1_0,
				ship_list = var_1_5,
				commanders = var_1_6
			}

			table.insert(var_1_4, var_1_7)

	if not var_1_1 or var_1_1.isEnd():
		return

	pg.ConnectionMgr.GetInstance().Send(24002, {
		activity_id = var_1_1.id,
		group_list = var_1_4,
		mode = var_1_0
	}, 24003, function(arg_5_0)
		if arg_5_0.result == 0:
			local function var_5_0()
				arg_1_0.sendNotification(GAME.CHALLENGE2_INITIAL_DONE, {
					mode = var_1_0
				})

			arg_1_0.sendNotification(GAME.CHALLENGE2_INFO, {
				callback = var_5_0
			}))

return var_0_0
