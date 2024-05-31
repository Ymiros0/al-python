local var_0_0 = class("IdolMedalCollectionMediator", import("view.base.ContextMediator"))

def var_0_0.register(arg_1_0):
	arg_1_0.BindEvent()

def var_0_0.BindEvent(arg_2_0):
	return

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		GAME.MEMORYBOOK_UNLOCK_DONE,
		ActivityProxy.ACTIVITY_SHOW_AWARDS,
		ActivityProxy.ACTIVITY_UPDATED
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == GAME.MEMORYBOOK_UNLOCK_DONE:
		arg_4_0.viewComponent.updateAfterSubmit(var_4_1)
	elif var_4_0 == ActivityProxy.ACTIVITY_UPDATED:
		if var_4_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_PUZZLA:
			arg_4_0.viewComponent.UpdateActivity()
	elif var_4_0 == ActivityProxy.ACTIVITY_SHOW_AWARDS:
		local var_4_2 = getProxy(ContextProxy).getContextByMediator(ActivityMediator)

		arg_4_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_4_1.awards, var_4_1.callback)

return var_0_0
