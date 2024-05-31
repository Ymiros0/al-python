local var_0_0 = class("AddShipCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.type
	local var_1_3 = var_1_0.callBack
	local var_1_4 = getProxy(DormProxy)
	local var_1_5 = getProxy(BayProxy).getShipById(var_1_1)
	local var_1_6 = var_1_4.getData()

	if table.contains(var_1_6.shipIds, var_1_1):
		if var_1_3:
			var_1_3()

		return

	pg.ConnectionMgr.GetInstance().Send(19002, {
		ship_id = var_1_1,
		type = var_1_2
	}, 19003, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(BayProxy)

			if var_1_2 == 1:
				var_1_5.state_info_1 = pg.TimeMgr.GetInstance().GetServerTime()
				var_1_5.state_info_2 = var_1_5.getTotalExp()

				var_1_5.updateState(Ship.STATE_TRAIN)

				if var_1_6.next_timestamp == 0:
					var_1_6.restNextTime()
					var_1_4.updateDrom(var_1_6, BackYardConst.DORM_UPDATE_TYPE_SHIP)
			elif var_1_2 == 2:
				var_1_5.updateState(Ship.STATE_REST)

			var_2_0.updateShip(var_1_5)
			var_1_4.addShip(var_1_5.id)
			arg_1_0.sendNotification(GAME.ADD_SHIP_DONE, {
				id = var_1_1,
				type = var_1_2
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("backyard_addShip", arg_2_0.result))

		if var_1_3:
			var_1_3())

return var_0_0
