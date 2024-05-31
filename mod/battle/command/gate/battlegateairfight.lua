local var_0_0 = class("BattleGateAirFight")

ys.Battle.BattleGateAirFight = var_0_0
var_0_0.__name = "BattleGateAirFight"

function var_0_0.Entrance(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_0.stageId
	local var_1_1 = pg.expedition_data_template[var_1_0].dungeon_id
	local var_1_2 = ys.Battle.BattleDataFunction.GetDungeonTmpDataByID(var_1_1).fleet_prefab
	local var_1_3 = {
		prefabFleet = var_1_2,
		stageId = var_1_0,
		system = SYSTEM_AIRFIGHT
	}

	arg_1_1:sendNotification(GAME.BEGIN_STAGE_DONE, var_1_3)
end

function var_0_0.Exit(arg_2_0, arg_2_1)
	local var_2_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_AIRFIGHT_BATTLE)

	if arg_2_0.statistics._battleScore >= ys.Battle.BattleConst.BattleScore.B and var_2_0 and not var_2_0:isEnd() then
		local var_2_1 = 0
		local var_2_2 = var_2_0:getConfig("config_client")[1]

		for iter_2_0 = 1, var_2_2 do
			var_2_1 = var_2_1 + (var_2_0:getKVPList(1, iter_2_0) or 0)
		end

		local var_2_3 = pg.TimeMgr.GetInstance()
		local var_2_4 = var_2_3:DiffDay(var_2_0.data1, var_2_3:GetServerTime()) + 1

		if var_2_1 < math.min(var_2_4 * 2, var_2_2 * 3) then
			local var_2_5 = arg_2_0.stageId
			local var_2_6 = var_2_0:getConfig("config_client")[2]
			local var_2_7 = table.indexof(var_2_6, var_2_5)
			local var_2_8 = math.floor((var_2_7 - 1) / (#var_2_6 / var_2_2)) + 1
			local var_2_9 = var_2_0:getKVPList(1, var_2_8) or 0
			local var_2_10 = var_2_0:getKVPList(2, var_2_8) == 1

			if var_2_9 < 3 and not var_2_10 then
				arg_2_1:sendNotification(GAME.ACTIVITY_OPERATION, {
					cmd = 1,
					activity_id = var_2_0 and var_2_0.id,
					arg1 = var_2_8,
					statistics = arg_2_0.statistics
				})

				return
			end
		end
	end

	arg_2_1:sendNotification(GAME.FINISH_STAGE_DONE, {
		statistics = arg_2_0.statistics,
		score = arg_2_0.statistics._battleScore,
		system = SYSTEM_AIRFIGHT
	})
end

return var_0_0
