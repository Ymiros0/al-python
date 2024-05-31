﻿local var_0_0 = class("ChargeItemBoxLayer", import("...base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "ChargeItemBoxUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0:initData()
	arg_2_0:findUI()
	arg_2_0:addListener()
	arg_2_0:initUIText()
end

function var_0_0.didEnter(arg_3_0)
	arg_3_0:updatePanel()
	pg.UIMgr.GetInstance():BlurPanel(arg_3_0._tf)
end

function var_0_0.willExit(arg_4_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_4_0._tf)
end

function var_0_0.initData(arg_5_0)
	arg_5_0.panelConfig = arg_5_0.contextData.panelConfig
end

function var_0_0.initUIText(arg_6_0)
	local var_6_0 = arg_6_0:findTF("window/button_container/button_cancel/Image")
	local var_6_1 = arg_6_0:findTF("window/button_container/button_ok/Image")

	setText(var_6_0, i18n("text_cancel"))
	setText(var_6_1, i18n("text_buy"))
end

function var_0_0.findUI(arg_7_0)
	arg_7_0.bg = arg_7_0:findTF("back_sign")
	arg_7_0.detailWindow = arg_7_0:findTF("window")
	arg_7_0.cancelBtn = arg_7_0:findTF("button_container/button_cancel", arg_7_0.detailWindow)
	arg_7_0.confirmBtn = arg_7_0:findTF("button_container/button_ok", arg_7_0.detailWindow)
	arg_7_0.detailName = arg_7_0:findTF("goods/name", arg_7_0.detailWindow)
	arg_7_0.detailIcon = arg_7_0:findTF("goods/icon", arg_7_0.detailWindow)
	arg_7_0.detailRmb = arg_7_0:findTF("prince_bg/contain/icon_rmb", arg_7_0.detailWindow)
	arg_7_0.detailGem = arg_7_0:findTF("prince_bg/contain/icon_gem", arg_7_0.detailWindow)
	arg_7_0.detailPrice = arg_7_0:findTF("prince_bg/contain/Text", arg_7_0.detailWindow)
	arg_7_0.detailTag = arg_7_0:findTF("goods/tag", arg_7_0.detailWindow)
	arg_7_0.detailTags = {}

	table.insert(arg_7_0.detailTags, arg_7_0:findTF("hot", arg_7_0.detailTag))
	table.insert(arg_7_0.detailTags, arg_7_0:findTF("new", arg_7_0.detailTag))
	table.insert(arg_7_0.detailTags, arg_7_0:findTF("advice", arg_7_0.detailTag))
	table.insert(arg_7_0.detailTags, arg_7_0:findTF("double", arg_7_0.detailTag))
	table.insert(arg_7_0.detailTags, arg_7_0:findTF("discount", arg_7_0.detailTag))

	arg_7_0.detailTagAdviceTF = arg_7_0.detailTags[3]
	arg_7_0.detailTagDoubleTF = arg_7_0.detailTags[4]
	arg_7_0.detailNormalTip = arg_7_0:findTF("NormalTips", arg_7_0.detailWindow)
end

function var_0_0.addListener(arg_8_0)
	onButton(arg_8_0, arg_8_0.bg, function()
		arg_8_0:closeView()
	end, SFX_PANEL)
	onButton(arg_8_0, arg_8_0.cancelBtn, function()
		arg_8_0:closeView()
	end, SFX_PANEL)
	onButton(arg_8_0, arg_8_0.confirmBtn, function()
		if arg_8_0.panelConfig.onYes then
			arg_8_0.panelConfig.onYes()
			arg_8_0:closeView()
		end
	end, SFX_PANEL)
end

function var_0_0.updatePanel(arg_12_0)
	local var_12_0 = arg_12_0.panelConfig.icon
	local var_12_1 = arg_12_0.panelConfig.name and arg_12_0.panelConfig.name or ""

	if not arg_12_0.panelConfig.tipBonus then
		local var_12_2 = ""
	end

	local var_12_3 = arg_12_0.panelConfig.bonusItem

	if not arg_12_0.panelConfig.tipExtra or not arg_12_0.panelConfig.tipExtra then
		local var_12_4 = ""
	end

	if not arg_12_0.panelConfig.extraItems or not arg_12_0.panelConfig.extraItems then
		local var_12_5 = {}
	end

	local var_12_6 = arg_12_0.panelConfig.price and arg_12_0.panelConfig.price or 0
	local var_12_7 = arg_12_0.panelConfig.isChargeType
	local var_12_8 = arg_12_0.panelConfig.isLocalPrice
	local var_12_9 = arg_12_0.panelConfig.isMonthCard
	local var_12_10 = arg_12_0.panelConfig.tagType
	local var_12_11 = arg_12_0.panelConfig.normalTip
	local var_12_12 = arg_12_0.panelConfig.extraDrop

	if arg_12_0.detailNormalTip then
		setActive(arg_12_0.detailNormalTip, var_12_11)
	end

	if var_12_11 then
		if arg_12_0.detailNormalTip:GetComponent("Text") then
			setText(arg_12_0.detailNormalTip, var_12_11)
		else
			setButtonText(arg_12_0.detailNormalTip, var_12_11)
		end
	end

	setActive(arg_12_0.detailTag, var_12_10 > 0)

	if var_12_10 > 0 then
		for iter_12_0, iter_12_1 in ipairs(arg_12_0.detailTags) do
			setActive(iter_12_1, iter_12_0 == var_12_10)
		end
	end

	GetImageSpriteFromAtlasAsync(var_12_0, "", arg_12_0.detailIcon, false)
	setText(arg_12_0.detailName, var_12_1)

	if PLATFORM_CODE == PLATFORM_CHT then
		setActive(arg_12_0.detailRmb, var_12_7 and not var_12_8)
	else
		setActive(arg_12_0.detailRmb, var_12_7)
	end

	setActive(arg_12_0.detailGem, not var_12_7)
	setText(arg_12_0.detailPrice, var_12_6)
end

return var_0_0
