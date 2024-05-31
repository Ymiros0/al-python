local var_0_0 = class("CommanderCatteryOPCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().op
	local var_1_1 = getProxy(CommanderProxy).GetCommanderHome()

	pg.ConnectionMgr.GetInstance().Send(25028, {
		type = var_1_0
	}, 25029, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.awards)
			local var_2_1 = 0
			local var_2_2 = 0
			local var_2_3 = {}

			if var_1_0 == 1:
				var_1_1.IncCleanValue()
			elif var_1_0 == 2:
				var_2_3 = arg_1_0.AddCommanderExpByFeed()
			elif var_1_0 == 3:
				-- block empty

			local var_2_4 = var_1_1.GetCatteries()
			local var_2_5 = {}

			for iter_2_0, iter_2_1 in pairs(var_2_4):
				if iter_2_1.ExistOP(var_1_0) and iter_2_1.CommanderCanOP(var_1_0):
					local var_2_6 = iter_2_1.GetCommander()

					iter_2_1.ClearOP(var_1_0)
					var_2_6.UpdateHomeOpTime(var_1_0, arg_2_0.op_time)
					getProxy(CommanderProxy).updateCommander(var_2_6)
					table.insert(var_2_5, iter_2_1.id)

			local var_2_7 = Clone(var_1_1)

			var_1_1.UpdateExpAndLevel(arg_2_0.level, arg_2_0.exp)

			if var_1_1.level > var_2_7.level:
				var_2_2 = var_2_7.GetNextLevelExp() - var_2_7.exp + var_1_1.exp
			else
				var_2_2 = var_1_1.exp - var_2_7.exp

			arg_1_0.sendNotification(GAME.COMMANDER_CATTERY_OP_DONE, {
				awards = var_2_0,
				cmd = var_1_0,
				opCatteries = var_2_5,
				commanderExps = var_2_3,
				homeExp = var_2_2
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

def var_0_0.AddCommanderExpByFeed(arg_3_0):
	local var_3_0 = {}

	local function var_3_1(arg_4_0, arg_4_1)
		local var_4_0 = arg_4_0.GetCommanderId()
		local var_4_1 = getProxy(CommanderProxy)
		local var_4_2 = var_4_1.getCommanderById(var_4_0)
		local var_4_3 = var_4_2.isMaxLevel()

		if var_4_3:
			arg_4_1 = 0

		var_4_2.addExp(arg_4_1)

		if not var_4_3 and var_4_2.isMaxLevel():
			arg_4_1 = arg_4_1 - var_4_2.exp

		table.insert(var_3_0, {
			id = arg_4_0.id,
			value = arg_4_1
		})
		var_4_1.updateCommander(var_4_2)

	local var_3_2 = getProxy(CommanderProxy).GetCommanderHome()
	local var_3_3 = var_3_2.GetCatteries()
	local var_3_4 = var_3_2.getConfig("feed_level")[2]

	for iter_3_0, iter_3_1 in pairs(var_3_3):
		if iter_3_1.ExistCommander() and iter_3_1.ExiseFeedOP():
			var_3_1(iter_3_1, var_3_4)

	return var_3_0

return var_0_0
