local var_0_0 = class("GuildSelectWeeklyTaskCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.taskId
	local var_1_2 = var_1_0.num
	local var_1_3 = getProxy(GuildProxy).getRawData()

	if not var_1_3:
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_no_exist"))

		return

	if var_1_3.getWeeklyTask().getState() != GuildTask.STATE_EMPTY:
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_week_task_state_is_wrong"))

		return

	if not GuildMember.IsAdministrator(var_1_3.getSelfDuty()):
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_commander_and_sub_op"))

		return

	pg.ConnectionMgr.GetInstance().Send(62013, {
		id = var_1_1
	}, 62014, function(arg_2_0)
		if arg_2_0.result == 0:
			arg_1_0.sendNotification(GAME.GUILD_SELECT_TASK_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
