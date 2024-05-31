ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffStun = class("BattleBuffStun", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffStun.__name = "BattleBuffStun"

local var_0_1 = var_0_0.Battle.BattleBuffStun

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0._tempData.arg_list

def var_0_1.onAttach(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0.onTrigger(arg_3_1, arg_3_2)

def var_0_1.onUpdate(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0.onTrigger(arg_4_1, arg_4_2)

def var_0_1.onTrigger(arg_5_0, arg_5_1, arg_5_2):
	var_0_1.super.onTrigger(arg_5_0, arg_5_1, arg_5_2)
	var_0_0.Battle.BattleAttr.Stun(arg_5_1)
	arg_5_1.UpdateMoveLimit()

def var_0_1.onRemove(arg_6_0, arg_6_1, arg_6_2):
	var_0_0.Battle.BattleAttr.CancelStun(arg_6_1)
	arg_6_1.UpdateMoveLimit()
