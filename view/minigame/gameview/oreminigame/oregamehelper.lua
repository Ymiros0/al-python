local var_0_0 = class("OreGameHelper")

local function var_0_1(arg_1_0)
	local var_1_0 = arg_1_0.x * 90 + 90
	local var_1_1 = arg_1_0.y * 90 + 90
	local var_1_2 = var_1_0

	if var_1_1 < 90 then
		if var_1_0 <= 90 then
			var_1_2 = 270 + var_1_1
		elseif var_1_0 > 90 then
			var_1_2 = 180 + (90 - var_1_1)
		end
	end

	return var_1_2
end

local var_0_2 = {
	"W",
	"NW",
	"N",
	"NE",
	"E",
	"SE",
	"S",
	"SW",
	"STAND"
}
local var_0_3 = {
	W = Vector2(-1, 0),
	NW = Vector2(-1, 1).normalized,
	N = Vector2(0, 1),
	NE = Vector2(1, 1).normalized,
	E = Vector2(1, 0),
	SE = Vector2(1, -1).normalized,
	S = Vector2(0, -1),
	SW = Vector2(-1, -1).normalized,
	STAND = Vector2(0, 0)
}

local function var_0_4(arg_2_0)
	if arg_2_0.x == 0 and arg_2_0.y == 0 then
		return "STAND"
	end

	local var_2_0 = var_0_1(arg_2_0)

	for iter_2_0 = 1, 8 do
		if iter_2_0 == 1 then
			if var_2_0 >= 0 and var_2_0 <= 22.5 or var_2_0 >= 337.5 and var_2_0 <= 360 then
				return var_0_2[iter_2_0]
			end
		else
			local var_2_1 = 22.5 + (iter_2_0 - 2) * 45

			if var_2_1 < var_2_0 and var_2_0 <= var_2_1 + 45 then
				return var_0_2[iter_2_0]
			end
		end
	end

	return "STAND"
end

function var_0_0.GetEightDirVector(arg_3_0)
	local var_3_0 = var_0_4(arg_3_0)

	return var_0_3[var_3_0]
end

local var_0_5 = {
	"W",
	"N",
	"E",
	"S"
}

function var_0_0.GetFourDirLabel(arg_4_0)
	if arg_4_0.x == 0 and arg_4_0.y == 0 then
		return "STAND"
	end

	local var_4_0 = var_0_1(arg_4_0)

	for iter_4_0 = 1, 4 do
		if iter_4_0 == 1 then
			if var_4_0 >= 0 and var_4_0 <= 45 or var_4_0 >= 315 and var_4_0 <= 360 then
				return var_0_5[iter_4_0]
			end
		else
			local var_4_1 = 45 + (iter_4_0 - 2) * 90

			if var_4_1 < var_4_0 and var_4_0 <= var_4_1 + 90 then
				return var_0_5[iter_4_0]
			end
		end
	end

	return "STAND"
end

function var_0_0.CheckRemovable(arg_5_0)
	if arg_5_0.x >= OreGameConfig.RANGE_X[1] and arg_5_0.x <= OreGameConfig.RANGE_X[2] and arg_5_0.y >= OreGameConfig.RANGE_Y[1] and arg_5_0.y <= OreGameConfig.RANGE_Y[2] then
		if arg_5_0.y >= OreGameConfig.BAN_Y[1] then
			return true
		elseif arg_5_0.x >= OreGameConfig.BAN_Y[2][1] and arg_5_0.x <= OreGameConfig.BAN_Y[2][2] then
			return true
		end
	end

	return false
end

function var_0_0.GetBeziersPoints(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
	local var_6_0 = arg_6_0:Clone():Mul((1 - arg_6_3) * (1 - arg_6_3))
	local var_6_1 = arg_6_2:Clone():Mul(2 * arg_6_3 * (1 - arg_6_3))
	local var_6_2 = arg_6_1:Clone():Mul(arg_6_3 * arg_6_3)

	return var_6_0:Add(var_6_1):Add(var_6_2)
end

function var_0_0.GetOreIDWithWeight(arg_7_0)
	local var_7_0 = 0

	for iter_7_0, iter_7_1 in ipairs(arg_7_0) do
		var_7_0 = var_7_0 + iter_7_1[2]
	end

	local var_7_1 = math.random() * var_7_0
	local var_7_2 = 0

	for iter_7_2, iter_7_3 in ipairs(arg_7_0) do
		var_7_2 = var_7_2 + iter_7_3[2]

		if var_7_1 <= var_7_2 then
			return iter_7_3[1]
		end
	end
end

function var_0_0.GetAABBWithTF(arg_8_0, arg_8_1)
	local var_8_0 = arg_8_0.rect.width
	local var_8_1 = arg_8_0.rect.height
	local var_8_2 = arg_8_0.anchoredPosition
	local var_8_3 = {
		var_8_2.x - var_8_0 / 2,
		var_8_2.y + var_8_1 / 2
	}
	local var_8_4 = {
		var_8_2.x + var_8_0 / 2,
		var_8_2.y - var_8_1 / 2
	}

	if arg_8_1 then
		var_8_3 = {
			var_8_2.x + var_8_0 / 2,
			var_8_2.y + var_8_1 / 2
		}
		var_8_4 = {
			var_8_2.x - var_8_0 / 2,
			var_8_2.y - var_8_1 / 2
		}
	end

	return {
		var_8_3,
		var_8_4
	}
end

return var_0_0
