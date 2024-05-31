ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffLockHealth = class("BattleBuffLockHealth", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffLockHealth.__name = "BattleBuffLockHealth"

local var_0_1 = var_0_0.Battle.BattleBuffLockHealth

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._rate = arg_2_0._tempData.arg_list.rate
	arg_2_0._threshold = arg_2_0._tempData.arg_list.value
end

function var_0_1.onAttach(arg_3_0, arg_3_1, arg_3_2)
	if arg_3_0._rate then
		arg_3_0._threshold = math.floor(arg_3_1:GetMaxHP() * arg_3_0._rate)
	end
end

function var_0_1.onTrigger(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	local var_4_0 = arg_4_1:GetCurrentHP()

	if var_4_0 <= arg_4_0._threshold then
		arg_4_3.damage = 0
	elseif var_4_0 - arg_4_3.damage < arg_4_0._threshold then
		arg_4_3.damage = var_4_0 - arg_4_0._threshold
	end
end
