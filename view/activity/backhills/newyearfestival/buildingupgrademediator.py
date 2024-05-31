local var_0_0 = class("BuildingUpgradeMediator", import("view.base.ContextMediator"))

var_0_0.ACTIVITY_OPERATION = "ACTIVITY_OPERATION"

def var_0_0.register(arg_1_0):
	arg_1_0.BindEvent()

	local var_1_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF)

	assert(var_1_0, "Building Activity Not Found")
	arg_1_0.viewComponent.UpdateActivity(var_1_0)

def var_0_0.BindEvent(arg_2_0):
	arg_2_0.bind(var_0_0.ACTIVITY_OPERATION, function(arg_3_0, arg_3_1)
		arg_2_0.sendNotification(GAME.ACTIVITY_OPERATION, arg_3_1))

def var_0_0.listNotificationInterests(arg_4_0):
	return {
		ActivityProxy.ACTIVITY_UPDATED
	}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

	if var_5_0 == ActivityProxy.ACTIVITY_UPDATED and var_5_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF:
		arg_5_0.viewComponent.UpdateActivity(var_5_1)
		arg_5_0.viewComponent.Set(var_5_1)

return var_0_0
