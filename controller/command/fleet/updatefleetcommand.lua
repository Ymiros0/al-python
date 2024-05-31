﻿local var_0_0 = class("UpdateFleetCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.fleet
	local var_1_2 = var_1_0.callback

	assert(isa(var_1_1, Fleet), "should be an instance of Fleet")

	local var_1_3 = getProxy(PlayerProxy)
	local var_1_4 = getProxy(FleetProxy)
	local var_1_5 = var_1_4:getFleetById(var_1_1.id)

	if var_1_5 == nil then
		return
	end

	local var_1_6 = {}

	_.each(var_1_1.vanguardShips, function(arg_2_0)
		var_1_6[#var_1_6 + 1] = arg_2_0
	end)
	_.each(var_1_1.mainShips, function(arg_3_0)
		var_1_6[#var_1_6 + 1] = arg_3_0
	end)
	_.each(var_1_1.subShips, function(arg_4_0)
		var_1_6[#var_1_6 + 1] = arg_4_0
	end)
	pg.ConnectionMgr.GetInstance():Send(12102, {
		id = var_1_1.id,
		ship_list = var_1_6
	}, 12103, function(arg_5_0)
		if arg_5_0.result == 0 then
			var_1_1.name = var_1_5.name

			var_1_4:updateFleet(var_1_1)

			if var_1_1:isEmpty() and var_1_3.combatFleetId == var_1_1.id then
				var_1_3.combatFleetId = 1
			end

			arg_1_0:sendNotification(GAME.UPDATE_FLEET_DONE, var_1_1.id)
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("fleet_updateFleet", arg_5_0.result))
		end

		if var_1_2 ~= nil then
			var_1_2()
		end
	end)
end

return var_0_0
