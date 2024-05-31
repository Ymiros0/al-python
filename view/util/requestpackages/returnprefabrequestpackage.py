local var_0_0 = class("ReturnPrefabRequestPackage", import(".RequestPackage"))

def var_0_0.__call(arg_1_0):
	if arg_1_0.stopped:
		return

	if arg_1_0.callback:
		arg_1_0.callback(arg_1_0.go)

	PoolMgr.GetInstance().ReturnPrefab(arg_1_0.path, arg_1_0.name, arg_1_0.go, True)

	return arg_1_0

def var_0_0.Ctor(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4):
	arg_2_0.path = arg_2_1
	arg_2_0.name = arg_2_2
	arg_2_0.go = arg_2_3
	arg_2_0.callback = arg_2_4

return var_0_0
