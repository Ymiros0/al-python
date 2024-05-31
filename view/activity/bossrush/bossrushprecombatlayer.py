local var_0_0 = class("BossRushPreCombatLayer", import("view.base.BaseUI"))
local var_0_1 = import("view.ship.FormationUI")
local var_0_2 = {
	[99] = True
}

def var_0_0.getUIName(arg_1_0):
	return "BossRushPreCombatUI"

def var_0_0.ResUISettings(arg_2_0):
	return True

def var_0_0.tempCache(arg_3_0):
	return True

def var_0_0.init(arg_4_0):
	arg_4_0.CommonInit()

	arg_4_0._formationLogic = BaseFormation.New(arg_4_0._tf, arg_4_0._heroContainer, arg_4_0._heroInfo, arg_4_0._gridTFs)

	arg_4_0.Register()

def var_0_0.CommonInit(arg_5_0):
	arg_5_0.eventTriggers = {}
	arg_5_0._startBtn = arg_5_0.findTF("right/start")
	arg_5_0._costContainer = arg_5_0.findTF("right/start/cost_container")
	arg_5_0._popup = arg_5_0._costContainer.Find("popup")
	arg_5_0._costText = arg_5_0._popup.Find("Text")
	arg_5_0._moveLayer = arg_5_0.findTF("moveLayer")

	local var_5_0 = arg_5_0.findTF("middle")

	arg_5_0._autoToggle = arg_5_0.findTF("auto_toggle")
	arg_5_0._autoSubToggle = arg_5_0.findTF("sub_toggle_container/sub_toggle")
	arg_5_0._fleetInfo = var_5_0.Find("fleet_info")
	arg_5_0._fleetNameText = var_5_0.Find("fleet_info/fleet_name/Text")
	arg_5_0._fleetNumText = var_5_0.Find("fleet_info/fleet_number")

	setActive(arg_5_0._fleetInfo, arg_5_0.contextData.system != SYSTEM_DUEL)

	arg_5_0._mainGS = var_5_0.Find("gear_score/main/Text")
	arg_5_0._vanguardGS = var_5_0.Find("gear_score/vanguard/Text")
	arg_5_0._subGS = var_5_0.Find("gear_score/submarine/Text")
	arg_5_0._bgFleet = var_5_0.Find("mask/grid_bg")
	arg_5_0._bgSub = var_5_0.Find("mask/bg_sub")
	arg_5_0._gridTFs = {
		[TeamType.Vanguard] = {},
		[TeamType.Main] = {},
		[TeamType.Submarine] = {}
	}
	arg_5_0._gridFrame = var_5_0.Find("mask/GridFrame")

	for iter_5_0 = 1, 3:
		arg_5_0._gridTFs[TeamType.Main][iter_5_0] = arg_5_0._gridFrame.Find("main_" .. iter_5_0)
		arg_5_0._gridTFs[TeamType.Vanguard][iter_5_0] = arg_5_0._gridFrame.Find("vanguard_" .. iter_5_0)
		arg_5_0._gridTFs[TeamType.Submarine][iter_5_0] = arg_5_0._gridFrame.Find("submarine_" .. iter_5_0)

	arg_5_0._nextPage = arg_5_0.findTF("middle/nextPage")
	arg_5_0._prevPage = arg_5_0.findTF("middle/prevPage")
	arg_5_0._heroContainer = var_5_0.Find("HeroContainer")
	arg_5_0._checkBtn = var_5_0.Find("checkBtn")
	arg_5_0._blurPanel = arg_5_0.findTF("blur_panel")
	arg_5_0.topPanel = arg_5_0.findTF("top", arg_5_0._blurPanel)
	arg_5_0.topPanelBg = arg_5_0.findTF("top_bg", arg_5_0._blurPanel)
	arg_5_0._backBtn = arg_5_0.findTF("back_btn", arg_5_0.topPanel)
	arg_5_0._spoilsContainer = arg_5_0.findTF("right/infomation/atlasloot/spoils/items/items_container")
	arg_5_0._item = arg_5_0.findTF("right/infomation/atlasloot/spoils/items/item_tpl")

	SetActive(arg_5_0._item, False)

	arg_5_0._goals = arg_5_0.findTF("right/infomation/target/goal")
	arg_5_0._heroInfo = arg_5_0.getTpl("heroInfo")
	arg_5_0._starTpl = arg_5_0.getTpl("star_tpl")

	setText(findTF(arg_5_0._tf, "middle/gear_score/vanguard/line/Image/Text1"), i18n("pre_combat_vanguard"))
	setText(findTF(arg_5_0._tf, "middle/gear_score/main/line/Image/Text1"), i18n("pre_combat_main"))
	setText(findTF(arg_5_0._tf, "middle/gear_score/submarine/line/Image/text1"), i18n("pre_combat_submarine"))
	setText(arg_5_0._costContainer.Find("title"), i18n("pre_combat_consume"))
	setText(findTF(arg_5_0._tf, "right/infomation/target/title/GameObject"), i18n("pre_combat_targets"))
	setText(findTF(arg_5_0._tf, "right/infomation/atlasloot/atlasloot/title/GameObject"), i18n("pre_combat_atlasloot"))
	setText(arg_5_0._startBtn.Find("text"), i18n("pre_combat_start"))
	setText(arg_5_0._startBtn.Find("text_en"), i18n("pre_combat_start_en"))

	arg_5_0._middle = arg_5_0.findTF("middle")
	arg_5_0._right = arg_5_0.findTF("right")

	setAnchoredPosition(arg_5_0._middle, {
		x = -840
	})
	setAnchoredPosition(arg_5_0._right, {
		x = 470
	})

	arg_5_0.guideDesc = arg_5_0.findTF("guideDesc", arg_5_0._middle)
	arg_5_0._costTip = arg_5_0._startBtn.Find("cost_container/popup/tip")
	arg_5_0._continuousBtn = arg_5_0.findTF("right/multiple")

	setText(arg_5_0._continuousBtn.Find("text"), i18n("multiple_sorties_title"))
	setText(arg_5_0._continuousBtn.Find("text_en"), i18n("multiple_sorties_title_eng"))

def var_0_0.Register(arg_6_0):
	arg_6_0._formationLogic.AddLoadComplete(function()
		return)
	arg_6_0._formationLogic.AddHeroInfoModify(function(arg_8_0, arg_8_1)
		setAnchoredPosition(arg_8_0, {
			x = 0,
			y = 0
		})
		SetActive(arg_8_0, True)

		arg_8_0.name = "info"

		local var_8_0 = findTF(arg_8_0, "info")
		local var_8_1 = findTF(var_8_0, "stars")
		local var_8_2 = arg_8_1.energy <= Ship.ENERGY_MID
		local var_8_3 = findTF(var_8_0, "energy")

		if var_8_2:
			local var_8_4, var_8_5 = arg_8_1.getEnergyPrint()
			local var_8_6 = GetSpriteFromAtlas("energy", var_8_4)

			if not var_8_6:
				warning("找不到疲劳")

			setImageSprite(var_8_3, var_8_6)

		setActive(var_8_3, var_8_2 and arg_6_0.contextData.system != SYSTEM_DUEL)

		local var_8_7 = arg_8_1.getStar()

		for iter_8_0 = 1, var_8_7:
			cloneTplTo(arg_6_0._starTpl, var_8_1)

		local var_8_8 = GetSpriteFromAtlas("shiptype", shipType2print(arg_8_1.getShipType()))

		if not var_8_8:
			warning("找不到船形, shipConfigId. " .. arg_8_1.configId)

		setImageSprite(findTF(var_8_0, "type"), var_8_8, True)
		setText(findTF(var_8_0, "frame/lv_contain/lv"), arg_8_1.level)

		local var_8_9 = var_8_0.Find("expbuff")

		setActive(var_8_9, False))
	arg_6_0._formationLogic.AddLongPress(function(arg_9_0, arg_9_1, arg_9_2, arg_9_3)
		arg_6_0.emit(BossRushPreCombatMediator.OPEN_SHIP_INFO, arg_9_1.id, arg_9_2))
	arg_6_0._formationLogic.AddBeginDrag(function(arg_10_0)
		local var_10_0 = findTF(arg_10_0, "info")

		SetActive(var_10_0, False))
	arg_6_0._formationLogic.AddEndDrag(function(arg_11_0)
		local var_11_0 = findTF(arg_11_0, "info")

		SetActive(var_11_0, True))
	arg_6_0._formationLogic.AddClick(function(arg_12_0, arg_12_1, arg_12_2)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_CLICK)
		arg_6_0.emit(BossRushPreCombatMediator.CHANGE_FLEET_SHIP, arg_12_0, arg_12_2, arg_12_1))
	arg_6_0._formationLogic.AddShiftOnly(function(arg_13_0)
		arg_6_0.emit(BossRushPreCombatMediator.CHANGE_FLEET_SHIPS_ORDER, arg_13_0))
	arg_6_0._formationLogic.AddRemoveShip(function(arg_14_0, arg_14_1)
		arg_6_0.emit(BossRushPreCombatMediator.REMOVE_SHIP, arg_14_0, arg_14_1))
	arg_6_0._formationLogic.AddCheckRemove(function(arg_15_0, arg_15_1, arg_15_2, arg_15_3, arg_15_4)
		if not arg_15_3.canRemove(arg_15_2):
			local var_15_0, var_15_1 = arg_15_3.getShipPos(arg_15_2)

			pg.TipsMgr.GetInstance().ShowTips(i18n("ship_formationUI_removeError_onlyShip", arg_15_2.getConfigTable().name, arg_15_3.name or "", Fleet.C_TEAM_NAME[var_15_1]))
			arg_15_0()
		else
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				zIndex = -100,
				hideNo = False,
				content = i18n("battle_preCombatLayer_quest_leaveFleet", arg_15_2.getConfigTable().name),
				onYes = arg_15_1,
				onNo = arg_15_0
			}))
	arg_6_0._formationLogic.AddSwitchToDisplayMode(function()
		arg_6_0.SetFleetStepper())
	arg_6_0._formationLogic.AddSwitchToShiftMode(function()
		arg_6_0.SetFleetStepper())
	arg_6_0._formationLogic.AddSwitchToPreviewMode(function()
		arg_6_0.SetFleetStepper())
	arg_6_0._formationLogic.AddGridTipClick(function(arg_19_0, arg_19_1)
		arg_6_0.emit(BossRushPreCombatMediator.CHANGE_FLEET_SHIP, None, arg_6_0._currentFleetVO, arg_19_0))

def var_0_0.SetPlayerInfo(arg_20_0, arg_20_1):
	return

def var_0_0.SetSubFlag(arg_21_0, arg_21_1):
	arg_21_0._subUseable = arg_21_1 or False

	arg_21_0.UpdateSubToggle()

def var_0_0.SetShips(arg_22_0, arg_22_1):
	arg_22_0._shipVOs = arg_22_1

	arg_22_0._formationLogic.SetShipVOs(arg_22_0._shipVOs)

def var_0_0.SetStageIds(arg_23_0, arg_23_1):
	removeAllChildren(arg_23_0._spoilsContainer)

	local var_23_0 = {}

	table.Foreach(arg_23_1, function(arg_24_0, arg_24_1)
		local var_24_0 = pg.expedition_data_template[arg_24_1]
		local var_24_1 = Clone(var_24_0.award_display)
		local var_24_2 = checkExist(pg.expedition_activity_template[arg_24_1], {
			"pt_drop_display"
		})

		if var_24_2 and type(var_24_2) == "table":
			local var_24_3 = getProxy(ActivityProxy)

			for iter_24_0 = #var_24_2, 1, -1:
				local var_24_4 = var_24_3.getActivityById(var_24_2[iter_24_0][1])

				if var_24_4 and not var_24_4.isEnd():
					table.insert(var_24_1, 1, {
						2,
						id2ItemId(var_24_2[iter_24_0][2])
					})

		table.insertto(var_23_0, var_24_1)

		if arg_24_0 > 1:
			return

		local function var_24_5(arg_25_0, arg_25_1)
			if type(arg_25_0) == "table":
				setActive(arg_25_1, True)

				local var_25_0 = i18n(PreCombatLayer.ObjectiveList[arg_25_0[1]], arg_25_0[2])

				setWidgetText(arg_25_1, var_25_0)
			else
				setActive(arg_25_1, False)

		local var_24_6 = {
			findTF(arg_23_0._goals, "goal_tpl"),
			findTF(arg_23_0._goals, "goal_sink"),
			findTF(arg_23_0._goals, "goal_time")
		}
		local var_24_7 = {
			var_24_0.objective_1,
			var_24_0.objective_2,
			var_24_0.objective_3
		}
		local var_24_8 = 1

		for iter_24_1, iter_24_2 in ipairs(var_24_7):
			if type(iter_24_2) != "string":
				var_24_5(iter_24_2, var_24_6[var_24_8])

				var_24_8 = var_24_8 + 1

		for iter_24_3 = var_24_8, #var_24_6:
			var_24_5("", var_24_6[iter_24_3]))

	local var_23_1 = {}

	for iter_23_0, iter_23_1 in ipairs(var_23_0):
		if (function()
			for iter_26_0, iter_26_1 in ipairs(var_23_1):
				if iter_23_1[1] == iter_26_1[1] and iter_23_1[2] == iter_26_1[2]:
					return False

			return True)():
			table.insert(var_23_1, iter_23_1)

	var_23_0 = var_23_1

	for iter_23_2, iter_23_3 in ipairs(var_23_0):
		local var_23_2 = cloneTplTo(arg_23_0._item, arg_23_0._spoilsContainer)
		local var_23_3 = {
			id = iter_23_3[2],
			type = iter_23_3[1]
		}

		updateDrop(var_23_2, var_23_3)
		onButton(arg_23_0, var_23_2, function()
			local var_27_0 = Item.getConfigData(iter_23_3[2])

			if var_27_0 and var_0_2[var_27_0.type]:
				local var_27_1 = var_27_0.display_icon
				local var_27_2 = {}

				for iter_27_0, iter_27_1 in ipairs(var_27_1):
					local var_27_3 = iter_27_1[1]
					local var_27_4 = iter_27_1[2]

					var_27_2[#var_27_2 + 1] = {
						hideName = True,
						type = var_27_3,
						id = var_27_4
					}

				arg_23_0.emit(var_0_0.ON_DROP_LIST, {
					item2Row = True,
					itemList = var_27_2,
					content = var_27_0.display
				})
			else
				arg_23_0.emit(var_0_0.ON_DROP, var_23_3), SFX_PANEL)

def var_0_0.SetFleets(arg_28_0, arg_28_1):
	arg_28_0._fleetVOs = {}
	arg_28_0._legalFleetIdList = {}

	_.each(arg_28_1, function(arg_29_0)
		arg_28_0._fleetVOs[arg_29_0.id] = arg_29_0

		table.insert(arg_28_0._legalFleetIdList, arg_29_0.id))

def var_0_0.SetCurrentFleet(arg_30_0, arg_30_1):
	arg_30_0._currentFleetVO = arg_30_0._fleetVOs[arg_30_1]

	arg_30_0._formationLogic.SetFleetVO(arg_30_0._currentFleetVO)

	for iter_30_0, iter_30_1 in ipairs(arg_30_0._legalFleetIdList):
		if arg_30_0._currentFleetVO.id == iter_30_1:
			arg_30_0._curFleetIndex = iter_30_0

			break

def var_0_0.CheckLegalFleet(arg_31_0):
	assert(False)

def var_0_0.UpdateFleetView(arg_32_0, arg_32_1):
	arg_32_0.displayFleetInfo()
	arg_32_0.updateFleetBg()
	arg_32_0._formationLogic.UpdateGridVisibility()
	arg_32_0._formationLogic.ResetGrid(TeamType.Vanguard, False)
	arg_32_0._formationLogic.ResetGrid(TeamType.Main, False)
	arg_32_0._formationLogic.ResetGrid(TeamType.Submarine, False)
	arg_32_0.resetFormationComponent()

	if arg_32_1:
		arg_32_0._formationLogic.LoadAllCharacter()
	else
		arg_32_0._formationLogic.SetAllCharacterPos()

def var_0_0.updateFleetBg(arg_33_0):
	local var_33_0 = arg_33_0._currentFleetVO.getFleetType()

	setActive(arg_33_0._bgFleet, var_33_0 == FleetType.Normal)
	setActive(arg_33_0._bgSub, var_33_0 == FleetType.Submarine)

def var_0_0.resetFormationComponent(arg_34_0):
	SetActive(arg_34_0._gridTFs.main[1].Find("flag"), #arg_34_0._currentFleetVO.getTeamByName(TeamType.Main) != 0)
	SetActive(arg_34_0._gridTFs.submarine[1].Find("flag"), #arg_34_0._currentFleetVO.getTeamByName(TeamType.Submarine) != 0)

def var_0_0.uiStartAnimating(arg_35_0):
	local var_35_0 = 0
	local var_35_1 = 0.3

	shiftPanel(arg_35_0._middle, 0, None, var_35_1, var_35_0, True, True)
	shiftPanel(arg_35_0._right, 0, None, var_35_1, var_35_0, True, True)

def var_0_0.uiExitAnimating(arg_36_0):
	shiftPanel(arg_36_0._middle, -840, None, None, None, True, True)
	shiftPanel(arg_36_0._right, 470, None, None, None, True, True)

def var_0_0.didEnter(arg_37_0):
	onButton(arg_37_0, arg_37_0._backBtn, function()
		GetOrAddComponent(arg_37_0._tf, typeof(CanvasGroup)).interactable = False

		arg_37_0.uiExitAnimating()
		LeanTween.delayedCall(0.3, System.Action(function()
			arg_37_0.emit(var_0_0.ON_CLOSE)))
		arg_37_0.emit(BossRushPreCombatMediator.ON_UPDATE_CUSTOM_FLEET), SFX_CANCEL)
	onButton(arg_37_0, arg_37_0._tf.Find("blur_panel/top/option"), function()
		arg_37_0.quickExitFunc()
		arg_37_0.emit(BossRushPreCombatMediator.ON_UPDATE_CUSTOM_FLEET), SFX_PANEL)
	onButton(arg_37_0, arg_37_0._startBtn, function()
		arg_37_0.emit(BossRushPreCombatMediator.ON_START), SFX_UI_WEIGHANCHOR)
	onButton(arg_37_0, arg_37_0._nextPage, function()
		arg_37_0.emit(BossRushPreCombatMediator.ON_CHANGE_FLEET, arg_37_0._legalFleetIdList[arg_37_0._curFleetIndex + 1]), SFX_PANEL)
	onButton(arg_37_0, arg_37_0._prevPage, function()
		arg_37_0.emit(BossRushPreCombatMediator.ON_CHANGE_FLEET, arg_37_0._legalFleetIdList[arg_37_0._curFleetIndex - 1]), SFX_PANEL)
	arg_37_0.UpdateFleetView(True)
	pg.UIMgr.GetInstance().BlurPanel(arg_37_0._tf)
	setActive(arg_37_0._autoToggle, True)
	onToggle(arg_37_0, arg_37_0._autoToggle, function(arg_44_0)
		arg_37_0.emit(BossRushPreCombatMediator.ON_AUTO, {
			isOn = not arg_44_0,
			toggle = arg_37_0._autoToggle
		})

		arg_37_0.autoFlag = arg_44_0

		arg_37_0.UpdateSubToggle(), SFX_PANEL, SFX_PANEL)
	onToggle(arg_37_0, arg_37_0._autoSubToggle, function(arg_45_0)
		arg_37_0.emit(BossRushPreCombatMediator.ON_SUB_AUTO, {
			isOn = not arg_45_0,
			toggle = arg_37_0._autoSubToggle
		}), SFX_PANEL, SFX_PANEL)
	triggerToggle(arg_37_0._autoToggle, ys.Battle.BattleState.IsAutoBotActive())
	onNextTick(function()
		arg_37_0.uiStartAnimating())

	local var_37_0 = getProxy(ActivityProxy).getActivityById(arg_37_0.contextData.actId)
	local var_37_1 = arg_37_0.contextData.seriesData

	;(function()
		local var_47_0 = var_37_1.GetType() == BossRushSeriesData.TYPE.NORMAL

		setActive(arg_37_0._continuousBtn, var_47_0)

		if not var_47_0:
			return

		local var_47_1 = var_37_0.HasPassSeries(var_37_1.id)

		setActive(arg_37_0._continuousBtn.Find("lock"), not var_47_1)

		local var_47_2 = var_47_1 and Color.white or Color.New(0.2980392156862745, 0.2980392156862745, 0.2980392156862745)

		setImageColor(arg_37_0._continuousBtn, var_47_2)
		setTextColor(arg_37_0._continuousBtn.Find("text"), var_47_2)
		setTextColor(arg_37_0._continuousBtn.Find("text_en"), var_47_2)
		onButton(arg_37_0, arg_37_0._continuousBtn, function()
			if var_47_1:
				arg_37_0.emit(BossRushPreCombatMediator.SHOW_CONTINUOUS_OPERATION_WINDOW, arg_37_0._currentFleetVO.id)
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("multiple_sorties_locked_tip")), SFX_PANEL))()

	local var_37_2 = var_37_1.GetExpeditionIds()
	local var_37_3 = var_37_1.GetBossIcons()
	local var_37_4 = arg_37_0._tf.Find("middle/Boss")

	UIItemList.StaticAlign(var_37_4, var_37_4.GetChild(0), #var_37_2, function(arg_49_0, arg_49_1, arg_49_2)
		if arg_49_0 != UIItemList.EventUpdate:
			return

		local var_49_0 = var_37_2[arg_49_1 + 1]
		local var_49_1 = var_37_3[arg_49_1 + 1][1]
		local var_49_2 = pg.expedition_data_template[var_49_0].level
		local var_49_3 = arg_49_2.Find("shiptpl")
		local var_49_4 = findTF(var_49_3, "icon_bg")
		local var_49_5 = findTF(var_49_3, "icon_bg/frame")

		SetCompomentEnabled(var_49_4, "Image", False)
		SetCompomentEnabled(var_49_5, "Image", False)
		setActive(arg_49_2.Find("shiptpl/icon_bg/lv"), False)

		local var_49_6 = arg_49_2.Find("shiptpl/icon_bg/icon")

		GetImageSpriteFromAtlasAsync("SquareIcon/" .. var_49_1, "", var_49_6)

		local var_49_7 = findTF(var_49_3, "ship_type")

		if var_49_7:
			setActive(var_49_7, True)
			setImageSprite(var_49_7, GetSpriteFromAtlas("shiptype", shipType2print(var_37_3[arg_49_1 + 1][2]))))
	arg_37_0.SetFleetStepper()
	arg_37_0.SetStageIds(arg_37_0.contextData.stageIds)

def var_0_0.UpdateSubToggle(arg_50_0):
	if arg_50_0.autoFlag and arg_50_0._subUseable == True:
		setActive(arg_50_0._autoSubToggle, True)
		triggerToggle(arg_50_0._autoSubToggle, ys.Battle.BattleState.IsAutoSubActive())
	else
		setActive(arg_50_0._autoSubToggle, False)

def var_0_0.displayFleetInfo(arg_51_0):
	local var_51_0 = arg_51_0._currentFleetVO.getFleetType()

	setActive(arg_51_0._vanguardGS.parent, var_51_0 == FleetType.Normal)
	setActive(arg_51_0._mainGS.parent, var_51_0 == FleetType.Normal)

	local var_51_1 = math.floor(arg_51_0._currentFleetVO.GetGearScoreSum(TeamType.Vanguard))
	local var_51_2 = math.floor(arg_51_0._currentFleetVO.GetGearScoreSum(TeamType.Main))

	setActive(arg_51_0._subGS.parent, var_51_0 == FleetType.Submarine)

	local var_51_3 = math.floor(arg_51_0._currentFleetVO.GetGearScoreSum(TeamType.Submarine))
	local var_51_4 = arg_51_0.contextData.system

	setActive(arg_51_0._costContainer, var_51_4 != SYSTEM_DUEL)
	var_0_1.tweenNumText(arg_51_0._vanguardGS, var_51_1)
	var_0_1.tweenNumText(arg_51_0._mainGS, var_51_2)
	var_0_1.tweenNumText(arg_51_0._subGS, var_51_3)
	setText(arg_51_0._fleetNameText, Fleet.DEFAULT_NAME[arg_51_0._curFleetIndex])
	setText(arg_51_0._fleetNumText, arg_51_0._curFleetIndex)

	local var_51_5 = arg_51_0.contextData.seriesData
	local var_51_6 = var_51_5.GetExpeditionIds()
	local var_51_7 = arg_51_0._tf.Find("middle/Boss")

	UIItemList.StaticAlign(var_51_7, var_51_7.GetChild(0), #var_51_6, function(arg_52_0, arg_52_1, arg_52_2)
		if arg_52_0 != UIItemList.EventUpdate:
			return

		local var_52_0 = arg_52_1 + 1 == arg_51_0._curFleetIndex or arg_51_0._curFleetIndex > #var_51_6 or arg_51_0.contextData.mode == BossRushSeriesData.MODE.SINGLE

		setActive(arg_52_2.Find("Select"), var_52_0)
		setActive(arg_52_2.Find("Image"), var_52_0))

	local var_51_8 = arg_51_0.contextData.fleets
	local var_51_9 = var_51_8[#var_51_8]
	local var_51_10 = _.slice(var_51_8, 1, #var_51_8 - 1)
	local var_51_11 = arg_51_0.contextData.mode
	local var_51_12 = False
	local var_51_13 = (function()
		local var_53_0 = 0
		local var_53_1 = pg.battle_cost_template[var_51_4]
		local var_53_2 = var_51_5.GetOilLimit()
		local var_53_3 = var_53_1.oil_cost > 0

		local function var_53_4(arg_54_0, arg_54_1)
			local var_54_0 = 0

			if var_53_3:
				var_54_0 = arg_54_0.GetCostSum().oil

				if arg_54_1 > 0:
					var_54_0 = math.min(arg_54_1, var_54_0)
					var_51_12 = var_51_12 and var_54_0 < arg_54_1

			return var_54_0

		local var_53_5 = #var_51_5.GetExpeditionIds()

		if var_51_11 == BossRushSeriesData.MODE.SINGLE:
			var_53_0 = var_53_0 + var_53_4(var_51_10[1], var_53_2[1])
			var_53_0 = var_53_0 + var_53_4(var_51_9, var_53_2[2])
			var_53_0 = var_53_0 * var_53_5
		else
			var_53_0 = var_53_4(var_51_9, var_53_2[2]) * var_53_5

			_.each(var_51_10, function(arg_55_0)
				var_53_0 = var_53_0 + var_53_4(arg_55_0, var_53_2[1]))

		return var_53_0)()

	local function var_51_14()
		local var_56_0 = 0
		local var_56_1 = pg.battle_cost_template[var_51_4]
		local var_56_2 = var_51_5.GetOilLimit()
		local var_56_3 = var_56_1.oil_cost > 0

		local function var_56_4(arg_57_0, arg_57_1)
			local var_57_0 = 0

			if var_56_3:
				var_57_0 = arg_57_0.GetCostSum().oil

			return var_57_0

		local var_56_5 = #var_51_5.GetExpeditionIds()

		if var_51_11 == BossRushSeriesData.MODE.SINGLE:
			var_56_0 = var_56_0 + var_56_4(var_51_10[1], var_56_2[1])
			var_56_0 = var_56_0 + var_56_4(var_51_9, var_56_2[2])
			var_56_0 = var_56_0 * var_56_5
		else
			var_56_0 = var_56_4(var_51_9, var_56_2[2]) * var_56_5

			_.each(var_51_10, function(arg_58_0)
				var_56_0 = var_56_0 + var_56_4(arg_58_0, var_56_2[1]))

		return var_56_0

	local var_51_15 = 0

	if var_51_12:
		var_51_15 = var_51_14()

	var_0_1.tweenNumText(arg_51_0._costText, var_51_13)
	setActive(arg_51_0._costTip, var_51_12)

	if var_51_12:
		onButton(arg_51_0, arg_51_0._costTip, function()
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				hideNo = True,
				content = i18n("use_oil_limit_help", var_51_15, var_51_13),
				weight = LayerWeightConst.SECOND_LAYER
			}))

def var_0_0.SetFleetStepper(arg_60_0):
	SetActive(arg_60_0._nextPage, arg_60_0._curFleetIndex < #arg_60_0._legalFleetIdList)
	SetActive(arg_60_0._prevPage, arg_60_0._curFleetIndex > 1)

def var_0_0.onBackPressed(arg_61_0):
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)
	triggerButton(arg_61_0._backBtn)

def var_0_0.willExit(arg_62_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_62_0._tf)
	arg_62_0._formationLogic.Destroy()

	arg_62_0._formationLogic = None

return var_0_0
