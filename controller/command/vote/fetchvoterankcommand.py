local var_0_0 = class("FetchVoteRankCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.voteId
	local var_1_2 = var_1_0.callback
	local var_1_3 = getProxy(VoteProxy).RawGetTempVoteGroup(var_1_1)

	if var_1_3 and var_1_3.id == var_1_1:
		var_1_2()

		return

	pg.ConnectionMgr.GetInstance().Send(17203, {
		type = var_1_1
	}, 17204, function(arg_2_0)
		getProxy(VoteProxy).AddTempVoteGroup(arg_2_0, var_1_1)
		var_1_2())

return var_0_0
