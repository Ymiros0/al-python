local var_0_0 = class("CrusingWindowMediator", import("view.base.ContextMediator"))

var_0_0.GO_CRUSING = "CrusingWindowMediator.GO_CRUSING"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.GO_CRUSING, function(arg_2_0)
		arg_1_0.contextData.onClose = None

		arg_1_0.viewComponent.closeView()
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.CRUSING))

def var_0_0.listNotificationInterests(arg_3_0):
	return {}

def var_0_0.remove(arg_4_0):
	if arg_4_0.contextData.onClose:
		arg_4_0.contextData.onClose()

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

return var_0_0
