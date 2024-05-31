local var_0_0 = class("GatewayNoticeMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	arg_1_0.updateNotices()

def var_0_0.updateNotices(arg_2_0):
	local var_2_0 = getProxy(GatewayNoticeProxy)

	arg_2_0.viewComponent.updateNotices(var_2_0.getGatewayNotices(False))

return var_0_0
