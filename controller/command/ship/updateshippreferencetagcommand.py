local var_0_0 = class("UpdateShipPreferenceTagCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.shipId
	local var_1_2 = var_1_0.tag

	pg.ConnectionMgr.GetInstance().Send(12040, {
		ship_id = var_1_1,
		flag = var_1_2
	}, 12041, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(BayProxy)
			local var_2_1

			if var_1_2 == Ship.PREFERENCE_TAG_COMMON:
				var_2_1 = "ship_preference_common"
			elif var_1_2 == Ship.PREFERENCE_TAG_NONE:
				var_2_1 = "ship_preference_non"

			local var_2_2 = var_2_0.getShipById(var_1_1)

			var_2_2.SetPreferenceTag(var_1_2)
			var_2_0.updateShip(var_2_2)
			arg_1_0.sendNotification(GAME.UPDATE_PREFERENCE_DONE, var_2_2)
			pg.TipsMgr.GetInstance().ShowTips(i18n(var_2_1, var_2_2.getName()))
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("ship_updateShipLock", arg_2_0.result)))

return var_0_0
