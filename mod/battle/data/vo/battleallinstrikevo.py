ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleAllInStrikeVO = class("BattleAllInStrikeVO", var_0_0.Battle.BattlePlayerWeaponVO)
var_0_0.Battle.BattleAllInStrikeVO.__name = "BattleAllInStrikeVO"

local var_0_2 = var_0_0.Battle.BattleAllInStrikeVO

var_0_2.GCD = var_0_1.AirAssistCFG.GCD

def var_0_2.Ctor(arg_1_0):
	var_0_2.super.Ctor(arg_1_0, var_0_2.GCD)

def var_0_2.AppendWeapon(arg_2_0, arg_2_1):
	arg_2_1.SetAllInWeaponVO(arg_2_0)
	var_0_2.super.AppendWeapon(arg_2_0, arg_2_1)

def var_0_2.GetCurrentWeaponIconIndex(arg_3_0):
	return 3
