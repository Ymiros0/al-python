﻿local var_0_0 = class("BattleGateBossSingle")

ys.Battle.BattleGateBossSingle = var_0_0
var_0_0.__name = "BattleGateBossSingle"

function var_0_0.Entrance(arg_1_0, arg_1_1)
	if BeginStageCommand.DockOverload() then
		return
	end

	local var_1_0 = arg_1_0.actId
	local var_1_1 = getProxy(PlayerProxy)
	local var_1_2 = getProxy(FleetProxy)
	local var_1_3 = getProxy(BayProxy)
	local var_1_4 = pg.battle_cost_template[SYSTEM_BOSS_SINGLE]
	local var_1_5 = var_1_4.oil_cost > 0
	local var_1_6 = getProxy(ActivityProxy):getActivityById(var_1_0)
	local var_1_7 = arg_1_0.stageId
	local var_1_8 = arg_1_0.mainFleetId
	local var_1_9 = var_1_2:getActivityFleets()[var_1_0][var_1_8]
	local var_1_10 = {}
	local var_1_11 = var_1_3:getSortShipsByFleet(var_1_9)

	for iter_1_0, iter_1_1 in ipairs(var_1_11) do
		var_1_10[#var_1_10 + 1] = iter_1_1.id
	end

	local var_1_12 = var_1_6:GetEnemyDataByStageId(var_1_7)
	local var_1_13 = 0
	local var_1_14 = var_1_1:getRawData()
	local var_1_15 = var_1_9:GetCostSum().oil
	local var_1_16 = var_1_12:GetOilLimit()
	local var_1_17 = math.min(var_1_15, var_1_16[1])

	if var_1_5 and var_1_17 > var_1_14.oil then
		pg.TipsMgr.GetInstance():ShowTips(i18n("stage_beginStage_error_noResource"))

		return
	end

	arg_1_1.ShipVertify()

	local var_1_18 = var_1_9:getStartCost().oil

	local function var_1_19(arg_2_0)
		if var_1_5 then
			var_1_14:consume({
				gold = 0,
				oil = var_1_18
			})
		end

		if var_1_4.enter_energy_cost > 0 then
			local var_2_0 = pg.gameset.battle_consume_energy.key_value

			for iter_2_0, iter_2_1 in ipairs(var_1_11) do
				iter_2_1:cosumeEnergy(var_2_0)
				var_1_3:updateShip(iter_2_1)
			end
		end

		var_1_1:updatePlayer(var_1_14)

		local var_2_1 = {
			mainFleetId = var_1_8,
			prefabFleet = {},
			stageId = var_1_7,
			system = SYSTEM_BOSS_SINGLE,
			actId = var_1_0,
			token = arg_2_0.key,
			continuousBattleTimes = arg_1_0.continuousBattleTimes,
			totalBattleTimes = arg_1_0.totalBattleTimes
		}

		arg_1_1:sendNotification(GAME.BEGIN_STAGE_DONE, var_2_1)
	end

	local function var_1_20(arg_3_0)
		arg_1_1:RequestFailStandardProcess(arg_3_0)
	end

	BeginStageCommand.SendRequest(SYSTEM_BOSS_SINGLE, var_1_10, {
		var_1_7
	}, var_1_19, var_1_20)
end

function var_0_0.Exit(arg_4_0, arg_4_1)
	local var_4_0 = pg.battle_cost_template[SYSTEM_BOSS_SINGLE]
	local var_4_1 = getProxy(FleetProxy)
	local var_4_2 = getProxy(BayProxy)
	local var_4_3 = arg_4_0.statistics._battleScore
	local var_4_4 = getProxy(ActivityProxy):getActivityById(arg_4_0.actId):GetEnemyDataByStageId(arg_4_0.stageId):GetOilLimit()
	local var_4_5 = var_4_1:getActivityFleets()[arg_4_0.actId]
	local var_4_6 = var_4_5[arg_4_0.mainFleetId]
	local var_4_7
	local var_4_8 = 0
	local var_4_9 = {}
	local var_4_10 = {}
	local var_4_11 = var_4_0.oil_cost > 0

	local function var_4_12(arg_5_0, arg_5_1)
		if var_4_11 then
			local var_5_0 = arg_5_0:getEndCost().oil

			if arg_5_1 > 0 then
				local var_5_1 = arg_5_0:getStartCost().oil

				var_5_0 = math.clamp(arg_5_1 - var_5_1, 0, var_5_0)
			end

			var_4_8 = var_4_8 + var_5_0
		end

		table.insertto(var_4_9, var_4_2:getSortShipsByFleet(arg_5_0))
		table.insertto(var_4_10, arg_5_0.commanderIds)
	end

	var_4_12(var_4_6, var_4_4[1] or 0)

	if arg_4_0.statistics.submarineAid then
		var_4_7 = var_4_5[arg_4_0.mainFleetId + 10]

		if var_4_7 then
			var_4_12(var_4_7, var_4_4[2] or 0)
		else
			originalPrint("finish stage error: can not find submarin fleet.")
		end
	end

	local var_4_13 = arg_4_1.GeneralPackage(arg_4_0, var_4_9)

	var_4_13.commander_id_list = var_4_10

	local function var_4_14(arg_6_0)
		arg_4_1.addShipsExp(arg_6_0.ship_exp_list, arg_4_0.statistics, true)

		arg_4_0.statistics.mvpShipID = arg_6_0.mvp

		local var_6_0, var_6_1 = arg_4_1:GeneralLoot(arg_6_0)
		local var_6_2 = var_4_3 > ys.Battle.BattleConst.BattleScore.C
		local var_6_3 = arg_4_1.GenerateCommanderExp(arg_6_0, var_4_6, var_4_7)

		arg_4_1.GeneralPlayerCosume(SYSTEM_BOSS_SINGLE, var_6_2, var_4_8, arg_6_0.player_exp)

		if var_6_2 then
			local var_6_4 = getProxy(ActivityProxy):getActivityById(arg_4_0.actId)
			local var_6_5 = var_6_4:GetEnemyDataByStageId(arg_4_0.stageId)

			var_6_4:AddDailyCount(var_6_5.id)
			var_6_4:AddPassStage(var_6_5:GetExpeditionId())
			getProxy(ActivityProxy):updateActivity(var_6_4)
		end

		local var_6_6 = {
			system = SYSTEM_BOSS_SINGLE,
			statistics = arg_4_0.statistics,
			score = var_4_3,
			result = arg_6_0.result,
			drops = var_6_0,
			commanderExps = var_6_3,
			extraDrops = var_6_1
		}

		if PlayerConst.CanDropItem(var_6_0) then
			local var_6_7 = {}

			for iter_6_0, iter_6_1 in ipairs(var_6_0) do
				table.insert(var_6_7, iter_6_1)
			end

			for iter_6_2, iter_6_3 in ipairs(var_6_1) do
				iter_6_3.riraty = true

				table.insert(var_6_7, iter_6_3)
			end

			if getProxy(ContextProxy):getCurrentContext():getContextByMediator(BossSingleContinuousOperationMediator) then
				getProxy(ChapterProxy):AddBossSingleRewards(var_6_7)
			end
		end

		arg_4_1:sendNotification(GAME.FINISH_STAGE_DONE, var_6_6)
	end

	arg_4_1:SendRequest(var_4_13, var_4_14)
end

return var_0_0
