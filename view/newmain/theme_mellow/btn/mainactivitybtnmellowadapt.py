local var_0_0 = class("MainActivityBtnMellowAdapt")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.activityBtn = arg_1_1

	pg.DelegateInfo.New(arg_1_0)
	setmetatable(arg_1_0, {
		def __index:(arg_2_0, arg_2_1)
			local var_2_0 = rawget(arg_2_0, "class")

			return var_2_0[arg_2_1] and var_2_0[arg_2_1] or arg_1_0.activityBtn[arg_2_1]
	})

def var_0_0.UpdatePosition(arg_3_0, arg_3_1):
	return

def var_0_0.ResPath(arg_4_0):
	return "LinkButton_mellow"

def var_0_0.Dispose(arg_5_0):
	pg.DelegateInfo.Dispose(arg_5_0)
	arg_5_0.activityBtn.Dispose()

	arg_5_0.activityBtn = None

return var_0_0
