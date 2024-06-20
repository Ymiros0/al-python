﻿local var_0_0 = class("ChargeGiftShopView", import("...base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "ChargeGiftShopUI"
end

function var_0_0.OnInit(arg_2_0)
	arg_2_0:initData()
	arg_2_0:initUI()
	arg_2_0:Show()
end

function var_0_0.OnDestroy(arg_3_0)
	for iter_3_0, iter_3_1 in pairs(arg_3_0.chargeCardTable or {}) do
		iter_3_1:destoryTimer()
	end

	arg_3_0:removeUpdateTimer()
end

function var_0_0.initData(arg_4_0)
	arg_4_0.giftGoodsVOList = {}
	arg_4_0.giftGoodsVOListForShow = {}
	arg_4_0.updateTime = nil
	arg_4_0.updateTimer = nil
	arg_4_0.player = getProxy(PlayerProxy):getData()

	arg_4_0:updateData()
end

function var_0_0.initUI(arg_5_0)
	arg_5_0.lScrollRect = GetComponent(arg_5_0._tf, "LScrollRect")
	arg_5_0.chargeCardTable = {}

	arg_5_0:initScrollRect()
	arg_5_0:updateScrollRect()
end

function var_0_0.initScrollRect(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
	arg_6_0.chargeCardTable = {}

	local function var_6_0(arg_7_0)
		local var_7_0 = ChargeCard.New(arg_7_0)

		onButton(arg_6_0, var_7_0.tr, function()
			if var_7_0.goods:isChargeType() and var_7_0.goods:isTecShipShowGift() then
				arg_6_0:emit(ChargeMediator.OPEN_TEC_SHIP_GIFT_SELL_LAYER, var_7_0.goods, arg_6_0.chargedList)
			else
				arg_6_0:confirm(var_7_0.goods)
			end
		end, SFX_PANEL)
		onButton(arg_6_0, var_7_0.viewBtn, function()
			if not var_7_0.goods:isChargeType() then
				return
			end

			local var_9_0 = var_7_0.goods:GetSkinProbability()
			local var_9_1 = getProxy(ShipSkinProxy):GetProbabilitySkins(var_9_0)

			if #var_9_0 <= 0 or #var_9_0 ~= #var_9_1 then
				local var_9_2 = var_7_0.goods:GetSkinProbabilityItem()

				arg_6_0:emit(BaseUI.ON_DROP, var_9_2)
			else
				arg_6_0:emit(ChargeMediator.VIEW_SKIN_PROBABILITY, var_7_0.goods.id)
			end
		end, SFX_PANEL)

		arg_6_0.chargeCardTable[arg_7_0] = var_7_0
	end

	local function var_6_1(arg_10_0, arg_10_1)
		local var_10_0 = arg_6_0.chargeCardTable[arg_10_1]

		if not var_10_0 then
			var_6_0(arg_10_1)

			var_10_0 = arg_6_0.chargeCardTable[arg_10_1]
		end

		local var_10_1 = arg_6_0.giftGoodsVOListForShow[arg_10_0 + 1]

		if var_10_1 then
			var_10_0:update(var_10_1, arg_6_0.player, arg_6_0.firstChargeIds)
		end
	end

	arg_6_0.lScrollRect.onInitItem = var_6_0
	arg_6_0.lScrollRect.onUpdateItem = var_6_1
end

function var_0_0.updateScrollRect(arg_11_0)
	arg_11_0.lScrollRect:SetTotalCount(#arg_11_0.giftGoodsVOListForShow, arg_11_0.lScrollRect.value)
end

function var_0_0.confirm(arg_12_0, arg_12_1)
	if not arg_12_1 then
		return
	end

	arg_12_1 = Clone(arg_12_1)

	if arg_12_1:isChargeType() then
		local var_12_0 = not table.contains(arg_12_0.firstChargeIds, arg_12_1.id) and arg_12_1:firstPayDouble()
		local var_12_1 = var_12_0 and 4 or arg_12_1:getConfig("tag")

		if arg_12_1:isMonthCard() or arg_12_1:isGiftBox() or arg_12_1:isItemBox() or arg_12_1:isPassItem() then
			local var_12_2 = underscore.map(arg_12_1:getConfig("extra_service_item"), function(arg_13_0)
				return Drop.Create(arg_13_0)
			end)
			local var_12_3

			if arg_12_1:isPassItem() then
				local var_12_4 = arg_12_1:getConfig("sub_display")
				local var_12_5 = var_12_4[1]
				local var_12_6 = pg.battlepass_event_pt[var_12_5].pt

				var_12_3 = Drop.New({
					type = DROP_TYPE_RESOURCE,
					id = pg.battlepass_event_pt[var_12_5].pt,
					count = var_12_4[2]
				})
				var_12_2 = PlayerConst.MergePassItemDrop(underscore.map(pg.battlepass_event_pt[var_12_5].drop_client_pay, function(arg_14_0)
					return Drop.Create(arg_14_0)
				end))
			end

			local var_12_7 = arg_12_1:getConfig("gem") + arg_12_1:getConfig("extra_gem")
			local var_12_8

			if arg_12_1:isMonthCard() then
				var_12_8 = Drop.New({
					type = DROP_TYPE_RESOURCE,
					id = PlayerConst.ResDiamond,
					count = var_12_7
				})
			elseif var_12_7 > 0 then
				table.insert(var_12_2, Drop.New({
					type = DROP_TYPE_RESOURCE,
					id = PlayerConst.ResDiamond,
					count = var_12_7
				}))
			end

			local var_12_9
			local var_12_10

			if arg_12_1:isPassItem() then
				var_12_9 = i18n("battlepass_pay_tip")
			elseif arg_12_1:isMonthCard() then
				var_12_9 = i18n("charge_title_getitem_month")
				var_12_10 = i18n("charge_title_getitem_soon")
			else
				var_12_9 = i18n("charge_title_getitem")
			end

			local var_12_11 = {
				isChargeType = true,
				icon = "chargeicon/" .. arg_12_1:getConfig("picture"),
				name = arg_12_1:getConfig("name_display"),
				tipExtra = var_12_9,
				extraItems = var_12_2,
				price = arg_12_1:getConfig("money"),
				isLocalPrice = arg_12_1:IsLocalPrice(),
				tagType = var_12_1,
				isMonthCard = arg_12_1:isMonthCard(),
				tipBonus = var_12_10,
				bonusItem = var_12_8,
				extraDrop = var_12_3,
				descExtra = arg_12_1:getConfig("descrip_extra"),
				limitArgs = arg_12_1:getConfig("limit_args"),
				onYes = function()
					if ChargeConst.isNeedSetBirth() then
						arg_12_0:emit(ChargeMediator.OPEN_CHARGE_BIRTHDAY)
					else
						arg_12_0:emit(ChargeMediator.CHARGE, arg_12_1.id)
					end
				end
			}

			arg_12_0:emit(ChargeMediator.OPEN_CHARGE_ITEM_PANEL, var_12_11)
		elseif arg_12_1:isGem() then
			local var_12_12 = arg_12_1:getConfig("money")
			local var_12_13 = arg_12_1:getConfig("gem")

			if var_12_0 then
				var_12_13 = var_12_13 + arg_12_1:getConfig("gem")
			else
				var_12_13 = var_12_13 + arg_12_1:getConfig("extra_gem")
			end

			local var_12_14 = {
				isChargeType = true,
				icon = "chargeicon/" .. arg_12_1:getConfig("picture"),
				name = arg_12_1:getConfig("name_display"),
				price = arg_12_1:getConfig("money"),
				isLocalPrice = arg_12_1:IsLocalPrice(),
				tagType = var_12_1,
				normalTip = i18n("charge_start_tip", var_12_12, var_12_13),
				onYes = function()
					if ChargeConst.isNeedSetBirth() then
						arg_12_0:emit(ChargeMediator.OPEN_CHARGE_BIRTHDAY)
					else
						arg_12_0:emit(ChargeMediator.CHARGE, arg_12_1.id)
					end
				end
			}

			arg_12_0:emit(ChargeMediator.OPEN_CHARGE_ITEM_BOX, var_12_14)
		end
	else
		local var_12_15 = {}
		local var_12_16 = arg_12_1:getConfig("effect_args")
		local var_12_17 = Item.getConfigData(var_12_16[1])
		local var_12_18 = var_12_17.display_icon

		if type(var_12_18) == "table" then
			for iter_12_0, iter_12_1 in ipairs(var_12_18) do
				table.insert(var_12_15, {
					type = iter_12_1[1],
					id = iter_12_1[2],
					count = iter_12_1[3]
				})
			end
		end

		local var_12_19 = {
			isMonthCard = false,
			isChargeType = false,
			isLocalPrice = false,
			icon = var_12_17.icon,
			name = var_12_17.name,
			tipExtra = i18n("charge_title_getitem"),
			extraItems = var_12_15,
			price = arg_12_1:getConfig("resource_num"),
			tagType = arg_12_1:getConfig("tag"),
			onYes = function()
				pg.MsgboxMgr.GetInstance():ShowMsgBox({
					content = i18n("charge_scene_buy_confirm", arg_12_1:getConfig("resource_num"), var_12_17.name),
					onYes = function()
						arg_12_0:emit(ChargeMediator.BUY_ITEM, arg_12_1.id, 1)
					end
				})
			end
		}

		arg_12_0:emit(ChargeMediator.OPEN_CHARGE_ITEM_PANEL, var_12_19)
	end
end

function var_0_0.updateGiftGoodsVOList(arg_19_0)
	arg_19_0.giftGoodsVOList = {}

	local var_19_0 = RefluxShopView.getAllRefluxPackID()
	local var_19_1 = pg.pay_data_display

	for iter_19_0, iter_19_1 in pairs(var_19_1.all) do
		if not table.contains(var_19_0, iter_19_1) then
			local var_19_2 = var_19_1[iter_19_1].extra_service

			if var_19_2 == Goods.ITEM_BOX or var_19_2 == Goods.PASS_ITEM then
				local var_19_3 = Goods.Create({
					shop_id = iter_19_1
				}, Goods.TYPE_CHARGE)

				if var_19_3:isTecShipGift() then
					if var_19_3:isTecShipShowGift() and arg_19_0:fliteTecShipGift(var_19_3) then
						table.insert(arg_19_0.giftGoodsVOList, var_19_3)
					end
				else
					table.insert(arg_19_0.giftGoodsVOList, var_19_3)
				end
			end
		end
	end

	for iter_19_2, iter_19_3 in pairs(pg.shop_template.get_id_list_by_genre.gift_package) do
		if not table.contains(var_19_0, iter_19_3) then
			local var_19_4 = Goods.Create({
				shop_id = iter_19_3
			}, Goods.TYPE_GIFT_PACKAGE)

			table.insert(arg_19_0.giftGoodsVOList, var_19_4)
		end
	end
end

function var_0_0.sortGiftGoodsVOList(arg_20_0)
	arg_20_0.giftGoodsVOListForShow = {}

	for iter_20_0, iter_20_1 in ipairs(arg_20_0.giftGoodsVOList) do
		if iter_20_1:isChargeType() then
			local var_20_0 = ChargeConst.getBuyCount(arg_20_0.chargedList, iter_20_1.id)

			iter_20_1:updateBuyCount(var_20_0)

			if iter_20_1:canPurchase() and iter_20_1:inTime() then
				table.insert(arg_20_0.giftGoodsVOListForShow, iter_20_1)
			end
		elseif not iter_20_1:isLevelLimit(arg_20_0.player.level, true) then
			local var_20_1 = ChargeConst.getBuyCount(arg_20_0.normalList, iter_20_1.id)

			iter_20_1:updateBuyCount(var_20_1)

			local var_20_2 = iter_20_1:getConfig("group") or 0
			local var_20_3 = false

			if var_20_2 > 0 then
				local var_20_4 = iter_20_1:getConfig("group_limit")
				local var_20_5 = ChargeConst.getGroupLimit(arg_20_0.normalGroupList, var_20_2)

				iter_20_1:updateGroupCount(var_20_5)

				var_20_3 = var_20_4 > 0 and var_20_4 <= var_20_5
			end

			local var_20_6, var_20_7 = pg.TimeMgr.GetInstance():inTime(iter_20_1:getConfig("time"))

			if var_20_7 then
				arg_20_0:addUpdateTimer(var_20_7)
			end

			if var_20_6 and iter_20_1:canPurchase() and not var_20_3 then
				table.insert(arg_20_0.giftGoodsVOListForShow, iter_20_1)
			end
		end
	end

	local function var_20_8(arg_21_0)
		local var_21_0 = arg_21_0:getConfig("time")
		local var_21_1 = 0

		if type(var_21_0) == "string" then
			var_21_1 = var_21_1 + 999999999999
		elseif type(var_21_0) == "table" then
			var_21_1 = pg.TimeMgr.GetInstance():parseTimeFromConfig(var_21_0[2]) - pg.TimeMgr.GetInstance():GetServerTime()
			var_21_1 = var_21_1 > 0 and var_21_1 or 999999999999
		else
			var_21_1 = var_21_1 + 999999999999
		end

		return var_21_1
	end

	local var_20_9 = {}
	local var_20_10 = getProxy(ActivityProxy)

	for iter_20_2, iter_20_3 in ipairs(var_20_10:getActivitiesByType(ActivityConst.ACTIVITY_TYPE_GIFT_UP)) do
		if var_20_10:IsActivityNotEnd(iter_20_3.id) then
			underscore(iter_20_3:getConfig("config_client").gifts):chain():flatten():map(function(arg_22_0)
				var_20_9[arg_22_0] = true
			end)
		end
	end

	table.sort(arg_20_0.giftGoodsVOListForShow, CompareFuncs({
		function(arg_23_0)
			return var_20_9[arg_23_0.id] and 0 or 1
		end,
		function(arg_24_0)
			return (arg_24_0:getConfig("type_order") - 1) % 1000
		end,
		function(arg_25_0)
			return var_20_8(arg_25_0)
		end,
		function(arg_26_0)
			return -arg_26_0:getConfig("tag")
		end,
		function(arg_27_0)
			return arg_27_0:getConfig("order") or 999
		end,
		function(arg_28_0)
			return arg_28_0.id
		end
	}))
end

function var_0_0.updateGoodsData(arg_29_0)
	arg_29_0.firstChargeIds = arg_29_0.contextData.firstChargeIds
	arg_29_0.chargedList = arg_29_0.contextData.chargedList
	arg_29_0.normalList = arg_29_0.contextData.normalList
	arg_29_0.normalGroupList = arg_29_0.contextData.normalGroupList
end

function var_0_0.setGoodData(arg_30_0, arg_30_1, arg_30_2, arg_30_3, arg_30_4)
	arg_30_0.firstChargeIds = arg_30_1
	arg_30_0.chargedList = arg_30_2
	arg_30_0.normalList = arg_30_3
	arg_30_0.normalGroupList = arg_30_4
end

function var_0_0.updateData(arg_31_0)
	arg_31_0.player = getProxy(PlayerProxy):getData()

	arg_31_0:updateGiftGoodsVOList()
	arg_31_0:sortGiftGoodsVOList()
end

function var_0_0.addUpdateTimer(arg_32_0, arg_32_1)
	local var_32_0 = pg.TimeMgr.GetInstance()
	local var_32_1 = var_32_0:Table2ServerTime(arg_32_1)

	if arg_32_0.updateTime and var_32_1 > var_32_0:Table2ServerTime(arg_32_0.updateTime) then
		return
	end

	arg_32_0.updateTime = arg_32_1

	arg_32_0:removeUpdateTimer()

	arg_32_0.updateTimer = Timer.New(function()
		if var_32_0:GetServerTime() > var_32_1 then
			arg_32_0:removeUpdateTimer()
			arg_32_0:reUpdateAll()
		end
	end, 1, -1)

	arg_32_0.updateTimer:Start()
	arg_32_0.updateTimer.func()
end

function var_0_0.removeUpdateTimer(arg_34_0)
	if arg_34_0.updateTimer then
		arg_34_0.updateTimer:Stop()

		arg_34_0.updateTimer = nil
	end
end

function var_0_0.reUpdateAll(arg_35_0)
	arg_35_0:updateData()
	arg_35_0:updateScrollRect()
end

function var_0_0.fliteTecShipGift(arg_36_0, arg_36_1)
	if arg_36_1:isChargeType() and arg_36_1:isTecShipShowGift() then
		if arg_36_1:isLevelLimit(arg_36_0.player.level, true) then
			return false
		end

		local var_36_0 = arg_36_1:getSameGroupTecShipGift()
		local var_36_1
		local var_36_2
		local var_36_3

		for iter_36_0, iter_36_1 in ipairs(var_36_0) do
			if iter_36_1:getConfig("limit_arg") == Goods.Tec_Ship_Gift_Arg.Normal then
				var_36_1 = iter_36_1
			elseif iter_36_1:getConfig("limit_arg") == Goods.Tec_Ship_Gift_Arg.High then
				var_36_2 = iter_36_1
			elseif iter_36_1:getConfig("limit_arg") == Goods.Tec_Ship_Gift_Arg.Up then
				var_36_3 = iter_36_1
			end
		end

		local var_36_4 = ChargeConst.getBuyCount(arg_36_0.chargedList, var_36_1.id)
		local var_36_5 = ChargeConst.getBuyCount(arg_36_0.chargedList, var_36_2.id)
		local var_36_6 = ChargeConst.getBuyCount(arg_36_0.chargedList, var_36_3.id)

		if var_36_5 > 0 then
			return false
		elseif var_36_4 > 0 and var_36_6 > 0 then
			return false
		else
			return true
		end
	else
		return true
	end
end

return var_0_0