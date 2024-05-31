local var_0_0 = class("HoloLiveLinkLinkSelectMediator", import("view.base.ContextMediator"))

var_0_0.HUB_ID = 3

def var_0_0.register(arg_1_0):
	arg_1_0.BindEvent()
	arg_1_0.requestDataFromServer()

def var_0_0.requestDataFromServer(arg_2_0):
	pg.ConnectionMgr.GetInstance().Send(26101, {
		type = MiniGameRequestCommand.REQUEST_HUB_DATA
	}, 26102, function(arg_3_0)
		local var_3_0 = getProxy(MiniGameProxy)

		for iter_3_0, iter_3_1 in ipairs(arg_3_0.hubs):
			if iter_3_1.id == var_0_0.HUB_ID:
				var_3_0.UpdataHubData(iter_3_1))

def var_0_0.BindEvent(arg_4_0):
	return

def var_0_0.listNotificationInterests(arg_5_0):
	return {
		MiniGameProxy.ON_HUB_DATA_UPDATE,
		GAME.SEND_MINI_GAME_OP_DONE
	}

def var_0_0.handleNotification(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.getName()
	local var_6_1 = arg_6_1.getBody()

	if var_6_0 == MiniGameProxy.ON_HUB_DATA_UPDATE:
		if var_6_1.id == HoloLiveLinkLinkSelectScene.HOLOLIVE_LINKGAME_HUB_ID:
			arg_6_0.viewComponent.updateData()
			arg_6_0.viewComponent.updateUI()
	elif var_6_0 == GAME.SEND_MINI_GAME_OP_DONE and var_6_1.cmd == MiniGameOPCommand.CMD_ULTIMATE:
		local var_6_2 = {
			function(arg_7_0)
				local var_7_0 = var_6_1.awards

				if #var_7_0 > 0:
					arg_6_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_7_0, arg_7_0)
				else
					arg_7_0(),
			function(arg_8_0)
				arg_6_0.viewComponent.updateData()
				arg_6_0.viewComponent.updateUI()
		}

		seriesAsync(var_6_2)

return var_0_0
