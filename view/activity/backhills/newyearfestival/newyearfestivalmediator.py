local var_0_0 = class("NewYearFestivalMediator", import("..TemplateMV.BackHillMediatorTemplate"))

var_0_0.MINIGAME_OPERATION = "MINIGAME_OPERATION"
var_0_0.ON_OPEN_PILE_SIGNED = "ON_OPEN_PILE_SIGNED"

def var_0_0.BindEvent(arg_1_0):
	var_0_0.super.BindEvent(arg_1_0)
	arg_1_0.bind(var_0_0.ON_OPEN_PILE_SIGNED, function()
		arg_1_0.addSubLayers(Context.New({
			viewComponent = PileGameSignedLayer,
			mediator = PileGameSignedMediator
		})))
	arg_1_0.bind(var_0_0.MINIGAME_OPERATION, function(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
		arg_1_0.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_3_1,
			cmd = arg_3_2,
			args1 = arg_3_3
		}))

def var_0_0.listNotificationInterests(arg_4_0):
	return {
		GAME.SEND_MINI_GAME_OP_DONE,
		ActivityProxy.ACTIVITY_UPDATED
	}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

	if var_5_0 == GAME.SEND_MINI_GAME_OP_DONE:
		local var_5_2 = {
			function(arg_6_0)
				local var_6_0 = var_5_1.awards

				if #var_6_0 > 0:
					arg_5_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_6_0, arg_6_0)
				else
					arg_6_0(),
			function(arg_7_0)
				arg_5_0.viewComponent.UpdateView()
		}

		seriesAsync(var_5_2)
		arg_5_0.OnSendMiniGameOPDone(var_5_1)
	elif var_5_0 == ActivityProxy.ACTIVITY_UPDATED:
		arg_5_0.viewComponent.UpdateView()

def var_0_0.OnSendMiniGameOPDone(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1.argList
	local var_8_1 = var_8_0[1]
	local var_8_2 = var_8_0[2]

	if var_8_1 == 3 and var_8_2 == 1:
		arg_8_0.viewComponent.UpdateView()

return var_0_0
