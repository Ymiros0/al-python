local var_0_0 = class("SetGuildDutyCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.playerId
	local var_1_2 = var_1_0.dutyId

	if not var_1_2:
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_duty_id_is_null"))

		return

	if not var_1_1:
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_player_is_null"))

		return

	local var_1_3 = getProxy(GuildProxy).getData()

	if var_1_2 == GuildConst.DUTY_DEPUTY_COMMANDER and var_1_3.getAssistantCount() == var_1_3.getAssistantMaxCount():
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_duty_commder_max_count"))

		return

	pg.ConnectionMgr.GetInstance().Send(60012, {
		player_id = var_1_1,
		duty_id = var_1_2
	}, 60013, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(GuildProxy)
			local var_2_1 = var_2_0.getData()
			local var_2_2 = var_2_1.getMemberById(var_1_1)

			var_2_2.setDuty(var_1_2)

			if var_1_2 == GuildConst.DUTY_COMMANDER:
				local var_2_3 = getProxy(PlayerProxy).getRawData().id

				var_2_1.getMemberById(var_2_3).setDuty(GuildConst.DUTY_ORDINARY)

			var_2_0.updateGuild(var_2_1)
			arg_1_0.sendNotification(GAME.SET_GUILD_DUTY_DONE, var_2_2)
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_set_duty_sucess"))
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("guild_setduty_erro", arg_2_0.result)))

return var_0_0
