local var_0_0 = class("ZumaPTShopWindowMediator", import("...base.ContextMediator"))

def var_0_0.register(arg_1_0):
	return

def var_0_0.listNotificationInterests(arg_2_0):
	return {
		GAME.ISLAND_SHOPPING_DONE
	}

def var_0_0.handleNotification(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.getName()
	local var_3_1 = arg_3_1.getBody()

	if var_3_0 == GAME.ISLAND_SHOPPING_DONE:
		arg_3_0.viewComponent.closeView()

return var_0_0
