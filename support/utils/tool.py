pg = pg or {}

local var_0_0 = pg

var_0_0.Tool = class("Tool")

def var_0_0.Tool.Seq(arg_1_0):
	local var_1_0 = {}

	for iter_1_0 = 1, arg_1_0:
		var_1_0[iter_1_0] = iter_1_0

	return var_1_0

def var_0_0.Tool.Swap(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0[arg_2_2], arg_2_0[arg_2_1] = arg_2_0[arg_2_1], arg_2_0[arg_2_2]

def var_0_0.Tool.RandomMN(arg_3_0, arg_3_1):
	local var_3_0 = {}
	local var_3_1 = var_0_0.Tool.Seq(arg_3_0)
	local var_3_2 = #var_3_1

	for iter_3_0 = 1, arg_3_1:
		local var_3_3 = math.random(var_3_2)

		var_3_0[iter_3_0] = var_3_1[var_3_3]

		var_0_0.Tool.Swap(var_3_1, var_3_3, var_3_2)

		var_3_2 = var_3_2 - 1

	return var_3_0

def var_0_0.Tool.FilterY(arg_4_0):
	return Vector3(arg_4_0.x, 0, arg_4_0.z)

def var_0_0.Tool.FilterZ(arg_5_0):
	return Vector3(arg_5_0.x, arg_5_0.y, 0)

def var_0_0.Tool.GetShortName(arg_6_0, arg_6_1, arg_6_2):
	if arg_6_0 == None or arg_6_1 == None:
		return

	local var_6_0 = arg_6_0
	local var_6_1 = {}
	local var_6_2 = {}
	local var_6_3 = #var_6_0
	local var_6_4 = 0

	if arg_6_2 == None:
		arg_6_2 = arg_6_1 - 3

	for iter_6_0 = 1, var_6_3:
		local var_6_5 = string.byte(var_6_0, iter_6_0)
		local var_6_6 = 0

		if var_6_5 > 0 and var_6_5 <= 127:
			var_6_6 = 1
		elif var_6_5 >= 192 and var_6_5 < 223:
			var_6_6 = 2
		elif var_6_5 >= 224 and var_6_5 < 239:
			var_6_6 = 3
		elif var_6_5 >= 240 and var_6_5 <= 247:
			var_6_6 = 4

		local var_6_7

		if var_6_6 > 0:
			var_6_7 = string.sub(var_6_0, iter_6_0, iter_6_0 + var_6_6 - 1)
			iter_6_0 = iter_6_0 + var_6_6 - 1

		if var_6_6 == 1:
			var_6_4 = var_6_4 + 1

			table.insert(var_6_2, var_6_7)
			table.insert(var_6_1, 1)
		elif var_6_6 > 1:
			var_6_4 = var_6_4 + 2

			table.insert(var_6_2, var_6_7)
			table.insert(var_6_1, 2)

	if arg_6_1 < var_6_4:
		local var_6_8 = ""
		local var_6_9 = 0

		for iter_6_1 = 1, #var_6_2:
			var_6_8 = var_6_8 .. var_6_2[iter_6_1]
			var_6_9 = var_6_9 + var_6_1[iter_6_1]

			if arg_6_2 <= var_6_9:
				break

		arg_6_0 = var_6_8 .. "..."

	return arg_6_0

def var_0_0.Tool.Distances(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	local var_7_0 = arg_7_0 / 180 * math.pi
	local var_7_1 = arg_7_2 / 180 * math.pi
	local var_7_2 = arg_7_1 / 180 * math.pi
	local var_7_3 = arg_7_3 / 180 * math.pi
	local var_7_4 = var_7_0 - var_7_1
	local var_7_5 = var_7_2 - var_7_3

	return 2 * math.asin(math.sqrt(math.pow(math.sin(var_7_4 / 2), 2) + math.cos(var_7_0) * math.cos(var_7_1) * math.pow(math.sin(var_7_5 / 2), 2))) * 6378.137
