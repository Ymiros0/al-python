local var_0_0 = class("PileGameSignedMediator", import("...base.ContextMediator"))

var_0_0.ON_GET_AWARD = "PileGameSignedMediator.ON_GET_AWARD"
var_0_0.MINIGAME_ID = 5

def var_0_0.register(arg_1_0):
	local var_1_0 = getProxy(MiniGameProxy)

	arg_1_0.bind(var_0_0.ON_GET_AWARD, function(arg_2_0)
		arg_1_0.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = var_0_0.MINIGAME_ID,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		}))

	local var_1_1 = var_1_0.GetHubByHubId(var_0_0.MINIGAME_ID)

	arg_1_0.viewComponent.SetData(var_1_1)

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		MiniGameProxy.ON_HUB_DATA_UPDATE
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == MiniGameProxy.ON_HUB_DATA_UPDATE:
		arg_4_0.viewComponent.SetData(var_4_1)
		arg_4_0.viewComponent.UpdateSigned()

return var_0_0
