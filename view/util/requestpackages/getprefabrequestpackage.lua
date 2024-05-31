﻿local var_0_0 = class("GetPrefabRequestPackage", import(".RequestPackage"))

function var_0_0.__call(arg_1_0)
	if arg_1_0.stopped then
		return
	end

	local var_1_0 = arg_1_0.path
	local var_1_1 = arg_1_0.name

	PoolMgr.GetInstance():GetPrefab(var_1_0, var_1_1, true, function(arg_2_0)
		if arg_1_0.stopped then
			PoolMgr.GetInstance():ReturnPrefab(var_1_0, var_1_1, arg_2_0, true)

			return
		end

		if arg_1_0.onLoaded then
			arg_1_0.onLoaded(arg_2_0)
		end
	end)

	return arg_1_0
end

function var_0_0.Ctor(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	arg_3_0.path = arg_3_1
	arg_3_0.name = arg_3_2
	arg_3_0.onLoaded = arg_3_3
end

return var_0_0
