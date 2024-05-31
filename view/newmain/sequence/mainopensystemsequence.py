local var_0_0 = class("MainOpenSystemSequence")

def var_0_0.Execute(arg_1_0, arg_1_1):
	local var_1_0 = getProxy(PlayerProxy).getRawData()

	pg.SystemOpenMgr.GetInstance().notification(var_1_0.level)
	arg_1_1()

return var_0_0
