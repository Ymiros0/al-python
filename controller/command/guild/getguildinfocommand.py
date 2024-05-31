local var_0_0 = class("GetGuildInfoCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	if not getProxy(GuildProxy).getRawData() and not getProxy(GuildProxy).isFetchMainInfo:
		pg.ConnectionMgr.GetInstance().Send(60037, {
			type = 0
		}, 60000, function(arg_2_0)
			getProxy(GuildProxy).isFetchMainInfo = True

			arg_1_0.sendNotification(GAME.GET_GUILD_INFO_DONE))
	else
		arg_1_0.sendNotification(GAME.GET_GUILD_INFO_DONE)

return var_0_0
