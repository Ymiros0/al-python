local var_0_0 = class("Heap")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.array = arg_1_1
	arg_1_0.func = arg_1_2
	arg_1_0.values = underscore.map(arg_1_1, function(arg_2_0)
		return arg_1_2(arg_1_1))

	for iter_1_0 = math.floor(#arg_1_0.array / 2), 1, -1:
		arg_1_0.Dive(iter_1_0)

def var_0_0.Float(arg_3_0, arg_3_1):
	local var_3_0 = math.floor(arg_3_1 / 2)

	while var_3_0 > 0 and arg_3_0.values[arg_3_1] < arg_3_0.values[var_3_0]:
		arg_3_0.array[var_3_0], arg_3_0.array[arg_3_1] = arg_3_0.array[arg_3_1], arg_3_0.array[var_3_0]
		arg_3_0.values[var_3_0], arg_3_0.values[arg_3_1] = arg_3_0.values[arg_3_1], arg_3_0.values[var_3_0]
		arg_3_1, var_3_0 = var_3_0, math.floor(var_3_0 / 2)

def var_0_0.Dive(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1 + arg_4_1
	local var_4_1 = var_4_0 + (var_4_0 < #arg_4_0.array and arg_4_0.values[var_4_0 + 1] < arg_4_0.values[var_4_0] and 1 or 0)

	while var_4_1 <= #arg_4_0.array and arg_4_0.values[var_4_1] < arg_4_0.values[arg_4_1]:
		arg_4_0.array[var_4_1], arg_4_0.array[arg_4_1] = arg_4_0.array[arg_4_1], arg_4_0.array[var_4_1]
		arg_4_0.values[var_4_1], arg_4_0.values[arg_4_1] = arg_4_0.values[arg_4_1], arg_4_0.values[var_4_1]
		arg_4_1, var_4_1 = var_4_1, var_4_1 + var_4_1
		var_4_1 = var_4_1 + (var_4_1 < #arg_4_0.array and arg_4_0.values[var_4_1 + 1] < arg_4_0.values[var_4_1] and 1 or 0)

def var_0_0.POP(arg_5_0):
	assert(#arg_5_0.array == #arg_5_0.values)

	arg_5_0.array[1], arg_5_0.array[#arg_5_0.array] = arg_5_0.array[#arg_5_0.array], arg_5_0.array[1]
	arg_5_0.values[1], arg_5_0.values[#arg_5_0.values] = arg_5_0.values[#arg_5_0.values], arg_5_0.values[1]

	local var_5_0 = table.remove(arg_5_0.array)

	table.remove(arg_5_0.values)
	arg_5_0.Dive(1)

	return var_5_0

def var_0_0.PUSH(arg_6_0, arg_6_1):
	table.insert(arg_6_0.array, arg_6_1)
	table.insert(arg_6_0.values, arg_6_0.func(arg_6_1))
	arg_6_0.Float(#arg_6_0.array)

return var_0_0
