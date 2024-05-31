local var_0_0 = class("State")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4):
	arg_1_0.name = arg_1_1

	if arg_1_2 != None:
		arg_1_0.entering = arg_1_2

	if arg_1_3 != None:
		arg_1_0.exiting = arg_1_3

	if arg_1_4 != None:
		arg_1_0.changed = arg_1_4

	arg_1_0.transitions = {}

def var_0_0.defineTrans(arg_2_0, arg_2_1, arg_2_2):
	assert(arg_2_1, "action should not be None at " .. arg_2_0.name)
	assert(arg_2_2, "target should not be None at " .. arg_2_0.name)

	if arg_2_0.getTarget(arg_2_1) != None:
		return

	arg_2_0.transitions[arg_2_1] = arg_2_2

def var_0_0.removeTrans(arg_3_0, arg_3_1):
	arg_3_0.transitions[arg_3_1] = None

def var_0_0.getTarget(arg_4_0, arg_4_1):
	return arg_4_0.transitions[arg_4_1]

return var_0_0
