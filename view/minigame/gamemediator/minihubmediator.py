local var_0_0 = class("MiniHubMediator", import("..BaseMiniGameMediator"))

def var_0_0.register(arg_1_0):
	var_0_0.super.register(arg_1_0)

	local var_1_0 = {}

	arg_1_0.viewComponent.SetExtraData(var_1_0)

def var_0_0.OnMiniGameOPeration(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0.miniGameProxy.GetHubByGameId(arg_2_0.miniGameId)

	arg_2_0.sendNotification(GAME.SEND_MINI_GAME_OP, {
		hubid = var_2_0.id,
		cmd = arg_2_1,
		args1 = arg_2_2
	})

def var_0_0.OnMiniGameSuccess(arg_3_0, arg_3_1):
	if arg_3_0.gameRoomData:
		if arg_3_0.gameRoonCoinCount and arg_3_0.gameRoonCoinCount == 0:
			return

		local var_3_0 = arg_3_1
		local var_3_1 = arg_3_0.gameRoonCoinCount or 1
		local var_3_2 = arg_3_0.gameRoomData.id

		arg_3_0.sendNotification(GAME.GAME_ROOM_SUCCESS, {
			roomId = var_3_2,
			times = var_3_1,
			score = var_3_0
		})
	else
		local var_3_3 = arg_3_0.miniGameProxy.GetHubByGameId(arg_3_0.miniGameId)

		if var_3_3.count <= 0:
			return

		local var_3_4

		if arg_3_1 and type(arg_3_1) == "table":
			var_3_4 = arg_3_1
		else
			var_3_4 = {
				arg_3_1
			}

		arg_3_0.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = var_3_3.id,
			cmd = MiniGameOPCommand.CMD_COMPLETE,
			args1 = var_3_4,
			id = arg_3_0.miniGameId
		})

def var_0_0.OnMiniGameFailure(arg_4_0, arg_4_1):
	return

def var_0_0.listNotificationInterests(arg_5_0):
	local var_5_0 = {}

	table.insertto(var_5_0, var_0_0.super.listNotificationInterests(arg_5_0))

	return var_5_0

def var_0_0.handleNotification(arg_6_0, arg_6_1):
	var_0_0.super.handleNotification(arg_6_0, arg_6_1)

return var_0_0
