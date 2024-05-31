﻿ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffLink = class("BattleBuffLink", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffLink.__name = "BattleBuffLink"

function var_0_0.Battle.BattleBuffLink.Ctor(arg_1_0, arg_1_1)
	var_0_0.Battle.BattleBuffLink.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_0.Battle.BattleBuffLink.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._target = arg_2_0._tempData.arg_list.target
	arg_2_0._buff_id = arg_2_0._tempData.arg_list.buff_id
end

function var_0_0.Battle.BattleBuffLink.Trigger(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4)
	local var_3_0 = arg_3_0:getTargetList(arg_3_2, arg_3_0._target, arg_3_0._tempData.arg_list)

	if var_3_0 then
		for iter_3_0, iter_3_1 in ipairs(var_3_0) do
			local var_3_1 = iter_3_1:GetBuff(arg_3_0._buff_id)

			if var_3_1 then
				var_3_1:onTrigger(arg_3_1, iter_3_1, arg_3_4)
			end
		end
	end
end
