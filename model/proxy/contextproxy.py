local var_0_0 = class("ContextProxy", pm.Proxy)

def var_0_0.getCurrentContext(arg_1_0):
	return arg_1_0.data[#arg_1_0.data]

def var_0_0.pushContext(arg_2_0, arg_2_1):
	table.insert(arg_2_0.data, arg_2_1)

def var_0_0.popContext(arg_3_0):
	return table.remove(arg_3_0.data)

def var_0_0.cleanContext(arg_4_0):
	arg_4_0.data = {}

def var_0_0.getContextCount(arg_5_0):
	return #arg_5_0.data

def var_0_0.getContextByMediator(arg_6_0, arg_6_1):
	for iter_6_0 = #arg_6_0.data, 1, -1:
		local var_6_0 = arg_6_0.data[iter_6_0]
		local var_6_1 = var_6_0.getContextByMediator(arg_6_1)

		if var_6_1:
			return var_6_1, var_6_0

	return None

def var_0_0.CleanUntilMediator(arg_7_0, arg_7_1):
	for iter_7_0 = #arg_7_0.data, 1, -1:
		if not (arg_7_0.data[iter_7_0].mediator.__cname == arg_7_1.__cname):
			table.remove(arg_7_0.data, iter_7_0)
		else
			break

def var_0_0.GetPrevContext(arg_8_0, arg_8_1):
	return arg_8_0.data[#arg_8_0.data - arg_8_1]

def var_0_0.RemoveContext(arg_9_0, arg_9_1):
	for iter_9_0 = #arg_9_0.data, 1, -1:
		if arg_9_1 == arg_9_0.data[iter_9_0]:
			table.remove(arg_9_0.data, iter_9_0)

def var_0_0.PushContext2Prev(arg_10_0, arg_10_1, arg_10_2):
	arg_10_2 = arg_10_2 or 1

	local var_10_0 = math.clamp(#arg_10_0.data + 1 - arg_10_2, 1, #arg_10_0.data + 1)

	table.insert(arg_10_0.data, var_10_0, arg_10_1)

return var_0_0
