ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleCardPuzzleFormulas
local var_0_2 = class("BattleCardPuzzleSkillSetFleetAttr", var_0_0.Battle.BattleCardPuzzleSkillEffect)

var_0_0.Battle.BattleCardPuzzleSkillSetFleetAttr = var_0_2
var_0_2.__name = "BattleCardPuzzleSkillSetFleetAttr"

def var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_2.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._attr = arg_1_0._tempData.arg_list.attr
	arg_1_0._number = arg_1_0._tempData.arg_list.number
	arg_1_0._enhance = arg_1_0._tempData.arg_list.enhance_formula

def var_0_2.SkillEffectHandler(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_0._number

	if arg_2_0._enhance:
		var_2_0 = var_2_0 + var_0_1.parseFormula(arg_2_0._enhance, arg_2_0.GetCardPuzzleComponent().GetAttrManager())

	arg_2_0.GetCardPuzzleComponent().UpdateAttrBySet(arg_2_0._attr, var_2_0)
	arg_2_0.Finale()
