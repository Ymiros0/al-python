﻿local var_0_0 = class("UnloadBundleRequesetPackage", import(".RequestPackage"))

function var_0_0.__call(arg_1_0)
	if arg_1_0.stopped then
		return
	end

	ResourceMgr.Inst:ClearBundleRef(arg_1_0.path, true, true)

	return arg_1_0
end

function var_0_0.Ctor(arg_2_0, arg_2_1)
	arg_2_0.path = arg_2_1
end

return var_0_0
