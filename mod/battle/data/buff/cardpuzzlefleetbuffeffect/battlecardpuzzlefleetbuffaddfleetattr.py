ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleCardPuzzleFormulas
local var_0_2 = class("BattleCardPuzzleFleetBuffAddFleetAttr", var_0_0.Battle.BattleFleetBuffEffect)

var_0_0.Battle.BattleCardPuzzleFleetBuffAddFleetAttr = var_0_2
var_0_2.__name = "BattleCardPuzzleFleetBuffAddFleetAttr"
var_0_2.FX_TYPE = var_0_0.Battle.BattleBuffEffect.FX_TYPE_MOD_ATTR

def var_0_2.Ctor(arg_1_0, arg_1_1):
	arg_1_0._tempData = Clone(arg_1_1)
	arg_1_0._type = arg_1_0._tempData.type

	arg_1_0.SetActive()

def var_0_2.GetEffectType(arg_2_0):
	return var_0_2.FX_TYPE

def var_0_2.SetArgs(arg_3_0, arg_3_1, arg_3_2):
	var_0_2.super.SetArgs(arg_3_0, arg_3_1, arg_3_2)

	arg_3_0._group = arg_3_0._tempData.arg_list.group or arg_3_0._fleetBuff.GetID()
	arg_3_0._attr = arg_3_0._tempData.arg_list.attr
	arg_3_0._number = arg_3_0._tempData.arg_list.number

	if arg_3_0._tempData.arg_list.enhance_formula:
		local var_3_0 = arg_3_0._tempData.arg_list.enhance_formula

		arg_3_0._number = var_0_1.parseFormula(var_3_0, arg_3_1.GetAttrManager()) + arg_3_0._number

	arg_3_0._cache = arg_3_0._tempData.arg_list.maintain
	arg_3_0._numberBase = arg_3_0._number

def var_0_2.onRemove(arg_4_0):
	if arg_4_0._cache:
		arg_4_0._number = 0

	arg_4_0.onTrigger()

def var_0_2.GetGroup(arg_5_0):
	return arg_5_0._group

def var_0_2.GetNumber(arg_6_0):
	return arg_6_0._number * arg_6_0._fleetBuff.GetStack()

def var_0_2.IsSameAttr(arg_7_0, arg_7_1):
	return arg_7_0._attr == arg_7_1

def var_0_2.onTrigger(arg_8_0):
	local var_8_0 = arg_8_0._cardPuzzleComponent

	if arg_8_0._cache:
		local var_8_1 = var_8_0.GetBuffManager().GetCardPuzzleBuffList()
		local var_8_2 = 0
		local var_8_3 = 0
		local var_8_4 = {}
		local var_8_5 = {}

		for iter_8_0, iter_8_1 in pairs(var_8_1):
			for iter_8_2, iter_8_3 in ipairs(iter_8_1._effectList):
				if iter_8_3.GetEffectType() == var_0_2.FX_TYPE and iter_8_3.IsSameAttr(arg_8_0._attr):
					local var_8_6 = iter_8_3.GetNumber()
					local var_8_7 = iter_8_3.GetGroup()
					local var_8_8 = var_8_4[var_8_7] or 0
					local var_8_9 = var_8_5[var_8_7] or 0

					if var_8_8 < var_8_6 and var_8_6 > 0:
						var_8_2 = var_8_2 + var_8_6 - var_8_8
						var_8_8 = var_8_6

					if var_8_6 < var_8_9 and var_8_6 < 0:
						var_8_3 = var_8_3 + var_8_6 - var_8_9
						var_8_9 = var_8_6

					var_8_4[var_8_7] = var_8_8
					var_8_5[var_8_7] = var_8_9

		local var_8_10 = var_8_2 + var_8_3

		var_8_0.UpdateAttrByBuff(arg_8_0._attr, var_8_10)
	else
		var_8_0.AddAttrBySkill(arg_8_0._attr, arg_8_0.GetNumber())
