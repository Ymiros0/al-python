﻿local var_0_0 = class("CancelCommonFlagCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody().flagID

	pg.ConnectionMgr.GetInstance():Send(11021, {
		flag_id = var_1_0
	}, 11022, function(arg_2_0)
		local var_2_0 = getProxy(PlayerProxy)

		if var_2_0 then
			local var_2_1 = var_2_0:getData()

			var_2_1:CancelCommonFlag(var_1_0)
			var_2_0:updatePlayer(var_2_1)
		end
	end)
end

return var_0_0
