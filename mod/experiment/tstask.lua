local var_0_0 = class("TSTask")

function var_0_0.SetJob(arg_1_0, arg_1_1)
	arg_1_0.job = arg_1_1
end

function var_0_0.Execute(arg_2_0)
	local var_2_0 = os.clock()

	arg_2_0.job()

	return os.clock() - var_2_0
end

function var_0_0.Clear(arg_3_0)
	arg_3_0.job = nil
end

return var_0_0
