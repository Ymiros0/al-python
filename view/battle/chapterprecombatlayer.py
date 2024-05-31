local var_0_0 = class("ChapterPreCombatLayer", import("..base.BaseUI"))
local var_0_1 = import("..ship.FormationUI")
local var_0_2 = {
	[99] = True
}

def var_0_0.getUIName(arg_1_0):
	return "ChapterPreCombatUI"

def var_0_0.ResUISettings(arg_2_0):
	return True

def var_0_0.init(arg_3_0):
	arg_3_0._startBtn = arg_3_0.findTF("right/start")
	arg_3_0._popup = arg_3_0.findTF("right/popup")
	arg_3_0._costText = arg_3_0.findTF("right/popup/Text")
	arg_3_0._costTip = arg_3_0.findTF("right/popup/tip")
	arg_3_0._extraCostBuffIcon = arg_3_0.findTF("right/operation_buff_icon")
	arg_3_0._backBtn = arg_3_0.findTF("top/back_btn")
	arg_3_0._moveLayer = arg_3_0.findTF("moveLayer")

	local var_3_0 = arg_3_0.findTF("middle")

	arg_3_0._mainGS = var_3_0.Find("gear_score/main/Text")
	arg_3_0._vanguardGS = var_3_0.Find("gear_score/vanguard/Text")

	setText(arg_3_0._mainGS, 0)
	setText(arg_3_0._vanguardGS, 0)

	arg_3_0._gridTFs = {
		vanguard = {},
		main = {}
	}
	arg_3_0._gridFrame = var_3_0.Find("mask/GridFrame")

	for iter_3_0 = 1, 3:
		arg_3_0._gridTFs[TeamType.Vanguard][iter_3_0] = arg_3_0._gridFrame.Find("vanguard_" .. iter_3_0)
		arg_3_0._gridTFs[TeamType.Main][iter_3_0] = arg_3_0._gridFrame.Find("main_" .. iter_3_0)

	arg_3_0._heroContainer = var_3_0.Find("HeroContainer")
	arg_3_0._strategy = var_3_0.Find("strategy")

	setActive(arg_3_0._strategy, True)

	arg_3_0._spoilsContainer = arg_3_0.findTF("right/infomation/spoils/items/items_container")
	arg_3_0._goals = arg_3_0.findTF("right/infomation/goal")
	arg_3_0._item = arg_3_0.getTpl("right/infomation/spoils/items/item_tpl")
	arg_3_0._heroInfo = arg_3_0.getTpl("heroInfo")
	arg_3_0._starTpl = arg_3_0.getTpl("star_tpl")
	arg_3_0._middle = arg_3_0.findTF("middle")
	arg_3_0._right = arg_3_0.findTF("right")
	arg_3_0._formationLogic = BaseFormation.New(arg_3_0._tf, arg_3_0._heroContainer, arg_3_0._heroInfo, arg_3_0._gridTFs)

	local var_3_1 = {
		def Shift:(arg_4_0, arg_4_1, arg_4_2)
			return
	}

	setmetatable(var_3_1, arg_3_0._formationLogic)
	setText(findTF(arg_3_0._tf, "middle/gear_score/vanguard/line/Image/Text1"), i18n("pre_combat_vanguard"))
	setText(findTF(arg_3_0._tf, "middle/gear_score/main/line/Image/Text1"), i18n("pre_combat_main"))

	arg_3_0._fleet = arg_3_0.findTF("middle/fleet")

	setText(findTF(arg_3_0._fleet, "title_bg/Text"), i18n("pre_combat_team"))

	arg_3_0._ship_tpl = findTF(arg_3_0._fleet, "shiptpl")
	arg_3_0._empty_tpl = findTF(arg_3_0._fleet, "emptytpl")

	setActive(arg_3_0._ship_tpl, False)
	setActive(arg_3_0._empty_tpl, False)

	arg_3_0._autoToggle = arg_3_0.findTF("middle/auto_toggle")
	arg_3_0._autoSubToggle = arg_3_0.findTF("middle/sub_toggle_container/sub_toggle")
	arg_3_0.topPanel = arg_3_0.findTF("top")
	arg_3_0.strategyInfo = arg_3_0.findTF("strategy_info")

	setActive(arg_3_0.strategyInfo, False)

	arg_3_0._operaionBuffTips = arg_3_0._extraCostBuffIcon.Find("popup")

	setAnchoredPosition(arg_3_0._middle, {
		x = -840
	})
	setAnchoredPosition(arg_3_0._right, {
		x = 470
	})
	arg_3_0.Register()

def var_0_0.uiStartAnimating(arg_5_0):
	setAnchoredPosition(arg_5_0.topPanel, {
		y = 100
	})

	local var_5_0 = 0
	local var_5_1 = 0.3

	shiftPanel(arg_5_0._middle, 0, None, var_5_1, var_5_0, True, True)
	shiftPanel(arg_5_0._right, 0, None, var_5_1, var_5_0, True, True, None)
	shiftPanel(arg_5_0.topPanel, None, 0, var_5_1, var_5_0, True, True, None, None)

def var_0_0.uiExitAnimating(arg_6_0):
	local var_6_0 = 0
	local var_6_1 = 0.3

	shiftPanel(arg_6_0._middle, -840, None, var_6_1, var_6_0, True, True)
	shiftPanel(arg_6_0._right, 470, None, var_6_1, var_6_0, True, True)
	shiftPanel(arg_6_0.topPanel, None, arg_6_0.topPanel.rect.height, var_6_1, var_6_0, True, True, None, None)

def var_0_0.didEnter(arg_7_0):
	onButton(arg_7_0, arg_7_0._backBtn, function()
		GetOrAddComponent(arg_7_0._tf, typeof(CanvasGroup)).interactable = False

		arg_7_0.uiExitAnimating()
		LeanTween.delayedCall(0.3, System.Action(function()
			arg_7_0.emit(var_0_0.ON_CLOSE))), SFX_CANCEL)
	onButton(arg_7_0, arg_7_0._startBtn, function()
		arg_7_0.emit(ChapterPreCombatMediator.ON_START), SFX_UI_WEIGHANCHOR)
	onToggle(arg_7_0, arg_7_0._autoToggle, function(arg_11_0)
		arg_7_0.emit(ChapterPreCombatMediator.ON_AUTO, {
			isOn = not arg_11_0,
			toggle = arg_7_0._autoToggle
		})

		if arg_11_0 and arg_7_0.subUseable == True:
			setActive(arg_7_0._autoSubToggle, True)
			onToggle(arg_7_0, arg_7_0._autoSubToggle, function(arg_12_0)
				arg_7_0.emit(ChapterPreCombatMediator.ON_SUB_AUTO, {
					isOn = not arg_12_0,
					toggle = arg_7_0._autoSubToggle
				}), SFX_PANEL, SFX_PANEL)
			triggerToggle(arg_7_0._autoSubToggle, ys.Battle.BattleState.IsAutoSubActive())
		else
			setActive(arg_7_0._autoSubToggle, False), SFX_PANEL, SFX_PANEL)
	pg.UIMgr.GetInstance().OverlayPanel(arg_7_0._tf, {
		weight = LayerWeightConst.SECOND_LAYER,
		groupName = LayerWeightConst.GROUP_LEVELUI
	})
	onNextTick(function()
		if arg_7_0.exited:
			return

		triggerToggle(arg_7_0._autoToggle, ys.Battle.BattleState.IsAutoBotActive()))
	setAnchoredPosition(arg_7_0.topPanel, {
		y = arg_7_0.topPanel.rect.height
	})
	onNextTick(function()
		arg_7_0.uiStartAnimating())
	onButton(arg_7_0, arg_7_0.findTF("middle/gear_score/vanguard/SonarTip"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.fleet_antisub_range_tip.tip,
			weight = LayerWeightConst.SECOND_LAYER
		}), SFX_PANEL)
	onButton(arg_7_0, arg_7_0._costTip, function()
		local var_16_0 = arg_7_0.chapter.fleet
		local var_16_1 = arg_7_0.chapter.getStageId(var_16_0.line.row, var_16_0.line.column)
		local var_16_2, var_16_3, var_16_4 = arg_7_0.chapter.isOverFleetCost(var_16_0, var_16_1)

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = True,
			content = i18n("use_oil_limit_help", var_16_4, var_16_3),
			weight = LayerWeightConst.SECOND_LAYER
		}))

def var_0_0.Register(arg_17_0):
	arg_17_0._formationLogic.AddHeroInfoModify(function(arg_18_0, arg_18_1, arg_18_2)
		setAnchoredPosition(arg_18_0, {
			x = 0,
			y = 0
		})
		SetActive(arg_18_0, True)

		arg_18_0.name = "info"

		local var_18_0 = findTF(arg_18_0, "info")
		local var_18_1 = findTF(var_18_0, "stars")
		local var_18_2 = arg_18_1.getEnergy() <= Ship.ENERGY_MID
		local var_18_3 = findTF(var_18_0, "energy")

		if var_18_2:
			local var_18_4, var_18_5 = arg_18_1.getEnergyPrint()
			local var_18_6 = GetSpriteFromAtlas("energy", var_18_4)

			if not var_18_6:
				warning("找不到疲劳")

			setImageSprite(var_18_3, var_18_6)

		setActive(var_18_3, var_18_2)

		local var_18_7 = arg_18_1.getStar()

		for iter_18_0 = 1, var_18_7:
			cloneTplTo(arg_17_0._starTpl, var_18_1)

		local var_18_8 = GetSpriteFromAtlas("shiptype", shipType2print(arg_18_1.getShipType()))

		if not var_18_8:
			warning("找不到船形, shipConfigId. " .. arg_18_1.configId)

		setImageSprite(findTF(var_18_0, "type"), var_18_8, True)
		setText(findTF(var_18_0, "frame/lv_contain/lv"), arg_18_1.level)

		local var_18_9 = findTF(var_18_0, "blood")
		local var_18_10 = findTF(var_18_9, "fillarea/green")
		local var_18_11 = findTF(var_18_9, "fillarea/red")

		setActive(var_18_10, arg_18_1.hpRant >= ChapterConst.HpGreen)
		setActive(var_18_11, arg_18_1.hpRant < ChapterConst.HpGreen)

		;(arg_18_1.hpRant >= ChapterConst.HpGreen and var_18_10 or var_18_11).GetComponent("Image").fillAmount = arg_18_1.hpRant * 0.0001

		arg_18_2.SetVisible(arg_18_1.hpRant > 0)
		SetActive(arg_18_0, arg_18_1.hpRant > 0)

		local var_18_12 = getProxy(ActivityProxy).getBuffShipList()[arg_18_1.getGroupId()]
		local var_18_13 = var_18_0.Find("expbuff")

		setActive(var_18_13, var_18_12 != None)

		if var_18_12:
			local var_18_14 = var_18_12 / 100
			local var_18_15 = var_18_12 % 100
			local var_18_16 = tostring(var_18_14)

			if var_18_15 > 0:
				var_18_16 = var_18_16 .. "." .. tostring(var_18_15)

			setText(var_18_13.Find("text"), string.format("EXP +%s%%", var_18_16)))
	arg_17_0._formationLogic.AddShiftOnly(function(arg_19_0)
		arg_17_0.updateView(False))
	arg_17_0._formationLogic.AddEndDrag(function()
		arg_17_0.emit(ChapterPreCombatMediator.ON_SWITCH_SHIP, arg_17_0.chapter.fleet))
	arg_17_0._formationLogic.AddCheckRemove(function(arg_21_0, arg_21_1)
		arg_21_0())
	arg_17_0._formationLogic.AddCheckSwitch(function(arg_22_0, arg_22_1, arg_22_2, arg_22_3, arg_22_4)
		local var_22_0 = arg_22_3.getTeamByName(arg_22_4)

		if arg_22_3.ships[var_22_0[arg_22_2]].hpRant == 0:
			return

		arg_22_0())
	arg_17_0._formationLogic.AddCheckBeginDrag(function(arg_23_0, arg_23_1, arg_23_2)
		return arg_23_0.hpRant > 0)

def var_0_0.setPlayerInfo(arg_24_0, arg_24_1):
	return

def var_0_0.updateChapter(arg_25_0, arg_25_1):
	arg_25_0.chapter = arg_25_1

	local var_25_0 = arg_25_0.chapter.fleet

	arg_25_0._formationLogic.SetFleetVO(var_25_0)

	local var_25_1 = var_25_0.ships

	arg_25_0._formationLogic.SetShipVOs(var_25_1)
	arg_25_0.updateView(True)

def var_0_0.setSubFlag(arg_26_0, arg_26_1):
	arg_26_0.subUseable = arg_26_1 or False

def var_0_0.updateView(arg_27_0, arg_27_1):
	arg_27_0._formationLogic.ResetGrid(TeamType.Vanguard, True)
	arg_27_0._formationLogic.ResetGrid(TeamType.Main, True)
	SetActive(arg_27_0._gridTFs[TeamType.Main][1].Find("flag"), True)

	if arg_27_1:
		local var_27_0 = arg_27_0.chapter.fleet
		local var_27_1 = arg_27_0.chapter.getStageId(var_27_0.line.row, var_27_0.line.column)

		arg_27_0.updateStageView(var_27_1)
		arg_27_0._formationLogic.LoadAllCharacter()
	else
		arg_27_0._formationLogic.SetAllCharacterPos()

	arg_27_0.updateBattleFleetView()
	arg_27_0.updateStrategyIcon()
	arg_27_0.displayFleetInfo()

def var_0_0.updateStageView(arg_28_0, arg_28_1):
	local var_28_0 = pg.expedition_data_template[arg_28_1]

	assert(var_28_0, "expedition_data_template not exist. " .. arg_28_1)

	local var_28_1 = var_28_0.limit_type
	local var_28_2 = var_28_0.time_limit
	local var_28_3 = var_28_0.sink_limit
	local var_28_4 = Clone(var_28_0.award_display)
	local var_28_5 = checkExist(pg.expedition_activity_template[arg_28_1], {
		"pt_drop_display"
	})

	if var_28_5 and type(var_28_5) == "table":
		local var_28_6 = getProxy(ActivityProxy)

		for iter_28_0 = #var_28_5, 1, -1:
			local var_28_7 = var_28_6.getActivityById(var_28_5[iter_28_0][1])

			if var_28_7 and not var_28_7.isEnd():
				table.insert(var_28_4, 1, {
					2,
					id2ItemId(var_28_5[iter_28_0][2])
				})

	local var_28_8 = UIItemList.New(arg_28_0._spoilsContainer, arg_28_0._item)

	var_28_8.make(function(arg_29_0, arg_29_1, arg_29_2)
		local var_29_0 = arg_29_2
		local var_29_1 = var_28_4[arg_29_1 + 1]
		local var_29_2 = {
			type = var_29_1[1],
			id = var_29_1[2]
		}

		updateDrop(var_29_0, var_29_2)
		onButton(arg_28_0, var_29_0, function()
			local var_30_0 = Item.getConfigData(var_29_1[2])

			if var_30_0 and var_0_2[var_30_0.type]:
				local function var_30_1(arg_31_0)
					local var_31_0 = var_30_0.display_icon
					local var_31_1 = {}

					for iter_31_0, iter_31_1 in ipairs(var_31_0):
						local var_31_2 = iter_31_1[1]
						local var_31_3 = iter_31_1[2]
						local var_31_4 = var_31_2 == DROP_TYPE_SHIP and not table.contains(arg_31_0, var_31_3)

						var_31_1[#var_31_1 + 1] = {
							type = var_31_2,
							id = var_31_3,
							anonymous = var_31_4
						}

					arg_28_0.emit(var_0_0.ON_DROP_LIST, {
						item2Row = True,
						itemList = var_31_1,
						content = var_30_0.display
					})

				arg_28_0.emit(ChapterPreCombatMediator.GET_CHAPTER_DROP_SHIP_LIST, arg_28_0.chapter.id, var_30_1)
			else
				arg_28_0.emit(var_0_0.ON_DROP, var_29_2), SFX_PANEL))
	var_28_8.align(math.min(#var_28_4, 6))

	local function var_28_9(arg_32_0, arg_32_1)
		if type(arg_32_0) == "table":
			setActive(arg_32_1, True)

			local var_32_0 = i18n(PreCombatLayer.ObjectiveList[arg_32_0[1]], arg_32_0[2])

			setWidgetText(arg_32_1, var_32_0)
		else
			setActive(arg_32_1, False)

	local var_28_10 = {
		findTF(arg_28_0._goals, "goal_tpl"),
		findTF(arg_28_0._goals, "goal_sink"),
		findTF(arg_28_0._goals, "goal_time")
	}
	local var_28_11 = {
		var_28_0.objective_1,
		var_28_0.objective_2,
		var_28_0.objective_3
	}
	local var_28_12 = 1

	for iter_28_1, iter_28_2 in ipairs(var_28_11):
		if type(iter_28_2) != "string":
			var_28_9(iter_28_2, var_28_10[var_28_12])

			var_28_12 = var_28_12 + 1

	for iter_28_3 = var_28_12, #var_28_10:
		var_28_9("", var_28_10[iter_28_3])

def var_0_0.updateBattleFleetView(arg_33_0):
	local function var_33_0(arg_34_0, arg_34_1)
		removeAllChildren(arg_34_0)

		for iter_34_0 = 1, 3:
			if arg_34_1[iter_34_0]:
				local var_34_0 = cloneTplTo(arg_33_0._ship_tpl, arg_34_0)

				updateShip(var_34_0, arg_34_1[iter_34_0])

				local var_34_1 = arg_34_1[iter_34_0].hpRant
				local var_34_2 = findTF(var_34_0, "blood")
				local var_34_3 = findTF(var_34_0, "blood/fillarea/green")
				local var_34_4 = findTF(var_34_0, "blood/fillarea/red")

				setActive(var_34_3, var_34_1 >= ChapterConst.HpGreen)
				setActive(var_34_4, var_34_1 < ChapterConst.HpGreen)

				;(var_34_1 >= ChapterConst.HpGreen and var_34_3 or var_34_4).GetComponent("Image").fillAmount = var_34_1 * 0.0001

				setActive(findTF(var_34_0, "broken"), var_34_1 == 0)

	local var_33_1 = arg_33_0.chapter.fleet

	var_33_0(arg_33_0._fleet.Find("main"), var_33_1.getShipsByTeam(TeamType.Main, True))
	var_33_0(arg_33_0._fleet.Find("vanguard"), var_33_1.getShipsByTeam(TeamType.Vanguard, True))

def var_0_0.displayFleetInfo(arg_35_0):
	local var_35_0 = arg_35_0.chapter.fleet
	local var_35_1 = arg_35_0.chapter.getStageId(var_35_0.line.row, var_35_0.line.column)
	local var_35_2 = var_35_0.getCommanders()
	local var_35_3 = _.reduce(var_35_0.getShipsByTeam(TeamType.Vanguard, False), 0, function(arg_36_0, arg_36_1)
		return arg_36_0 + arg_36_1.getShipCombatPower(var_35_2))
	local var_35_4 = _.reduce(var_35_0.getShipsByTeam(TeamType.Main, False), 0, function(arg_37_0, arg_37_1)
		return arg_37_0 + arg_37_1.getShipCombatPower(var_35_2))
	local var_35_5 = 0

	for iter_35_0, iter_35_1 in ipairs({
		arg_35_0.chapter.getFleetCost(var_35_0, var_35_1)
	}):
		var_35_5 = var_35_5 + iter_35_1.oil

	local var_35_6 = arg_35_0.chapter.isOverFleetCost(var_35_0, var_35_1)

	setActive(arg_35_0._popup, True)
	setActive(arg_35_0._costTip, var_35_6)
	setTextColor(arg_35_0._costText, var_35_6 and Color(0.9803921568627451, 0.39215686274509803, 0.39215686274509803) or Color.white)
	var_0_1.tweenNumText(arg_35_0._costText, var_35_5)
	var_0_1.tweenNumText(arg_35_0._vanguardGS, var_35_3)
	var_0_1.tweenNumText(arg_35_0._mainGS, var_35_4)

	local var_35_7, var_35_8 = arg_35_0.chapter.GetExtraCostRate()

	setActive(arg_35_0._extraCostBuffIcon, #var_35_8 > 0)

	for iter_35_2, iter_35_3 in ipairs(var_35_8):
		if iter_35_3.benefit_type == Chapter.OPERATION_BUFF_TYPE_COST:
			setText(arg_35_0._extraCostBuffIcon.Find("text_cost"), tonumber(iter_35_3.benefit_effect) * 0.01 + 1)
		elif iter_35_3.benefit_type == Chapter.OPERATION_BUFF_TYPE_EXP:
			setText(arg_35_0._extraCostBuffIcon.Find("text_reward"), tonumber(iter_35_3.benefit_effect) * 0.01 + 1)
		elif iter_35_3.benefit_type == Chapter.OPERATION_BUFF_TYPE_DESC:
			onButton(arg_35_0, arg_35_0._extraCostBuffIcon, function()
				local var_38_0 = tonumber(iter_35_3.benefit_condition)
				local var_38_1 = pg.strategy_data_template[iter_35_3.id]

				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					hideNo = True,
					type = MSGBOX_TYPE_SINGLE_ITEM,
					drop = {
						count = 1,
						type = DROP_TYPE_ITEM,
						id = var_38_0
					},
					intro = var_38_1.desc,
					weight = LayerWeightConst.TOP_LAYER
				}))

	local var_35_9 = arg_35_0.findTF("middle/gear_score/vanguard")
	local var_35_10 = ChapterFleet.StaticTransformChapterFleet2Fleet(var_35_0).GetFleetSonarRange()

	setActive(var_35_9.Find("SonarActive"), var_35_10 > 0)
	setActive(var_35_9.Find("SonarInactive"), var_35_10 <= 0)

	if var_35_10 > 0:
		setText(var_35_9.Find("SonarActive/Text"), math.floor(var_35_10))

def var_0_0.updateStrategyIcon(arg_39_0):
	local var_39_0 = arg_39_0.chapter.fleet.getStrategies()
	local var_39_1 = _.detect(var_39_0, function(arg_40_0)
		return arg_40_0.id == ChapterConst.StrategyRepair)
	local var_39_2 = pg.strategy_data_template[var_39_1.id]

	GetImageSpriteFromAtlasAsync("strategyicon/" .. var_39_2.icon, "", arg_39_0._strategy.Find("icon"))
	onButton(arg_39_0, arg_39_0._strategy, function()
		arg_39_0.displayStrategyInfo(var_39_1), SFX_PANEL)
	setText(arg_39_0._strategy.Find("nums"), var_39_1.count)
	setActive(arg_39_0._strategy.Find("mask"), var_39_1.count == 0)
	setActive(arg_39_0._strategy.Find("selected"), False)

	local var_39_3 = arg_39_0.findTF("middle/formation_list")
	local var_39_4 = findTF(var_39_3, "formation")

	setActive(var_39_4, False)

	local var_39_5 = ChapterConst.StrategyForms
	local var_39_6 = {}
	local var_39_7 = arg_39_0.chapter.fleet.getFormationStg()

	table.insert(var_39_6, 1, {
		id = var_39_7
	})

	local var_39_8 = UIItemList.New(var_39_3, var_39_4)

	var_39_8.make(function(arg_42_0, arg_42_1, arg_42_2)
		if arg_42_0 == UIItemList.EventUpdate:
			local var_42_0 = var_39_6[arg_42_1 + 1]
			local var_42_1 = pg.strategy_data_template[var_42_0.id]

			if var_42_1.type != ChapterConst.StgTypeForm:
				return

			GetImageSpriteFromAtlasAsync("strategyicon/" .. var_42_1.icon, "", arg_42_2.Find("icon"))
			onButton(arg_39_0, arg_42_2, function()
				if var_42_1.type == ChapterConst.StgTypeForm:
					local var_43_0 = arg_39_0.chapter.fleet.getNextStgUser(var_42_0.id)
					local var_43_1 = table.indexof(var_39_5, var_42_0.id)

					arg_39_0.emit(ChapterPreCombatMediator.ON_OP, {
						type = ChapterConst.OpStrategy,
						id = var_43_0,
						arg1 = var_39_5[var_43_1 % #var_39_5 + 1]
					}), SFX_PANEL)
			setText(arg_42_2.Find("nums"), "")
			setActive(arg_42_2.Find("mask"), False)
			setActive(arg_42_2.Find("selected"), False))
	var_39_8.align(#var_39_6)

def var_0_0.displayStrategyInfo(arg_44_0, arg_44_1):
	arg_44_0.strategyPanel = arg_44_0.strategyPanel or StrategyPanel.New(arg_44_0.strategyInfo)

	arg_44_0.strategyPanel.attach(arg_44_0)
	arg_44_0.strategyPanel.set(arg_44_1)
	pg.UIMgr.GetInstance().BlurPanel(arg_44_0.strategyPanel._tf, False, {
		weight = LayerWeightConst.SECOND_LAYER
	})

	function arg_44_0.strategyPanel.onConfirm()
		local var_45_0 = arg_44_0.chapter.fleet
		local var_45_1 = pg.strategy_data_template[arg_44_1.id]

		if not var_45_0.canUseStrategy(arg_44_1):
			return

		local var_45_2 = var_45_0.getNextStgUser(arg_44_1.id)

		arg_44_0.emit(ChapterPreCombatMediator.ON_OP, {
			type = ChapterConst.OpStrategy,
			id = var_45_2,
			arg1 = arg_44_1.id
		})
		arg_44_0.hideStrategyInfo()

	function arg_44_0.strategyPanel.onCancel()
		arg_44_0.hideStrategyInfo()

def var_0_0.hideStrategyInfo(arg_47_0):
	if arg_47_0.strategyPanel:
		pg.UIMgr.GetInstance().UnblurPanel(arg_47_0.strategyPanel._tf)
		arg_47_0.strategyPanel.detach()

def var_0_0.onBackPressed(arg_48_0):
	if arg_48_0.strategyPanel and arg_48_0.strategyPanel._go and isActive(arg_48_0.strategyPanel._go):
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)
		arg_48_0.hideStrategyInfo()
	else
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)
		triggerButton(arg_48_0._backBtn)

def var_0_0.willExit(arg_49_0):
	if arg_49_0.strategyPanel and arg_49_0.strategyPanel._go and isActive(arg_49_0.strategyPanel._go):
		arg_49_0.hideStrategyInfo()

	arg_49_0._formationLogic.Destroy()

	arg_49_0._formationLogic = None

	pg.UIMgr.GetInstance().UnOverlayPanel(arg_49_0._tf)

return var_0_0
