local var_0_0 = class("IslandShoppingCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.shop
	local var_1_2 = getProxy(ActivityProxy).getActivityById(var_1_1.activityId)
	local var_1_3 = var_1_1.bindConfigTable()[var_1_0.arg1]
	local var_1_4 = var_1_0.arg2 or 1
	local var_1_5 = getProxy(PlayerProxy)
	local var_1_6 = var_1_5.getData()

	if var_1_6[id2res(var_1_3.resource_type)] < var_1_3.resource_num * var_1_4:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_resource"))

		return

	if var_1_3.commodity_type == DROP_TYPE_RESOURCE:
		if var_1_3.commodity_id == 1 and var_1_6.GoldMax(var_1_3.num * var_1_4):
			pg.TipsMgr.GetInstance().ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_shop"))

			return

		if var_1_3.commodity_id == 2 and var_1_6.OilMax(var_1_3.num * var_1_4):
			pg.TipsMgr.GetInstance().ShowTips(i18n("oil_max_tip_title") .. i18n("resource_max_tip_shop"))

			return
	elif var_1_3.commodity_type == DROP_TYPE_ITEM:
		local var_1_7 = Item.getConfigData(var_1_3.commodity_id).max_num

		if var_1_7 > 0 and var_1_7 < getProxy(BagProxy).getItemCountById(var_1_3.commodity_id) + var_1_3.num * var_1_4:
			pg.TipsMgr.GetInstance().ShowTips(i18n("island_shop_limit_error"))

			return

	pg.ConnectionMgr.GetInstance().Send(11202, {
		cmd = 1,
		activity_id = var_1_2.id,
		arg1 = var_1_0.arg1,
		arg2 = var_1_0.arg2
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			if table.contains(var_1_2.data1_list, var_1_0.arg1):
				for iter_2_0, iter_2_1 in ipairs(var_1_2.data1_list):
					if iter_2_1 == var_1_0.arg1:
						var_1_2.data2_list[iter_2_0] = var_1_2.data2_list[iter_2_0] + var_1_0.arg2

						break
			else
				table.insert(var_1_2.data1_list, var_1_0.arg1)
				table.insert(var_1_2.data2_list, var_1_0.arg2)

			local var_2_0 = var_1_1.bindConfigTable()[var_1_0.arg1]
			local var_2_1 = var_2_0.resource_num * var_1_0.arg2
			local var_2_2 = var_1_5.getData()

			var_2_2.consume({
				[id2res(var_2_0.resource_type)] = var_2_1
			})
			var_1_5.updatePlayer(var_2_2)
			var_1_1.getGoodsById(var_1_0.arg1).addBuyCount(var_1_0.arg2)
			getProxy(ActivityProxy).updateActivity(var_1_2)

			local var_2_3 = PlayerConst.GetTranAwards(var_1_0, arg_2_0)

			arg_1_0.sendNotification(GAME.ISLAND_SHOPPING_DONE, {
				awards = var_2_3,
				goodsId = var_1_0.arg1
			})
		else
			arg_1_0.sendNotification(ActivityProxy.ACTIVITY_OPERATION_ERRO, {
				actId = var_1_2.id,
				code = arg_2_0.result
			}))

return var_0_0
