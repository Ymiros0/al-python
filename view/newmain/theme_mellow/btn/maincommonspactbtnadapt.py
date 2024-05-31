local var_0_0 = class("MainCommonSpActBtnAdapt")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.spActBtn = arg_1_1

	pg.DelegateInfo.New(arg_1_0)
	setmetatable(arg_1_0, {
		def __index:(arg_2_0, arg_2_1)
			local var_2_0 = rawget(arg_2_0, "class")

			return var_2_0[arg_2_1] and var_2_0[arg_2_1] or arg_1_0.spActBtn[arg_2_1]
	})

def var_0_0.GetUIName(arg_3_0):
	return arg_3_0.spActBtn.GetUIName()

def var_0_0.Dispose(arg_4_0):
	pg.DelegateInfo.Dispose(arg_4_0)
	arg_4_0.spActBtn.Dispose()

	arg_4_0.spActBtn = None

return var_0_0
