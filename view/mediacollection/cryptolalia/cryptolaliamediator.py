local var_0_0 = class("CryptolaliaMediator", import("view.base.ContextMediator"))

var_0_0.UNLOCK = "CryptolaliaMediator.UNLOCK"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.UNLOCK, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0.sendNotification(GAME.UNLOCK_CRYPTOLALIA, {
			id = arg_2_1,
			costType = arg_2_2
		}))

	local var_1_0 = getProxy(PlayerProxy).getRawData()

	arg_1_0.viewComponent.SetCryptolaliaList(var_1_0.GetCryptolaliaList())

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		GAME.UNLOCK_CRYPTOLALIA_DONE
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == GAME.UNLOCK_CRYPTOLALIA_DONE:
		arg_4_0.viewComponent.emit(CryptolaliaScene.ON_UNLOCK, var_4_1.id)

return var_0_0
