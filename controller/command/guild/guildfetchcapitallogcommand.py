local var_0_0 = class("GuildFetchCapitalLogCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(GuildProxy)

	if not var_1_1.getData():
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_no_exist"))

		return

	pg.ConnectionMgr.GetInstance().Send(62011, {
		type = 0
	}, 62012, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = var_1_1.getData()
			local var_2_1 = {}

			for iter_2_0, iter_2_1 in ipairs(arg_2_0.inclog):
				local var_2_2 = GuildCapitalLog.New(iter_2_1)

				table.insert(var_2_1, var_2_2)

			for iter_2_2, iter_2_3 in ipairs(arg_2_0.declog):
				local var_2_3 = GuildCapitalLog.New(iter_2_3)

				table.insert(var_2_1, var_2_3)

			for iter_2_4, iter_2_5 in ipairs(arg_2_0.otherlog):
				local var_2_4 = GuildCapitalLog.New(iter_2_5)

				table.insert(var_2_1, var_2_4)

			if #var_2_1 > 0:
				var_2_0.updateCapitalLogs(var_2_1)
				var_1_1.updateGuild(var_2_0)

			arg_1_0.sendNotification(GAME.GUILD_FETCH_CAPITAL_LOG_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
