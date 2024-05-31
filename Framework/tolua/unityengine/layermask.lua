﻿local var_0_0 = Layer
local var_0_1 = rawget
local var_0_2 = setmetatable
local var_0_3 = {}

function var_0_3.__index(arg_1_0, arg_1_1)
	return var_0_1(var_0_3, arg_1_1)
end

function var_0_3.__call(arg_2_0, arg_2_1)
	return var_0_2({
		value = arg_2_1 or 0
	}, var_0_3)
end

function var_0_3.New(arg_3_0)
	return var_0_2({
		value = arg_3_0 or 0
	}, var_0_3)
end

function var_0_3.Get(arg_4_0)
	return arg_4_0.value
end

function var_0_3.NameToLayer(arg_5_0)
	return var_0_0[arg_5_0]
end

function var_0_3.GetMask(...)
	local var_6_0 = {
		...
	}
	local var_6_1 = 0

	for iter_6_0 = 1, #var_6_0 do
		local var_6_2 = var_0_3.NameToLayer(var_6_0[iter_6_0])

		if var_6_2 ~= nil then
			var_6_1 = var_6_1 + 2^var_6_2
		end
	end

	return var_6_1
end

UnityEngine.LayerMask = var_0_3

var_0_2(var_0_3, var_0_3)

return var_0_3
