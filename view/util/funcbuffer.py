local var_0_0 = class("FuncBuffer")

def var_0_0.Ctor(arg_1_0):
	arg_1_0.buffers = {}
	arg_1_0.notifier = False

def var_0_0.SetNotifier(arg_2_0, arg_2_1):
	arg_2_0.notifier = defaultValue(arg_2_1, False)

def var_0_0.IsEmpty(arg_3_0):
	return #arg_3_0.buffers <= 0

def var_0_0.Pop(arg_4_0):
	return table.remove(arg_4_0.buffers, 1)

def var_0_0.Push(arg_5_0, arg_5_1, ...):
	table.insert(arg_5_0.buffers, {
		funcName = arg_5_1,
		params = {
			...
		},
		paramLength = select("#", ...)
	})
	arg_5_0.ExcuteAll()

def var_0_0.ExcuteAll(arg_6_0):
	if arg_6_0.notifier:
		while not arg_6_0.IsEmpty():
			local var_6_0 = arg_6_0.Pop()

			arg_6_0.notifier[var_6_0.funcName](arg_6_0.notifier, unpack(var_6_0.params, 1, var_6_0.paramLength))

def var_0_0.Clear(arg_7_0):
	table.clear(arg_7_0.buffers)

def var_0_0.__index(arg_8_0, arg_8_1):
	return rawget(arg_8_0, arg_8_1) or var_0_0[arg_8_1] or function(arg_9_0, ...)
		arg_8_0.Push(arg_8_1, ...)

return var_0_0
