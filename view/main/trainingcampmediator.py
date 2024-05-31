local var_0_0 = class("TrainingCampMediator", import("..base.ContextMediator"))

var_0_0.ON_GET = "TrainingCampMediator.ON_GET"
var_0_0.ON_GO = "TrainingCampMediator.ON_GO"
var_0_0.ON_TRIGGER = "TrainingCampMediator.ON_TRIGGER"
var_0_0.ON_SELECTABLE_GET = "TrainingCampMediator.ON_SELECTABLE_GET"
var_0_0.ON_UPDATE = "TrainingCampMediator.ON_UPDATE"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_UPDATE, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.UPDATE_TASK_PROGRESS, {
			taskId = arg_2_1.id
		}))
	arg_1_0.bind(var_0_0.ON_SELECTABLE_GET, function(arg_3_0, arg_3_1, arg_3_2)
		arg_1_0.sendNotification(GAME.SUBMIT_TASK, {
			taskId = arg_3_1.id,
			index = arg_3_2
		}))
	arg_1_0.bind(var_0_0.ON_GET, function(arg_4_0, arg_4_1)
		arg_1_0.sendNotification(GAME.SUBMIT_TASK, arg_4_1.id))
	arg_1_0.bind(var_0_0.ON_GO, function(arg_5_0, arg_5_1)
		local var_5_0 = arg_5_1.getConfig("scene")

		if var_5_0 and #var_5_0 > 0:
			if var_5_0[1] == "LEVEL" and var_5_0[2] and var_5_0[2].chapterid:
				arg_1_0.goToLevel(var_5_0[2].chapterid)
			elif SCENE[var_5_0[1]]:
				arg_1_0.sendNotification(GAME.GO_SCENE, SCENE[var_5_0[1]], var_5_0[2])
		else
			arg_1_0.sendNotification(GAME.TASK_GO, {
				taskVO = arg_5_1
			}))
	arg_1_0.bind(var_0_0.ON_TRIGGER, function(arg_6_0, arg_6_1)
		arg_1_0.sendNotification(GAME.ACTIVITY_OPERATION, arg_6_1))

var_0_0.TASK_ADDED = "task added"
var_0_0.TASK_UPDATED = "task updated"
var_0_0.TASK_REMOVED = "task removed"

def var_0_0.listNotificationInterests(arg_7_0):
	return {
		TaskProxy.TASK_UPDATED,
		TaskProxy.TASK_REMOVED,
		GAME.SUBMIT_TASK_DONE,
		ActivityProxy.ACTIVITY_OPERATION_DONE
	}

def var_0_0.handleNotification(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1.getName()
	local var_8_1 = arg_8_1.getBody()

	if var_8_0 == TaskProxy.TASK_UPDATED or var_8_0 == TaskProxy.TASK_REMOVED:
		arg_8_0.viewComponent.switchPageByMediator()
		arg_8_0.viewComponent.updateSwitchBtnsTag()
	elif var_8_0 == GAME.SUBMIT_TASK_DONE:
		arg_8_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_8_1)
		arg_8_0.viewComponent.setPhrase()
		arg_8_0.viewComponent.updateSwitchBtnsTag()
	elif var_8_0 == ActivityProxy.ACTIVITY_OPERATION_DONE:
		arg_8_0.viewComponent.tryShowTecFixTip()
		arg_8_0.viewComponent.switchPageByMediator()
		arg_8_0.viewComponent.updateSwitchBtnsTag()

return var_0_0
