local var_0_0 = class("BattleGateSubmarine")

ys.Battle.BattleGateSubmarine = var_0_0
var_0_0.__name = "BattleGateSubmarine"

def var_0_0.Entrance(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_0.stageId
	local var_1_1 = pg.expedition_data_template[var_1_0].dungeon_id
	local var_1_2 = ys.Battle.BattleDataFunction.GetDungeonTmpDataByID(var_1_1).fleet_prefab
	local var_1_3 = {
		prefabFleet = var_1_2,
		stageId = var_1_0,
		system = SYSTEM_SUBMARINE_RUN
	}

	arg_1_1.sendNotification(GAME.BEGIN_STAGE_DONE, var_1_3)

def var_0_0.Exit(arg_2_0, arg_2_1):
	local var_2_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_SUBMARINE_RUN)

	arg_2_1.sendNotification(GAME.ACTIVITY_OPERATION, {
		cmd = 1,
		activity_id = var_2_0 and var_2_0.id,
		statistics = arg_2_0.statistics,
		arg1 = arg_2_0.statistics._battleScore,
		arg2 = arg_2_0.statistics.subRunResult.score
	})

return var_0_0
