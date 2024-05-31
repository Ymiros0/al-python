local var_0_0 = class("ContinuousOperationWindowMediator", import("view.base.ContextMediator"))

def var_0_0.register(arg_1_0):
	arg_1_0.bind(PreCombatMediator.CONTINUOUS_OPERATION, function(arg_2_0)
		getProxy(SettingsProxy).setActBossExchangeTicketTip(arg_1_0.contextData.useTicket and 1 or 0)
		arg_1_0.sendNotification(GAME.AUTO_BOT, {
			isActiveBot = False,
			system = SYSTEM_ACT_BOSS
		})

		local var_2_0 = ys.Battle.BattleState.IsAutoSubActive(SYSTEM_ACT_BOSS)

		getProxy(SettingsProxy).RecordContinuousOperationAutoSubStatus(var_2_0)
		arg_1_0.sendNotification(GAME.AUTO_SUB, {
			isActiveSub = False,
			system = SYSTEM_ACT_BOSS
		})
		arg_1_0.sendNotification(PreCombatMediator.CONTINUOUS_OPERATION, {
			mainFleetId = arg_1_0.contextData.mainFleetId,
			battleTimes = math.min(arg_1_0.contextData.battleTimes, 15)
		}))

	local var_1_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2)

	arg_1_0.viewComponent.SetActivity(var_1_0)

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		ActivityProxy.ACTIVITY_UPDATED,
		PlayerProxy.UPDATED
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == ActivityProxy.ACTIVITY_UPDATED:
		if var_4_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2:
			arg_4_0.viewComponent.SetActivity(var_4_1)
	elif var_4_0 == PlayerProxy.UPDATED:
		arg_4_0.viewComponent.UpdateContent()

def var_0_0.remove(arg_5_0):
	return

return var_0_0
