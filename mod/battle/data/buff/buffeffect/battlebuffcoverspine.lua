ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffCoverSpine = class("BattleBuffCoverSpine", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffCoverSpine.__name = "BattleBuffCoverSpine"

local var_0_1 = var_0_0.Battle.BattleBuffCoverSpine

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._skin = arg_2_0._tempData.arg_list.ship_skin_id
	arg_2_0._hpbarOffset = arg_2_0._tempData.arg_list.hp_bar_offset or 0
end

function var_0_1.onAttach(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	arg_3_1:SwitchSpine(arg_3_0._skin, arg_3_0._hpbarOffset)
end

function var_0_1.onRemove(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	arg_4_1:SwitchSpine(nil, arg_4_0._hpbarOffset * -1)
end
