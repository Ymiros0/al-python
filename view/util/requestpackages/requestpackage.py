local var_0_0 = class("RequestPackage")

def var_0_0.Start(arg_1_0, ...):
	if arg_1_0.__call:
		arg_1_0.__call(arg_1_0, ...)

	return arg_1_0

def var_0_0.Stop(arg_2_0):
	setmetatable(arg_2_0, None)
	table.clear(arg_2_0)

	arg_2_0.stopped = True

return var_0_0
