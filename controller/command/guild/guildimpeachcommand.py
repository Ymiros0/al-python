local var_0_0 = class("GuildImpeachCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	if getProxy(GuildProxy).getData().inKickTime():
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_commder_in_impeach_time"))

		return

	pg.ConnectionMgr.GetInstance().Send(60016, {
		player_id = var_1_0
	}, 60017, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(GuildProxy)
			local var_2_1 = var_2_0.getData()
			local var_2_2 = pg.TimeMgr.GetInstance().GetServerTime() + 86400

			var_2_1.setkickLeaderTime(var_2_2)
			var_2_0.updateGuild(var_2_1)
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_impeach_sucess"))
			arg_1_0.sendNotification(GAME.GUILD_IMPEACH_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("guild_impeach_erro", arg_2_0.result)))

return var_0_0
