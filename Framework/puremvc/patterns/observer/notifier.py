local var_0_0 = import("..facade.Facade")
local var_0_1 = class("Notifier")

def var_0_1.Ctor(arg_1_0):
	return

def var_0_1.sendNotification(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	local var_2_0 = arg_2_0.getFacade()

	if var_2_0 != None:
		var_2_0.sendNotification(arg_2_1, arg_2_2, arg_2_3)

def var_0_1.initializeNotifier(arg_3_0, arg_3_1):
	arg_3_0.multitonKey = arg_3_1
	arg_3_0.facade = arg_3_0.getFacade()

def var_0_1.getFacade(arg_4_0):
	if arg_4_0.multitonKey == None:
		error(var_0_1.MULTITON_MSG)

	return var_0_0.getInstance(arg_4_0.multitonKey)

var_0_1.MULTITON_MSG = "multitonKey for this Notifier not yet initialized!"

return var_0_1
