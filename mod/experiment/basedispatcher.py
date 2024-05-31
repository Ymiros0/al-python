local var_0_0 = class("BaseDispatcher")

def var_0_0.Ctor(arg_1_0):
	arg_1_0.__callbacks = {}
	arg_1_0.__list = {}

def var_0_0.AddListener(arg_2_0, arg_2_1, arg_2_2):
	assert(type(arg_2_1) == "string" and type(arg_2_2) == "function")

	if not arg_2_0.__callbacks[arg_2_1]:
		arg_2_0.__callbacks[arg_2_1] = {}

	table.insert(arg_2_0.__callbacks[arg_2_1], arg_2_2)

def var_0_0.RemoveListener(arg_3_0, arg_3_1, arg_3_2):
	assert(type(arg_3_1) == "string" and type(arg_3_2) == "function")

	local var_3_0 = arg_3_0.__callbacks[arg_3_1]

	if var_3_0:
		for iter_3_0 = #var_3_0, 1, -1:
			if var_3_0[iter_3_0] == arg_3_2:
				table.remove(var_3_0, iter_3_0)

def var_0_0.ClearListener(arg_4_0, arg_4_1):
	assert(type(arg_4_1) == "string")

	arg_4_0.__callbacks[arg_4_1] = None

def var_0_0.DispatchEvent(arg_5_0, arg_5_1, ...):
	assert(type(arg_5_1) == "string")

	local var_5_0 = arg_5_0.__callbacks[arg_5_1]

	if var_5_0:
		local var_5_1 = #var_5_0

		for iter_5_0 = 1, var_5_1:
			arg_5_0.__list[iter_5_0] = var_5_0[iter_5_0]

		for iter_5_1 = 1, var_5_1:
			arg_5_0.__list[iter_5_1](arg_5_1, arg_5_0, ...)

def var_0_0.ClearListeners(arg_6_0):
	for iter_6_0, iter_6_1 in pairs(arg_6_0.__callbacks):
		arg_6_0.__callbacks[iter_6_0] = None

	for iter_6_2, iter_6_3 in ipairs(arg_6_0.__list):
		arg_6_0.__list[iter_6_2] = None

return var_0_0
