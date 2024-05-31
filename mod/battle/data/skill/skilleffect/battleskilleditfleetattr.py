ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleSkillEditFleetAttr", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillEditFleetAttr = var_0_1
var_0_1.__name = "BattleSkillEditFleetAttr"

def var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_1.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._fleetAttrName = arg_1_0._tempData.arg_list.attr
	arg_1_0._value = arg_1_0._tempData.arg_list.value

def var_0_1.DoDataEffect(arg_2_0, arg_2_1, arg_2_2):
	if arg_2_1.GetFleetVO():
		local var_2_0 = arg_2_1.GetFleetVO().GetFleetAttr()
		local var_2_1 = var_2_0.GetCurrent(arg_2_0._fleetAttrName) + arg_2_0._value

		var_2_0.SetCurrent(arg_2_0._fleetAttrName, var_2_1)
