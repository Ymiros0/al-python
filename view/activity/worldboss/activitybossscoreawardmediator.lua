﻿local var_0_0 = class("ActivityBossScoreAwardMediator", import("view.base.ContextMediator"))

function var_0_0.register(arg_1_0)
	return
end

function var_0_0.listNotificationInterests(arg_2_0)
	return {}
end

function var_0_0.handleNotification(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_1:getName()
	local var_3_1 = arg_3_1:getBody()

	if var_3_0 == nil then
		-- block empty
	end
end

function var_0_0.remove(arg_4_0)
	return
end

return var_0_0
