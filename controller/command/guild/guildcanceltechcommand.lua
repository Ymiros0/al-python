﻿local var_0_0 = class("GuildCancelTechCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody().id
	local var_1_1 = getProxy(GuildProxy):getData()

	if not var_1_1 then
		pg.TipsMgr:GetInstance():ShowTips(i18n("guild_no_exist"))

		return
	end

	if not var_1_1:getActiveTechnologyGroup() then
		pg.TipsMgr:GetInstance():ShowTips(i18n("guild_not_exist_activation_tech"))

		return
	end

	local var_1_2 = var_1_1:getTechnologyGroupById(var_1_0)

	if not var_1_2 then
		pg.TipsMgr:GetInstance():ShowTips(i18n("guild_not_exist_tech"))

		return
	end

	if not var_1_1:CanCancelTech() then
		pg.TipsMgr:GetInstance():ShowTips(i18n("guild_cancel_only_once_pre_day"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(62026, {
		id = var_1_2.pid
	}, 62027, function(arg_2_0)
		if arg_2_0.result == 0 then
			arg_1_0:sendNotification(GAME.GUILD_CANCEL_TECH_DONE)
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end
	end)
end

return var_0_0
