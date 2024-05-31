local var_0_0 = class("GuildDissolveCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = getProxy(GuildProxy)

	if not var_1_1:getData() then
		pg.TipsMgr.GetInstance():ShowTips(i18n("guild_no_exist"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(60010, {
		id = var_1_0
	}, 60011, function(arg_2_0)
		if arg_2_0.result == 0 then
			var_1_1:exitGuild()
			arg_1_0:sendNotification(GAME.GUILD_DISSOLVE_DONE)

			local var_2_0 = getProxy(PlayerProxy)
			local var_2_1 = var_2_0:getData()

			var_2_1:setGuildWaitTime(pg.TimeMgr.GetInstance():GetServerTime() + 86400)
			var_2_0:updatePlayer(var_2_1)
			pg.TipsMgr.GetInstance():ShowTips(i18n("guild_dissolve_sucess"))
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("guild_dissolve_erro", arg_2_0.result))
		end
	end)
end

return var_0_0
