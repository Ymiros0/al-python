ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffDeactiveCLDBox = class("BattleBuffDeactiveCLDBox", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffDeactiveCLDBox.__name = "BattleBuffDeactiveCLDBox"

local var_0_1 = var_0_0.Battle.BattleBuffDeactiveCLDBox

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.GetEffectType(arg_2_0)
	return var_0_1.FX_TYPE
end

function var_0_1.onAttach(arg_3_0, arg_3_1, arg_3_2)
	arg_3_1:SetCldBoxImmune(true)
end

function var_0_1.onRemove(arg_4_0, arg_4_1, arg_4_2)
	arg_4_1:SetCldBoxImmune(false)
end
