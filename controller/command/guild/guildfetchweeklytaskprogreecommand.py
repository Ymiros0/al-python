local var_0_0 = class("GuildFetchWeeklyTaskProgreeCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(GuildProxy)
	local var_1_2 = var_1_1.getRawData()

	if not var_1_2:
		return

	local var_1_3 = var_1_2.getWeeklyTask()

	if not var_1_3 or var_1_3.getState() != GuildTask.STATE_ONGOING:
		return

	pg.ConnectionMgr.GetInstance().Send(62022, {
		type = 0
	}, 62023, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = var_1_1.getRawData()

			var_1_3 = var_2_0.getWeeklyTask()

			local var_2_1 = var_1_3.getState()

			var_1_3.updateProgress(arg_2_0.progress)
			var_1_1.updateGuild(var_2_0)
			var_2_0.setRefreshWeeklyTaskProgressTime()
			arg_1_0.sendNotification(GAME.GUILD_WEEKLY_TASK_PROGREE_UPDATE_DONE)

			if var_2_1 != var_1_3.getState():
				arg_1_0.sendNotification(GAME.GUILD_REFRESH_CAPITAL)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
