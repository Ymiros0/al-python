local var_0_0 = debug.getinfo
local var_0_1 = error
local var_0_2 = rawset
local var_0_3 = rawget
local var_0_4 = getmetatable(_G)

if var_0_4 == None:
	var_0_4 = {}

	setmetatable(_G, var_0_4)

var_0_4.__declared = {}

def var_0_4.__newindex(arg_1_0, arg_1_1, arg_1_2):
	if not var_0_4.__declared[arg_1_1]:
		local var_1_0 = var_0_0(2, "S")

		if var_1_0 and var_1_0.linedefined > 0:
			var_0_1("assign to undeclared variable '" .. arg_1_1 .. "'", 2)

		var_0_4.__declared[arg_1_1] = True

	var_0_2(arg_1_0, arg_1_1, arg_1_2)

def var_0_4.__index(arg_2_0, arg_2_1):
	if not var_0_4.__declared[arg_2_1]:
		local var_2_0 = var_0_0(2, "S")

		if var_2_0 and var_2_0.linedefined > 0:
			var_0_1("variable '" .. arg_2_1 .. "' is not declared", 2)

	return var_0_3(arg_2_0, arg_2_1)
