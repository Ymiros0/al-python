local var_0_0 = class("SixthAnniversaryJPDarkMediator", import("view.base.ContextMediator"))

var_0_0.GO_SCENE = "GO_SCENE"
var_0_0.GO_SUBLAYER = "GO_SUBLAYER"

def var_0_0.register(arg_1_0):
	arg_1_0.BindEvent()

def var_0_0.BindEvent(arg_2_0):
	arg_2_0.bind(var_0_0.GO_SCENE, function(arg_3_0, arg_3_1, ...)
		arg_2_0.sendNotification(GAME.GO_SCENE, arg_3_1, ...))
	arg_2_0.bind(var_0_0.GO_SUBLAYER, function(arg_4_0, arg_4_1, arg_4_2)
		arg_2_0.addSubLayers(arg_4_1, None, arg_4_2))

def var_0_0.listNotificationInterests(arg_5_0):
	return {
		ActivityProxy.ACTIVITY_UPDATED,
		GAME.SUBMIT_TASK_DONE
	}

def var_0_0.handleNotification(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.getName()
	local var_6_1 = arg_6_1.getBody()

	if var_6_0 == ActivityProxy.ACTIVITY_UPDATED:
		if var_6_1.id == ActivityConst.MINIGAME_ZUMA:
			arg_6_0.viewComponent.UpdateLevels()
			arg_6_0.viewComponent.UpdateCount()
	elif var_6_0 == GAME.SUBMIT_TASK_DONE:
		arg_6_0.viewComponent.UpdateTaskTip()

return var_0_0
