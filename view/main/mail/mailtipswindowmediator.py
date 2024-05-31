local var_0_0 = class("MailTipsWindowMediator", import("view.base.ContextMediator"))

def var_0_0.register(arg_1_0):
	return

def var_0_0.listNotificationInterests(arg_2_0):
	return {}

def var_0_0.remove(arg_3_0):
	if arg_3_0.contextData.onClose:
		arg_3_0.contextData.onClose()

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

return var_0_0
