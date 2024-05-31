﻿local var_0_0 = class("GuildFetchCapitalCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()

	pg.ConnectionMgr.GetInstance():Send(62024, {
		type = 0
	}, 62025, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = getProxy(GuildProxy)
			local var_2_1 = var_2_0:getData()

			var_2_1:setRefreshCaptialTime()
			var_2_1:updateCapital(arg_2_0.capital)
			var_2_0:updateGuild(var_2_1)
			arg_1_0:sendNotification(GAME.GUILD_REFRESH_CAPITAL_DONE)
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end
	end)
end

return var_0_0
