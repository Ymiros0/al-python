﻿local var_0_0 = class("ShipExpItemUsagePage", import("...base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "ShipExpItemUsagePage"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.backBtn = arg_2_0:findTF("frame/top/btnBack")
	arg_2_0.confirmBtn = arg_2_0:findTF("frame/buttons/confirm")
	arg_2_0.recomBtn = arg_2_0:findTF("frame/buttons/recom")
	arg_2_0.clearBtn = arg_2_0:findTF("frame/buttons/clear")
	arg_2_0.levelTxt = arg_2_0:findTF("frame/content/level/Text"):GetComponent(typeof(Text))
	arg_2_0.expTxt = arg_2_0:findTF("frame/content/level/exp"):GetComponent(typeof(Text))
	arg_2_0.currentProgress = arg_2_0:findTF("frame/content/level/y"):GetComponent(typeof(Slider))
	arg_2_0.tipProgress = arg_2_0:findTF("frame/content/level/w"):GetComponent(typeof(Slider))
	arg_2_0.previewProgress = arg_2_0:findTF("frame/content/level/g"):GetComponent(typeof(Slider))
	arg_2_0.itemIds = arg_2_0:GetAllItemIDs()

	local var_2_0 = #arg_2_0.itemIds <= 3

	if var_2_0 then
		arg_2_0.uiItemList = UIItemList.New(arg_2_0:findTF("frame/content/items"), arg_2_0:findTF("frame/content/items/tpl"))
	else
		arg_2_0.uiItemList = UIItemList.New(arg_2_0:findTF("frame/content/scrollrect/content"), arg_2_0:findTF("frame/content/items/tpl"))
	end

	setActive(arg_2_0:findTF("frame/content/items"), var_2_0)
	setActive(arg_2_0:findTF("frame/content/scrollrect"), not var_2_0)
	setText(arg_2_0:findTF("frame/top/bg/infomation/title"), i18n("ship_exp_item_title"))
	setText(arg_2_0:findTF("frame/content/label"), i18n("coures_level_tip"))
	setText(arg_2_0.confirmBtn:Find("pic"), i18n("ship_exp_item_label_confirm"))
	setText(arg_2_0.recomBtn:Find("pic"), i18n("ship_exp_item_label_recom"))
	setText(arg_2_0.clearBtn:Find("pic"), i18n("ship_exp_item_label_clear"))
end

function var_0_0.OnInit(arg_3_0)
	arg_3_0.cards = {}

	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0:Hide()
	end, SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.backBtn, function()
		arg_3_0:Hide()
	end, SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.recomBtn, function()
		triggerButton(arg_3_0.clearBtn)

		local var_6_0 = arg_3_0:Recommand()

		for iter_6_0, iter_6_1 in pairs(arg_3_0.cards) do
			iter_6_1.value = var_6_0[iter_6_1.item.id] or 0

			iter_6_1:UpdateValue()
		end
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.clearBtn, function()
		for iter_7_0, iter_7_1 in pairs(arg_3_0.cards) do
			iter_7_1.value = 0

			iter_7_1:UpdateValue()
		end
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		if _.all(_.values(arg_3_0.itemCnts), function(arg_9_0)
			return arg_9_0 == 0
		end) then
			pg.TipsMgr.GetInstance():ShowTips(i18n("ship_remould_no_material"))

			return
		end

		local function var_8_0(arg_10_0)
			arg_3_0:emit(ShipMainMediator.ON_ADD_SHIP_EXP, arg_3_0.shipVO.id, arg_3_0.itemCnts)

			if arg_10_0 then
				arg_3_0:Hide()
			else
				arg_3_0:Flush(arg_3_0.shipVO)
			end
		end

		local var_8_1 = arg_3_0:GetAdditionExp()
		local var_8_2 = Clone(arg_3_0.shipVO)
		local var_8_3 = var_8_2:getMaxLevel()

		var_8_2.exp = var_8_2.exp + var_8_1

		local var_8_4 = false

		while var_8_2:canLevelUp() do
			var_8_2.exp = var_8_2.exp - var_8_2:getLevelExpConfig().exp_interval
			var_8_2.level = math.min(var_8_2.level + 1, var_8_3)
			var_8_4 = true
		end

		local var_8_5 = var_8_2.maxLevel <= var_8_2.level

		if var_8_4 and (var_8_2.maxLevel == var_8_2.level and var_8_2.exp > 0 or var_8_2.maxLevel < var_8_2.level) then
			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				content = i18n("coures_exp_overflow_tip", var_8_2.exp),
				onYes = function()
					var_8_0(var_8_5)
				end
			})
		else
			var_8_0(var_8_5)
		end
	end, SFX_PANEL)
	arg_3_0.uiItemList:make(function(arg_12_0, arg_12_1, arg_12_2)
		if arg_12_0 == UIItemList.EventUpdate then
			local var_12_0 = arg_3_0.itemIds[arg_12_1 + 1]

			arg_3_0:UpdateItemPanel(var_12_0, arg_12_2)
		end
	end)
end

function var_0_0.GetItem(arg_13_0, arg_13_1)
	return getProxy(BagProxy):getItemById(arg_13_1) or Drop.New({
		count = 0,
		type = DROP_TYPE_ITEM,
		id = arg_13_1
	})
end

function var_0_0.Recommand(arg_14_0)
	local var_14_0 = {}
	local var_14_1 = Clone(arg_14_0.shipVO)
	local var_14_2 = underscore.map(arg_14_0:GetAllItemIDs(), function(arg_15_0)
		return arg_14_0:GetItem(arg_15_0)
	end)

	table.sort(var_14_2, CompareFuncs({
		function(arg_16_0)
			return -arg_16_0.id
		end
	}))

	for iter_14_0, iter_14_1 in ipairs(var_14_2) do
		var_14_0[iter_14_1.id] = 0

		local var_14_3 = iter_14_1:getConfig("usage_arg")
		local var_14_4 = iter_14_0 < #var_14_2 and var_14_2[iter_14_0 + 1]:getConfig("usage_arg") or 0

		for iter_14_2 = 1, iter_14_1.count do
			if iter_14_0 ~= #var_14_2 and arg_14_0:PreCalcExpOverFlow(var_14_1, tonumber(var_14_3), tonumber(var_14_4)) then
				break
			else
				var_14_1:addExp(tonumber(var_14_3))

				var_14_0[iter_14_1.id] = var_14_0[iter_14_1.id] + 1

				if var_14_1.maxLevel == var_14_1.level then
					return var_14_0
				end
			end
		end
	end

	return var_14_0
end

function var_0_0.PreCalcExpOverFlow(arg_17_0, arg_17_1, arg_17_2, arg_17_3)
	local var_17_0 = arg_17_1.exp
	local var_17_1 = arg_17_1.level

	arg_17_1.exp = arg_17_1.exp + arg_17_2

	local var_17_2 = arg_17_1:getMaxLevel()

	while arg_17_1:canLevelUp() do
		arg_17_1.exp = arg_17_1.exp - arg_17_1:getLevelExpConfig().exp_interval
		arg_17_1.level = math.min(arg_17_1.level + 1, var_17_2)
	end

	local var_17_3 = var_17_2 <= arg_17_1.level and arg_17_3 < arg_17_1.exp

	arg_17_1.exp = var_17_0
	arg_17_1.level = var_17_1

	return var_17_3
end

function var_0_0.GetAllItemIDs(arg_18_0)
	local var_18_0 = pg.gameset.ship_exp_books.description
	local var_18_1 = {}

	for iter_18_0, iter_18_1 in ipairs(var_18_0) do
		if Item.getConfigData(iter_18_1) then
			table.insert(var_18_1, iter_18_1)
		end
	end

	return var_18_1
end

function var_0_0.Show(arg_19_0, arg_19_1)
	pg.UIMgr.GetInstance():BlurPanel(arg_19_0._tf, false, {
		weight = LayerWeightConst.BASE_LAYER + 2
	})
	var_0_0.super.Show(arg_19_0)
	arg_19_0:Flush(arg_19_1)
end

function var_0_0.Flush(arg_20_0, arg_20_1)
	arg_20_0.itemCnts = {}
	arg_20_0.shipVO = arg_20_1

	arg_20_0:InitItems()
	arg_20_0:UpdateLevelInfo()
end

function var_0_0.Hide(arg_21_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_21_0._tf, arg_21_0._parentTf)
	var_0_0.super.Hide(arg_21_0)
end

function var_0_0.InitItems(arg_22_0)
	table.sort(arg_22_0.itemIds, function(arg_23_0, arg_23_1)
		return arg_23_0 < arg_23_1
	end)
	arg_22_0.uiItemList:align(#arg_22_0.itemIds)
end

function var_0_0.UpdateItemPanel(arg_24_0, arg_24_1, arg_24_2)
	local var_24_0 = arg_24_0.cards[arg_24_2]

	if not var_24_0 then
		var_24_0 = ShipExpItemUsageCard.New(arg_24_2)

		var_24_0:SetCallBack(function(arg_25_0, arg_25_1, arg_25_2, arg_25_3)
			arg_24_0:OnAddItem(arg_25_0, arg_25_1, arg_25_2, arg_25_3)
		end)

		arg_24_0.cards[arg_24_2] = var_24_0
	end

	var_24_0:Update(arg_24_1)
end

function var_0_0.OnAddItem(arg_26_0, arg_26_1, arg_26_2, arg_26_3, arg_26_4)
	if arg_26_0.shipVO.maxLevel == arg_26_0.shipVO.level then
		arg_26_1:ForceUpdateValue(arg_26_0.itemCnts[arg_26_2])
		pg.TipsMgr.GetInstance():ShowTips(i18n("coures_tip_exceeded_lv"))

		return
	end

	local var_26_0 = Clone(arg_26_0.shipVO)
	local var_26_1 = 0

	for iter_26_0, iter_26_1 in pairs(arg_26_0.itemCnts) do
		if iter_26_0 ~= arg_26_2 then
			local var_26_2 = Item.getConfigData(iter_26_0).usage_arg

			var_26_1 = var_26_1 + tonumber(var_26_2) * iter_26_1
		end
	end

	var_26_0:addExp(var_26_1)

	local var_26_3 = Item.getConfigData(arg_26_2).usage_arg
	local var_26_4 = 0

	if arg_26_4 then
		var_26_4 = arg_26_3
	elseif var_26_0.level ~= var_26_0.maxLevel then
		for iter_26_2 = 1, arg_26_3 do
			var_26_0:addExp(tonumber(var_26_3))

			var_26_4 = var_26_4 + 1

			if var_26_0.maxLevel == var_26_0.level then
				break
			end
		end
	end

	if arg_26_3 > (arg_26_0.itemCnts[arg_26_2] or 0) then
		var_26_4 = math.max(arg_26_0.itemCnts[arg_26_2] or 0, var_26_4)
	end

	if arg_26_3 ~= var_26_4 then
		arg_26_1:ForceUpdateValue(var_26_4)

		arg_26_3 = var_26_4
	end

	arg_26_0.itemCnts[arg_26_2] = arg_26_3

	arg_26_0:UpdateLevelInfo()
end

function var_0_0.GetTempShipVO(arg_27_0, arg_27_1, arg_27_2)
	if arg_27_2 > 0 then
		local var_27_0 = Clone(arg_27_1)

		var_27_0:addExp(arg_27_2)

		return var_27_0
	end

	return arg_27_1
end

function var_0_0.GetAdditionExp(arg_28_0)
	local var_28_0 = 0

	for iter_28_0, iter_28_1 in pairs(arg_28_0.itemCnts) do
		local var_28_1 = Item.getConfigData(iter_28_0).usage_arg

		var_28_0 = var_28_0 + tonumber(var_28_1) * iter_28_1
	end

	return var_28_0
end

function var_0_0.UpdateLevelInfo(arg_29_0)
	local var_29_0 = arg_29_0.shipVO
	local var_29_1 = arg_29_0:GetAdditionExp()
	local var_29_2 = arg_29_0:GetTempShipVO(var_29_0, var_29_1)
	local var_29_3 = var_29_2.level - var_29_0.level
	local var_29_4 = var_29_3 <= 0 and (var_29_1 > 0 and "+0" or "") or "<color=" .. COLOR_GREEN .. ">+" .. var_29_3 .. "</color>"

	arg_29_0.levelTxt.text = var_29_0.level .. var_29_4

	local var_29_5 = var_29_0:getLevelExpConfig().exp_interval

	arg_29_0.expTxt.text = string.format("%d<color=%s>(+%d)</color>/%d", var_29_0.exp, COLOR_GREEN, var_29_1, var_29_5)

	local var_29_6 = var_29_0.exp / var_29_5

	arg_29_0.currentProgress.value = var_29_6
	arg_29_0.tipProgress.value = var_29_1 <= 0 and var_29_6 or var_29_6 + 0.003
	arg_29_0.previewProgress.value = var_29_1 <= 0 and 0 or var_29_3 >= 1 and 1 or var_29_2.exp / var_29_5
end

function var_0_0.OnDestroy(arg_30_0)
	for iter_30_0, iter_30_1 in pairs(arg_30_0.cards) do
		iter_30_1:Dispose()
	end

	arg_30_0.cards = nil
end

return var_0_0
