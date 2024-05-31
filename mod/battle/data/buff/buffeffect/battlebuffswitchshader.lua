ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffSwitchShader = class("BattleBuffSwitchShader", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffSwitchShader.__name = "BattleBuffSwitchShader"

local var_0_1 = var_0_0.Battle.BattleBuffSwitchShader

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._shader = arg_2_0._tempData.arg_list.shader
	arg_2_0._invisible = arg_2_0._tempData.arg_list.invisible or 0.7
end

function var_0_1.onAttach(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	local var_3_0 = {
		invisible = arg_3_0._invisible
	}

	arg_3_1:SwitchShader(arg_3_0._shader, nil, var_3_0)
end

function var_0_1.onRemove(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	arg_4_1:SwitchShader("COLORED_ALPHA")
end
