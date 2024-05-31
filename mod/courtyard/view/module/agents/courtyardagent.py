local var_0_0 = class("CourtYardAgent")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	setmetatable(arg_1_0, {
		def __index:(arg_2_0, arg_2_1)
			local var_2_0 = rawget(arg_2_0, "class")

			return var_2_0[arg_2_1] and var_2_0[arg_2_1] or arg_1_1[arg_2_1]
	})

def var_0_0.Dispose(arg_3_0):
	return

return var_0_0
