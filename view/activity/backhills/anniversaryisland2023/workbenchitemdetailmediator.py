local var_0_0 = class("WorkBenchItemDetailMediator", import("view.base.ContextMediator"))

var_0_0.SHOW_DETAIL = "SHOW_DETAIL"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(GAME.WORKBENCH_ITEM_GO, function(arg_2_0, arg_2_1)
		arg_1_0.viewComponent.closeView()
		arg_1_0.sendNotification(GAME.WORKBENCH_ITEM_GO, arg_2_1))

def var_0_0.listNotificationInterests(arg_3_0):
	return {}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == None:
		-- block empty

def var_0_0.remove(arg_5_0):
	return

return var_0_0
