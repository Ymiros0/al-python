local var_0_0 = class("GuildEventStartCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = getProxy(GuildProxy)

	if var_1_0.getData():
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_boss_appear"))

		var_1_0.eventTip = True

		arg_1_0.sendNotification(GAME.BOSS_EVENT_START_DONE)

return var_0_0
