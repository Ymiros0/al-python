local var_0_0 = class("UnloadBundleRequesetPackage", import(".RequestPackage"))

def var_0_0.__call(arg_1_0):
	if arg_1_0.stopped:
		return

	ResourceMgr.Inst.ClearBundleRef(arg_1_0.path, True, True)

	return arg_1_0

def var_0_0.Ctor(arg_2_0, arg_2_1):
	arg_2_0.path = arg_2_1

return var_0_0
