local var_0_0 = class("LimitChallengeReqCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = {
		type = 1
	}

	pg.ConnectionMgr.GetInstance().Send(24020, var_1_1, 24021, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(LimitChallengeProxy)

			var_2_0.setTimeDataFromServer(arg_2_0.times)
			var_2_0.setAwardedDataFromServer(arg_2_0.awards)
			var_2_0.setCurMonthPassedIDList(arg_2_0.pass_ids)
			arg_1_0.sendNotification(LimitChallengeConst.REQ_CHALLENGE_INFO_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_2_0.result)))

return var_0_0
