local var_0_0 = class("SetComanderPrefabFleetCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.commanders
	local var_1_3 = getProxy(CommanderProxy)
	local var_1_4 = {}

	for iter_1_0, iter_1_1 in pairs(var_1_2):
		table.insert(var_1_4, {
			id = iter_1_1.id,
			pos = iter_1_0
		})

	if #var_1_4 == 0 or _.all(var_1_4, function(arg_2_0)
		return arg_2_0.id == 0):
		return

	pg.ConnectionMgr.GetInstance().Send(25022, {
		id = var_1_1,
		commandersid = var_1_4
	}, 25023, function(arg_3_0)
		if arg_3_0.result == 0:
			local var_3_0 = var_1_3.getPrefabFleetById(var_1_1)

			var_3_0.updateCommanders(var_1_2)
			var_1_3.updatePrefabFleet(var_3_0)
			arg_1_0.sendNotification(GAME.SET_COMMANDER_PREFAB_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_3_0.result]))

return var_0_0
