local var_0_0 = class("EducateExtraAttrMediator", import(".base.EducateContextMediator"))

var_0_0.ON_ATTR_ADD = "EducateExtraAttrMediator.ON_ATTR_ADD"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_ATTR_ADD, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.EDUCATE_ADD_EXTRA_ATTR, {
			id = arg_2_1.id
		}))

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		GAME.EDUCATE_ADD_EXTRA_ATTR_DONE
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == GAME.EDUCATE_ADD_EXTRA_ATTR_DONE:
		arg_4_0.viewComponent.closeview()

return var_0_0
