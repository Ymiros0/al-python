local var_0_0 = class("RefluxGetPTAwardCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0)
	pg.ConnectionMgr.GetInstance():Send(11755, {
		type = 0
	}, 11756, function(arg_2_0)
		if arg_2_0.result == 0 then
			getProxy(RefluxProxy):addPTStage()

			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.award_list)

			pg.m02:sendNotification(GAME.REFLUX_GET_PT_AWARD_DONE, {
				awards = var_2_0
			})
		end
	end)
end

return var_0_0
