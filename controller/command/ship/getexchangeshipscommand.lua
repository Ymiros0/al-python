local var_0_0 = class("GetExchangeShipsCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody().time

	pg.ConnectionMgr.GetInstance():Send(16100, {
		time = var_1_0
	}, 16101, function(arg_2_0)
		local var_2_0 = getProxy(BuildShipProxy)
		local var_2_1 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.ship_id_list) do
			table.insert(var_2_1, {
				isFetched = false,
				id = iter_2_1
			})
		end

		for iter_2_2, iter_2_3 in ipairs(arg_2_0.fetched_index_list) do
			var_2_1[iter_2_3].isFetched = true
		end

		var_2_0:updateExchangeList(arg_2_0.flag_ship_flash_time, arg_2_0.flash_time, var_2_1)
		arg_1_0:sendNotification(GAME.GET_EXCHANGE_SHIPS_DONE)
	end)
end

return var_0_0
