ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffAirStrikeCoolDown = class("BattleBuffAirStrikeCoolDown", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffAirStrikeCoolDown.__name = "BattleBuffAirStrikeCoolDown"

local var_0_1 = var_0_0.Battle.BattleBuffAirStrikeCoolDown

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._rant = arg_2_0._tempData.arg_list.rant or 10000

def var_0_1.onTrigger(arg_3_0, arg_3_1):
	var_0_1.super.onTrigger(arg_3_0, arg_3_1, buff, attach)

	if var_0_0.Battle.BattleFormulas.IsHappen(arg_3_0._rant):
		local var_3_0 = arg_3_1.GetAirAssistQueue().GetQueueHead()

		if var_3_0:
			var_3_0.QuickCoolDown()
