local var_0_0 = class("VoteCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.voteId
	local var_1_2 = var_1_0.gid
	local var_1_3 = var_1_0.count
	local var_1_4 = getProxy(VoteProxy)
	local var_1_5 = var_1_4.GetVoteActivityByConfigId(var_1_1)

	if not var_1_5 or var_1_5.isEnd():
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

		return

	local var_1_6 = var_1_5.id
	local var_1_7 = var_1_4.RawGetVoteGroupByConfigId(var_1_1)

	if not var_1_7:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

		return

	if not var_1_7.IsOpening():
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

		return

	if var_1_3 > var_1_4.GetVotesByConfigId(var_1_1):
		pg.TipsMgr.GetInstance().ShowTips(i18n("vote_not_enough"))

		return

	pg.ConnectionMgr.GetInstance().Send(11202, {
		cmd = 1,
		activity_id = var_1_6,
		arg1 = var_1_1,
		arg2 = var_1_2,
		arg3 = var_1_3,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.award_list)
			local var_2_1 = getProxy(ActivityProxy)
			local var_2_2 = var_2_1.getActivityById(var_1_6)

			var_2_2.data1 = var_2_2.data1 - var_1_3
			var_2_2.data2 = var_2_2.data2 + var_1_3

			var_2_1.updateActivity(var_2_2)
			var_1_7.UpdateVoteCnt(var_1_2, var_1_3)
			arg_1_0.sendNotification(GAME.ON_NEW_VOTE_DONE, {
				awards = var_2_0
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result]))

return var_0_0
