local var_0_0 = class("ShipAddInimacyCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	pg.ConnectionMgr.GetInstance().Send(19011, {
		id = var_1_0
	}, 19012, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(BayProxy)
			local var_2_1 = var_2_0.getShipById(var_1_0)
			local var_2_2 = var_2_1.state_info_3

			var_2_1.addLikability(var_2_2)

			var_2_1.state_info_3 = 0

			var_2_0.updateShip(var_2_1)

			if var_2_2 == 0:
				pg.TipsMgr.GetInstance().ShowTips(i18n("backyard_getResource_emptry"))
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("backyard_shipAddInimacy_ok", var_2_1.getName()))

			getProxy(DormProxy).UpdateInimacyAndMoney()
			arg_1_0.sendNotification(GAME.BACKYARD_ADD_INTIMACY_DONE, {
				id = var_1_0
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("backyard_shipAddInimacy", arg_2_0.result)))

return var_0_0
