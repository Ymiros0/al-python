﻿local var_0_0 = class("ChargeMenuScene", import("...base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "ChargeMenuUI"
end

function var_0_0.preload(arg_2_0, arg_2_1)
	if getProxy(ShopsProxy):ShouldRefreshChargeList() then
		pg.m02:sendNotification(GAME.GET_CHARGE_LIST, {
			callback = arg_2_1
		})
	else
		arg_2_1()
	end
end

function var_0_0.init(arg_3_0)
	arg_3_0:initData()
	arg_3_0:findUI()
	arg_3_0:addListener()
	arg_3_0:initUIText()
	arg_3_0:InitBanner()
end

function var_0_0.didEnter(arg_4_0)
	arg_4_0:updatePlayerRes()
	arg_4_0:updatePanel()
	arg_4_0:tryAutoOpenShop()
end

function var_0_0.ResUISettings(arg_5_0)
	return true
end

function var_0_0.onBackPressed(arg_6_0)
	if arg_6_0.chargeTipWindow and arg_6_0.chargeTipWindow:GetLoaded() and arg_6_0.chargeTipWindow:isShowing() then
		arg_6_0.chargeTipWindow:Hide()

		return
	end

	var_0_0.super.onBackPressed(arg_6_0)
end

function var_0_0.willExit(arg_7_0)
	if arg_7_0.bannerRect then
		arg_7_0.bannerRect:Dispose()

		arg_7_0.bannerRect = nil
	end

	if arg_7_0.chargeOrPurchaseHandler then
		arg_7_0.chargeOrPurchaseHandler:Dispose()

		arg_7_0.chargeOrPurchaseHandler = nil
	end

	if arg_7_0.chargeTipWindow then
		arg_7_0.chargeTipWindow:Destroy()

		arg_7_0.chargeTipWindow = nil
	end
end

function var_0_0.initData(arg_8_0)
	return
end

function var_0_0.initUIText(arg_9_0)
	return
end

function var_0_0.findUI(arg_10_0)
	arg_10_0.blurTF = arg_10_0:findTF("blur_panel")
	arg_10_0.topTF = arg_10_0:findTF("adapt/top", arg_10_0.blurTF)
	arg_10_0.resTF = arg_10_0:findTF("res", arg_10_0.topTF)
	arg_10_0.backBtn = arg_10_0:findTF("back_button", arg_10_0.topTF)
	arg_10_0.menuTF = arg_10_0:findTF("menu_screen")
	arg_10_0.skinShopBtn = arg_10_0:findTF("skin_shop", arg_10_0.menuTF)
	arg_10_0.diamondShopBtn = arg_10_0:findTF("dimond_shop", arg_10_0.menuTF)
	arg_10_0.itemShopBtn = arg_10_0:findTF("props", arg_10_0.menuTF)
	arg_10_0.giftShopBtn = arg_10_0:findTF("gift_shop", arg_10_0.menuTF)
	arg_10_0.supplyShopBtn = arg_10_0:findTF("supply", arg_10_0.menuTF)
	arg_10_0.monthCardTag = arg_10_0:findTF("monthcard_tag", arg_10_0.diamondShopBtn)
	arg_10_0.giftTag = arg_10_0:findTF("tip", arg_10_0.giftShopBtn)
	arg_10_0.bannerRect = BannerScrollRect.New(arg_10_0:findTF("menu_screen/banner/mask/content"), arg_10_0:findTF("menu_screen/banner/dots"))
	arg_10_0.chargeOrPurchaseHandler = ChargeOrPurchaseHandler.New()
	arg_10_0.chargeTipWindow = ChargeTipWindow.New(arg_10_0._tf, arg_10_0.event)
end

local function var_0_1(arg_11_0, arg_11_1, arg_11_2)
	setText(arg_11_1:Find("name"), arg_11_2:GetName())
	setText(arg_11_1:Find("desc"), arg_11_2:GetDesc())

	local var_11_0 = arg_11_2:GetDropList()
	local var_11_1 = UIItemList.New(arg_11_1:Find("items"), arg_11_1:Find("items/award"))

	var_11_1:make(function(arg_12_0, arg_12_1, arg_12_2)
		if arg_12_0 == UIItemList.EventUpdate then
			local var_12_0 = var_11_0[arg_12_1 + 1]

			updateDrop(arg_12_2, var_12_0)
			onButton(arg_11_0, arg_12_2, function()
				arg_11_0:emit(BaseUI.ON_DROP, var_12_0)
			end, SFX_PANEL)
		end
	end)
	var_11_1:align(#var_11_0)

	local var_11_2 = arg_11_2:GetGem()

	setActive(arg_11_1:Find("gem"), var_11_2 > 0)
	setText(arg_11_1:Find("gem/Text"), var_11_2)

	local var_11_3, var_11_4, var_11_5 = arg_11_2:GetPrice()

	setText(arg_11_1:Find("price/Text"), var_11_4)
	setActive(arg_11_1:Find("price/Text/icon"), var_11_3 ~= RecommendCommodity.PRICE_TYPE_RMB)
	setText(arg_11_1:Find("price/Text/label"), var_11_3 == RecommendCommodity.PRICE_TYPE_RMB and GetMoneySymbol() or "")

	local var_11_6 = arg_11_1:Find("icon")

	GetSpriteFromAtlasAsync(arg_11_2:GetIcon(), "", function(arg_14_0)
		setImageSprite(var_11_6, arg_14_0)
	end)

	var_11_6.sizeDelta = Vector2(180, 180)
end

function var_0_0.InitBanner(arg_15_0)
	local var_15_0 = getProxy(ShopsProxy):GetRecommendCommodities()

	for iter_15_0, iter_15_1 in ipairs(var_15_0) do
		local var_15_1 = arg_15_0.bannerRect:AddChild()

		var_0_1(arg_15_0, var_15_1, iter_15_1)
		onButton(arg_15_0, var_15_1, function()
			local var_16_0, var_16_1 = iter_15_1:IsMonthCardAndCantPurchase()

			if var_16_0 then
				pg.TipsMgr.GetInstance():ShowTips(var_16_1)

				return
			end

			arg_15_0.bannerRect:Puase()

			arg_15_0.lookUpIndex = iter_15_0

			pg.m02:sendNotification(GAME.TRACK, TrackConst.GetTrackData(TrackConst.SYSTEM_SHOP, TrackConst.ACTION_LOOKUP_RECOMMEND, iter_15_0))
			arg_15_0.chargeOrPurchaseHandler:ChargeOrPurchaseAsyn(iter_15_1:GetRealCommodity())
		end, SFX_PANEL)
	end

	arg_15_0.bannerRect:SetUp()
end

function var_0_0.FlushBanner(arg_17_0)
	arg_17_0.bannerRect:Reset()
	arg_17_0:InitBanner()
end

function var_0_0.addListener(arg_18_0)
	onButton(arg_18_0, arg_18_0.backBtn, function()
		arg_18_0:closeView()
	end, SFX_CANCEL)
	onButton(arg_18_0, arg_18_0.skinShopBtn, function()
		arg_18_0:emit(ChargeMenuMediator.GO_SKIN_SHOP)
	end, SFX_PANEL)
	onButton(arg_18_0, arg_18_0.diamondShopBtn, function()
		arg_18_0:emit(ChargeMenuMediator.GO_CHARGE_SHOP, ChargeScene.TYPE_DIAMOND)
	end, SFX_PANEL)
	onButton(arg_18_0, arg_18_0.giftShopBtn, function()
		arg_18_0:emit(ChargeMenuMediator.GO_CHARGE_SHOP, ChargeScene.TYPE_GIFT)

		local var_22_0 = isActive(arg_18_0.giftTag)

		pg.m02:sendNotification(GAME.TRACK, TrackConst.GetTrackData(TrackConst.SYSTEM_SHOP, TrackConst.ACTION_ENTER_GIFT, var_22_0))
	end, SFX_PANEL)
	onButton(arg_18_0, arg_18_0.itemShopBtn, function()
		arg_18_0:emit(ChargeMenuMediator.GO_CHARGE_SHOP, ChargeScene.TYPE_ITEM)
	end, SFX_PANEL)
	onButton(arg_18_0, arg_18_0.supplyShopBtn, function()
		arg_18_0:emit(ChargeMenuMediator.GO_SUPPLY_SHOP, {
			warp = NewShopsScene.TYPE_SHOP_STREET
		})
	end, SFX_PANEL)
end

function var_0_0.updatePlayerRes(arg_25_0)
	return
end

function var_0_0.updatePanel(arg_26_0)
	local var_26_0 = getProxy(ActivityProxy)
	local var_26_1 = var_26_0:getActiveBannerByType(GAMEUI_BANNER_9)

	if var_26_1 ~= nil then
		LoadImageSpriteAsync("activitybanner/" .. var_26_1.pic, arg_26_0.skinShopBtn)
	end

	local var_26_2 = var_26_0:getActiveBannerByType(GAMEUI_BANNER_11)

	if var_26_2 ~= nil then
		LoadImageSpriteAsync("activitybanner/" .. var_26_2.pic, arg_26_0:findTF("BG", arg_26_0.giftShopBtn))
	end

	local var_26_3 = MonthCardOutDateTipPanel.GetShowMonthCardTag()

	setActive(arg_26_0.monthCardTag, var_26_3)
	MonthCardOutDateTipPanel.SetMonthCardTagDate()
	TagTipHelper.SetFuDaiTagMark()
	TagTipHelper.SetSkinTagMark()
	TagTipHelper.FreeGiftTag({
		arg_26_0.giftTag
	})
end

function var_0_0.tryAutoOpenShop(arg_27_0)
	local var_27_0 = arg_27_0.contextData.wrap

	if var_27_0 ~= nil then
		if var_27_0 == ChargeScene.TYPE_DIAMOND then
			triggerButton(arg_27_0.diamondShopBtn)
		elseif var_27_0 == ChargeScene.TYPE_GIFT then
			triggerButton(arg_27_0.giftShopBtn)
		elseif var_27_0 == ChargeScene.TYPE_ITEM then
			triggerButton(arg_27_0.itemShopBtn)
		end
	end
end

function var_0_0.OnRemoveLayer(arg_28_0, arg_28_1)
	if arg_28_1.mediator == ChargeItemPanelMediator and arg_28_0.bannerRect then
		arg_28_0.bannerRect:Resume()
	end
end

function var_0_0.OnChargeSuccess(arg_29_0, arg_29_1)
	arg_29_0.chargeTipWindow:ExecuteAction("Show", arg_29_1)
end

return var_0_0
