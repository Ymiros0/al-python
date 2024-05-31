local var_0_0 = class("BattleGateLimitChallenge")

ys.Battle.BattleGateLimitChallenge = var_0_0
var_0_0.__name = "BattleGateLimitChallenge"
var_0_0.BattleSystem = SYSTEM_LIMIT_CHALLENGE

def var_0_0.Entrance(arg_1_0, arg_1_1):
	local var_1_0 = FleetProxy.CHALLENGE_FLEET_ID

	if not arg_1_1.LegalFleet(var_1_0):
		return

	local var_1_1 = getProxy(PlayerProxy)
	local var_1_2 = var_1_1.getData()
	local var_1_3 = getProxy(FleetProxy)
	local var_1_4 = getProxy(BayProxy)
	local var_1_5 = getProxy(LimitChallengeProxy)
	local var_1_6 = arg_1_0.stageId
	local var_1_7 = pg.expedition_data_template[var_1_6].dungeon_id
	local var_1_8 = ys.Battle.BattleDataFunction.GetDungeonTmpDataByID(var_1_7).fleet_prefab
	local var_1_9 = var_1_3.getFleetById(FleetProxy.CHALLENGE_FLEET_ID)
	local var_1_10 = {}
	local var_1_11 = var_1_4.getSortShipsByFleet(var_1_9)

	for iter_1_0, iter_1_1 in ipairs(var_1_11):
		var_1_10[#var_1_10 + 1] = iter_1_1.id

	local var_1_12 = pg.battle_cost_template[var_0_0.BattleSystem]
	local var_1_13 = var_1_12.oil_cost > 0
	local var_1_14 = 0
	local var_1_15 = 0

	if var_1_13:
		var_1_14 = var_1_9.getStartCost().oil
		var_1_15 = var_1_9.GetCostSum().oil

	if var_1_13 and var_1_15 > var_1_2.oil:
		pg.TipsMgr.GetInstance().ShowTips(i18n("stage_beginStage_error_noResource"))

		return

	arg_1_1.ShipVertify()

	local function var_1_16(arg_2_0)
		if var_1_13:
			var_1_2.consume({
				gold = 0,
				oil = var_1_14
			})

		if var_1_12.enter_energy_cost > 0:
			local var_2_0 = pg.gameset.battle_consume_energy.key_value

			for iter_2_0, iter_2_1 in ipairs(var_1_11):
				iter_2_1.cosumeEnergy(var_2_0)
				var_1_4.updateShip(iter_2_1)

		var_1_1.updatePlayer(var_1_2)

		local var_2_1 = {
			mainFleetId = mainFleetID,
			prefabFleet = var_1_8,
			stageId = var_1_6,
			system = var_0_0.BattleSystem,
			token = arg_2_0.key
		}

		arg_1_1.sendNotification(GAME.BEGIN_STAGE_DONE, var_2_1)

	local function var_1_17(arg_3_0)
		arg_1_1.RequestFailStandardProcess(arg_3_0)

	BeginStageCommand.SendRequest(var_0_0.BattleSystem, var_1_10, {
		var_1_6
	}, var_1_16, var_1_17)

def var_0_0.Exit(arg_4_0, arg_4_1):
	local var_4_0 = pg.battle_cost_template[var_0_0.BattleSystem]
	local var_4_1 = getProxy(FleetProxy)
	local var_4_2 = getProxy(BayProxy)
	local var_4_3 = arg_4_0.statistics._battleScore
	local var_4_4 = 0
	local var_4_5 = {}
	local var_4_6 = {}
	local var_4_7 = arg_4_0.stageId
	local var_4_8 = var_4_1.getFleetById(FleetProxy.CHALLENGE_FLEET_ID)
	local var_4_9

	if arg_4_0.statistics.submarineAid:
		var_4_9 = var_4_1.getFleetById(FleetProxy.CHALLENGE_SUB_FLEET_ID)

	;(function()
		local function var_5_0(arg_6_0)
			local var_6_0 = arg_6_0.getEndCost().oil

			var_4_4 = var_4_4 + var_6_0

			table.insertto(var_4_6, _.values(arg_6_0.commanderIds))
			table.insertto(var_4_5, var_4_2.getSortShipsByFleet(arg_6_0))

		var_5_0(var_4_8)

		if arg_4_0.statistics.submarineAid:
			var_5_0(var_4_9))()

	local var_4_10 = arg_4_1.GeneralPackage(arg_4_0, var_4_5)

	var_4_10.commander_id_list = var_4_6

	local function var_4_11(arg_7_0)
		arg_4_1.addShipsExp(arg_7_0.ship_exp_list, arg_4_0.statistics, True)

		arg_4_0.statistics.mvpShipID = arg_7_0.mvp

		local var_7_0, var_7_1 = arg_4_1.GeneralLoot(arg_7_0)
		local var_7_2 = var_4_3 > ys.Battle.BattleConst.BattleScore.C
		local var_7_3 = arg_4_1.GenerateCommanderExp(arg_7_0, var_4_8, var_4_9)

		arg_4_1.GeneralPlayerCosume(var_0_0.BattleSystem, var_7_2, var_4_4, arg_7_0.player_exp)

		local var_7_4 = {
			system = var_0_0.BattleSystem,
			statistics = arg_4_0.statistics,
			score = var_4_3,
			drops = var_7_0,
			commanderExps = var_7_3,
			result = arg_7_0.result,
			extraDrops = var_7_1
		}

		arg_4_1.sendNotification(GAME.FINISH_STAGE_DONE, var_7_4)

		if var_7_2:
			local var_7_5 = LimitChallengeConst.GetChallengeIDByStageID(var_4_7)
			local var_7_6 = arg_4_0.statistics._totalTime

			getProxy(LimitChallengeProxy).setPassTime(var_7_5, var_7_6)

	arg_4_1.SendRequest(var_4_10, var_4_11)

return var_0_0
