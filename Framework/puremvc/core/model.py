local var_0_0 = class("Model")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	if var_0_0.instanceMap[arg_1_1]:
		error(var_0_0.MULTITON_MSG)

	arg_1_0.multitonKey = arg_1_1
	var_0_0.instanceMap[arg_1_1] = arg_1_0
	arg_1_0.proxyMap = {}

	arg_1_0.initializeModel()

def var_0_0.initializeModel(arg_2_0):
	return

def var_0_0.getInstance(arg_3_0):
	if arg_3_0 == None:
		return None

	if var_0_0.instanceMap[arg_3_0] == None:
		return var_0_0.New(arg_3_0)
	else
		return var_0_0.instanceMap[arg_3_0]

def var_0_0.registerProxy(arg_4_0, arg_4_1):
	arg_4_1.initializeNotifier(arg_4_0.multitonKey)

	arg_4_0.proxyMap[arg_4_1.getProxyName()] = arg_4_1

	arg_4_1.onRegister()

def var_0_0.retrieveProxy(arg_5_0, arg_5_1):
	return arg_5_0.proxyMap[arg_5_1]

def var_0_0.hasProxy(arg_6_0, arg_6_1):
	return arg_6_0.proxyMap[arg_6_1] != None

def var_0_0.removeProxy(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_0.proxyMap[arg_7_1]

	if var_7_0 != None:
		arg_7_0.proxyMap[arg_7_1] = None

		var_7_0.onRemove()

	return var_7_0

def var_0_0.removeModel(arg_8_0):
	var_0_0.instanceMap[arg_8_0] = None

var_0_0.instanceMap = {}
var_0_0.MULTITON_MSG = "Model instance for this Multiton key already constructed!"

return var_0_0
