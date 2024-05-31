local var_0_0 = class("PreCombatLayerSubmarine", import(".PreCombatLayer"))
local var_0_1 = import("..ship.FormationUI")

var_0_0.FORM_EDIT = "EDIT"
var_0_0.FORM_PREVIEW = "PREVIEW"

function var_0_0.getUIName(arg_1_0)
	return "PreCombatUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0:CommonInit()

	local var_2_0 = arg_2_0:findTF("middle")
	local var_2_1 = var_2_0:Find("mask/grid_bg")

	SetActive(var_2_1, false)
	SetActive(var_2_0:Find("gear_score/main"), false)
	SetActive(var_2_0:Find("gear_score/vanguard"), false)
	SetActive(var_2_0:Find("gear_score/submarine"), true)

	arg_2_0._subBg = var_2_0:Find("mask/bg_sub")
	arg_2_0._subFrame = var_2_0:Find("mask/GridFrame")

	SetActive(arg_2_0._subBg, true)

	arg_2_0._formationLogic = BaseFormation.New(arg_2_0._tf, arg_2_0._heroContainer, arg_2_0._heroInfo, arg_2_0._gridTFs)

	arg_2_0:Register()
end

function var_0_0.SetFleets(arg_3_0, arg_3_1)
	local var_3_0 = _.filter(_.values(arg_3_1), function(arg_4_0)
		return arg_4_0:getFleetType() == FleetType.Submarine
	end)

	arg_3_0._fleetVOs = {}
	arg_3_0._fleetIDList = {}

	local var_3_1 = 0

	_.each(var_3_0, function(arg_5_0)
		if #arg_5_0.ships > 0 then
			arg_3_0._fleetVOs[arg_5_0.id] = arg_5_0

			table.insert(arg_3_0._fleetIDList, arg_5_0.id)

			var_3_1 = var_3_1 + 1
		end
	end)

	if var_3_1 == 0 then
		arg_3_0._fleetVOs[11] = var_3_0[1]

		table.insert(arg_3_0._fleetIDList, 11)
	else
		table.sort(arg_3_0._fleetIDList, function(arg_6_0, arg_6_1)
			return arg_6_0 < arg_6_1
		end)
	end
end

function var_0_0.SetCurrentFleet(arg_7_0, arg_7_1)
	arg_7_1 = arg_7_1 or arg_7_0._fleetIDList[1]
	arg_7_0._currentFleetVO = arg_7_0._fleetVOs[arg_7_1]

	arg_7_0._formationLogic:SetFleetVO(arg_7_0._currentFleetVO)
end

function var_0_0.UpdateFleetView(arg_8_0, arg_8_1)
	arg_8_0:displayFleetInfo()
	arg_8_0._formationLogic:UpdateGridVisibility()
	arg_8_0._formationLogic:ResetGrid(TeamType.Submarine, arg_8_0._currentForm ~= var_0_0.FORM_EDIT)

	if arg_8_1 then
		arg_8_0._formationLogic:LoadAllCharacter()
	else
		arg_8_0._formationLogic:SetAllCharacterPos()
	end
end

function var_0_0.didEnter(arg_9_0)
	onButton(arg_9_0, arg_9_0._backBtn, function()
		local var_10_0 = {}

		if arg_9_0._currentForm == var_0_0.FORM_EDIT then
			table.insert(var_10_0, function(arg_11_0)
				pg.MsgboxMgr.GetInstance():ShowMsgBox({
					zIndex = -100,
					hideNo = false,
					content = i18n("battle_preCombatLayer_save_confirm"),
					onYes = function()
						arg_9_0:emit(PreCombatMediator.ON_COMMIT_EDIT, function()
							pg.TipsMgr.GetInstance():ShowTips(i18n("battle_preCombatLayer_save_success"))
							arg_11_0()
						end)
					end,
					onNo = function()
						arg_9_0:emit(PreCombatMediator.ON_ABORT_EDIT)
						arg_11_0()
					end
				})
			end)
		end

		seriesAsync(var_10_0, function()
			GetOrAddComponent(arg_9_0._tf, typeof(CanvasGroup)).interactable = false

			arg_9_0:uiExitAnimating()
			LeanTween.delayedCall(0.3, System.Action(function()
				arg_9_0:emit(var_0_0.ON_CLOSE)
			end))
		end)
	end, SFX_CANCEL)
	onButton(arg_9_0, arg_9_0._startBtn, function()
		local var_17_0 = {}

		if arg_9_0._currentForm == var_0_0.FORM_EDIT then
			table.insert(var_17_0, function(arg_18_0)
				pg.MsgboxMgr.GetInstance():ShowMsgBox({
					zIndex = -100,
					hideNo = false,
					content = i18n("battle_preCombatLayer_save_march"),
					onYes = function()
						arg_9_0:emit(PreCombatMediator.ON_COMMIT_EDIT, function()
							pg.TipsMgr.GetInstance():ShowTips(i18n("battle_preCombatLayer_save_success"))
							arg_18_0()
						end)
					end
				})
			end)
		end

		seriesAsync(var_17_0, function()
			arg_9_0:emit(PreCombatMediator.ON_START, arg_9_0._currentFleetVO.id)
		end)
	end, SFX_UI_WEIGHANCHOR)
	onButton(arg_9_0, arg_9_0._nextPage, function()
		local var_22_0 = arg_9_0:getNextFleetID()

		if var_22_0 then
			arg_9_0:emit(PreCombatMediator.ON_CHANGE_FLEET, var_22_0, true)
		end
	end, SFX_PANEL)
	onButton(arg_9_0, arg_9_0._prevPage, function()
		local var_23_0 = arg_9_0:getPrevFleetID()

		if var_23_0 then
			arg_9_0:emit(PreCombatMediator.ON_CHANGE_FLEET, var_23_0, true)
		end
	end, SFX_PANEL)
	onButton(arg_9_0, arg_9_0._checkBtn, function()
		if arg_9_0._currentForm == var_0_0.FORM_EDIT then
			arg_9_0:emit(PreCombatMediator.ON_COMMIT_EDIT, function()
				pg.TipsMgr.GetInstance():ShowTips(i18n("battle_preCombatLayer_save_success"))
				arg_9_0._formationLogic:SwitchToPreviewMode()
			end)
		elseif arg_9_0._currentForm == var_0_0.FORM_PREVIEW then
			arg_9_0._formationLogic:SwitchToDisplayMode()
		else
			assert("currentForm error")
		end
	end, SFX_PANEL)

	arg_9_0._currentForm = arg_9_0.contextData.form
	arg_9_0.contextData.form = nil

	arg_9_0:UpdateFleetView(true)

	if arg_9_0._currentForm == var_0_0.FORM_EDIT then
		arg_9_0._formationLogic:SwitchToDisplayMode()
	else
		arg_9_0._formationLogic:SwitchToPreviewMode()
	end

	pg.UIMgr.GetInstance():BlurPanel(arg_9_0._tf)
	setActive(arg_9_0._autoToggle, false)
	setActive(arg_9_0._autoSubToggle, false)
	onNextTick(function()
		arg_9_0:uiStartAnimating()
	end)

	if arg_9_0._currentForm == var_0_0.FORM_PREVIEW and arg_9_0.contextData.system == SYSTEM_DUEL and #arg_9_0._currentFleetVO.mainShips <= 0 then
		triggerButton(arg_9_0._checkBtn)
	end
end

function var_0_0.getNextFleetID(arg_27_0)
	local var_27_0

	for iter_27_0, iter_27_1 in ipairs(arg_27_0._fleetIDList) do
		if iter_27_1 == arg_27_0._currentFleetVO.id then
			var_27_0 = iter_27_0

			break
		end
	end

	return arg_27_0._fleetIDList[var_27_0 + 1]
end

function var_0_0.getPrevFleetID(arg_28_0)
	local var_28_0

	for iter_28_0, iter_28_1 in ipairs(arg_28_0._fleetIDList) do
		if iter_28_1 == arg_28_0._currentFleetVO.id then
			var_28_0 = iter_28_0

			break
		end
	end

	return arg_28_0._fleetIDList[var_28_0 - 1]
end

function var_0_0.displayFleetInfo(arg_29_0)
	local var_29_0 = arg_29_0._currentFleetVO:GetPropertiesSum()
	local var_29_1 = arg_29_0._currentFleetVO:GetGearScoreSum(TeamType.Submarine)
	local var_29_2 = arg_29_0._currentFleetVO:GetCostSum()

	setActive(arg_29_0._popup, true)
	var_0_1.tweenNumText(arg_29_0._costText, var_29_2.oil)
	var_0_1.tweenNumText(arg_29_0._subGS, var_29_1)
	setText(arg_29_0._fleetNameText, var_0_1.defaultFleetName(arg_29_0._currentFleetVO))
	setText(arg_29_0._fleetNumText, arg_29_0._currentFleetVO.id - 10)
end

function var_0_0.SetFleetStepper(arg_30_0)
	if arg_30_0._currentForm == var_0_0.FORM_EDIT then
		SetActive(arg_30_0._nextPage, false)
		SetActive(arg_30_0._prevPage, false)
	else
		setActive(arg_30_0._nextPage, arg_30_0:getNextFleetID() ~= nil)
		setActive(arg_30_0._prevPage, arg_30_0:getPrevFleetID() ~= nil)
	end
end

function var_0_0.willExit(arg_31_0)
	if arg_31_0.eventTriggers then
		for iter_31_0, iter_31_1 in pairs(arg_31_0.eventTriggers) do
			ClearEventTrigger(iter_31_0)
		end

		arg_31_0.eventTriggers = nil
	end

	arg_31_0._formationLogic:Destroy()

	arg_31_0._formationLogic = nil

	if arg_31_0.tweens then
		cancelTweens(arg_31_0.tweens)
	end

	pg.UIMgr.GetInstance():UnblurPanel(arg_31_0._tf)

	if arg_31_0._resPanel then
		arg_31_0._resPanel:exit()

		arg_31_0._resPanel = nil
	end
end

return var_0_0
