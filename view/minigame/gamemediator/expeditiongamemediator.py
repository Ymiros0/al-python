local var_0_0 = class("ExpeditionGameMediator", import(".MiniHubMediator"))

def var_0_0.listNotificationInterests(arg_1_0):
	local var_1_0 = {
		ActivityProxy.ACTIVITY_UPDATED,
		ActivityProxy.ACTIVITY_SHOW_AWARDS,
		GAME.BEGIN_STAGE_DONE
	}

	table.insertto(var_1_0, var_0_0.super.listNotificationInterests(arg_1_0))

	return var_1_0

def var_0_0.handleNotification(arg_2_0, arg_2_1):
	var_0_0.super.handleNotification(arg_2_0, arg_2_1)

	local var_2_0 = arg_2_1.getName()
	local var_2_1 = arg_2_1.getBody()

	if var_2_0 == ActivityProxy.ACTIVITY_UPDATED:
		arg_2_0.viewComponent.activityUpdate()
	elif var_2_0 == ActivityProxy.ACTIVITY_SHOW_AWARDS:
		arg_2_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_2_1.awards, var_2_1.callback)
	elif var_2_0 == GAME.BEGIN_STAGE_DONE:
		arg_2_0.sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_2_1)

return var_0_0
