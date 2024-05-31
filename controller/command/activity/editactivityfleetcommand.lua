local var_0_0 = class("EditActivityFleetCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.actID
	local var_1_2 = var_1_0.fleets
	local var_1_3 = {}

	for iter_1_0, iter_1_1 in pairs(var_1_2) do
		local var_1_4 = {}

		_.each(iter_1_1.vanguardShips, function(arg_2_0)
			var_1_4[#var_1_4 + 1] = arg_2_0
		end)
		_.each(iter_1_1.mainShips, function(arg_3_0)
			var_1_4[#var_1_4 + 1] = arg_3_0
		end)
		_.each(iter_1_1.subShips, function(arg_4_0)
			var_1_4[#var_1_4 + 1] = arg_4_0
		end)

		local var_1_5 = {}

		for iter_1_2, iter_1_3 in pairs(iter_1_1.commanderIds) do
			table.insert(var_1_5, {
				pos = iter_1_2,
				id = iter_1_3
			})
		end

		local var_1_6 = {
			id = iter_1_0,
			ship_list = var_1_4,
			commanders = var_1_5
		}

		table.insert(var_1_3, var_1_6)
	end

	pg.ConnectionMgr.GetInstance():Send(11204, {
		activity_id = var_1_1,
		group_list = var_1_3
	}, 11205, function(arg_5_0)
		if arg_5_0.result == 0 then
			-- block empty
		end
	end)
end

return var_0_0
