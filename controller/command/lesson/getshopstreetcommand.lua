local var_0_0 = class("GetShopStreetCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0 and var_1_0.callback

	pg.ConnectionMgr.GetInstance():Send(22101, {
		type = 0
	}, 22102, function(arg_2_0)
		arg_1_0:sendNotification(GAME.GET_SHOPSTREET_DONE)

		local var_2_0 = getProxy(ShopsProxy):getShopStreet()

		if var_1_1 then
			var_1_1(var_2_0)
		end
	end)
end

return var_0_0
