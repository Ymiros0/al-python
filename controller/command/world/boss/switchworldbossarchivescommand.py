local var_0_0 = class("SwitchWorldBossArchivesCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().id

	pg.ConnectionMgr.GetInstance().Send(34527, {
		boss_id = var_1_0
	}, 34528, function(arg_2_0)
		if arg_2_0.result == 0:
			nowWorld().GetBossProxy().SetArchivesId(var_1_0)
			arg_1_0.sendNotification(GAME.SWITCH_WORLD_BOSS_ARCHIVES_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
