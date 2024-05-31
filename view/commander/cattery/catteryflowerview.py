local var_0_0 = class("CatteryFlowerView")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0.default = arg_1_0._tf.Find("1")
	arg_1_0.levels = {
		arg_1_0._tf.Find("2"),
		arg_1_0._tf.Find("3"),
		arg_1_0._tf.Find("4"),
		arg_1_0._tf.Find("5")
	}

def var_0_0.Update(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_1.GetCleanLevel()
	local var_2_1 = True

	for iter_2_0, iter_2_1 in pairs(arg_2_0.levels):
		local var_2_2 = var_2_0 == iter_2_0

		setActive(iter_2_1, var_2_2)

		if var_2_1 and var_2_2:
			var_2_1 = False

	setActive(arg_2_0.default, var_2_1)

def var_0_0.Dispose(arg_3_0):
	arg_3_0.levels = None

return var_0_0
