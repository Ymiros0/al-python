local var_0_0 = class("WorldShopMediator", import("view.base.ContextMediator"))

var_0_0.BUY_ITEM = "WorldShopMediator.BUY_ITEM"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.BUY_ITEM, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0.sendNotification(GAME.SHOPPING, {
			id = arg_2_1,
			count = arg_2_2
		}))

	local var_1_0 = getProxy(PlayerProxy)

	arg_1_0.viewComponent.setPlayer(var_1_0.getRawData())

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		PlayerProxy.UPDATED,
		GAME.SHOPPING_DONE
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == PlayerProxy.UPDATED:
		arg_4_0.viewComponent.setPlayer(var_4_1)
	elif var_4_0 == GAME.SHOPPING_DONE and #var_4_1.awards > 0:
		arg_4_0.viewComponent.emit(BaseUI.ON_AWARD, {
			items = var_4_1.awards
		})

return var_0_0
