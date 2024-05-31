local var_0_0 = class("UpdateFleetCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.fleet
	local var_1_2 = var_1_0.callback

	assert(isa(var_1_1, Fleet), "should be an instance of Fleet")

	local var_1_3 = getProxy(PlayerProxy)
	local var_1_4 = getProxy(FleetProxy)
	local var_1_5 = var_1_4.getFleetById(var_1_1.id)

	if var_1_5 == None:
		return

	local var_1_6 = {}

	_.each(var_1_1.vanguardShips, function(arg_2_0)
		var_1_6[#var_1_6 + 1] = arg_2_0)
	_.each(var_1_1.mainShips, function(arg_3_0)
		var_1_6[#var_1_6 + 1] = arg_3_0)
	_.each(var_1_1.subShips, function(arg_4_0)
		var_1_6[#var_1_6 + 1] = arg_4_0)
	pg.ConnectionMgr.GetInstance().Send(12102, {
		id = var_1_1.id,
		ship_list = var_1_6
	}, 12103, function(arg_5_0)
		if arg_5_0.result == 0:
			var_1_1.name = var_1_5.name

			var_1_4.updateFleet(var_1_1)

			if var_1_1.isEmpty() and var_1_3.combatFleetId == var_1_1.id:
				var_1_3.combatFleetId = 1

			arg_1_0.sendNotification(GAME.UPDATE_FLEET_DONE, var_1_1.id)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("fleet_updateFleet", arg_5_0.result))

		if var_1_2 != None:
			var_1_2())

return var_0_0
