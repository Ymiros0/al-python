local var_0_0 = class("ShootingGameMediator", import(".MiniHubMediator"))

def var_0_0.handleNotification(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getName()
	local var_1_1 = arg_1_1.getBody()

	if var_1_0 == GAME.SEND_MINI_GAME_OP_DONE and var_1_1.cmd == MiniGameOPCommand.CMD_COMPLETE:
		local var_1_2 = {
			function(arg_2_0)
				local var_2_0 = var_1_1.awards

				if #var_2_0 > 0:
					arg_1_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_2_0, arg_2_0)
				else
					arg_2_0(),
			function(arg_3_0)
				arg_1_0.viewComponent.OnGetAwardDone(var_1_1)
				arg_3_0()
		}

		arg_1_0.viewComponent.updateAfterFinish()
		arg_1_0.viewComponent.showResultPanel(var_1_1.awards, function()
			seriesAsync(var_1_2)
			arg_1_0.viewComponent.OnSendMiniGameOPDone(var_1_1))
	else
		var_0_0.super.handleNotification(arg_1_0, arg_1_1)

return var_0_0
