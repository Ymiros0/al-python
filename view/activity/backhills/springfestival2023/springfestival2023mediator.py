local var_0_0 = class("SpringFestival2023Mediator", import("..TemplateMV.BackHillMediatorTemplate"))

var_0_0.MINI_GAME_OPERATOR = "MINI_GAME_OPERATOR"
var_0_0.GO_SCENE = "GO_SCENE"
var_0_0.GO_SUBLAYER = "GO_SUBLAYER"
var_0_0.PLAY_FIREWORKS = "PLAY_FIREWORKS"

def var_0_0.register(arg_1_0):
	arg_1_0.BindEvent()

def var_0_0.BindEvent(arg_2_0):
	arg_2_0.bind(var_0_0.GO_SCENE, function(arg_3_0, arg_3_1, ...)
		arg_2_0.sendNotification(GAME.GO_SCENE, arg_3_1, ...))
	arg_2_0.bind(var_0_0.GO_SUBLAYER, function(arg_4_0, arg_4_1, arg_4_2)
		arg_2_0.addSubLayers(arg_4_1, None, arg_4_2))
	arg_2_0.bind(var_0_0.MINI_GAME_OPERATOR, function(arg_5_0, ...)
		arg_2_0.sendNotification(GAME.SEND_MINI_GAME_OP, ...))

def var_0_0.listNotificationInterests(arg_6_0):
	return {
		GAME.SEND_MINI_GAME_OP_DONE,
		ActivityProxy.ACTIVITY_UPDATED,
		var_0_0.PLAY_FIREWORKS
	}

def var_0_0.handleNotification(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_1.getName()
	local var_7_1 = arg_7_1.getBody()

	if var_7_0 == GAME.SEND_MINI_GAME_OP_DONE:
		local var_7_2 = {
			function(arg_8_0)
				local var_8_0 = var_7_1.awards

				if #var_8_0 > 0:
					arg_7_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_8_0, arg_8_0)
				else
					arg_8_0(),
			function(arg_9_0)
				arg_7_0.viewComponent.UpdateView()
		}

		seriesAsync(var_7_2)
	elif var_7_0 == ActivityProxy.ACTIVITY_UPDATED:
		arg_7_0.viewComponent.UpdateActivity(var_7_1)
	elif var_7_0 == var_0_0.PLAY_FIREWORKS:
		arg_7_0.viewComponent.PlayFireworks(var_7_1)

return var_0_0
