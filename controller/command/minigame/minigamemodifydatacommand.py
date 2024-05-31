local var_0_0 = class("MiniGameModifyDataCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.map
	local var_1_3 = getProxy(MiniGameProxy).GetMiniGameData(var_1_1)

	for iter_1_0, iter_1_1 in pairs(var_1_2):
		var_1_3.SetRuntimeData(iter_1_0, iter_1_1)

	arg_1_0.sendNotification(GAME.MODIFY_MINI_GAME_DATA_DONE, {
		id = var_1_1,
		map = var_1_2
	})

return var_0_0
