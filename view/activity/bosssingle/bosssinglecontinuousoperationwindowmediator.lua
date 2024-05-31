local var_0_0 = class("BossSingleContinuousOperationWindowMediator", import("view.base.ContextMediator"))

function var_0_0.register(arg_1_0)
	arg_1_0:bind(PreCombatMediator.CONTINUOUS_OPERATION, function(arg_2_0)
		arg_1_0:sendNotification(GAME.AUTO_BOT, {
			isActiveBot = false,
			system = SYSTEM_BOSS_SINGLE
		})

		local var_2_0 = ys.Battle.BattleState.IsAutoSubActive(SYSTEM_BOSS_SINGLE)

		getProxy(SettingsProxy):RecordContinuousOperationAutoSubStatus(var_2_0)
		arg_1_0:sendNotification(GAME.AUTO_SUB, {
			isActiveSub = false,
			system = SYSTEM_BOSS_SINGLE
		})
		arg_1_0:sendNotification(BossSinglePreCombatMediator.CONTINUOUS_OPERATION, {
			mainFleetId = arg_1_0.contextData.mainFleetId,
			battleTimes = math.min(arg_1_0.contextData.battleTimes, 15)
		})
	end)
end

function var_0_0.listNotificationInterests(arg_3_0)
	return {
		PlayerProxy.UPDATED
	}
end

function var_0_0.handleNotification(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:getName()
	local var_4_1 = arg_4_1:getBody()

	if var_4_0 == PlayerProxy.UPDATED then
		arg_4_0.viewComponent:UpdateContent()
	end
end

function var_0_0.remove(arg_5_0)
	return
end

return var_0_0
