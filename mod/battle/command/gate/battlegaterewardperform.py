local var_0_0 = class("BattleGateRewardPerform")

ys.Battle.BattleGateRewardPerform = var_0_0
var_0_0.__name = "BattleGateRewardPerform"

def var_0_0.Entrance(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_0.stageId
	local var_1_1 = pg.expedition_data_template[var_1_0].dungeon_id
	local var_1_2 = ys.Battle.BattleDataFunction.GetDungeonTmpDataByID(var_1_1).fleet_prefab
	local var_1_3 = {
		prefabFleet = var_1_2,
		stageId = var_1_0,
		system = SYSTEM_REWARD_PERFORM
	}

	arg_1_1.sendNotification(GAME.BEGIN_STAGE_DONE, var_1_3)

def var_0_0.Exit(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_0
	local var_2_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_EXPEDITION)
	local var_2_2 = var_2_1.data1_list
	local var_2_3

	for iter_2_0 = 1, #var_2_2:
		if bit.rshift(var_2_2[iter_2_0], 4) == var_2_0.stageId:
			var_2_3 = iter_2_0

			break

	arg_2_1.sendNotification(GAME.ACTIVITY_OPERATION, {
		cmd = 3,
		activity_id = var_2_1 and var_2_1.id,
		statistics = var_2_0.statistics,
		arg1 = var_2_0.statistics._battleScore,
		arg2 = var_2_3
	})

return var_0_0
