ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleBuffGuarded", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffGuarded = var_0_1
var_0_1.__name = "BattleBuffGuarded"

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._casterUID = arg_2_2.GetCaster().GetUniqueID()

def var_0_1.onAttach(arg_3_0, arg_3_1, arg_3_2):
	var_0_0.Battle.BattleAttr.AddGuardianID(arg_3_1, arg_3_0._casterUID)

def var_0_1.onRemove(arg_4_0, arg_4_1, arg_4_2):
	var_0_0.Battle.BattleAttr.RemoveGuardianID(arg_4_1, arg_4_0._casterUID)
