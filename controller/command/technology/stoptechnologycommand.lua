local var_0_0 = class("StopTechnologyCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.pool_id
	local var_1_3 = getProxy(TechnologyProxy)
	local var_1_4 = var_1_3:getTechnologyById(var_1_1)

	if not var_1_4 or not var_1_4:isActivate() or var_1_4:isCompleted() then
		return
	end

	pg.ConnectionMgr.GetInstance():Send(63005, {
		tech_id = var_1_1,
		refresh_id = var_1_2
	}, 63006, function(arg_2_0)
		if arg_2_0.result == 0 then
			var_1_4:reset()
			var_1_3:updateTechnology(var_1_4)
			arg_1_0:sendNotification(GAME.STOP_TECHNOLOGY_DONE)
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("blueprint_stop_erro") .. arg_2_0.result)
		end
	end)
end

return var_0_0
