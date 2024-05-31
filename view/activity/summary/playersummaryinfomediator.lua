local var_0_0 = class("PlayerSummaryInfoMediator", import("...base.ContextMediator"))

var_0_0.GET_PLAYER_SUMMARY_INFO = "PlayerSummaryInfoMediator:GET_PLAYER_SUMMARY_INFO"

function var_0_0.register(arg_1_0)
	local var_1_0 = getProxy(ActivityProxy)

	arg_1_0:bind(var_0_0.GET_PLAYER_SUMMARY_INFO, function(arg_2_0)
		local var_2_0 = var_1_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_SUMMARY)

		if var_2_0 and not var_2_0:isEnd() then
			arg_1_0:sendNotification(GAME.GET_PLAYER_SUMMARY_INFO, {
				activityId = var_2_0.id
			})
		end
	end)

	local var_1_1 = var_1_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_SUMMARY)

	arg_1_0.viewComponent:setActivity(var_1_1)

	local var_1_2 = getProxy(PlayerProxy)

	arg_1_0.viewComponent:setPlayer(var_1_2:getData())

	local var_1_3 = var_1_2:getSummaryInfo()

	arg_1_0.viewComponent:setSummaryInfo(var_1_3)
end

function var_0_0.listNotificationInterests(arg_3_0)
	return {
		GAME.GET_PLAYER_SUMMARY_INFO_DONE
	}
end

function var_0_0.handleNotification(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:getName()
	local var_4_1 = arg_4_1:getBody()

	if var_4_0 == GAME.GET_PLAYER_SUMMARY_INFO_DONE then
		arg_4_0.viewComponent:setSummaryInfo(var_4_1)
		arg_4_0.viewComponent:initSummaryInfo()
	end
end

return var_0_0
