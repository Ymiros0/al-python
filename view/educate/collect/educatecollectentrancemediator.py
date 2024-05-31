local var_0_0 = class("EducateCollectEntranceMediator", import("..base.EducateContextMediator"))

def var_0_0.register(arg_1_0):
	return

def var_0_0.listNotificationInterests(arg_2_0):
	return {
		EducateProxy.CLEAR_NEW_TIP
	}

def var_0_0.handleNotification(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.getName()
	local var_3_1 = arg_3_1.getBody()

	if var_3_0 == EducateProxy.CLEAR_NEW_TIP and var_3_1.index == EducateTipHelper.NEW_MEMORY:
		arg_3_0.viewComponent.updateMemoryTip()

return var_0_0
