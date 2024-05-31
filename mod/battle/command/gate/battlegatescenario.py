local var_0_0 = class("BattleGateScenario")

ys.Battle.BattleGateScenario = var_0_0
var_0_0.__name = "BattleGateScenario"

def var_0_0.Entrance(arg_1_0, arg_1_1):
	if BeginStageCommand.DockOverload():
		getProxy(ChapterProxy).StopAutoFight(ChapterConst.AUTOFIGHT_STOP_REASON.DOCK_OVERLOADED)

		return

	local var_1_0 = getProxy(PlayerProxy)
	local var_1_1 = getProxy(BayProxy)
	local var_1_2 = pg.battle_cost_template[SYSTEM_SCENARIO]
	local var_1_3 = var_1_2.oil_cost > 0
	local var_1_4 = {}
	local var_1_5 = 0
	local var_1_6 = 0
	local var_1_7 = 0
	local var_1_8 = 0
	local var_1_9 = getProxy(ChapterProxy).getActiveChapter()
	local var_1_10 = var_1_9.fleet
	local var_1_11 = var_1_10.getShips(False)

	for iter_1_0, iter_1_1 in ipairs(var_1_11):
		var_1_4[#var_1_4 + 1] = iter_1_1.id

	local var_1_12, var_1_13 = var_1_9.getFleetCost(var_1_10, arg_1_0.stageId)
	local var_1_14 = var_1_12.gold
	local var_1_15 = var_1_12.oil
	local var_1_16 = var_1_12.gold + var_1_13.gold
	local var_1_17 = var_1_12.oil + var_1_13.oil
	local var_1_18 = var_1_0.getData()

	if var_1_3 and var_1_17 > var_1_18.oil:
		getProxy(ChapterProxy).StopAutoFight(ChapterConst.AUTOFIGHT_STOP_REASON.OIL_LACK)

		if not ItemTipPanel.ShowOilBuyTip(var_1_17):
			pg.TipsMgr.GetInstance().ShowTips(i18n("stage_beginStage_error_noResource"))

		return

	local var_1_19 = arg_1_0.stageId
	local var_1_20 = pg.expedition_data_template[var_1_19].dungeon_id
	local var_1_21 = ys.Battle.BattleDataFunction.GetDungeonTmpDataByID(var_1_20).fleet_prefab

	arg_1_1.ShipVertify()

	local var_1_22

	if var_1_9.getPlayType() == ChapterConst.TypeExtra:
		var_1_22 = True

	local var_1_23 = var_1_9.GetExtraCostRate()

	local function var_1_24(arg_2_0)
		if var_1_3:
			var_1_18.consume({
				gold = 0,
				oil = var_1_15
			})

		if var_1_2.enter_energy_cost > 0 and not var_1_22:
			local var_2_0 = pg.gameset.battle_consume_energy.key_value * var_1_23

			for iter_2_0, iter_2_1 in ipairs(var_1_4):
				local var_2_1 = var_1_1.getShipById(iter_2_1)

				if var_2_1:
					var_2_1.cosumeEnergy(var_2_0)
					var_1_1.updateShip(var_2_1)

		var_1_0.updatePlayer(var_1_18)

		local var_2_2 = {
			prefabFleet = var_1_21,
			stageId = var_1_19,
			system = SYSTEM_SCENARIO,
			token = arg_2_0.key,
			exitCallback = arg_2_0.exitCallback
		}

		arg_1_1.sendNotification(GAME.BEGIN_STAGE_DONE, var_2_2)

	local function var_1_25(arg_3_0)
		arg_1_1.RequestFailStandardProcess(arg_3_0)
		getProxy(ChapterProxy).StopAutoFight(ChapterConst.AUTOFIGHT_STOP_REASON.UNKNOWN)

	BeginStageCommand.SendRequest(SYSTEM_SCENARIO, var_1_4, {
		var_1_19
	}, var_1_24, var_1_25)

def var_0_0.Exit(arg_4_0, arg_4_1):
	if arg_4_1.CheaterVertify():
		return

	local var_4_0 = pg.battle_cost_template[SYSTEM_SCENARIO]
	local var_4_1 = getProxy(FleetProxy)
	local var_4_2 = getProxy(ChapterProxy)
	local var_4_3 = arg_4_0.statistics._battleScore
	local var_4_4 = 0
	local var_4_5 = 0
	local var_4_6 = {}
	local var_4_7 = var_4_2.getActiveChapter()
	local var_4_8 = var_4_7.fleet
	local var_4_9 = var_4_8.getShips(True)

	for iter_4_0, iter_4_1 in ipairs(var_4_9):
		table.insert(var_4_6, iter_4_1)

	local var_4_10 = arg_4_0.stageId
	local var_4_11, var_4_12 = var_4_7.getFleetCost(var_4_8, var_4_10)
	local var_4_13 = var_4_12.gold
	local var_4_14 = var_4_12.oil
	local var_4_15 = var_4_7.GetExtraCostRate()

	if arg_4_0.statistics.submarineAid:
		local var_4_16 = var_4_7.GetSubmarineFleet()

		if var_4_16:
			local var_4_17 = 0

			for iter_4_2, iter_4_3 in ipairs(var_4_16.getShipsByTeam(TeamType.Submarine, True)):
				if arg_4_0.statistics[iter_4_3.id]:
					table.insert(var_4_6, iter_4_3)

					var_4_17 = var_4_17 + iter_4_3.getEndBattleExpend()

			var_4_14 = var_4_14 + math.min(var_4_17, var_4_7.GetLimitOilCost(True)) * var_4_15
		else
			originalPrint("finish stage error. can not find submarine fleet.")

	local var_4_18 = var_4_3 > ys.Battle.BattleConst.BattleScore.C

	var_4_7.writeBack(var_4_18, arg_4_0)
	var_4_2.updateChapter(var_4_7)

	local var_4_19 = arg_4_1.GeneralPackage(arg_4_0, var_4_6)

	local function var_4_20(arg_5_0)
		local var_5_0 = var_4_7.getPlayType() == ChapterConst.TypeExtra

		arg_4_1.addShipsExp(arg_5_0.ship_exp_list, arg_4_0.statistics, True)

		local var_5_1 = arg_4_1.GenerateCommanderExp(arg_5_0, var_4_2.getActiveChapter().fleet, var_4_7.GetSubmarineFleet())

		arg_4_0.statistics.mvpShipID = arg_5_0.mvp

		local var_5_2, var_5_3 = arg_4_1.GeneralLoot(arg_5_0)

		arg_4_1.GeneralPlayerCosume(SYSTEM_SCENARIO, var_4_18, var_4_14, arg_5_0.player_exp, var_5_0)

		local var_5_4 = {
			system = SYSTEM_SCENARIO,
			statistics = arg_4_0.statistics,
			score = var_4_3,
			drops = var_5_2,
			commanderExps = var_5_1,
			result = arg_5_0.result,
			extraDrops = var_5_3,
			exitCallback = arg_4_0.exitCallback
		}

		var_4_2.updateActiveChapterShips()

		local var_5_5 = var_4_2.getActiveChapter()

		var_5_5.writeDrops(var_5_2)
		var_4_2.updateChapter(var_5_5)

		if PlayerConst.CanDropItem(var_5_2):
			local var_5_6 = {}

			for iter_5_0, iter_5_1 in ipairs(var_5_2):
				table.insert(var_5_6, iter_5_1)

			for iter_5_2, iter_5_3 in ipairs(var_5_3):
				iter_5_3.riraty = True

				table.insert(var_5_6, iter_5_3)

			local var_5_7 = getProxy(ChapterProxy).getActiveChapter(True)

			if var_5_7:
				if var_5_7.isLoop():
					getProxy(ChapterProxy).AddExtendChapterDataArray(var_5_7.id, "TotalDrops", var_5_6)

				var_5_7.writeDrops(var_5_6)

		local var_5_8 = var_4_2.getLastUnlockMap().id
		local var_5_9 = var_4_2.getLastUnlockMap().id

		if Map.lastMap and var_5_9 != var_5_8 and var_5_8 < var_5_9:
			Map.autoNextPage = True

		arg_4_1.sendNotification(GAME.CHAPTER_BATTLE_RESULT_REQUEST, {
			def callback:()
				arg_4_1.sendNotification(GAME.FINISH_STAGE_DONE, var_5_4)
		})

	arg_4_1.SendRequest(var_4_19, var_4_20)

return var_0_0
