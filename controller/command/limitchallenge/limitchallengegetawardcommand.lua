local var_0_0 = class("LimitChallengeGetAwardCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = {
		challengeids = var_1_0.challengeIDList
	}

	pg.ConnectionMgr.GetInstance():Send(24022, var_1_1, 24023, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = getProxy(LimitChallengeProxy)

			for iter_2_0, iter_2_1 in ipairs(var_1_0.challengeIDList) do
				var_2_0:setAwarded(iter_2_1)
			end

			local var_2_1 = PlayerConst.addTranDrop(arg_2_0.drop_list)

			pg.m02:sendNotification(LimitChallengeConst.GET_CHALLENGE_AWARD_DONE, {
				awards = var_2_1
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end
	end)
end

return var_0_0
