local var_0_0 = class("MainRequestVoteInfoSequence")

def var_0_0.Execute(arg_1_0, arg_1_1):
	if not arg_1_0.ExistVoteAct():
		arg_1_1()

		return

	seriesAsync({
		function(arg_2_0)
			arg_1_0.RequestMainStage(arg_2_0),
		function(arg_3_0)
			arg_1_0.RequestFunStage(arg_3_0)
	}, arg_1_1)

def var_0_0.ExistVoteAct(arg_4_0):
	return MainVoteEntranceBtn.New().InShowTime()

def var_0_0.RequestMainStage(arg_5_0, arg_5_1):
	local var_5_0 = _.detect(pg.activity_vote.all, function(arg_6_0)
		local var_6_0 = pg.activity_vote[arg_6_0]
		local var_6_1 = var_6_0.time_vote

		return pg.TimeMgr.GetInstance().inTime(var_6_1) and var_6_0.is_in_game == 1 and var_6_0.type != VoteConst.RACE_TYPE_FUN)

	if not var_5_0 or not arg_5_0.ShouldRequestMainStage(var_5_0):
		arg_5_1()

		return

	pg.m02.sendNotification(GAME.FETCH_VOTE_INFO, {
		voteId = var_5_0,
		def callback:()
			var_0_0.lastRequestTime = pg.TimeMgr.GetInstance().GetServerTime()

			arg_5_1()
	})

def var_0_0.ShouldRequestMainStage(arg_8_0, arg_8_1):
	local var_8_0 = getProxy(VoteProxy).RawGetVoteGroupByConfigId(arg_8_1)
	local var_8_1 = pg.TimeMgr.GetInstance().GetServerTime()

	return not var_8_0 or var_8_1 - (var_0_0.lastRequestTime or 0) > VoteConst.RankExpiredTime or var_8_0 and var_8_0.configId != arg_8_1

def var_0_0.RequestFunStage(arg_9_0, arg_9_1):
	local var_9_0 = _.detect(pg.activity_vote.all, function(arg_10_0)
		local var_10_0 = pg.activity_vote[arg_10_0]
		local var_10_1 = var_10_0.time_vote

		return pg.TimeMgr.GetInstance().inTime(var_10_1) and var_10_0.is_in_game == 1 and var_10_0.type == VoteConst.RACE_TYPE_FUN)

	if not var_9_0 or not arg_9_0.ShouldRequestFunStage(var_9_0):
		arg_9_1()

		return

	pg.m02.sendNotification(GAME.FETCH_VOTE_INFO, {
		voteId = var_9_0,
		def callback:()
			var_0_0.lastRequestTimeForFun = pg.TimeMgr.GetInstance().GetServerTime()

			arg_9_1()
	})

def var_0_0.ShouldRequestFunStage(arg_12_0, arg_12_1):
	local var_12_0 = getProxy(VoteProxy).RawGetVoteGroupByConfigId(arg_12_1)
	local var_12_1 = pg.TimeMgr.GetInstance().GetServerTime()

	return not var_12_0 or var_12_1 - (var_0_0.lastRequestTimeForFun or 0) > VoteConst.RankExpiredTime or var_12_0 and var_12_0.configId != arg_12_1

return var_0_0
