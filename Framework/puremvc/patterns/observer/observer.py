local var_0_0 = class("Observer")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.setNotifyMethod(arg_1_1)
	arg_1_0.setNotifyContext(arg_1_2)

def var_0_0.setNotifyMethod(arg_2_0, arg_2_1):
	arg_2_0.notify = arg_2_1

def var_0_0.setNotifyContext(arg_3_0, arg_3_1):
	arg_3_0.context = arg_3_1

def var_0_0.getNotifyMethod(arg_4_0):
	return arg_4_0.notify

def var_0_0.getNotifyContext(arg_5_0):
	return arg_5_0.context

def var_0_0.notifyObserver(arg_6_0, arg_6_1):
	arg_6_0.notify(arg_6_0.context, arg_6_1)

def var_0_0.compareNotifyContext(arg_7_0, arg_7_1):
	return arg_7_1 == arg_7_0.context

return var_0_0
