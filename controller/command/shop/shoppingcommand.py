local var_0_0 = class("ShoppingCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.count
	local var_1_3 = pg.shop_template[var_1_1]

	if not var_1_1:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_shopId_noFound"))

		return

	if var_1_3.type == DROP_TYPE_WORLD_ITEM and not nowWorld().IsActivate():
		pg.TipsMgr.GetInstance().ShowTips(i18n("world_shop_bag_unactivated"))

		return

	local var_1_4 = getProxy(PlayerProxy)
	local var_1_5 = var_1_4.getData()

	if var_1_3.type == DROP_TYPE_ITEM:
		local var_1_6 = var_1_3.effect_args
		local var_1_7 = Item.getConfigData(var_1_6[1]).display_icon

		for iter_1_0, iter_1_1 in pairs(var_1_7):
			if iter_1_1[1] == 1:
				if iter_1_1[2] == 1 and var_1_5.GoldMax(iter_1_1[3]):
					pg.TipsMgr.GetInstance().ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_shop"))

					return

				if iter_1_1[2] == 2 and var_1_5.OilMax(iter_1_1[3]):
					pg.TipsMgr.GetInstance().ShowTips(i18n("oil_max_tip_title") .. i18n("resource_max_tip_shop"))

					return

	if var_1_3.type == DROP_TYPE_RESOURCE:
		if var_1_3.effect_args[1] == 1 and var_1_5.GoldMax(var_1_3.num * var_1_2):
			pg.TipsMgr.GetInstance().ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_shop"))

			return

		if var_1_3.effect_args[1] == 2:
			local var_1_8 = var_1_3.num

			if var_1_8 == -1 and var_1_3.genre == ShopArgs.BuyOil:
				var_1_8 = ShopArgs.getOilByLevel(var_1_5.level)

			if var_1_5.OilMax(var_1_8 * var_1_2):
				pg.TipsMgr.GetInstance().ShowTips(i18n("oil_max_tip_title") .. i18n("resource_max_tip_shop"))

				return

	if var_1_2 == 0:
		return

	local var_1_9 = getProxy(ShopsProxy)
	local var_1_10 = var_1_9.getShopStreet()
	local var_1_11 = False
	local var_1_12 = var_1_3.resource_num
	local var_1_13 = getProxy(NavalAcademyProxy)

	if var_1_12 == -1:
		if var_1_3.effect_args == ShopArgs.EffectShopStreetLevel:
			var_1_12 = pg.navalacademy_shoppingstreet_template[var_1_10.level].lv_up_cost[2] * var_1_2
		else
			local var_1_14 = switch(var_1_3.effect_args, {
				[ShopArgs.EffectTradingPortLevel] = function()
					return var_1_13._goldVO,
				[ShopArgs.EffectOilFieldLevel] = function()
					return var_1_13._oilVO,
				[ShopArgs.EffectClassLevel] = function()
					return var_1_13._classVO
			})

			if var_1_14:
				var_1_12 = var_1_14.bindConfigTable()[var_1_14.GetLevel()].use[2] * var_1_2
	else
		var_1_12 = var_1_3.resource_num * var_1_2

		if var_1_10 and var_1_3.genre == ShopArgs.ShoppingStreetLimit:
			var_1_11 = True

			local var_1_15 = var_1_10.getGoodsById(var_1_1)

			var_1_12 = math.ceil(var_1_15.discount / 100 * var_1_12)

	if var_1_3.limit_args:
		for iter_1_2, iter_1_3 in ipairs(var_1_3.limit_args):
			if type(iter_1_3) == "table" and iter_1_3[1] == "level" and iter_1_3[2] > var_1_5.level:
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_limit_level", iter_1_3[2]))

				return

	if var_1_3.discount != 0 and CommonCommodity.InCommodityDiscountTime(var_1_3.id):
		var_1_12 = var_1_12 * ((100 - var_1_3.discount) / 100)

	if var_1_12 > var_1_5[id2res(var_1_3.resource_type)]:
		local var_1_16 = Drop.New({
			type = DROP_TYPE_RESOURCE,
			id = var_1_3.resource_type
		}).getName()

		if var_1_3.resource_type == 1:
			GoShoppingMsgBox(i18n("switch_to_shop_tip_2", i18n("word_gold")), ChargeScene.TYPE_ITEM, {
				{
					59001,
					var_1_12 - var_1_5[id2res(var_1_3.resource_type)],
					var_1_12
				}
			})
		elif var_1_3.resource_type == 4 or var_1_3.resource_type == 14:
			GoShoppingMsgBox(i18n("switch_to_shop_tip_3", i18n("word_gem")), ChargeScene.TYPE_DIAMOND)
		elif not ItemTipPanel.ShowItemTip(DROP_TYPE_RESOURCE, var_1_3.resource_type):
			pg.TipsMgr.GetInstance().ShowTips(i18n("buyProp_noResource_error", var_1_16))

		return

	local var_1_17 = {}

	table.insert(var_1_17, function(arg_5_0)
		if var_1_3.genre == ShopArgs.GiftPackage or var_1_3.genre == ShopArgs.NewServerShop:
			local var_5_0 = Drop.New({
				count = 1,
				type = DROP_TYPE_ITEM,
				id = var_1_3.effect_args[1]
			})
			local var_5_1 = GetItemsOverflowDic({
				var_5_0
			})
			local var_5_2, var_5_3 = CheckOverflow(var_5_1)

			if not var_5_2:
				switch(var_5_3, {
					def gold:()
						pg.TipsMgr.GetInstance().ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_shop")),
					def oil:()
						pg.TipsMgr.GetInstance().ShowTips(i18n("oil_max_tip_title") .. i18n("resource_max_tip_shop")),
					def equip:()
						NoPosMsgBox(i18n("switch_to_shop_tip_noPos"), openDestroyEquip, gotoChargeScene),
					def ship:()
						NoPosMsgBox(i18n("switch_to_shop_tip_noDockyard"), openDockyardClear, gotoChargeScene, openDockyardIntensify)
				})

				return

			if not CheckShipExpOverflow(var_5_1):
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("player_expResource_mail_fullBag"),
					onYes = arg_5_0
				})

				return

		arg_5_0())
	seriesAsync(var_1_17, function()
		pg.ConnectionMgr.GetInstance().Send(16001, {
			id = var_1_1,
			number = var_1_2
		}, 16002, function(arg_11_0)
			if arg_11_0.result == 0:
				local var_11_0 = {}

				if var_1_3.type == 0:
					arg_1_0.sendNotification(GAME.EXTEND, {
						id = var_1_1,
						count = var_1_2
					})
				else
					var_11_0 = PlayerConst.addTranDrop(arg_11_0.drop_list)

					pg.TipsMgr.GetInstance().ShowTips(i18n("common_buy_success"))

				local var_11_1 = var_1_4.getData()

				var_11_1.consume({
					[id2res(var_1_3.resource_type)] = var_1_12
				})

				local var_11_2

				if var_1_11:
					local var_11_3 = var_1_9.getShopStreet()
					local var_11_4 = var_11_3.getGoodsById(var_1_1)

					var_11_2 = var_11_3.type

					var_11_4.reduceBuyCount()
					var_1_9.UpdateShopStreet(var_11_3)
				else
					switch(var_1_3.genre, {
						[ShopArgs.BuyOil] = function()
							var_11_1.increaseBuyOilCount(),
						[ShopArgs.ArenaShopLimit] = function()
							local var_13_0 = getProxy(ShopsProxy)
							local var_13_1 = var_13_0.getMeritorousShop()
							local var_13_2 = var_13_1.getGoodsById(var_1_1)

							var_13_2.increaseBuyCount()
							var_13_1.updateGoods(var_13_2)

							var_11_2 = var_13_1.type

							var_13_0.updateMeritorousShop(var_13_1),
						[ShopArgs.GiftPackage] = function()
							var_1_9.GetNormalByID(var_1_1).increaseBuyCount(),
						[ShopArgs.NewServerShop] = function()
							var_1_9.GetNormalByID(var_1_1).increaseBuyCount(),
						[ShopArgs.SkinShop] = function()
							assert(False, "must be used ShoppingCommand"),
						[ShopArgs.SkinShopTimeLimit] = function()
							assert(False, "must be used ShoppingCommand"),
						[ShopArgs.guildShop] = function()
							local var_18_0 = getProxy(ShopsProxy).getGuildShop()

							var_18_0.getGoodsById(var_1_1).reduceBuyCount()
							var_1_9.updateGuildShop(var_18_0),
						[ShopArgs.WorldShop] = function()
							nowWorld().UpdateWorldShopGoods({
								{
									goods_id = var_1_1,
									count = var_1_2
								}
							}),
						[ShopArgs.WorldCollection] = function()
							nowWorld().UpdateWorldShopGoods({
								{
									goods_id = var_1_1,
									count = var_1_2
								}
							})
					})

				var_1_4.updatePlayer(var_11_1)

				if var_1_3.group > 0:
					var_1_9.updateNormalGroupList(var_1_3.group, var_1_3.group_buy_count)

				switch(var_1_3.effect_args, {
					[ShopArgs.EffecetShipBagSize] = function()
						pg.TipsMgr.GetInstance().ShowTips(i18n("shop_extendship_success")),
					[ShopArgs.EffecetEquipBagSize] = function()
						pg.TipsMgr.GetInstance().ShowTips(i18n("shop_extendequip_success")),
					[ShopArgs.EffectCommanderBagSize] = function()
						pg.TipsMgr.GetInstance().ShowTips(i18n("shop_extendcommander_success")),
					[ShopArgs.EffectSpWeaponBagSize] = function()
						pg.TipsMgr.GetInstance().ShowTips(i18n("shop_spweapon_success"))
				})

				if not var_1_0.isQuickShopping:
					arg_1_0.sendNotification(GAME.SHOPPING_DONE, {
						id = var_1_1,
						shopType = var_11_2,
						normalList = var_1_9.GetNormalList(),
						normalGroupList = var_1_9.GetNormalGroupList(),
						awards = var_11_0
					})
			else
				originalPrint(arg_11_0.result)

				if arg_11_0.result == 4400:
					pg.TipsMgr.GetInstance().ShowTips(i18n("shopping_error_time_limit"))
				else
					pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_11_0.result))))

return var_0_0
