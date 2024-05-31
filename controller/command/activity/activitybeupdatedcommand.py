local var_0_0 = class("ActivityBeUpdatedCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.activity
	local var_1_2 = var_1_0.isInit

	if var_1_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_INSTAGRAM:
		if var_1_1.CanBeActivated():
			getProxy(ActivityProxy).AddInstagramTimer(var_1_1.id)
	elif not var_1_2 and var_1_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_PT_BUFF and arg_1_0.IsLinkVoteAct(var_1_1):
		local var_1_3 = ActivityPtData.New(var_1_1)

		if var_1_3.CanGetAward():
			local var_1_4 = var_1_3.GetCurrTarget()

			arg_1_0.sendNotification(GAME.ACT_NEW_PT, {
				cmd = 4,
				activity_id = var_1_3.GetId(),
				arg1 = var_1_4
			})
	elif var_1_2 and var_1_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_COLLECTION_EVENT:
		local var_1_5 = var_1_1.GetCollectionList()

		getProxy(EventProxy).AddActivityEvents(var_1_5, var_1_1.id)

def var_0_0.IsLinkVoteAct(arg_2_0, arg_2_1):
	local var_2_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.VOTE_ENTRANCE_ACT_ID)

	if var_2_0 and not var_2_0.isEnd():
		local var_2_1 = var_2_0.getConfig("config_client")[1]

		return arg_2_1.id == var_2_1

	return False

return var_0_0
