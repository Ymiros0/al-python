local var_0_0 = class("CheckCustomNameShip", import("model.vo.Ship"))

def var_0_0.getName(arg_1_0):
	if getProxy(PlayerProxy).getRawData().ShouldCheckCustomName():
		return arg_1_0.GetDefaultName()
	else
		return var_0_0.super.getName(arg_1_0)

return var_0_0
