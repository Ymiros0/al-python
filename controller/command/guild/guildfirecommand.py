local var_0_0 = class("GuildFireCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(GuildProxy)
	local var_1_2 = getProxy(PlayerProxy).getData()
	local var_1_3 = var_1_1.getData()

	if var_1_3.getDutyByMemberId(var_1_2.id) >= var_1_3.getDutyByMemberId(var_1_0):
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_fire_duty_limit"))

		return

	pg.ConnectionMgr.GetInstance().Send(60014, {
		player_id = var_1_0
	}, 60015, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = var_1_1.getData()
			local var_2_1 = var_1_1.getData()

			var_2_1.deleteMember(var_1_0)
			var_1_1.updateGuild(var_2_1)
			arg_1_0.sendNotification(GAME.GUILD_FIRE_DONE)
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_fire_succeed"))
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("guild_fire_erro", arg_2_0.result)))

return var_0_0
