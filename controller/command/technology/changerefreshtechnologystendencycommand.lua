﻿local var_0_0 = class("ChangeRefreshTechnologysTendencyCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.pool_id
	local var_1_2 = var_1_0.tendency

	pg.ConnectionMgr.GetInstance():Send(63009, {
		id = var_1_1,
		target = var_1_2
	}, 63010, function(arg_2_0)
		if arg_2_0.result == 0 then
			getProxy(TechnologyProxy):setTendency(var_1_1, var_1_2)
			arg_1_0:sendNotification(GAME.CHANGE_REFRESH_TECHNOLOGYS_TENDENCY_DONE)
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("change_technology_refresh_erro") .. arg_2_0.result)
		end
	end)
end

return var_0_0
