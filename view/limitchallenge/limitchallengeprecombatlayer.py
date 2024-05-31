local var_0_0 = class("LimitChallengePreCombatLayer", import("view.base.BaseUI"))
local var_0_1 = import("view.ship.FormationUI")
local var_0_2 = {
	[99] = True
}

def var_0_0.getUIName(arg_1_0):
	return "LimitChallengePreCombatUI"

def var_0_0.tempCache(arg_2_0):
	return True

def var_0_0.init(arg_3_0):
	arg_3_0.CommonInit()

	arg_3_0._formationLogic = BaseFormation.New(arg_3_0._tf, arg_3_0._heroContainer, arg_3_0._heroInfo, arg_3_0._gridTFs)

	arg_3_0.Register()

def var_0_0.CommonInit(arg_4_0):
	arg_4_0.eventTriggers = {}
	arg_4_0._startBtn = arg_4_0.findTF("right/start")
	arg_4_0._costContainer = arg_4_0.findTF("right/start/cost_container")
	arg_4_0._popup = arg_4_0._costContainer.Find("popup")
	arg_4_0._costText = arg_4_0._popup.Find("Text")
	arg_4_0._moveLayer = arg_4_0.findTF("moveLayer")

	local var_4_0 = arg_4_0.findTF("middle")

	arg_4_0._autoToggle = arg_4_0.findTF("auto_toggle")
	arg_4_0._autoSubToggle = arg_4_0.findTF("sub_toggle_container/sub_toggle")
	arg_4_0._fleetInfo = arg_4_0._tf.Find("right/fleet_info")
	arg_4_0._fleetNameText = arg_4_0._fleetInfo.Find("fleet_name/Text")
	arg_4_0._fleetNumText = arg_4_0._fleetInfo.Find("fleet_number")

	setActive(arg_4_0._fleetInfo, True)

	arg_4_0._mainGS = var_4_0.Find("gear_score/main/Text")
	arg_4_0._vanguardGS = var_4_0.Find("gear_score/vanguard/Text")
	arg_4_0._subGS = var_4_0.Find("gear_score/submarine/Text")
	arg_4_0._bgFleet = var_4_0.Find("mask/grid_bg")
	arg_4_0._bgSub = var_4_0.Find("mask/bg_sub")
	arg_4_0._gridTFs = {
		[TeamType.Vanguard] = {},
		[TeamType.Main] = {},
		[TeamType.Submarine] = {}
	}
	arg_4_0._gridFrame = var_4_0.Find("mask/GridFrame")

	for iter_4_0 = 1, 3:
		arg_4_0._gridTFs[TeamType.Main][iter_4_0] = arg_4_0._gridFrame.Find("main_" .. iter_4_0)
		arg_4_0._gridTFs[TeamType.Vanguard][iter_4_0] = arg_4_0._gridFrame.Find("vanguard_" .. iter_4_0)
		arg_4_0._gridTFs[TeamType.Submarine][iter_4_0] = arg_4_0._gridFrame.Find("submarine_" .. iter_4_0)

	arg_4_0._nextPage = arg_4_0.findTF("middle/nextPage")
	arg_4_0._prevPage = arg_4_0.findTF("middle/prevPage")
	arg_4_0._heroContainer = var_4_0.Find("HeroContainer")
	arg_4_0._blurPanel = arg_4_0.findTF("blur_panel")
	arg_4_0.topPanel = arg_4_0.findTF("top", arg_4_0._blurPanel)
	arg_4_0.topPanelBg = arg_4_0.findTF("top_bg", arg_4_0._blurPanel)
	arg_4_0._backBtn = arg_4_0.findTF("back_btn", arg_4_0.topPanel)
	arg_4_0._spoilsContainer = arg_4_0.findTF("right/infomation/atlasloot/spoils/items/items_container")
	arg_4_0._item = arg_4_0.findTF("right/infomation/atlasloot/spoils/items/item_tpl")

	SetActive(arg_4_0._item, False)

	arg_4_0._goals = arg_4_0.findTF("right/infomation/target/goal")
	arg_4_0._heroInfo = arg_4_0.getTpl("heroInfo")
	arg_4_0._starTpl = arg_4_0.getTpl("star_tpl")

	setText(findTF(arg_4_0._tf, "middle/gear_score/vanguard/line/Image/Text1"), i18n("pre_combat_vanguard"))
	setText(findTF(arg_4_0._tf, "middle/gear_score/main/line/Image/Text1"), i18n("pre_combat_main"))
	setText(findTF(arg_4_0._tf, "middle/gear_score/submarine/line/Image/text1"), i18n("pre_combat_submarine"))
	setText(arg_4_0._costContainer.Find("title"), i18n("pre_combat_consume"))
	setText(findTF(arg_4_0._tf, "right/infomation/target/title/GameObject"), i18n("pre_combat_targets"))
	setText(findTF(arg_4_0._tf, "right/infomation/atlasloot/atlasloot/title/GameObject"), i18n("pre_combat_atlasloot"))
	setText(arg_4_0._startBtn.Find("text"), i18n("pre_combat_start"))
	setText(arg_4_0._startBtn.Find("text_en"), i18n("pre_combat_start_en"))

	arg_4_0._middle = arg_4_0.findTF("middle")
	arg_4_0._right = arg_4_0.findTF("right")
	arg_4_0._bottom = arg_4_0.findTF("bottom")
	arg_4_0.btnRegular = arg_4_0.findTF("fleet_select/regular", arg_4_0._bottom)
	arg_4_0.btnSub = arg_4_0.findTF("fleet_select/sub", arg_4_0._bottom)

	setText(arg_4_0.btnRegular.Find("fleet/CnFleet"), Fleet.DEFAULT_NAME[1])
	setText(arg_4_0.btnSub.Find("fleet/CnFleet"), Fleet.DEFAULT_NAME[1])
	setAnchoredPosition(arg_4_0._middle, {
		x = -840
	})
	setAnchoredPosition(arg_4_0._right, {
		x = 470
	})
	arg_4_0.SetStageID(arg_4_0.contextData.stageId)

	arg_4_0.commanderFormationPanel = LimitChallengeCommanderFormationPage.New(arg_4_0._tf, arg_4_0.event, arg_4_0.contextData)

def var_0_0.Register(arg_5_0):
	arg_5_0._formationLogic.AddLoadComplete(function()
		return)
	arg_5_0._formationLogic.AddHeroInfoModify(function(arg_7_0, arg_7_1)
		setAnchoredPosition(arg_7_0, {
			x = 0,
			y = 0
		})
		SetActive(arg_7_0, True)

		arg_7_0.name = "info"

		local var_7_0 = findTF(arg_7_0, "info")
		local var_7_1 = findTF(var_7_0, "stars")
		local var_7_2 = arg_7_1.energy <= Ship.ENERGY_MID
		local var_7_3 = findTF(var_7_0, "energy")

		if var_7_2:
			local var_7_4, var_7_5 = arg_7_1.getEnergyPrint()
			local var_7_6 = GetSpriteFromAtlas("energy", var_7_4)

			if not var_7_6:
				warning("找不到疲劳")

			setImageSprite(var_7_3, var_7_6)

		setActive(var_7_3, var_7_2 and arg_5_0.contextData.system != SYSTEM_DUEL)

		local var_7_7 = arg_7_1.getStar()

		for iter_7_0 = 1, var_7_7:
			cloneTplTo(arg_5_0._starTpl, var_7_1)

		local var_7_8 = GetSpriteFromAtlas("shiptype", shipType2print(arg_7_1.getShipType()))

		if not var_7_8:
			warning("找不到船形, shipConfigId. " .. arg_7_1.configId)

		setImageSprite(findTF(var_7_0, "type"), var_7_8, True)
		setText(findTF(var_7_0, "frame/lv_contain/lv"), arg_7_1.level)

		local var_7_9 = var_7_0.Find("expbuff")

		setActive(var_7_9, False))
	arg_5_0._formationLogic.AddLongPress(function(arg_8_0, arg_8_1, arg_8_2, arg_8_3)
		arg_5_0.emit(LimitChallengePreCombatMediator.OPEN_SHIP_INFO, arg_8_1.id, arg_8_2))
	arg_5_0._formationLogic.AddBeginDrag(function(arg_9_0)
		local var_9_0 = findTF(arg_9_0, "info")

		SetActive(var_9_0, False))
	arg_5_0._formationLogic.AddEndDrag(function(arg_10_0)
		local var_10_0 = findTF(arg_10_0, "info")

		SetActive(var_10_0, True))
	arg_5_0._formationLogic.AddClick(function(arg_11_0, arg_11_1, arg_11_2)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_CLICK)
		arg_5_0.emit(LimitChallengePreCombatMediator.CHANGE_FLEET_SHIP, arg_11_0, arg_11_2, arg_11_1))
	arg_5_0._formationLogic.AddShiftOnly(function(arg_12_0)
		arg_5_0.emit(LimitChallengePreCombatMediator.CHANGE_FLEET_SHIPS_ORDER, arg_12_0))
	arg_5_0._formationLogic.AddRemoveShip(function(arg_13_0, arg_13_1)
		arg_5_0.emit(LimitChallengePreCombatMediator.REMOVE_SHIP, arg_13_0, arg_13_1))
	arg_5_0._formationLogic.AddCheckRemove(function(arg_14_0, arg_14_1, arg_14_2, arg_14_3, arg_14_4)
		if not arg_14_3.canRemove(arg_14_2):
			local var_14_0, var_14_1 = arg_14_3.getShipPos(arg_14_2)

			pg.TipsMgr.GetInstance().ShowTips(i18n("ship_formationUI_removeError_onlyShip", arg_14_2.getConfigTable().name, arg_14_3.name, Fleet.C_TEAM_NAME[var_14_1]))
			arg_14_0()
		else
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				zIndex = -100,
				hideNo = False,
				content = i18n("battle_preCombatLayer_quest_leaveFleet", arg_14_2.getConfigTable().name),
				onYes = arg_14_1,
				onNo = arg_14_0
			}))
	arg_5_0._formationLogic.AddSwitchToDisplayMode(function()
		return)
	arg_5_0._formationLogic.AddSwitchToShiftMode(function()
		arg_5_0.SetFleetStepper())
	arg_5_0._formationLogic.AddSwitchToPreviewMode(function()
		arg_5_0.SetFleetStepper())
	arg_5_0._formationLogic.AddGridTipClick(function(arg_18_0, arg_18_1)
		arg_5_0.emit(LimitChallengePreCombatMediator.CHANGE_FLEET_SHIP, None, arg_5_0._currentFleetVO, arg_18_0))

def var_0_0.SetPlayerInfo(arg_19_0, arg_19_1):
	return

def var_0_0.SetSubFlag(arg_20_0, arg_20_1):
	arg_20_0._subUseable = arg_20_1 or False

	arg_20_0.UpdateSubToggle()

def var_0_0.SetShips(arg_21_0, arg_21_1):
	arg_21_0._shipVOs = arg_21_1

	arg_21_0._formationLogic.SetShipVOs(arg_21_0._shipVOs)

def var_0_0.SetStageID(arg_22_0, arg_22_1):
	removeAllChildren(arg_22_0._spoilsContainer)

	arg_22_0._stageID = arg_22_1

	local var_22_0 = pg.expedition_data_template[arg_22_1]
	local var_22_1 = Clone(var_22_0.award_display)
	local var_22_2 = checkExist(pg.expedition_activity_template[arg_22_1], {
		"pt_drop_display"
	})

	if var_22_2 and type(var_22_2) == "table":
		local var_22_3 = getProxy(ActivityProxy)

		for iter_22_0 = #var_22_2, 1, -1:
			local var_22_4 = var_22_3.getActivityById(var_22_2[iter_22_0][1])

			if var_22_4 and not var_22_4.isEnd():
				table.insert(var_22_1, 1, {
					2,
					id2ItemId(var_22_2[iter_22_0][2])
				})

	for iter_22_1, iter_22_2 in ipairs(var_22_1):
		local var_22_5 = cloneTplTo(arg_22_0._item, arg_22_0._spoilsContainer)
		local var_22_6 = {
			id = iter_22_2[2],
			type = iter_22_2[1]
		}

		updateDrop(var_22_5, var_22_6)
		onButton(arg_22_0, var_22_5, function()
			local var_23_0 = Item.getConfigData(iter_22_2[2])

			if var_23_0 and var_0_2[var_23_0.type]:
				local var_23_1 = var_23_0.display_icon
				local var_23_2 = {}

				for iter_23_0, iter_23_1 in ipairs(var_23_1):
					local var_23_3 = iter_23_1[1]
					local var_23_4 = iter_23_1[2]

					var_23_2[#var_23_2 + 1] = {
						hideName = True,
						type = var_23_3,
						id = var_23_4
					}

				arg_22_0.emit(var_0_0.ON_DROP_LIST, {
					item2Row = True,
					itemList = var_23_2,
					content = var_23_0.display
				})
			else
				arg_22_0.emit(var_0_0.ON_DROP, var_22_6), SFX_PANEL)

	local function var_22_7(arg_24_0, arg_24_1)
		if type(arg_24_0) == "table":
			setActive(arg_24_1, True)

			local var_24_0 = i18n(PreCombatLayer.ObjectiveList[arg_24_0[1]], arg_24_0[2])

			setWidgetText(arg_24_1, var_24_0)
		else
			setActive(arg_24_1, False)

	local var_22_8 = {
		findTF(arg_22_0._goals, "goal_tpl"),
		findTF(arg_22_0._goals, "goal_sink"),
		findTF(arg_22_0._goals, "goal_time")
	}
	local var_22_9 = {
		var_22_0.objective_1,
		var_22_0.objective_2,
		var_22_0.objective_3
	}
	local var_22_10 = 1

	for iter_22_3, iter_22_4 in ipairs(var_22_9):
		if type(iter_22_4) != "string":
			var_22_7(iter_22_4, var_22_8[var_22_10])

			var_22_10 = var_22_10 + 1

	for iter_22_5 = var_22_10, #var_22_8:
		var_22_7("", var_22_8[iter_22_5])

def var_0_0.SetFleets(arg_25_0, arg_25_1):
	arg_25_0._fleetVOs = {}
	arg_25_0._legalFleetIdList = {}

	_.each(arg_25_1, function(arg_26_0)
		arg_25_0._fleetVOs[arg_26_0.id] = arg_26_0

		table.insert(arg_25_0._legalFleetIdList, arg_26_0.id))

def var_0_0.SetCurrentFleet(arg_27_0, arg_27_1):
	arg_27_0._currentFleetVO = arg_27_0._fleetVOs[arg_27_1]

	arg_27_0._formationLogic.SetFleetVO(arg_27_0._currentFleetVO)

	for iter_27_0, iter_27_1 in ipairs(arg_27_0._legalFleetIdList):
		if arg_27_0._currentFleetVO.id == iter_27_1:
			arg_27_0._curFleetIndex = iter_27_0

			break

	arg_27_0.updateCommanderFormation()

def var_0_0.SetOpenCommander(arg_28_0, arg_28_1):
	arg_28_0.isOpenCommander = arg_28_1

def var_0_0.CheckLegalFleet(arg_29_0):
	assert(False)

def var_0_0.UpdateFleetView(arg_30_0, arg_30_1):
	arg_30_0.displayFleetInfo()
	arg_30_0.updateFleetBg()
	arg_30_0._formationLogic.UpdateGridVisibility()
	arg_30_0._formationLogic.ResetGrid(TeamType.Vanguard)
	arg_30_0._formationLogic.ResetGrid(TeamType.Main)
	arg_30_0._formationLogic.ResetGrid(TeamType.Submarine)
	arg_30_0.resetFormationComponent()

	if arg_30_1:
		arg_30_0._formationLogic.LoadAllCharacter()
	else
		arg_30_0._formationLogic.SetAllCharacterPos()

	local var_30_0 = arg_30_0._currentFleetVO.getFleetType()

	setActive(arg_30_0.btnRegular.Find("on"), var_30_0 == FleetType.Normal)
	setActive(arg_30_0.btnRegular.Find("off"), var_30_0 != FleetType.Normal)
	setActive(arg_30_0.btnSub.Find("on"), var_30_0 == FleetType.Submarine)
	setActive(arg_30_0.btnSub.Find("off"), var_30_0 != FleetType.Submarine)

def var_0_0.updateFleetBg(arg_31_0):
	local var_31_0 = arg_31_0._currentFleetVO.getFleetType()

	setActive(arg_31_0._bgFleet, var_31_0 == FleetType.Normal)
	setActive(arg_31_0._bgSub, var_31_0 == FleetType.Submarine)

def var_0_0.resetFormationComponent(arg_32_0):
	SetActive(arg_32_0._gridTFs.main[1].Find("flag"), #arg_32_0._currentFleetVO.getTeamByName(TeamType.Main) != 0)
	SetActive(arg_32_0._gridTFs.submarine[1].Find("flag"), #arg_32_0._currentFleetVO.getTeamByName(TeamType.Submarine) != 0)

def var_0_0.uiStartAnimating(arg_33_0):
	local var_33_0 = 0
	local var_33_1 = 0.3

	shiftPanel(arg_33_0._middle, 0, None, var_33_1, var_33_0, True, True)
	shiftPanel(arg_33_0._right, 0, None, var_33_1, var_33_0, True, True)

def var_0_0.uiExitAnimating(arg_34_0):
	shiftPanel(arg_34_0._middle, -840, None, None, None, True, True)
	shiftPanel(arg_34_0._right, 470, None, None, None, True, True)

def var_0_0.didEnter(arg_35_0):
	onButton(arg_35_0, arg_35_0._backBtn, function()
		arg_35_0.emit(LimitChallengePreCombatMediator.ON_UPDATE_CUSTOM_FLEET)

		GetOrAddComponent(arg_35_0._tf, typeof(CanvasGroup)).interactable = False

		arg_35_0.uiExitAnimating()
		LeanTween.delayedCall(0.3, System.Action(function()
			arg_35_0.closeView())), SFX_CANCEL)
	onButton(arg_35_0, arg_35_0._tf.Find("blur_panel/top/option"), function()
		arg_35_0.emit(LimitChallengePreCombatMediator.ON_UPDATE_CUSTOM_FLEET)
		arg_35_0.quickExitFunc(), SFX_PANEL)
	onButton(arg_35_0, arg_35_0._startBtn, function()
		arg_35_0.emit(LimitChallengePreCombatMediator.ON_START), SFX_UI_WEIGHANCHOR)
	onButton(arg_35_0, arg_35_0._nextPage, function()
		arg_35_0.emit(LimitChallengePreCombatMediator.ON_CHANGE_FLEET, arg_35_0._legalFleetIdList[arg_35_0._curFleetIndex + 1]), SFX_PANEL)
	onButton(arg_35_0, arg_35_0._prevPage, function()
		arg_35_0.emit(LimitChallengePreCombatMediator.ON_CHANGE_FLEET, arg_35_0._legalFleetIdList[arg_35_0._curFleetIndex - 1]), SFX_PANEL)
	arg_35_0.UpdateFleetView(True)
	setActive(arg_35_0._autoToggle, True)
	onToggle(arg_35_0, arg_35_0._autoToggle, function(arg_42_0)
		arg_35_0.emit(LimitChallengePreCombatMediator.ON_AUTO, {
			isOn = not arg_42_0,
			toggle = arg_35_0._autoToggle
		})

		arg_35_0.autoFlag = arg_42_0

		arg_35_0.UpdateSubToggle(), SFX_PANEL, SFX_PANEL)
	onToggle(arg_35_0, arg_35_0._autoSubToggle, function(arg_43_0)
		arg_35_0.emit(LimitChallengePreCombatMediator.ON_SUB_AUTO, {
			isOn = not arg_43_0,
			toggle = arg_35_0._autoSubToggle
		}), SFX_PANEL, SFX_PANEL)
	onButton(arg_35_0, arg_35_0._tf.Find("bottom/fleet_select/regular"), function()
		arg_35_0.emit(LimitChallengePreCombatMediator.ON_CHANGE_FLEET, FleetProxy.CHALLENGE_FLEET_ID), SFX_PANEL)
	onButton(arg_35_0, arg_35_0._tf.Find("bottom/fleet_select/sub"), function()
		arg_35_0.emit(LimitChallengePreCombatMediator.ON_CHANGE_FLEET, FleetProxy.CHALLENGE_SUB_FLEET_ID), SFX_PANEL)

	if arg_35_0.isOpenCommander:
		arg_35_0.commanderFormationPanel.ActionInvoke("Show")

	triggerToggle(arg_35_0._autoToggle, ys.Battle.BattleState.IsAutoBotActive())
	onNextTick(function()
		arg_35_0.uiStartAnimating())
	arg_35_0.SetFleetStepper()
	pg.UIMgr.GetInstance().OverlayPanel(arg_35_0._tf, {
		groupName = LayerWeightConst.GROUP_FORMATION_PAGE
	})

def var_0_0.UpdateSubToggle(arg_47_0):
	if arg_47_0.autoFlag and arg_47_0._subUseable == True:
		setActive(arg_47_0._autoSubToggle, True)
		triggerToggle(arg_47_0._autoSubToggle, ys.Battle.BattleState.IsAutoSubActive())
	else
		setActive(arg_47_0._autoSubToggle, False)

def var_0_0.displayFleetInfo(arg_48_0):
	local var_48_0 = arg_48_0._currentFleetVO.getFleetType()

	setActive(arg_48_0._vanguardGS.parent, var_48_0 == FleetType.Normal)
	setActive(arg_48_0._mainGS.parent, var_48_0 == FleetType.Normal)

	local var_48_1 = math.floor(arg_48_0._currentFleetVO.GetGearScoreSum(TeamType.Vanguard))
	local var_48_2 = math.floor(arg_48_0._currentFleetVO.GetGearScoreSum(TeamType.Main))

	setActive(arg_48_0._subGS.parent, var_48_0 == FleetType.Submarine)

	local var_48_3 = math.floor(arg_48_0._currentFleetVO.GetGearScoreSum(TeamType.Submarine))
	local var_48_4 = arg_48_0.contextData.system

	setActive(arg_48_0._costContainer, var_48_4 != SYSTEM_DUEL)
	var_0_1.tweenNumText(arg_48_0._vanguardGS, var_48_1)
	var_0_1.tweenNumText(arg_48_0._mainGS, var_48_2)
	var_0_1.tweenNumText(arg_48_0._subGS, var_48_3)
	setText(arg_48_0._fleetNameText, arg_48_0._currentFleetVO.GetName())
	setText(arg_48_0._fleetNumText, arg_48_0._curFleetIndex)

	local var_48_5 = arg_48_0.contextData.fleets
	local var_48_6 = var_48_5[#var_48_5]
	local var_48_7 = _.slice(var_48_5, 1, #var_48_5 - 1)
	local var_48_8 = (function()
		local var_49_0 = 0
		local var_49_1 = pg.battle_cost_template[var_48_4].oil_cost > 0

		local function var_49_2(arg_50_0, arg_50_1)
			local var_50_0 = 0

			if var_49_1:
				var_50_0 = arg_50_0.GetCostSum().oil

				if arg_50_1 > 0:
					var_50_0 = math.min(arg_50_1, var_50_0)

			return var_50_0

		return var_49_0 + var_49_2(var_48_7[1], 0) + var_49_2(var_48_6, 0))()

	var_0_1.tweenNumText(arg_48_0._costText, var_48_8)

def var_0_0.SetFleetStepper(arg_51_0):
	SetActive(arg_51_0._nextPage, arg_51_0._curFleetIndex < #arg_51_0._legalFleetIdList)
	SetActive(arg_51_0._prevPage, arg_51_0._curFleetIndex > 1)

def var_0_0.updateCommanderFormation(arg_52_0):
	if arg_52_0.isOpenCommander:
		arg_52_0.commanderFormationPanel.Load()
		arg_52_0.commanderFormationPanel.ActionInvoke("Update", arg_52_0._currentFleetVO)

def var_0_0.onBackPressed(arg_53_0):
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)
	triggerButton(arg_53_0._backBtn)

def var_0_0.willExit(arg_54_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_54_0._tf)
	arg_54_0.commanderFormationPanel.Destroy()
	arg_54_0._formationLogic.Destroy()

	arg_54_0._formationLogic = None

return var_0_0
