local var_0_0 = class("ShoppingCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.count
	local var_1_3 = pg.shop_template[var_1_1]

	if not var_1_1:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_shopId_noFound"))

		return

	if var_1_2 == 0:
		return

	local var_1_4 = getProxy(ShopsProxy)
	local var_1_5 = var_1_4.getShopStreet()
	local var_1_6 = False
	local var_1_7 = var_1_3.resource_num * var_1_2
	local var_1_8 = getProxy(PlayerProxy)
	local var_1_9 = var_1_8.getData()

	if var_1_3.limit_args:
		for iter_1_0, iter_1_1 in ipairs(var_1_3.limit_args):
			if type(iter_1_1) == "table" and iter_1_1[1] == "level" and iter_1_1[2] > var_1_9.level:
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_limit_level", iter_1_1[2]))

				return

	if var_1_3.discount != 0 and CommonCommodity.InCommodityDiscountTime(var_1_3.id):
		var_1_7 = var_1_7 * ((100 - var_1_3.discount) / 100)

	if var_1_7 > var_1_9[id2res(var_1_3.resource_type)]:
		local var_1_10 = Drop.New({
			type = DROP_TYPE_RESOURCE,
			id = var_1_3.resource_type
		}).getName()

		if var_1_3.resource_type == 1:
			GoShoppingMsgBox(i18n("switch_to_shop_tip_2", i18n("word_gold")), ChargeScene.TYPE_ITEM, {
				{
					59001,
					var_1_7 - var_1_9[id2res(var_1_3.resource_type)],
					var_1_7
				}
			})
		elif var_1_3.resource_type == 4 or var_1_3.resource_type == 14:
			GoShoppingMsgBox(i18n("switch_to_shop_tip_3", i18n("word_gem")), ChargeScene.TYPE_DIAMOND)
		elif not ItemTipPanel.ShowItemTip(DROP_TYPE_RESOURCE, var_1_3.resource_type):
			pg.TipsMgr.GetInstance().ShowTips(i18n("buyProp_noResource_error", var_1_10))

		return

	local var_1_11 = {}

	seriesAsync(var_1_11, function()
		pg.ConnectionMgr.GetInstance().Send(16001, {
			id = var_1_1,
			number = var_1_2
		}, 16002, function(arg_3_0)
			if arg_3_0.result == 0:
				local var_3_0 = {}
				local var_3_1 = var_1_8.getData()

				var_3_1.consume({
					[id2res(var_1_3.resource_type)] = var_1_7
				})

				local var_3_2

				switch(var_1_3.genre, {
					[ShopArgs.SkinShop] = function()
						var_3_0 = PlayerConst.addTranDrop(arg_3_0.drop_list)

						local var_4_0 = var_1_3.effect_args[1]
						local var_4_1 = getProxy(ShipSkinProxy)
						local var_4_2 = ShipSkin.New({
							id = var_4_0
						})

						var_4_1.addSkin(var_4_2),
					[ShopArgs.SkinShopTimeLimit] = function()
						local var_5_0 = var_1_3.effect_args[1]
						local var_5_1 = getProxy(ShipSkinProxy)
						local var_5_2 = var_5_1.getSkinById(var_5_0)

						if var_5_2 and var_5_2.isExpireType():
							local var_5_3 = var_1_3.time_second * var_1_2 + var_5_2.endTime
							local var_5_4 = ShipSkin.New({
								id = var_5_0,_time = var_5_3
							})

							var_5_1.addSkin(var_5_4)
						elif not var_5_2:
							local var_5_5 = var_1_3.time_second * var_1_2 + pg.TimeMgr.GetInstance().GetServerTime()
							local var_5_6 = ShipSkin.New({
								id = var_5_0,_time = var_5_5
							})

							var_5_1.addSkin(var_5_6)
				})
				var_1_8.updatePlayer(var_3_1)

				if var_1_3.group > 0:
					var_1_4.updateNormalGroupList(var_1_3.group, var_1_3.group_buy_count)

				arg_1_0.sendNotification(GAME.SKIN_SHOPPIGN_DONE, {
					id = var_1_1,
					shopType = var_3_2,
					normalList = var_1_4.GetNormalList(),
					normalGroupList = var_1_4.GetNormalGroupList(),
					awards = var_3_0
				})
			else
				originalPrint(arg_3_0.result)

				if arg_3_0.result == 4400:
					pg.TipsMgr.GetInstance().ShowTips(i18n("shopping_error_time_limit"))
				else
					pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_3_0.result))))

return var_0_0
