local var_0_0 = class("GetChargeListCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	pg.ConnectionMgr.GetInstance().Send(16104, {
		type = 0
	}, 16105, function(arg_2_0)
		local var_2_0 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.pay_list):
			local var_2_1 = Goods.Create(iter_2_1, Goods.TYPE_CHARGE)

			var_2_0[var_2_1.id] = var_2_1

		local var_2_2 = {}

		for iter_2_2, iter_2_3 in ipairs(arg_2_0.first_pay_list):
			table.insert(var_2_2, iter_2_3)

		local var_2_3 = {}

		for iter_2_4, iter_2_5 in ipairs(arg_2_0.normal_list):
			local var_2_4 = Goods.Create(iter_2_5, Goods.TYPE_GIFT_PACKAGE)

			var_2_3[var_2_4.id] = var_2_4

			table.insert(var_2_3, iter_2_5)

		local var_2_5 = {}

		for iter_2_6, iter_2_7 in ipairs(arg_2_0.normal_group_list):
			table.insert(var_2_5, iter_2_7)

		local var_2_6 = getProxy(ShopsProxy)

		var_2_6.setChargedList(var_2_0)
		var_2_6.setFirstChargeList(var_2_2)
		var_2_6.setNormalList(var_2_3)
		var_2_6.setNormalGroupList(var_2_5)

		var_2_6.refreshChargeList = False

		arg_1_0.sendNotification(GAME.GET_CHARGE_LIST_DONE, {
			chargedList = var_2_0,
			firstChargeIds = var_2_2,
			normalList = var_2_3,
			normalGroupList = var_2_5
		})

		if var_1_0 and var_1_0.callback:
			var_1_0.callback())

return var_0_0
