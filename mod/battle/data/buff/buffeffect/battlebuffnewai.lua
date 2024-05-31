ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffNewAI = class("BattleBuffNewAI", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffNewAI.__name = "BattleBuffNewAI"

function var_0_0.Battle.BattleBuffNewAI.Ctor(arg_1_0, arg_1_1)
	var_0_0.Battle.BattleBuffNewAI.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_0.Battle.BattleBuffNewAI.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._AIOnAttach = arg_2_0._tempData.arg_list.ai_onAttach
	arg_2_0._AIOnRemove = arg_2_0._tempData.arg_list.ai_onRemove
end

function var_0_0.Battle.BattleBuffNewAI.onAttach(arg_3_0, arg_3_1, arg_3_2)
	if arg_3_0._AIOnAttach then
		arg_3_1:SetAI(arg_3_0._AIOnAttach)
	end
end

function var_0_0.Battle.BattleBuffNewAI.onRemove(arg_4_0, arg_4_1, arg_4_2)
	if arg_4_0._AIOnRemove then
		arg_4_1:SetAI(arg_4_0._AIOnRemove)
	end
end
