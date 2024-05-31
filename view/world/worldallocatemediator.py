local var_0_0 = class("WorldAllocateMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	arg_1_0.viewComponent.setItem(arg_1_0.contextData.itemVO)
	arg_1_0.viewComponent.setFleets(arg_1_0.contextData.fleetList)
	arg_1_0.viewComponent.setConfirmCallback(arg_1_0.contextData.confirmCallback)

def var_0_0.listNotificationInterests(arg_2_0):
	return {
		GAME.WORLD_ITEM_USE_DONE
	}

def var_0_0.handleNotification(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.getName()
	local var_3_1 = arg_3_1.getBody()

	if var_3_0 == GAME.WORLD_ITEM_USE_DONE:
		arg_3_0.viewComponent.flush(var_3_1.item)

return var_0_0
