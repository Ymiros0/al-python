local var_0_0 = class("RedPacketMediator", import("view.base.ContextMediator"))

def var_0_0.register(arg_1_0):
	return

def var_0_0.listNotificationInterests(arg_2_0):
	return {
		ActivityProxy.ACTIVITY_SHOW_RED_PACKET_AWARDS,
		ActivityProxy.ACTIVITY_UPDATED
	}

def var_0_0.handleNotification(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.getName()
	local var_3_1 = arg_3_1.getBody()

	if var_3_0 == ActivityProxy.ACTIVITY_SHOW_RED_PACKET_AWARDS:
		arg_3_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_3_1.awards, var_3_1.callback)
	elif var_3_0 == ActivityProxy.ACTIVITY_UPDATED and var_3_1.id == arg_3_0.viewComponent.activityID:
		arg_3_0.viewComponent.onSubmitFinished()

return var_0_0
