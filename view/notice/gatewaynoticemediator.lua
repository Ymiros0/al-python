local var_0_0 = class("GatewayNoticeMediator", import("..base.ContextMediator"))

function var_0_0.register(arg_1_0)
	arg_1_0:updateNotices()
end

function var_0_0.updateNotices(arg_2_0)
	local var_2_0 = getProxy(GatewayNoticeProxy)

	arg_2_0.viewComponent:updateNotices(var_2_0:getGatewayNotices(false))
end

return var_0_0
