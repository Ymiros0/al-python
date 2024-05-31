ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleFleetBuffFixSubRefLine = class("BattleFleetBuffFixSubRefLine", var_0_0.Battle.BattleFleetBuffEffect)
var_0_0.Battle.BattleFleetBuffFixSubRefLine.__name = "BattleFleetBuffFixSubRefLine"

local var_0_1 = var_0_0.Battle.BattleFleetBuffFixSubRefLine

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.onAttach(arg_2_0, arg_2_1, arg_2_2):
	arg_2_1.FixSubRefLine(arg_2_0._tempData.arg_list.line)

def var_0_1.onRemove(arg_3_0, arg_3_1, arg_3_2):
	arg_3_1.FixSubRefLine()
