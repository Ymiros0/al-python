﻿local var_0_0 = class("BackYardSettlementMediator", import("...base.ContextMediator"))

function var_0_0.register(arg_1_0)
	local var_1_0 = getProxy(DormProxy)

	arg_1_0.viewComponent:setShipVOs(arg_1_0.contextData.oldShips, arg_1_0.contextData.newShips)
	arg_1_0.viewComponent:setDormVO(var_1_0:getRawData())
end

function var_0_0.listNotificationInterests(arg_2_0)
	return {}
end

function var_0_0.handleNotification(arg_3_0)
	return
end

return var_0_0