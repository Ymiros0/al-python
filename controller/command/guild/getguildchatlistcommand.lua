local var_0_0 = class("GetGuildChatListCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = GuildConst.CHAT_LOG_MAX_COUNT
	local var_1_2 = getProxy(GuildProxy)
	local var_1_3 = var_1_2:getData()

	if not var_1_3 then
		return
	end

	pg.ConnectionMgr.GetInstance():Send(60100, {
		count = var_1_1
	}, 60101, function(arg_2_0)
		var_1_2.isGetChatMsg = true

		local var_2_0 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.chat_list or {}) do
			local var_2_1 = var_1_3:warpChatInfo(iter_2_1)

			var_1_2:addMsg(var_2_1)
		end

		arg_1_0:sendNotification(GAME.GET_GUILD_CHAT_LIST_DONE)
	end)
end

return var_0_0
