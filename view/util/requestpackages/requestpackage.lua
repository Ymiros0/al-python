local var_0_0 = class("RequestPackage")

function var_0_0.Start(arg_1_0, ...)
	if arg_1_0.__call then
		arg_1_0.__call(arg_1_0, ...)
	end

	return arg_1_0
end

function var_0_0.Stop(arg_2_0)
	setmetatable(arg_2_0, nil)
	table.clear(arg_2_0)

	arg_2_0.stopped = true
end

return var_0_0
