ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffSetAttr = class("BattleBuffSetAttr", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffSetAttr.__name = "BattleBuffSetAttr"

local var_0_1 = var_0_0.Battle.BattleBuffSetAttr
local var_0_2 = var_0_0.Battle.BattleAttr

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._attr = arg_2_0._tempData.arg_list.attr
	arg_2_0._value = arg_2_0._tempData.arg_list.value

def var_0_1.onAttach(arg_3_0, arg_3_1, arg_3_2):
	if arg_3_0._attr == "TargetChoise":
		var_0_2.AddTargetSelect(arg_3_1, arg_3_0._value)
	else
		var_0_2.SetCurrent(arg_3_1, arg_3_0._attr, arg_3_0._value)

def var_0_1.onRemove(arg_4_0, arg_4_1, arg_4_2):
	if arg_4_0._attr == "TargetChoise":
		var_0_2.RemoveTargetSelect(arg_4_1, arg_4_0._value)
	else
		var_0_2.SetCurrent(arg_4_1, arg_4_0._attr, 0)
