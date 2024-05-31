local var_0_0 = class("BattleGateRoutine")

ys.Battle.BattleGateRoutine = var_0_0
var_0_0.__name = "BattleGateRoutine"

function var_0_0.Entrance(arg_1_0, arg_1_1)
	if not arg_1_1.LegalFleet(arg_1_0.mainFleetId) then
		return
	end

	if BeginStageCommand.DockOverload() then
		return
	end

	local var_1_0 = getProxy(PlayerProxy)
	local var_1_1 = getProxy(BayProxy)
	local var_1_2 = getProxy(FleetProxy)
	local var_1_3 = pg.battle_cost_template[SYSTEM_ROUTINE]
	local var_1_4 = var_1_3.oil_cost > 0
	local var_1_5 = {}
	local var_1_6 = 0
	local var_1_7 = 0
	local var_1_8 = 0
	local var_1_9 = 0
	local var_1_10 = var_1_2:getFleetById(arg_1_0.mainFleetId)
	local var_1_11 = var_1_1:getSortShipsByFleet(var_1_10)

	for iter_1_0, iter_1_1 in ipairs(var_1_11) do
		var_1_5[#var_1_5 + 1] = iter_1_1.id
	end

	local var_1_12 = var_1_10:getStartCost().oil
	local var_1_13 = var_1_10:GetCostSum().oil
	local var_1_14 = var_1_0:getData()

	if var_1_4 and var_1_13 > var_1_14.oil then
		pg.TipsMgr.GetInstance():ShowTips(i18n("stage_beginStage_error_noResource"))

		return
	end

	local var_1_15 = arg_1_0.mainFleetId
	local var_1_16 = arg_1_0.stageId
	local var_1_17 = pg.expedition_data_template[var_1_16].dungeon_id
	local var_1_18 = ys.Battle.BattleDataFunction.GetDungeonTmpDataByID(var_1_17).fleet_prefab

	arg_1_1.ShipVertify()

	local function var_1_19(arg_2_0)
		if var_1_4 then
			var_1_14:consume({
				gold = 0,
				oil = var_1_12
			})
		end

		if var_1_3.enter_energy_cost > 0 and not exFlag then
			local var_2_0 = pg.gameset.battle_consume_energy.key_value

			for iter_2_0, iter_2_1 in ipairs(var_1_11) do
				iter_2_1:cosumeEnergy(var_2_0)
				var_1_1:updateShip(iter_2_1)
			end
		end

		var_1_0:updatePlayer(var_1_14)

		local var_2_1 = {
			mainFleetId = var_1_15,
			prefabFleet = var_1_18,
			stageId = var_1_16,
			system = SYSTEM_ROUTINE,
			token = arg_2_0.key
		}

		arg_1_1:sendNotification(GAME.BEGIN_STAGE_DONE, var_2_1)
	end

	local function var_1_20(arg_3_0)
		arg_1_1:RequestFailStandardProcess(arg_3_0)
	end

	BeginStageCommand.SendRequest(SYSTEM_ROUTINE, var_1_5, {
		var_1_16
	}, var_1_19, var_1_20)
end

function var_0_0.Exit(arg_4_0, arg_4_1)
	local var_4_0 = pg.battle_cost_template[SYSTEM_ROUTINE]
	local var_4_1 = getProxy(FleetProxy)
	local var_4_2 = getProxy(BayProxy)
	local var_4_3 = arg_4_0.statistics._battleScore
	local var_4_4 = 0
	local var_4_5 = {}
	local var_4_6 = var_4_1:getFleetById(arg_4_0.mainFleetId)
	local var_4_7 = var_4_2:getSortShipsByFleet(var_4_6)
	local var_4_8 = var_4_6:getEndCost().oil
	local var_4_9 = arg_4_1.GeneralPackage(arg_4_0, var_4_7)

	local function var_4_10(arg_5_0)
		arg_4_1.addShipsExp(arg_5_0.ship_exp_list, arg_4_0.statistics, true)

		arg_4_0.statistics.mvpShipID = arg_5_0.mvp

		local var_5_0, var_5_1 = arg_4_1:GeneralLoot(arg_5_0)
		local var_5_2 = var_4_3 > ys.Battle.BattleConst.BattleScore.C

		arg_4_1.GeneralPlayerCosume(SYSTEM_ROUTINE, var_5_2, var_4_8, arg_5_0.player_exp, exFlag)

		local var_5_3 = getProxy(DailyLevelProxy)

		if var_5_2 then
			var_5_3.data[var_5_3.dailyLevelId] = (var_5_3.data[var_5_3.dailyLevelId] or 0) + 1
		end

		if var_4_3 == ys.Battle.BattleConst.BattleScore.S then
			var_5_3:AddQuickStage(arg_4_0.stageId)
		end

		local var_5_4 = {
			system = SYSTEM_ROUTINE,
			statistics = arg_4_0.statistics,
			score = var_4_3,
			drops = var_5_0,
			commanderExps = {},
			result = arg_5_0.result,
			extraDrops = var_5_1
		}

		arg_4_1:sendNotification(GAME.FINISH_STAGE_DONE, var_5_4)
	end

	arg_4_1:SendRequest(var_4_9, var_4_10)
end

return var_0_0
