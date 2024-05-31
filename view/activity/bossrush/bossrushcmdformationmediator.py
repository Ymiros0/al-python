local var_0_0 = class("BossRushCMDFormationMediator", import("view.base.ContextMediator"))

def var_0_0.register(arg_1_0):
	local var_1_0 = getProxy(CommanderProxy).getPrefabFleet()

	arg_1_0.viewComponent.updateFleet(arg_1_0.contextData.fleet)
	arg_1_0.viewComponent.setCommanderPrefabs(var_1_0)
	arg_1_0.viewComponent.setCallback(arg_1_0.contextData.callback)

def var_0_0.listNotificationInterests(arg_2_0):
	return {
		CommanderProxy.PREFAB_FLEET_UPDATE,
		GAME.COMMANDER_ACTIVITY_FORMATION_OP_DONE
	}

def var_0_0.handleNotification(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.getName()
	local var_3_1 = arg_3_1.getBody()

	if var_3_0 == None:
		-- block empty
	elif var_3_0 == CommanderProxy.PREFAB_FLEET_UPDATE:
		local var_3_2 = getProxy(CommanderProxy).getPrefabFleet()

		arg_3_0.viewComponent.setCommanderPrefabs(var_3_2)
	elif var_3_0 == GAME.COMMANDER_ACTIVITY_FORMATION_OP_DONE:
		arg_3_0.viewComponent.updateRecordFleet()
		arg_3_0.viewComponent.updateDesc()
		arg_3_0.viewComponent.updateRecordPanel()

def var_0_0.remove(arg_4_0):
	return

return var_0_0
