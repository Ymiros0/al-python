﻿local var_0_0 = class("TrackCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.system
	local var_1_2 = var_1_0.id
	local var_1_3 = var_1_0.desc

	pg.ConnectionMgr.GetInstance():Send(10993, {
		action_arg = 0,
		action_system = var_1_1,
		action_id = var_1_2,
		action_des = var_1_3
	})
end

return var_0_0
