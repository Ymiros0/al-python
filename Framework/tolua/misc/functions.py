local var_0_0 = require
local var_0_1 = string
local var_0_2 = table

int64.zero = int64.new(0, 0)
uint64.zero = uint64.new(0, 0)

def var_0_1.split(arg_1_0, arg_1_1):
	arg_1_0 = tostring(arg_1_0)
	arg_1_1 = tostring(arg_1_1)

	if arg_1_1 == "":
		return False

	local var_1_0 = 0
	local var_1_1 = {}

	for iter_1_0, iter_1_1 in function()
		return var_0_1.find(arg_1_0, arg_1_1, var_1_0, True):
		var_0_2.insert(var_1_1, var_0_1.sub(arg_1_0, var_1_0, iter_1_0 - 1))

		var_1_0 = iter_1_1 + 1

	var_0_2.insert(var_1_1, var_0_1.sub(arg_1_0, var_1_0))

	return var_1_1

def import(arg_3_0, arg_3_1):
	local var_3_0
	local var_3_1 = arg_3_0
	local var_3_2 = 1

	while True:
		if var_0_1.byte(arg_3_0, var_3_2) != 46:
			var_3_1 = var_0_1.sub(arg_3_0, var_3_2)

			if var_3_0 and #var_3_0 > 0:
				var_3_1 = var_0_2.concat(var_3_0, ".") .. "." .. var_3_1

			break

		var_3_2 = var_3_2 + 1

		if not var_3_0:
			if not arg_3_1:
				local var_3_3, var_3_4 = debug.getlocal(3, 1)

				arg_3_1 = var_3_4

			var_3_0 = var_0_1.split(arg_3_1, ".")

		var_0_2.remove(var_3_0, #var_3_0)

	return var_0_0(var_3_1)

def reimport(arg_4_0):
	local var_4_0 = package

	var_4_0.loaded[arg_4_0] = None
	var_4_0.preload[arg_4_0] = None

	return var_0_0(arg_4_0)
