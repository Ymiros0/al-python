local var_0_0 = class("SelectTecTargetCatchupCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.tecID
	local var_1_2 = var_1_0.charID

	pg.ConnectionMgr.GetInstance():Send(63011, {
		version = var_1_1,
		target = var_1_2
	}, 63012, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = getProxy(TechnologyProxy)
			local var_2_1 = var_1_0.tecID
			local var_2_2 = var_1_2

			if var_1_2 == 0 then
				-- block empty
			else
				var_2_0:setCurCatchupTecInfo(var_2_1, var_2_2)
			end

			arg_1_0:sendNotification(GAME.SELECT_TEC_TARGET_CATCHUP_DONE, {
				tecID = var_2_1
			})
		else
			pg.TipsMgr.GetInstance():ShowTips("Error Code" .. arg_2_0.result)
		end
	end)
end

return var_0_0
