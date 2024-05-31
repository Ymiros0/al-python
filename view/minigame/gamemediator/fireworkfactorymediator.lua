local var_0_0 = class("FireworkFactoryMediator", import(".MiniHubMediator"))

function var_0_0.handleNotification(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getName()
	local var_1_1 = arg_1_1:getBody()

	if var_1_0 == MiniGameProxy.ON_HUB_DATA_UPDATE then
		arg_1_0.viewComponent:SetMGHubData(var_1_1)
	elseif var_1_0 == GAME.SEND_MINI_GAME_OP_DONE and var_1_1.cmd == MiniGameOPCommand.CMD_COMPLETE then
		local var_1_2 = var_1_1.argList
		local var_1_3 = var_1_1.cmd
		local var_1_4 = {
			function(arg_2_0)
				local var_2_0 = (getProxy(MiniGameProxy):GetMiniGameData(MiniGameDataCreator.ShrineGameID):GetRuntimeData("count") or 0) + 1

				arg_1_0:sendNotification(GAME.MODIFY_MINI_GAME_DATA, {
					id = MiniGameDataCreator.ShrineGameID,
					map = {
						count = var_2_0
					}
				})
				arg_2_0()
			end,
			function(arg_3_0)
				local var_3_0 = var_1_1.awards

				if #var_3_0 > 0 then
					arg_1_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_3_0, arg_3_0)
				else
					arg_3_0()
				end
			end,
			function(arg_4_0)
				arg_1_0.viewComponent:OnGetAwardDone(var_1_1)
			end
		}

		seriesAsync(var_1_4)
		arg_1_0.viewComponent:OnSendMiniGameOPDone(var_1_1)
	elseif var_1_0 == GAME.MODIFY_MINI_GAME_DATA_DONE then
		arg_1_0.viewComponent:OnModifyMiniGameDataDone(var_1_1)
	else
		var_0_0.super.handleNotification(arg_1_0, arg_1_1)
	end
end

return var_0_0
