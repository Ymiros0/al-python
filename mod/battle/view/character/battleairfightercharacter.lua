ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleAirFighterUnit

var_0_0.Battle.BattleAirFighterCharacter = class("BattleAirFighterCharacter", var_0_0.Battle.BattleAircraftCharacter)
var_0_0.Battle.BattleAirFighterCharacter.__name = "BattleAirFighterCharacter"

local var_0_3 = var_0_0.Battle.BattleAirFighterCharacter

function var_0_3.Ctor(arg_1_0)
	var_0_3.super.Ctor(arg_1_0)

	arg_1_0._scaleVector = Vector3(1, 1, 1)
end

function var_0_3.SetUnitData(arg_2_0, arg_2_1)
	arg_2_0._unitData = arg_2_1

	arg_2_0:AddUnitEvent()
	arg_2_1:SetUnVisitable()
end

function var_0_3.AddModel(arg_3_0, arg_3_1)
	arg_3_0:SetGO(arg_3_1)
	arg_3_0:SetBoneList()
	arg_3_0._unitData:ActiveCldBox()
end

function var_0_3.Update(arg_4_0)
	arg_4_0:UpdateMatrix()
	arg_4_0:UpdateUIComponentPosition()
	arg_4_0:UpdateHPPop()
	arg_4_0:UpdateHPPopContainerPosition()
	arg_4_0:UpdateHPBarPosition()
	arg_4_0:UpdatePosition()
	arg_4_0:UpdateHpBar()

	local var_4_0 = arg_4_0._unitData:GetStrikeState()

	if var_4_0 == var_0_2.STRIKE_STATE_DOWN or var_4_0 == var_0_2.STRIKE_STATE_ATTACK or var_4_0 == var_0_2.STRIKE_STATE_UP then
		arg_4_0:UpdateShadow()
	end
end

function var_0_3.AddUnitEvent(arg_5_0)
	var_0_3.super.AddUnitEvent(arg_5_0)
	arg_5_0._unitData:RegisterEventListener(arg_5_0, var_0_1.AIR_STRIKE_STATE_CHANGE, arg_5_0.onStrikeStateChange)
end

function var_0_3.RemoveUnitEvent(arg_6_0)
	var_0_3.super.RemoveUnitEvent(arg_6_0)
	arg_6_0._unitData:UnregisterEventListener(arg_6_0, var_0_1.AIR_STRIKE_STATE_CHANGE)
end

function var_0_3.onStrikeStateChange(arg_7_0)
	local var_7_0 = arg_7_0._unitData:GetStrikeState()

	if var_7_0 == var_0_2.STRIKE_STATE_FLY then
		local var_7_1 = (12 / (arg_7_0._unitData:GetFormationIndex() + 3) + 1) * arg_7_0._unitData:GetSize()

		arg_7_0._scaleVector:Set(var_7_1, var_7_1, var_7_1)

		arg_7_0._tf.localScale = arg_7_0._scaleVector

		arg_7_0._shadow:SetActive(false)
	elseif var_7_0 == var_0_2.STRIKE_STATE_BACK then
		local var_7_2 = arg_7_0._unitData:GetSize()

		arg_7_0._scaleVector:Set(-var_7_2, var_7_2, var_7_2)

		arg_7_0._tf.localScale = arg_7_0._scaleVector

		arg_7_0._HPBar:SetActive(true)
		arg_7_0._shadow:SetActive(true)
	elseif var_7_0 == var_0_2.STRIKE_STATE_DOWN then
		-- block empty
	elseif var_7_0 == var_0_2.STRIKE_STATE_ATTACK then
		-- block empty
	elseif var_7_0 == var_0_2.STRIKE_STATE_UP then
		-- block empty
	elseif var_7_0 == var_0_2.STRIKE_STATE_FREE then
		-- block empty
	elseif var_7_0 == var_0_2.STRIKE_STATE_BACKWARD then
		local var_7_3 = arg_7_0._unitData:GetSize()

		arg_7_0._scaleVector:Set(var_7_3, var_7_3, var_7_3)

		arg_7_0._tf.localScale = arg_7_0._scaleVector
	end
end
