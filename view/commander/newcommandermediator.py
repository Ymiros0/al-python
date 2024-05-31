local var_0_0 = class("NewCommanderMediator", import("..base.ContextMediator"))

var_0_0.ON_LOCK = "NewCommanderMediator.ON_LOCK"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_LOCK, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0.sendNotification(GAME.COMMANDER_LOCK, {
			commanderId = arg_2_1,
			flag = arg_2_2
		}))

	local var_1_0 = arg_1_0.contextData.commander

	assert(var_1_0, "commander can not be None")

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		GAME.COMMANDER_LOCK_DONE
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == GAME.COMMANDER_LOCK_DONE:
		arg_4_0.viewComponent.updateLockState()

return var_0_0
