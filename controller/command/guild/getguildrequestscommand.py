local var_0_0 = class("GetGuildRequestsCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	pg.ConnectionMgr.GetInstance().Send(60003, {
		id = var_1_0
	}, 60004, function(arg_2_0)
		local var_2_0 = {}
		local var_2_1 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.request_list):
			local var_2_2 = ChatMsg.New(ChatConst.ChannelGuild, {
				player = Player.New(iter_2_1.player),
				content = iter_2_1.content,
				timestamp = iter_2_1.timestamp
			})

			var_2_0[var_2_2.player.id] = var_2_2

			table.insert(var_2_1, var_2_2)

		getProxy(GuildProxy).setRequestList(var_2_0)
		arg_1_0.sendNotification(GAME.GUILD_GET_REQUEST_LIST_DONE, var_2_1))

return var_0_0
