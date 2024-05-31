local var_0_0 = class("HoloLiveLinkGameMediator", import(".MiniHubMediator"))

function var_0_0.handleNotification(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getName()
	local var_1_1 = arg_1_1:getBody()

	if var_1_0 == GAME.SEND_MINI_GAME_OP_DONE and var_1_1.cmd == MiniGameOPCommand.CMD_COMPLETE then
		local var_1_2 = {
			function(arg_2_0)
				local var_2_0 = var_1_1.awards

				if #var_2_0 > 0 then
					arg_1_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_2_0, arg_2_0)
				else
					arg_2_0()
				end
			end,
			function(arg_3_0)
				arg_1_0.viewComponent:playStory()
			end
		}

		seriesAsync(var_1_2)
	else
		var_0_0.super.handleNotification(arg_1_0, arg_1_1)
	end
end

return var_0_0
