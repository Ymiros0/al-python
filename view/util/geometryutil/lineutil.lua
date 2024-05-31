local var_0_0 = {}
local var_0_1 = import(".SegmentUtil")
local var_0_2 = 1e-06

local function var_0_3(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1 - arg_1_0
	local var_1_1 = arg_1_0.x * var_1_0.y - arg_1_0.y * var_1_0.x

	return {
		a = -var_1_0.y,
		b = var_1_0.x,
		c = var_1_1
	}
end

var_0_0.GetVerticalCrossPoint, var_0_0.TwoPointToCommon = function(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = var_0_3(arg_2_0, arg_2_1)
	local var_2_1 = var_2_0.b * arg_2_2.x - var_2_0.a * arg_2_2.y
	local var_2_2 = (var_2_0.b * var_2_1 - var_2_0.a * var_2_0.c) / (var_2_0.a * var_2_0.a + var_2_0.b * var_2_0.b)
	local var_2_3

	if var_0_1.IsZero(var_2_0.b) then
		var_2_3 = (var_2_0.x * var_2_2 + var_2_0.c) / -var_2_0.b
	else
		var_2_3 = arg_2_0.y
	end

	return Vector2(var_2_2, var_2_3)
end, var_0_3

return var_0_0
