local var_0_0 = class("ChargeDiamondShopView", import("...base.BaseSubView"))

var_0_0.MonthCardID = 1

function var_0_0.getUIName(arg_1_0)
	return "ChargeDiamondShopUI"
end

function var_0_0.OnInit(arg_2_0)
	arg_2_0:initData()
	arg_2_0:initUI()
	arg_2_0:Show()
end

function var_0_0.OnDestroy(arg_3_0)
	return
end

function var_0_0.initData(arg_4_0)
	arg_4_0.isNeedHideMonthCard = (PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US) and pg.SdkMgr.GetInstance():CheckAudit()
	arg_4_0.diamondGoodsVOList = {}
	arg_4_0.diamondGoodsVOListForShow = {}
	arg_4_0.player = getProxy(PlayerProxy):getData()

	arg_4_0:updateData()
end

function var_0_0.initUI(arg_5_0)
	arg_5_0.itemTpl = arg_5_0:findTF("ItemTpl")

	local var_5_0 = arg_5_0:findTF("content")

	arg_5_0.monthCardTF = arg_5_0:findTF("ItemMonth", var_5_0)
	arg_5_0.itemContainerTF = arg_5_0:findTF("ItemList", var_5_0)
	arg_5_0.uiItemList = arg_5_0:initUIItemList()

	arg_5_0:updateView()
end

function var_0_0.initUIItemList(arg_6_0)
	local var_6_0 = UIItemList.New(arg_6_0.itemContainerTF, arg_6_0.itemTpl)

	var_6_0:make(function(arg_7_0, arg_7_1, arg_7_2)
		if arg_7_0 == UIItemList.EventUpdate then
			arg_7_1 = arg_7_1 + 1

			local var_7_0 = ChargeDiamondCard.New(go(arg_7_2), arg_6_0.monthCardTF, arg_6_0)
			local var_7_1 = arg_6_0.diamondGoodsVOListForShow[arg_7_1]

			var_7_0:update(var_7_1, arg_6_0.player, arg_6_0.firstChargeIds)
			onButton(arg_6_0, var_7_0.tr, function()
				arg_6_0:confirm(var_7_0.goods)
			end, SFX_PANEL)
		end
	end)

	arg_6_0.uiItemList = var_6_0

	return var_6_0
end

function var_0_0.updateUIItemList(arg_9_0)
	arg_9_0.uiItemList:align(#arg_9_0.diamondGoodsVOListForShow)
end

function var_0_0.updateView(arg_10_0)
	setActive(arg_10_0.monthCardTF, not arg_10_0.isNeedHideMonthCard)
	arg_10_0:updateUIItemList()
end

function var_0_0.confirm(arg_11_0, arg_11_1)
	if not arg_11_1 then
		return
	end

	arg_11_1 = Clone(arg_11_1)

	if arg_11_1:isChargeType() then
		local var_11_0 = not table.contains(arg_11_0.firstChargeIds, arg_11_1.id) and arg_11_1:firstPayDouble()
		local var_11_1 = var_11_0 and 4 or arg_11_1:getConfig("tag")

		if arg_11_1:isMonthCard() or arg_11_1:isGiftBox() or arg_11_1:isItemBox() or arg_11_1:isPassItem() then
			local var_11_2 = underscore.map(arg_11_1:getConfig("extra_service_item"), function(arg_12_0)
				return Drop.Create(arg_12_0)
			end)
			local var_11_3

			if arg_11_1:isPassItem() then
				local var_11_4 = arg_11_1:getConfig("sub_display")
				local var_11_5 = var_11_4[1]
				local var_11_6 = pg.battlepass_event_pt[var_11_5].pt

				var_11_3 = Drop.New({
					type = DROP_TYPE_RESOURCE,
					id = pg.battlepass_event_pt[var_11_5].pt,
					count = var_11_4[2]
				})
				var_11_2 = PlayerConst.MergePassItemDrop(underscore.map(pg.battlepass_event_pt[var_11_5].drop_client_pay, function(arg_13_0)
					return Drop.Create(arg_13_0)
				end))
			end

			local var_11_7 = arg_11_1:getConfig("gem") + arg_11_1:getConfig("extra_gem")
			local var_11_8

			if arg_11_1:isMonthCard() then
				var_11_8 = Drop.New({
					type = DROP_TYPE_RESOURCE,
					id = PlayerConst.ResDiamond,
					count = var_11_7
				})
			elseif var_11_7 > 0 then
				table.insert(var_11_2, Drop.New({
					type = DROP_TYPE_RESOURCE,
					id = PlayerConst.ResDiamond,
					count = var_11_7
				}))
			end

			local var_11_9
			local var_11_10

			if arg_11_1:isPassItem() then
				var_11_9 = i18n("battlepass_pay_tip")
			elseif arg_11_1:isMonthCard() then
				var_11_9 = i18n("charge_title_getitem_month")
				var_11_10 = i18n("charge_title_getitem_soon")
			else
				var_11_9 = i18n("charge_title_getitem")
			end

			local var_11_11 = {
				isChargeType = true,
				icon = "chargeicon/" .. arg_11_1:getConfig("picture"),
				name = arg_11_1:getConfig("name_display"),
				tipExtra = var_11_9,
				extraItems = var_11_2,
				price = arg_11_1:getConfig("money"),
				isLocalPrice = arg_11_1:IsLocalPrice(),
				tagType = var_11_1,
				isMonthCard = arg_11_1:isMonthCard(),
				tipBonus = var_11_10,
				bonusItem = var_11_8,
				extraDrop = var_11_3,
				descExtra = arg_11_1:getConfig("descrip_extra"),
				onYes = function()
					if ChargeConst.isNeedSetBirth() then
						arg_11_0:emit(ChargeMediator.OPEN_CHARGE_BIRTHDAY)
					else
						arg_11_0:emit(ChargeMediator.CHARGE, arg_11_1.id)
					end
				end
			}

			arg_11_0:emit(ChargeMediator.OPEN_CHARGE_ITEM_PANEL, var_11_11)
		elseif arg_11_1:isGem() then
			local var_11_12 = arg_11_1:getConfig("money")
			local var_11_13 = arg_11_1:getConfig("gem")

			if var_11_0 then
				var_11_13 = var_11_13 + arg_11_1:getConfig("gem")
			else
				var_11_13 = var_11_13 + arg_11_1:getConfig("extra_gem")
			end

			local var_11_14 = {
				isChargeType = true,
				icon = "chargeicon/" .. arg_11_1:getConfig("picture"),
				name = arg_11_1:getConfig("name_display"),
				price = arg_11_1:getConfig("money"),
				isLocalPrice = arg_11_1:IsLocalPrice(),
				tagType = var_11_1,
				normalTip = i18n("charge_start_tip", var_11_12, var_11_13),
				onYes = function()
					if ChargeConst.isNeedSetBirth() then
						arg_11_0:emit(ChargeMediator.OPEN_CHARGE_BIRTHDAY)
					else
						arg_11_0:emit(ChargeMediator.CHARGE, arg_11_1.id)
					end
				end
			}

			arg_11_0:emit(ChargeMediator.OPEN_CHARGE_ITEM_BOX, var_11_14)
		end
	else
		local var_11_15 = {}
		local var_11_16 = arg_11_1:getConfig("effect_args")
		local var_11_17 = Item.getConfigData(var_11_16[1])
		local var_11_18 = var_11_17.display_icon

		if type(var_11_18) == "table" then
			for iter_11_0, iter_11_1 in ipairs(var_11_18) do
				table.insert(var_11_15, {
					type = iter_11_1[1],
					id = iter_11_1[2],
					count = iter_11_1[3]
				})
			end
		end

		local var_11_19 = {
			isMonthCard = false,
			isChargeType = false,
			isLocalPrice = false,
			icon = var_11_17.icon,
			name = var_11_17.name,
			tipExtra = i18n("charge_title_getitem"),
			extraItems = var_11_15,
			price = arg_11_1:getConfig("resource_num"),
			tagType = arg_11_1:getConfig("tag"),
			onYes = function()
				pg.MsgboxMgr.GetInstance():ShowMsgBox({
					content = i18n("charge_scene_buy_confirm", arg_11_1:getConfig("resource_num"), var_11_17.name),
					onYes = function()
						arg_11_0:emit(ChargeMediator.BUY_ITEM, arg_11_1.id, 1)
					end
				})
			end
		}

		arg_11_0:emit(ChargeMediator.OPEN_CHARGE_ITEM_PANEL, var_11_19)
	end
end

function var_0_0.updateDiamondGoodsVOList(arg_18_0)
	arg_18_0.diamondGoodsVOList = {}

	local var_18_0 = pg.pay_data_display

	for iter_18_0, iter_18_1 in pairs(var_18_0.all) do
		local var_18_1 = var_18_0[iter_18_1].extra_service

		if arg_18_0.isNeedHideMonthCard and iter_18_1 == var_0_0.MonthCardID then
			-- block empty
		elseif pg.SdkMgr.GetInstance():IgnorePlatform(var_18_0[iter_18_1].ignorePlatform) then
			-- block empty
		elseif var_18_1 == Goods.MONTH_CARD or var_18_1 == Goods.GEM or var_18_1 == Goods.GIFT_BOX then
			local var_18_2 = Goods.Create({
				shop_id = iter_18_1
			}, Goods.TYPE_CHARGE)

			table.insert(arg_18_0.diamondGoodsVOList, var_18_2)
		end
	end
end

function var_0_0.sortDiamondGoodsVOList(arg_19_0)
	arg_19_0.diamondGoodsVOListForShow = {}

	for iter_19_0, iter_19_1 in ipairs(arg_19_0.diamondGoodsVOList) do
		local var_19_0 = ChargeConst.getBuyCount(arg_19_0.chargedList, iter_19_1.id)

		iter_19_1:updateBuyCount(var_19_0)

		if iter_19_1:canPurchase() and iter_19_1:inTime() then
			table.insert(arg_19_0.diamondGoodsVOListForShow, iter_19_1)
		end
	end

	table.sort(arg_19_0.diamondGoodsVOListForShow, function(arg_20_0, arg_20_1)
		local var_20_0 = not table.contains(arg_19_0.firstChargeIds, arg_20_0.id) and arg_20_0:firstPayDouble() and 1 or 0
		local var_20_1 = not table.contains(arg_19_0.firstChargeIds, arg_20_1.id) and arg_20_1:firstPayDouble() and 1 or 0
		local var_20_2 = 0
		local var_20_3 = 0

		if arg_20_0:isFree() then
			return true
		elseif arg_20_1:isFree() then
			return false
		end

		if arg_20_0:isChargeType() and arg_20_0:isMonthCard() then
			local var_20_4 = arg_19_0.player:getCardById(VipCard.MONTH)

			if var_20_4 then
				local var_20_5 = var_20_4:getLeftDate()
				local var_20_6 = pg.TimeMgr.GetInstance():GetServerTime()

				var_20_2 = math.floor((var_20_5 - var_20_6) / 86400) > (arg_20_0:getConfig("limit_arg") or 0) and 1 or 0
			end
		end

		if arg_20_1:isChargeType() and arg_20_1:isMonthCard() then
			local var_20_7 = arg_19_0.player:getCardById(VipCard.MONTH)

			if var_20_7 then
				local var_20_8 = var_20_7:getLeftDate()
				local var_20_9 = pg.TimeMgr.GetInstance():GetServerTime()

				var_20_3 = math.floor((var_20_8 - var_20_9) / 86400) > (arg_20_1:getConfig("limit_arg") or 0) and 1 or 0
			end
		end

		if var_20_2 ~= var_20_3 then
			return var_20_2 < var_20_3
		end

		local var_20_10 = arg_20_0:getConfig("tag") == 2 and 1 or 0
		local var_20_11 = arg_20_1:getConfig("tag") == 2 and 1 or 0

		if var_20_0 == var_20_1 and var_20_10 == var_20_11 then
			return arg_20_0.id < arg_20_1.id
		else
			return var_20_1 < var_20_0 or var_20_0 == var_20_1 and var_20_11 < var_20_10
		end
	end)
end

function var_0_0.updateGoodsData(arg_21_0)
	arg_21_0.firstChargeIds = arg_21_0.contextData.firstChargeIds
	arg_21_0.chargedList = arg_21_0.contextData.chargedList
	arg_21_0.normalList = arg_21_0.contextData.normalList
	arg_21_0.normalGroupList = arg_21_0.contextData.normalGroupList
end

function var_0_0.setGoodData(arg_22_0, arg_22_1, arg_22_2, arg_22_3, arg_22_4)
	arg_22_0.firstChargeIds = arg_22_1
	arg_22_0.chargedList = arg_22_2
	arg_22_0.normalList = arg_22_3
	arg_22_0.normalGroupList = arg_22_4
end

function var_0_0.updateData(arg_23_0)
	arg_23_0.player = getProxy(PlayerProxy):getData()

	arg_23_0:updateDiamondGoodsVOList()
	arg_23_0:sortDiamondGoodsVOList()
end

function var_0_0.reUpdateAll(arg_24_0)
	arg_24_0:updateData()
	arg_24_0:updateView()
end

return var_0_0
