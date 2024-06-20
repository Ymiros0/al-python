local var_0_0 = class("GetExchangeItemsCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().type

	pg.ConnectionMgr.GetInstance().Send(16106, {
		type = 0
	}, 16107, function(arg_2_0)
		local var_2_0 = getProxy(BuildShipProxy)
		local var_2_1 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.item_shop_id_list):
			table.insert(var_2_1, {
				isFetched = False,
				id = iter_2_1
			})

		for iter_2_2, iter_2_3 in ipairs(arg_2_0.item_fetch_list):
			for iter_2_4, iter_2_5 in pairs(var_2_1):
				if iter_2_5.id == iter_2_3:
					var_2_1[iter_2_4].isFetched = True

		var_2_0.updateExchangeItemList(arg_2_0.item_flash_time, var_2_1)

		if var_1_0 and var_1_0 == 1:
			var_2_0.addExChangeItemTimer()

		arg_1_0.sendNotification(GAME.GET_EXCHANGE_ITEMS_DONE))

return var_0_0