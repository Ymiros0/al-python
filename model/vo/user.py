local var_0_0 = class("User", import(".BaseVO"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.type = arg_1_1.type
	arg_1_0.arg1 = arg_1_1.arg1
	arg_1_0.arg2 = arg_1_1.arg2
	arg_1_0.arg3 = arg_1_1.arg3
	arg_1_0.arg4 = arg_1_1.arg4
	arg_1_0.id = arg_1_1.uid
	arg_1_0.uid = arg_1_1.uid
	arg_1_0.token = arg_1_1.token
	arg_1_0.server = arg_1_1.server

def var_0_0.isLogin(arg_2_0):
	return tobool(arg_2_0.uid and arg_2_0.server and arg_2_0.token)

def var_0_0.clear(arg_3_0):
	arg_3_0.id = None
	arg_3_0.uid = None
	arg_3_0.token = None
	arg_3_0.server = None

return var_0_0
