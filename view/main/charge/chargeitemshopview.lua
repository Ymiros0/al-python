local var_0_0 = class("ChargeItemShopView", import("...base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "ChargeItemShopUI"
end

function var_0_0.OnInit(arg_2_0)
	arg_2_0:initData()
	arg_2_0:initUI()
	arg_2_0:Show()
end

function var_0_0.OnDestroy(arg_3_0)
	for iter_3_0, iter_3_1 in ipairs(arg_3_0.cardList) do
		iter_3_1:Dispose()
	end
end

function var_0_0.initData(arg_4_0)
	arg_4_0.itemGoodsVOList = {}
	arg_4_0.player = getProxy(PlayerProxy):getData()

	arg_4_0:updateData()
end

function var_0_0.initUI(arg_5_0)
	arg_5_0.contextTF = arg_5_0:findTF("content")
	arg_5_0.lScrollRect = GetComponent(arg_5_0.contextTF, "LScrollRect")
	arg_5_0.cardTable = {}
	arg_5_0.cardList = {}

	arg_5_0:initScrollRect()
	arg_5_0:updateScrollRect()
end

function var_0_0.initScrollRect(arg_6_0)
	arg_6_0.cardTable = {}
	arg_6_0.cardList = {}

	local function var_6_0(arg_7_0)
		local var_7_0 = ChargeGoodsCard.New(arg_7_0)

		table.insert(arg_6_0.cardList, var_7_0)
		onButton(arg_6_0, var_7_0.tr, function()
			if var_7_0.goodsVO:isLevelLimit(arg_6_0.player.level) then
				pg.TipsMgr.GetInstance():ShowTips(i18n("charge_level_limit"))

				return
			end

			local var_8_0 = var_7_0.goodsVO:getConfig("effect_args")
			local var_8_1 = {}
			local var_8_2

			if var_8_0 == "ship_bag_size" then
				if arg_6_0.player:getMaxShipBagExcludeGuild() >= Player.MAX_SHIP_BAG then
					pg.TipsMgr.GetInstance():ShowTips(i18n("charge_ship_bag_max"))

					return
				end

				var_8_1 = {
					count = 1,
					type = DROP_TYPE_ITEM,
					id = Goods.SHIP_BAG_SIZE_ITEM
				}
				var_8_2 = var_8_1.id
			elseif var_8_0 == "equip_bag_size" then
				if arg_6_0.player:getMaxEquipmentBagExcludeGuild() >= Player.MAX_EQUIP_BAG then
					pg.TipsMgr.GetInstance():ShowTips(i18n("charge_equip_bag_max"))

					return
				end

				var_8_1 = {
					count = 1,
					type = DROP_TYPE_ITEM,
					id = Goods.EQUIP_BAG_SIZE_ITEM
				}
				var_8_2 = var_8_1.id
			elseif var_8_0 == "commander_bag_size" then
				if arg_6_0.player.commanderBagMax >= Player.MAX_COMMANDER_BAG then
					pg.TipsMgr.GetInstance():ShowTips(i18n("charge_commander_bag_max"))

					return
				end

				var_8_1 = {
					count = 1,
					type = DROP_TYPE_ITEM,
					id = Goods.COMMANDER_BAG_SIZE_ITEM
				}
				var_8_2 = var_8_1.id
			elseif var_8_0 == "spweapon_bag_size" then
				if getProxy(EquipmentProxy):GetSpWeaponCapacity() >= EquipmentProxy.MAX_SPWEAPON_BAG then
					pg.TipsMgr.GetInstance():ShowTips(i18n("charge_equip_bag_max"))

					return
				end

				var_8_1 = {
					count = 1,
					type = DROP_TYPE_ITEM,
					id = Goods.SPWEAPON_BAG_SIZE_ITEM
				}
				var_8_2 = var_8_1.id
			else
				var_8_1 = {
					id = var_7_0.goodsVO:getConfig("effect_args")[1],
					type = var_7_0.goodsVO:getConfig("type"),
					count = var_7_0.goodsVO:getConfig("num")
				}

				if var_7_0.goodsVO:getConfig("type") == DROP_TYPE_RESOURCE then
					var_8_2 = id2ItemId(var_8_1.id)
				else
					var_8_2 = var_8_1.id
				end
			end

			local var_8_3 = ChargeConst.getGroupLimit(arg_6_0.normalGroupList, var_7_0.goodsVO:getConfig("group"))
			local var_8_4 = var_7_0.goodsVO:IsGroupSale() and i18n("gem_shop_xinzhi_tip", var_8_3) or ""

			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				yesText = "text_buy",
				type = MSGBOX_TYPE_SINGLE_ITEM,
				drop = var_8_1,
				subIntro = var_8_4,
				onYes = function()
					if var_8_2 then
						local var_9_0 = var_7_0.goodsVO:GetPrice()
						local var_9_1 = Item.New({
							id = var_8_2
						}):getConfig("name")

						pg.MsgboxMgr.GetInstance():ShowMsgBox({
							content = i18n("charge_scene_buy_confirm", var_9_0, var_9_1),
							onYes = function()
								arg_6_0:emit(ChargeMediator.BUY_ITEM, var_7_0.goodsVO.id, 1)
							end
						})
					end
				end
			})
		end)

		arg_6_0.cardTable[arg_7_0] = var_7_0
	end

	local function var_6_1(arg_11_0, arg_11_1)
		local var_11_0 = arg_6_0.cardTable[arg_11_1]

		if not var_11_0 then
			var_6_0(arg_11_1)

			var_11_0 = arg_6_0.cardTable[arg_11_1]
		end

		local var_11_1 = arg_6_0.itemGoodsVOList[arg_11_0 + 1]

		var_11_0:update(var_11_1)
		var_11_0:setLevelMask(arg_6_0.player.level)

		local var_11_2 = ChargeConst.getGroupLimit(arg_6_0.normalGroupList, var_11_1:getConfig("group"))

		var_11_0:setGroupMask(var_11_2)
	end

	arg_6_0.lScrollRect.onInitItem = var_6_0
	arg_6_0.lScrollRect.onUpdateItem = var_6_1
end

function var_0_0.updateScrollRect(arg_12_0)
	arg_12_0.lScrollRect:SetTotalCount(#arg_12_0.itemGoodsVOList, arg_12_0.lScrollRect.value)
end

function var_0_0.updateItemGoodsVOList(arg_13_0)
	arg_13_0.itemGoodsVOList = {}

	local var_13_0 = pg.shop_template

	for iter_13_0, iter_13_1 in pairs(var_13_0.all) do
		local var_13_1 = var_13_0[iter_13_1]

		if var_13_1.genre == "gem_shop" then
			local var_13_2, var_13_3, var_13_4 = ChargeConst.getGoodsLimitInfo(iter_13_1)
			local var_13_5 = false
			local var_13_6 = var_13_1.effect_args

			if var_13_6 == "ship_bag_size" and var_13_3 and var_13_4 then
				local var_13_7 = arg_13_0.player:getMaxShipBagExcludeGuild()

				if var_13_3 <= var_13_7 and var_13_7 <= var_13_4 then
					var_13_5 = true
				end
			elseif var_13_6 == "equip_bag_max" and var_13_3 and var_13_4 then
				local var_13_8 = arg_13_0.player:getMaxEquipmentBag()

				if var_13_3 <= var_13_8 and var_13_8 <= var_13_4 then
					var_13_5 = true
				end
			elseif var_13_6 == "commander_bag_size" and var_13_3 and var_13_4 then
				local var_13_9 = arg_13_0.player.commanderBagMax

				if var_13_3 <= var_13_9 and var_13_9 <= var_13_4 then
					var_13_5 = true
				end
			else
				var_13_5 = true
			end

			if var_13_5 == true then
				local var_13_10 = Goods.Create({
					count = 0,
					shop_id = iter_13_1
				}, Goods.TYPE_MILITARY)

				table.insert(arg_13_0.itemGoodsVOList, var_13_10)
			end
		end
	end

	for iter_13_2 = #arg_13_0.itemGoodsVOList, 1, -1 do
		local var_13_11 = arg_13_0.itemGoodsVOList[iter_13_2]
		local var_13_12 = ChargeConst.getGroupLimit(arg_13_0.normalGroupList, var_13_11:getConfig("group"))

		if not var_13_11:IsShowWhenGroupSale(var_13_12) then
			table.remove(arg_13_0.itemGoodsVOList, iter_13_2)
		end
	end
end

function var_0_0.sortItemGoodsVOList(arg_14_0)
	table.sort(arg_14_0.itemGoodsVOList, function(arg_15_0, arg_15_1)
		local var_15_0 = arg_15_0:isLevelLimit(arg_14_0.player.level) and 1 or 0
		local var_15_1 = arg_15_1:isLevelLimit(arg_14_0.player.level) and 1 or 0
		local var_15_2 = arg_15_0:getConfig("order")
		local var_15_3 = arg_15_1:getConfig("order")

		if var_15_2 == var_15_3 then
			if var_15_0 == var_15_1 then
				return arg_15_0.id > arg_15_1.id
			end

			return var_15_0 < var_15_1
		else
			return var_15_2 < var_15_3
		end
	end)
end

function var_0_0.updateGoodsData(arg_16_0)
	arg_16_0.firstChargeIds = arg_16_0.contextData.firstChargeIds
	arg_16_0.chargedList = arg_16_0.contextData.chargedList
	arg_16_0.normalList = arg_16_0.contextData.normalList
	arg_16_0.normalGroupList = arg_16_0.contextData.normalGroupList
end

function var_0_0.setGoodData(arg_17_0, arg_17_1, arg_17_2, arg_17_3, arg_17_4)
	arg_17_0.firstChargeIds = arg_17_1
	arg_17_0.chargedList = arg_17_2
	arg_17_0.normalList = arg_17_3
	arg_17_0.normalGroupList = arg_17_4
end

function var_0_0.updateData(arg_18_0)
	arg_18_0.player = getProxy(PlayerProxy):getData()

	arg_18_0:updateItemGoodsVOList()
	arg_18_0:sortItemGoodsVOList()
end

function var_0_0.reUpdateAll(arg_19_0)
	arg_19_0:updateData()
	arg_19_0:updateScrollRect()
end

return var_0_0
