ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = class("BattleTriggerAOEData", var_0_0.Battle.BattleAOEData)

var_0_0.Battle.BattleTriggerAOEData = var_0_2
var_0_2.__name = "BattleTriggerAOEData"

def var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	var_0_2.super.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)

def var_0_2.Settle(arg_2_0):
	if #arg_2_0._cldObjList > 0:
		arg_2_0.SortCldObjList(arg_2_0._cldObjList)
		arg_2_0._cldComponent.GetCldData().func(arg_2_0._cldObjList)

		arg_2_0._flag = False
