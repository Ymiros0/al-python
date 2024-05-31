local var_0_0 = class("PtAwardMediator", import("view.base.ContextMediator"))

def var_0_0.register(arg_1_0):
	arg_1_0.bind(ActivityMediator.EVENT_PT_OPERATION, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.ACT_NEW_PT, arg_2_1))

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		ActivityProxy.ACTIVITY_UPDATED,
		GAME.ACT_NEW_PT_DONE
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == None:
		-- block empty
	elif var_4_0 == ActivityProxy.ACTIVITY_ADDED or var_4_0 == ActivityProxy.ACTIVITY_UPDATED:
		if var_4_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_PT_BUFF and var_4_1.getDataConfig("pt") == arg_4_0.contextData.ptId:
			if arg_4_0.contextData.ptData:
				arg_4_0.contextData.ptData.Update(var_4_1)
			else
				arg_4_0.contextData.ptData = ActivityBossPtData.New(var_4_1)

			arg_4_0.viewComponent.UpdateView()
	elif var_4_0 == GAME.ACT_NEW_PT_DONE:
		arg_4_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_4_1.awards)

def var_0_0.remove(arg_5_0):
	return

return var_0_0
