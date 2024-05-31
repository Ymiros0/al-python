local var_0_0 = class("ComposeItemCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.count
	local var_1_3 = getProxy(BagProxy)
	local var_1_4 = var_1_3.getItemById(var_1_1)

	if var_1_2 == 0:
		return

	local var_1_5 = var_1_4.getConfig("target_id")
	local var_1_6 = var_1_4.getConfig("compose_number")

	if var_1_2 > var_1_4.count / var_1_6:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_item_1"))

		return

	pg.ConnectionMgr.GetInstance().Send(15006, {
		id = var_1_1,
		num = var_1_2
	}, 15007, function(arg_2_0)
		if arg_2_0.result == 0:
			var_1_3.removeItemById(var_1_1, var_1_2 * var_1_6)

			local var_2_0 = Drop.New({
				type = DROP_TYPE_ITEM,
				id = var_1_5,
				count = var_1_2
			})

			arg_1_0.sendNotification(GAME.ADD_ITEM, var_2_0)
			arg_1_0.sendNotification(GAME.USE_ITEM_DONE, {
				var_2_0
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_2_0.result)))

return var_0_0
