def string.split(arg_1_0, arg_1_1):
	arg_1_0 = tostring(arg_1_0)
	arg_1_1 = tostring(arg_1_1)

	if arg_1_1 == "":
		return False

	local var_1_0 = 0
	local var_1_1 = {}

	for iter_1_0, iter_1_1 in function()
		return string.find(arg_1_0, arg_1_1, var_1_0, True):
		table.insert(var_1_1, string.sub(arg_1_0, var_1_0, iter_1_0 - 1))

		var_1_0 = iter_1_1 + 1

	table.insert(var_1_1, string.sub(arg_1_0, var_1_0))

	return var_1_1

def import(arg_3_0, arg_3_1):
	local var_3_0
	local var_3_1 = arg_3_0
	local var_3_2 = 1

	while True:
		if string.byte(arg_3_0, var_3_2) != 46:
			var_3_1 = string.sub(arg_3_0, var_3_2)

			if var_3_0 and #var_3_0 > 0:
				var_3_1 = table.concat(var_3_0, ".") .. "." .. var_3_1

			break

		var_3_2 = var_3_2 + 1

		if not var_3_0:
			if not arg_3_1:
				local var_3_3, var_3_4 = debug.getlocal(3, 1)

				arg_3_1 = var_3_4

			var_3_0 = string.split(arg_3_1, ".")

		table.remove(var_3_0, #var_3_0)

	return require(var_3_1)
