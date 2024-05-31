local var_0_0 = class("MetaCharacterSynMediator", import("...base.ContextMediator"))

var_0_0.OPEN_PT_GET_WAY_LAYER = "MetaCharacterSynMediator.OPEN_PT_GET_WAY_LAYER"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.OPEN_PT_GET_WAY_LAYER, function(arg_2_0)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = MetaPTGetPreviewLayer,
			mediator = MetaPTGetPreviewMediator,
			data = {}
		})))

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		GAME.ACT_NEW_PT_DONE,
		GAME.GET_META_PT_AWARD_DONE
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == GAME.GET_META_PT_AWARD_DONE:
		arg_4_0.viewComponent.updateData()
		arg_4_0.viewComponent.updateTaskList()
		arg_4_0.viewComponent.updateGetAwardBtn()

return var_0_0
