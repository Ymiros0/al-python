﻿local var_0_0 = class("ChargeTecShipGiftSellLayer", import("...base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "ChargeTecShipGiftSellLayer"
end

function var_0_0.init(arg_2_0)
	arg_2_0:initData()
	arg_2_0:findUI()
	arg_2_0:addListener()
	arg_2_0:initUIText()
end

function var_0_0.didEnter(arg_3_0)
	pg.UIMgr.GetInstance():BlurPanel(arg_3_0._tf)
	arg_3_0:updateGiftList()
end

function var_0_0.willExit(arg_4_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_4_0._tf)
end

function var_0_0.initData(arg_5_0)
	arg_5_0.showGoodVO = arg_5_0.contextData.showGoodVO
	arg_5_0.chargedList = arg_5_0.contextData.chargedList
	arg_5_0.goodVOList = arg_5_0.showGoodVO:getSameGroupTecShipGift()
	arg_5_0.normalGoodVO = nil
	arg_5_0.highGoodVO = nil
	arg_5_0.upGoodVO = nil

	for iter_5_0, iter_5_1 in ipairs(arg_5_0.goodVOList) do
		if iter_5_1:getConfig("limit_arg") == Goods.Tec_Ship_Gift_Arg.Normal then
			arg_5_0.normalGoodVO = iter_5_1
		elseif iter_5_1:getConfig("limit_arg") == Goods.Tec_Ship_Gift_Arg.High then
			arg_5_0.highGoodVO = iter_5_1
		elseif iter_5_1:getConfig("limit_arg") == Goods.Tec_Ship_Gift_Arg.Up then
			arg_5_0.upGoodVO = iter_5_1
		end
	end

	arg_5_0.goodVOShowList = {}

	local var_5_0 = ChargeConst.getBuyCount(arg_5_0.chargedList, arg_5_0.normalGoodVO.id)
	local var_5_1 = ChargeConst.getBuyCount(arg_5_0.chargedList, arg_5_0.highGoodVO.id)
	local var_5_2 = ChargeConst.getBuyCount(arg_5_0.chargedList, arg_5_0.upGoodVO.id)

	if var_5_0 == 0 and var_5_1 == 0 and var_5_2 == 0 then
		table.insert(arg_5_0.goodVOShowList, arg_5_0.normalGoodVO)
		table.insert(arg_5_0.goodVOShowList, arg_5_0.highGoodVO)
	elseif var_5_0 > 0 and var_5_1 == 0 and var_5_2 == 0 then
		table.insert(arg_5_0.goodVOShowList, arg_5_0.normalGoodVO)
		table.insert(arg_5_0.goodVOShowList, arg_5_0.upGoodVO)
	elseif (not (var_5_0 > 0) or not (var_5_2 > 0)) and var_5_1 > 0 then
		-- block empty
	end
end

function var_0_0.initUIText(arg_6_0)
	local var_6_0 = arg_6_0:findTF("Adapt/TipBG/Text")

	setText(var_6_0, i18n("tech_package_tip"))
end

function var_0_0.findUI(arg_7_0)
	arg_7_0.bg = arg_7_0:findTF("BG")

	local var_7_0 = GetComponent(arg_7_0._tf, "ItemList").prefabItem[0]
	local var_7_1 = Instantiate(var_7_0)

	arg_7_0.itemTpl = arg_7_0:findTF("ItemTpl")

	local var_7_2 = arg_7_0:findTF("Container", arg_7_0.itemTpl)

	setParent(var_7_1, var_7_2, false)

	arg_7_0.giftTpl = arg_7_0:findTF("GiftTpl")
	arg_7_0.giftContainer = arg_7_0:findTF("List")
	arg_7_0.giftUIItemList = UIItemList.New(arg_7_0.giftContainer, arg_7_0.giftTpl)

	arg_7_0.giftUIItemList:make(function(arg_8_0, arg_8_1, arg_8_2)
		if arg_8_0 == UIItemList.EventUpdate then
			arg_8_1 = arg_8_1 + 1

			local var_8_0 = arg_7_0.goodVOShowList[arg_8_1]

			arg_7_0:updateGiftTF(arg_8_2, var_8_0)
		end
	end)
end

function var_0_0.addListener(arg_9_0)
	onButton(arg_9_0, arg_9_0.bg, function()
		arg_9_0:closeView()
	end, SFX_PANEL)
end

function var_0_0.updateGiftTF(arg_11_0, arg_11_1, arg_11_2)
	local var_11_0 = arg_11_0:findTF("BG/Normal", arg_11_1)
	local var_11_1 = arg_11_0:findTF("BG/Special", arg_11_1)
	local var_11_2 = arg_11_0:findTF("Buy/Normal", arg_11_1)
	local var_11_3 = arg_11_0:findTF("Buy/Special", arg_11_1)
	local var_11_4 = arg_11_0:findTF("Buy/Up", arg_11_1)
	local var_11_5 = arg_11_0:findTF("Buy/Disable", arg_11_1)
	local var_11_6 = arg_11_0:findTF("Title", arg_11_1)
	local var_11_7 = arg_11_0:findTF("GiftImage", arg_11_1)
	local var_11_8 = arg_11_0:findTF("Desc1", arg_11_1)
	local var_11_9 = arg_11_0:findTF("Desc2", arg_11_1)
	local var_11_10 = arg_11_0:findTF("List", arg_11_1)
	local var_11_11 = arg_11_2:getConfig("limit_arg") == Goods.Tec_Ship_Gift_Arg.Normal
	local var_11_12 = arg_11_2:getConfig("limit_arg") == Goods.Tec_Ship_Gift_Arg.High
	local var_11_13 = arg_11_2:getConfig("limit_arg") == Goods.Tec_Ship_Gift_Arg.Up
	local var_11_14 = ChargeConst.getBuyCount(arg_11_0.chargedList, arg_11_0.normalGoodVO.id) > 0

	setActive(var_11_0, var_11_11)
	setActive(var_11_1, not var_11_11)
	setActive(var_11_2, var_11_11 and not var_11_14)
	setActive(var_11_3, var_11_12)
	setActive(var_11_4, var_11_13)
	setActive(var_11_5, var_11_11 and var_11_14)

	if var_11_11 and var_11_14 then
		setGray(arg_11_1, true, true)
	end

	local function var_11_15()
		pg.m02:sendNotification(GAME.CHARGE_OPERATION, {
			shopId = arg_11_2.id
		})
		arg_11_0:closeView()
	end

	onButton(arg_11_0, var_11_2, function()
		var_11_15()
	end, SFX_PANEL)
	onButton(arg_11_0, var_11_3, function()
		var_11_15()
	end, SFX_PANEL)
	onButton(arg_11_0, var_11_4, function()
		var_11_15()
	end, SFX_PANEL)
	setText(var_11_6, arg_11_2:getConfig("name_display"))
	setText(var_11_8, arg_11_2:getConfig("descrip"))
	setText(var_11_9, arg_11_2:getConfig("descrip_extra"))
	setImageSprite(var_11_7, LoadSprite("chargeicon/" .. arg_11_2:getConfig("picture")), true)

	local var_11_16 = {}

	for iter_11_0, iter_11_1 in ipairs(arg_11_2:getConfig("display")) do
		table.insert(var_11_16, Drop.Create(iter_11_1))
	end

	local var_11_17 = UIItemList.New(var_11_10, arg_11_0.itemTpl)

	var_11_17:make(function(arg_16_0, arg_16_1, arg_16_2)
		if arg_16_0 == UIItemList.EventUpdate then
			local var_16_0 = arg_11_0:findTF("Container", arg_16_2):GetChild(0)
			local var_16_1 = arg_11_0:findTF("TextMask/Text", arg_16_2)

			arg_16_1 = arg_16_1 + 1

			local var_16_2 = var_11_16[arg_16_1]

			updateDrop(var_16_0, var_16_2)
			onButton(arg_11_0, var_16_0, function()
				arg_11_0:emit(BaseUI.ON_DROP, var_16_2)
			end, SFX_PANEL)
			setScrollText(var_16_1, var_16_2:getName())
		end
	end)
	var_11_17:align(#var_11_16)
end

function var_0_0.updateGiftList(arg_18_0)
	arg_18_0.giftUIItemList:align(#arg_18_0.goodVOShowList)
end

return var_0_0
