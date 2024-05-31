local var_0_0 = class("WorldOverviewMediator", import("..base.ContextMediator"))

var_0_0.OnAchieveStar = "WorldOverviewMediator.OnAchieveStar"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.OnAchieveStar, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.WORLD_ACHIEVE, {
			list = arg_2_1
		})
	end)
end

function var_0_0.listNotificationInterests(arg_3_0)
	return {
		GAME.WORLD_ACHIEVE_DONE
	}
end

function var_0_0.handleNotification(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:getName()
	local var_4_1 = arg_4_1:getBody()

	if var_4_0 == GAME.WORLD_ACHIEVE_DONE then
		-- block empty
	end
end

return var_0_0
