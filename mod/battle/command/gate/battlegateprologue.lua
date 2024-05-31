local var_0_0 = class("BattleGatePrologue")

ys.Battle.BattleGatePrologue = var_0_0
var_0_0.__name = "BattleGatePrologue"

function var_0_0.Entrance(arg_1_0, arg_1_1)
	local var_1_0 = PROLOGUE_DUNGEON
	local var_1_1 = pg.expedition_data_template[var_1_0].dungeon_id
	local var_1_2 = ys.Battle.BattleDataFunction.GetDungeonTmpDataByID(var_1_1).fleet_prefab
	local var_1_3 = {
		prefabFleet = var_1_2,
		stageId = var_1_0,
		system = SYSTEM_PROLOGUE
	}

	arg_1_1:sendNotification(GAME.BEGIN_STAGE_DONE, var_1_3)
end

function var_0_0.Exit(arg_2_0, arg_2_1)
	arg_2_1:sendNotification(GAME.FINISH_STAGE_DONE, {
		system = SYSTEM_PROLOGUE
	})
end

return var_0_0
