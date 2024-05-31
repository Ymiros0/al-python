local var_0_0 = class("ShipAddMoneyCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	pg.ConnectionMgr.GetInstance().Send(19013, {
		id = var_1_0
	}, 19014, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(BayProxy)
			local var_2_1 = var_2_0.getShipById(var_1_0)
			local var_2_2 = var_2_1.state_info_4

			var_2_1.state_info_4 = 0

			var_2_0.updateShip(var_2_1)

			local var_2_3 = getProxy(PlayerProxy)
			local var_2_4 = var_2_3.getData()

			var_2_4.addResources({
				dormMoney = var_2_2
			})
			var_2_3.updatePlayer(var_2_4)

			if var_2_2 == 0:
				pg.TipsMgr.GetInstance().ShowTips(i18n("backyard_getResource_emptry"))
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("backyard_shipAddMoney_ok", var_2_1.getName(), var_2_2))

			getProxy(DormProxy).UpdateInimacyAndMoney()
			arg_1_0.sendNotification(GAME.BACKYARD_ADD_MONEY_DONE, {
				id = var_1_0
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("backyard_shipAddMoney", arg_2_0.result)))

return var_0_0
