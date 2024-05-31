﻿local var_0_0 = class("UpdateExerciseFleetCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.fleet
	local var_1_2 = var_1_1.vanguardShips
	local var_1_3 = var_1_1.mainShips
	local var_1_4 = var_1_0.callback
	local var_1_5 = getProxy(MilitaryExerciseProxy):getExerciseFleet()
	local var_1_6 = Clone(var_1_5)
	local var_1_7 = getProxy(FleetProxy):getFleetById(1)

	if table.getCount(var_1_3) == 0 or table.getCount(var_1_2) == 0 then
		var_1_2 = var_1_7.vanguardShips
		var_1_3 = var_1_7.mainShips
		arg_1_0.resetFleet = true
	end

	if table.getCount(var_1_2) > 3 or table.getCount(var_1_3) > 3 then
		return
	end

	pg.ConnectionMgr.GetInstance():Send(18008, {
		vanguard_ship_id_list = var_1_2,
		main_ship_id_list = var_1_3
	}, 18009, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = getProxy(MilitaryExerciseProxy)
			local var_2_1 = {}

			_.each(var_1_2, function(arg_3_0)
				table.insert(var_2_1, arg_3_0)
			end)
			_.each(var_1_3, function(arg_4_0)
				table.insert(var_2_1, arg_4_0)
			end)
			var_1_5:updateShips(var_2_1)
			var_2_0:updateExerciseFleet(var_1_5)

			if arg_1_0.resetFleet then
				arg_1_0.resetFleet = nil

				arg_1_0:sendNotification(GAME.EXERCISE_FLEET_RESET, var_1_5)
			end

			arg_1_0:sendNotification(GAME.UPDATE_EXERCISE_FLEET_DONE, {
				oldFleet = var_1_6,
				newFleet = var_1_5
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end

		if var_1_4 then
			var_1_4()
		end
	end)
end

return var_0_0
