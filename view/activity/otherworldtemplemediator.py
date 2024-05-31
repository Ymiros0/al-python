local var_0_0 = class("OtherWorldTempleMediator", import("..base.ContextMediator"))

var_0_0.OPEN_TERMINAL = "OPEN_TERMINAL"
var_0_0.SHOW_CHAR_AWARDS = "SHOW_CHAR_AWARDS"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.OPEN_TERMINAL, function()
		arg_1_0.addSubLayers(Context.New({
			mediator = OtherworldTerminalMediator,
			viewComponent = OtherworldTerminalLayer
		})))
	arg_1_0.bind(var_0_0.SHOW_CHAR_AWARDS, function(arg_3_0, arg_3_1, arg_3_2)
		arg_1_0.viewComponent.emit(BaseUI.ON_ACHIEVE, arg_3_1, arg_3_2))

def var_0_0.onUIAvalible(arg_4_0):
	return

def var_0_0.listNotificationInterests(arg_5_0):
	return {
		ActivityProxy.ACTIVITY_OPERATION_DONE,
		ActivityProxy.ACTIVITY_LOTTERY_SHOW_AWARDS,
		GAME.ZERO_HOUR_OP_DONE
	}

def var_0_0.handleNotification(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.getName()
	local var_6_1 = arg_6_1.getBody()

	if var_6_0 == ActivityProxy.ACTIVITY_OPERATION_DONE:
		if var_6_1 == ActivityConst.OTHER_WORLD_TERMINAL_LOTTERY_ID:
			arg_6_0.viewComponent.updateActivity()
			arg_6_0.viewComponent.displayTempleCharAward()
	elif var_6_0 == ActivityProxy.ACTIVITY_LOTTERY_SHOW_AWARDS:
		arg_6_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_6_1.awards, function()
			if var_6_1.callback:
				var_6_1.callback())
	elif var_6_0 == GAME.ZERO_HOUR_OP_DONE:
		-- block empty

return var_0_0
