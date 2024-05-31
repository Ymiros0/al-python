local var_0_0 = require("Mgr/Pool/PoolUtil")
local var_0_1 = class("PoolSingleton")

def var_0_1.Ctor(arg_1_0, arg_1_1):
	arg_1_0.prefab = arg_1_1
	arg_1_0.index = 0

def var_0_1.Clear(arg_2_0):
	var_0_0.Destroy(arg_2_0.prefab)

	arg_2_0.prefab = None
	arg_2_0.index = 0

return var_0_1
