local var_0_0 = class("EducateCharDockMediator", import("view.base.ContextMediator"))

var_0_0.GO_PROFILE = "EducateCharDockMediator.GO_PROFILE"
var_0_0.ON_SELECTED = "EducateCharDockMediator.ON_SELECTED"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_SELECTED, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.CHANGE_EDUCATE, {
			id = arg_2_1
		}))
	arg_1_0.bind(var_0_0.GO_PROFILE, function(arg_3_0)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.EDUCATE_PROFILE))

def var_0_0.listNotificationInterests(arg_4_0):
	return {
		GAME.CLEAR_EDUCATE_TIP
	}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

	if var_5_0 == GAME.CLEAR_EDUCATE_TIP:
		arg_5_0.viewComponent.emit(EducateCharDockScene.MSG_CLEAR_TIP, var_5_1.id)

return var_0_0
