local var_0_0 = type
local var_0_1 = {}
local var_0_2 = tolua.typeof
local var_0_3 = tolua.findtype

def typeof(arg_1_0):
	local var_1_0 = var_0_0(arg_1_0)
	local var_1_1

	if var_1_0 == "table":
		var_1_1 = var_0_1[arg_1_0]

		if var_1_1 == None:
			var_1_1 = var_0_2(arg_1_0)
			var_0_1[arg_1_0] = var_1_1
	elif var_1_0 == "string":
		var_1_1 = var_0_1[arg_1_0]

		if var_1_1 == None:
			var_1_1 = var_0_3(arg_1_0)
			var_0_1[arg_1_0] = var_1_1
	else
		error(debug.traceback("attemp to call typeof on type " .. var_1_0))

	return var_1_1
