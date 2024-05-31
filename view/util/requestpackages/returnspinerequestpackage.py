local var_0_0 = class("ReturnSpineRequestPackage", import(".RequestPackage"))

def var_0_0.__call(arg_1_0):
	if arg_1_0.stopped:
		return

	if arg_1_0.callback:
		arg_1_0.callback(arg_1_0.model)

	pg.PoolMgr.GetInstance().ReturnSpineChar(arg_1_0.name, arg_1_0.model)

	return arg_1_0

def var_0_0.Ctor(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	arg_2_0.path = "Spine"
	arg_2_0.name = arg_2_1
	arg_2_0.model = arg_2_2
	arg_2_0.callback = arg_2_3

return var_0_0
