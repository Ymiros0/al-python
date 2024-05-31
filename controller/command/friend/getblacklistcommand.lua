﻿local var_0_0 = class("GetBlackListCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()

	pg.ConnectionMgr.GetInstance():Send(50016, {
		type = 0
	}, 50017, function(arg_2_0)
		local var_2_0 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.black_list) do
			local var_2_1 = Player.New(iter_2_1)

			var_2_0[var_2_1.id] = var_2_1
		end

		getProxy(FriendProxy):setBlackList(var_2_0)
		arg_1_0:sendNotification(GAME.GET_BLACK_LIST_DONE)
	end)
end

return var_0_0
