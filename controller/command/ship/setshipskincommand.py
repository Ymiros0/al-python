local var_0_0 = class("SetShipSkinCommand", pm.SimpleCommand)

var_0_0.SKIN_UPDATED = "skin updated"

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.shipId
	local var_1_2 = var_1_0.skinId
	local var_1_3 = var_1_0.hideTip

	pg.ConnectionMgr.GetInstance().Send(12202, {
		ship_id = var_1_1,
		skin_id = var_1_2
	}, 12203, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(BayProxy)
			local var_2_1 = var_2_0.getShipById(var_1_1)

			var_2_1.skinId = var_1_2 or 0

			if var_2_1.skinId == 0:
				var_2_1.skinId = var_2_1.getConfig("skin_id")

			if not var_2_1.skinId or var_2_1.skinId == 0:
				var_2_1.skinId = var_2_1.getConfig("skin_id")

			var_2_0.updateShip(var_2_1)

			local var_2_2 = getProxy(PlayerProxy)
			local var_2_3 = var_2_2.getData()

			if var_2_3.character == var_1_1:
				var_2_3.skinId = var_2_1.skinId

				var_2_2.updatePlayer(var_2_3)

			arg_1_0.sendNotification(var_0_0.SKIN_UPDATED, {
				ship = var_2_1
			})

			if not var_1_3:
				pg.TipsMgr.GetInstance().ShowTips(i18n("ship_set_skin_success"))
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("ship_set_skin_error", arg_2_0.result)))

return var_0_0
