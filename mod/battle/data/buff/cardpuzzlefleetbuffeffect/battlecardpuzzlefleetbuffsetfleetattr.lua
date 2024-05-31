ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleCardPuzzleFleetBuffSetFleetAttr", var_0_0.Battle.BattleFleetBuffEffect)

var_0_0.Battle.BattleCardPuzzleFleetBuffSetFleetAttr = var_0_1
var_0_1.__name = "BattleCardPuzzleFleetBuffSetFleetAttr"
var_0_1.FX_TYPE = var_0_0.Battle.BattleBuffEffect.FX_TYPE_MOD_ATTR

function var_0_1.Ctor(arg_1_0, arg_1_1)
	arg_1_0._tempData = Clone(arg_1_1)
	arg_1_0._type = arg_1_0._tempData.type

	arg_1_0:SetActive()
end

function var_0_1.GetEffectType(arg_2_0)
	return var_0_1.FX_TYPE
end

function var_0_1.SetArgs(arg_3_0, arg_3_1, arg_3_2)
	var_0_1.super.SetArgs(arg_3_0, arg_3_1, arg_3_2)

	arg_3_0._group = arg_3_0._tempData.arg_list.group or arg_3_0._fleetBuff:GetID()
	arg_3_0._attr = arg_3_0._tempData.arg_list.attr
	arg_3_0._number = arg_3_0._tempData.arg_list.number

	if arg_3_0._tempData.arg_list.enhance_formula then
		local var_3_0 = arg_3_0._tempData.arg_list.enhance_formula

		arg_3_0._number = DBGformula.parseFormula(var_3_0, arg_3_1:GetAttrManager()) + arg_3_0._number
	end

	arg_3_0._cache = arg_3_0._tempData.arg_list.maintain
	arg_3_0._numberBase = arg_3_0._number
end

function var_0_1.onRemove(arg_4_0)
	if arg_4_0._cache then
		arg_4_0._number = 0
	end

	arg_4_0:onTrigger()
end

function var_0_1.GetGroup(arg_5_0)
	return arg_5_0._group
end

function var_0_1.GetNumber(arg_6_0)
	return arg_6_0._number * arg_6_0._fleetBuff:GetStack()
end

function var_0_1.IsSameAttr(arg_7_0, arg_7_1)
	return arg_7_0._attr == arg_7_1
end

function var_0_1.onTrigger(arg_8_0)
	arg_8_0._cardPuzzleComponent:UpdateAttrBySet(arg_8_0._attr, arg_8_0:GetNumber())
end
