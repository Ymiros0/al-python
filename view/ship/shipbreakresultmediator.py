local var_0_0 = class("ShipBreakResultMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	if arg_1_0.contextData.newShip and arg_1_0.contextData.oldShip:
		arg_1_0.viewComponent.updateStatistics()

def var_0_0.listNotificationInterests(arg_2_0):
	return {}

def var_0_0.handleNotification(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.getName()
	local var_3_1 = arg_3_1.getBody()

return var_0_0
