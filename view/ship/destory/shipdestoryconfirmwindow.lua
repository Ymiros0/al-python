local var_0_0 = class("ShipDestoryConfirmWindow", import("...base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "DestoryConfirmWindow"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.closeBtn = arg_2_0:findTF("window/top/btnBack")

	setActive(arg_2_0:findTF("window/top/bg/infomation/title_en"), PLATFORM_CODE ~= PLATFORM_US)
	setText(arg_2_0:findTF("window/top/bg/infomation/title"), i18n("title_info"))

	arg_2_0.cancelBtn = arg_2_0:findTF("window/cancel_btn")
	arg_2_0.confirmBtn = arg_2_0:findTF("window/confirm_btn")

	setText(findTF(arg_2_0.confirmBtn, "pic"), i18n("destroy_confirm_access"))
	setText(findTF(arg_2_0.cancelBtn, "pic"), i18n("destroy_confirm_cancel"))

	arg_2_0.title = arg_2_0:findTF("window/content/Text")
	arg_2_0.label = arg_2_0:findTF("window/content/desc/label")

	setText(arg_2_0.label, i18n("destory_ship_before_tip"))

	arg_2_0.urLabel = arg_2_0:findTF("window/content/desc/label1")
	arg_2_0.urInput = arg_2_0:findTF("window/content/desc/InputField")
	arg_2_0.urOverflowLabel = arg_2_0:findTF("window/content/desc/label2")

	setText(arg_2_0.urOverflowLabel, i18n("destory_ur_pt_overflowa"))

	local var_2_0 = arg_2_0:findTF("Placeholder", arg_2_0.urInput)

	setText(var_2_0, i18n("box_ship_del_click"))
end

function var_0_0.OnInit(arg_3_0)
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		arg_3_0:Confirm()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf:Find("bg"), function()
		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0:Hide()
	end, SFX_PANEL)
end

function var_0_0.SetCallBack(arg_8_0, arg_8_1)
	arg_8_0.callback = arg_8_1
end

function var_0_0.Confirm(arg_9_0)
	if arg_9_0.key then
		local var_9_0 = getInputText(arg_9_0.urInput)

		if arg_9_0.key ~= tonumber(var_9_0) then
			pg.TipsMgr:GetInstance():ShowTips(i18n("destory_ship_input_erro"))

			return
		end

		local var_9_1 = arg_9_0.callback

		arg_9_0:Hide()
		existCall(var_9_1)
	else
		local var_9_2 = arg_9_0.callback

		arg_9_0:Hide()
		existCall(var_9_2)
	end
end

function var_0_0.Show(arg_10_0, arg_10_1, arg_10_2, arg_10_3, arg_10_4)
	var_0_0.super.Show(arg_10_0)
	pg.UIMgr.GetInstance():BlurPanel(arg_10_0._tf)

	arg_10_0.key = nil
	arg_10_0.eliteShips = arg_10_1
	arg_10_0.highLevelShips = arg_10_2
	arg_10_0.overflow = arg_10_3

	arg_10_0:SetCallBack(arg_10_4)
	arg_10_0:Updatelayout()
	arg_10_0:UpdateShips()
end

function var_0_0.ShowEliteTag(arg_11_0, arg_11_1, arg_11_2)
	var_0_0.super.Show(arg_11_0)
	pg.UIMgr.GetInstance():BlurPanel(arg_11_0._tf)
	arg_11_0:SetCallBack(arg_11_2)
	setText(arg_11_0.title, i18n("destroy_eliteship_tip", i18n("destroy_inHardFormation_tip")))
	setActive(arg_11_0.urOverflowLabel, false)
	setActive(arg_11_0.urLabel, false)
	setActive(arg_11_0.urInput, false)

	arg_11_0.ships = arg_11_1

	if #arg_11_0.ships > 5 then
		setActive(arg_11_0._tf:Find("window/content/ships"), true)
		setActive(arg_11_0._tf:Find("window/content/ships_single"), false)

		local var_11_0 = arg_11_0._tf:Find("window/content/ships/content"):GetComponent("LScrollRect")

		function var_11_0.onUpdateItem(arg_12_0, arg_12_1)
			updateShip(tf(arg_12_1), arg_11_0.ships[arg_12_0 + 1])
		end

		onNextTick(function()
			var_11_0:SetTotalCount(#arg_11_0.ships)
		end)
	else
		setActive(arg_11_0._tf:Find("window/content/ships"), false)
		setActive(arg_11_0._tf:Find("window/content/ships_single"), true)

		local var_11_1 = arg_11_0._tf:Find("window/content/ships_single")
		local var_11_2 = UIItemList.New(var_11_1, var_11_1:Find("IconTpl"))

		var_11_2:make(function(arg_14_0, arg_14_1, arg_14_2)
			if arg_14_0 == UIItemList.EventUpdate then
				updateShip(arg_14_2, arg_11_0.ships[arg_14_1 + 1])
			end
		end)
		var_11_2:align(#arg_11_0.ships)
	end
end

function var_0_0.Updatelayout(arg_15_0)
	local var_15_0 = arg_15_0.eliteShips
	local var_15_1 = arg_15_0.highLevelShips
	local var_15_2 = {}

	if #var_15_0 > 0 then
		table.insert(var_15_2, i18n("destroy_high_rarity_tip"))
	end

	if #var_15_1 > 0 then
		table.insert(var_15_2, i18n("destroy_high_level_tip", ""))
	end

	setText(arg_15_0.title, i18n("destroy_eliteship_tip", table.concat(var_15_2, "、")))

	local var_15_3 = _.any(var_15_0, function(arg_16_0)
		return arg_16_0:getConfig("rarity") >= ShipRarity.SSR
	end)

	if var_15_3 and not arg_15_0.key then
		arg_15_0.key = math.random(100000, 999999)

		setText(arg_15_0.urLabel, i18n("destroy_ur_rarity_tip", arg_15_0.key))
	else
		setText(arg_15_0.urLabel, "")
	end

	local var_15_4 = var_15_3 and arg_15_0.overflow

	setActive(arg_15_0.urOverflowLabel, var_15_4)
	setActive(arg_15_0.urLabel, var_15_3)
	setActive(arg_15_0.urInput, var_15_3)
end

function var_0_0.UpdateShips(arg_17_0)
	local var_17_0 = arg_17_0.eliteShips
	local var_17_1 = arg_17_0.highLevelShips
	local var_17_2 = table.mergeArray(var_17_1, var_17_0)

	mergeSort(var_17_2, CompareFuncs({
		function(arg_18_0)
			return -arg_18_0.level
		end,
		function(arg_19_0)
			return -arg_19_0:getRarity()
		end
	}, true))

	arg_17_0.ships = var_17_2

	if #arg_17_0.ships > 5 then
		setActive(arg_17_0._tf:Find("window/content/ships"), true)
		setActive(arg_17_0._tf:Find("window/content/ships_single"), false)

		local var_17_3 = arg_17_0._tf:Find("window/content/ships/content"):GetComponent("LScrollRect")

		function var_17_3.onUpdateItem(arg_20_0, arg_20_1)
			updateShip(tf(arg_20_1), arg_17_0.ships[arg_20_0 + 1])
		end

		onNextTick(function()
			var_17_3:SetTotalCount(#arg_17_0.ships)
		end)
	else
		setActive(arg_17_0._tf:Find("window/content/ships"), false)
		setActive(arg_17_0._tf:Find("window/content/ships_single"), true)

		local var_17_4 = arg_17_0._tf:Find("window/content/ships_single")
		local var_17_5 = UIItemList.New(var_17_4, var_17_4:Find("IconTpl"))

		var_17_5:make(function(arg_22_0, arg_22_1, arg_22_2)
			if arg_22_0 == UIItemList.EventUpdate then
				updateShip(arg_22_2, arg_17_0.ships[arg_22_1 + 1])
			end
		end)
		var_17_5:align(#arg_17_0.ships)
	end
end

function var_0_0.Hide(arg_23_0)
	var_0_0.super.Hide(arg_23_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_23_0._tf, arg_23_0._parentTf)

	arg_23_0.key = nil
	arg_23_0.callback = nil

	setInputText(arg_23_0.urInput, "")
end

function var_0_0.OnDestroy(arg_24_0)
	if arg_24_0:isShowing() then
		arg_24_0:Hide()
	end
end

return var_0_0
