﻿local var_0_0 = class("FetchVoteInfoCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.voteId
	local var_1_2 = var_1_0.callback

	if not var_1_1 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_error"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(17203, {
		type = var_1_1
	}, 17204, function(arg_2_0)
		getProxy(VoteProxy):AddVoteGroup(arg_2_0, var_1_1)
		arg_1_0:sendNotification(GAME.FETCH_VOTE_INFO_DONE)
		var_1_2()
	end)
end

return var_0_0
