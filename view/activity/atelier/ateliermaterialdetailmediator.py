local var_0_0 = class("AtelierMaterialDetailMediator", import("view.base.ContextMediator"))

var_0_0.SHOW_DETAIL = "SHOW_DETAIL"
var_0_0.GO_RECIPE = "GO_RECIPE"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(GAME.GO_SCENE, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0.viewComponent.closeView()
		arg_1_0.sendNotification(GAME.GO_SCENE, arg_2_1, arg_2_2))
	arg_1_0.bind(var_0_0.GO_RECIPE, function(arg_3_0, arg_3_1)
		arg_1_0.viewComponent.closeView()

		if getProxy(ContextProxy).getCurrentContext().getContextByMediator(AtelierCompositeMediator):
			arg_1_0.sendNotification(AtelierCompositeMediator.OPEN_FORMULA, arg_3_1)
		else
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.ATELIER_COMPOSITE, {
				formulaId = arg_3_1
			}))

def var_0_0.listNotificationInterests(arg_4_0):
	return {}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

	if var_5_0 == None:
		-- block empty

def var_0_0.remove(arg_6_0):
	return

return var_0_0
