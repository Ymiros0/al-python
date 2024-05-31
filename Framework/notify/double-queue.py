local var_0_0 = setmetatable
local var_0_1 = {}
local var_0_2 = {}
local var_0_3 = {
	__index = var_0_2
}

def var_0_1.New():
	return var_0_0({
		first = 1,
		last = 0,
		data = {},
		data_position = {}
	}, var_0_3)

local function var_0_4(arg_2_0)
	while arg_2_0.first <= arg_2_0.last:
		if arg_2_0.data[arg_2_0.first]:
			return True

		arg_2_0.first = arg_2_0.first + 1

def var_0_2.is_empty(arg_3_0):
	return arg_3_0.first > arg_3_0.last

def var_0_2.push_front(arg_4_0, arg_4_1):
	if arg_4_0.data_position[arg_4_1]:
		return

	arg_4_0.first = arg_4_0.first - 1
	arg_4_0.data[arg_4_0.first] = arg_4_1
	arg_4_0.data_position[arg_4_1] = arg_4_0.first

def var_0_2.push_back(arg_5_0, arg_5_1):
	if arg_5_0.data_position[arg_5_1]:
		return

	arg_5_0.last = arg_5_0.last + 1
	arg_5_0.data[arg_5_0.last] = arg_5_1
	arg_5_0.data_position[arg_5_1] = arg_5_0.last

def var_0_2.get_iterator(arg_6_0):
	local var_6_0 = arg_6_0.first

	return function()
		while var_6_0 <= arg_6_0.last:
			local var_7_0 = arg_6_0.data[var_6_0]

			var_6_0 = var_6_0 + 1

			if var_7_0:
				return var_7_0

def var_0_2.remove(arg_8_0, arg_8_1):
	if not arg_8_0.data_position[arg_8_1]:
		return

	arg_8_0.data[arg_8_0.data_position[arg_8_1]] = None
	arg_8_0.data_position[arg_8_1] = None

	var_0_4(arg_8_0)

return var_0_1
