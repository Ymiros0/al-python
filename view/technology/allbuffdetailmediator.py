local var_0_0 = class("AllBuffDetailMediator", import("..base.ContextMediator"))

var_0_0.OPEN_SET_VALUE_LAYER = "AllBuffDetailMediator.OPEN_SET_VALUE_LAYER"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.OPEN_SET_VALUE_LAYER, function()
		arg_1_0.addSubLayers(Context.New({
			mediator = TechnologyTreeSetAttrMediator,
			viewComponent = TechnologyTreeSetAttrLayer,
			data = {
				LayerWeightMgr_weight = LayerWeightConst.TOP_LAYER
			},
			def onRemoved:()
				arg_1_0.viewComponent.updateDetail()
		})))

def var_0_0.listNotificationInterests(arg_4_0):
	return {}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

return var_0_0
