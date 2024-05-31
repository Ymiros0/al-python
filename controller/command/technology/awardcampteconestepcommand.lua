local var_0_0 = class("AwardCampTecCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = 1
	local var_1_1 = {
		type = var_1_0
	}

	print("64007 Get TecCamp Award OneStep", var_1_0)
	pg.ConnectionMgr.GetInstance():Send(64007, var_1_1, 64008, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.rewards)
			local var_2_1 = getProxy(TechnologyNationProxy)

			var_2_1:updateTecItemAwardOneStep()
			arg_1_0:sendNotification(TechnologyConst.GOT_TEC_CAMP_AWARD_ONESTEP, {
				awardList = var_2_0
			})
			var_2_1:refreshRedPoint()
			arg_1_0:sendNotification(TechnologyConst.UPDATE_REDPOINT_ON_TOP)
		else
			pg.TipsMgr.GetInstance():ShowTips("64007 Error Code:" .. arg_2_0.result)
		end
	end)
end

return var_0_0
