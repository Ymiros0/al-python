ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleSkillConsumeBuff = class("BattleSkillConsumeBuff", var_0_0.Battle.BattleSkillEffect)
var_0_0.Battle.BattleSkillConsumeBuff.__name = "BattleSkillConsumeBuff"

local var_0_1 = var_0_0.Battle.BattleSkillConsumeBuff

function var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_1.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._buffID = arg_1_0._tempData.arg_list.buff_id
	arg_1_0._count = arg_1_0._tempData.arg_list.consume_count
end

function var_0_1.DoDataEffect(arg_2_0, arg_2_1, arg_2_2)
	if arg_2_2:IsAlive() then
		arg_2_2:ConsumeBuffStack(arg_2_0._buffID, arg_2_0._count)
	end
end
