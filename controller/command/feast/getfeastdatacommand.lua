﻿local var_0_0 = class("GetFeastDataCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.callback
	local var_1_2 = var_1_0.activityId

	pg.ConnectionMgr.GetInstance():Send(26156, {
		act_id = var_1_2
	}, 26157, function(arg_2_0)
		if arg_2_0.ret == 0 then
			local var_2_0 = FeastDorm.New({
				id = 4
			}, arg_2_0)

			arg_1_0:FixStoryList(var_2_0)
			getProxy(FeastProxy):SetData(var_2_0)
			arg_1_0:sendNotification(GAME.GET_FEAST_DATA_DONE)
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end

		if var_1_1 then
			var_1_1()
		end
	end)
end

function var_0_0.FixStoryList(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_1:GetInvitedFeastShips()
	local var_3_1 = {}

	for iter_3_0, iter_3_1 in pairs(var_3_0) do
		if iter_3_1:GotTicket() then
			table.insert(var_3_1, iter_3_1:GetInvitationStory())
		end

		if iter_3_1:GotGift() then
			table.insert(var_3_1, iter_3_1:GetGiftStory())
		end
	end

	if #var_3_1 <= 0 then
		return
	end

	local var_3_2 = {}

	for iter_3_2, iter_3_3 in pairs(var_3_1) do
		if not pg.NewStoryMgr.GetInstance():IsPlayed(iter_3_3) then
			table.insert(var_3_2, iter_3_3)
		end
	end

	if #var_3_2 > 0 then
		for iter_3_4, iter_3_5 in ipairs(var_3_2) do
			pg.m02:sendNotification(GAME.STORY_UPDATE, {
				storyId = iter_3_5
			})
		end
	end
end

return var_0_0
