ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffSize = class("BattleBuffSize", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffSize.__name = "BattleBuffSize"

function var_0_0.Battle.BattleBuffSize.Ctor(arg_1_0, arg_1_1)
	var_0_0.Battle.BattleBuffSize.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_0.Battle.BattleBuffSize.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._number = arg_2_0._tempData.arg_list.number or 1
end

function var_0_0.Battle.BattleBuffSize.onAttach(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = {
		size_ratio = arg_3_0._number
	}

	arg_3_1:DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleBuffEvent.BUFF_EFFECT_CHNAGE_SIZE, var_3_0))
end

function var_0_0.Battle.BattleBuffSize.onRemove(arg_4_0, arg_4_1, arg_4_2)
	local var_4_0 = {
		size_ratio = 1 / arg_4_0._number
	}

	arg_4_1:DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleBuffEvent.BUFF_EFFECT_CHNAGE_SIZE, var_4_0))
end
