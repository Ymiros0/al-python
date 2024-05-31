local var_0_0 = class("HololiveMedalCollectionMediator", import("view.base.ContextMediator"))

def var_0_0.register(arg_1_0):
	arg_1_0.BindEvent()

def var_0_0.BindEvent(arg_2_0):
	arg_2_0.bind(ActivityMediator.ON_TASK_SUBMIT, function(arg_3_0, arg_3_1)
		arg_2_0.sendNotification(GAME.SUBMIT_TASK, arg_3_1.id))
	arg_2_0.bind(ActivityMediator.ON_TASK_GO, function(arg_4_0, arg_4_1)
		arg_2_0.sendNotification(GAME.TASK_GO, {
			taskVO = arg_4_1
		}))

def var_0_0.listNotificationInterests(arg_5_0):
	return {
		GAME.MEMORYBOOK_UNLOCK_DONE,
		ActivityProxy.ACTIVITY_SHOW_AWARDS,
		GAME.SUBMIT_TASK_DONE,
		ActivityProxy.ACTIVITY_OPERATION_DONE
	}

def var_0_0.handleNotification(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.getName()
	local var_6_1 = arg_6_1.getBody()

	if var_6_0 == GAME.MEMORYBOOK_UNLOCK_DONE:
		arg_6_0.viewComponent.UpdateView()
	elif var_6_0 == ActivityProxy.ACTIVITY_SHOW_AWARDS:
		arg_6_0.viewComponent.PlayStory(function()
			arg_6_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_6_1.awards, var_6_1.callback))
	elif var_6_0 == GAME.SUBMIT_TASK_DONE:
		arg_6_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_6_1, function()
			arg_6_0.viewComponent.UpdateView())
	elif var_6_0 == ActivityProxy.ACTIVITY_OPERATION_DONE:
		arg_6_0.viewComponent.UpdateView()

return var_0_0
