﻿ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleBuffEvent
local var_0_2 = var_0_0.Battle.BattleConst.BuffEffectType
local var_0_3 = class("BattleFleetBuffUnit")

var_0_0.Battle.BattleFleetBuffUnit = var_0_3
var_0_3.__name = "BattleFleetBuffUnit"

function var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_2 = arg_1_2 or 1
	arg_1_0._id = arg_1_1
	arg_1_0._tempData = var_0_0.Battle.BattleDataFunction.GetBuffTemplate(arg_1_1, arg_1_2)
	arg_1_0._time = arg_1_0._tempData.time
	arg_1_0._RemoveTime = 0
	arg_1_0._effectList = {}
	arg_1_0._triggerSearchTable = {}
	arg_1_0._level = arg_1_2

	for iter_1_0, iter_1_1 in ipairs(arg_1_0._tempData.effect_list) do
		local var_1_0 = var_0_0.Battle[iter_1_1.type].New(iter_1_1)

		arg_1_0._effectList[iter_1_0] = var_1_0

		local var_1_1 = iter_1_1.trigger

		for iter_1_2, iter_1_3 in ipairs(var_1_1) do
			local var_1_2 = arg_1_0._triggerSearchTable[iter_1_3]

			if var_1_2 == nil then
				var_1_2 = {}
				arg_1_0._triggerSearchTable[iter_1_3] = var_1_2
			end

			var_1_2[#var_1_2 + 1] = var_1_0
		end
	end

	arg_1_0:SetActive()
end

function var_0_3.SetArgs(arg_2_0, arg_2_1)
	arg_2_0._host = arg_2_1

	for iter_2_0, iter_2_1 in ipairs(arg_2_0._effectList) do
		iter_2_1:SetArgs(arg_2_1, arg_2_0)
	end
end

function var_0_3.setRemoveTime(arg_3_0)
	arg_3_0._RemoveTime = pg.TimeMgr.GetInstance():GetCombatTime() + arg_3_0._time
	arg_3_0._cancelTime = nil
end

function var_0_3.Attach(arg_4_0, arg_4_1)
	arg_4_0._stack = 1

	arg_4_0:SetArgs(arg_4_1)
	arg_4_0:onTrigger(var_0_2.ON_ATTACH, arg_4_1)
	arg_4_0:setRemoveTime()
end

function var_0_3.Stack(arg_5_0, arg_5_1)
	arg_5_0._stack = math.min(arg_5_0._stack + 1, arg_5_0._tempData.stack)

	arg_5_0:onTrigger(var_0_2.ON_STACK, arg_5_1)
	arg_5_0:setRemoveTime()
end

function var_0_3.UpdateStack(arg_6_0, arg_6_1, arg_6_2)
	return
end

function var_0_3.Remove(arg_7_0)
	arg_7_0:onTrigger(var_0_2.ON_REMOVE, arg_7_0._host)

	arg_7_0._host:GetFleetBuffList()[arg_7_0._id] = nil

	arg_7_0:Clear()
end

function var_0_3.Update(arg_8_0, arg_8_1, arg_8_2)
	if arg_8_0:IsTimeToRemove(arg_8_2) then
		arg_8_0:Remove()
	else
		arg_8_0:onTrigger(var_0_2.ON_UPDATE, arg_8_1, arg_8_2)
	end
end

function var_0_3.onTrigger(arg_9_0, arg_9_1, arg_9_2, arg_9_3)
	local var_9_0 = arg_9_0._triggerSearchTable[arg_9_1]

	if var_9_0 == nil or #var_9_0 == 0 then
		return
	end

	for iter_9_0, iter_9_1 in ipairs(var_9_0) do
		assert(type(iter_9_1[arg_9_1]) == "function", "fleet buff效果的触发函数缺失,buff id:>>" .. arg_9_0._id .. "<<, trigger:>>" .. arg_9_1 .. "<<")

		if iter_9_1:IsActive() then
			iter_9_1:NotActive()
			iter_9_1:Trigger(arg_9_1, arg_9_2, arg_9_0, arg_9_3)
			iter_9_1:SetActive()
		end
	end
end

function var_0_3.IsTimeToRemove(arg_10_0, arg_10_1)
	if arg_10_0._time == 0 then
		return false
	else
		return arg_10_1 >= arg_10_0._RemoveTime
	end
end

function var_0_3.IsActive(arg_11_0)
	return arg_11_0._isActive
end

function var_0_3.SetActive(arg_12_0)
	arg_12_0._isActive = true
end

function var_0_3.NotActive(arg_13_0)
	arg_13_0._isActive = false
end

function var_0_3.GetCaster(arg_14_0)
	return nil
end

function var_0_3.GetID(arg_15_0)
	return arg_15_0._id
end

function var_0_3.GetLv(arg_16_0)
	return 1
end

function var_0_3.Clear(arg_17_0)
	arg_17_0._host = nil

	for iter_17_0, iter_17_1 in ipairs(arg_17_0._effectList) do
		iter_17_1:Clear()
	end
end
