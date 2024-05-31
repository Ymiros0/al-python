local var_0_0 = class("MainSubmitTaskSequence")

def var_0_0.Execute(arg_1_0, arg_1_1):
	getProxy(TaskProxy).pushAutoSubmitTask()
	arg_1_1()

return var_0_0
