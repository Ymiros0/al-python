local var_0_0 = class("BatchGetCommanderCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().boxIds
	local var_1_1 = {}
	local var_1_2 = {}
	local var_1_3 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_0):
		table.insert(var_1_3, function(arg_2_0)
			if arg_1_0.CheckFullCapacity():
				arg_2_0()

				return

			arg_1_0.sendNotification(GAME.COMMANDER_ON_OPEN_BOX, {
				notify = False,
				id = iter_1_1,
				def callback:(arg_3_0)
					if arg_3_0:
						table.insert(var_1_1, arg_3_0)
						table.insert(var_1_2, iter_1_1)

					arg_2_0()
			}))

	seriesAsync(var_1_3, function()
		arg_1_0.sendNotification(GAME.COMMANDER_ON_BATCH_DONE, {
			boxIds = var_1_2,
			commanders = var_1_1
		}))

def var_0_0.CheckFullCapacity(arg_5_0):
	if getProxy(PlayerProxy).getRawData().commanderBagMax <= getProxy(CommanderProxy).getCommanderCnt():
		return True

	return False

return var_0_0
