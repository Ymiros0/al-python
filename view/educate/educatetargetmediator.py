local var_0_0 = class("EducateTargetMediator", import(".base.EducateContextMediator"))

var_0_0.ON_TASK_SUBMIT = "EducateTargetMediator.ON_TASK_SUBMIT"
var_0_0.ON_GET_TARGET_AWARD = "EducateTargetMediator.ON_GET_TARGET_AWARD"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_TASK_SUBMIT, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.EDUCATE_SUBMIT_TASK, {
			id = arg_2_1.id,
			system = arg_2_1.GetSystemType()
		}))
	arg_1_0.bind(var_0_0.ON_GET_TARGET_AWARD, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.EDUCATE_GET_TARGET_AWARD))

def var_0_0.listNotificationInterests(arg_4_0):
	return {
		GAME.EDUCATE_SUBMIT_TASK_DONE,
		GAME.EDUCATE_GET_TARGET_AWARD_DONE
	}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

	if var_5_0 == GAME.EDUCATE_SUBMIT_TASK_DONE or var_5_0 == GAME.EDUCATE_GET_TARGET_AWARD_DONE:
		arg_5_0.viewComponent.emit(EducateBaseUI.EDUCATE_ON_AWARD, {
			items = var_5_1.awards
		})
		arg_5_0.viewComponent.updateView()

return var_0_0
