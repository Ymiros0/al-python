local var_0_0 = class("TechnologyTreeSetAttrMediator", import("..base.ContextMediator"))

function var_0_0.register(arg_1_0)
	return
end

function var_0_0.listNotificationInterests(arg_2_0)
	return {
		TechnologyConst.SET_TEC_ATTR_ADDITION_FINISH
	}
end

function var_0_0.handleNotification(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_1:getName()
	local var_3_1 = arg_3_1:getBody()

	if var_3_0 == TechnologyConst.SET_TEC_ATTR_ADDITION_FINISH then
		local var_3_2 = var_3_1.onSuccess

		if var_3_2 then
			var_3_2()
		end
	end
end

return var_0_0
