local var_0_0 = class("RandomDockYardScene", import("view.base.BaseUI"))

var_0_0.MODE_VIEW = 1
var_0_0.MODE_ADD = 2
var_0_0.MODE_REMOVE = 3

function var_0_0.getUIName(arg_1_0)
	return "RandomDockYardUI"
end

function var_0_0.OnChangeRandomShips(arg_2_0)
	arg_2_0.randomFlagShips = nil
	arg_2_0.dockyardShips = nil

	if arg_2_0.mode ~= var_0_0.MODE_VIEW then
		arg_2_0:Switch(var_0_0.MODE_VIEW)
	end
end

function var_0_0.init(arg_3_0)
	arg_3_0.titleImg = arg_3_0:findTF("blur_panel/adapt/top/title"):GetComponent(typeof(Image))
	arg_3_0.titleEnImg = arg_3_0:findTF("blur_panel/adapt/top/title/title_en"):GetComponent(typeof(Image))
	arg_3_0.scrollrect = arg_3_0:findTF("main/ship_container/ships"):GetComponent("LScrollRect")
	arg_3_0.emptyTr = arg_3_0:findTF("empty")
	arg_3_0.backBtn = arg_3_0:findTF("blur_panel/adapt/top/back")
	arg_3_0.addBtn = arg_3_0:findTF("blur_panel/select_panel/add_button")
	arg_3_0.removeBtn = arg_3_0:findTF("blur_panel/select_panel/remove_button")
	arg_3_0.cancelBtn = arg_3_0:findTF("blur_panel/select_panel/cancel_button")
	arg_3_0.confirmBtn = arg_3_0:findTF("blur_panel/select_panel/confirm_button")
	arg_3_0.confirmBtnMask = arg_3_0.confirmBtn:Find("mask")
	arg_3_0.allBtn = arg_3_0:findTF("blur_panel/select_panel/all_button")
	arg_3_0.tipTxt = arg_3_0:findTF("blur_panel/select_panel/tip"):GetComponent(typeof(Text))
	arg_3_0.selectedTxt = arg_3_0:findTF("blur_panel/select_panel/bottom_info/bg_input/selected"):GetComponent(typeof(Text))
	arg_3_0.frequentlyUseToggle = arg_3_0:findTF("blur_panel/adapt/top/preference_toggle")
	arg_3_0.lockToggle = arg_3_0:findTF("blur_panel/adapt/top/lock_toggle")
	arg_3_0.sortBtn = arg_3_0:findTF("blur_panel/adapt/top/sort_button")
	arg_3_0.sortTxt = arg_3_0.sortBtn:Find("Image"):GetComponent(typeof(Text))
	arg_3_0.sortUp = arg_3_0.sortBtn:Find("asc")
	arg_3_0.sortDown = arg_3_0.sortBtn:Find("desc")
	arg_3_0.indexBtn = arg_3_0:findTF("blur_panel/adapt/top/index_button")
	arg_3_0.indexBtnSel = arg_3_0.indexBtn:Find("Image")
	arg_3_0.selectedCntTxt = arg_3_0:findTF("blur_panel/select_panel/bottom_info/bg_input/count"):GetComponent(typeof(Text))
	arg_3_0.selectPanelFrame = arg_3_0:findTF("blur_panel/select_panel/bottom_info/bg_input")

	setActive(arg_3_0.sortUp, false)
	setActive(arg_3_0.sortDown, true)
	setText(arg_3_0.emptyTr:Find("Text"), i18n("random_ship_custom_mode_main_empty"))
	setText(arg_3_0.addBtn:Find("Text"), i18n("random_ship_custom_mode_main_button_add"))
	setText(arg_3_0.removeBtn:Find("Text"), i18n("random_ship_custom_mode_main_button_remove"))
	setText(arg_3_0.cancelBtn:Find("Text"), i18n("text_cancel"))
	setText(arg_3_0.confirmBtn:Find("Text"), i18n("text_confirm"))
	setText(arg_3_0.allBtn:Find("Text"), i18n("random_ship_custom_mode_select_all"))

	arg_3_0.msgbox = RandomDockYardMsgBoxPgae.New(arg_3_0._tf, arg_3_0.event)

	arg_3_0:InitDefault()
end

function var_0_0.InitDefault(arg_4_0)
	arg_4_0.selected = {}
	arg_4_0.titles = {
		[var_0_0.MODE_VIEW] = GetSpriteFromAtlas("ui/dockyardui_atlas", "title_random_ship"),
		[var_0_0.MODE_ADD] = GetSpriteFromAtlas("ui/dockyardui_atlas", "title_add_random_ship"),
		[var_0_0.MODE_REMOVE] = GetSpriteFromAtlas("ui/dockyardui_atlas", "title_remove_random_ship")
	}
	arg_4_0.titleEns = {
		[var_0_0.MODE_VIEW] = GetSpriteFromAtlas("ui/dockyardui_atlas", "title_rd_en"),
		[var_0_0.MODE_ADD] = GetSpriteFromAtlas("ui/dockyardui_atlas", "title_add_en"),
		[var_0_0.MODE_REMOVE] = GetSpriteFromAtlas("ui/dockyardui_atlas", "title_remove_en")
	}
	arg_4_0.msgBoxTitle = {
		[var_0_0.MODE_VIEW] = {
			cn = "",
			en = ""
		},
		[var_0_0.MODE_ADD] = {
			en = "ADD",
			cn = i18n("random_ship_custom_mode_add_title")
		},
		[var_0_0.MODE_REMOVE] = {
			en = "REMOVE",
			cn = i18n("random_ship_custom_mode_remove_title")
		}
	}
	arg_4_0.msgBoxSubTitle = {
		[var_0_0.MODE_VIEW] = "",
		[var_0_0.MODE_ADD] = i18n("random_ship_custom_mode_add_tip2"),
		[var_0_0.MODE_REMOVE] = i18n("random_ship_custom_mode_remove_tip2")
	}
	arg_4_0.tips = {
		[var_0_0.MODE_VIEW] = i18n("random_ship_custom_mode_main_tip1"),
		[var_0_0.MODE_ADD] = i18n("random_ship_custom_mode_add_tip1"),
		[var_0_0.MODE_REMOVE] = i18n("random_ship_custom_mode_remove_tip1")
	}
	arg_4_0.selectedTxts = {
		[var_0_0.MODE_VIEW] = i18n("random_ship_custom_mode_main_tip2"),
		[var_0_0.MODE_ADD] = i18n("random_ship_custom_mode_select_number"),
		[var_0_0.MODE_REMOVE] = i18n("random_ship_custom_mode_select_number")
	}
	arg_4_0.frequentlyUseFlags = {
		[var_0_0.MODE_VIEW] = false,
		[var_0_0.MODE_ADD] = false,
		[var_0_0.MODE_REMOVE] = false
	}
	arg_4_0.lockFlags = {
		[var_0_0.MODE_VIEW] = false,
		[var_0_0.MODE_ADD] = false,
		[var_0_0.MODE_REMOVE] = false
	}
	arg_4_0.sortFlags = {
		[var_0_0.MODE_VIEW] = false,
		[var_0_0.MODE_ADD] = false,
		[var_0_0.MODE_REMOVE] = false
	}
	arg_4_0.indexDatas = {
		[var_0_0.MODE_VIEW] = {
			sortIndex = ShipIndexConst.SortLevel,
			typeIndex = ShipIndexConst.TypeAll,
			campIndex = ShipIndexConst.CampAll,
			rarityIndex = ShipIndexConst.RarityAll,
			extraIndex = ShipIndexConst.ExtraALL
		},
		[var_0_0.MODE_ADD] = {
			sortIndex = ShipIndexConst.SortLevel,
			typeIndex = ShipIndexConst.TypeAll,
			campIndex = ShipIndexConst.CampAll,
			rarityIndex = ShipIndexConst.RarityAll,
			extraIndex = ShipIndexConst.ExtraALL
		},
		[var_0_0.MODE_REMOVE] = {
			sortIndex = ShipIndexConst.SortLevel,
			typeIndex = ShipIndexConst.TypeAll,
			campIndex = ShipIndexConst.CampAll,
			rarityIndex = ShipIndexConst.RarityAll,
			extraIndex = ShipIndexConst.ExtraALL
		}
	}
end

function var_0_0.didEnter(arg_5_0)
	arg_5_0.cards = {}

	function arg_5_0.scrollrect.onInitItem(arg_6_0)
		arg_5_0:OnItemUpdate(arg_6_0)
	end

	function arg_5_0.scrollrect.onUpdateItem(arg_7_0, arg_7_1)
		arg_5_0:OnUpdateItem(arg_7_0, arg_7_1)
	end

	onButton(arg_5_0, arg_5_0.backBtn, function()
		if arg_5_0.mode ~= var_0_0.MODE_VIEW then
			arg_5_0:Switch(var_0_0.MODE_VIEW)

			return
		end

		arg_5_0:emit(var_0_0.ON_RETURN, {
			page = NewSettingsScene.PAGE_OPTION,
			scroll = SettingsRandomFlagShipAndSkinPanel
		})
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.addBtn, function()
		arg_5_0:Switch(var_0_0.MODE_ADD)
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.removeBtn, function()
		arg_5_0:Switch(var_0_0.MODE_REMOVE)
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.cancelBtn, function()
		if arg_5_0.mode == var_0_0.MODE_VIEW then
			return
		end

		arg_5_0:Switch(var_0_0.MODE_VIEW)
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.confirmBtn, function()
		if arg_5_0.mode == var_0_0.MODE_VIEW then
			return
		end

		arg_5_0:OnConfirm()
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.allBtn, function()
		if arg_5_0.mode == var_0_0.MODE_VIEW then
			return
		end

		arg_5_0:OnAll()
	end, SFX_PANEL)
	onToggle(arg_5_0, arg_5_0.frequentlyUseToggle, function(arg_14_0)
		arg_5_0.frequentlyUseFlags[arg_5_0.mode] = arg_14_0

		local var_14_0 = arg_5_0:GetShipList(arg_5_0.mode)

		arg_5_0:FlushShipList(var_14_0)
	end, SFX_PANEL)
	onToggle(arg_5_0, arg_5_0.lockToggle, function(arg_15_0)
		arg_5_0.lockFlags[arg_5_0.mode] = arg_15_0

		local var_15_0 = arg_5_0:GetShipList(arg_5_0.mode)

		arg_5_0:FlushShipList(var_15_0)
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.sortBtn, function()
		arg_5_0.sortFlags[arg_5_0.mode] = not arg_5_0.sortFlags[arg_5_0.mode]

		setActive(arg_5_0.sortUp, arg_5_0.sortFlags[arg_5_0.mode])
		setActive(arg_5_0.sortDown, not arg_5_0.sortFlags[arg_5_0.mode])

		local var_16_0 = arg_5_0:GetShipList(arg_5_0.mode)

		arg_5_0:FlushShipList(var_16_0)
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.indexBtn, function()
		arg_5_0:emit(RandomDockYardMediator.OPEN_INDEX, {
			OnFilter = function(arg_18_0)
				arg_5_0:OnFilter(arg_18_0)
			end,
			defaultIndex = arg_5_0.indexDatas[arg_5_0.mode]
		})
	end, SFX_PANEL)
	arg_5_0:Switch(var_0_0.MODE_VIEW)
end

function var_0_0.GetRandomFlagShips(arg_19_0)
	if not arg_19_0.randomFlagShips then
		local var_19_0 = getProxy(PlayerProxy):getRawData()

		arg_19_0.randomFlagShips = {}

		local var_19_1 = getProxy(BayProxy)

		for iter_19_0, iter_19_1 in ipairs(var_19_0:GetCustomRandomShipList()) do
			local var_19_2 = var_19_1:RawGetShipById(iter_19_1)

			if var_19_2 then
				table.insert(arg_19_0.randomFlagShips, var_19_2)
			end
		end
	end

	return arg_19_0.randomFlagShips
end

function var_0_0.GetDockYardShipAndNotInRandom(arg_20_0)
	if not arg_20_0.dockyardShips then
		local var_20_0 = arg_20_0:GetRandomFlagShips()
		local var_20_1 = {}

		for iter_20_0, iter_20_1 in ipairs(var_20_0) do
			var_20_1[iter_20_1.id] = true
		end

		arg_20_0.dockyardShips = {}

		local var_20_2 = getProxy(BayProxy):getRawData()

		for iter_20_2, iter_20_3 in pairs(var_20_2) do
			if not var_20_1[iter_20_3.id] and not iter_20_3:isActivityNpc() then
				table.insert(arg_20_0.dockyardShips, iter_20_3)
			end
		end
	end

	return arg_20_0.dockyardShips
end

function var_0_0.GetShipList(arg_21_0, arg_21_1)
	local var_21_0 = {}

	if arg_21_1 == var_0_0.MODE_VIEW then
		var_21_0 = arg_21_0:GetRandomFlagShips()
	elseif arg_21_1 == var_0_0.MODE_ADD then
		var_21_0 = arg_21_0:GetDockYardShipAndNotInRandom()
	elseif arg_21_1 == var_0_0.MODE_REMOVE then
		var_21_0 = arg_21_0:GetRandomFlagShips()
	end

	return var_21_0
end

function var_0_0.Switch(arg_22_0, arg_22_1)
	arg_22_0:Clear()

	arg_22_0.selected = {}

	local var_22_0 = arg_22_0:GetShipList(arg_22_1)

	arg_22_0:UpdateModeStyle(arg_22_1, #var_22_0)

	arg_22_0.mode = arg_22_1

	arg_22_0:FlushShipList(var_22_0)

	if arg_22_0.mode == var_0_0.MODE_VIEW then
		arg_22_0:UpdateSelectedCnt(var_22_0)
	else
		arg_22_0:UpdateSelectedCnt(arg_22_0.selected)
	end
end

function var_0_0.UpdateModeStyle(arg_23_0, arg_23_1, arg_23_2)
	arg_23_0.titleImg.sprite = arg_23_0.titles[arg_23_1]

	arg_23_0.titleImg:SetNativeSize()

	arg_23_0.titleEnImg.sprite = arg_23_0.titleEns[arg_23_1]

	arg_23_0.titleEnImg:SetNativeSize()
	setActive(arg_23_0.addBtn, arg_23_1 == var_0_0.MODE_VIEW)
	setActive(arg_23_0.removeBtn, arg_23_1 == var_0_0.MODE_VIEW)
	setActive(arg_23_0.cancelBtn, arg_23_1 == var_0_0.MODE_ADD or arg_23_1 == var_0_0.MODE_REMOVE)
	setActive(arg_23_0.confirmBtn, arg_23_1 == var_0_0.MODE_ADD or arg_23_1 == var_0_0.MODE_REMOVE)
	setActive(arg_23_0.allBtn, arg_23_1 == var_0_0.MODE_ADD or arg_23_1 == var_0_0.MODE_REMOVE)

	arg_23_0.tipTxt.text = arg_23_0.tips[arg_23_1]
	arg_23_0.selectedTxt.text = arg_23_0.selectedTxts[arg_23_1]

	setButtonEnabled(arg_23_0.removeBtn, arg_23_1 == var_0_0.MODE_VIEW and arg_23_2 > 0)
	setAnchoredPosition(arg_23_0.selectPanelFrame, {
		x = arg_23_1 == var_0_0.MODE_VIEW and 0 or 180
	})
end

function var_0_0.OnConfirm(arg_24_0)
	local var_24_0 = {}

	for iter_24_0, iter_24_1 in pairs(arg_24_0.selected) do
		table.insert(var_24_0, iter_24_0)
	end

	local function var_24_1()
		if arg_24_0.mode == var_0_0.MODE_ADD then
			arg_24_0:emit(RandomDockYardMediator.ON_ADD_SHIPS, var_24_0)
		elseif arg_24_0.mode == var_0_0.MODE_REMOVE then
			arg_24_0:emit(RandomDockYardMediator.ON_REMOVE_SHIPS, var_24_0)
		end
	end

	local var_24_2 = arg_24_0.msgBoxTitle[arg_24_0.mode]
	local var_24_3 = arg_24_0.msgBoxSubTitle[arg_24_0.mode]

	arg_24_0.msgbox:ExecuteAction("Flush", var_24_2, var_24_3, var_24_0, var_24_1)
end

function var_0_0.OnAll(arg_26_0)
	for iter_26_0, iter_26_1 in ipairs(arg_26_0.displays) do
		arg_26_0.selected[iter_26_1.id] = true
	end

	arg_26_0.scrollrect:SetTotalCount(#arg_26_0.displays)
	arg_26_0:UpdateSelectedCnt(arg_26_0.selected)
end

function var_0_0.UpdateSelectedCnt(arg_27_0, arg_27_1)
	local var_27_0 = 0

	for iter_27_0, iter_27_1 in pairs(arg_27_1) do
		var_27_0 = var_27_0 + 1
	end

	arg_27_0.selectedCntTxt.text = var_27_0

	setButtonEnabled(arg_27_0.confirmBtn, var_27_0 > 0)
	setActive(arg_27_0.confirmBtnMask, var_27_0 <= 0)
end

local function var_0_1(arg_28_0)
	return arg_28_0.sortIndex ~= ShipIndexConst.SortLevel or arg_28_0.typeIndex ~= ShipIndexConst.TypeAll or arg_28_0.campIndex ~= ShipIndexConst.CampAll or arg_28_0.rarityIndex ~= ShipIndexConst.RarityAll or arg_28_0.extraIndex ~= ShipIndexConst.ExtraALL
end

function var_0_0.OnFilter(arg_29_0, arg_29_1)
	local var_29_0 = arg_29_0.indexDatas[arg_29_0.mode]

	var_29_0.sortIndex = arg_29_1.sortIndex
	var_29_0.typeIndex = arg_29_1.typeIndex
	var_29_0.campIndex = arg_29_1.campIndex
	var_29_0.rarityIndex = arg_29_1.rarityIndex
	var_29_0.extraIndex = arg_29_1.extraIndex

	setActive(arg_29_0.indexBtnSel, var_0_1(var_29_0))

	local var_29_1 = arg_29_0:GetShipList(arg_29_0.mode)

	arg_29_0:FlushShipList(var_29_1)
end

function var_0_0.OnItemUpdate(arg_30_0, arg_30_1)
	local var_30_0 = RandomDockYardCard.New(arg_30_1)

	onButton(arg_30_0, var_30_0._go, function()
		if arg_30_0.mode == var_0_0.MODE_VIEW then
			return
		end

		if arg_30_0.selected[var_30_0.ship.id] then
			arg_30_0.selected[var_30_0.ship.id] = nil
		else
			arg_30_0.selected[var_30_0.ship.id] = true
		end

		arg_30_0:UpdateSelectedCnt(arg_30_0.selected)
		var_30_0:UpdateSelected(arg_30_0.selected[var_30_0.ship.id])
	end, SFX_PANEL)

	arg_30_0.cards[arg_30_1] = var_30_0
end

function var_0_0.OnUpdateItem(arg_32_0, arg_32_1, arg_32_2)
	local var_32_0 = arg_32_0.cards[arg_32_2]

	if not var_32_0 then
		arg_32_0:OnItemUpdate(arg_32_2)

		var_32_0 = arg_32_0.cards[arg_32_2]
	end

	local var_32_1 = arg_32_0.displays[arg_32_1 + 1]
	local var_32_2 = arg_32_0.selected[var_32_1.id]

	var_32_0:Update(var_32_1, var_32_2)
end

function var_0_0.FlushShipList(arg_33_0, arg_33_1)
	arg_33_0.displays = {}

	arg_33_0:FilterShips(arg_33_1, arg_33_0.displays)
	arg_33_0:SortShips(arg_33_0.displays)

	local var_33_0 = #arg_33_0.displays

	arg_33_0.scrollrect:SetTotalCount(var_33_0)
	setActive(arg_33_0.emptyTr, var_33_0 <= 0)
end

function var_0_0.FilterShips(arg_34_0, arg_34_1, arg_34_2)
	local var_34_0 = arg_34_0.lockFlags[arg_34_0.mode]
	local var_34_1 = arg_34_0.frequentlyUseFlags[arg_34_0.mode]
	local var_34_2 = arg_34_0.indexDatas[arg_34_0.mode]

	local function var_34_3(arg_35_0)
		local var_35_0 = not var_34_0 or not not arg_35_0:IsLocked()
		local var_35_1 = not var_34_1 or not not arg_35_0:IsPreferenceTag()
		local var_35_2 = ShipIndexConst.filterByType(arg_35_0, var_34_2.typeIndex)
		local var_35_3 = ShipIndexConst.filterByCamp(arg_35_0, var_34_2.campIndex)
		local var_35_4 = ShipIndexConst.filterByRarity(arg_35_0, var_34_2.rarityIndex)
		local var_35_5 = ShipIndexConst.filterByExtra(arg_35_0, var_34_2.extraIndex)

		return var_35_0 and var_35_1 and var_35_2 and var_35_3 and var_35_4 and var_35_5
	end

	for iter_34_0, iter_34_1 in ipairs(arg_34_1) do
		if var_34_3(iter_34_1) then
			table.insert(arg_34_2, iter_34_1)
		end
	end
end

function var_0_0.SortShips(arg_36_0, arg_36_1)
	local var_36_0 = arg_36_0.indexDatas[arg_36_0.mode]
	local var_36_1 = arg_36_0.sortFlags[arg_36_0.mode]
	local var_36_2 = var_36_0.sortIndex
	local var_36_3, var_36_4 = ShipIndexConst.getSortFuncAndName(var_36_2, var_36_1)

	table.insert(var_36_3, 1, function(arg_37_0)
		return -arg_37_0.activityNpc
	end)
	table.sort(arg_36_1, CompareFuncs(var_36_3))

	arg_36_0.sortTxt.text = i18n(var_36_4)
end

function var_0_0.onBackPressed(arg_38_0)
	var_0_0.super.onBackPressed(arg_38_0)
end

function var_0_0.Clear(arg_39_0)
	for iter_39_0, iter_39_1 in pairs(arg_39_0.cards) do
		iter_39_1:Dispose()
	end

	arg_39_0.cards = {}
end

function var_0_0.willExit(arg_40_0)
	arg_40_0.titles = nil

	if arg_40_0.msgbox then
		arg_40_0.msgbox:Destroy()
	end

	arg_40_0.msgbox = nil
end

return var_0_0
