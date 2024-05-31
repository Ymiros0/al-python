local var_0_0 = class("BaseShopPage", import("...base.BaseSubView"))

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4)
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)

	arg_1_0.lScrollrect = arg_1_4
	arg_1_0.scrollbar = arg_1_1:Find("Scrollbar")

	assert(arg_1_0.lScrollrect)
end

function var_0_0.Load(arg_2_0)
	if arg_2_0._state ~= var_0_0.STATES.NONE then
		return
	end

	arg_2_0._state = var_0_0.STATES.LOADING

	pg.UIMgr.GetInstance():LoadingOn()

	local var_2_0 = GameObject.Find("__Pool__")
	local var_2_1 = findTF(var_2_0, arg_2_0:getUIName())

	if IsNil(var_2_1) then
		PoolMgr.GetInstance():GetUI(arg_2_0:getUIName(), true, function(arg_3_0)
			arg_2_0:Loaded(arg_3_0)
			arg_2_0:Init()
		end)
	else
		arg_2_0:Loaded(var_2_1.gameObject)
		arg_2_0:Init()
	end
end

function var_0_0.Loaded(arg_4_0, arg_4_1)
	arg_4_0.canvasGroup = arg_4_1:GetComponent(typeof(CanvasGroup))

	assert(arg_4_0.canvasGroup)
	var_0_0.super.Loaded(arg_4_0, arg_4_1)
end

function var_0_0.SetShop(arg_5_0, arg_5_1)
	arg_5_0.shop = arg_5_1
end

function var_0_0.SetPlayer(arg_6_0, arg_6_1)
	arg_6_0.player = arg_6_1

	arg_6_0:OnUpdatePlayer()
end

function var_0_0.SetItems(arg_7_0, arg_7_1)
	arg_7_0.items = arg_7_1

	arg_7_0:OnUpdateItems()
end

function var_0_0.SetUp(arg_8_0, arg_8_1, arg_8_2, arg_8_3)
	arg_8_0:SetShop(arg_8_1)
	arg_8_0:Show()
	arg_8_0:SetPlayer(arg_8_2)
	arg_8_0:SetItems(arg_8_3)
	arg_8_0:InitCommodities()
	arg_8_0:OnSetUp()
	arg_8_0:SetPainting()
end

function var_0_0.InitCommodities(arg_9_0)
	arg_9_0.displays, arg_9_0.cards = arg_9_0.shop:GetCommodities(), {}

	arg_9_0.lScrollrect:SetTotalCount(#arg_9_0.displays, 0)
	setActive(arg_9_0.scrollbar, #arg_9_0.displays > 10)
end

function var_0_0.Show(arg_10_0)
	function arg_10_0.lScrollrect.onInitItem(arg_11_0)
		arg_10_0:OnInitItem(arg_11_0)
	end

	function arg_10_0.lScrollrect.onUpdateItem(arg_12_0, arg_12_1)
		arg_10_0:OnUpdateItem(arg_12_0, arg_12_1)
	end

	arg_10_0.canvasGroup.alpha = 1
	arg_10_0.canvasGroup.blocksRaycasts = true

	arg_10_0:ShowOrHideResUI(true)
end

function var_0_0.Hide(arg_13_0)
	for iter_13_0, iter_13_1 in pairs(arg_13_0.cards) do
		iter_13_1:Dispose()
	end

	arg_13_0.displays = {}
	arg_13_0.cards = {}

	ClearLScrollrect(arg_13_0.lScrollrect)

	arg_13_0.canvasGroup.alpha = 0
	arg_13_0.canvasGroup.blocksRaycasts = false

	arg_13_0:ShowOrHideResUI(false)
end

function var_0_0.Destroy(arg_14_0)
	if arg_14_0:isShowing() then
		arg_14_0:Hide()
	end

	var_0_0.super.Destroy(arg_14_0)
end

function var_0_0.SetPainting(arg_15_0)
	local var_15_0, var_15_1, var_15_2 = arg_15_0:GetPaintingName()

	if arg_15_0.contextData.paintingView.name ~= var_15_0 then
		arg_15_0.contextData.paintingView:Init(var_15_0, var_15_1, var_15_2, function()
			local var_16_0, var_16_1, var_16_2 = arg_15_0:GetPaintingEnterVoice()

			arg_15_0.contextData.paintingView:Chat(var_16_0, var_16_1, var_16_2, true)
		end)
		onButton(arg_15_0, arg_15_0.contextData.paintingView.touch, function()
			local var_17_0, var_17_1, var_17_2 = arg_15_0:GetPaintingTouchVoice()

			arg_15_0.contextData.paintingView:Chat(var_17_0, var_17_1, var_17_2, false)
		end, SFX_PANEL)
	end
end

function var_0_0.UpdateShop(arg_18_0, arg_18_1)
	arg_18_0:SetShop(arg_18_1)
	pg.MsgboxMgr.GetInstance():hide()

	if arg_18_0.contextData.singleWindow:GetLoaded() and arg_18_0.contextData.singleWindow:isShowing() then
		arg_18_0.contextData.singleWindow:ExecuteAction("Close")
	end

	if arg_18_0.contextData.multiWindow:GetLoaded() and arg_18_0.contextData.multiWindow:isShowing() then
		arg_18_0.contextData.multiWindow:ExecuteAction("Close")
	end

	arg_18_0:OnUpdateAll()
end

function var_0_0.UpdateCommodity(arg_19_0, arg_19_1, arg_19_2)
	arg_19_0:SetShop(arg_19_1)

	local var_19_0 = arg_19_1:GetCommodityById(arg_19_2)

	if DROP_TYPE_SHIP == var_19_0:getConfig("commodity_type") then
		arg_19_0:OnUpdateAll()
	else
		arg_19_0:OnUpdateCommodity(var_19_0)
	end

	local var_19_1
	local var_19_2
	local var_19_3

	if arg_19_1:IsPurchaseAll() then
		var_19_1, var_19_2, var_19_3 = arg_19_0:GetPaintingAllPurchaseVoice()
	else
		var_19_1, var_19_2, var_19_3 = arg_19_0:GetPaintingCommodityUpdateVoice()
	end

	arg_19_0.contextData.paintingView:Chat(var_19_1, var_19_2, var_19_3, true)
end

function var_0_0.OnClickCommodity(arg_20_0, arg_20_1, arg_20_2)
	local var_20_0 = Drop.New({
		type = arg_20_1:getConfig("commodity_type"),
		id = arg_20_1:getConfig("commodity_id"),
		count = arg_20_1:getConfig("num")
	})

	if var_20_0.type == DROP_TYPE_VITEM and var_20_0:getConfig("virtual_type") == 22 then
		local var_20_1 = getProxy(ActivityProxy):getActivityById(var_20_0:getConfig("link_id"))

		if not var_20_1 or var_20_1:isEnd() then
			pg.TipsMgr.GetInstance():ShowTips(i18n("tip_build_ticket_exchange_expired", var_20_0:getName()))

			return
		end
	end

	local var_20_2

	if var_20_0.type == DROP_TYPE_EQUIPMENT_SKIN then
		var_20_2 = arg_20_0.contextData.singleWindowForESkin
	elseif arg_20_1:getConfig("num_limit") == 1 or arg_20_1:getConfig("commodity_type") == 4 or isa(arg_20_1, QuotaCommodity) and arg_20_1:GetLimitGoodCount() == 1 then
		var_20_2 = arg_20_0.contextData.singleWindow
	else
		var_20_2 = arg_20_0.contextData.multiWindow
	end

	var_20_2:ExecuteAction("Open", arg_20_1, function(arg_21_0, arg_21_1, arg_21_2)
		local var_21_0 = {}

		if arg_21_0:getConfig("commodity_type") == 4 or arg_20_0.shop.type == ShopArgs.ShopActivity then
			table.insert(var_21_0, function(arg_22_0)
				arg_20_0:TipPurchase(arg_21_0, arg_21_1, arg_21_2, arg_22_0)
			end)
		else
			table.insert(var_21_0, function(arg_23_0)
				if arg_20_0:getSpecialRule(arg_21_0) then
					arg_23_0()
				end
			end)
		end

		table.insert(var_21_0, function(arg_24_0)
			if not arg_21_0:canPurchase() then
				pg.TipsMgr.GetInstance():ShowTips(i18n("buy_countLimit"))

				return
			end

			local var_24_0 = Drop.New({
				type = arg_21_0:getConfig("resource_category"),
				id = arg_21_0:getConfig("resource_type")
			})

			if var_24_0:getOwnedCount() < arg_21_0:getConfig("resource_num") * arg_21_1 then
				if not ItemTipPanel.ShowItemTip(arg_21_0:getConfig("resource_category"), arg_21_0:getConfig("resource_type")) then
					pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_x", var_24_0:getName()))
				end

				return
			end

			arg_24_0()
		end)
		seriesAsync(var_21_0, function()
			arg_20_2(arg_21_0, arg_21_1)
		end)
	end)
end

function var_0_0.TipPurchase(arg_26_0, arg_26_1, arg_26_2, arg_26_3, arg_26_4)
	pg.MsgboxMgr.GetInstance():ShowMsgBox({
		content = i18n("pt_reconfirm", arg_26_3 or "??"),
		onYes = arg_26_4
	})
end

function var_0_0.getSpecialRule(arg_27_0, arg_27_1)
	if arg_27_1:getConfig("commodity_type") == DROP_TYPE_ITEM and arg_27_0.shop.type == ShopArgs.ShopFragment then
		local var_27_0 = arg_27_1:getConfig("commodity_id")
		local var_27_1 = Item.getConfigData(var_27_0)

		if var_27_1 and var_27_1.type == 7 and #var_27_1.shiptrans_id > 0 then
			local var_27_2 = getProxy(BayProxy)

			if getProxy(BagProxy):getItemCountById(var_27_0) > 0 or underscore.any(var_27_1.shiptrans_id, function(arg_28_0)
				return var_27_2:getConfigShipCount(arg_28_0) > 0
			end) then
				pg.TipsMgr.GetInstance():ShowTips(i18n("special_transform_limit_reach"))

				return false
			end
		end
	end

	return true
end

function var_0_0.CanOpen(arg_29_0, arg_29_1, arg_29_2)
	return true
end

function var_0_0.GetPaintingName(arg_30_0)
	return "buzhihuo_shop"
end

function var_0_0.GetPaintingEnterVoice(arg_31_0)
	local var_31_0 = pg.navalacademy_shoppingstreet_template[1].words_enter
	local var_31_1 = string.split(var_31_0, "|")
	local var_31_2 = math.random(#var_31_1)

	return var_31_1[var_31_2], "enter_" .. var_31_2, false
end

function var_0_0.GetPaintingCommodityUpdateVoice(arg_32_0)
	local var_32_0 = pg.navalacademy_shoppingstreet_template[1].words_buy
	local var_32_1 = string.split(var_32_0, "|")
	local var_32_2 = math.random(#var_32_1)

	return var_32_1[var_32_2], "buy_" .. var_32_2, false
end

function var_0_0.GetPaintingAllPurchaseVoice(arg_33_0)
	return nil, nil, nil
end

function var_0_0.GetPaintingTouchVoice(arg_34_0)
	local var_34_0 = pg.navalacademy_shoppingstreet_template[1].words_touch
	local var_34_1 = string.split(var_34_0, "|")
	local var_34_2 = math.random(#var_34_1)

	return var_34_1[var_34_2], "touch_" .. var_34_2, false
end

function var_0_0.GetBg(arg_35_0, arg_35_1)
	return
end

function var_0_0.OnSetUp(arg_36_0)
	return
end

function var_0_0.OnUpdateAll(arg_37_0)
	return
end

function var_0_0.OnUpdateCommodity(arg_38_0, arg_38_1)
	return
end

function var_0_0.OnUpdatePlayer(arg_39_0)
	return
end

function var_0_0.OnUpdateItems(arg_40_0)
	return
end

function var_0_0.OnInitItem(arg_41_0, arg_41_1)
	return
end

function var_0_0.OnUpdateItem(arg_42_0, arg_42_1, arg_42_2)
	return
end

function var_0_0.CanOpenPurchaseWindow(arg_43_0, arg_43_1)
	return arg_43_1:canPurchase()
end

return var_0_0
