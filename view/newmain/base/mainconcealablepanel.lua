﻿local var_0_0 = class("MainConcealablePanel", import(".MainBasePanel"))

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)

	arg_1_0.initPosition = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_0.btns) do
		if not iter_1_1:IsFixed() then
			table.insert(arg_1_0.initPosition, iter_1_1._tf.localPosition)
		end
	end

	arg_1_0.isChanged = false
end

function var_0_0.Init(arg_2_0)
	var_0_0.super.Init(arg_2_0)
	arg_2_0:CalcLayout()
end

function var_0_0.Refresh(arg_3_0)
	var_0_0.super.Refresh(arg_3_0)
	arg_3_0:CalcLayout()
end

function var_0_0.CalcLayout(arg_4_0)
	local var_4_0 = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.btns) do
		if not iter_4_1:IsFixed() and isActive(iter_4_1._tf) then
			table.insert(var_4_0, iter_4_1._tf)
		end
	end

	local var_4_1 = #var_4_0 >= #arg_4_0.initPosition

	if var_4_1 and not arg_4_0.isChanged then
		return
	end

	arg_4_0:FillEmptySlot(var_4_0)

	arg_4_0.isChanged = not var_4_1
end

function var_0_0.FillEmptySlot(arg_5_0, arg_5_1)
	local var_5_0 = #arg_5_0.initPosition

	for iter_5_0 = #arg_5_1, 1, -1 do
		arg_5_1[iter_5_0].localPosition = arg_5_0.initPosition[var_5_0]
		var_5_0 = var_5_0 - 1
	end
end

return var_0_0
