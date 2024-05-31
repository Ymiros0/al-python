local var_0_0 = class("ProposeExchangeRingCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(BagProxy)
	local var_1_2 = pg.gameset.vow_prop_conversion.description

	if var_1_1.getItemCountById(var_1_2[1]) < 1:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_item_1"))

		return

	pg.ConnectionMgr.GetInstance().Send(15010, {
		id = 0
	}, 15011, function(arg_2_0)
		if arg_2_0.result == 0:
			var_1_1.removeItemById(var_1_2[1], 1)
			var_1_1.addItemById(var_1_2[2], 1)
			arg_1_0.sendNotification(GAME.PROPOSE_EXCHANGE_RING_DONE, {
				items = {
					Drop.New({
						count = 1,
						type = DROP_TYPE_ITEM,
						id = var_1_2[2]
					})
				}
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_2_0.result)))

return var_0_0
