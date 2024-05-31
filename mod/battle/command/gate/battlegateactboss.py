local var_0_0 = class("BattleGateActBoss")

ys.Battle.BattleGateActBoss = var_0_0
var_0_0.__name = "BattleGateActBoss"

def var_0_0.Entrance(arg_1_0, arg_1_1):
	if BeginStageCommand.DockOverload():
		return

	local var_1_0 = arg_1_0.continuousBattleTimes
	local var_1_1 = arg_1_0.totalBattleTimes
	local var_1_2 = arg_1_0.actId
	local var_1_3 = getProxy(ActivityProxy).getActivityById(var_1_2)
	local var_1_4 = var_1_3.getConfig("config_id")
	local var_1_5 = pg.activity_event_worldboss[var_1_4]
	local var_1_6 = getProxy(PlayerProxy)
	local var_1_7 = getProxy(BayProxy)
	local var_1_8 = getProxy(FleetProxy)
	local var_1_9 = pg.battle_cost_template[SYSTEM_ACT_BOSS]
	local var_1_10 = var_1_9.oil_cost > 0
	local var_1_11 = {}
	local var_1_12 = 0
	local var_1_13 = 0
	local var_1_14 = 0
	local var_1_15 = 0
	local var_1_16 = arg_1_0.stageId
	local var_1_17 = arg_1_0.mainFleetId
	local var_1_18 = var_1_8.getActivityFleets()[var_1_2][var_1_17]
	local var_1_19 = var_1_7.getSortShipsByFleet(var_1_18)

	for iter_1_0, iter_1_1 in ipairs(var_1_19):
		var_1_11[#var_1_11 + 1] = iter_1_1.id

	local var_1_20 = var_1_18.getStartCost().oil
	local var_1_21 = var_1_18.GetCostSum().oil
	local var_1_22 = var_1_5.use_oil_limit[var_1_17]

	if var_1_3.IsOilLimit(var_1_16) and var_1_22[1] > 0:
		var_1_21 = math.min(var_1_21, var_1_22[1])

	local var_1_23 = var_1_6.getData()

	if var_1_10 and var_1_21 > var_1_23.oil:
		pg.TipsMgr.GetInstance().ShowTips(i18n("stage_beginStage_error_noResource"))

		return

	local var_1_24 = pg.expedition_data_template[var_1_16].dungeon_id
	local var_1_25 = ys.Battle.BattleDataFunction.GetDungeonTmpDataByID(var_1_24).fleet_prefab

	arg_1_1.ShipVertify()

	local function var_1_26(arg_2_0)
		if var_1_10:
			var_1_23.consume({
				gold = 0,
				oil = var_1_20
			})

		if var_1_9.enter_energy_cost > 0:
			local var_2_0 = pg.gameset.battle_consume_energy.key_value

			for iter_2_0, iter_2_1 in ipairs(var_1_19):
				iter_2_1.cosumeEnergy(var_2_0)
				var_1_7.updateShip(iter_2_1)

		var_1_6.updatePlayer(var_1_23)

		local var_2_1 = {
			mainFleetId = var_1_17,
			actId = var_1_2,
			prefabFleet = var_1_25,
			stageId = var_1_16,
			system = SYSTEM_ACT_BOSS,
			token = arg_2_0.key,
			continuousBattleTimes = var_1_0,
			totalBattleTimes = var_1_1
		}

		arg_1_1.sendNotification(GAME.BEGIN_STAGE_DONE, var_2_1)

	local function var_1_27(arg_3_0)
		arg_1_1.RequestFailStandardProcess(arg_3_0)

	BeginStageCommand.SendRequest(SYSTEM_ACT_BOSS, var_1_11, {
		var_1_16
	}, var_1_26, var_1_27)

def var_0_0.Exit(arg_4_0, arg_4_1):
	local var_4_0 = pg.battle_cost_template[SYSTEM_ACT_BOSS]
	local var_4_1 = getProxy(FleetProxy)
	local var_4_2 = getProxy(BayProxy)
	local var_4_3 = arg_4_0.statistics._battleScore
	local var_4_4 = getProxy(ActivityProxy).getActivityById(arg_4_0.actId)
	local var_4_5 = var_4_4.getConfig("config_id")
	local var_4_6 = pg.activity_event_worldboss[var_4_5].use_oil_limit[arg_4_0.mainFleetId]
	local var_4_7 = var_4_4.IsOilLimit(arg_4_0.stageId)
	local var_4_8 = var_4_1.getActivityFleets()[arg_4_0.actId]
	local var_4_9 = var_4_8[arg_4_0.mainFleetId]
	local var_4_10
	local var_4_11 = 0
	local var_4_12 = {}
	local var_4_13 = {}
	local var_4_14 = var_4_0.oil_cost > 0

	local function var_4_15(arg_5_0, arg_5_1)
		if var_4_14:
			local var_5_0 = arg_5_0.getEndCost().oil

			if arg_5_1 > 0:
				local var_5_1 = arg_5_0.getStartCost().oil

				var_5_0 = math.clamp(arg_5_1 - var_5_1, 0, var_5_0)

			var_4_11 = var_4_11 + var_5_0

		table.insertto(var_4_12, var_4_2.getSortShipsByFleet(arg_5_0))
		table.insertto(var_4_13, arg_5_0.commanderIds)

	var_4_15(var_4_9, var_4_7 and var_4_6[1] or 0)

	if arg_4_0.statistics.submarineAid:
		var_4_10 = var_4_8[arg_4_0.mainFleetId + 10]

		if var_4_10:
			var_4_15(var_4_10, var_4_7 and var_4_6[2] or 0)
		else
			originalPrint("finish stage error. can not find submarin fleet.")

	local var_4_16 = arg_4_1.GeneralPackage(arg_4_0, var_4_12)

	var_4_16.commander_id_list = var_4_13

	local function var_4_17(arg_6_0)
		arg_4_1.addShipsExp(arg_6_0.ship_exp_list, arg_4_0.statistics, True)

		arg_4_0.statistics.mvpShipID = arg_6_0.mvp

		local var_6_0, var_6_1 = arg_4_1.GeneralLoot(arg_6_0)
		local var_6_2 = var_4_3 > ys.Battle.BattleConst.BattleScore.C
		local var_6_3 = arg_4_1.GenerateCommanderExp(arg_6_0, var_4_9, var_4_10)

		arg_4_1.GeneralPlayerCosume(SYSTEM_ACT_BOSS, var_6_2, var_4_11, arg_6_0.player_exp)

		local var_6_4

		if var_6_2:
			var_6_4 = (function()
				local var_7_0 = getProxy(ActivityProxy).getActivityById(arg_4_0.actId)
				local var_7_1 = arg_4_0.stageId

				return var_7_0.data1KeyValueList[1][var_7_1] == 1 and var_7_0.data1KeyValueList[2][var_7_1] <= 0)()

			arg_4_1.sendNotification(GAME.ACT_BOSS_NORMAL_UPDATE, {
				stageId = arg_4_0.stageId
			})

		local var_6_5 = {
			system = SYSTEM_ACT_BOSS,
			statistics = arg_4_0.statistics,
			score = var_4_3,
			drops = var_6_0,
			commanderExps = var_6_3,
			result = arg_6_0.result,
			extraDrops = var_6_1,
			isLastBonus = var_6_4
		}

		if PlayerConst.CanDropItem(var_6_0):
			local var_6_6 = {}

			for iter_6_0, iter_6_1 in ipairs(var_6_0):
				table.insert(var_6_6, iter_6_1)

			for iter_6_2, iter_6_3 in ipairs(var_6_1):
				iter_6_3.riraty = True

				table.insert(var_6_6, iter_6_3)

			if getProxy(ContextProxy).getCurrentContext().getContextByMediator(ContinuousOperationMediator):
				getProxy(ChapterProxy).AddActBossRewards(var_6_6)

		arg_4_1.sendNotification(GAME.FINISH_STAGE_DONE, var_6_5)

	arg_4_1.SendRequest(var_4_16, var_4_17)

return var_0_0
