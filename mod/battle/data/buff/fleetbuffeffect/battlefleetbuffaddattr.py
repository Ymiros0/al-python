ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleFleetBuffInk = class("BattleFleetBuffInk", var_0_0.Battle.BattleFleetBuffEffect)
var_0_0.Battle.BattleFleetBuffInk.__name = "BattleFleetBuffInk"

local var_0_1 = var_0_0.Battle.BattleFleetBuffInk

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.onAttach(arg_2_0, arg_2_1, arg_2_2):
	arg_2_1.Blinding(True)
	arg_2_1.SetWeaponBlock(1)

def var_0_1.onRemove(arg_3_0, arg_3_1, arg_3_2):
	arg_3_1.Blinding(False)
	arg_3_1.SetWeaponBlock(-1)
