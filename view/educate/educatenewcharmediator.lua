local var_0_0 = class("EducateNewCharMediator", import(".base.EducateContextMediator"))

var_0_0.ON_SET_CALL = "EducateNewCharMediator:ON_SET_CALL"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ON_SET_CALL, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.EDUCATE_SET_CALL, {
			name = arg_2_1
		})
	end)
end

function var_0_0.listNotificationInterests(arg_3_0)
	return {
		GAME.EDUCATE_SET_CALL_DONE
	}
end

function var_0_0.handleNotification(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:getName()
	local var_4_1 = arg_4_1:getBody()

	if var_4_0 == GAME.EDUCATE_SET_CALL_DONE then
		arg_4_0.viewComponent:closeView()
	end
end

return var_0_0
