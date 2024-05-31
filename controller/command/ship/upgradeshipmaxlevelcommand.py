local var_0_0 = class("", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().shipId

	if not var_1_0:
		return

	local var_1_1 = getProxy(BayProxy)
	local var_1_2 = var_1_1.getShipById(var_1_0)

	if not var_1_2:
		return

	local var_1_3, var_1_4 = var_1_2.canUpgradeMaxLevel()

	if not var_1_3:
		pg.TipsMgr.GetInstance().ShowTips(var_1_4)

		return

	pg.ConnectionMgr.GetInstance().Send(12038, {
		ship_id = var_1_0
	}, 12039, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = Clone(var_1_2)
			local var_2_1 = var_1_2.getNextMaxLevelConsume()
			local var_2_2 = var_1_2.getNextMaxLevel()

			var_1_2.updateMaxLevel(var_2_2)
			_.each(var_2_1, function(arg_3_0)
				arg_1_0.sendNotification(GAME.CONSUME_ITEM, arg_3_0))
			var_1_2.addExp(0, True)
			arg_1_0.sendNotification(GAME.UPGRADE_MAX_LEVEL_DONE, {
				oldShip = var_2_0,
				newShip = var_1_2,
				def callback:()
					var_1_1.updateShip(var_1_2)
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("ship_buildShip_error", arg_2_0.result)))

return var_0_0
