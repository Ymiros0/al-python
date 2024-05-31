local var_0_0 = class("resumeMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	local var_1_0 = arg_1_0.contextData.player

	arg_1_0.viewComponent.setPlayerVO(var_1_0)

def var_0_0.listNotificationInterests(arg_2_0):
	return {}

def var_0_0.handleNotification(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.getName()
	local var_3_1 = arg_3_1.getBody()

return var_0_0
