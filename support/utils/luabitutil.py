local var_0_0 = {
	[0] = "0",
	"1",
	"2",
	"3",
	"4",
	"5",
	"6",
	"7",
	"8",
	"9",
	"A",
	"B",
	"C",
	"D",
	"E",
	"F",
	"G"
}

local function var_0_1(arg_1_0)
	for iter_1_0, iter_1_1 in pairs(var_0_0):
		if iter_1_1 == arg_1_0:
			return iter_1_0

	return 0

local function var_0_2(arg_2_0, arg_2_1)
	local function var_2_0(arg_3_0, arg_3_1)
		if arg_3_0 < arg_2_1:
			table.insert(arg_3_1, arg_3_0)
		else
			var_2_0(math.floor(arg_3_0 / arg_2_1), arg_3_1)
			table.insert(arg_3_1, arg_3_0 % arg_2_1)

	local var_2_1 = {}

	var_2_0(arg_2_0, var_2_1)

	return var_2_1

def ConvertDec2X(arg_4_0, arg_4_1):
	local var_4_0 = var_0_2(arg_4_0, arg_4_1)
	local var_4_1 = ""

	for iter_4_0, iter_4_1 in ipairs(var_4_0):
		var_4_1 = var_4_1 .. var_0_0[iter_4_1]

	return var_4_1

def ConvertStr2Dec(arg_5_0, arg_5_1):
	local var_5_0 = {}
	local var_5_1 = string.len(arg_5_0)

	while var_5_1 > 0:
		local var_5_2 = string.sub(arg_5_0, var_5_1, var_5_1)

		var_5_0[#var_5_0 + 1] = var_0_1(var_5_2)
		var_5_1 = var_5_1 - 1

	local var_5_3 = 0

	for iter_5_0, iter_5_1 in ipairs(var_5_0):
		var_5_3 = var_5_3 + iter_5_1 * math.pow(arg_5_1, iter_5_0 - 1)

	return var_5_3
