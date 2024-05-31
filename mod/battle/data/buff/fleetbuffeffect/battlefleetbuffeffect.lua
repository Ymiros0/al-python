ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleFleetBuffEffect = class("BattleFleetBuffEffect")
var_0_0.Battle.BattleFleetBuffEffect.__name = "BattleFleetBuffEffect"

local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleFleetBuffEffect

function var_0_2.Ctor(arg_1_0, arg_1_1)
	arg_1_0._tempData = Clone(arg_1_1)
	arg_1_0._type = arg_1_0._tempData.type

	arg_1_0:SetActive()
end

function var_0_2.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._fleetVO = arg_2_1
	arg_2_0._fleetBuff = arg_2_2
end

function var_0_2.Trigger(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4)
	arg_3_0[arg_3_1](arg_3_0, arg_3_2, arg_3_3, arg_3_4)
end

function var_0_2.onAttach(arg_4_0, arg_4_1, arg_4_2)
	arg_4_0:onTrigger(arg_4_1, arg_4_2)
end

function var_0_2.onRemove(arg_5_0, arg_5_1, arg_5_2)
	arg_5_0:onTrigger(arg_5_1, arg_5_2)
end

function var_0_2.onUpdate(arg_6_0, arg_6_1, arg_6_2)
	arg_6_0:onTrigger(arg_6_1, arg_6_2)
end

function var_0_2.onStack(arg_7_0, arg_7_1, arg_7_2)
	arg_7_0:onTrigger(arg_7_1, arg_7_2)
end

function var_0_2.getTargetList(arg_8_0, arg_8_1, arg_8_2, arg_8_3)
	local var_8_0
	local var_8_1 = arg_8_1:GetUnitList()[1]

	for iter_8_0, iter_8_1 in ipairs(arg_8_2) do
		var_8_0 = var_0_0.Battle.BattleTargetChoise[iter_8_1](var_8_1, arg_8_3, var_8_0)
	end

	return var_8_0
end

function var_0_2.IsActive(arg_9_0)
	return arg_9_0._isActive
end

function var_0_2.SetActive(arg_10_0)
	arg_10_0._isActive = true
end

function var_0_2.NotActive(arg_11_0)
	arg_11_0._isActive = false
end

function var_0_2.Clear(arg_12_0)
	return
end

function var_0_2.Dispose(arg_13_0)
	return
end
