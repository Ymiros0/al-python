local var_0_0 = require("Mgr/Pool/PoolUtil")
local var_0_1 = class("PoolObjPack")

function var_0_1.Ctor(arg_1_0, arg_1_1)
	arg_1_0.type = arg_1_1
	arg_1_0.items = {}
end

function var_0_1.Get(arg_2_0, arg_2_1)
	return arg_2_0.items[arg_2_1]
end

function var_0_1.Set(arg_3_0, arg_3_1, arg_3_2)
	arg_3_0.items[arg_3_1] = arg_3_2
end

function var_0_1.Remove(arg_4_0, arg_4_1)
	return table.removebykey(arg_4_0.items, arg_4_1)
end

function var_0_1.GetAmount(arg_5_0)
	return table.getCount(arg_5_0.items)
end

function var_0_1.Clear(arg_6_0)
	arg_6_0.items = nil
end

return var_0_1
