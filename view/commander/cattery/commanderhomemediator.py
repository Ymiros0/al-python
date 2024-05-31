local var_0_0 = class("CommanderHomeMediator", import("...base.ContextMediator"))

var_0_0.ON_CLEAN = "CommanderHomeMediator.ON_CLEAN"
var_0_0.ON_FEED = "CommanderHomeMediator.ON_FEED"
var_0_0.ON_PLAY = "CommanderHomeMediator.ON_PLAY"
var_0_0.ON_SEL_COMMANDER = "CommanderHomeMediator.ON_SEL_COMMANDER"
var_0_0.ON_CHANGE_STYLE = "CommanderHomeMediator.ON_CHANGE_STYLE"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_CLEAN, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.COMMANDER_CATTERY_OP, {
			op = 1
		}))
	arg_1_0.bind(var_0_0.ON_FEED, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.COMMANDER_CATTERY_OP, {
			op = 2
		}))
	arg_1_0.bind(var_0_0.ON_PLAY, function(arg_4_0, arg_4_1)
		arg_1_0.sendNotification(GAME.COMMANDER_CATTERY_OP, {
			op = 3
		}))
	arg_1_0.bind(var_0_0.ON_SEL_COMMANDER, function(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4)
		arg_5_3 = defaultValue(arg_5_3, True)

		arg_1_0.sendNotification(GAME.PUT_COMMANDER_IN_CATTERY, {
			id = arg_5_1,
			commanderId = arg_5_2,
			tip = arg_5_3,
			callback = arg_5_4
		}))
	arg_1_0.bind(var_0_0.ON_CHANGE_STYLE, function(arg_6_0, arg_6_1, arg_6_2)
		arg_1_0.sendNotification(GAME.COMMANDER_CHANGE_CATTERY_STYLE, {
			id = arg_6_1,
			styleId = arg_6_2
		}))
	arg_1_0.viewComponent.SetHome(getProxy(CommanderProxy).GetCommanderHome())

def var_0_0.listNotificationInterests(arg_7_0):
	return {
		GAME.PUT_COMMANDER_IN_CATTERY_DONE,
		GAME.COMMANDER_CHANGE_CATTERY_STYLE_DONE,
		GAME.COMMANDER_CATTERY_OP_DONE,
		GAME.ZERO_HOUR_OP_DONE,
		GAME.CALC_CATTERY_EXP_DONE
	}

def var_0_0.handleNotification(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1.getName()
	local var_8_1 = arg_8_1.getBody()

	if var_8_0 == GAME.PUT_COMMANDER_IN_CATTERY_DONE:
		arg_8_0.viewComponent.OnCatteryUpdate(var_8_1.id)
	elif var_8_0 == GAME.COMMANDER_CHANGE_CATTERY_STYLE_DONE:
		arg_8_0.viewComponent.OnCatteryStyleUpdate(var_8_1.id)
	elif var_8_0 == GAME.COMMANDER_CATTERY_OP_DONE:
		arg_8_0.viewComponent.forbiddenClose = True

		seriesAsync({
			function(arg_9_0)
				arg_8_0.viewComponent.OnCatteryOPDone()
				arg_8_0.viewComponent.OnOpAnimtion(var_8_1.cmd, var_8_1.opCatteries, arg_9_0),
			function(arg_10_0)
				arg_8_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_8_1.awards, arg_10_0)

				arg_8_0.viewComponent.forbiddenClose = False,
			function(arg_11_0)
				local var_11_0 = var_8_1.cmd

				arg_8_0.viewComponent.OnDisplayAwardDone(var_8_1)
		})
	elif var_8_0 == GAME.ZERO_HOUR_OP_DONE:
		arg_8_0.viewComponent.OnZeroHour()
	elif var_8_0 == GAME.CALC_CATTERY_EXP_DONE:
		arg_8_0.viewComponent.OnCommanderExpChange(var_8_1.commanderExps)

return var_0_0
