local var_0_0 = class("MusicFestivalMediator", import("..TemplateMV.BackHillMediatorTemplate"))

function var_0_0.listNotificationInterests(arg_1_0)
	return {
		GAME.SEND_MINI_GAME_OP_DONE,
		GAME.ACT_INSTAGRAM_OP_DONE,
		ActivityProxy.ACTIVITY_UPDATED
	}
end

function var_0_0.handleNotification(arg_2_0, arg_2_1)
	local var_2_0 = arg_2_1:getName()
	local var_2_1 = arg_2_1:getBody()

	if var_2_0 == GAME.SEND_MINI_GAME_OP_DONE then
		local var_2_2 = {
			function(arg_3_0)
				local var_3_0 = var_2_1.awards

				if #var_3_0 > 0 then
					arg_2_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_3_0, arg_3_0)
				else
					arg_3_0()
				end
			end,
			function(arg_4_0)
				arg_2_0.viewComponent:UpdateView()
			end
		}

		seriesAsync(var_2_2)
	elseif var_2_0 == GAME.ACT_INSTAGRAM_OP_DONE or var_2_0 == ActivityProxy.ACTIVITY_UPDATED then
		arg_2_0.viewComponent:UpdateView()
	end
end

return var_0_0
