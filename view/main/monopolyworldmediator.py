local var_0_0 = class("MonthCardSetMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	return

def var_0_0.listNotificationInterests(arg_2_0):
	return {
		GAME.MONOPOLY_AWARD_DONE
	}

def var_0_0.handleNotification(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.getName()
	local var_3_1 = arg_3_1.getBody()

	if var_3_0 == GAME.MONOPOLY_AWARD_DONE:
		arg_3_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_3_1.awards, var_3_1.callback)

return var_0_0
