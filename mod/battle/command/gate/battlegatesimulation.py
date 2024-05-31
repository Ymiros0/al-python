local var_0_0 = class("BattleGateSimulation")

ys.Battle.BattleGateSimulation = var_0_0
var_0_0.__name = "BattleGateSimulation"

def var_0_0.Entrance(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_0.stageId
	local var_1_1 = pg.expedition_data_template[var_1_0].dungeon_id
	local var_1_2 = ys.Battle.BattleDataFunction.GetDungeonTmpDataByID(var_1_1).fleet_prefab
	local var_1_3 = {
		prefabFleet = var_1_2,
		stageId = var_1_0,
		system = SYSTEM_SIMULATION,
		exitCallback = arg_1_0.exitCallback,
		warnMsg = arg_1_0.warnMsg
	}

	arg_1_1.sendNotification(GAME.BEGIN_STAGE_DONE, var_1_3)

def var_0_0.Exit(arg_2_0, arg_2_1):
	arg_2_1.sendNotification(GAME.FINISH_STAGE_DONE, {
		system = SYSTEM_SIMULATION,
		exitCallback = arg_2_0.exitCallback
	})

return var_0_0
