local var_0_0 = class("BattleGateCooperate")

ys.Battle.BattleGateCooperate = var_0_0
var_0_0.__name = "BattleGateCooperate"

function var_0_0.Entrance(arg_1_0, arg_1_1)
	if BeginStageCommand.DockOverload() then
		return
	end

	local var_1_0 = arg_1_0.actId
	local var_1_1 = getProxy(PlayerProxy)
	local var_1_2 = getProxy(BayProxy)
	local var_1_3 = getProxy(FleetProxy)
	local var_1_4 = pg.battle_cost_template[SYSTEM_HP_SHARE_ACT_BOSS]
	local var_1_5 = var_1_4.oil_cost > 0
	local var_1_6 = {}
	local var_1_7 = 0
	local var_1_8 = 0
	local var_1_9 = 0
	local var_1_10 = 0
	local var_1_11 = var_1_3:getActivityFleets()[var_1_0][Fleet.REGULAR_FLEET_ID]

	for iter_1_0, iter_1_1 in ipairs(var_1_11.ships) do
		var_1_6[#var_1_6 + 1] = iter_1_1
	end

	local var_1_12 = var_1_11:getStartCost().oil
	local var_1_13 = var_1_11:GetCostSum().oil
	local var_1_14 = var_1_2:getSortShipsByFleet(var_1_11)
	local var_1_15 = var_1_1:getData()

	if var_1_5 and var_1_13 > var_1_15.oil then
		pg.TipsMgr.GetInstance():ShowTips(i18n("stage_beginStage_error_noResource"))

		return
	end

	local var_1_16 = arg_1_0.stageId
	local var_1_17 = pg.expedition_data_template[var_1_16].dungeon_id
	local var_1_18 = ys.Battle.BattleDataFunction.GetDungeonTmpDataByID(var_1_17).fleet_prefab

	arg_1_1.ShipVertify()

	local var_1_19

	if chapter:getPlayType() == ChapterConst.TypeExtra then
		var_1_19 = true
	end

	local function var_1_20(arg_2_0)
		if var_1_5 then
			var_1_15:consume({
				gold = 0,
				oil = var_1_12
			})
		end

		if var_1_4.enter_energy_cost > 0 and not var_1_19 then
			local var_2_0 = pg.gameset.battle_consume_energy.key_value

			for iter_2_0, iter_2_1 in ipairs(var_1_14) do
				iter_2_1:cosumeEnergy(var_2_0)
				var_1_2:updateShip(iter_2_1)
			end
		end

		var_1_1:updatePlayer(var_1_15)

		local var_2_1 = Fleet.REGULAR_FLEET_ID
		local var_2_2 = {
			mainFleetId = var_2_1,
			prefabFleet = var_1_18,
			stageId = var_1_16,
			actId = var_1_0,
			system = SYSTEM_HP_SHARE_ACT_BOSS,
			token = arg_2_0.key
		}

		arg_1_1:sendNotification(GAME.BEGIN_STAGE_DONE, var_2_2)
	end

	local function var_1_21(arg_3_0)
		arg_1_1:RequestFailStandardProcess(arg_3_0)
	end

	BeginStageCommand.SendRequest(SYSTEM_HP_SHARE_ACT_BOSS, var_1_6, {
		var_1_16
	}, var_1_20, var_1_21)
end

function var_0_0.Exit(arg_4_0, arg_4_1)
	if client.CheaterVertify() then
		return
	end

	local var_4_0 = pg.battle_cost_template[SYSTEM_HP_SHARE_ACT_BOSS]
	local var_4_1 = getProxy(FleetProxy)
	local var_4_2 = getProxy(ChapterProxy)
	local var_4_3 = ys.Battle.BattleConst.BattleScore.S
	local var_4_4 = 0
	local var_4_5 = 0
	local var_4_6
	local var_4_7 = var_4_1:getActivityFleets()[arg_4_0.actId][arg_4_0.mainFleetId]
	local var_4_8 = bayProxy:getSortShipsByFleet(var_4_7)
	local var_4_9 = var_4_7:getEndCost().oil

	if arg_4_0.statistics.submarineAid then
		local var_4_10 = var_4_1:getActivityFleets()[arg_4_0.actId][Fleet.SUBMARINE_FLEET_ID]

		if var_4_10 then
			local var_4_11 = bayProxy:getSortShipsByFleet(var_4_10)

			for iter_4_0, iter_4_1 in ipairs(var_4_11) do
				if arg_4_0.statistics[iter_4_1.id] then
					table.insert(var_4_8, iter_4_1)

					var_4_9 = var_4_9 + iter_4_1:getEndBattleExpend()
				end
			end
		else
			originalPrint("finish stage error: can not find submarine fleet.")
		end
	end

	local var_4_12 = client.GeneralPackage(arg_4_0, var_4_8)
	local var_4_13 = {}

	for iter_4_2, iter_4_3 in ipairs(arg_4_0.statistics._enemyInfoList) do
		table.insert(var_4_13, {
			enemy_id = iter_4_3.id,
			damage_taken = iter_4_3.damage,
			total_hp = iter_4_3.totalHp
		})
	end

	var_4_12.enemy_info = var_4_13

	local function var_4_14(arg_5_0)
		client.addShipsExp(arg_5_0.ship_exp_list, arg_4_0.statistics)

		arg_4_0.statistics.mvpShipID = arg_5_0.mvp

		local var_5_0, var_5_1 = client:GeneralLoot(arg_5_0)
		local var_5_2 = var_4_3 > ys.Battle.BattleConst.BattleScore.C

		var_0_0.GeneralPlayerCosume(SYSTEM_HP_SHARE_ACT_BOSS, var_5_2, var_4_9, arg_5_0.player_exp)

		local var_5_3 = {
			system = SYSTEM_HP_SHARE_ACT_BOSS,
			statistics = arg_4_0.statistics,
			score = var_4_3,
			drops = var_5_0,
			commanderExps = {},
			result = arg_5_0.result,
			extraDrops = var_5_1
		}

		client:sendNotification(GAME.FINISH_STAGE_DONE, var_5_3)
	end

	client:SendRequest(var_4_12, var_4_14)
end

return var_0_0
