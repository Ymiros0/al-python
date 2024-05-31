local var_0_0 = class("BattleGateChallenge")

ys.Battle.BattleGateChallenge = var_0_0
var_0_0.__name = "BattleGateChallenge"

def var_0_0.Entrance(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_0.mode
	local var_1_1 = arg_1_0.actId
	local var_1_2 = getProxy(PlayerProxy)
	local var_1_3 = getProxy(BayProxy)
	local var_1_4 = getProxy(ChallengeProxy)
	local var_1_5 = pg.battle_cost_template[SYSTEM_CHALLENGE]
	local var_1_6 = var_1_5.oil_cost > 0
	local var_1_7 = {}
	local var_1_8 = 0
	local var_1_9 = 0
	local var_1_10 = 0
	local var_1_11 = 0
	local var_1_12 = var_1_4.getUserChallengeInfo(var_1_0)
	local var_1_13 = var_1_12.getRegularFleet().getShips(False)

	for iter_1_0, iter_1_1 in ipairs(var_1_13):
		var_1_7[#var_1_7 + 1] = iter_1_1.id

	local var_1_14 = var_1_2.getData()

	if var_1_6 and var_1_11 > var_1_14.oil:
		pg.TipsMgr.GetInstance().ShowTips(i18n("stage_beginStage_error_noResource"))

		return

	local var_1_15 = var_1_12.getLevel()
	local var_1_16 = var_1_12.getNextStageID()
	local var_1_17 = {
		var_1_15,
		var_1_0
	}

	arg_1_1.ShipVertify()

	local function var_1_18(arg_2_0)
		if var_1_6:
			var_1_14.consume({
				gold = 0,
				oil = var_1_9
			})

		if var_1_5.enter_energy_cost > 0:
			local var_2_0 = pg.gameset.battle_consume_energy.key_value

			for iter_2_0, iter_2_1 in ipairs(var_1_13):
				iter_2_1.cosumeEnergy(var_2_0)
				var_1_3.updateShip(iter_2_1)

		var_1_2.updatePlayer(var_1_14)

		local var_2_1 = {
			prefabFleet = {},
			stageId = var_1_16,
			system = SYSTEM_CHALLENGE,
			actId = var_1_1,
			token = arg_2_0.key,
			mode = var_1_0
		}

		arg_1_1.sendNotification(GAME.BEGIN_STAGE_DONE, var_2_1)

	local function var_1_19(arg_3_0)
		arg_1_1.RequestFailStandardProcess(arg_3_0)

	BeginStageCommand.SendRequest(SYSTEM_CHALLENGE, var_1_7, {
		var_1_16,
		var_1_17
	}, var_1_18, var_1_19)

def var_0_0.Exit(arg_4_0, arg_4_1):
	local var_4_0 = pg.battle_cost_template[SYSTEM_CHALLENGE]
	local var_4_1 = getProxy(FleetProxy)
	local var_4_2 = getProxy(ChallengeProxy)
	local var_4_3 = arg_4_0.statistics._battleScore
	local var_4_4 = 0
	local var_4_5 = {}
	local var_4_6 = {}
	local var_4_7 = arg_4_0.mode
	local var_4_8 = var_4_2.getUserChallengeInfo(var_4_7)
	local var_4_9 = var_4_8.getRegularFleet().getShips(True)

	for iter_4_0, iter_4_1 in ipairs(var_4_9):
		table.insert(var_4_6, iter_4_1)

	local var_4_10 = {
		var_4_8.getLevel(),
		var_4_7
	}
	local var_4_11 = 0
	local var_4_12 = arg_4_1.GeneralPackage(arg_4_0, var_4_6)

	var_4_12.data2 = var_4_10

	local function var_4_13(arg_5_0)
		arg_4_1.addShipsExp(arg_5_0.ship_exp_list, arg_4_0.statistics)

		arg_4_0.statistics.mvpShipID = arg_5_0.mvp

		local var_5_0, var_5_1 = arg_4_1.GeneralLoot(arg_5_0)
		local var_5_2 = var_4_3 > ys.Battle.BattleConst.BattleScore.C

		arg_4_1.GeneralPlayerCosume(SYSTEM_CHALLENGE, var_5_2, var_4_11, arg_5_0.player_exp, exFlag)

		local var_5_3 = {
			system = SYSTEM_CHALLENGE,
			statistics = arg_4_0.statistics,
			score = var_4_3,
			drops = var_5_0,
			commanderExps = {},
			result = arg_5_0.result,
			extraDrops = var_5_1
		}

		arg_4_1.sendNotification(GAME.FINISH_STAGE_DONE, var_5_3)

		local var_5_4 = var_4_8.getShipUIDList()

		local function var_5_5(arg_6_0)
			local var_6_0 = arg_4_0.statistics[arg_6_0]

			if var_6_0:
				var_4_8.updateShipHP(arg_6_0, var_6_0.bp)

		for iter_5_0, iter_5_1 in pairs(var_5_4):
			var_5_5(iter_5_1)

	arg_4_1.SendRequest(var_4_12, var_4_13)

return var_0_0
