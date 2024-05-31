local var_0_0 = {
	p = pg.gameset.air_dominance_p.key_value,
	q = pg.gameset.air_dominance_q.key_value,
	s = pg.gameset.air_dominance_s.key_value,
	t = pg.gameset.air_dominance_t.key_value,
	r = pg.gameset.air_dominance_r.key_value,
	a = pg.gameset.air_dominance_a.key_value,
	x = pg.gameset.air_dominance_x.key_value,
	y = pg.gameset.air_dominance_y.key_value
}

def calcAirDominanceValue(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_0.getAircraftCount()
	local var_1_1 = arg_1_0.getEquipmentProperties()

	return defaultValue(arg_1_0.getProperties(arg_1_1)[AttributeType.Air], 0) * (defaultValue(var_1_0[EquipType.FighterAircraft], 0) * var_0_0.p + defaultValue(var_1_0[EquipType.TorpedoAircraft], 0) * var_0_0.q + defaultValue(var_1_0[EquipType.BomberAircraft], 0) * var_0_0.s + defaultValue(var_1_0[EquipType.SeaPlane], 0) * var_0_0.t) * (0.8 + arg_1_0.level * var_0_0.r / 100) / 100 + defaultValue(var_1_1[AttributeType.AirDominate], 0)

def calcAirDominanceStatus(arg_2_0, arg_2_1, arg_2_2):
	arg_2_1 = arg_2_1 * (var_0_0.a / (arg_2_2 + var_0_0.a))

	if arg_2_0 == 0:
		if arg_2_1 <= var_0_0.x:
			return 0
		elif arg_2_1 <= var_0_0.y:
			return 2
		else
			return 1
	elif arg_2_0 <= var_0_0.x:
		if arg_2_1 == 0:
			return 0
		elif arg_2_1 <= var_0_0.x:
			return 0
		elif arg_2_1 <= var_0_0.y:
			if arg_2_0 <= arg_2_1 * 0.75:
				return 2
			elif arg_2_0 <= arg_2_1 * 1.3:
				return 3
			else
				return 4
		elif arg_2_0 <= arg_2_1 * 0.5:
			return 1
		elif arg_2_0 <= arg_2_1 * 0.75:
			return 2
		elif arg_2_0 <= arg_2_1 * 1.3:
			return 3
		else
			return 4
	elif arg_2_0 <= var_0_0.y:
		if arg_2_1 == 0:
			return 4
		elif arg_2_1 <= var_0_0.y:
			if arg_2_0 <= arg_2_1 * 0.75:
				return 2
			elif arg_2_0 <= arg_2_1 * 1.3:
				return 3
			else
				return 4
		elif arg_2_0 <= arg_2_1 * 0.5:
			return 1
		elif arg_2_0 <= arg_2_1 * 0.75:
			return 2
		elif arg_2_0 <= arg_2_1 * 1.3:
			return 3
		else
			return 4
	elif arg_2_1 == 0:
		return 5
	elif arg_2_0 <= arg_2_1 * 0.5:
		return 1
	elif arg_2_0 <= arg_2_1 * 0.75:
		return 2
	elif arg_2_0 <= arg_2_1 * 1.3:
		return 3
	elif arg_2_0 <= arg_2_1 * 2:
		return 4
	else
		return 5

def calcPositionAngle(arg_3_0, arg_3_1):
	local var_3_0 = Vector3(arg_3_0, arg_3_1, 0)
	local var_3_1 = Vector3.up
	local var_3_2 = Vector2.Angle(var_3_0, var_3_1)

	return Vector3.Cross(var_3_0, var_3_1).z > 0 and var_3_2 or -var_3_2

def DOAParabolaCalc(arg_4_0, arg_4_1, arg_4_2):
	assert(arg_4_2 < arg_4_1 * arg_4_1 * arg_4_0 / 2, "x is unreal")

	local var_4_0 = arg_4_0 * math.sqrt(arg_4_1 / 2)
	local var_4_1 = 0
	local var_4_2 = var_4_0 * var_4_0
	local var_4_3

	while var_4_2 - var_4_1 > 0.01:
		local var_4_4 = (var_4_1 + var_4_2) / 2

		if var_4_0 > math.sqrt(var_4_4) + math.sqrt(var_4_4 + arg_4_2):
			var_4_1 = var_4_4
		else
			var_4_2 = var_4_4

	return var_4_1

def mergeSort(arg_5_0, arg_5_1):
	arg_5_1 = arg_5_1 or function(arg_6_0, arg_6_1)
		return arg_6_0 <= arg_6_1

	local var_5_0 = {}

	local function var_5_1(arg_7_0, arg_7_1)
		if arg_7_1 <= arg_7_0:
			return

		local var_7_0 = math.floor((arg_7_0 + arg_7_1) / 2)

		var_5_1(arg_7_0, var_7_0)
		var_5_1(var_7_0 + 1, arg_7_1)

		local var_7_1 = arg_7_0
		local var_7_2 = var_7_0 + 1

		while var_7_1 <= var_7_0 and var_7_2 <= arg_7_1:
			if arg_5_1(arg_5_0[var_7_1], arg_5_0[var_7_2]):
				var_5_0[var_7_1 + var_7_2 - var_7_0 - 1] = arg_5_0[var_7_1]
				var_7_1 = var_7_1 + 1
			else
				var_5_0[var_7_1 + var_7_2 - var_7_0 - 1] = arg_5_0[var_7_2]
				var_7_2 = var_7_2 + 1

		while var_7_1 <= var_7_0:
			var_5_0[var_7_1 + var_7_2 - var_7_0 - 1] = arg_5_0[var_7_1]
			var_7_1 = var_7_1 + 1

		while var_7_2 <= arg_7_1:
			var_5_0[var_7_1 + var_7_2 - var_7_0 - 1] = arg_5_0[var_7_2]
			var_7_2 = var_7_2 + 1

		for iter_7_0 = arg_7_0, arg_7_1:
			arg_5_0[iter_7_0] = var_5_0[iter_7_0]

	var_5_1(1, #arg_5_0)

def LineLine(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	local var_8_0 = False
	local var_8_1
	local var_8_2
	local var_8_3 = (arg_8_3.y - arg_8_2.y) * (arg_8_1.x - arg_8_0.x) - (arg_8_3.x - arg_8_2.x) * (arg_8_1.y - arg_8_0.y)

	if var_8_3 != 0:
		var_8_1 = ((arg_8_3.x - arg_8_2.x) * (arg_8_0.y - arg_8_2.y) - (arg_8_3.y - arg_8_2.y) * (arg_8_0.x - arg_8_2.x)) / var_8_3
		var_8_2 = ((arg_8_1.x - arg_8_0.x) * (arg_8_0.y - arg_8_2.y) - (arg_8_1.y - arg_8_0.y) * (arg_8_0.x - arg_8_2.x)) / var_8_3

		if var_8_1 >= 0 and var_8_1 <= 1 and var_8_2 >= 0 and var_8_2 <= 1:
			var_8_0 = True

	return var_8_0, var_8_1, var_8_2

def ConversionBase(arg_9_0, arg_9_1):
	local var_9_0 = {
		0
	}
	local var_9_1 = 0

	while arg_9_1 > 0:
		var_9_1 = var_9_1 + 1
		var_9_0[var_9_1] = arg_9_1 % arg_9_0

		if var_9_0[var_9_1] < 10:
			var_9_0[var_9_1] = string.format("%c", var_9_0[var_9_1] + 48)
		else
			var_9_0[var_9_1] = string.format("%c", var_9_0[var_9_1] + 55)

		arg_9_1 = math.floor(arg_9_1 / arg_9_0)

	for iter_9_0 = 1, math.floor(#var_9_0 / 2):
		var_9_0[iter_9_0], var_9_0[#var_9_0 - iter_9_0 + 1] = var_9_0[#var_9_0 - iter_9_0 + 1], var_9_0[iter_9_0]

	return table.concat(var_9_0)

base64 = {}

local var_0_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64.enc(arg_10_0):
	return (arg_10_0.gsub(".", function(arg_11_0)
		local var_11_0 = ""
		local var_11_1 = arg_11_0.byte()

		for iter_11_0 = 8, 1, -1:
			var_11_0 = var_11_0 .. (var_11_1 % 2^iter_11_0 - var_11_1 % 2^(iter_11_0 - 1) > 0 and "1" or "0")

		return var_11_0) .. "0000").gsub("%d%d%d?%d?%d?%d?", function(arg_12_0)
		if #arg_12_0 < 6:
			return ""

		local var_12_0 = 0

		for iter_12_0 = 1, 6:
			var_12_0 = var_12_0 + (arg_12_0.sub(iter_12_0, iter_12_0) == "1" and 2^(6 - iter_12_0) or 0)

		return var_0_1.sub(var_12_0 + 1, var_12_0 + 1)) .. ({
		"",
		"==",
		"="
	})[#arg_10_0 % 3 + 1]

def base64.dec(arg_13_0):
	arg_13_0 = string.gsub(arg_13_0, "[^" .. var_0_1 .. "=]", "")

	return (arg_13_0.gsub(".", function(arg_14_0)
		if arg_14_0 == "=":
			return ""

		local var_14_0 = ""
		local var_14_1 = var_0_1.find(arg_14_0) - 1

		for iter_14_0 = 6, 1, -1:
			var_14_0 = var_14_0 .. (var_14_1 % 2^iter_14_0 - var_14_1 % 2^(iter_14_0 - 1) > 0 and "1" or "0")

		return var_14_0).gsub("%d%d%d?%d?%d?%d?%d?%d?", function(arg_15_0)
		if #arg_15_0 != 8:
			return ""

		local var_15_0 = 0

		for iter_15_0 = 1, 8:
			var_15_0 = var_15_0 + (arg_15_0.sub(iter_15_0, iter_15_0) == "1" and 2^(8 - iter_15_0) or 0)

		return string.char(var_15_0)))
