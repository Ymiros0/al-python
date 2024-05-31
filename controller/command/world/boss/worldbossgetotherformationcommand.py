local var_0_0 = class("WorldBossGetOtherFormationCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.bossId
	local var_1_2 = var_1_0.userId

	pg.ConnectionMgr.GetInstance().Send(34519, {
		boss_id = var_1_1,
		userId = var_1_2
	}, 34520, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = {}

			for iter_2_0, iter_2_1 in ipairs(arg_2_0.ship_list):
				local var_2_1 = MetaBossRankShip.New(iter_2_1)

				table.insert(var_2_0, var_2_1)

			arg_1_0.sendNotification(GAME.WORLD_BOSS_GET_FORMATION_DONE, {
				ships = var_2_0
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
