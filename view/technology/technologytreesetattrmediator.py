local var_0_0 = class("TechnologyTreeSetAttrMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	return

def var_0_0.listNotificationInterests(arg_2_0):
	return {
		TechnologyConst.SET_TEC_ATTR_ADDITION_FINISH
	}

def var_0_0.handleNotification(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.getName()
	local var_3_1 = arg_3_1.getBody()

	if var_3_0 == TechnologyConst.SET_TEC_ATTR_ADDITION_FINISH:
		local var_3_2 = var_3_1.onSuccess

		if var_3_2:
			var_3_2()

return var_0_0
