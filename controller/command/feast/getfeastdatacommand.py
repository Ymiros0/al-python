local var_0_0 = class("GetFeastDataCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.callback
	local var_1_2 = var_1_0.activityId

	pg.ConnectionMgr.GetInstance().Send(26156, {
		act_id = var_1_2
	}, 26157, function(arg_2_0)
		if arg_2_0.ret == 0:
			local var_2_0 = FeastDorm.New({
				id = 4
			}, arg_2_0)

			arg_1_0.FixStoryList(var_2_0)
			getProxy(FeastProxy).SetData(var_2_0)
			arg_1_0.sendNotification(GAME.GET_FEAST_DATA_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)

		if var_1_1:
			var_1_1())

def var_0_0.FixStoryList(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.GetInvitedFeastShips()
	local var_3_1 = {}

	for iter_3_0, iter_3_1 in pairs(var_3_0):
		if iter_3_1.GotTicket():
			table.insert(var_3_1, iter_3_1.GetInvitationStory())

		if iter_3_1.GotGift():
			table.insert(var_3_1, iter_3_1.GetGiftStory())

	if #var_3_1 <= 0:
		return

	local var_3_2 = {}

	for iter_3_2, iter_3_3 in pairs(var_3_1):
		if not pg.NewStoryMgr.GetInstance().IsPlayed(iter_3_3):
			table.insert(var_3_2, iter_3_3)

	if #var_3_2 > 0:
		for iter_3_4, iter_3_5 in ipairs(var_3_2):
			pg.m02.sendNotification(GAME.STORY_UPDATE, {
				storyId = iter_3_5
			})

return var_0_0
