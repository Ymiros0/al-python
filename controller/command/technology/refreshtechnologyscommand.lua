﻿local var_0_0 = class("RefreshTechnologysCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = getProxy(TechnologyProxy)

	if var_1_1.refreshTechnologysFlag ~= 0 then
		return
	end

	if tobool(var_1_1:getActivateTechnology()) then
		return
	end

	pg.ConnectionMgr.GetInstance():Send(63007, {
		type = 1
	}, 63008, function(arg_2_0)
		if arg_2_0.result == 0 then
			var_1_1:updateTechnologys(arg_2_0.refresh_list)
			var_1_1:updateRefreshFlag(1)
			arg_1_0:sendNotification(GAME.REFRESH_TECHNOLOGYS_DONE)
			pg.TipsMgr.GetInstance():ShowTips(i18n("technology_refresh_sucess"))
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("technology_refresh_erro") .. arg_2_0.result)
		end
	end)
end

return var_0_0
