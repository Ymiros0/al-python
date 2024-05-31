local var_0_0 = class("GuideDoFunctionStep", import(".GuideStep"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.func = arg_1_1.doFunc

def var_0_0.GetType(arg_2_0):
	return GuideStep.TYPE_DOFUNC

def var_0_0.GetFunction(arg_3_0):
	return arg_3_0.func

def var_0_0.ExistTrigger(arg_4_0):
	return True

return var_0_0
