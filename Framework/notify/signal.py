local var_0_0 = require
local var_0_1 = setmetatable
local var_0_2 = var_0_0("Framework.notify.double-queue")
local var_0_3 = {}
local var_0_4 = {}
local var_0_5 = {
	__index = var_0_4
}

def var_0_4.disconnect(arg_1_0, arg_1_1):
	arg_1_0.handlers.remove(arg_1_1)

	arg_1_0.handlers_block[arg_1_1] = None

def var_0_4.connect(arg_2_0, arg_2_1):
	if not arg_2_0.handlers_block[arg_2_1]:
		arg_2_0.handlers_block[arg_2_1] = 0

		arg_2_0.handlers.push_back(arg_2_1)

def var_0_4.block(arg_3_0, arg_3_1):
	if arg_3_0.handlers_block[arg_3_1]:
		arg_3_0.handlers_block[arg_3_1] = arg_3_0.handlers_block[arg_3_1] + 1

def var_0_4.unblock(arg_4_0, arg_4_1):
	if arg_4_0.handlers_block[arg_4_1] and arg_4_0.handlers_block[arg_4_1] > 0:
		arg_4_0.handlers_block[arg_4_1] = arg_4_0.handlers_block[arg_4_1] - 1

def var_0_4.emit(arg_5_0, ...):
	arg_5_0.signal_stopped = False

	for iter_5_0 in arg_5_0.pre_emit_funcs.get_iterator():
		iter_5_0()

	for iter_5_1 in arg_5_0.handlers.get_iterator():
		if arg_5_0.signal_stopped:
			break

		if arg_5_0.handlers_block[iter_5_1] == 0:
			iter_5_1(...)

	for iter_5_2 in arg_5_0.post_emit_funcs.get_iterator():
		iter_5_2()

def var_0_4.emit_with_accumulator(arg_6_0, arg_6_1, ...):
	arg_6_0.signal_stopped = False

	for iter_6_0 in arg_6_0.pre_emit_funcs.get_iterator():
		iter_6_0()

	for iter_6_1 in arg_6_0.handlers.get_iterator():
		if arg_6_0.signal_stopped:
			break

		if arg_6_0.handlers_block[iter_6_1] == 0:
			arg_6_1(iter_6_1(...))

	for iter_6_2 in arg_6_0.post_emit_funcs.get_iterator():
		iter_6_2()

def var_0_4.add_pre_emit(arg_7_0, arg_7_1):
	arg_7_0.pre_emit_funcs.push_back(arg_7_1)

def var_0_4.remove_pre_emit(arg_8_0, arg_8_1):
	arg_8_0.pre_emit_funcs.remove(arg_8_1)

def var_0_4.add_post_emit(arg_9_0, arg_9_1):
	arg_9_0.post_emit_funcs.push_front(arg_9_1)

def var_0_4.remove_post_emit(arg_10_0, arg_10_1):
	arg_10_0.post_emit_funcs.remove(arg_10_1)

def var_0_4.stop(arg_11_0):
	arg_11_0.signal_stopped = True

def var_0_3.New():
	local var_12_0 = {}

	var_0_1(var_12_0, var_0_5)

	var_12_0.handlers_block = {}
	var_12_0.handlers = var_0_2.New()
	var_12_0.pre_emit_funcs = var_0_2.New()
	var_12_0.post_emit_funcs = var_0_2.New()
	var_12_0.signal_stopped = False

	return var_12_0

return var_0_3
