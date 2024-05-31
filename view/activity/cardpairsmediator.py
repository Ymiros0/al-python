local var_0_0 = class("CardPairsMediator", import("..base.ContextMediator"))

var_0_0.EVENT_OPERATION = "event operation"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.EVENT_OPERATION, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.ACTIVITY_OPERATION, arg_2_1))
	arg_1_0.setActivityData()
	arg_1_0.setPlayerData()

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		ActivityProxy.ACTIVITY_UPDATED,
		PlayerProxy.UPDATED,
		ActivityProxy.ACTIVITY_SHOW_AWARDS,
		ActivityProxy.ACTIVITY_OPERATION_DONE
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == ActivityProxy.ACTIVITY_UPDATED:
		arg_4_0.viewComponent.setActivityData(var_4_1)
	elif var_4_0 == PlayerProxy.UPDATED:
		arg_4_0.viewComponent.setPlayerData(var_4_1)
	elif var_4_0 == ActivityProxy.ACTIVITY_SHOW_AWARDS:
		arg_4_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_4_1.awards, var_4_1.callback)
	elif var_4_0 == ActivityProxy.ACTIVITY_OPERATION_DONE:
		arg_4_0.viewComponent.checkActivityEnd()

def var_0_0.setPlayerData(arg_5_0):
	local var_5_0 = getProxy(PlayerProxy).getData()

	arg_5_0.viewComponent.setPlayerData(var_5_0)

def var_0_0.setActivityData(arg_6_0):
	local var_6_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_CARD_PAIRS)

	arg_6_0.viewComponent.setActivityData(var_6_0)

return var_0_0
