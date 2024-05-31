﻿local var_0_0 = class("BossSinglePreCombatLayer", import("view.base.BaseUI"))
local var_0_1 = import("view.ship.FormationUI")
local var_0_2 = {
	[99] = true
}

function var_0_0.getUIName(arg_1_0)
	return "BossSinglePreCombatUI"
end

function var_0_0.ResUISettings(arg_2_0)
	return {
		order = 5,
		anim = true,
		showType = PlayerResUI.TYPE_ALL
	}
end

function var_0_0.init(arg_3_0)
	arg_3_0:CommonInit()

	arg_3_0._formationLogic = BaseFormation.New(arg_3_0._tf, arg_3_0._heroContainer, arg_3_0._heroInfo, arg_3_0._gridTFs)

	arg_3_0:Register()
end

function var_0_0.CommonInit(arg_4_0)
	arg_4_0.eventTriggers = {}
	arg_4_0._startBtn = arg_4_0:findTF("right/start")
	arg_4_0._costContainer = arg_4_0:findTF("right/start/cost_container")
	arg_4_0._popup = arg_4_0._costContainer:Find("popup")
	arg_4_0._costText = arg_4_0._popup:Find("Text")
	arg_4_0._moveLayer = arg_4_0:findTF("moveLayer")

	local var_4_0 = arg_4_0:findTF("middle")

	arg_4_0._autoToggle = arg_4_0:findTF("auto_toggle")
	arg_4_0._autoSubToggle = arg_4_0:findTF("sub_toggle_container/sub_toggle")
	arg_4_0._fleetInfo = var_4_0:Find("fleet_info")
	arg_4_0._fleetNameText = var_4_0:Find("fleet_info/fleet_name/Text")
	arg_4_0._fleetNumText = var_4_0:Find("fleet_info/fleet_number")

	setActive(arg_4_0._fleetInfo, true)

	arg_4_0._mainGS = var_4_0:Find("gear_score/main/Text")
	arg_4_0._vanguardGS = var_4_0:Find("gear_score/vanguard/Text")
	arg_4_0._subGS = var_4_0:Find("gear_score/submarine/Text")
	arg_4_0._bgFleet = var_4_0:Find("mask/grid_bg")
	arg_4_0._bgSub = var_4_0:Find("mask/bg_sub")
	arg_4_0._gridTFs = {
		[TeamType.Vanguard] = {},
		[TeamType.Main] = {},
		[TeamType.Submarine] = {}
	}
	arg_4_0._gridFrame = var_4_0:Find("mask/GridFrame")

	for iter_4_0 = 1, 3 do
		arg_4_0._gridTFs[TeamType.Main][iter_4_0] = arg_4_0._gridFrame:Find("main_" .. iter_4_0)
		arg_4_0._gridTFs[TeamType.Vanguard][iter_4_0] = arg_4_0._gridFrame:Find("vanguard_" .. iter_4_0)
		arg_4_0._gridTFs[TeamType.Submarine][iter_4_0] = arg_4_0._gridFrame:Find("submarine_" .. iter_4_0)
	end

	arg_4_0._nextPage = arg_4_0:findTF("middle/nextPage")
	arg_4_0._prevPage = arg_4_0:findTF("middle/prevPage")
	arg_4_0._heroContainer = var_4_0:Find("HeroContainer")
	arg_4_0._checkBtn = var_4_0:Find("checkBtn")
	arg_4_0._blurPanel = arg_4_0:findTF("blur_panel")
	arg_4_0.topPanel = arg_4_0:findTF("top", arg_4_0._blurPanel)
	arg_4_0.topPanelBg = arg_4_0:findTF("top_bg", arg_4_0._blurPanel)
	arg_4_0._backBtn = arg_4_0:findTF("back_btn", arg_4_0.topPanel)
	arg_4_0._spoilsContainer = arg_4_0:findTF("right/infomation/atlasloot/spoils/items/items_container")
	arg_4_0._item = arg_4_0:findTF("right/infomation/atlasloot/spoils/items/item_tpl")

	SetActive(arg_4_0._item, false)

	arg_4_0._goals = arg_4_0:findTF("right/infomation/target/goal")
	arg_4_0._heroInfo = arg_4_0:getTpl("heroInfo")
	arg_4_0._starTpl = arg_4_0:getTpl("star_tpl")

	setText(findTF(arg_4_0._tf, "middle/gear_score/vanguard/line/Image/Text1"), i18n("pre_combat_vanguard"))
	setText(findTF(arg_4_0._tf, "middle/gear_score/main/line/Image/Text1"), i18n("pre_combat_main"))
	setText(findTF(arg_4_0._tf, "middle/gear_score/submarine/line/Image/text1"), i18n("pre_combat_submarine"))
	setText(arg_4_0._costContainer:Find("title"), i18n("pre_combat_consume"))
	setText(findTF(arg_4_0._tf, "right/infomation/target/title/GameObject"), i18n("pre_combat_targets"))
	setText(findTF(arg_4_0._tf, "right/infomation/atlasloot/atlasloot/title/GameObject"), i18n("pre_combat_atlasloot"))
	setText(arg_4_0._startBtn:Find("text"), i18n("pre_combat_start"))
	setText(arg_4_0._startBtn:Find("text_en"), i18n("pre_combat_start_en"))

	arg_4_0._middle = arg_4_0:findTF("middle")
	arg_4_0._right = arg_4_0:findTF("right")

	setAnchoredPosition(arg_4_0._middle, {
		x = -840
	})
	setAnchoredPosition(arg_4_0._right, {
		x = 470
	})

	arg_4_0.guideDesc = arg_4_0:findTF("guideDesc", arg_4_0._middle)

	if arg_4_0.contextData.stageId then
		arg_4_0:SetStageID(arg_4_0.contextData.stageId)
	end

	arg_4_0._costTip = arg_4_0._startBtn:Find("cost_container/popup/tip")
	arg_4_0._continuousBtn = arg_4_0:findTF("right/multiple")

	setText(arg_4_0._continuousBtn:Find("text"), i18n("multiple_sorties_title"))
	setText(arg_4_0._continuousBtn:Find("text_en"), i18n("multiple_sorties_title_eng"))
end

function var_0_0.Register(arg_5_0)
	arg_5_0._formationLogic:AddLoadComplete(function()
		if arg_5_0._currentForm ~= PreCombatLayer.FORM_EDIT then
			arg_5_0._formationLogic:SwitchToPreviewMode()
		end
	end)
	arg_5_0._formationLogic:AddHeroInfoModify(function(arg_7_0, arg_7_1)
		setAnchoredPosition(arg_7_0, {
			x = 0,
			y = 0
		})
		SetActive(arg_7_0, true)

		arg_7_0.name = "info"

		local var_7_0 = findTF(arg_7_0, "info")
		local var_7_1 = findTF(var_7_0, "stars")
		local var_7_2 = arg_7_1.energy <= Ship.ENERGY_MID
		local var_7_3 = findTF(var_7_0, "energy")

		if var_7_2 then
			local var_7_4, var_7_5 = arg_7_1:getEnergyPrint()
			local var_7_6 = GetSpriteFromAtlas("energy", var_7_4)

			if not var_7_6 then
				warning("找不到疲劳")
			end

			setImageSprite(var_7_3, var_7_6)
		end

		local var_7_7 = arg_5_0.contextData.system
		local var_7_8 = pg.battle_cost_template[var_7_7]

		setActive(var_7_3, var_7_2 and var_7_8.enter_energy_cost > 0)

		local var_7_9 = arg_7_1:getStar()

		for iter_7_0 = 1, var_7_9 do
			cloneTplTo(arg_5_0._starTpl, var_7_1)
		end

		local var_7_10 = GetSpriteFromAtlas("shiptype", shipType2print(arg_7_1:getShipType()))

		if not var_7_10 then
			warning("找不到船形, shipConfigId: " .. arg_7_1.configId)
		end

		setImageSprite(findTF(var_7_0, "type"), var_7_10, true)
		setText(findTF(var_7_0, "frame/lv_contain/lv"), arg_7_1.level)

		if var_7_8.ship_exp_award > 0 then
			local var_7_11 = getProxy(ActivityProxy):getBuffShipList()[arg_7_1:getGroupId()]
			local var_7_12 = var_7_0:Find("expbuff")

			setActive(var_7_12, var_7_11 ~= nil)

			if var_7_11 then
				local var_7_13 = var_7_11 / 100
				local var_7_14 = var_7_11 % 100
				local var_7_15 = tostring(var_7_13)

				if var_7_14 > 0 then
					var_7_15 = var_7_15 .. "." .. tostring(var_7_14)
				end

				setText(var_7_12:Find("text"), string.format("EXP +%s%%", var_7_15))
			end
		else
			local var_7_16 = var_7_0:Find("expbuff")

			setActive(var_7_16, false)
		end
	end)
	arg_5_0._formationLogic:AddLongPress(function(arg_8_0, arg_8_1, arg_8_2, arg_8_3)
		arg_5_0:emit(BossSinglePreCombatMediator.OPEN_SHIP_INFO, arg_8_1.id, arg_8_2)
	end)
	arg_5_0._formationLogic:AddBeginDrag(function(arg_9_0)
		local var_9_0 = findTF(arg_9_0, "info")

		SetActive(var_9_0, false)
	end)
	arg_5_0._formationLogic:AddEndDrag(function(arg_10_0)
		local var_10_0 = findTF(arg_10_0, "info")

		SetActive(var_10_0, true)
	end)
	arg_5_0._formationLogic:AddClick(function(arg_11_0, arg_11_1, arg_11_2)
		return
	end)
	arg_5_0._formationLogic:AddShiftOnly(function(arg_12_0)
		arg_5_0:emit(BossSinglePreCombatMediator.CHANGE_FLEET_SHIPS_ORDER, arg_12_0)
	end)
	arg_5_0._formationLogic:AddRemoveShip(function(arg_13_0, arg_13_1)
		return
	end)
	arg_5_0._formationLogic:AddCheckRemove(function(arg_14_0, arg_14_1, arg_14_2, arg_14_3, arg_14_4)
		arg_14_0()
	end)
	arg_5_0._formationLogic:AddSwitchToDisplayMode(function()
		arg_5_0._currentForm = PreCombatLayer.FORM_EDIT
		arg_5_0._checkBtn:GetComponent("Button").interactable = true

		arg_5_0:SetFleetStepper()
		setActive(arg_5_0._checkBtn:Find("save"), true)
		setActive(arg_5_0._checkBtn:Find("edit"), false)
	end)
	arg_5_0._formationLogic:AddSwitchToShiftMode(function()
		arg_5_0:SetFleetStepper()

		arg_5_0._checkBtn:GetComponent("Button").interactable = false
	end)
	arg_5_0._formationLogic:AddSwitchToPreviewMode(function()
		arg_5_0._currentForm = PreCombatLayer.FORM_PREVIEW
		arg_5_0._checkBtn:GetComponent("Button").interactable = true

		arg_5_0:SetFleetStepper()
		setActive(arg_5_0._checkBtn:Find("save"), false)
		setActive(arg_5_0._checkBtn:Find("edit"), true)
	end)
	arg_5_0._formationLogic:AddGridTipClick(function(arg_18_0, arg_18_1)
		return
	end)
	arg_5_0._formationLogic:DisableTip()
end

function var_0_0.SetPlayerInfo(arg_19_0, arg_19_1)
	return
end

function var_0_0.SetSubFlag(arg_20_0, arg_20_1)
	arg_20_0._subUseable = arg_20_1 or false
end

function var_0_0.SetShips(arg_21_0, arg_21_1)
	arg_21_0._shipVOs = arg_21_1

	arg_21_0._formationLogic:SetShipVOs(arg_21_0._shipVOs)
end

function var_0_0.SetStageID(arg_22_0, arg_22_1)
	removeAllChildren(arg_22_0._spoilsContainer)

	arg_22_0._stageID = arg_22_1

	local var_22_0 = pg.expedition_data_template[arg_22_1]
	local var_22_1 = Clone(var_22_0.award_display)
	local var_22_2 = checkExist(pg.expedition_activity_template[arg_22_1], {
		"pt_drop_display"
	})

	if var_22_2 and type(var_22_2) == "table" then
		local var_22_3 = getProxy(ActivityProxy)

		for iter_22_0 = #var_22_2, 1, -1 do
			local var_22_4 = var_22_3:getActivityById(var_22_2[iter_22_0][1])

			if var_22_4 and not var_22_4:isEnd() then
				table.insert(var_22_1, 1, {
					2,
					id2ItemId(var_22_2[iter_22_0][2])
				})
			end
		end
	end

	if arg_22_0.contextData.system ~= SYSTEM_BOSS_EXPERIMENT then
		for iter_22_1, iter_22_2 in ipairs(var_22_1) do
			local var_22_5 = cloneTplTo(arg_22_0._item, arg_22_0._spoilsContainer)
			local var_22_6 = {
				id = iter_22_2[2],
				type = iter_22_2[1]
			}

			updateDrop(var_22_5, var_22_6)
			onButton(arg_22_0, var_22_5, function()
				local var_23_0 = Item.getConfigData(iter_22_2[2])

				if var_23_0 and var_0_2[var_23_0.type] then
					local var_23_1 = var_23_0.display_icon
					local var_23_2 = {}

					for iter_23_0, iter_23_1 in ipairs(var_23_1) do
						local var_23_3 = iter_23_1[1]
						local var_23_4 = iter_23_1[2]

						var_23_2[#var_23_2 + 1] = {
							hideName = true,
							type = var_23_3,
							id = var_23_4
						}
					end

					arg_22_0:emit(var_0_0.ON_DROP_LIST, {
						item2Row = true,
						itemList = var_23_2,
						content = var_23_0.display
					})
				else
					arg_22_0:emit(var_0_0.ON_DROP, var_22_6)
				end
			end, SFX_PANEL)
		end
	end

	local function var_22_7(arg_24_0, arg_24_1)
		if type(arg_24_0) == "table" then
			setActive(arg_24_1, true)

			local var_24_0 = i18n(PreCombatLayer.ObjectiveList[arg_24_0[1]], arg_24_0[2])

			setWidgetText(arg_24_1, var_24_0)
		else
			setActive(arg_24_1, false)
		end
	end

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

	for iter_22_3, iter_22_4 in ipairs(var_22_9) do
		if type(iter_22_4) ~= "string" then
			var_22_7(iter_22_4, var_22_8[var_22_10])

			var_22_10 = var_22_10 + 1
		end
	end

	for iter_22_5 = var_22_10, #var_22_8 do
		var_22_7("", var_22_8[iter_22_5])
	end

	local var_22_11 = var_22_0.guide_desc and #var_22_0.guide_desc > 0

	setActive(arg_22_0.guideDesc, var_22_11)

	if var_22_11 then
		setText(arg_22_0.guideDesc, var_22_0.guide_desc)
	end
end

function var_0_0.SetFleets(arg_25_0, arg_25_1)
	local var_25_0 = _.filter(_.values(arg_25_1), function(arg_26_0)
		return arg_26_0:getFleetType() == FleetType.Normal
	end)

	arg_25_0._fleetVOs = {}

	_.each(var_25_0, function(arg_27_0)
		arg_25_0._fleetVOs[arg_27_0.id] = arg_27_0
	end)
	arg_25_0:CheckLegalFleet()
end

function var_0_0.SetCurrentFleet(arg_28_0, arg_28_1)
	arg_28_0._currentFleetVO = arg_28_0._fleetVOs[arg_28_1]

	arg_28_0._formationLogic:SetFleetVO(arg_28_0._currentFleetVO)
	arg_28_0:CheckLegalFleet()

	for iter_28_0, iter_28_1 in ipairs(arg_28_0._legalFleetIdList) do
		if arg_28_0._currentFleetVO.id == iter_28_1 then
			arg_28_0._curFleetIndex = iter_28_0

			break
		end
	end
end

function var_0_0.CheckLegalFleet(arg_29_0)
	arg_29_0._legalFleetIdList = {}

	for iter_29_0, iter_29_1 in pairs(arg_29_0._fleetVOs) do
		if #iter_29_1.ships > 0 and iter_29_1.id ~= FleetProxy.PVP_FLEET_ID then
			table.insert(arg_29_0._legalFleetIdList, iter_29_1.id)
		end
	end

	table.sort(arg_29_0._legalFleetIdList)
end

function var_0_0.UpdateFleetView(arg_30_0, arg_30_1)
	arg_30_0:displayFleetInfo()
	arg_30_0:updateFleetBg()
	arg_30_0._formationLogic:UpdateGridVisibility()
	arg_30_0._formationLogic:ResetGrid(TeamType.Vanguard, arg_30_0._currentForm ~= PreCombatLayer.FORM_EDIT)
	arg_30_0._formationLogic:ResetGrid(TeamType.Main, arg_30_0._currentForm ~= PreCombatLayer.FORM_EDIT)
	arg_30_0._formationLogic:ResetGrid(TeamType.Submarine, arg_30_0._currentForm ~= PreCombatLayer.FORM_EDIT)
	arg_30_0:resetFormationComponent()

	if arg_30_1 then
		arg_30_0._formationLogic:LoadAllCharacter()
	else
		arg_30_0._formationLogic:SetAllCharacterPos()
	end
end

function var_0_0.updateFleetBg(arg_31_0)
	local var_31_0 = arg_31_0._currentFleetVO:getFleetType()

	setActive(arg_31_0._bgFleet, var_31_0 == FleetType.Normal)
	setActive(arg_31_0._bgSub, var_31_0 == FleetType.Submarine)
end

function var_0_0.resetFormationComponent(arg_32_0)
	SetActive(arg_32_0._gridTFs.main[1]:Find("flag"), #arg_32_0._currentFleetVO:getTeamByName(TeamType.Main) ~= 0)
	SetActive(arg_32_0._gridTFs.submarine[1]:Find("flag"), #arg_32_0._currentFleetVO:getTeamByName(TeamType.Submarine) ~= 0)
end

function var_0_0.uiStartAnimating(arg_33_0)
	local var_33_0 = 0
	local var_33_1 = 0.3

	shiftPanel(arg_33_0._middle, 0, nil, var_33_1, var_33_0, true, true)
	shiftPanel(arg_33_0._right, 0, nil, var_33_1, var_33_0, true, true)
end

function var_0_0.uiExitAnimating(arg_34_0)
	shiftPanel(arg_34_0._middle, -840, nil, nil, nil, true, true)
	shiftPanel(arg_34_0._right, 470, nil, nil, nil, true, true)
end

function var_0_0.quickExitFunc(arg_35_0)
	if arg_35_0._currentForm == PreCombatLayer.FORM_EDIT then
		arg_35_0:emit(BossSinglePreCombatMediator.ON_ABORT_EDIT)
	end

	var_0_0.super.quickExitFunc(arg_35_0)
end

function var_0_0.didEnter(arg_36_0)
	onButton(arg_36_0, arg_36_0._backBtn, function()
		local var_37_0 = {}

		if arg_36_0._currentForm == PreCombatLayer.FORM_EDIT then
			table.insert(var_37_0, function(arg_38_0)
				pg.MsgboxMgr.GetInstance():ShowMsgBox({
					zIndex = -100,
					hideNo = false,
					content = i18n("battle_preCombatLayer_save_confirm"),
					onYes = function()
						arg_36_0:emit(BossSinglePreCombatMediator.ON_COMMIT_EDIT, function()
							pg.TipsMgr.GetInstance():ShowTips(i18n("battle_preCombatLayer_save_success"))
							arg_38_0()
						end)
					end,
					onNo = function()
						arg_36_0:emit(BossSinglePreCombatMediator.ON_ABORT_EDIT)
						arg_38_0()
					end,
					weight = LayerWeightConst.TOP_LAYER
				})
			end)
		end

		seriesAsync(var_37_0, function()
			GetOrAddComponent(arg_36_0._tf, typeof(CanvasGroup)).interactable = false

			arg_36_0:uiExitAnimating()
			LeanTween.delayedCall(0.3, System.Action(function()
				arg_36_0:emit(var_0_0.ON_CLOSE)
			end))
		end)
	end, SFX_CANCEL)
	onButton(arg_36_0, arg_36_0._startBtn, function()
		local var_44_0 = {}

		if arg_36_0._currentForm == PreCombatLayer.FORM_EDIT then
			table.insert(var_44_0, function(arg_45_0)
				pg.MsgboxMgr.GetInstance():ShowMsgBox({
					zIndex = -100,
					hideNo = false,
					content = i18n("battle_preCombatLayer_save_march"),
					onYes = function()
						arg_36_0:emit(BossSinglePreCombatMediator.ON_COMMIT_EDIT, function()
							pg.TipsMgr.GetInstance():ShowTips(i18n("battle_preCombatLayer_save_success"))
							arg_45_0()
						end)
					end
				})
			end)
		end

		seriesAsync(var_44_0, function()
			arg_36_0:emit(BossSinglePreCombatMediator.ON_START, arg_36_0._currentFleetVO.id)
		end)
	end, SFX_UI_WEIGHANCHOR)
	onButton(arg_36_0, arg_36_0._checkBtn, function()
		if arg_36_0._currentForm == PreCombatLayer.FORM_EDIT then
			arg_36_0:emit(BossSinglePreCombatMediator.ON_COMMIT_EDIT, function()
				pg.TipsMgr.GetInstance():ShowTips(i18n("battle_preCombatLayer_save_success"))
				arg_36_0._formationLogic:SwitchToPreviewMode()
			end)
		elseif arg_36_0._currentForm == PreCombatLayer.FORM_PREVIEW then
			arg_36_0._formationLogic:SwitchToDisplayMode()
		else
			assert("currentForm error")
		end
	end, SFX_PANEL)

	arg_36_0._currentForm = arg_36_0.contextData.form
	arg_36_0.contextData.form = nil

	arg_36_0:UpdateFleetView(true)

	if arg_36_0._currentForm == PreCombatLayer.FORM_EDIT then
		arg_36_0._formationLogic:SwitchToDisplayMode()
	else
		arg_36_0._formationLogic:SwitchToPreviewMode()
	end

	pg.UIMgr.GetInstance():BlurPanel(arg_36_0._tf)
	setActive(arg_36_0._autoToggle, true)
	onToggle(arg_36_0, arg_36_0._autoToggle, function(arg_51_0)
		arg_36_0:emit(BossSinglePreCombatMediator.ON_AUTO, {
			isOn = not arg_51_0,
			toggle = arg_36_0._autoToggle
		})

		if arg_51_0 and arg_36_0._subUseable == true then
			setActive(arg_36_0._autoSubToggle, true)
			onToggle(arg_36_0, arg_36_0._autoSubToggle, function(arg_52_0)
				arg_36_0:emit(BossSinglePreCombatMediator.ON_SUB_AUTO, {
					isOn = not arg_52_0,
					toggle = arg_36_0._autoSubToggle
				})
			end, SFX_PANEL, SFX_PANEL)
			triggerToggle(arg_36_0._autoSubToggle, ys.Battle.BattleState.IsAutoSubActive())
		else
			setActive(arg_36_0._autoSubToggle, false)
		end
	end, SFX_PANEL, SFX_PANEL)
	triggerToggle(arg_36_0._autoToggle, ys.Battle.BattleState.IsAutoBotActive())
	onNextTick(function()
		arg_36_0:uiStartAnimating()
	end)

	local var_36_0 = arg_36_0.contextData.stageId
	local var_36_1 = getProxy(ActivityProxy):getActivityById(arg_36_0.contextData.actId)
	local var_36_2 = var_36_1:GetEnemyDataByStageId(var_36_0):IsContinuousType()
	local var_36_3 = var_36_2 and var_36_1:HasPassStage(var_36_0)

	setActive(arg_36_0._continuousBtn, var_36_2)
	setActive(arg_36_0._continuousBtn:Find("lock"), not var_36_3)

	local var_36_4 = var_36_3 and Color.white or Color.New(0.2980392156862745, 0.2980392156862745, 0.2980392156862745)

	setImageColor(arg_36_0._continuousBtn, var_36_4)
	setTextColor(arg_36_0._continuousBtn:Find("text"), var_36_4)
	setTextColor(arg_36_0._continuousBtn:Find("text_en"), var_36_4)
	onButton(arg_36_0, arg_36_0._continuousBtn, function()
		if var_36_3 then
			arg_36_0:emit(BossSinglePreCombatMediator.SHOW_CONTINUOUS_OPERATION_WINDOW, arg_36_0._currentFleetVO.id)
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("multiple_sorties_locked_tip"))
		end
	end, SFX_PANEL)
end

function var_0_0.displayFleetInfo(arg_55_0)
	local var_55_0 = arg_55_0._currentFleetVO:getFleetType()

	setActive(arg_55_0._vanguardGS.parent, var_55_0 == FleetType.Normal)
	setActive(arg_55_0._mainGS.parent, var_55_0 == FleetType.Normal)

	local var_55_1 = math.floor(arg_55_0._currentFleetVO:GetGearScoreSum(TeamType.Vanguard))
	local var_55_2 = math.floor(arg_55_0._currentFleetVO:GetGearScoreSum(TeamType.Main))

	setActive(arg_55_0._subGS.parent, var_55_0 == FleetType.Submarine)

	local var_55_3 = math.floor(arg_55_0._currentFleetVO:GetGearScoreSum(TeamType.Submarine))
	local var_55_4 = arg_55_0._currentFleetVO:GetCostSum()
	local var_55_5 = arg_55_0.contextData.system
	local var_55_6 = pg.battle_cost_template[var_55_5].oil_cost == 0 and 0 or var_55_4.oil

	setActive(arg_55_0._costContainer, true)
	var_0_1.tweenNumText(arg_55_0._costText, var_55_6)
	var_0_1.tweenNumText(arg_55_0._vanguardGS, var_55_1)
	var_0_1.tweenNumText(arg_55_0._mainGS, var_55_2)
	var_0_1.tweenNumText(arg_55_0._subGS, var_55_3)
	setText(arg_55_0._fleetNameText, Fleet.DEFAULT_NAME_BOSS_SINGLE_ACT[arg_55_0._currentFleetVO.id])
	setText(arg_55_0._fleetNumText, arg_55_0._currentFleetVO.id)

	local var_55_7 = arg_55_0.contextData.stageId
	local var_55_8 = getProxy(ActivityProxy):getActivityById(arg_55_0.contextData.actId)
	local var_55_9 = pg.battle_cost_template[var_55_5].oil_cost > 0
	local var_55_10 = 0
	local var_55_11 = 0
	local var_55_12 = false

	for iter_55_0, iter_55_1 in ipairs({
		arg_55_0.contextData.fleets[1]
	}) do
		local var_55_13 = iter_55_1:GetCostSum().oil

		if not var_55_9 then
			var_55_13 = 0
		end

		var_55_11 = var_55_11 + var_55_13

		local var_55_14 = iter_55_0 == 1
		local var_55_15 = arg_55_0.contextData.costLimit[var_55_14 and 1 or 2]

		if var_55_15 > 0 then
			var_55_12 = var_55_12 or var_55_15 < var_55_13
			var_55_13 = math.min(var_55_13, var_55_15)
		end

		var_55_10 = var_55_10 + var_55_13
	end

	setTextColor(arg_55_0._costText, var_55_12 and Color(0.9803921568627451, 0.39215686274509803, 0.39215686274509803) or Color.white)
	var_0_1.tweenNumText(arg_55_0._costText, var_55_10)
	setActive(arg_55_0._costTip, var_55_12)

	if var_55_12 then
		onButton(arg_55_0, arg_55_0._costTip, function()
			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				hideNo = true,
				content = i18n("use_oil_limit_help", var_55_11, var_55_10),
				weight = LayerWeightConst.SECOND_LAYER
			})
		end)
	end
end

function var_0_0.SetFleetStepper(arg_57_0)
	SetActive(arg_57_0._nextPage, false)
	SetActive(arg_57_0._prevPage, false)
end

function var_0_0.onBackPressed(arg_58_0)
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CANCEL)
	triggerButton(arg_58_0._backBtn)
end

function var_0_0.willExit(arg_59_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_59_0._tf)
	arg_59_0._formationLogic:Destroy()

	arg_59_0._formationLogic = nil
end

return var_0_0
