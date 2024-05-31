ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffManualTorpedoCoolDown = class("BattleBuffManualTorpedoCoolDown", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffManualTorpedoCoolDown.__name = "BattleBuffManualTorpedoCoolDown"

local var_0_1 = var_0_0.Battle.BattleBuffManualTorpedoCoolDown

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._rant = arg_2_0._tempData.arg_list.rant or 10000
end

function var_0_1.onTrigger(arg_3_0, arg_3_1)
	var_0_1.super.onTrigger(arg_3_0, arg_3_1, buff, attach)

	if var_0_0.Battle.BattleFormulas.IsHappen(arg_3_0._rant) then
		local var_3_0 = arg_3_1:GetTorpedoQueue():GetQueueHead()

		if var_3_0 then
			var_3_0:QuickCoolDown()
		end
	end
end
