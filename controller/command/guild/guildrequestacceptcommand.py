local var_0_0 = class("GuildRequestAcceptCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(GuildProxy)
	local var_1_2 = var_1_1.getData()

	if var_1_2.memberCount >= var_1_2.getMaxMember():
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_member_max_count"))

		return

	pg.ConnectionMgr.GetInstance().Send(60020, {
		player_id = var_1_0
	}, 60021, function(arg_2_0)
		if arg_2_0.result == 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_new_member_join"))
			arg_1_0.sendNotification(GAME.GUIDL_REQUEST_ACCEPT_DONE)
		elif arg_2_0.result == 4:
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_player_in_cd_time"))
		elif arg_2_0.result == 1:
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_player_already_join"))
			arg_1_0.sendNotification(GAME.GUIDL_REQUEST_REJECT, var_1_0, True)
		elif arg_2_0.result == 4305:
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_tip_grand_fleet_is_frozen"))
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("guild_accept_erro", arg_2_0.result))

		var_1_1.deleteRequest(var_1_0))

return var_0_0
