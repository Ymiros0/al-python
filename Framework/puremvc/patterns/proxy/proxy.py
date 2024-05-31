local var_0_0 = import("..observer.Notifier")
local var_0_1 = class("Proxy", var_0_0)

def var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2):
	if arg_1_1 != None:
		arg_1_0.setData(arg_1_1)

	arg_1_0.proxyName = arg_1_2 or arg_1_0.__cname or var_0_1.NAME

var_0_1.NAME = "Proxy"

def var_0_1.getProxyName(arg_2_0):
	return arg_2_0.proxyName

def var_0_1.setData(arg_3_0, arg_3_1):
	arg_3_0.data = arg_3_1

def var_0_1.getData(arg_4_0):
	return arg_4_0.data

def var_0_1.onRegister(arg_5_0):
	return

def var_0_1.onRemove(arg_6_0):
	return

return var_0_1
