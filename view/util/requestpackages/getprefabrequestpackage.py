local var_0_0 = class("GetPrefabRequestPackage", import(".RequestPackage"))

def var_0_0.__call(arg_1_0):
	if arg_1_0.stopped:
		return

	local var_1_0 = arg_1_0.path
	local var_1_1 = arg_1_0.name

	PoolMgr.GetInstance().GetPrefab(var_1_0, var_1_1, True, function(arg_2_0)
		if arg_1_0.stopped:
			PoolMgr.GetInstance().ReturnPrefab(var_1_0, var_1_1, arg_2_0, True)

			return

		if arg_1_0.onLoaded:
			arg_1_0.onLoaded(arg_2_0))

	return arg_1_0

def var_0_0.Ctor(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	arg_3_0.path = arg_3_1
	arg_3_0.name = arg_3_2
	arg_3_0.onLoaded = arg_3_3

return var_0_0
