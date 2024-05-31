local var_0_0 = class("GuildGetUserInfoCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(GuildProxy)

	if not var_1_1.getData():
		return

	pg.ConnectionMgr.GetInstance().Send(60102, {
		type = 0
	}, 60103, function(arg_2_0)
		local var_2_0 = var_1_1.getData()

		var_2_0.updateUserInfo(arg_2_0)
		var_1_1.updateGuild(var_2_0)
		arg_1_0.sendNotification(GAME.GUILD_GET_USER_INFO_DONE))

return var_0_0
