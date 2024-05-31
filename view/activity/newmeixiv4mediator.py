local var_0_0 = class("NewMeixiV4Mediator", import("view.base.ContextMediator"))

var_0_0.ON_TASK_GO = "ON_TASK_GO"
var_0_0.ON_TASK_SUBMIT = "ON_TASK_SUBMIT"
var_0_0.GO_STORY = "GO_STORY"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_TASK_GO, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.TASK_GO, {
			taskVO = arg_2_1
		}))
	arg_1_0.bind(var_0_0.ON_TASK_SUBMIT, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.SUBMIT_TASK, arg_3_1.id))
	arg_1_0.bind(var_0_0.GO_STORY, function(arg_4_0, arg_4_1)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.WORLD_COLLECTION, {
			memoryGroup = arg_4_1
		}))

	local var_1_0 = getProxy(PlayerProxy)

	arg_1_0.viewComponent.setPlayer(var_1_0.getData())

def var_0_0.listNotificationInterests(arg_5_0):
	return {
		ActivityProxy.ACTIVITY_UPDATED,
		PlayerProxy.UPDATED,
		GAME.SUBMIT_TASK_DONE
	}

def var_0_0.handleNotification(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.getName()
	local var_6_1 = arg_6_1.getBody()

	if var_6_0 == ActivityProxy.ACTIVITY_UPDATED:
		if var_6_1.id == ActivityConst.NEWMEIXIV4_SKIRMISH_ID:
			arg_6_0.viewComponent.onUpdateTask()
	elif var_6_0 == PlayerProxy.UPDATED:
		arg_6_0.viewComponent.onUpdateRes(var_6_1)
	elif var_6_0 == GAME.SUBMIT_TASK_DONE:
		arg_6_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_6_1, function()
			arg_6_0.viewComponent.onUpdateTask())

return var_0_0
