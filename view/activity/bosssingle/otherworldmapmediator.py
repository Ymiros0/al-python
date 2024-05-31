local var_0_0 = class("OtherworldMapMediator", import("view.activity.BossSingle.BossSingleMediatorTemplate"))

var_0_0.ON_EVENT_TRIGGER = "OtherworldMapMediator.ON_EVENT_TRIGGER"

def var_0_0.register(arg_1_0):
	arg_1_0.BindBattleEvents()
	arg_1_0.bind(var_0_0.ON_EVENT_TRIGGER, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.SINGLE_EVENT_TRIGGER, {
			actId = arg_2_1.actId,
			eventId = arg_2_1.eventId
		}))

	local var_1_0 = getProxy(ActivityProxy)
	local var_1_1 = var_1_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_EVENT_SINGLE)

	if var_1_1 and not var_1_1.isEnd():
		arg_1_0.viewComponent.SetEventAct(var_1_1)
	else
		arg_1_0.viewComponent.SetEventAct(None)

	local var_1_2 = var_1_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_LOTTERY)

	if not var_1_2:
		assert(None, "not exist lottery act")

		return

	local var_1_3 = var_1_2.getConfig("config_data")[1]

	arg_1_0.contextData.resId = pg.activity_random_award_template[var_1_3].resource_type

def var_0_0.initNotificationHandleDic(arg_3_0):
	arg_3_0.handleDic = {
		[GAME.BEGIN_STAGE_DONE] = function(arg_4_0, arg_4_1)
			local var_4_0 = arg_4_1.getBody()

			arg_4_0.contextData.editFleet = None

			if not getProxy(ContextProxy).getContextByMediator(PreCombatMediator):
				arg_4_0.sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_4_0),
		[GAME.COMMANDER_ACTIVITY_FORMATION_OP_DONE] = function(arg_5_0, arg_5_1)
			local var_5_0 = arg_5_1.getBody()
			local var_5_1 = getProxy(FleetProxy).getActivityFleets()[var_5_0.actId]

			arg_5_0.contextData.actFleets = var_5_1

			arg_5_0.viewComponent.updateEditPanel()
			arg_5_0.viewComponent.updateCommanderFleet(var_5_1[var_5_0.fleetId]),
		[CommanderProxy.PREFAB_FLEET_UPDATE] = function(arg_6_0, arg_6_1)
			local var_6_0 = arg_6_1.getBody()
			local var_6_1 = getProxy(CommanderProxy).getPrefabFleet()

			arg_6_0.viewComponent.setCommanderPrefabs(var_6_1)
			arg_6_0.viewComponent.updateCommanderPrefab(),
		[PlayerProxy.UPDATED] = function(arg_7_0, arg_7_1)
			arg_7_0.viewComponent.UpdateRes()
			arg_7_0.viewComponent.UpdateWangduBtn(),
		[ActivityProxy.ACTIVITY_UPDATED] = function(arg_8_0, arg_8_1)
			local var_8_0 = arg_8_1.getBody()

			if not var_8_0 or var_8_0.isEnd():
				return

			if var_8_0.id == ActivityConst.OTHER_WORLD_TERMINAL_PT_ID:
				arg_8_0.viewComponent.UpdateTerminalTip(),
		[GAME.SINGLE_EVENT_TRIGGER_DONE] = function(arg_9_0, arg_9_1)
			local var_9_0 = arg_9_1.getBody()
			local var_9_1 = {}

			if #var_9_0.awards > 0:
				table.insert(var_9_1, function(arg_10_0)
					arg_9_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_9_0.awards, arg_10_0))

			seriesAsync(var_9_1, function()
				arg_9_0.viewComponent.SetEventAct(var_9_0.activity)
				arg_9_0.viewComponent.UpdateEvents(var_9_0.eventId)),
		[GAME.SINGLE_EVENT_REFRESH_DONE] = function(arg_12_0, arg_12_1)
			local var_12_0 = arg_12_1.getBody()

			arg_12_0.viewComponent.SetEventAct(var_12_0.activity)
			arg_12_0.viewComponent.UpdateEvents(),
		[GAME.ACT_NEW_PT_DONE] = function(arg_13_0, arg_13_1)
			local var_13_0 = arg_13_1.getBody()

			arg_13_0.viewComponent.UpdateTerminalTip(),
		[AvatarFrameProxy.FRAME_TASK_UPDATED] = function(arg_14_0, arg_14_1)
			arg_14_0.viewComponent.UpdateWangduBtn(),
		[AvatarFrameProxy.FRAME_TASK_TIME_OUT] = function(arg_15_0, arg_15_1)
			arg_15_0.viewComponent.UpdateWangduBtn()
	}

def var_0_0.remove(arg_16_0):
	return

return var_0_0
