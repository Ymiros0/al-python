local var_0_0 = class("AsyncParallelExcutionRequestPackage", import(".RequestPackage"))

def var_0_0.__call(arg_1_0):
	if arg_1_0.stopped:
		return

	if not arg_1_0.funcs or #arg_1_0.funcs == 0:
		return

	local var_1_0 = arg_1_0.funcs
	local var_1_1 = #var_1_0

	local function var_1_2()
		if arg_1_0.stopped:
			return

		var_1_1 = var_1_1 - 1

		if var_1_1 == 0 and arg_1_0.final:
			arg_1_0.final()

	if var_1_1 > 0:
		for iter_1_0, iter_1_1 in ipairs(var_1_0):
			iter_1_1(var_1_2)
	elif arg_1_0.final:
		arg_1_0.final()

def var_0_0.Ctor(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0.funcs = arg_3_1
	arg_3_0.final = arg_3_2

return var_0_0
