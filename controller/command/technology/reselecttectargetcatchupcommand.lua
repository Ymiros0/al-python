local var_0_0 = class("ReSelectTecTargetCatchupCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody().charID

	pg.ConnectionMgr.GetInstance():Send(63013, {
		target = var_1_0
	}, 63014, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = getProxy(TechnologyProxy)
			local var_2_1 = var_2_0:getNewestCatchupTecID()
			local var_2_2 = var_1_0

			var_2_0:setCurCatchupTecInfo(var_2_1, var_2_2)
			arg_1_0:sendNotification(GAME.RESELECT_TEC_TARGET_CATCHUP_DONE)
		else
			pg.TipsMgr.GetInstance():ShowTips("Error Code" .. arg_2_0.result)
		end
	end)
end

return var_0_0
