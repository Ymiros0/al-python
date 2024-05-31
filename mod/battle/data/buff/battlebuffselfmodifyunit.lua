ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleBuffEvent
local var_0_2 = var_0_0.Battle.BattleConst.BuffEffectType
local var_0_3 = class("BattleBuffSelfModifyUnit", var_0_0.Battle.BattleBuffUnit)

var_0_0.Battle.BattleBuffSelfModifyUnit = var_0_3
var_0_3.__name = "BattleBuffSelfModifyUnit"

function var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4)
	arg_1_0._selfModifyTempData = arg_1_4

	var_0_3.super.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4)
end

function var_0_3.SetTemplate(arg_2_0)
	arg_2_0._tempData = arg_2_0._selfModifyTempData
end
