local var_0_0 = class("PlayerVitaeShipsPage", import("...base.BaseSubView"))
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = 1
local var_0_5 = 2

var_0_0.RANDOM_FLAG_SHIP_PAGE = var_0_5
var_0_0.EDUCATE_CHAR_SLOT_ID = 6
var_0_0.ON_BEGIN_DRAG_CARD = "PlayerVitaeShipsPage:ON_BEGIN_DRAG_CARD"
var_0_0.ON_DRAGING_CARD = "PlayerVitaeShipsPage:ON_DRAGING_CARD"
var_0_0.ON_DRAG_END_CARD = "PlayerVitaeShipsPage:ON_DRAG_END_CARD"

function var_0_0.GetSlotIndexList()
	local var_1_0, var_1_1 = var_0_0.GetSlotMaxCnt()
	local var_1_2 = {}

	for iter_1_0 = 1, var_1_1 do
		table.insert(var_1_2, iter_1_0)
	end

	if var_0_0.GetEducateCharSlotMaxCnt() > 0 then
		table.insert(var_1_2, var_0_0.EDUCATE_CHAR_SLOT_ID)
	end

	return var_1_2
end

function var_0_0.GetAllUnlockSlotCnt()
	local var_2_0, var_2_1 = var_0_0.GetSlotMaxCnt()

	return var_2_1 + var_0_0.GetEducateCharSlotMaxCnt()
end

function var_0_0.GetEducateCharSlotMaxCnt()
	if LOCK_EDUCATE_SYSTEM then
		return 0
	end

	if getProxy(PlayerProxy):getRawData():ExistEducateChar() or getProxy(EducateProxy):IsUnlockSecretary() then
		return 1
	else
		return 0
	end
end

function var_0_0.GetSlotMaxCnt()
	local var_4_0 = pg.gameset.secretary_group_unlock.description
	local var_4_1 = var_4_0[#var_4_0][2]
	local var_4_2 = 1

	for iter_4_0, iter_4_1 in ipairs(var_4_0) do
		if getProxy(ChapterProxy):isClear(iter_4_1[1]) then
			var_4_2 = iter_4_1[2]
		end
	end

	return var_4_1, var_4_2
end

function var_0_0.getUIName(arg_5_0)
	return "PlayerVitaeShipsPage"
end

function var_0_0.UpdateCard(arg_6_0, arg_6_1)
	local var_6_0 = arg_6_0.cards[var_0_1]

	for iter_6_0, iter_6_1 in ipairs(var_6_0) do
		if isActive(iter_6_1._tf) and iter_6_1.displayShip and iter_6_1.displayShip.id == arg_6_1 then
			iter_6_1:Refresh()

			break
		end
	end
end

function var_0_0.UpdateCardPaintingTag(arg_7_0)
	local var_7_0 = arg_7_0.cards[var_0_1]

	for iter_7_0, iter_7_1 in ipairs(var_7_0) do
		iter_7_1:updatePaintingTag()
	end
end

function var_0_0.RefreshShips(arg_8_0)
	arg_8_0:Update()
end

function var_0_0.OnLoaded(arg_9_0)
	arg_9_0.cardContainer = arg_9_0:findTF("frame")
	arg_9_0.shipTpl = arg_9_0:findTF("frame/shipCard")
	arg_9_0.emptyTpl = arg_9_0:findTF("frame/addCard")
	arg_9_0.lockTpl = arg_9_0:findTF("frame/lockCard")
	arg_9_0.helpBtn = arg_9_0:findTF("help_btn")
	arg_9_0.settingBtn = arg_9_0:findTF("setting_btn")
	arg_9_0.settingBtnSlider = arg_9_0:findTF("toggle/on", arg_9_0.settingBtn)
	arg_9_0.randomBtn = arg_9_0:findTF("ran_setting_btn")
	arg_9_0.randomBtnSlider = arg_9_0:findTF("toggle/on", arg_9_0.randomBtn)
	arg_9_0.settingSeceneBtn = arg_9_0:findTF("setting_scene_btn")
	arg_9_0.nativeBtn = arg_9_0:findTF("native_setting_btn")
	arg_9_0.nativeBtnOn = arg_9_0.nativeBtn:Find("on")
	arg_9_0.nativeBtnOff = arg_9_0.nativeBtn:Find("off")
	arg_9_0.educateCharTr = arg_9_0:findTF("educate_char")
	arg_9_0.educateCharSettingList = UIItemList.New(arg_9_0:findTF("educate_char/shipCard/settings/panel"), arg_9_0:findTF("educate_char/shipCard/settings/panel/tpl"))
	arg_9_0.educateCharSettingBtn = arg_9_0:findTF("educate_char/shipCard/settings/tpl")
	arg_9_0.educateCharTrTip = arg_9_0.educateCharTr:Find("tip")

	if LOCK_EDUCATE_SYSTEM then
		setActive(arg_9_0.educateCharTr, false)
		setAnchoredPosition(arg_9_0.cardContainer, {
			x = 0
		})
		setAnchoredPosition(arg_9_0:findTF("flagship"), {
			x = -720
		})
		setAnchoredPosition(arg_9_0:findTF("zs"), {
			x = 763
		})
		setAnchoredPosition(arg_9_0:findTF("line"), {
			x = 740
		})
	end

	arg_9_0.educateCharCards = {
		[var_0_1] = PlayerVitaeEducateShipCard.New(arg_9_0:findTF("educate_char/shipCard"), arg_9_0.event),
		[var_0_2] = PlayerVitaeEducateAddCard.New(arg_9_0:findTF("educate_char/addCard"), arg_9_0.event),
		[var_0_3] = PlayerVitaeEducateLockCard.New(arg_9_0:findTF("educate_char/lockCard"), arg_9_0.event)
	}
	arg_9_0.tip = arg_9_0:findTF("tip"):GetComponent(typeof(Text))
	arg_9_0.flagShipMark = arg_9_0:findTF("flagship")

	arg_9_0:bind(var_0_0.ON_BEGIN_DRAG_CARD, function(arg_10_0, arg_10_1)
		arg_9_0:OnBeginDragCard(arg_10_1)
	end)
	arg_9_0:bind(var_0_0.ON_DRAGING_CARD, function(arg_11_0, arg_11_1)
		arg_9_0:OnDragingCard(arg_11_1)
	end)
	arg_9_0:bind(var_0_0.ON_DRAG_END_CARD, function(arg_12_0)
		arg_9_0:OnEndDragCard()
	end)
	setText(arg_9_0.nativeBtnOn:Find("Text"), i18n("random_ship_before"))
	setText(arg_9_0.nativeBtnOff:Find("Text"), i18n("random_ship_now"))
	setText(arg_9_0.settingBtn:Find("Text"), i18n("player_vitae_skin_setting"))
	setText(arg_9_0.randomBtn:Find("Text"), i18n("random_ship_label"))
	setText(arg_9_0.settingSeceneBtn:Find("Text"), i18n("playervtae_setting_btn_label"))

	arg_9_0.cardContainerCG = GetOrAddComponent(arg_9_0.cardContainer, typeof(CanvasGroup))
end

function var_0_0.OnBeginDragCard(arg_13_0, arg_13_1)
	arg_13_0.dragIndex = arg_13_1
	arg_13_0.displayCards = {}
	arg_13_0.displayPos = {}

	local var_13_0 = arg_13_0.cards[var_0_1]

	for iter_13_0, iter_13_1 in ipairs(var_13_0) do
		if isActive(iter_13_1._tf) then
			arg_13_0.displayCards[iter_13_0] = iter_13_1
			arg_13_0.displayPos[iter_13_0] = iter_13_1._tf.localPosition
		end
	end

	for iter_13_2, iter_13_3 in pairs(arg_13_0.displayCards) do
		if iter_13_2 ~= arg_13_1 then
			iter_13_3:DisableDrag()
		end
	end
end

function var_0_0.OnDragingCard(arg_14_0, arg_14_1)
	local var_14_0 = arg_14_0.displayCards[arg_14_0.dragIndex - 1]
	local var_14_1 = arg_14_0.displayCards[arg_14_0.dragIndex + 1]

	if var_14_0 and arg_14_0:ShouldSwap(arg_14_1, arg_14_0.dragIndex - 1) then
		arg_14_0:Swap(arg_14_0.dragIndex, arg_14_0.dragIndex - 1)
	elseif var_14_1 and arg_14_0:ShouldSwap(arg_14_1, arg_14_0.dragIndex + 1) then
		arg_14_0:Swap(arg_14_0.dragIndex, arg_14_0.dragIndex + 1)
	end
end

function var_0_0.Swap(arg_15_0, arg_15_1, arg_15_2)
	local var_15_0 = arg_15_0.displayCards[arg_15_1]
	local var_15_1 = arg_15_0.displayPos[arg_15_1]
	local var_15_2 = arg_15_0.displayCards[arg_15_2]

	var_15_2._tf.localPosition = var_15_1
	arg_15_0.displayCards[arg_15_1], arg_15_0.displayCards[arg_15_2] = arg_15_0.displayCards[arg_15_2], arg_15_0.displayCards[arg_15_1]
	arg_15_0.dragIndex = arg_15_2
	var_15_0.slotIndex = arg_15_2
	var_15_2.slotIndex = arg_15_1
	var_15_0.typeIndex, var_15_2.typeIndex = var_15_2.typeIndex, var_15_0.typeIndex

	local var_15_3 = arg_15_0.cards[var_0_1]

	var_15_3[arg_15_1], var_15_3[arg_15_2] = var_15_3[arg_15_2], var_15_3[arg_15_1]
end

function var_0_0.ShouldSwap(arg_16_0, arg_16_1, arg_16_2)
	local var_16_0 = arg_16_0.displayPos[arg_16_2]

	return math.abs(var_16_0.x - arg_16_1.x) <= 130
end

function var_0_0.OnEndDragCard(arg_17_0)
	local var_17_0 = arg_17_0.displayPos[arg_17_0.dragIndex]

	arg_17_0.displayCards[arg_17_0.dragIndex]._tf.localPosition = var_17_0

	local var_17_1 = {}
	local var_17_2 = getProxy(PlayerProxy):getRawData()
	local var_17_3 = false

	for iter_17_0, iter_17_1 in pairs(arg_17_0.displayCards) do
		iter_17_1:EnableDrag()
		table.insert(var_17_1, iter_17_1.displayShip.id)

		if not var_17_3 and var_17_2.characters[#var_17_1] ~= iter_17_1.displayShip.id then
			var_17_3 = true
		end
	end

	arg_17_0.dragIndex = nil
	arg_17_0.displayCards = nil
	arg_17_0.displayPos = nil
	arg_17_0.cardContainerCG.blocksRaycasts = false

	if var_17_3 then
		arg_17_0:emit(PlayerVitaeMediator.CHANGE_PAINTS, var_17_1, function()
			Timer.New(function()
				if arg_17_0.cardContainerCG then
					arg_17_0.cardContainerCG.blocksRaycasts = true
				end
			end, 0.3, 1):Start()
		end)
	else
		arg_17_0.cardContainerCG.blocksRaycasts = true
	end
end

function var_0_0.OnInit(arg_20_0)
	onButton(arg_20_0, arg_20_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("secretary_help")
		})
	end, SFX_PANEL)

	local var_20_0 = false

	local function var_20_1()
		local var_22_0 = {
			68,
			-68
		}

		setAnchoredPosition(arg_20_0.settingBtnSlider, {
			x = var_22_0[var_20_0 and 1 or 2]
		})
	end

	onButton(arg_20_0, arg_20_0.settingBtn, function()
		var_20_0 = not var_20_0

		arg_20_0:EditCards(var_20_0)
		var_20_1()
	end, SFX_PANEL)
	var_20_1()

	local var_20_2 = getProxy(SettingsProxy)

	arg_20_0.randomFlag = var_20_2:IsOpenRandomFlagShip()
	arg_20_0.nativeFlag = false

	local function var_20_3()
		local var_24_0 = {
			68,
			-68
		}

		setAnchoredPosition(arg_20_0.randomBtnSlider, {
			x = var_24_0[arg_20_0.randomFlag and 1 or 2]
		})
		setActive(arg_20_0.nativeBtn, arg_20_0.randomFlag)
		setActive(arg_20_0.flagShipMark, not arg_20_0.randomFlag or arg_20_0.nativeFlag)

		if arg_20_0.randomFlag and var_20_0 then
			triggerButton(arg_20_0.settingBtn)
		end
	end

	local function var_20_4()
		setActive(arg_20_0.nativeBtnOn, arg_20_0.nativeFlag)
		setActive(arg_20_0.nativeBtnOff, not arg_20_0.nativeFlag)
		setActive(arg_20_0.flagShipMark, not arg_20_0.randomFlag or arg_20_0.nativeFlag)

		if var_20_0 then
			triggerButton(arg_20_0.settingBtn)
		end
	end

	onButton(arg_20_0, arg_20_0.randomBtn, function()
		arg_20_0.randomFlag = not arg_20_0.randomFlag

		if arg_20_0.randomFlag then
			local var_26_0 = MainRandomFlagShipSequence.New():Random()

			if not var_26_0 or #var_26_0 <= 0 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("random_ship_off_0"))

				arg_20_0.randomFlag = not arg_20_0.randomFlag

				return
			end

			var_20_2:UpdateRandomFlagShipList(var_26_0)
		else
			var_20_2:UpdateRandomFlagShipList({})

			arg_20_0.nativeFlag = false

			var_20_4()
		end

		arg_20_0:SwitchToPage(arg_20_0.randomFlag and var_0_5 or var_0_4)
		var_20_3()

		local var_26_1 = arg_20_0.randomFlag and i18n("random_ship_on") or i18n("random_ship_off")

		pg.TipsMgr.GetInstance():ShowTips(var_26_1)
		arg_20_0:emit(PlayerVitaeMediator.ON_SWITCH_RANDOM_FLAG_SHIP_BTN, arg_20_0.randomFlag)
	end, SFX_PANEL)
	var_20_3()
	onButton(arg_20_0, arg_20_0.nativeBtn, function()
		arg_20_0.nativeFlag = not arg_20_0.nativeFlag

		var_20_4()
		arg_20_0:SwitchToPage(arg_20_0.nativeFlag and var_0_4 or var_0_5)
	end, SFX_PANEL)
	var_20_4()
	onButton(arg_20_0, arg_20_0.educateCharSettingBtn, function()
		local var_28_0 = isActive(arg_20_0.educateCharSettingList.container)

		setActive(arg_20_0.educateCharSettingList.container, not var_28_0)
	end, SFX_PANEL)
	onButton(arg_20_0, arg_20_0.settingSeceneBtn, function()
		arg_20_0.contextData.showSelectCharacters = true

		arg_20_0:emit(PlayerVitaeMediator.GO_SCENE, SCENE.SETTINGS, {
			page = NewSettingsScene.PAGE_OPTION,
			scroll = SettingsRandomFlagShipAndSkinPanel
		})
	end, SFX_PANEL)

	arg_20_0.cards = {
		{},
		{},
		{}
	}

	table.insert(arg_20_0.cards[var_0_1], PlayerVitaeShipCard.New(arg_20_0.shipTpl, arg_20_0.event))
	table.insert(arg_20_0.cards[var_0_2], PlayerVitaeAddCard.New(arg_20_0.emptyTpl, arg_20_0.event))
	table.insert(arg_20_0.cards[var_0_3], PlayerVitaeLockCard.New(arg_20_0.lockTpl, arg_20_0.event))
end

function var_0_0.Update(arg_30_0)
	local var_30_0 = getProxy(SettingsProxy)
	local var_30_1

	if arg_30_0.randomFlag and arg_30_0.nativeFlag then
		var_30_1 = var_0_4
	else
		var_30_1 = var_30_0:IsOpenRandomFlagShip() and var_0_5 or var_0_4
	end

	arg_30_0:SwitchToPage(var_30_1)
	arg_30_0:UpdateEducateChar()
	arg_30_0:Show()
end

function var_0_0.UpdateEducateChar(arg_31_0)
	arg_31_0:UpdateEducateCharSettings()
	arg_31_0:UpdateEducateSlot()
	arg_31_0:UpdateEducateCharTrTip()
end

function var_0_0.UpdateEducateCharTrTip(arg_32_0)
	setActive(arg_32_0.educateCharTrTip, getProxy(SettingsProxy):ShouldEducateCharTip())
end

local function var_0_6()
	if var_0_0.GetEducateCharSlotMaxCnt() <= 0 then
		return var_0_3
	end

	if getProxy(PlayerProxy):getRawData():ExistEducateChar() then
		return var_0_1
	end

	return var_0_2
end

function var_0_0.UpdateEducateSlot(arg_34_0)
	local var_34_0 = var_0_6()
	local var_34_1

	for iter_34_0, iter_34_1 in pairs(arg_34_0.educateCharCards) do
		local var_34_2 = iter_34_0 == var_34_0

		iter_34_1:ShowOrHide(var_34_2)

		if var_34_2 then
			var_34_1 = iter_34_1
		end
	end

	var_34_1:Flush()
end

function var_0_0.UpdateEducateCharSettings(arg_35_0)
	local var_35_0 = getProxy(SettingsProxy)

	local function var_35_1()
		local var_36_0 = var_35_0:GetFlagShipDisplayMode()

		setText(arg_35_0.educateCharSettingBtn:Find("Text"), i18n("flagship_display_mode_" .. var_36_0))
	end

	local var_35_2 = {
		FlAG_SHIP_DISPLAY_ONLY_SHIP,
		FlAG_SHIP_DISPLAY_ONLY_EDUCATECHAR,
		FlAG_SHIP_DISPLAY_ALL
	}

	arg_35_0.educateCharSettingList:make(function(arg_37_0, arg_37_1, arg_37_2)
		if arg_37_0 == UIItemList.EventUpdate then
			local var_37_0 = var_35_2[arg_37_1 + 1]

			setText(arg_37_2:Find("Text"), i18n("flagship_display_mode_" .. var_37_0))
			onButton(arg_35_0, arg_37_2, function()
				var_35_0:SetFlagShipDisplayMode(var_37_0)
				var_35_1()
				setActive(arg_35_0.educateCharSettingList.container, false)
			end, SFX_PANEL)
			setActive(arg_37_2:Find("line"), arg_37_1 + 1 ~= #var_35_2)
		end
	end)
	arg_35_0.educateCharSettingList:align(#var_35_2)
	var_35_1()
end

function var_0_0.SwitchToPage(arg_39_0, arg_39_1)
	local var_39_0

	if arg_39_1 == var_0_5 then
		var_39_0 = _.select(getProxy(SettingsProxy):GetRandomFlagShipList(), function(arg_40_0)
			return getProxy(BayProxy):RawGetShipById(arg_40_0) ~= nil
		end)
		arg_39_0.tip.text = i18n("random_ship_tips1")

		arg_39_0:emit(PlayerVitaeScene.ON_PAGE_SWTICH, PlayerVitaeScene.PAGE_RANDOM_SHIPS)
	elseif arg_39_1 == var_0_4 then
		var_39_0 = getProxy(PlayerProxy):getRawData().characters
		arg_39_0.tip.text = i18n("random_ship_tips2")

		arg_39_0:emit(PlayerVitaeScene.ON_PAGE_SWTICH, PlayerVitaeScene.PAGE_NATIVE_SHIPS)
	end

	arg_39_0:Flush(var_39_0, arg_39_1)
	setActive(arg_39_0.tip.gameObject, arg_39_0.randomFlag)
end

function var_0_0.Flush(arg_41_0, arg_41_1, arg_41_2)
	local var_41_0, var_41_1 = var_0_0.GetSlotMaxCnt()

	arg_41_0.max = var_41_0
	arg_41_0.unlockCnt = var_41_1

	local var_41_2 = arg_41_0:GetUnlockShipCnt(arg_41_1)

	arg_41_0:UpdateCards(arg_41_2, arg_41_1, var_41_2)
end

function var_0_0.UpdateCards(arg_42_0, arg_42_1, arg_42_2, arg_42_3)
	local var_42_0 = {
		0
	}
	local var_42_1 = {}

	for iter_42_0, iter_42_1 in ipairs(arg_42_3) do
		table.insert(var_42_1, function(arg_43_0)
			arg_42_0:UpdateTypeCards(arg_42_1, arg_42_2, iter_42_0, iter_42_1, var_42_0, arg_43_0)
		end)
	end

	seriesAsync(var_42_1)
end

function var_0_0.UpdateTypeCards(arg_44_0, arg_44_1, arg_44_2, arg_44_3, arg_44_4, arg_44_5, arg_44_6)
	local var_44_0 = {}
	local var_44_1 = arg_44_0.cards[arg_44_3]

	local function var_44_2(arg_45_0)
		local var_45_0 = var_44_1[arg_45_0]

		if not var_45_0 then
			var_45_0 = var_44_1[1]:Clone()
			var_44_1[arg_45_0] = var_45_0
		end

		arg_44_5[1] = arg_44_5[1] + 1

		var_45_0:Enable()
		var_45_0:Update(arg_44_5[1], arg_45_0, arg_44_2, arg_44_1, arg_44_0.nativeFlag)
	end

	for iter_44_0 = 1, arg_44_4 do
		table.insert(var_44_0, function(arg_46_0)
			if arg_44_0.exited then
				return
			end

			var_44_2(iter_44_0)
			onNextTick(arg_46_0)
		end)
	end

	for iter_44_1 = #var_44_1, arg_44_4 + 1, -1 do
		var_44_1[iter_44_1]:Disable()
	end

	seriesAsync(var_44_0, arg_44_6)
end

function var_0_0.GetUnlockShipCnt(arg_47_0, arg_47_1)
	local var_47_0 = 0
	local var_47_1 = 0
	local var_47_2 = 0
	local var_47_3 = #arg_47_1
	local var_47_4 = arg_47_0.unlockCnt - var_47_3
	local var_47_5 = arg_47_0.max - arg_47_0.unlockCnt

	return {
		var_47_3,
		var_47_4,
		var_47_5
	}
end

function var_0_0.EditCards(arg_48_0, arg_48_1)
	local var_48_0 = {
		var_0_1,
		var_0_2
	}

	for iter_48_0, iter_48_1 in ipairs(var_48_0) do
		local var_48_1 = arg_48_0.cards[iter_48_1]

		for iter_48_2, iter_48_3 in ipairs(var_48_1) do
			if isActive(iter_48_3._tf) then
				iter_48_3:EditCard(arg_48_1)
			end
		end
	end

	arg_48_0.IsOpenEdit = arg_48_1
end

function var_0_0.EditCardsForRandom(arg_49_0, arg_49_1)
	local var_49_0 = {}
	local var_49_1 = arg_49_0.cards[var_0_1]

	for iter_49_0, iter_49_1 in ipairs(var_49_1) do
		if isActive(iter_49_1._tf) then
			if not arg_49_1 then
				var_49_0[iter_49_1.slotIndex] = iter_49_1:GetRandomFlagValue()
			end

			iter_49_1:EditCardForRandom(arg_49_1)
		end
	end

	arg_49_0.IsOpenEditForRandom = arg_49_1

	if #var_49_0 > 0 then
		arg_49_0:SaveRandomSettings(var_49_0)
	end

	local var_49_2 = arg_49_0.cards[var_0_2]

	for iter_49_2, iter_49_3 in ipairs(var_49_2) do
		if isActive(iter_49_3._tf) then
			iter_49_3:EditCard(arg_49_1)
		end
	end
end

function var_0_0.SaveRandomSettings(arg_50_0, arg_50_1)
	local var_50_0 = getProxy(PlayerProxy):getRawData()

	for iter_50_0 = 1, arg_50_0.max do
		if not arg_50_1[iter_50_0] then
			arg_50_1[iter_50_0] = var_50_0:RawGetRandomShipAndSkinValueInpos(iter_50_0)
		end
	end

	arg_50_0:emit(PlayerVitaeMediator.CHANGE_RANDOM_SETTING, arg_50_1)
end

function var_0_0.Show(arg_51_0)
	var_0_0.super.Show(arg_51_0)

	Input.multiTouchEnabled = false
end

function var_0_0.Hide(arg_52_0)
	var_0_0.super.Hide(arg_52_0)

	if arg_52_0.IsOpenEdit then
		triggerButton(arg_52_0.settingBtn)
	end

	if arg_52_0.IsOpenEditForRandom then
		triggerButton(arg_52_0.randomBtn)
	end

	Input.multiTouchEnabled = true

	arg_52_0:emit(PlayerVitaeScene.ON_PAGE_SWTICH, PlayerVitaeScene.PAGE_DEFAULT)
end

function var_0_0.OnDestroy(arg_53_0)
	arg_53_0:Hide()

	for iter_53_0, iter_53_1 in pairs(arg_53_0.cards) do
		for iter_53_2, iter_53_3 in pairs(iter_53_1) do
			iter_53_3:Dispose()
		end
	end

	arg_53_0.exited = true
end

return var_0_0
