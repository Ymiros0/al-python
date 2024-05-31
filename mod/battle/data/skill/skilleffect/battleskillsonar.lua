ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = class("BattleSkillSonar", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillSonar = var_0_2
var_0_2.__name = "BattleSkillSonar"

function var_0_2.Ctor(arg_1_0, arg_1_1)
	var_0_2.super.Ctor(arg_1_0, arg_1_1, lv)

	arg_1_0._range = arg_1_0._tempData.arg_list.range
	arg_1_0._duration = arg_1_0._tempData.arg_list.duration
end

function var_0_2.DoDataEffect(arg_2_0, arg_2_1)
	arg_2_1:GetFleetVO():AppendIndieSonar(arg_2_0._range, arg_2_0._duration)
end

function var_0_2.DataEffectWithoutTarget(arg_3_0, arg_3_1)
	arg_3_1:GetFleetVO():AppendIndieSonar(arg_3_0._range, arg_3_0._duration)
end
