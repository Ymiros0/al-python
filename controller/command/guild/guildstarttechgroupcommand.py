local var_0_0 = class("GuildStartTechGroupCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().id
	local var_1_1 = getProxy(GuildProxy).getData()

	if not var_1_1:
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_no_exist"))

		return

	if not var_1_1.CanCancelTech():
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_cancel_only_once_pre_day"))

		return

	local var_1_2 = var_1_1.getTechnologyGroupById(var_1_0)

	if not var_1_2:
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_not_exist_tech"))

		return

	if var_1_2.isMaxLevel():
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_tech_is_max_level"))

		return

	pg.ConnectionMgr.GetInstance().Send(62020, {
		id = var_1_2.pid
	}, 62021, function(arg_2_0)
		if arg_2_0.result == 0:
			arg_1_0.sendNotification(GAME.GUILD_START_TECH_TASK_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
