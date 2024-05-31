local var_0_0 = class("WSAnim", import("...BaseEntity"))

var_0_0.Fields = {
	caches = "table"
}

def var_0_0.Setup(arg_1_0):
	arg_1_0.caches = {}

def var_0_0.Dispose(arg_2_0):
	for iter_2_0, iter_2_1 in pairs(arg_2_0.caches):
		iter_2_1.Dispose()

	arg_2_0.Clear()

def var_0_0.GetAnim(arg_3_0, arg_3_1):
	return arg_3_0.caches[arg_3_1]

def var_0_0.SetAnim(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0.caches[arg_4_1] = arg_4_2

def var_0_0.Stop(arg_5_0):
	for iter_5_0, iter_5_1 in pairs(arg_5_0.caches):
		if iter_5_1.playing:
			iter_5_1.Stop()

return var_0_0
