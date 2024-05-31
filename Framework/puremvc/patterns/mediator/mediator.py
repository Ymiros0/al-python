local var_0_0 = import("..observer.Notifier")
local var_0_1 = class("Mediator", var_0_0)

def var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.mediatorName = arg_1_1 or arg_1_0.__cname or var_0_1.NAME
	arg_1_0.viewComponent = arg_1_2

var_0_1.NAME = "Mediator"

def var_0_1.getMediatorName(arg_2_0):
	return arg_2_0.mediatorName

def var_0_1.setViewComponent(arg_3_0, arg_3_1):
	arg_3_0.viewComponent = arg_3_1

def var_0_1.getViewComponent(arg_4_0):
	return arg_4_0.viewComponent

def var_0_1.listNotificationInterests(arg_5_0):
	return {}

def var_0_1.handleNotification(arg_6_0, arg_6_1):
	return

def var_0_1.onRegister(arg_7_0):
	return

def var_0_1.onRemove(arg_8_0):
	return

return var_0_1
