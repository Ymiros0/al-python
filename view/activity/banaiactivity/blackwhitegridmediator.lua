local var_0_0 = class("BlackWhiteGridMediator", import("...base.ContextMediator"))

var_0_0.ON_FINISH = "VirtualSpaceMediator:ON_FINISH"
var_0_0.ON_UPDATE_SCORE = "VirtualSpaceMediator:ON_UPDATE_SCORE"

function var_0_0.register(arg_1_0)
	local var_1_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_BLACKWHITE)

	arg_1_0.viewComponent:setActivity(var_1_0)
	arg_1_0:bind(var_0_0.ON_FINISH, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0:sendNotification(GAME.BLACK_WHITE_GRID_OP, {
			cmd = 1,
			activityId = var_1_0.id,
			id = arg_2_1,
			score = arg_2_2
		})
	end)
	arg_1_0:bind(var_0_0.ON_UPDATE_SCORE, function(arg_3_0, arg_3_1, arg_3_2)
		arg_1_0:sendNotification(GAME.BLACK_WHITE_GRID_OP, {
			cmd = 2,
			activityId = var_1_0.id,
			id = arg_3_1,
			score = arg_3_2
		})
	end)

	local var_1_1 = getProxy(PlayerProxy):getRawData()

	arg_1_0.viewComponent:setPlayer(var_1_1)
end

function var_0_0.listNotificationInterests(arg_4_0)
	return {
		GAME.BLACK_WHITE_GRID_OP_DONE,
		ActivityProxy.ACTIVITY_UPDATED
	}
end

function var_0_0.handleNotification(arg_5_0, arg_5_1)
	local var_5_0 = arg_5_1:getName()
	local var_5_1 = arg_5_1:getBody()

	if var_5_0 == GAME.BLACK_WHITE_GRID_OP_DONE then
		local var_5_2 = {
			function(arg_6_0)
				arg_5_0.viewComponent:playStory(arg_6_0)
			end,
			function(arg_7_0)
				local var_7_0 = var_5_1.awards

				if #var_7_0 > 0 then
					arg_5_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_7_0, arg_7_0)
				else
					arg_7_0()
				end
			end,
			function(arg_8_0)
				arg_5_0.viewComponent:updateBtnsState()
				arg_8_0()
			end
		}

		seriesAsync(var_5_2)
	elseif var_5_0 == ActivityProxy.ACTIVITY_UPDATED and arg_5_0.viewComponent.activityVO.id == var_5_1.id then
		arg_5_0.viewComponent:setActivity(var_5_1)
	end
end

return var_0_0
