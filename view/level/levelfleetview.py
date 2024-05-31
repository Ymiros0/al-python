local var_0_0 = class("LevelFleetView", import("..base.BaseSubView"))
local var_0_1 = {
	vanguard = 1,
	submarine = 3,
	main = 2
}

var_0_0.TabIndex = {
	Duty = 3,
	Commander = 2,
	Formation = 1,
	Adjustment = 4
}

local var_0_2 = {
	SELECT = 1,
	EDIT = 2
}
local var_0_3 = {
	NORMAL = 1,
	ADDITION_SUPPORT = 2
}

def var_0_0.getUIName(arg_1_0):
	return "LevelFleetSelectView"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.InitUI()
	arg_2_0.bind(LevelUIConst.CONTINUOUS_OPERATION, function(arg_3_0, arg_3_1)
		local var_3_0 = arg_3_1.battleTimes

		getProxy(ChapterProxy).InitContinuousTime(SYSTEM_SCENARIO, var_3_0)
		LoadContextCommand.RemoveLayerByMediator(LevelContinuousOperationWindowMediator)

		local var_3_1 = "chapter_autofight_flag_" .. arg_2_0.chapter.id

		PlayerPrefs.SetInt(var_3_1, 1)
		triggerButton(arg_2_0.btnGo))
	arg_2_0.bind(LevelMediator2.ON_SPITEM_CHANGED, function(arg_4_0, arg_4_1)
		setActive(arg_2_0.spCheckMark, not arg_4_1)
		triggerButton(arg_2_0.btnSp))

def var_0_0.OnDestroy(arg_5_0):
	if arg_5_0.isShowing():
		arg_5_0.Hide()

def var_0_0.Show(arg_6_0):
	local var_6_0 = arg_6_0.chapter.getConfig("special_operation_list")
	local var_6_1 = arg_6_0.chapter.GetDailyBonusQuota()

	arg_6_0.initSPOPView()

	if type(var_6_0) == "table" and #var_6_0 > 0 and not var_6_1:
		setActive(arg_6_0.btnSp, True)
	else
		setActive(arg_6_0.btnSp, False)

	setActive(arg_6_0._tf, True)

	local var_6_2 = {
		arg_6_0.formationToggle,
		arg_6_0.commanderToggle,
		arg_6_0.dutyToggle,
		arg_6_0.adjustmentToggle
	}
	local var_6_3 = var_6_2[arg_6_0.contextData.tabIndex or var_0_0.TabIndex.Formation]

	if not isActive(var_6_3):
		var_6_3 = var_6_2[var_0_0.TabIndex.Formation]

	for iter_6_0, iter_6_1 in ipairs(var_6_2):
		if isActive(iter_6_1):
			triggerToggle(iter_6_1, iter_6_1 == var_6_3)

	pg.UIMgr.GetInstance().BlurPanel(arg_6_0._tf)
	arg_6_0.TryPlaySupportGuide()
	arg_6_0.CheckGuideElement()

def var_0_0.CheckGuideElement(arg_7_0):
	if not IsUnityEditor:
		return

	local var_7_0 = {
		"panel/Fixed/start_button",
		"panel/ShipList/support/1/support"
	}

	_.each(var_7_0, function(arg_8_0)
		local var_8_0 = arg_7_0._tf.Find(arg_8_0)

		assert(var_8_0, "Missing Guide Need GameObject Path. " .. arg_8_0))

def var_0_0.TryPlaySupportGuide(arg_9_0):
	if arg_9_0.getLimitNums(FleetType.Support) == 0:
		return

	if not pg.NewStoryMgr.GetInstance().IsPlayed("NG0041"):
		pg.SystemGuideMgr.GetInstance().PlayByGuideId("NG0041")

def var_0_0.Hide(arg_10_0):
	setActive(arg_10_0.dropDown, False)
	setActive(arg_10_0.btnSp, False)
	setActive(arg_10_0._tf, False)

	arg_10_0.spItemID = None

	pg.UIMgr.GetInstance().UnblurPanel(arg_10_0._tf, arg_10_0._parentTf)

def var_0_0.setOpenCommanderTag(arg_11_0, arg_11_1):
	arg_11_0.openedCommanerSystem = arg_11_1

def var_0_0.SetDutyTabEnabled(arg_12_0, arg_12_1):
	arg_12_0.dutyTabEnabled = arg_12_1

def var_0_0.onConfirm(arg_13_0):
	local var_13_0 = arg_13_0.chapter
	local var_13_1 = arg_13_0.getSelectIds()
	local var_13_2 = var_13_0.getNpcShipByType(2)

	if #var_13_2 > 0:
		local var_13_3 = {
			[TeamType.Vanguard] = #arg_13_0.getFleetById(var_13_1[1]).getTeamByName(TeamType.Vanguard),
			[TeamType.Main] = #arg_13_0.getFleetById(var_13_1[1]).getTeamByName(TeamType.Main)
		}
		local var_13_4 = {
			[TeamType.Vanguard] = 0,
			[TeamType.Main] = 0
		}
		local var_13_5

		for iter_13_0, iter_13_1 in ipairs(var_13_2):
			var_13_5 = iter_13_1

			local var_13_6 = iter_13_1.getTeamType()

			var_13_4[var_13_6] = var_13_4[var_13_6] + 1

			if var_13_3[var_13_6] + var_13_4[var_13_6] > 3:
				break

		for iter_13_2, iter_13_3 in pairs(var_13_3):
			if iter_13_3 + var_13_4[iter_13_2] > 3:
				arg_13_0.emit(LevelUIConst.HANDLE_SHOW_MSG_BOX, {
					modal = True,
					hideNo = True,
					content = i18n("chapter_tip_with_npc", var_13_5.name)
				})

				return

	local var_13_7 = "chapter_autofight_flag_" .. var_13_0.id
	local var_13_8
	local var_13_9

	seriesAsync({
		function(arg_14_0)
			local var_14_0 = PlayerPrefs.GetInt("autoFight_firstUse_sp", 0) == 1

			if not (PlayerPrefs.GetInt(var_13_7, 1) == 1) or var_14_0 or not arg_13_0.getSPItem():
				return arg_14_0()

			PlayerPrefs.SetInt("autoFight_firstUse_sp", 1)
			PlayerPrefs.Save()

			local function var_14_1()
				arg_13_0.clearSPBuff()

			arg_13_0.emit(LevelUIConst.HANDLE_SHOW_MSG_BOX, {
				hideNo = True,
				content = i18n("autofight_special_operation_tip"),
				onYes = var_14_1,
				onNo = var_14_1
			}),
		function(arg_16_0)
			var_13_9 = var_13_0.GetActiveSPItemID()
			var_13_8 = var_13_0.isLoop() and arg_13_0.GetOrderedDuties() or None

			arg_13_0.onCancel()
			arg_16_0(),
		function(arg_17_0)
			getProxy(ChapterProxy).SetLastFleetIndex(var_13_1)

			local var_17_0 = PlayerPrefs.GetInt(var_13_7, 1) == 1
			local var_17_1 = LevelMediator2.ON_TRACKING
			local var_17_2 = packEx(var_13_0.id, var_13_0.loopFlag, var_13_9, var_13_8, var_17_0)

			if pg.m02.retrieveMediator(LevelMediator2.__cname):
				pg.m02.sendNotification(var_17_1, var_17_2)

				return

			local var_17_3 = getProxy(ContextProxy).getContextByMediator(LevelMediator2)

			if var_17_3:
				var_17_3.extendData({
					ToTrackingData = {
						var_17_1,
						var_17_2
					}
				})
	})

def var_0_0.onCancel(arg_18_0):
	arg_18_0.clear()
	arg_18_0.emit(LevelUIConst.HIDE_FLEET_SELECT)

def var_0_0.InitUI(arg_19_0):
	arg_19_0.tfShipTpl = arg_19_0.findTF("panel/Fixed/shiptpl")
	arg_19_0.tfEmptyTpl = arg_19_0.findTF("panel/Fixed/emptytpl")
	arg_19_0.tfFleets = {
		[FleetType.Normal] = {
			arg_19_0.findTF("panel/ShipList/fleet/1"),
			arg_19_0.findTF("panel/ShipList/fleet/2")
		},
		[FleetType.Submarine] = {
			arg_19_0.findTF("panel/ShipList/sub/1")
		},
		[FleetType.Support] = {
			arg_19_0.findTF("panel/ShipList/support/1")
		}
	}

	local var_19_0 = arg_19_0.findTF("panel/Fixed/RightTabs")
	local var_19_1 = PLATFORM_CODE == PLATFORM_US and arg_19_0.findTF("panel/Fixed/RightTabs/hTplBtn") or arg_19_0.findTF("panel/Fixed/RightTabs/vTplBtn")
	local var_19_2 = {
		"formation_btn",
		"commander_btn",
		"duty_btn",
		"adjustment_btn"
	}

	for iter_19_0 = 1, #var_19_2:
		local var_19_3 = Instantiate(var_19_1)

		var_19_3.name = var_19_2[iter_19_0]

		SetParent(tf(var_19_3), var_19_0)
		setActive(var_19_3, False)

	arg_19_0.tfLimit = arg_19_0.findTF("panel/Fixed/limit_list/limit")
	arg_19_0.tfLimitTips = arg_19_0.findTF("panel/Fixed/limit_list/limit_tip")
	arg_19_0.tfLimitElite = arg_19_0.findTF("panel/Fixed/limit_list/limit_elite")
	arg_19_0.tfLimitSubTip = arg_19_0.findTF("panel/Fixed/limit_list/limit_sub_tip")
	arg_19_0.tfLimitContainer = arg_19_0.findTF("panel/Fixed/limit_list/limit_elite/limit_list")
	arg_19_0.rtCostLimit = arg_19_0._tf.Find("panel/Fixed/limit_list/cost_limit")
	arg_19_0.btnBack = arg_19_0.findTF("panel/Fixed/btnBack")
	arg_19_0.btnGo = arg_19_0.findTF("panel/Fixed/start_button")
	arg_19_0.btnMultiple = arg_19_0.findTF("panel/Fixed/multiple")
	arg_19_0.formationToggle = arg_19_0.findTF("panel/Fixed/RightTabs/formation_btn")
	arg_19_0.commanderToggle = arg_19_0.findTF("panel/Fixed/RightTabs/commander_btn")
	arg_19_0.dutyToggle = arg_19_0.findTF("panel/Fixed/RightTabs/duty_btn")
	arg_19_0.adjustmentToggle = arg_19_0.findTF("panel/Fixed/RightTabs/adjustment_btn")
	arg_19_0.toggleMask = arg_19_0.findTF("mask")
	arg_19_0.toggleList = arg_19_0.findTF("mask/list")
	arg_19_0.toggles = {}

	setText(findTF(arg_19_0.tfLimit, "text"), i18n("level_fleet_ship_desc"))
	setText(findTF(arg_19_0.tfLimit, "text_sub"), i18n("level_fleet_sub_desc"))

	for iter_19_1 = 0, arg_19_0.toggleList.childCount - 1:
		table.insert(arg_19_0.toggles, arg_19_0.toggleList.Find("item" .. iter_19_1 + 1))

	arg_19_0.btnSp = arg_19_0.findTF("panel/Fixed/sp")
	arg_19_0.spMask = arg_19_0.findTF("mask_sp")
	arg_19_0.dutyItems = {}

	for iter_19_2 = 1, 2:
		local var_19_4 = arg_19_0._tf.Find(string.format("panel/ShipList/fleet/%d/DutySelect", iter_19_2))

		arg_19_0.dutyItems[iter_19_2] = {}

		for iter_19_3 = 1, 4:
			local var_19_5 = var_19_4.Find("Item" .. iter_19_3)

			arg_19_0.dutyItems[iter_19_2][iter_19_3] = var_19_5

			setText(var_19_5.Find("Text"), i18n("autofight_function" .. iter_19_3))

	local var_19_6 = arg_19_0._tf.Find("panel/ShipList/sub/1/DutySelect")

	arg_19_0.dutyItems[3] = {}

	for iter_19_4 = 1, 2:
		local var_19_7 = var_19_6.Find("Item" .. iter_19_4)

		arg_19_0.dutyItems[3][iter_19_4] = var_19_7

		setText(var_19_7.Find("Text"), i18n("autofight_function" .. 6 - iter_19_4))

	setActive(arg_19_0.tfShipTpl, False)
	setActive(arg_19_0.tfEmptyTpl, False)
	setActive(arg_19_0.toggleMask, False)
	setActive(arg_19_0.btnSp, False)
	setActive(arg_19_0.spMask, False)
	setText(arg_19_0.findTF("panel/Fixed/RightTabs/formation_btn/text"), i18n("autofight_formation"))
	setText(arg_19_0.findTF("panel/Fixed/RightTabs/commander_btn/text"), i18n("autofight_cat"))
	setText(arg_19_0.findTF("panel/Fixed/RightTabs/duty_btn/text"), i18n("autofight_function"))
	setText(arg_19_0.adjustmentToggle.Find("text"), i18n("word_adjustFleet"))

	arg_19_0.dropDown = arg_19_0._tf.Find("panel/FixedTop/Dropdown")

	setActive(arg_19_0.dropDown, False)

	arg_19_0.dropDownSide = arg_19_0._tf.Find("panel/Fixed/title/DropSide")

	onButton(arg_19_0, arg_19_0.dropDownSide.Find("Click"), function()
		local var_20_0 = isActive(arg_19_0.dropDown)

		setActive(arg_19_0.dropDown, not var_20_0), SFX_UI_CLICK)
	onButton(arg_19_0, arg_19_0.dropDown, function()
		local var_21_0 = isActive(arg_19_0.dropDown)

		setActive(arg_19_0.dropDown, not var_21_0), SFX_UI_CLICK)
	onButton(arg_19_0, arg_19_0.dropDownSide.Find("Layout/Item3"), function()
		arg_19_0.emit(LevelUIConst.HANDLE_SHOW_MSG_BOX, {
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.fleet_antisub_range_tip.tip
		}), SFX_PANEL)
	assert(OPEN_AIR_DOMINANCE, "Not Prepare for BANNED OPEN_AIR_DOMINANCE")

	arg_19_0.btnASHelp = arg_19_0.dropDownSide.Find("help")

	setText(arg_19_0.dropDownSide.Find("Layout/Item1/Text"), i18n("word_investigate"))
	setText(arg_19_0.dropDownSide.Find("Layout/Item2/Text"), i18n("word_attr_ac"))
	setText(arg_19_0.dropDownSide.Find("Layout/Item3/Text"), i18n("fleet_antisub_range"))
	setText(arg_19_0.dropDown.Find("Investigation/Text"), i18n("level_scene_title_word_1"))
	setText(arg_19_0.dropDown.Find("Airsupport/Text"), i18n("level_scene_title_word_3"))

	arg_19_0.supportFleetHelp = arg_19_0._tf.Find("panel/Fixed/title/Image/Help")

	onButton(arg_19_0, arg_19_0.supportFleetHelp, function()
		arg_19_0.emit(LevelUIConst.HANDLE_SHOW_MSG_BOX, {
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_supportfleet.tip
		}), SFX_PANEL)

	for iter_19_5 = 1, 2:
		for iter_19_6 = 1, 4:
			local var_19_8 = arg_19_0.dutyItems[iter_19_5][iter_19_6]

			onButton(arg_19_0, var_19_8, function()
				arg_19_0.SetDuty(iter_19_5, iter_19_6))

	for iter_19_7 = 1, 2:
		local var_19_9 = arg_19_0.dutyItems[3][iter_19_7]

		onButton(arg_19_0, var_19_9, function()
			arg_19_0.SetAutoSub(iter_19_7 == 1))

def var_0_0.onCancelSupport(arg_26_0, arg_26_1):
	if arg_26_1:
		arg_26_0.emit(LevelMediator2.ON_UPDATE_CUSTOM_FLEET, arg_26_0.chapter)

def var_0_0.set(arg_27_0, arg_27_1, arg_27_2, arg_27_3):
	arg_27_0.chapter = arg_27_1
	arg_27_0.mode = var_0_2.SELECT
	arg_27_0.selects = arg_27_3
	arg_27_0.chapterASValue = arg_27_0.chapter.getConfig("air_dominance")
	arg_27_0.suggestionValue = arg_27_0.chapter.getConfig("best_air_dominance")

	arg_27_0.SetDutyTabEnabled(arg_27_1.isLoop())

	arg_27_0.supportFleet = arg_27_0.chapter.getSupportFleet()

	local var_27_0 = arg_27_0.getLimitNums(FleetType.Support) > 0

	setActive(arg_27_0.supportFleetHelp, var_27_0)

	arg_27_0.displayMode = var_27_0 and var_0_3.ADDITION_SUPPORT or var_0_3.NORMAL

	arg_27_0.SwitchDisplayMode()

	arg_27_0.fleets = _(_.values(arg_27_2)).chain().filter(function(arg_28_0)
		return arg_28_0.isRegularFleet()).sort(function(arg_29_0, arg_29_1)
		return arg_29_0.id < arg_29_1.id).value()
	arg_27_0.selectIds = {
		[FleetType.Normal] = {},
		[FleetType.Submarine] = {}
	}

	for iter_27_0, iter_27_1 in ipairs(arg_27_3 or {}):
		local var_27_1 = arg_27_0.getFleetById(iter_27_1)

		if var_27_1:
			local var_27_2 = var_27_1.getFleetType()
			local var_27_3 = arg_27_0.selectIds[var_27_2]

			if #var_27_3 < arg_27_0.getLimitNums(var_27_2):
				table.insert(var_27_3, iter_27_1)

	arg_27_0.duties = {}

	local var_27_4 = PlayerPrefs.GetInt("lastFleetDuty_" .. (arg_27_0.chapter.id or 0), 0)

	if var_27_4 > 0:
		local var_27_5 = bit.band(var_27_4, 255)
		local var_27_6 = bit.rshift(var_27_4, 8)
		local var_27_7 = bit.band(var_27_6, 255)

		if var_27_5 > 0 and var_27_7 > 0:
			arg_27_0.duties[var_27_5] = var_27_7

	setActive(arg_27_0.tfLimitElite, False)
	setActive(arg_27_0.tfLimitSubTip, False)
	setActive(arg_27_0.tfLimitTips, False)
	setActive(arg_27_0.tfLimit, True)

	local var_27_8 = arg_27_0.chapter.isLoop() and arg_27_0.chapter.getConfig("use_oil_limit") or {}

	setActive(arg_27_0.rtCostLimit, #var_27_8 > 0)
	setText(arg_27_0.rtCostLimit.Find("text"), i18n("formationScene_use_oil_limit_tip"))

	if #var_27_8 > 0:
		setActive(arg_27_0.rtCostLimit.Find("cost_noraml"), var_27_8[1] > 0)
		setText(arg_27_0.rtCostLimit.Find("cost_noraml/Text"), string.format("%s(%d)", i18n("formationScene_use_oil_limit_enemy"), var_27_8[1]))
		setActive(arg_27_0.rtCostLimit.Find("cost_boss"), var_27_8[2] > 0)
		setText(arg_27_0.rtCostLimit.Find("cost_boss/Text"), string.format("%s(%d)", i18n("formationScene_use_oil_limit_flagship"), var_27_8[2]))
		setActive(arg_27_0.rtCostLimit.Find("cost_sub"), var_27_8[3] > 0)
		setText(arg_27_0.rtCostLimit.Find("cost_sub/Text"), string.format("%s(%d)", i18n("formationScene_use_oil_limit_submarine"), var_27_8[3]))

	onButton(arg_27_0, arg_27_0.btnGo, function()
		local function var_30_0()
			arg_27_0.onConfirm()

		local var_30_1 = arg_27_0.getSPItem()

		if var_30_1 and var_30_1 != 0:
			if PlayerPrefs.GetInt("SPOPItemReminder") != 1:
				local var_30_2 = Item.getConfigData(var_30_1).name
				local var_30_3 = pg.benefit_buff_template[Chapter.GetSPBuffByItem(var_30_1)].desc
				local var_30_4 = i18n("levelScene_select_SP_OP_reminder", var_30_2, var_30_3)

				local function var_30_5()
					PlayerPrefs.SetInt("SPOPItemReminder", 1)
					PlayerPrefs.Save()
					var_30_0()

				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					type = MSGBOX_TYPE_SINGLE_ITEM,
					drop = {
						count = 1,
						type = DROP_TYPE_ITEM,
						id = var_30_1
					},
					intro = var_30_4,
					onYes = var_30_5,
					weight = LayerWeightConst.TOP_LAYER
				})
			else
				var_30_0()
		else
			var_30_0(), SFX_UI_WEIGHANCHOR_GO)
	setActive(arg_27_0.btnMultiple, AutoBotCommand.autoBotSatisfied() and arg_27_0.chapter.isLoop())
	onButton(arg_27_0, arg_27_0.btnMultiple, function()
		local var_33_0 = arg_27_0.getSelectIds()
		local var_33_1 = arg_27_0.getSPItem()
		local var_33_2 = arg_27_0.GetOrderedDuties()

		arg_27_0.emit(LevelUIConst.OPEN_NORMAL_CONTINUOUS_WINDOW, arg_27_0.chapter, var_33_0, var_33_1, var_33_2), SFX_PANEL)
	onButton(arg_27_0, arg_27_0.btnASHelp, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("help_battle_ac")
		}), SFX_UI_CLICK)
	onButton(arg_27_0, arg_27_0.btnBack, function()
		arg_27_0.onCancel()
		arg_27_0.onCancelSupport(True), SFX_CANCEL)
	onButton(arg_27_0, arg_27_0._tf.Find("bg"), function()
		arg_27_0.onCancel()
		arg_27_0.onCancelSupport(True), SFX_CANCEL)
	onButton(arg_27_0, arg_27_0.toggleMask, function()
		arg_27_0.hideToggleMask(), SFX_CANCEL)
	onToggle(arg_27_0, arg_27_0.formationToggle, function(arg_38_0)
		if arg_38_0:
			arg_27_0.contextData.tabIndex = var_0_0.TabIndex.Formation

			arg_27_0.updateFleets(), SFX_PANEL)
	onToggle(arg_27_0, arg_27_0.commanderToggle, function(arg_39_0)
		if arg_39_0:
			arg_27_0.contextData.tabIndex = var_0_0.TabIndex.Commander

			arg_27_0.updateFleets(), SFX_PANEL)
	onToggle(arg_27_0, arg_27_0.dutyToggle, function(arg_40_0)
		if arg_40_0:
			arg_27_0.contextData.tabIndex = var_0_0.TabIndex.Duty

			arg_27_0.updateFleets(), SFX_PANEL)
	setActive(arg_27_0.formationToggle, True)
	setActive(arg_27_0.commanderToggle, arg_27_0.openedCommanerSystem)
	setActive(arg_27_0.dutyToggle, arg_27_0.dutyTabEnabled)
	setActive(arg_27_0.adjustmentToggle, False)
	arg_27_0.clearFleets()
	arg_27_0.updateFleets()
	arg_27_0.updateLimit()
	arg_27_0.updateASValue()
	arg_27_0.UpdateSonarRange()
	arg_27_0.UpdateInvestigation()

def var_0_0.getFleetById(arg_41_0, arg_41_1):
	return _.detect(arg_41_0.fleets, function(arg_42_0)
		return arg_42_0.id == arg_41_1)

def var_0_0.getLimitNums(arg_43_0, arg_43_1):
	local var_43_0 = 0

	if arg_43_1 == FleetType.Normal:
		var_43_0 = arg_43_0.chapter.getConfig("group_num")
	elif arg_43_1 == FleetType.Submarine:
		var_43_0 = arg_43_0.chapter.getConfig("submarine_num")
	elif arg_43_1 == FleetType.Support:
		var_43_0 = arg_43_0.chapter.getConfig("support_group_num")

	return var_43_0

def var_0_0.getSelectIds(arg_44_0):
	local var_44_0 = {}

	for iter_44_0, iter_44_1 in ipairs({
		FleetType.Normal,
		FleetType.Submarine
	}):
		local var_44_1 = arg_44_0.selectIds[iter_44_1]

		for iter_44_2, iter_44_3 in ipairs(var_44_1):
			if iter_44_3 > 0:
				table.insert(var_44_0, iter_44_3)

	return var_44_0

def var_0_0.updateFleets(arg_45_0):
	for iter_45_0, iter_45_1 in pairs(arg_45_0.tfFleets):
		for iter_45_2 = 1, #iter_45_1:
			if iter_45_0 != FleetType.Support:
				arg_45_0.updateFleet(iter_45_0, iter_45_2)
			else
				arg_45_0.UpdateEliteFleet(iter_45_0, iter_45_2)

	arg_45_0.RefreshDutyBar()

def var_0_0.updateLimit(arg_46_0):
	local var_46_0 = #_.filter(arg_46_0.selectIds[FleetType.Normal], function(arg_47_0)
		return arg_47_0 > 0)
	local var_46_1 = #_.filter(arg_46_0.selectIds[FleetType.Submarine], function(arg_48_0)
		return arg_48_0 > 0)
	local var_46_2 = arg_46_0.getLimitNums(FleetType.Normal)

	setText(arg_46_0.tfLimit.Find("number"), string.format("%d/%d", var_46_0, var_46_2))

	local var_46_3 = arg_46_0.getLimitNums(FleetType.Submarine)

	setText(arg_46_0.tfLimit.Find("number_sub"), string.format("%d/%d", var_46_1, var_46_3))

def var_0_0.selectFleet(arg_49_0, arg_49_1, arg_49_2, arg_49_3):
	local var_49_0 = arg_49_0.selectIds[arg_49_1]

	if arg_49_3 > 0 and table.contains(var_49_0, arg_49_3):
		return

	if arg_49_1 == FleetType.Normal and arg_49_0.getLimitNums(arg_49_1) > 0 and arg_49_3 == 0 and #_.filter(var_49_0, function(arg_50_0)
		return arg_50_0 > 0) == 1:
		pg.TipsMgr.GetInstance().ShowTips(i18n("level_fleet_lease_one_ship"))

		return

	local var_49_1 = arg_49_0.getFleetById(arg_49_3)

	if var_49_1:
		if not var_49_1.isUnlock():
			return

		if var_49_1.isLegalToFight() != True:
			pg.TipsMgr.GetInstance().ShowTips(i18n("level_fleet_not_enough"))

			return

	local var_49_2 = {
		not arg_49_0.IsListOfFleetEmpty(1) or None,
		not arg_49_0.IsListOfFleetEmpty(2) or None
	}
	local var_49_3 = var_49_0[arg_49_2]

	var_49_0[arg_49_2] = arg_49_3

	arg_49_0.updateFleet(arg_49_1, arg_49_2)
	arg_49_0.updateLimit()
	arg_49_0.updateASValue()
	arg_49_0.UpdateSonarRange()
	arg_49_0.RefreshDutyBar()

	local var_49_4 = {
		not arg_49_0.IsListOfFleetEmpty(1) or None,
		not arg_49_0.IsListOfFleetEmpty(2) or None
	}

	if arg_49_0.dutyTabEnabled and table.getCount(var_49_2) == 2 and table.getCount(var_49_4) == 1:
		pg.TipsMgr.GetInstance().ShowTips(i18n("autofight_change_tip"))

	arg_49_0.UpdateInvestigation()

def var_0_0.updateFleet(arg_51_0, arg_51_1, arg_51_2):
	local var_51_0 = arg_51_0.contextData.tabIndex == var_0_0.TabIndex.Formation
	local var_51_1 = arg_51_0.contextData.tabIndex == var_0_0.TabIndex.Commander
	local var_51_2 = arg_51_0.contextData.tabIndex == var_0_0.TabIndex.Duty
	local var_51_3 = arg_51_0.contextData.tabIndex == var_0_0.TabIndex.Adjustment
	local var_51_4 = arg_51_0.selectIds[arg_51_1][arg_51_2]
	local var_51_5 = arg_51_0.getFleetById(var_51_4)
	local var_51_6 = arg_51_2 <= arg_51_0.getLimitNums(arg_51_1)
	local var_51_7 = arg_51_0.tfFleets[arg_51_1][arg_51_2]
	local var_51_8 = findTF(var_51_7, "bg/name")
	local var_51_9 = arg_51_0.findTF("btn_select", var_51_7)
	local var_51_10 = arg_51_0.findTF("btn_recom", var_51_7)
	local var_51_11 = arg_51_0.findTF("btn_clear", var_51_7)
	local var_51_12 = arg_51_0.findTF("blank", var_51_7)
	local var_51_13 = arg_51_0.findTF("selected", var_51_7)
	local var_51_14 = arg_51_0.findTF("commander", var_51_7)
	local var_51_15 = var_51_7.Find("adjustment_flag")

	setActive(var_51_10, False)
	setActive(var_51_13, False)
	setText(var_51_8, "")

	local var_51_16 = arg_51_0.findTF(TeamType.Main, var_51_7)
	local var_51_17 = arg_51_0.findTF(TeamType.Vanguard, var_51_7)
	local var_51_18 = arg_51_0.findTF(TeamType.Submarine, var_51_7)

	if not var_51_6:
		setActive(var_51_11, False)
		setActive(var_51_9, False)
		setActive(var_51_14, False)
		setActive(var_51_15, False)
		setActive(var_51_12, True)

		if arg_51_1 == FleetType.Submarine:
			setActive(var_51_18, False)
		else
			setActive(var_51_16, False)
			setActive(var_51_17, False)

		return

	setActive(var_51_11, var_51_0)
	setActive(var_51_9, var_51_0)
	setActive(var_51_14, var_51_1 and var_51_5)
	setActive(var_51_15, var_51_3)
	setActive(var_51_12, var_51_2 or var_51_3 or var_51_1 and not var_51_5)
	setText(var_51_8, var_51_5 and var_51_5.GetName() or "")

	if arg_51_1 == FleetType.Submarine:
		setActive(var_51_18, var_51_5)
	else
		setActive(var_51_16, var_51_5)
		setActive(var_51_17, var_51_5)

	if var_51_5:
		if arg_51_1 == FleetType.Submarine:
			arg_51_0.updateShips(var_51_18, var_51_5.subShips)
		else
			arg_51_0.updateShips(var_51_16, var_51_5.mainShips)
			arg_51_0.updateShips(var_51_17, var_51_5.vanguardShips)

		arg_51_0.updateCommanders(var_51_14, var_51_5)

	onButton(arg_51_0, var_51_9, function()
		arg_51_0.toggleList.position = (var_51_9.position + var_51_11.position) / 2
		arg_51_0.toggleList.anchoredPosition = arg_51_0.toggleList.anchoredPosition + Vector2(-arg_51_0.toggleList.rect.width / 2, -var_51_9.rect.height / 2)

		arg_51_0.showToggleMask(arg_51_1, function(arg_53_0)
			arg_51_0.hideToggleMask()
			arg_51_0.selectFleet(arg_51_1, arg_51_2, arg_53_0)), SFX_UI_CLICK)
	onButton(arg_51_0, var_51_11, function()
		arg_51_0.selectFleet(arg_51_1, arg_51_2, 0), SFX_UI_CLICK)

def var_0_0.updateCommanders(arg_55_0, arg_55_1, arg_55_2):
	for iter_55_0 = 1, 2:
		local var_55_0 = arg_55_2.getCommanderByPos(iter_55_0)
		local var_55_1 = arg_55_1.Find("pos" .. iter_55_0)
		local var_55_2 = var_55_1.Find("add")
		local var_55_3 = var_55_1.Find("info")

		setActive(var_55_2, not var_55_0)
		setActive(var_55_3, var_55_0)

		if var_55_0:
			local var_55_4 = Commander.rarity2Frame(var_55_0.getRarity())

			setImageSprite(var_55_3.Find("frame"), GetSpriteFromAtlas("weaponframes", "commander_" .. var_55_4))
			GetImageSpriteFromAtlasAsync("CommanderHrz/" .. var_55_0.getPainting(), "", var_55_3.Find("mask/icon"))

		onButton(arg_55_0, var_55_2, function()
			arg_55_0.emit(LevelUIConst.OPEN_COMMANDER_PANEL, arg_55_2, arg_55_0.chapter), SFX_PANEL)
		onButton(arg_55_0, var_55_3, function()
			arg_55_0.emit(LevelUIConst.OPEN_COMMANDER_PANEL, arg_55_2, arg_55_0.chapter), SFX_PANEL)

def var_0_0.updateShips(arg_58_0, arg_58_1, arg_58_2):
	local var_58_0 = UIItemList.New(arg_58_1, arg_58_0.tfShipTpl)

	var_58_0.make(function(arg_59_0, arg_59_1, arg_59_2)
		if arg_59_0 == UIItemList.EventUpdate:
			local var_59_0 = getProxy(BayProxy).getShipById(arg_58_2[arg_59_1 + 1])

			updateShip(arg_59_2, var_59_0)
			setActive(findTF(arg_59_2, "ship_type"), False)

			local var_59_1 = arg_59_2.Find("icon_bg/energy")
			local var_59_2 = var_59_0.getEnergeConfig()

			if var_59_2 and var_59_2.id <= 2:
				setActive(var_59_1, True)
				GetImageSpriteFromAtlasAsync("energy", var_59_2.icon, var_59_1)
			else
				setActive(var_59_1, False))
	var_58_0.align(#arg_58_2)

	for iter_58_0, iter_58_1 in ipairs(arg_58_2):
		local var_58_1 = arg_58_1.GetChild(iter_58_0 - 1)
		local var_58_2 = GetOrAddComponent(var_58_1, "UILongPressTrigger").onLongPressed

		pg.DelegateInfo.Add(arg_58_0, var_58_2)
		var_58_2.RemoveAllListeners()
		var_58_2.AddListener(function()
			arg_58_0.emit(LevelMediator2.ON_SHIP_DETAIL, {
				id = iter_58_1,
				chapter = arg_58_0.chapter
			}))

def var_0_0.showToggleMask(arg_61_0, arg_61_1, arg_61_2):
	setActive(arg_61_0.toggleMask, True)

	local var_61_0 = _.filter(arg_61_0.fleets, function(arg_62_0)
		return arg_62_0.getFleetType() == arg_61_1)

	for iter_61_0, iter_61_1 in ipairs(arg_61_0.toggles):
		local var_61_1 = var_61_0[iter_61_0]

		setActive(iter_61_1, var_61_1)

		if var_61_1:
			local var_61_2 = iter_61_1.GetComponent(typeof(Toggle))
			local var_61_3 = iter_61_1.Find("lock")
			local var_61_4, var_61_5 = var_61_1.isUnlock()

			setToggleEnabled(iter_61_1, var_61_4)
			setActive(var_61_3, not var_61_4)

			local var_61_6 = table.contains(arg_61_0.selectIds[arg_61_1], var_61_1.id)

			setActive(iter_61_1.Find("on"), var_61_6)
			setActive(iter_61_1.Find("off"), not var_61_6)

			if var_61_4:
				var_61_2.isOn = False

				onToggle(arg_61_0, iter_61_1, function(arg_63_0)
					if arg_63_0:
						setActive(arg_61_0.toggleMask, False)
						arg_61_2(var_61_1.id), SFX_UI_TAG)
			else
				onButton(arg_61_0, var_61_3, function()
					pg.TipsMgr.GetInstance().ShowTips(var_61_5), SFX_UI_CLICK)

def var_0_0.hideToggleMask(arg_65_0):
	setActive(arg_65_0.toggleMask, False)

def var_0_0.clearFleets(arg_66_0):
	for iter_66_0, iter_66_1 in pairs(arg_66_0.tfFleets):
		_.each(iter_66_1, function(arg_67_0)
			arg_66_0.clearFleet(arg_67_0))

def var_0_0.UpdateInvestigation(arg_68_0):
	if not arg_68_0.chapter.existAmbush():
		arg_68_0.UpdateLoopInvestigation()

		return

	local var_68_0 = 0

	for iter_68_0 = 1, 2:
		local var_68_1 = arg_68_0.selectIds[FleetType.Normal][iter_68_0] or 0
		local var_68_2 = arg_68_0.getFleetById(var_68_1)
		local var_68_3 = var_68_2 and math.floor(var_68_2.getInvestSums(True)) or 0

		var_68_0 = math.max(var_68_0, var_68_3)

	local var_68_4 = arg_68_0.chapter.getConfig("avoid_require")

	arg_68_0.UpdateInvestigationComparision(var_68_0, var_68_4)

def var_0_0.UpdateEliteInvestigation(arg_69_0):
	if not arg_69_0.chapter.existAmbush():
		arg_69_0.UpdateLoopInvestigation()

		return

	local var_69_0 = 0

	for iter_69_0 = 1, 2:
		local var_69_1 = arg_69_0.eliteFleetList[iter_69_0]
		local var_69_2 = {}

		for iter_69_1, iter_69_2 in pairs(arg_69_0.eliteCommanderList[iter_69_0]):
			table.insert(var_69_2, {
				pos = iter_69_1,
				id = iter_69_2
			})

		local var_69_3 = TypedFleet.New({
			ship_list = var_69_1,
			commanders = var_69_2,
			fleetType = FleetType.Normal
		})
		local var_69_4 = var_69_3 and math.floor(var_69_3.getInvestSums()) or 0

		var_69_0 = math.max(var_69_0, var_69_4)

	local var_69_5 = arg_69_0.chapter.getConfig("avoid_require")

	arg_69_0.UpdateInvestigationComparision(var_69_0, var_69_5)

def var_0_0.UpdateLoopInvestigation(arg_70_0):
	local var_70_0 = arg_70_0.dropDown.Find("Investigation")

	setText(var_70_0.Find("Value1"), "-")
	setText(var_70_0.Find("Value2"), "-")
	triggerToggle(arg_70_0.dropDownSide.Find("Layout/Item1/Dot"), True)

def var_0_0.UpdateInvestigationComparision(arg_71_0, arg_71_1, arg_71_2):
	arg_71_1 = math.floor(arg_71_1)

	local var_71_0 = arg_71_0.dropDown.Find("Investigation")
	local var_71_1 = arg_71_2 <= arg_71_1

	setText(var_71_0.Find("Value1"), setColorStr(arg_71_1, var_71_1 and "#51FF55" or COLOR_WHITE))
	setText(var_71_0.Find("Value2"), arg_71_2)
	triggerToggle(arg_71_0.dropDownSide.Find("Layout/Item1/Dot"), var_71_1)

def var_0_0.updateASValue(arg_72_0):
	if arg_72_0.chapterASValue <= 0:
		arg_72_0.UpdateBannedAS()

		return

	local var_72_0 = 0

	for iter_72_0 = 1, 2:
		local var_72_1 = arg_72_0.selectIds[FleetType.Normal][iter_72_0] or 0
		local var_72_2 = arg_72_0.getFleetById(var_72_1)

		var_72_0 = var_72_0 + (var_72_2 and var_72_2.getFleetAirDominanceValue() or 0)

	for iter_72_1 = 1, 1:
		local var_72_3 = arg_72_0.selectIds[FleetType.Submarine][iter_72_1] or 0
		local var_72_4 = arg_72_0.getFleetById(var_72_3)

		var_72_0 = var_72_0 + (var_72_4 and var_72_4.getFleetAirDominanceValue() or 0)

	arg_72_0.UpdateASComparision(var_72_0, arg_72_0.suggestionValue)

def var_0_0.updateEliteASValue(arg_73_0):
	if arg_73_0.chapterASValue <= 0:
		arg_73_0.UpdateBannedAS()

		return

	local var_73_0 = getProxy(BayProxy)
	local var_73_1 = 0

	for iter_73_0, iter_73_1 in ipairs(arg_73_0.eliteFleetList):
		local var_73_2 = {}

		for iter_73_2, iter_73_3 in pairs(arg_73_0.eliteCommanderList[iter_73_0]):
			var_73_2[iter_73_2] = getProxy(CommanderProxy).RawGetCommanderById(iter_73_3)

		for iter_73_4, iter_73_5 in ipairs(iter_73_1):
			var_73_1 = var_73_1 + calcAirDominanceValue(var_73_0.RawGetShipById(iter_73_5), var_73_2)

	arg_73_0.UpdateASComparision(var_73_1, arg_73_0.suggestionValue)

def var_0_0.UpdateBannedAS(arg_74_0):
	local var_74_0 = arg_74_0.dropDown.Find("Airsupport")

	setText(var_74_0.Find("Value1"), "-")
	setText(var_74_0.Find("Value2"), "-")
	triggerToggle(arg_74_0.dropDownSide.Find("Layout/Item2/Dot"), True)

def var_0_0.UpdateASComparision(arg_75_0, arg_75_1, arg_75_2):
	arg_75_1 = math.floor(arg_75_1)

	local var_75_0 = arg_75_0.dropDown.Find("Airsupport")

	setText(var_75_0.Find("Text"), i18n("level_scene_title_word_3"))

	local var_75_1 = arg_75_2 < arg_75_1

	setText(var_75_0.Find("Value1"), setColorStr(arg_75_1, var_75_1 and "#51FF55" or COLOR_WHITE))
	setText(var_75_0.Find("Value2"), arg_75_2)
	triggerToggle(arg_75_0.dropDownSide.Find("Layout/Item2/Dot"), var_75_1)

def var_0_0.UpdateSonarRange(arg_76_0):
	for iter_76_0 = 1, 2:
		local var_76_0 = arg_76_0.selectIds[FleetType.Normal][iter_76_0] or 0
		local var_76_1 = arg_76_0.getFleetById(var_76_0)
		local var_76_2 = var_76_1 and math.floor(var_76_1.GetFleetSonarRange()) or 0

		arg_76_0.UpdateSonarRangeValues(iter_76_0, var_76_2)

def var_0_0.UpdateEliteSonarRange(arg_77_0):
	for iter_77_0 = 1, 2:
		local var_77_0 = arg_77_0.eliteFleetList[iter_77_0]
		local var_77_1 = {}

		for iter_77_1, iter_77_2 in pairs(arg_77_0.eliteCommanderList[iter_77_0]):
			table.insert(var_77_1, {
				pos = iter_77_1,
				id = iter_77_2
			})

		local var_77_2 = TypedFleet.New({
			ship_list = var_77_0,
			commanders = var_77_1,
			fleetType = FleetType.Normal
		})
		local var_77_3 = var_77_2 and math.floor(var_77_2.GetFleetSonarRange()) or 0

		arg_77_0.UpdateSonarRangeValues(iter_77_0, var_77_3)

def var_0_0.UpdateSonarRangeValues(arg_78_0, arg_78_1, arg_78_2):
	local var_78_0 = arg_78_0.dropDownSide.Find("Layout/Item3/Values")

	setText(var_78_0.GetChild(arg_78_1 - 1), arg_78_2)

def var_0_0.clearFleet(arg_79_0, arg_79_1):
	local var_79_0 = arg_79_0.findTF(TeamType.Main, arg_79_1)
	local var_79_1 = arg_79_0.findTF(TeamType.Vanguard, arg_79_1)
	local var_79_2 = arg_79_0.findTF(TeamType.Submarine, arg_79_1)

	if var_79_0:
		removeAllChildren(var_79_0)

	if var_79_1:
		removeAllChildren(var_79_1)

	if var_79_2:
		removeAllChildren(var_79_2)

def var_0_0.clear(arg_80_0):
	arg_80_0.contextData.tabIndex = None
	arg_80_0.duties = None

def var_0_0.onCancelHard(arg_81_0, arg_81_1):
	if arg_81_1:
		arg_81_0.emit(LevelMediator2.ON_UPDATE_CUSTOM_FLEET, arg_81_0.chapter)

	arg_81_0.emit(LevelUIConst.HIDE_FLEET_EDIT)

def var_0_0.setHardShipVOs(arg_82_0, arg_82_1):
	arg_82_0.shipVOs = arg_82_1

def var_0_0.setOnHard(arg_83_0, arg_83_1):
	arg_83_0.chapter = arg_83_1
	arg_83_0.mode = var_0_2.EDIT
	arg_83_0.propetyLimitation = arg_83_0.chapter.getConfig("property_limitation")
	arg_83_0.eliteFleetList = arg_83_0.chapter.getEliteFleetList()
	arg_83_0.chapterASValue = arg_83_0.chapter.getConfig("air_dominance")
	arg_83_0.suggestionValue = arg_83_0.chapter.getConfig("best_air_dominance")
	arg_83_0.eliteCommanderList = arg_83_0.chapter.getEliteFleetCommanders()
	arg_83_0.typeLimitations = arg_83_0.chapter.getConfig("limitation")

	arg_83_0.SetDutyTabEnabled(arg_83_1.isLoop())

	local var_83_0 = arg_83_0.getLimitNums(FleetType.Support) > 0

	setActive(arg_83_0.supportFleetHelp, var_83_0)

	arg_83_0.displayMode = var_83_0 and var_0_3.ADDITION_SUPPORT or var_0_3.NORMAL

	arg_83_0.SwitchDisplayMode()

	arg_83_0.duties = {}

	local var_83_1 = PlayerPrefs.GetInt("lastFleetDuty_" .. (arg_83_0.chapter.id or 0), 0)

	if var_83_1 > 0:
		local var_83_2 = bit.band(var_83_1, 255)
		local var_83_3 = bit.rshift(var_83_1, 8)
		local var_83_4 = bit.band(var_83_3, 255)

		if var_83_2 > 0 and var_83_4 > 0:
			arg_83_0.duties[var_83_2] = var_83_4

	onButton(arg_83_0, arg_83_0.btnGo, function()
		local var_84_0 = "chapter_autofight_flag_" .. arg_83_0.chapter.id
		local var_84_1 = arg_83_0.chapter
		local var_84_2
		local var_84_3

		seriesAsync({
			function(arg_85_0)
				local var_85_0 = PlayerPrefs.GetInt("autoFight_firstUse_sp", 0) == 1

				if not (PlayerPrefs.GetInt(var_84_0, 1) == 1) or not arg_83_0.getSPItem() or var_85_0:
					return arg_85_0()

				PlayerPrefs.SetInt("autoFight_firstUse_sp", 1)
				PlayerPrefs.Save()

				local function var_85_1()
					arg_83_0.clearSPBuff()

				arg_83_0.emit(LevelUIConst.HANDLE_SHOW_MSG_BOX, {
					hideNo = True,
					content = i18n("autofight_special_operation_tip"),
					onYes = var_85_1,
					onNo = var_85_1
				}),
			function(arg_87_0)
				var_84_2 = arg_83_0.chapter.GetActiveSPItemID()
				var_84_3 = arg_83_0.chapter.isLoop() and arg_83_0.GetOrderedDuties() or None

				arg_83_0.clear()
				arg_83_0.onCancelHard()
				arg_87_0(),
			function(arg_88_0)
				local var_88_0 = PlayerPrefs.GetInt(var_84_0, 1) == 1
				local var_88_1 = LevelMediator2.ON_ELITE_TRACKING
				local var_88_2 = packEx(var_84_1.id, var_84_1.loopFlag, var_84_2, var_84_3, var_88_0)

				if pg.m02.retrieveMediator(LevelMediator2.__cname):
					pg.m02.sendNotification(var_88_1, var_88_2)

					return

				local var_88_3 = getProxy(ContextProxy).getContextByMediator(LevelMediator2)

				if var_88_3:
					var_88_3.extendData({
						ToTrackingData = {
							var_88_1,
							var_88_2
						}
					})
		}), SFX_UI_WEIGHANCHOR_GO)
	setActive(arg_83_0.btnMultiple, AutoBotCommand.autoBotSatisfied() and arg_83_0.chapter.isLoop())
	onButton(arg_83_0, arg_83_0.btnMultiple, function()
		local var_89_0 = arg_83_0.getSPItem()
		local var_89_1 = arg_83_0.GetOrderedDuties()

		arg_83_0.emit(LevelUIConst.OPEN_ELITE_CONTINUOUS_WINDOW, arg_83_0.chapter, var_89_0, var_89_1), SFX_PANEL)
	onButton(arg_83_0, arg_83_0.btnASHelp, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("help_battle_ac")
		}), SFX_UI_CLICK)
	onButton(arg_83_0, arg_83_0.btnBack, function()
		arg_83_0.clear()
		arg_83_0.onCancelHard(True), SFX_CANCEL)
	onButton(arg_83_0, arg_83_0._tf.Find("bg"), function()
		arg_83_0.clear()
		arg_83_0.onCancelHard(True), SFX_CANCEL)
	onToggle(arg_83_0, arg_83_0.commanderToggle, function(arg_93_0)
		if arg_93_0:
			arg_83_0.contextData.tabIndex = var_0_0.TabIndex.Commander

			arg_83_0.flush(), SFX_PANEL)
	onToggle(arg_83_0, arg_83_0.formationToggle, function(arg_94_0)
		if arg_94_0:
			arg_83_0.contextData.tabIndex = var_0_0.TabIndex.Formation

			arg_83_0.flush(), SFX_PANEL)
	onToggle(arg_83_0, arg_83_0.dutyToggle, function(arg_95_0)
		if arg_95_0:
			arg_83_0.contextData.tabIndex = var_0_0.TabIndex.Duty

			arg_83_0.flush(), SFX_UI_TAG)
	onToggle(arg_83_0, arg_83_0.adjustmentToggle, function(arg_96_0)
		if arg_96_0:
			arg_83_0.contextData.tabIndex = var_0_0.TabIndex.Adjustment

			arg_83_0.flush(), SFX_PANEL)
	setActive(arg_83_0.formationToggle, True)
	setActive(arg_83_0.commanderToggle, arg_83_0.openedCommanerSystem)
	setActive(arg_83_0.dutyToggle, arg_83_0.dutyTabEnabled)
	setActive(arg_83_0.adjustmentToggle, True)
	arg_83_0.flush()

def var_0_0.flush(arg_97_0):
	arg_97_0.updateEliteLimit()
	arg_97_0.updateEliteASValue()

	arg_97_0.lastFleetVaildStatus = arg_97_0.lastFleetVaildStatus or {}

	local var_97_0 = {
		not arg_97_0.IsListOfFleetEmpty(1) or None,
		not arg_97_0.IsListOfFleetEmpty(2) or None
	}

	if arg_97_0.dutyTabEnabled and table.getCount(arg_97_0.lastFleetVaildStatus) == 2 and table.getCount(var_97_0) == 1:
		pg.TipsMgr.GetInstance().ShowTips(i18n("autofight_change_tip"))

	arg_97_0.lastFleetVaildStatus = var_97_0

	arg_97_0.updateEliteFleets()
	arg_97_0.UpdateEliteSonarRange()
	arg_97_0.UpdateEliteInvestigation()

def var_0_0.updateEliteLimit(arg_98_0):
	setActive(arg_98_0.toggleMask, False)
	setActive(arg_98_0.tfLimit, False)
	setActive(arg_98_0.tfLimitTips, #arg_98_0.propetyLimitation == 0)
	setActive(arg_98_0.tfLimitElite, #arg_98_0.propetyLimitation > 0)
	setActive(arg_98_0.tfLimitSubTip, #arg_98_0.propetyLimitation > 0)

	if #arg_98_0.propetyLimitation > 0:
		local var_98_0, var_98_1 = arg_98_0.chapter.IsPropertyLimitationSatisfy()
		local var_98_2 = UIItemList.New(arg_98_0.tfLimitContainer, arg_98_0.tfLimitContainer.GetChild(0))

		var_98_2.make(function(arg_99_0, arg_99_1, arg_99_2)
			arg_99_1 = arg_99_1 + 1

			if arg_99_0 == UIItemList.EventUpdate:
				local var_99_0 = arg_98_0.propetyLimitation[arg_99_1]
				local var_99_1, var_99_2, var_99_3, var_99_4 = unpack(var_99_0)

				if var_98_0[arg_99_1] == 1:
					arg_98_0.findTF("Text", arg_99_2).GetComponent(typeof(Text)).color = Color.New(1, 0.9607843137254902, 0.5019607843137255)
				else
					arg_98_0.findTF("Text", arg_99_2).GetComponent(typeof(Text)).color = Color.New(0.9568627450980393, 0.30196078431372547, 0.30196078431372547)

				setActive(arg_99_2, True)

				local var_99_5 = (AttributeType.EliteCondition2Name(var_99_1, var_99_4) .. AttributeType.eliteConditionCompareTip(var_99_2) .. var_99_3) .. "（" .. var_98_1[var_99_1] .. "）"

				setText(arg_98_0.findTF("Text", arg_99_2), var_99_5))
		var_98_2.align(#arg_98_0.propetyLimitation)
		setActive(arg_98_0.tfLimitSubTip, arg_98_0.chapter.getConfig("submarine_num") > 0)

	local var_98_3 = arg_98_0.chapter.isLoop() and arg_98_0.chapter.getConfig("use_oil_limit") or {}

	setActive(arg_98_0.rtCostLimit, #var_98_3 > 0)
	setText(arg_98_0.rtCostLimit.Find("text"), i18n("formationScene_use_oil_limit_tip"))

	if #var_98_3 > 0:
		setActive(arg_98_0.rtCostLimit.Find("cost_noraml"), var_98_3[1] > 0)
		setText(arg_98_0.rtCostLimit.Find("cost_noraml/Text"), string.format("%s(%d)", i18n("formationScene_use_oil_limit_enemy"), var_98_3[1]))
		setActive(arg_98_0.rtCostLimit.Find("cost_boss"), var_98_3[2] > 0)
		setText(arg_98_0.rtCostLimit.Find("cost_boss/Text"), string.format("%s(%d)", i18n("formationScene_use_oil_limit_flagship"), var_98_3[2]))
		setActive(arg_98_0.rtCostLimit.Find("cost_sub"), var_98_3[3] > 0)
		setText(arg_98_0.rtCostLimit.Find("cost_sub/Text"), string.format("%s(%d)", i18n("formationScene_use_oil_limit_submarine"), var_98_3[3]))

def var_0_0.initAddButton(arg_100_0, arg_100_1, arg_100_2, arg_100_3, arg_100_4):
	local var_100_0 = arg_100_0.eliteFleetList[arg_100_4]
	local var_100_1 = {}
	local var_100_2 = {}

	for iter_100_0, iter_100_1 in ipairs(var_100_0):
		var_100_1[arg_100_0.shipVOs[iter_100_1]] = True

		if arg_100_2 == arg_100_0.shipVOs[iter_100_1].getTeamType():
			table.insert(var_100_2, iter_100_1)

	local var_100_3 = findTF(arg_100_1, arg_100_2)

	removeAllChildren(var_100_3)

	local var_100_4 = 0
	local var_100_5 = False
	local var_100_6 = 0

	arg_100_3 = var_0_0.sortTeamLimitation(arg_100_3)

	local var_100_7 = var_100_3.GetComponent("ContentSizeFitter")
	local var_100_8 = var_100_3.GetComponent("HorizontalLayoutGroup")

	var_100_7.enabled = True
	var_100_8.enabled = True
	arg_100_0.isDraging = False

	for iter_100_2 = 1, 3:
		local var_100_9
		local var_100_10
		local var_100_11
		local var_100_12 = var_100_2[iter_100_2] and arg_100_0.shipVOs[var_100_2[iter_100_2]] or None

		if var_100_12:
			for iter_100_3, iter_100_4 in ipairs(arg_100_3):
				if ShipType.ContainInLimitBundle(iter_100_4, var_100_12.getShipType()):
					var_100_10 = var_100_12
					var_100_11 = iter_100_4

					table.remove(arg_100_3, iter_100_3)

					var_100_5 = var_100_5 or iter_100_4 != 0

					break
		else
			var_100_11 = arg_100_3[1]

			table.remove(arg_100_3, 1)

		if var_100_11 == 0:
			var_100_6 = var_100_6 + 1

		local var_100_13 = var_100_10 and cloneTplTo(arg_100_0.tfShipTpl, var_100_3) or cloneTplTo(arg_100_0.tfEmptyTpl, var_100_3)

		setActive(var_100_13, True)

		if var_100_10:
			updateShip(var_100_13, var_100_10)
			setActive(arg_100_0.findTF("event_block", var_100_13), var_100_10.getFlag("inEvent"))

			var_100_1[var_100_10] = True
		else
			var_100_4 = var_100_4 + 1

		setActive(arg_100_0.findTF("ship_type", var_100_13), var_100_11 and var_100_11 != 0)

		if var_100_11 and var_100_11 != 0:
			if type(var_100_11) == "number":
				local var_100_14 = GetSpriteFromAtlas("shiptype", ShipType.Type2CNLabel(var_100_11))

				setImageSprite(arg_100_0.findTF("ship_type", var_100_13), var_100_14, True)
			elif type(var_100_11) == "string":
				local var_100_15 = GetSpriteFromAtlas("shiptype", ShipType.BundleType2CNLabel(var_100_11))

				setImageSprite(arg_100_0.findTF("ship_type", var_100_13), var_100_15, True)

		local var_100_16 = _.map(var_100_0, function(arg_101_0)
			return arg_100_0.shipVOs[arg_101_0])

		table.sort(var_100_16, function(arg_102_0, arg_102_1)
			return var_0_1[arg_102_0.getTeamType()] < var_0_1[arg_102_1.getTeamType()] or var_0_1[arg_102_0.getTeamType()] == var_0_1[arg_102_1.getTeamType()] and table.indexof(var_100_0, arg_102_0.id) < table.indexof(var_100_0, arg_102_1.id))

		local var_100_17 = GetOrAddComponent(var_100_13, typeof(UILongPressTrigger))

		var_100_17.onLongPressed.RemoveAllListeners()

		if var_100_10 and arg_100_0.contextData.tabIndex != var_0_0.TabIndex.Adjustment:
			var_100_17.onLongPressed.AddListener(function()
				arg_100_0.onCancelHard(True)
				arg_100_0.emit(LevelMediator2.ON_FLEET_SHIPINFO, {
					shipId = var_100_10.id,
					shipVOs = var_100_16,
					chapter = arg_100_0.chapter
				}))

		local var_100_18 = GetOrAddComponent(var_100_13, "EventTriggerListener")

		var_100_18.RemovePointClickFunc()
		var_100_18.AddPointClickFunc(function(arg_104_0, arg_104_1)
			if arg_104_0 != var_100_13.gameObject:
				return

			if arg_100_0.isDraging:
				return

			arg_100_0.onCancelHard()
			arg_100_0.emit(LevelMediator2.ON_ELITE_OEPN_DECK, {
				shipType = var_100_11,
				fleet = var_100_1,
				chapter = arg_100_0.chapter,
				shipVO = var_100_10,
				fleetIndex = arg_100_4,
				teamType = arg_100_2
			}))
		var_100_18.RemoveBeginDragFunc()
		var_100_18.RemoveDragFunc()
		var_100_18.RemoveDragEndFunc()

		if var_100_10 and arg_100_0.contextData.tabIndex == var_0_0.TabIndex.Adjustment:
			local var_100_19 = var_100_13.rect.width * 0.5
			local var_100_20 = {}
			local var_100_21 = {}

			var_100_18.AddBeginDragFunc(function(arg_105_0, arg_105_1)
				if arg_105_0 != var_100_13.gameObject:
					return

				if arg_100_0.isDraging:
					return

				arg_100_0.isDraging = True
				var_100_7.enabled = False
				var_100_8.enabled = False

				for iter_105_0 = 1, 3:
					local var_105_0 = var_100_3.GetChild(iter_105_0 - 1)

					if var_100_13 == var_105_0:
						arg_100_0.dragIndex = iter_105_0

					var_100_20[iter_105_0] = var_105_0.anchoredPosition
					var_100_21[iter_105_0] = var_105_0)
			var_100_18.AddDragFunc(function(arg_106_0, arg_106_1)
				if arg_106_0 != var_100_13.gameObject:
					return

				if not arg_100_0.isDraging:
					return

				local var_106_0 = var_100_13.localPosition

				var_106_0.x = arg_100_0.change2ScrPos(var_100_13.parent, arg_106_1.position).x
				var_106_0.x = math.clamp(var_106_0.x, var_100_20[1].x, var_100_20[3].x)
				var_100_13.localPosition = var_106_0

				local var_106_1 = 1

				for iter_106_0 = 1, 3:
					if var_100_13 != var_100_21[iter_106_0] and var_100_13.localPosition.x > var_100_21[iter_106_0].localPosition.x + (var_106_1 < arg_100_0.dragIndex and 1.1 or -1.1) * var_100_19:
						var_106_1 = var_106_1 + 1

				if arg_100_0.dragIndex != var_106_1:
					local var_106_2 = var_106_1 < arg_100_0.dragIndex and -1 or 1

					while arg_100_0.dragIndex != var_106_1:
						local var_106_3 = arg_100_0.dragIndex
						local var_106_4 = arg_100_0.dragIndex + var_106_2

						var_100_2[var_106_3], var_100_2[var_106_4] = var_100_2[var_106_4], var_100_2[var_106_3]
						var_100_21[var_106_3], var_100_21[var_106_4] = var_100_21[var_106_4], var_100_21[var_106_3]
						arg_100_0.dragIndex = arg_100_0.dragIndex + var_106_2

					for iter_106_1 = 1, 3:
						if var_100_13 != var_100_21[iter_106_1]:
							var_100_21[iter_106_1].anchoredPosition = var_100_20[iter_106_1])
			var_100_18.AddDragEndFunc(function(arg_107_0, arg_107_1)
				if arg_107_0 != var_100_13.gameObject:
					return

				if not arg_100_0.isDraging:
					return

				arg_100_0.isDraging = False

				for iter_107_0 = 1, 3:
					if not var_100_2[iter_107_0]:
						for iter_107_1 = iter_107_0 + 1, 3:
							if var_100_2[iter_107_1]:
								var_100_2[iter_107_0], var_100_2[iter_107_1] = var_100_2[iter_107_1], var_100_2[iter_107_0]
								var_100_21[iter_107_0], var_100_21[iter_107_1] = var_100_21[iter_107_1], var_100_21[iter_107_0]

					if var_100_2[iter_107_0]:
						table.removebyvalue(var_100_0, var_100_2[iter_107_0])
						table.insert(var_100_0, var_100_2[iter_107_0])
					else
						break

				for iter_107_2 = 1, 3:
					var_100_21[iter_107_2].SetSiblingIndex(iter_107_2 - 1)

				var_100_7.enabled = True
				var_100_8.enabled = True
				arg_100_0.dragIndex = None

				arg_100_0.emit(LevelMediator2.ON_ELITE_ADJUSTMENT, arg_100_0.chapter))

	if (var_100_5 == True or var_100_6 == 3) and var_100_4 != 3:
		return True
	else
		return False

def var_0_0.change2ScrPos(arg_108_0, arg_108_1, arg_108_2):
	local var_108_0 = pg.UIMgr.GetInstance().overlayCameraComp

	return (LuaHelper.ScreenToLocal(arg_108_1, arg_108_2, var_108_0))

def var_0_0.updateEliteFleets(arg_109_0):
	for iter_109_0, iter_109_1 in pairs(arg_109_0.tfFleets):
		for iter_109_2 = 1, #iter_109_1:
			arg_109_0.UpdateEliteFleet(iter_109_0, iter_109_2)

	arg_109_0.RefreshDutyBar()

def var_0_0.UpdateEliteFleet(arg_110_0, arg_110_1, arg_110_2):
	local var_110_0 = arg_110_0.contextData.tabIndex == var_0_0.TabIndex.Formation
	local var_110_1 = arg_110_0.contextData.tabIndex == var_0_0.TabIndex.Commander
	local var_110_2 = arg_110_0.contextData.tabIndex == var_0_0.TabIndex.Duty
	local var_110_3 = arg_110_0.contextData.tabIndex == var_0_0.TabIndex.Adjustment
	local var_110_4 = arg_110_2 <= arg_110_0.getLimitNums(arg_110_1)
	local var_110_5 = arg_110_0.tfFleets[arg_110_1][arg_110_2]
	local var_110_6 = findTF(var_110_5, "bg/name")
	local var_110_7 = arg_110_0.findTF("btn_select", var_110_5)
	local var_110_8 = arg_110_0.findTF("btn_recom", var_110_5)
	local var_110_9 = arg_110_0.findTF("btn_clear", var_110_5)
	local var_110_10 = arg_110_0.findTF("blank", var_110_5)
	local var_110_11 = arg_110_0.findTF("selected", var_110_5)
	local var_110_12 = arg_110_0.findTF("commander", var_110_5)
	local var_110_13 = var_110_5.Find("adjustment_flag")

	setActive(var_110_7, False)

	local var_110_14 = arg_110_0.findTF(TeamType.Main, var_110_5)
	local var_110_15 = arg_110_0.findTF(TeamType.Vanguard, var_110_5)
	local var_110_16 = arg_110_0.findTF(TeamType.Submarine, var_110_5)
	local var_110_17 = arg_110_0.findTF(TeamType.Support, var_110_5)

	if not var_110_4:
		setActive(var_110_9, False)
		setActive(var_110_8, False)
		setActive(var_110_12, False)
		setActive(var_110_13, False)
		setActive(var_110_10, True)
		setActive(var_110_11, False)
		setText(var_110_6, "")

		if arg_110_1 == FleetType.Normal:
			setActive(var_110_14, False)
			setActive(var_110_15, False)
		elif arg_110_1 == FleetType.Submarine:
			setActive(var_110_16, False)
		elif arg_110_1 == FleetType.Support:
			setActive(var_110_17, False)

		return

	local var_110_18 = arg_110_1 == FleetType.Support

	setActive(var_110_9, var_110_0)
	setActive(var_110_8, var_110_0)
	setActive(var_110_12, var_110_1 and not var_110_18)
	setActive(var_110_13, var_110_3)
	setActive(var_110_10, var_110_2 or var_110_3 or var_110_1 and var_110_18)

	local var_110_19 = arg_110_2

	if arg_110_1 == FleetType.Normal:
		setText(var_110_6, Fleet.DEFAULT_NAME[arg_110_2])
		setActive(var_110_14, True)
		setActive(var_110_15, True)
	elif arg_110_1 == FleetType.Submarine:
		var_110_19 = 3

		setText(var_110_6, Fleet.DEFAULT_NAME[Fleet.SUBMARINE_FLEET_ID + arg_110_2 - 1])
		setActive(var_110_16, True)
	elif arg_110_1 == FleetType.Support:
		var_110_19 = 4

		setText(var_110_6, "")
		setActive(var_110_17, True)

	local var_110_20 = 6

	if arg_110_1 == FleetType.Normal:
		local var_110_21 = arg_110_0.typeLimitations[arg_110_2]
		local var_110_22 = var_110_21[1]
		local var_110_23 = var_110_21[2]
		local var_110_24 = arg_110_0.initAddButton(var_110_5, TeamType.Main, var_110_22, var_110_19)
		local var_110_25 = arg_110_0.initAddButton(var_110_5, TeamType.Vanguard, var_110_23, var_110_19)

		setActive(var_110_11, var_110_24 and var_110_25)
	elif arg_110_1 == FleetType.Submarine:
		var_110_20 = 3

		local var_110_26 = arg_110_0.initAddButton(var_110_5, TeamType.Submarine, {
			0,
			0,
			0
		}, var_110_19)

		setActive(var_110_11, var_110_26)
	elif arg_110_1 == FleetType.Support:
		var_110_20 = 3

		local var_110_27 = arg_110_0.initSupportAddButton(var_110_5, TeamType.Support, {
			"hang",
			"hang",
			"hang"
		})

		setActive(var_110_11, arg_110_0.mode == var_0_2.EDIT and var_110_27)

	if not var_110_18:
		arg_110_0.initCommander(var_110_19, var_110_12, arg_110_0.chapter)

	onButton(arg_110_0, var_110_9, function()
		if #(not var_110_18 and arg_110_0.eliteFleetList[var_110_19] or arg_110_0.supportFleet) == 0:
			return

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("battle_preCombatLayer_clear_confirm"),
			def onYes:()
				if not var_110_18:
					arg_110_0.emit(LevelMediator2.ON_ELITE_CLEAR, {
						index = var_110_19,
						chapterVO = arg_110_0.chapter
					})
				else
					arg_110_0.emit(LevelMediator2.ON_SUPPORT_CLEAR, {
						index = var_110_19,
						chapterVO = arg_110_0.chapter
					})
		}))
	onButton(arg_110_0, var_110_8, function()
		local var_113_0 = #(not var_110_18 and arg_110_0.eliteFleetList[var_110_19] or arg_110_0.supportFleet)

		if var_113_0 == var_110_20:
			return

		seriesAsync({
			function(arg_114_0)
				if var_113_0 == 0:
					return arg_114_0()

				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("battle_preCombatLayer_auto_confirm"),
					onYes = arg_114_0
				}),
			function()
				if not var_110_18:
					arg_110_0.emit(LevelMediator2.ON_ELITE_RECOMMEND, {
						index = var_110_19,
						chapterVO = arg_110_0.chapter
					})
				else
					arg_110_0.emit(LevelMediator2.ON_SUPPORT_RECOMMEND, {
						index = var_110_19,
						chapterVO = arg_110_0.chapter
					})
		}))

def var_0_0.initCommander(arg_116_0, arg_116_1, arg_116_2, arg_116_3):
	local var_116_0 = arg_116_3.getEliteFleetCommanders()[arg_116_1]

	for iter_116_0 = 1, 2:
		local var_116_1 = var_116_0[iter_116_0]
		local var_116_2

		if var_116_1:
			var_116_2 = getProxy(CommanderProxy).getCommanderById(var_116_1)

		local var_116_3 = arg_116_2.Find("pos" .. iter_116_0)
		local var_116_4 = var_116_3.Find("add")
		local var_116_5 = var_116_3.Find("info")

		setActive(var_116_4, not var_116_2)
		setActive(var_116_5, var_116_2)

		if var_116_2:
			local var_116_6 = Commander.rarity2Frame(var_116_2.getRarity())

			setImageSprite(var_116_5.Find("frame"), GetSpriteFromAtlas("weaponframes", "commander_" .. var_116_6))
			GetImageSpriteFromAtlasAsync("CommanderHrz/" .. var_116_2.getPainting(), "", var_116_5.Find("mask/icon"))

		local var_116_7 = arg_116_3.wrapEliteFleet(arg_116_1)

		onButton(arg_116_0, var_116_4, function()
			arg_116_0.emit(LevelUIConst.OPEN_COMMANDER_PANEL, var_116_7, arg_116_3, arg_116_1), SFX_PANEL)
		onButton(arg_116_0, var_116_5, function()
			arg_116_0.emit(LevelUIConst.OPEN_COMMANDER_PANEL, var_116_7, arg_116_3, arg_116_1), SFX_PANEL)

def var_0_0.initSupportAddButton(arg_119_0, arg_119_1, arg_119_2, arg_119_3):
	local var_119_0 = {}
	local var_119_1 = {}

	for iter_119_0, iter_119_1 in ipairs(arg_119_0.supportFleet):
		var_119_0[arg_119_0.shipVOs[iter_119_1]] = True

		table.insert(var_119_1, iter_119_1)

	local var_119_2 = findTF(arg_119_1, arg_119_2)

	removeAllChildren(var_119_2)

	local var_119_3 = 0
	local var_119_4 = False
	local var_119_5 = 0

	arg_119_3 = var_0_0.sortTeamLimitation(arg_119_3)

	for iter_119_2 = 1, 3:
		local var_119_6
		local var_119_7
		local var_119_8 = var_119_1[iter_119_2] and arg_119_0.shipVOs[var_119_1[iter_119_2]] or None

		if var_119_8:
			for iter_119_3, iter_119_4 in ipairs(arg_119_3):
				if ShipType.ContainInLimitBundle(iter_119_4, var_119_8.getShipType()):
					var_119_6 = var_119_8
					var_119_7 = iter_119_4

					table.remove(arg_119_3, iter_119_3)

					var_119_4 = var_119_4 or iter_119_4 != 0

					break
		else
			var_119_7 = arg_119_3[1]

			table.remove(arg_119_3, 1)

		if var_119_7 == 0:
			var_119_5 = var_119_5 + 1

		local var_119_9 = var_119_6 and cloneTplTo(arg_119_0.tfShipTpl, var_119_2) or cloneTplTo(arg_119_0.tfEmptyTpl, var_119_2)

		setActive(var_119_9, True)

		if var_119_6:
			updateShip(var_119_9, var_119_6)
			setActive(arg_119_0.findTF("event_block", var_119_9), var_119_6.getFlag("inEvent"))

			var_119_0[var_119_6] = True
		else
			var_119_3 = var_119_3 + 1

		setActive(arg_119_0.findTF("ship_type", var_119_9), var_119_7 and var_119_7 != 0)

		if var_119_7 and var_119_7 != 0:
			if type(var_119_7) == "number":
				local var_119_10 = GetSpriteFromAtlas("shiptype", ShipType.Type2CNLabel(var_119_7))

				setImageSprite(arg_119_0.findTF("ship_type", var_119_9), var_119_10, True)
			elif type(var_119_7) == "string":
				local var_119_11 = GetSpriteFromAtlas("shiptype", ShipType.BundleType2CNLabel(var_119_7))

				setImageSprite(arg_119_0.findTF("ship_type", var_119_9), var_119_11, True)

		local var_119_12 = _.map(arg_119_0.supportFleet, function(arg_120_0)
			return arg_119_0.shipVOs[arg_120_0])
		local var_119_13 = GetOrAddComponent(var_119_9, typeof(UILongPressTrigger))

		var_119_13.onLongPressed.RemoveAllListeners()

		if var_119_6 and arg_119_0.contextData.tabIndex != var_0_0.TabIndex.Adjustment:
			var_119_13.onLongPressed.AddListener(function()
				arg_119_0.onCancelSupport(True)
				arg_119_0.emit(LevelMediator2.ON_SUPPORT_SHIPINFO, {
					shipId = var_119_6.id,
					shipVOs = var_119_12,
					chapter = arg_119_0.chapter
				}))

		local var_119_14 = GetOrAddComponent(var_119_9, "EventTriggerListener")

		var_119_14.RemovePointClickFunc()
		var_119_14.AddPointClickFunc(function(arg_122_0, arg_122_1)
			if arg_122_0 != var_119_9.gameObject:
				return

			if arg_119_0.isDraging:
				return

			arg_119_0.onCancelSupport()
			arg_119_0.emit(LevelMediator2.ON_SUPPORT_OPEN_DECK, {
				shipType = var_119_7,
				fleet = var_119_0,
				chapter = arg_119_0.chapter,
				shipVO = var_119_6
			}))
		var_119_14.RemoveBeginDragFunc()
		var_119_14.RemoveDragFunc()
		var_119_14.RemoveDragEndFunc()

	if (var_119_4 == True or var_119_5 == 3) and var_119_3 != 3:
		return True
	else
		return False

def var_0_0.updateSpecialOperationTickets(arg_123_0, arg_123_1):
	arg_123_0.spOPTicketItems = arg_123_1 or {}

def var_0_0.getLegalSPBuffList(arg_124_0):
	local var_124_0 = arg_124_0.chapter.GetSpItems()

	return _.map(var_124_0, function(arg_125_0)
		return Chapter.GetSPBuffByItem(arg_125_0.GetConfigID()))

def var_0_0.initSPOPView(arg_126_0):
	arg_126_0.spPanel = arg_126_0.btnSp.Find("sp_panel")
	arg_126_0.spItem = arg_126_0.btnSp.Find("item")
	arg_126_0.spDesc = arg_126_0.btnSp.Find("desc")
	arg_126_0.spCheckBox = arg_126_0.btnSp.Find("checkbox")
	arg_126_0.spCheckMark = arg_126_0.spCheckBox.Find("mark")
	arg_126_0.spTpl = arg_126_0.spPanel.Find("sp_tpl")
	arg_126_0.spContainer = arg_126_0.spPanel.Find("sp_container")
	arg_126_0.spItemEmptyBlock = arg_126_0.btnSp.Find("empty_block")

	setText(arg_126_0.spItemEmptyBlock, i18n("levelScene_select_noitem"))
	removeAllChildren(arg_126_0.spContainer)

	local var_126_0 = arg_126_0.getLegalSPBuffList()
	local var_126_1 = arg_126_0.chapter.GetActiveSPItemID()

	arg_126_0.setSPBtnFormByBuffCount()

	if #var_126_0 == 0:
		arg_126_0.clearSPBuff()
	elif #var_126_0 == 1:
		local var_126_2 = var_126_0[1]
		local var_126_3 = pg.benefit_buff_template[var_126_2]

		arg_126_0.setTicketInfo(arg_126_0.btnSp, var_126_3.benefit_condition)
		setText(arg_126_0.spDesc, var_126_3.desc)
		onButton(arg_126_0, arg_126_0.btnSp.Find("item"), function()
			arg_126_0.emit(BaseUI.ON_ITEM, tonumber(var_126_3.benefit_condition)))
		onButton(arg_126_0, arg_126_0.btnSp, function()
			local var_128_0 = Chapter.GetSPOperationItemCacheKey(arg_126_0.chapter.id)

			if arg_126_0.spCheckMark.gameObject.activeSelf:
				PlayerPrefs.SetInt(var_128_0, 0)
				arg_126_0.clearSPBuff()
			else
				arg_126_0.spItemID = tonumber(var_126_3.benefit_condition)

				PlayerPrefs.SetInt(var_128_0, arg_126_0.spItemID)
				pg.TipsMgr.GetInstance().ShowTips(i18n("levelScene_select_sp"))
				setActive(arg_126_0.spCheckMark, True))
		setActive(arg_126_0.spCheckMark, var_126_1 == 0)
		triggerButton(arg_126_0.btnSp)
	elif #var_126_0 > 1:
		setText(arg_126_0.spDesc, i18n("levelScene_select_SP_OP"))

		for iter_126_0, iter_126_1 in ipairs(var_126_0):
			local var_126_4 = cloneTplTo(arg_126_0.spTpl, arg_126_0.spContainer)

			setText(var_126_4.Find("desc"), iter_126_1.desc)
			arg_126_0.setTicketInfo(var_126_4, iter_126_1.benefit_condition)
			setActive(var_126_4.Find("block"), False)
			onButton(arg_126_0, var_126_4, function()
				arg_126_0.setSPBuffSelected(iter_126_1.id)
				setActive(arg_126_0.spPanel, False))

		onButton(arg_126_0, arg_126_0.btnSp, function()
			if arg_126_0.spPanel.gameObject.activeSelf:
				arg_126_0.clearSPBuff()

				local var_130_0 = Chapter.GetSPOperationItemCacheKey(arg_126_0.chapter.id)

				PlayerPrefs.SetInt(var_130_0, 0)
				setActive(arg_126_0.spPanel, False)
			else
				setActive(arg_126_0.spPanel, True)
				setActive(arg_126_0.btnSp.Find("item"), False)
				setText(arg_126_0.spDesc, i18n("levelScene_unselect_SP_OP")))

		if var_126_1 != 0:
			local var_126_5

			for iter_126_2, iter_126_3 in ipairs(var_126_0):
				if iter_126_3.id == Chapter.GetSPBuffByItem(var_126_1):
					var_126_5 = True

					break

			if var_126_5:
				local var_126_6 = Chapter.GetSPBuffByItem(var_126_1)

				arg_126_0.setSPBuffSelected(var_126_6)
			else
				arg_126_0.clearSPBuff()
		else
			arg_126_0.clearSPBuff()

	setActive(arg_126_0.spPanel, False)

def var_0_0.setSPBuffSelected(arg_131_0, arg_131_1):
	local var_131_0 = pg.benefit_buff_template[arg_131_1]

	arg_131_0.spItemID = tonumber(var_131_0.benefit_condition)

	arg_131_0.setTicketInfo(arg_131_0.btnSp, arg_131_0.spItemID)
	setText(arg_131_0.spDesc, var_131_0.desc)

	local var_131_1 = Chapter.GetSPOperationItemCacheKey(arg_131_0.chapter.id)

	PlayerPrefs.SetInt(var_131_1, arg_131_0.spItemID)

def var_0_0.clearSPBuff(arg_132_0):
	local var_132_0 = arg_132_0.getLegalSPBuffList()

	arg_132_0.spItemID = None

	arg_132_0.setSPBtnFormByBuffCount()

	if #var_132_0 == 0:
		setActive(arg_132_0.btnSp.Find("item"), False)
	elif #var_132_0 == 1:
		setActive(arg_132_0.btnSp.Find("item"), True)
		setActive(arg_132_0.spCheckMark, False)
	elif #var_132_0 > 1:
		setActive(arg_132_0.btnSp.Find("item"), False)
		setText(arg_132_0.spDesc, i18n("levelScene_select_SP_OP"))

def var_0_0.setSPBtnFormByBuffCount(arg_133_0):
	local var_133_0 = arg_133_0.getLegalSPBuffList()

	if #var_133_0 == 0:
		setActive(arg_133_0.spItemEmptyBlock, True)
		setActive(arg_133_0.spDesc, False)
		setActive(arg_133_0.spCheckBox, False)
		setActive(arg_133_0.btnSp.Find("add"), False)
	elif #var_133_0 == 1:
		setActive(arg_133_0.spItemEmptyBlock, False)
		setActive(arg_133_0.spDesc, True)
		setActive(arg_133_0.spCheckBox, True)
		setActive(arg_133_0.btnSp.Find("add"), False)
	elif #var_133_0 > 1:
		setActive(arg_133_0.spItemEmptyBlock, False)
		setActive(arg_133_0.spDesc, True)
		setActive(arg_133_0.spCheckBox, False)
		setActive(arg_133_0.btnSp.Find("add"), True)

def var_0_0.setTicketInfo(arg_134_0, arg_134_1, arg_134_2):
	local var_134_0

	arg_134_2 = tonumber(arg_134_2)

	for iter_134_0, iter_134_1 in ipairs(arg_134_0.spOPTicketItems):
		if arg_134_2 == iter_134_1.configId:
			var_134_0 = iter_134_1

			break

	if var_134_0:
		setText(arg_134_1.Find("item/count"), var_134_0.count)
		GetImageSpriteFromAtlasAsync(var_134_0.getConfig("icon"), "", arg_134_1.Find("item/icon"))
	else
		setText(arg_134_1.Find("item/count"), 0)
		GetImageSpriteFromAtlasAsync(Drop.New({
			type = DROP_TYPE_ITEM,
			id = arg_134_2
		}).getIcon(), "", arg_134_1.Find("item/icon"))

	setActive(arg_134_1.Find("item"), True)

def var_0_0.getSPItem(arg_135_0):
	return arg_135_0.spItemID

def var_0_0.SetDuty(arg_136_0, arg_136_1, arg_136_2):
	if not arg_136_2 or not arg_136_0.duties:
		return

	if arg_136_0.duties[arg_136_1] == arg_136_2:
		return

	arg_136_0.duties[arg_136_1] = arg_136_2
	arg_136_0.duties[3 - arg_136_1] = None

	arg_136_0.RefreshDutyBar()

def var_0_0.UpdateDuties(arg_137_0):
	if not arg_137_0.dutyTabEnabled:
		return

	local var_137_0 = 0
	local var_137_1 = 0

	for iter_137_0 = 1, 2:
		if not arg_137_0.IsListOfFleetEmpty(iter_137_0):
			var_137_0 = var_137_0 + 1
			var_137_1 = iter_137_0

	if var_137_0 == 0:
		table.clear(arg_137_0.duties)
	elif var_137_0 == 1:
		arg_137_0.duties[var_137_1] = ChapterFleet.DUTY_KILLALL
		arg_137_0.duties[3 - var_137_1] = None
	elif var_137_0 == 2:
		if arg_137_0.duties[1]:
			local var_137_2 = arg_137_0.duties[1]
			local var_137_3 = var_137_2 < 3 and 3 - var_137_2 or 7 - var_137_2

			arg_137_0.duties[2] = var_137_3
		elif arg_137_0.duties[2]:
			local var_137_4 = arg_137_0.duties[2]
			local var_137_5 = var_137_4 < 3 and 3 - var_137_4 or 7 - var_137_4

			arg_137_0.duties[1] = var_137_5
		else
			arg_137_0.duties[1] = ChapterFleet.DUTY_CLEANPATH
			arg_137_0.duties[2] = ChapterFleet.DUTY_KILLBOSS

	if var_137_1 != 0:
		local var_137_6 = "lastFleetDuty_" .. (arg_137_0.chapter.id or 0)
		local var_137_7 = 0
		local var_137_8 = 8

		for iter_137_1, iter_137_2 in ipairs({
			var_137_1,
			arg_137_0.duties[var_137_1]
		}):
			var_137_7 = var_137_7 + bit.lshift(iter_137_2, var_137_8 * (iter_137_1 - 1))

		PlayerPrefs.SetInt(var_137_6, var_137_7)
		PlayerPrefs.Save()

def var_0_0.RefreshDutyBar(arg_138_0):
	arg_138_0.UpdateDuties()
	arg_138_0.UpdateDutyBar()

def var_0_0.UpdateDutyBar(arg_139_0):
	local var_139_0 = arg_139_0.contextData.tabIndex == var_0_0.TabIndex.Duty

	for iter_139_0 = 1, 2:
		local var_139_1 = arg_139_0._tf.Find(string.format("panel/ShipList/fleet/%d/DutySelect", iter_139_0))

		setActive(var_139_1, var_139_0 and arg_139_0.duties[iter_139_0] != None)

	local var_139_2 = arg_139_0._tf.Find("panel/ShipList/sub/1/DutySelect")

	setActive(var_139_2, var_139_0 and not arg_139_0.IsListOfFleetEmpty(3))

	if not var_139_0:
		return

	for iter_139_1, iter_139_2 in pairs(arg_139_0.duties):
		for iter_139_3 = 1, 4:
			setActive(arg_139_0.dutyItems[iter_139_1][iter_139_3].Find("Checkmark"), iter_139_3 == iter_139_2)

	local var_139_3 = ys.Battle.BattleState.IsAutoSubActive()

	for iter_139_4 = 1, 2:
		local var_139_4 = arg_139_0.dutyItems[3][iter_139_4]

		setActive(var_139_4.Find("Checkmark"), iter_139_4 == 1 == var_139_3)

def var_0_0.GetOrderedDuties(arg_140_0):
	if not arg_140_0.duties:
		return

	arg_140_0.UpdateDuties()

	local var_140_0 = {}
	local var_140_1 = 1

	for iter_140_0 = 1, 2:
		if arg_140_0.duties[iter_140_0]:
			var_140_0[var_140_1] = arg_140_0.duties[iter_140_0]
			var_140_1 = var_140_1 + 1

	return var_140_0

def var_0_0.SetAutoSub(arg_141_0, arg_141_1):
	arg_141_1 = tobool(arg_141_1)

	if arg_141_1 == ys.Battle.BattleState.IsAutoSubActive():
		return

	if not AutoBotCommand.autoBotSatisfied():
		return

	pg.m02.sendNotification(GAME.AUTO_SUB, {
		isActiveSub = not arg_141_1
	})
	arg_141_0.UpdateDutyBar()

def var_0_0.GetValidFleets(arg_142_0, arg_142_1):
	if arg_142_0.mode == var_0_2.SELECT:
		local var_142_0 = {}
		local var_142_1 = arg_142_1 and {
			arg_142_1
		} or {
			FleetType.Normal,
			FleetType.Submarine
		}

		for iter_142_0, iter_142_1 in ipairs(var_142_1):
			local var_142_2 = arg_142_0.selectIds[iter_142_1]

			for iter_142_2, iter_142_3 in ipairs(var_142_2):
				if iter_142_3 > 0:
					table.insert(var_142_0, arg_142_0.fleets[iter_142_3])

		return var_142_0
	elif arg_142_0.mode == var_0_2.EDIT:
		local var_142_3 = {}
		local var_142_4
		local var_142_5

		if arg_142_1 == FleetType.Normal:
			var_142_4 = 1
			var_142_5 = 2
		elif arg_142_1 == FleetType.Submarine:
			var_142_4 = 3
			var_142_5 = 3
		elif not arg_142_1:
			var_142_4 = 1
			var_142_5 = 3

		for iter_142_4 = var_142_4, var_142_5:
			local var_142_6 = arg_142_0.eliteFleetList[iter_142_4]

			if #var_142_6 > 0:
				local var_142_7 = {}

				for iter_142_5, iter_142_6 in pairs(arg_142_0.eliteCommanderList[iter_142_4]):
					table.insert(var_142_7, {
						pos = iter_142_5,
						id = iter_142_6
					})

				local var_142_8 = TypedFleet.New({
					ship_list = var_142_6,
					commanders = var_142_7,
					fleetType = FleetType.Normal
				})

				table.insert(var_142_3, var_142_8)

		return var_142_3

def var_0_0.IsListOfFleetEmpty(arg_143_0, arg_143_1):
	if arg_143_1 > 0 and arg_143_1 < 3 and arg_143_1 > arg_143_0.getLimitNums(FleetType.Normal):
		return True
	elif arg_143_1 == 3 and arg_143_1 - 2 > arg_143_0.getLimitNums(FleetType.Submarine):
		return True

	if arg_143_0.mode == var_0_2.SELECT:
		local var_143_0

		if arg_143_1 > 0 and arg_143_1 < 3:
			var_143_0 = arg_143_0.selectIds[FleetType.Normal][arg_143_1] or 0
		elif arg_143_1 == 3:
			var_143_0 = arg_143_0.selectIds[FleetType.Submarine][arg_143_1 - 2] or 0

		return var_143_0 == 0
	elif arg_143_0.mode == var_0_2.EDIT:
		return #arg_143_0.eliteFleetList[arg_143_1] == 0

def var_0_0.GetListFleets(arg_144_0):
	local var_144_0 = {}
	local var_144_1 = arg_144_0.getLimitNums(FleetType.Normal)
	local var_144_2 = arg_144_0.getLimitNums(FleetType.Submarine)

	if arg_144_0.mode == var_0_2.SELECT:
		local var_144_3 = arg_144_0.selectIds[FleetType.Normal]

		for iter_144_0 = 1, var_144_1:
			local var_144_4 = var_144_3[iter_144_0] or 0

			var_144_0[iter_144_0] = var_144_4 > 0 and arg_144_0.fleets[var_144_4] or None

		local var_144_5 = arg_144_0.selectIds[FleetType.Submarine]

		for iter_144_1 = 1, var_144_2:
			local var_144_6 = var_144_5[iter_144_1] or 0

			var_144_0[iter_144_1 + var_144_1] = var_144_6 > 0 and arg_144_0.fleets[var_144_6] or None
	elif arg_144_0.mode == var_0_2.EDIT:
		local var_144_7 = {}

		for iter_144_2 = 1, var_144_1:
			table.insert(var_144_7, iter_144_2)

		for iter_144_3 = 1, var_144_2:
			table.insert(var_144_7, iter_144_3 + 2)

		for iter_144_4 = 1, #var_144_7:
			local var_144_8 = var_144_7[iter_144_4]
			local var_144_9
			local var_144_10 = arg_144_0.eliteFleetList[var_144_8]

			if #var_144_10 > 0:
				local var_144_11 = var_144_8 > 2 and FleetType.Submarine or FleetType.Normal
				local var_144_12 = {}

				for iter_144_5, iter_144_6 in pairs(arg_144_0.eliteCommanderList[var_144_8]):
					table.insert(var_144_12, {
						pos = iter_144_5,
						id = iter_144_6
					})

				var_144_9 = TypedFleet.New({
					ship_list = var_144_10,
					commanders = var_144_12,
					fleetType = var_144_11
				})

			var_144_0[iter_144_4] = var_144_9

	return var_144_0

def var_0_0.IsSelectMode(arg_145_0):
	return arg_145_0.mode == var_0_2.SELECT

def var_0_0.SwitchDisplayMode(arg_146_0):
	local var_146_0 = arg_146_0.displayMode == var_0_3.ADDITION_SUPPORT

	setActive(arg_146_0.findTF("panel/ShipList/Line"), not var_146_0)
	setActive(arg_146_0.findTF("panel/ShipList/support"), var_146_0)

	local var_146_1 = arg_146_0.findTF("panel/ShipList").GetComponent(typeof(VerticalLayoutGroup))
	local var_146_2 = var_146_1.padding

	var_146_2.top = var_146_0 and 9 or 20
	var_146_2.bottom = var_146_0 and 14 or 25
	var_146_1.padding = var_146_2
	var_146_1.spacing = var_146_0 and 13 or 20

def var_0_0.sortTeamLimitation(arg_147_0):
	arg_147_0 = Clone(arg_147_0)

	table.sort(arg_147_0, function(arg_148_0, arg_148_1)
		local var_148_0 = type(arg_148_0)
		local var_148_1 = type(arg_148_1)

		if var_148_0 == var_148_1:
			return var_148_1 < var_148_0
		elif arg_148_1 == 0 or var_148_1 == "string" and arg_148_0 != 0:
			return True
		else
			return False)

	return arg_147_0

return var_0_0
