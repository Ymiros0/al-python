local var_0_0 = class("FragmentSellCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(BagProxy)
	local var_1_2 = getProxy(PlayerProxy).getRawData()
	local var_1_3 = {}
	local var_1_4 = {}

	for iter_1_0, iter_1_1 in pairs(var_1_0):
		if var_1_1.getItemCountById(iter_1_1.id) < iter_1_1.count:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_x", iter_1_1.getConfig("name")))

			return

		local var_1_5 = iter_1_1.getConfig("price")
		local var_1_6 = (var_1_4[var_1_5[1]] or 0) + var_1_5[2] * iter_1_1.count

		var_1_4[var_1_5[1]] = var_1_6

		table.insert(var_1_3, {
			id = iter_1_1.id,
			count = iter_1_1.count
		})

	pg.ConnectionMgr.GetInstance().Send(15008, {
		item_list = var_1_3
	}, 15009, function(arg_2_0)
		if arg_2_0.result == 0:
			for iter_2_0, iter_2_1 in ipairs(var_1_0):
				reducePlayerOwn(iter_2_1)

			local var_2_0 = {}

			for iter_2_2, iter_2_3 in pairs(var_1_4):
				local var_2_1 = {
					type = DROP_TYPE_RESOURCE,
					id = iter_2_2,
					count = iter_2_3
				}

				addPlayerOwn(var_2_1)
				table.insert(var_2_0, var_2_1)

			arg_1_0.sendNotification(GAME.FRAG_SELL_DONE, {
				awards = var_2_0
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_2_0.result)))

return var_0_0
