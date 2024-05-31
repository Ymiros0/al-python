local var_0_0 = class("ShipExitCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(DormProxy)
	local var_1_2 = var_1_0.shipId
	local var_1_3 = getProxy(BayProxy)
	local var_1_4 = var_1_3.getShipById(var_1_2)
	local var_1_5 = var_1_0.callback

	if not var_1_1.getShipById(var_1_2):
		pg.TipsMgr.GetInstance().ShowTips(i18n("backyard_no_ship_tip"))

		return

	pg.ConnectionMgr.GetInstance().Send(19004, {
		ship_id = var_1_2
	}, 19005, function(arg_2_0)
		local var_2_0 = 0

		if arg_2_0.result == 0:
			local var_2_1 = var_1_4.state

			if var_2_1 == Ship.STATE_REST:
				-- block empty
			elif var_2_1 == Ship.STATE_TRAIN:
				var_1_4.state_info_2 = var_1_4.getTotalExp()

			var_1_4.updateStateInfo34(0, 0)
			var_1_1.exitYardById(var_1_2)
			var_1_4.updateState(Ship.STATE_NORMAL)

			var_2_0 = arg_2_0.exp

			var_1_4.addExp(var_2_0)
			var_1_3.updateShip(var_1_4)
			arg_1_0.sendNotification(GAME.EXIT_SHIP_DONE, var_1_4)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("backyard_shipExit", arg_2_0.result))

		if var_1_5 != None:
			var_1_5(var_2_0))

return var_0_0
