ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleAttr

var_0_0.Battle.DiveOxyState = class("DiveOxyState", var_0_0.Battle.IOxyState)
var_0_0.Battle.DiveOxyState.__name = "DiveOxyState"

local var_0_3 = var_0_0.Battle.DiveOxyState

def var_0_3.Ctor(arg_1_0):
	var_0_3.super.Ctor(arg_1_0)

def var_0_3.GetWeaponUseableList(arg_2_0):
	return {}

def var_0_3.UpdateCldData(arg_3_0, arg_3_1, arg_3_2):
	local var_3_0 = arg_3_2.GetDiveState()
	local var_3_1 = arg_3_0.GetDiveState()

	arg_3_1.GetCldData().Surface = var_3_1

	if var_3_0 != var_3_1:
		var_0_2.UnitCldImmune(arg_3_1)

def var_0_3.GetDiveState(arg_4_0):
	return var_0_1.OXY_STATE.DIVE

def var_0_3.GetBubbleFlag(arg_5_0):
	return True

def var_0_3.IsVisible(arg_6_0):
	return False

def var_0_3.GetBarVisible(arg_7_0):
	return True

def var_0_3.RunMode(arg_8_0):
	return False
