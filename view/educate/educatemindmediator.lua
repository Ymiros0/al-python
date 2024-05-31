local var_0_0 = class("EducateMindMediator", import(".base.EducateContextMediator"))

var_0_0.ON_TASK_SUBMIT = "EducateMindMediator:ON_TASK_SUBMIT"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ON_TASK_SUBMIT, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.EDUCATE_SUBMIT_TASK, {
			id = arg_2_1.id,
			system = arg_2_1:GetSystemType()
		})
	end)
end

function var_0_0.listNotificationInterests(arg_3_0)
	return {
		GAME.EDUCATE_SUBMIT_TASK_DONE
	}
end

function var_0_0.handleNotification(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:getName()
	local var_4_1 = arg_4_1:getBody()

	if var_4_0 == GAME.EDUCATE_SUBMIT_TASK_DONE then
		arg_4_0.viewComponent:emit(EducateBaseUI.EDUCATE_ON_AWARD, {
			items = var_4_1.awards
		})
		arg_4_0.viewComponent:updateView()
	end
end

return var_0_0
