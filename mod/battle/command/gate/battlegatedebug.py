local var_0_0 = class("BattleGateDebug")

ys.Battle.BattleGateDebug = var_0_0
var_0_0.__name = "BattleGateDebug"

def var_0_0.Entrance(arg_1_0, arg_1_1):
	local var_1_0 = getProxy(FleetProxy).getFleetById(1)

	if var_1_0 == None or var_1_0.isEmpty():
		pg.TipsMgr.GetInstance().ShowTips(i18n("stage_beginStage_error_fleetEmpty"))

		return

	local var_1_1 = PROLOGUE_DUNGEON
	local var_1_2 = {
		mainFleetId = 1,
		prefabFleet = {},
		stageId = var_1_1,
		system = SYSTEM_DEBUG
	}

	arg_1_1.sendNotification(GAME.BEGIN_STAGE_DONE, var_1_2)

def var_0_0.Exit():
	return

return var_0_0
