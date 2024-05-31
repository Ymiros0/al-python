﻿local var_0_0 = class("GuildBuySupplyCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = getProxy(GuildProxy):getData()

	if not var_1_1 then
		pg.TipsMgr:GetInstance():ShowTips(i18n("guild_no_exist"))

		return
	end

	if not GuildMember.IsAdministrator(var_1_1:getSelfDuty()) then
		pg.TipsMgr:GetInstance():ShowTips(i18n("guild_op_only_administrator"))

		return
	end

	if var_1_1:getSupplyConsume() > var_1_1:getCapital() then
		pg.TipsMgr:GetInstance():ShowTips(i18n("common_no_resource"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(62007, {
		type = 0
	}, 62008, function(arg_2_0)
		if arg_2_0.result == 0 then
			arg_1_0:sendNotification(GAME.GUILD_BUY_SUPPLY_DONE)
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end
	end)
end

return var_0_0
