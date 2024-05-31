ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleBuffAntiSubMine", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffAntiSubMine = var_0_1
var_0_1.__name = "BattleBuffAntiSubMine"

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.onAttach(arg_2_0, arg_2_1):
	arg_2_1.InitOxygen()
	arg_2_1.ChangeOxygenState(var_0_0.Battle.OxyState.STATE_DEEP_MINE)
