local var_0_0 = {}
local var_0_1 = import(".SegmentUtil")
local var_0_2 = UnityEngine.Vector2
local var_0_3 = 1e-06

local function var_0_4(arg_1_0, arg_1_1)
	return (arg_1_0 - 1) % arg_1_1 + 1
end

local function var_0_5(arg_2_0, arg_2_1)
	local var_2_0 = 0
	local var_2_1 = #arg_2_1

	for iter_2_0 = 0, var_2_1 do
		local var_2_2 = arg_2_1[var_0_4(iter_2_0)]
		local var_2_3 = arg_2_1[var_0_4(iter_2_0 + 1)]

		if (var_2_2.y <= arg_2_0.y and var_2_3.y - var_0_3 > arg_2_0.y or var_2_3.y <= arg_2_0.y and var_2_2.y - var_0_3 > arg_2_0.y) and (var_2_2.x >= arg_2_0.x or var_2_3.x >= arg_2_0.x) and arg_2_0.x + var_0_3 < var_2_2.x + (arg_2_0.y - var_2_2.y) / (var_2_3.y - var_2_2.y) * (var_2_3.x - var_2_2.x) then
			var_2_0 = var_2_0 + 1
		end
	end

	return var_2_0
end

local function var_0_6(arg_3_0, arg_3_1)
	local var_3_0 = var_0_5(arg_3_0, arg_3_1)

	return bit.band(var_3_0, 1) > 0
end

local function var_0_7(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	local var_4_0 = var_0_1.VectorCross(arg_4_0, arg_4_2, arg_4_3)
	local var_4_1 = var_0_1.VectorCross(arg_4_0, arg_4_2, arg_4_1)
	local var_4_2 = var_0_1.VectorCross(arg_4_0, arg_4_1, arg_4_3)

	if var_0_1.IsZero(var_4_0) then
		return var_4_1 <= var_0_1.eps or var_4_2 <= var_0_1.eps
	else
		return var_4_1 <= var_0_1.eps and var_4_2 <= var_0_1.eps
	end
end

local function var_0_8(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4, arg_5_5)
	local var_5_0 = arg_5_4

	while var_5_0 ~= arg_5_5 do
		local var_5_1 = var_0_4(var_5_0 + 1, #arg_5_3)

		if var_0_1.IsSegamentCross(arg_5_0, arg_5_1, arg_5_2[arg_5_3[var_5_0]], arg_5_2[arg_5_3[var_5_1]]) then
			return true
		end

		var_5_0 = var_5_1
	end

	return false
end

local function var_0_9(arg_6_0)
	if #arg_6_0 < 4 then
		return {
			0,
			1,
			2
		}
	end

	local var_6_0 = {}
	local var_6_1 = {}
	local var_6_2 = {}

	for iter_6_0 = 1, #arg_6_0 do
		local var_6_3 = var_0_1.CycleIndex(iter_6_0 + 2)

		table.insert(var_6_1, iter_6_0)
		table.insert(var_6_2, {
			iter_6_0,
			Vector2.Distance(arg_6_0[iter_6_0], arg_6_0[var_6_3])
		})
	end

	local function var_6_4(arg_7_0, arg_7_1)
		return arg_7_0[2] < arg_7_1[2]
	end

	table.sort(var_6_2, var_6_4)

	while #var_6_1 > 2 and #var_6_2 > 0 do
		local var_6_5 = var_6_2[1][1]
		local var_6_6 = table.indexof(var_6_1, var_6_5)
		local var_6_7 = var_0_4(var_6_6 + 1, #var_6_1)
		local var_6_8 = var_0_4(var_6_6 + 2, #var_6_1)
		local var_6_9 = var_6_1[var_6_7]
		local var_6_10 = var_6_1[var_6_8]

		if var_0_1.VectorCross(arg_6_0[var_6_5], arg_6_0[var_6_10], arg_6_0[var_6_9]) > 0 and not var_0_8(arg_6_0[var_6_5], arg_6_0[var_6_10], arg_6_0, var_6_1, var_6_8, var_6_6) then
			table.insert(var_6_0, var_6_5)
			table.insert(var_6_0, var_6_9)
			table.insert(var_6_0, var_6_10)

			local var_6_11 = var_6_1[var_0_4(var_6_6 - 1, #var_6_1)]
			local var_6_12 = var_6_1[var_0_4(var_6_8 + 1, #var_6_1)]

			for iter_6_1 = #var_6_2, 1, -1 do
				local var_6_13 = var_6_2[iter_6_1][1]

				if var_6_13 == var_6_9 or var_6_13 == var_6_11 then
					table.remove(var_6_2, iter_6_1)
				end
			end

			table.insert(var_6_2, {
				var_6_11,
				Vector2.Distance(arg_6_0[var_6_11], arg_6_0[var_6_10])
			})
			table.insert(var_6_2, {
				var_6_5,
				Vector2.Distance(arg_6_0[var_6_5], arg_6_0[var_6_12])
			})
			table.remove(var_6_1, var_6_9)
			table.sort(var_6_2, var_6_4)
		end

		table.remove(var_6_2, 1)
	end

	return var_6_0
end

local function var_0_10(arg_8_0)
	local var_8_0 = #arg_8_0

	if var_8_0 < 3 then
		return 0
	end

	local var_8_1 = 0
	local var_8_2 = 0

	for iter_8_0 = 1, var_8_0 do
		local var_8_3 = arg_8_0[iter_8_0]
		local var_8_4 = arg_8_0[var_0_4(iter_8_0 + 1, var_8_0)]

		var_8_1 = var_8_1 + var_8_3.x * var_8_4.y
		var_8_2 = var_8_2 + var_8_3.y * var_8_4.x
	end

	return (var_8_1 - var_8_2) / 2
end

local function var_0_11(arg_9_0)
	local var_9_0 = var_0_10(arg_9_0)

	return var_0_1.Sign(var_9_0)
end

var_0_0.CycleIndex = var_0_4
var_0_0.RayCross = var_0_5
var_0_0.Contains = var_0_6
var_0_0.IsPointInAngle = var_0_7
var_0_0.IsCrossAnyEdge = var_0_8
var_0_0.Triangulated = var_0_9
var_0_0.CalculateArea = var_0_10
var_0_0.IsPolygonClockwise = var_0_11

return var_0_0
