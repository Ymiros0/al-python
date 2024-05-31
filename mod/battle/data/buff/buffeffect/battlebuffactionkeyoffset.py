ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffActionKeyOffset = class("BattleBuffActionKeyOffset", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffActionKeyOffset.__name = "BattleBuffActionKeyOffset"

local var_0_1 = var_0_0.Battle.BattleBuffActionKeyOffset

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._actionKey = arg_2_0._tempData.arg_list.key

def var_0_1.onAttach(arg_3_0, arg_3_1, arg_3_2):
	if arg_3_1.ActionKeyOffsetUseable():
		arg_3_1.SetActionKeyOffset(arg_3_0._actionKey)

def var_0_1.onRemove(arg_4_0, arg_4_1, arg_4_2):
	if arg_4_1.ActionKeyOffsetUseable():
		arg_4_1.SetActionKeyOffset(None)
