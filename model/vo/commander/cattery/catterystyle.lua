local var_0_0 = class("CatteryStyle", import("...BaseVO"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_0.id
	arg_1_0.own = arg_1_1.own
end

function var_0_0.bindConfigTable(arg_2_0)
	return pg.commander_home_style
end

function var_0_0.IsOwn(arg_3_0)
	return arg_3_0.own
end

function var_0_0.GetName(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_0:getConfig("name")

	return arg_4_1 and var_4_0 .. "_d" or var_4_0
end

return var_0_0
