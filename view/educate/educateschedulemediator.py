local var_0_0 = class("EducateScheduleMediator", import(".base.EducateContextMediator"))

var_0_0.GET_PLANS = "GET_PLANS"
var_0_0.OPEN_FILTER_LAYER = "OPEN_FILTER_LAYER"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.GET_PLANS, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.EDUCATE_GET_PLANS, {
			plans = EducatePlanProxy.GridData2ProtData(arg_2_1.gridData),
			isSkip = arg_2_1.isSkip,
			def callback:()
				return
		}))
	arg_1_0.bind(var_0_0.OPEN_FILTER_LAYER, function(arg_4_0, arg_4_1)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = EducateScheduleFilterLayer,
			mediator = EducateScheduleFilterMediator,
			data = arg_4_1
		})))

def var_0_0.listNotificationInterests(arg_5_0):
	return {
		GAME.EDUCATE_REFRESH_DONE
	}

def var_0_0.handleNotification(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.getName()
	local var_6_1 = arg_6_1.getBody()

	if var_6_0 == GAME.EDUCATE_REFRESH_DONE:
		arg_6_0.viewComponent.emit(EducateBaseUI.EDUCATE_CHANGE_SCENE, SCENE.EDUCATE)

return var_0_0
