ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleSubmarineAidVO = class("BattleSubmarineAidVO", var_0_0.Battle.BattlePlayerWeaponVO)
var_0_0.Battle.BattleSubmarineAidVO.__name = "BattleSubmarineAidVO"

local var_0_2 = var_0_0.Battle.BattleSubmarineAidVO

var_0_2.GCD = var_0_1.AirAssistCFG.GCD

def var_0_2.Ctor(arg_1_0):
	var_0_2.super.Ctor(arg_1_0, var_0_2.GCD)

def var_0_2.SetUseable(arg_2_0, arg_2_1):
	arg_2_0._useable = arg_2_1
	arg_2_0._current = arg_2_1 and 1 or 0
	arg_2_0._max = 1

	arg_2_0.DispatchOverLoadChange()
	arg_2_0.DispatchCountChange()

def var_0_2.GetUseable(arg_3_0):
	return arg_3_0._useable

def var_0_2.IsOverLoad(arg_4_0):
	return arg_4_0._current < arg_4_0._max or arg_4_0._count < 1

def var_0_2.Cast(arg_5_0):
	arg_5_0._count = arg_5_0._count - 1

	arg_5_0.resetCurrent()
	arg_5_0.DispatchOverLoadChange()
	arg_5_0.DispatchCountChange()
