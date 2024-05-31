local var_0_0 = class("BaseMiniGameView", import("..base.BaseUI"))

def var_0_0.SetExtraData(arg_1_0, arg_1_1):
	arg_1_0.mg_extraData = arg_1_1

def var_0_0.GetExtraValue(arg_2_0, arg_2_1):
	if arg_2_0.mg_extraData[arg_2_1]:
		return arg_2_0.mg_extraData[arg_2_1]
	else
		return None

def var_0_0.SetMGData(arg_3_0, arg_3_1):
	arg_3_0.mg_data = arg_3_1

def var_0_0.GetMGData(arg_4_0):
	return arg_4_0.mg_data

def var_0_0.SetMGHubData(arg_5_0, arg_5_1):
	arg_5_0.mg_hubData = arg_5_1

def var_0_0.GetMGHubData(arg_6_0):
	return arg_6_0.mg_hubData

def var_0_0.setGameRoomData(arg_7_0, arg_7_1):
	arg_7_0.gameRoomData = arg_7_1

def var_0_0.getGameRoomData(arg_8_0):
	return arg_8_0.gameRoomData or None

def var_0_0.SendSuccess(arg_9_0, ...):
	arg_9_0.emit(BaseMiniGameMediator.MINI_GAME_SUCCESS, ...)

def var_0_0.SendFailure(arg_10_0, ...):
	arg_10_0.emit(BaseMiniGameMediator.MINI_GAME_FAILURE, ...)

def var_0_0.StoreDataToServer(arg_11_0, arg_11_1):
	if arg_11_0.mg_data.getConfig("type") == MiniGameConst.MG_TYPE_2:
		local var_11_0 = {
			arg_11_0.mg_data.id,
			2
		}

		table.insertto(var_11_0, arg_11_1)
		arg_11_0.mg_data.SetRuntimeData("elements", arg_11_1)
		arg_11_0.emit(BaseMiniGameMediator.MINI_GAME_OPERATOR, MiniGameOPCommand.CMD_SPECIAL_GAME, var_11_0)

def var_0_0.SendOperator(arg_12_0, arg_12_1, arg_12_2):
	arg_12_0.emit(BaseMiniGameMediator.MINI_GAME_OPERATOR, arg_12_1, arg_12_2)

def var_0_0.OnSendMiniGameOPDone(arg_13_0, arg_13_1):
	return

def var_0_0.OnModifyMiniGameDataDone(arg_14_0, arg_14_1):
	return

def var_0_0.loadCoinLayer(arg_15_0):
	if not arg_15_0.coinLayer:
		arg_15_0.emit(BaseMiniGameMediator.MINI_GAME_COIN)

def var_0_0.setCoinLayer(arg_16_0):
	if arg_16_0.coinLayer:
		return

	arg_16_0.checkTicktRemind()

	arg_16_0.coinLayer = True

def var_0_0.openCoinLayer(arg_17_0, arg_17_1):
	if not arg_17_0.coinLayer:
		return

	if arg_17_1:
		arg_17_0.checkTicktRemind()

	arg_17_0.coinLayerVisible = arg_17_1

	arg_17_0.emit(BaseMiniGameMediator.COIN_WINDOW_CHANGE, arg_17_1)

def var_0_0.checkTicktRemind(arg_18_0):
	local var_18_0 = getProxy(GameRoomProxy).ticketMaxTip()

	if var_18_0 and not GameRoomProxy.ticket_remind:
		GameRoomProxy.ticket_remind = True

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = var_18_0,
			def onYes:()
				return,
			def onNo:()
				arg_18_0.closeView()
		})

def var_0_0.OnGetAwardDone(arg_21_0, arg_21_1):
	return

def var_0_0.OnApplicationPaused(arg_22_0, arg_22_1):
	return

return var_0_0
