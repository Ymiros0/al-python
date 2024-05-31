local var_0_0 = class("LaunchBallTaskMediator", import("..base.ContextMediator"))

var_0_0.SUBMIT_ALL = "SUBMIT_ALL"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(LaunchBallTaskMediator.SUBMIT_ALL, function(arg_2_0, arg_2_1)
		arg_1_0.submit = #arg_2_1
		arg_1_0.awards = {}

		for iter_2_0 = 1, #arg_2_1:
			arg_1_0.sendNotification(GAME.SUBMIT_TASK, arg_2_1[iter_2_0].id))

def var_0_0.onUIAvalible(arg_3_0):
	return

def var_0_0.listNotificationInterests(arg_4_0):
	return {
		GAME.SUBMIT_TASK_DONE
	}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

	if var_5_0 == GAME.SUBMIT_AVATAR_TASK_DONE:
		if #var_5_1.awards > 0:
			arg_5_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_5_1.awards)

		if var_5_1.callback:
			-- block empty

		arg_5_0.viewComponent.updateTask(True)
	elif var_5_0 == GAME.SUBMIT_TASK_DONE:
		if arg_5_0.submit and arg_5_0.submit > 0:
			for iter_5_0 = 1, #var_5_1:
				table.insert(arg_5_0.awards, var_5_1[iter_5_0])

			arg_5_0.submit = arg_5_0.submit - 1

			if arg_5_0.submit == 0:
				arg_5_0.viewComponent.emit(BaseUI.ON_ACHIEVE, arg_5_0.awards, function()
					arg_5_0.viewComponent.updateTasks())
		else
			arg_5_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_5_1, function()
				arg_5_0.viewComponent.updateTasks())

return var_0_0
