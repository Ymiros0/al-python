local var_0_0 = class("ActivityBossPreCombatLayer", import("view.battle.PreCombatLayer"))
local var_0_1 = import("view.ship.FormationUI")
local var_0_2 = {
	[99] = true
}

function var_0_0.getUIName(arg_1_0)
	return "ActivityBossPrecombatUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0:CommonInit()

	arg_2_0._formationLogic = BaseFormation.New(arg_2_0._tf, arg_2_0._heroContainer, arg_2_0._heroInfo, arg_2_0._gridTFs)

	arg_2_0:Register()
end

function var_0_0.CommonInit(arg_3_0)
	arg_3_0.eventTriggers = {}
	arg_3_0._startBtn = arg_3_0:findTF("right/start")
	arg_3_0._costContainer = arg_3_0:findTF("right/start/cost_container")
	arg_3_0._popup = arg_3_0._costContainer:Find("popup")
	arg_3_0._costText = arg_3_0._popup:Find("Text")
	arg_3_0._moveLayer = arg_3_0:findTF("moveLayer")

	local var_3_0 = arg_3_0:findTF("middle")

	arg_3_0._autoToggle = arg_3_0:findTF("auto_toggle")
	arg_3_0._autoSubToggle = arg_3_0:findTF("sub_toggle_container/sub_toggle")
	arg_3_0._fleetInfo = var_3_0:Find("fleet_info")
	arg_3_0._fleetNameText = var_3_0:Find("fleet_info/fleet_name/Text")
	arg_3_0._fleetNumText = var_3_0:Find("fleet_info/fleet_number")

	setActive(arg_3_0._fleetInfo, true)

	arg_3_0._mainGS = var_3_0:Find("gear_score/main/Text")
	arg_3_0._vanguardGS = var_3_0:Find("gear_score/vanguard/Text")
	arg_3_0._subGS = var_3_0:Find("gear_score/submarine/Text")
	arg_3_0._bgFleet = var_3_0:Find("mask/grid_bg")
	arg_3_0._bgSub = var_3_0:Find("mask/bg_sub")
	arg_3_0._gridTFs = {
		[TeamType.Vanguard] = {},
		[TeamType.Main] = {},
		[TeamType.Submarine] = {}
	}
	arg_3_0._gridFrame = var_3_0:Find("mask/GridFrame")

	for iter_3_0 = 1, 3 do
		arg_3_0._gridTFs[TeamType.Main][iter_3_0] = arg_3_0._gridFrame:Find("main_" .. iter_3_0)
		arg_3_0._gridTFs[TeamType.Vanguard][iter_3_0] = arg_3_0._gridFrame:Find("vanguard_" .. iter_3_0)
		arg_3_0._gridTFs[TeamType.Submarine][iter_3_0] = arg_3_0._gridFrame:Find("submarine_" .. iter_3_0)
	end

	arg_3_0._nextPage = arg_3_0:findTF("middle/nextPage")
	arg_3_0._prevPage = arg_3_0:findTF("middle/prevPage")
	arg_3_0._heroContainer = var_3_0:Find("HeroContainer")
	arg_3_0._checkBtn = var_3_0:Find("checkBtn")
	arg_3_0._blurPanel = arg_3_0:findTF("blur_panel")
	arg_3_0.topPanel = arg_3_0:findTF("top", arg_3_0._blurPanel)
	arg_3_0.topPanelBg = arg_3_0:findTF("top_bg", arg_3_0._blurPanel)
	arg_3_0._backBtn = arg_3_0:findTF("back_btn", arg_3_0.topPanel)
	arg_3_0._spoilsContainer = arg_3_0:findTF("right/infomation/atlasloot/spoils/items/items_container")
	arg_3_0._item = arg_3_0:findTF("right/infomation/atlasloot/spoils/items/item_tpl")

	SetActive(arg_3_0._item, false)

	arg_3_0._goals = arg_3_0:findTF("right/infomation/target/goal")
	arg_3_0._heroInfo = arg_3_0:getTpl("heroInfo")
	arg_3_0._starTpl = arg_3_0:getTpl("star_tpl")

	setText(findTF(arg_3_0._tf, "middle/gear_score/vanguard/line/Image/Text1"), i18n("pre_combat_vanguard"))
	setText(findTF(arg_3_0._tf, "middle/gear_score/main/line/Image/Text1"), i18n("pre_combat_main"))
	setText(findTF(arg_3_0._tf, "middle/gear_score/submarine/line/Image/text1"), i18n("pre_combat_submarine"))
	setText(arg_3_0._costContainer:Find("title"), i18n("pre_combat_consume"))
	setText(findTF(arg_3_0._tf, "right/infomation/target/title/GameObject"), i18n("pre_combat_targets"))
	setText(findTF(arg_3_0._tf, "right/infomation/atlasloot/atlasloot/title/GameObject"), i18n("pre_combat_atlasloot"))
	setText(arg_3_0._startBtn:Find("text"), i18n("pre_combat_start"))
	setText(arg_3_0._startBtn:Find("text_en"), i18n("pre_combat_start_en"))

	arg_3_0._middle = arg_3_0:findTF("middle")
	arg_3_0._right = arg_3_0:findTF("right")

	setAnchoredPosition(arg_3_0._middle, {
		x = -840
	})
	setAnchoredPosition(arg_3_0._right, {
		x = 470
	})

	arg_3_0.guideDesc = arg_3_0:findTF("guideDesc", arg_3_0._middle)

	if arg_3_0.contextData.stageId then
		arg_3_0:SetStageID(arg_3_0.contextData.stageId)
	end

	arg_3_0._ticket = arg_3_0._startBtn:Find("ticket")
	arg_3_0._bonus = arg_3_0._startBtn:Find("bonus")
	arg_3_0._costTip = arg_3_0._startBtn:Find("cost_container/popup/tip")
	arg_3_0._continuousBtn = arg_3_0:findTF("right/multiple")

	setText(arg_3_0._continuousBtn:Find("text"), i18n("multiple_sorties_title"))
	setText(arg_3_0._continuousBtn:Find("text_en"), i18n("multiple_sorties_title_eng"))
	setText(arg_3_0._ticket:Find("title"), i18n("ex_pass_use"))
	setText(arg_3_0._bonus:Find("title"), i18n("expedition_extra_drop_tip"))
end

function var_0_0.Register(arg_4_0)
	arg_4_0._formationLogic:AddLoadComplete(function()
		if arg_4_0._currentForm ~= PreCombatLayer.FORM_EDIT then
			arg_4_0._formationLogic:SwitchToPreviewMode()
		end
	end)
	arg_4_0._formationLogic:AddHeroInfoModify(function(arg_6_0, arg_6_1)
		setAnchoredPosition(arg_6_0, {
			x = 0,
			y = 0
		})
		SetActive(arg_6_0, true)

		arg_6_0.name = "info"

		local var_6_0 = findTF(arg_6_0, "info")
		local var_6_1 = findTF(var_6_0, "stars")
		local var_6_2 = arg_6_1.energy <= Ship.ENERGY_MID
		local var_6_3 = findTF(var_6_0, "energy")

		if var_6_2 then
			local var_6_4, var_6_5 = arg_6_1:getEnergyPrint()
			local var_6_6 = GetSpriteFromAtlas("energy", var_6_4)

			if not var_6_6 then
				warning("找不到疲劳")
			end

			setImageSprite(var_6_3, var_6_6)
		end

		local var_6_7 = arg_4_0.contextData.system
		local var_6_8 = pg.battle_cost_template[var_6_7]

		setActive(var_6_3, var_6_2 and var_6_8.enter_energy_cost > 0)

		local var_6_9 = arg_6_1:getStar()

		for iter_6_0 = 1, var_6_9 do
			cloneTplTo(arg_4_0._starTpl, var_6_1)
		end

		local var_6_10 = GetSpriteFromAtlas("shiptype", shipType2print(arg_6_1:getShipType()))

		if not var_6_10 then
			warning("找不到船形, shipConfigId: " .. arg_6_1.configId)
		end

		setImageSprite(findTF(var_6_0, "type"), var_6_10, true)
		setText(findTF(var_6_0, "frame/lv_contain/lv"), arg_6_1.level)

		if var_6_8.ship_exp_award > 0 then
			local var_6_11 = getProxy(ActivityProxy):getBuffShipList()[arg_6_1:getGroupId()]
			local var_6_12 = var_6_0:Find("expbuff")

			setActive(var_6_12, var_6_11 ~= nil)

			if var_6_11 then
				local var_6_13 = var_6_11 / 100
				local var_6_14 = var_6_11 % 100
				local var_6_15 = tostring(var_6_13)

				if var_6_14 > 0 then
					var_6_15 = var_6_15 .. "." .. tostring(var_6_14)
				end

				setText(var_6_12:Find("text"), string.format("EXP +%s%%", var_6_15))
			end
		else
			local var_6_16 = var_6_0:Find("expbuff")

			setActive(var_6_16, false)
		end
	end)
	arg_4_0._formationLogic:AddLongPress(function(arg_7_0, arg_7_1, arg_7_2, arg_7_3)
		arg_4_0:emit(ActivityBossPreCombatMediator.OPEN_SHIP_INFO, arg_7_1.id, arg_7_2)
	end)
	arg_4_0._formationLogic:AddBeginDrag(function(arg_8_0)
		local var_8_0 = findTF(arg_8_0, "info")

		SetActive(var_8_0, false)
	end)
	arg_4_0._formationLogic:AddEndDrag(function(arg_9_0)
		local var_9_0 = findTF(arg_9_0, "info")

		SetActive(var_9_0, true)
	end)
	arg_4_0._formationLogic:AddClick(function(arg_10_0, arg_10_1, arg_10_2)
		return
	end)
	arg_4_0._formationLogic:AddShiftOnly(function(arg_11_0)
		arg_4_0:emit(ActivityBossPreCombatMediator.CHANGE_FLEET_SHIPS_ORDER, arg_11_0)
	end)
	arg_4_0._formationLogic:AddRemoveShip(function(arg_12_0, arg_12_1)
		return
	end)
	arg_4_0._formationLogic:AddCheckRemove(function(arg_13_0, arg_13_1, arg_13_2, arg_13_3, arg_13_4)
		arg_13_0()
	end)
	arg_4_0._formationLogic:AddSwitchToDisplayMode(function()
		arg_4_0._currentForm = PreCombatLayer.FORM_EDIT
		arg_4_0._checkBtn:GetComponent("Button").interactable = true

		arg_4_0:SetFleetStepper()
		setActive(arg_4_0._checkBtn:Find("save"), true)
		setActive(arg_4_0._checkBtn:Find("edit"), false)
	end)
	arg_4_0._formationLogic:AddSwitchToShiftMode(function()
		arg_4_0:SetFleetStepper()

		arg_4_0._checkBtn:GetComponent("Button").interactable = false
	end)
	arg_4_0._formationLogic:AddSwitchToPreviewMode(function()
		arg_4_0._currentForm = PreCombatLayer.FORM_PREVIEW
		arg_4_0._checkBtn:GetComponent("Button").interactable = true

		arg_4_0:SetFleetStepper()
		setActive(arg_4_0._checkBtn:Find("save"), false)
		setActive(arg_4_0._checkBtn:Find("edit"), true)
	end)
	arg_4_0._formationLogic:AddGridTipClick(function(arg_17_0, arg_17_1)
		return
	end)

	if arg_4_0.contextData.system == SYSTEM_ACT_BOSS then
		arg_4_0._formationLogic:DisableTip()
	end
end

function var_0_0.SetPlayerInfo(arg_18_0, arg_18_1)
	return
end

function var_0_0.SetSubFlag(arg_19_0, arg_19_1)
	arg_19_0._subUseable = arg_19_1 or false
end

function var_0_0.SetShips(arg_20_0, arg_20_1)
	arg_20_0._shipVOs = arg_20_1

	arg_20_0._formationLogic:SetShipVOs(arg_20_0._shipVOs)
end

function var_0_0.SetStageID(arg_21_0, arg_21_1)
	removeAllChildren(arg_21_0._spoilsContainer)

	arg_21_0._stageID = arg_21_1

	local var_21_0 = pg.expedition_data_template[arg_21_1]
	local var_21_1 = Clone(var_21_0.award_display)
	local var_21_2 = checkExist(pg.expedition_activity_template[arg_21_1], {
		"pt_drop_display"
	})

	if var_21_2 and type(var_21_2) == "table" then
		local var_21_3 = getProxy(ActivityProxy)

		for iter_21_0 = #var_21_2, 1, -1 do
			local var_21_4 = var_21_3:getActivityById(var_21_2[iter_21_0][1])

			if var_21_4 and not var_21_4:isEnd() then
				table.insert(var_21_1, 1, {
					2,
					id2ItemId(var_21_2[iter_21_0][2])
				})
			end
		end
	end

	if arg_21_0.contextData.system ~= SYSTEM_BOSS_EXPERIMENT then
		for iter_21_1, iter_21_2 in ipairs(var_21_1) do
			local var_21_5 = cloneTplTo(arg_21_0._item, arg_21_0._spoilsContainer)
			local var_21_6 = {
				id = iter_21_2[2],
				type = iter_21_2[1]
			}

			updateDrop(var_21_5, var_21_6)
			onButton(arg_21_0, var_21_5, function()
				local var_22_0 = Item.getConfigData(iter_21_2[2])

				if var_22_0 and var_0_2[var_22_0.type] then
					local var_22_1 = var_22_0.display_icon
					local var_22_2 = {}

					for iter_22_0, iter_22_1 in ipairs(var_22_1) do
						local var_22_3 = iter_22_1[1]
						local var_22_4 = iter_22_1[2]

						var_22_2[#var_22_2 + 1] = {
							hideName = true,
							type = var_22_3,
							id = var_22_4
						}
					end

					arg_21_0:emit(var_0_0.ON_DROP_LIST, {
						item2Row = true,
						itemList = var_22_2,
						content = var_22_0.display
					})
				else
					arg_21_0:emit(var_0_0.ON_DROP, var_21_6)
				end
			end, SFX_PANEL)
		end
	end

	local function var_21_7(arg_23_0, arg_23_1)
		if type(arg_23_0) == "table" then
			setActive(arg_23_1, true)

			local var_23_0 = i18n(PreCombatLayer.ObjectiveList[arg_23_0[1]], arg_23_0[2])

			setWidgetText(arg_23_1, var_23_0)
		else
			setActive(arg_23_1, false)
		end
	end

	local var_21_8 = {
		findTF(arg_21_0._goals, "goal_tpl"),
		findTF(arg_21_0._goals, "goal_sink"),
		findTF(arg_21_0._goals, "goal_time")
	}
	local var_21_9 = {
		var_21_0.objective_1,
		var_21_0.objective_2,
		var_21_0.objective_3
	}
	local var_21_10 = 1

	for iter_21_3, iter_21_4 in ipairs(var_21_9) do
		if type(iter_21_4) ~= "string" then
			var_21_7(iter_21_4, var_21_8[var_21_10])

			var_21_10 = var_21_10 + 1
		end
	end

	for iter_21_5 = var_21_10, #var_21_8 do
		var_21_7("", var_21_8[iter_21_5])
	end

	local var_21_11 = var_21_0.guide_desc and #var_21_0.guide_desc > 0

	setActive(arg_21_0.guideDesc, var_21_11)

	if var_21_11 then
		setText(arg_21_0.guideDesc, var_21_0.guide_desc)
	end
end

function var_0_0.SetFleets(arg_24_0, arg_24_1)
	local var_24_0 = _.filter(_.values(arg_24_1), function(arg_25_0)
		return arg_25_0:getFleetType() == FleetType.Normal
	end)

	arg_24_0._fleetVOs = {}

	_.each(var_24_0, function(arg_26_0)
		arg_24_0._fleetVOs[arg_26_0.id] = arg_26_0
	end)
	arg_24_0:CheckLegalFleet()
end

function var_0_0.SetCurrentFleet(arg_27_0, arg_27_1)
	arg_27_0._currentFleetVO = arg_27_0._fleetVOs[arg_27_1]

	arg_27_0._formationLogic:SetFleetVO(arg_27_0._currentFleetVO)
	arg_27_0:CheckLegalFleet()

	for iter_27_0, iter_27_1 in ipairs(arg_27_0._legalFleetIdList) do
		if arg_27_0._currentFleetVO.id == iter_27_1 then
			arg_27_0._curFleetIndex = iter_27_0

			break
		end
	end
end

function var_0_0.SetTicketItemID(arg_28_0, arg_28_1)
	arg_28_0._ticketItemID = arg_28_1
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
		arg_35_0:emit(ActivityBossPreCombatMediator.ON_ABORT_EDIT)
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
						arg_36_0:emit(ActivityBossPreCombatMediator.ON_COMMIT_EDIT, function()
							pg.TipsMgr.GetInstance():ShowTips(i18n("battle_preCombatLayer_save_success"))
							arg_38_0()
						end)
					end,
					onNo = function()
						arg_36_0:emit(ActivityBossPreCombatMediator.ON_ABORT_EDIT)
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
						arg_36_0:emit(ActivityBossPreCombatMediator.ON_COMMIT_EDIT, function()
							pg.TipsMgr.GetInstance():ShowTips(i18n("battle_preCombatLayer_save_success"))
							arg_45_0()
						end)
					end
				})
			end)
		end

		seriesAsync(var_44_0, function()
			arg_36_0:emit(ActivityBossPreCombatMediator.ON_START, arg_36_0._currentFleetVO.id)
		end)
	end, SFX_UI_WEIGHANCHOR)
	onButton(arg_36_0, arg_36_0._checkBtn, function()
		if arg_36_0._currentForm == PreCombatLayer.FORM_EDIT then
			arg_36_0:emit(ActivityBossPreCombatMediator.ON_COMMIT_EDIT, function()
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
		arg_36_0:emit(ActivityBossPreCombatMediator.ON_AUTO, {
			isOn = not arg_51_0,
			toggle = arg_36_0._autoToggle
		})

		if arg_51_0 and arg_36_0._subUseable == true then
			setActive(arg_36_0._autoSubToggle, true)
			onToggle(arg_36_0, arg_36_0._autoSubToggle, function(arg_52_0)
				arg_36_0:emit(ActivityBossPreCombatMediator.ON_SUB_AUTO, {
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

	setActive(arg_36_0._continuousBtn, arg_36_0.contextData.system == SYSTEM_ACT_BOSS)

	local var_36_2 = var_36_1 and var_36_1:IsOilLimit(var_36_0)

	setActive(arg_36_0._continuousBtn:Find("lock"), not var_36_2)

	local var_36_3 = var_36_2 and Color.white or Color.New(0.2980392156862745, 0.2980392156862745, 0.2980392156862745)

	setImageColor(arg_36_0._continuousBtn, var_36_3)
	setTextColor(arg_36_0._continuousBtn:Find("text"), var_36_3)
	setTextColor(arg_36_0._continuousBtn:Find("text_en"), var_36_3)
	onButton(arg_36_0, arg_36_0._continuousBtn, function()
		if var_36_2 then
			arg_36_0:emit(ActivityBossPreCombatMediator.SHOW_CONTINUOUS_OPERATION_WINDOW, arg_36_0._currentFleetVO.id)
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
	setText(arg_55_0._fleetNameText, var_0_1.defaultFleetName(arg_55_0._currentFleetVO))
	setText(arg_55_0._fleetNumText, arg_55_0._currentFleetVO.id)

	local var_55_7 = arg_55_0.contextData.stageId
	local var_55_8 = getProxy(ActivityProxy):getActivityById(arg_55_0.contextData.actId):GetStageBonus(var_55_7)

	setActive(arg_55_0._bonus, var_55_8 > 0)
	setActive(arg_55_0._ticket, var_55_8 <= 0)
	setText(arg_55_0._bonus:Find("Text"), var_55_8)

	if var_55_8 <= 0 then
		local var_55_9 = Drop.New({
			type = DROP_TYPE_RESOURCE,
			id = arg_55_0._ticketItemID
		}):getIcon()
		local var_55_10 = LoadSprite(var_55_9, "")

		setImageSprite(arg_55_0._ticket:Find("icon"), var_55_10)

		local var_55_11 = getProxy(PlayerProxy):getRawData():getResource(arg_55_0._ticketItemID)
		local var_55_12 = 1
		local var_55_13 = arg_55_0._ticket:Find("checkbox")

		if var_55_5 == SYSTEM_BOSS_EXPERIMENT then
			var_55_12 = 0

			triggerToggle(var_55_13, false)
			setToggleEnabled(var_55_13, false)
		elseif var_55_5 == SYSTEM_HP_SHARE_ACT_BOSS then
			triggerToggle(var_55_13, true)
			setToggleEnabled(var_55_13, false)
		elseif var_55_5 == SYSTEM_ACT_BOSS_SP then
			setActive(arg_55_0._ticket, false)
		elseif var_55_5 == SYSTEM_ACT_BOSS then
			local var_55_14 = var_55_11 > 0
			local var_55_15 = getProxy(SettingsProxy):isTipActBossExchangeTicket() == 1

			setToggleEnabled(var_55_13, var_55_14)
			triggerToggle(var_55_13, var_55_14 and var_55_15)
		end

		var_55_11 = var_55_11 < var_55_12 and setColorStr(var_55_11, COLOR_RED) or var_55_11

		setText(arg_55_0._ticket:Find("Text"), var_55_12 .. "/" .. var_55_11)
		onToggle(arg_55_0, var_55_13, function(arg_56_0)
			getProxy(SettingsProxy):setActBossExchangeTicketTip(arg_56_0 and 1 or 0)
		end, SFX_PANEL, SFX_CANCEL)
	end

	local var_55_16 = pg.battle_cost_template[var_55_5].oil_cost > 0
	local var_55_17 = 0
	local var_55_18 = 0
	local var_55_19 = false

	for iter_55_0, iter_55_1 in ipairs({
		arg_55_0.contextData.fleets[1]
	}) do
		local var_55_20 = iter_55_1:GetCostSum().oil

		if not var_55_16 then
			var_55_20 = 0
		end

		var_55_18 = var_55_18 + var_55_20

		local var_55_21 = iter_55_0 == 1
		local var_55_22 = arg_55_0.contextData.costLimit[var_55_21 and 1 or 2]

		if var_55_22 > 0 then
			var_55_19 = var_55_19 or var_55_22 < var_55_20
			var_55_20 = math.min(var_55_20, var_55_22)
		end

		var_55_17 = var_55_17 + var_55_20
	end

	setTextColor(arg_55_0._costText, var_55_19 and Color(0.9803921568627451, 0.39215686274509803, 0.39215686274509803) or Color.white)
	var_0_1.tweenNumText(arg_55_0._costText, var_55_17)
	setActive(arg_55_0._costTip, var_55_19)

	if var_55_19 then
		onButton(arg_55_0, arg_55_0._costTip, function()
			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				hideNo = true,
				content = i18n("use_oil_limit_help", var_55_18, var_55_17),
				weight = LayerWeightConst.SECOND_LAYER
			})
		end)
	end

	setText(arg_55_0._fleetNameText, Fleet.DEFAULT_NAME_BOSS_ACT[arg_55_0._currentFleetVO.id])
end

function var_0_0.SetFleetStepper(arg_58_0)
	SetActive(arg_58_0._nextPage, false)
	SetActive(arg_58_0._prevPage, false)
end

function var_0_0.onBackPressed(arg_59_0)
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CANCEL)
	triggerButton(arg_59_0._backBtn)
end

function var_0_0.willExit(arg_60_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_60_0._tf)
	arg_60_0._formationLogic:Destroy()

	arg_60_0._formationLogic = nil
end

return var_0_0
