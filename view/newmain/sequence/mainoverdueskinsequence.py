local var_0_0 = class("MainOverDueSkinSequence", import(".MainOverDueAttireSequence"))

def var_0_0.Execute(arg_1_0, arg_1_1):
	local var_1_0 = getProxy(ShipSkinProxy).getOverDueSkins()

	if #var_1_0 > 0:
		arg_1_0.Display(SkinExpireDisplayPage, var_1_0, arg_1_1)
	else
		arg_1_1()

return var_0_0
