local var_0_0 = class("ShipBluePrintMediator", import("..base.ContextMediator"))

var_0_0.ON_CLICK_SPEEDUP_BTN = "ShipBluePrintMediator.ON_CLICK_SPEEDUP_BTN"
var_0_0.ON_START = "ShipBluePrintMediator.ON_START"
var_0_0.ON_FINISHED = "ShipBluePrintMediator.ON_FINISHED"
var_0_0.ON_ITEM_UNLOCK = "ShipBluePrintMediator.ON_ITEM_UNLOCK"
var_0_0.ON_FINISH_TASK = "ShipBluePrintMediator.ON_FINISH_TASK"
var_0_0.ON_MOD = "ShipBluePrintMediator.ON_MOD"
var_0_0.ON_PURSUING = "ShipBluePrintMediator.ON_PURSUING"
var_0_0.ON_TASK_OPEN = "ShipBluePrintMediator.ON_TASK_OPEN"
var_0_0.ON_CHECK_TAKES = "ShipBluePrintMediator.ON_CHECK_TAKES"
var_0_0.SHOW_SKILL_INFO = "ShipBluePrintMediator.SHOW_SKILL_INFO"
var_0_0.SET_TECHNOLOGY_VERSION = "ShipBluePrintMediator.SET_TECHNOLOGY_VERSION"
var_0_0.SIMULATION_BATTLE = "ShipBluePrintMediator.SIMULATION_BATTLE"
var_0_0.QUICK_EXCHAGE_BLUEPRINT = "ShipBluePrintMediator.QUICK_EXCHAGE_BLUEPRINT"

def var_0_0.register(arg_1_0):
	PlayerPrefs.SetString("technology_day_mark", pg.TimeMgr.GetInstance().CurrentSTimeDesc("%Y/%m/%d", True))

	local var_1_0 = getProxy(TechnologyProxy)

	if arg_1_0.contextData.shipId:
		local var_1_1 = getProxy(BayProxy).getShipById(arg_1_0.contextData.shipId)
		local var_1_2 = var_1_0.getBluePrintById(var_1_1.groupId)

		arg_1_0.contextData.shipBluePrintVO = var_1_2
	elif arg_1_0.contextData.shipGroupId:
		local var_1_3 = var_1_0.getBluePrintById(arg_1_0.contextData.shipGroupId)

		arg_1_0.contextData.shipBluePrintVO = var_1_3

	arg_1_0.bind(var_0_0.ON_CLICK_SPEEDUP_BTN, function()
		arg_1_0.addSubLayers(Context.New({
			viewComponent = TecSpeedUpLayer,
			mediator = TecSpeedUpMediator
		})))
	arg_1_0.bind(var_0_0.ON_START, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.BUILD_SHIP_BLUEPRINT, {
			id = arg_3_1
		}))
	arg_1_0.bind(var_0_0.ON_FINISHED, function(arg_4_0, arg_4_1)
		arg_1_0.sendNotification(GAME.FINISH_SHIP_BLUEPRINT, {
			id = arg_4_1
		}))
	arg_1_0.bind(var_0_0.ON_ITEM_UNLOCK, function(arg_5_0, arg_5_1, arg_5_2)
		arg_1_0.sendNotification(GAME.ITEM_LOCK_SHIP_BLUPRINT, {
			id = arg_5_1,
			itemId = arg_5_2
		}))
	arg_1_0.bind(var_0_0.ON_FINISH_TASK, function(arg_6_0, arg_6_1)
		local var_6_0 = Task.New({
			id = arg_6_1
		})

		if var_6_0.getConfig("sub_type") == TASK_SUB_TYPE_GIVE_ITEM:
			local var_6_1 = getDropInfo({
				{
					DROP_TYPE_ITEM,
					tonumber(var_6_0.getConfig("target_id")),
					var_6_0.getConfig("target_num")
				}
			})

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("blueprint_commit_tip", var_6_1),
				def onYes:()
					arg_1_0.sendNotification(GAME.SUBMIT_TASK, arg_6_1)
			})
		elif var_6_0.getConfig("sub_type") == TASK_SUB_TYPE_PLAYER_RES:
			local var_6_2 = getDropInfo({
				{
					DROP_TYPE_RESOURCE,
					tonumber(var_6_0.getConfig("target_id")),
					var_6_0.getConfig("target_num")
				}
			})

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("blueprint_commit_tip", var_6_2),
				def onYes:()
					arg_1_0.sendNotification(GAME.SUBMIT_TASK, arg_6_1)
			})
		else
			arg_1_0.sendNotification(GAME.SUBMIT_TASK, arg_6_1))
	arg_1_0.bind(var_0_0.ON_MOD, function(arg_9_0, arg_9_1, arg_9_2)
		arg_1_0.sendNotification(GAME.MOD_BLUEPRINT, {
			id = arg_9_1,
			count = arg_9_2
		}))
	arg_1_0.bind(var_0_0.ON_PURSUING, function(arg_10_0, arg_10_1, arg_10_2)
		arg_1_0.sendNotification(GAME.PURSUING_BLUEPRINT, {
			id = arg_10_1,
			count = arg_10_2
		}))
	arg_1_0.bind(var_0_0.ON_TASK_OPEN, function(arg_11_0, arg_11_1)
		if not getProxy(TaskProxy).isFinishPrevTasks(arg_11_1):
			return

		arg_1_0.sendNotification(GAME.TRIGGER_TASK, arg_11_1))
	arg_1_0.bind(var_0_0.ON_CHECK_TAKES, function(arg_12_0, arg_12_1)
		local var_12_0 = getProxy(TechnologyProxy)
		local var_12_1 = var_12_0.getBluePrintById(arg_12_1)

		if var_12_1.isFinishedAllTasks():
			var_12_1.finish()
			var_12_0.updateBluePrint(var_12_1))
	arg_1_0.bind(var_0_0.SHOW_SKILL_INFO, function(arg_13_0, arg_13_1, arg_13_2, arg_13_3)
		arg_1_0.addSubLayers(Context.New({
			mediator = SkillInfoMediator,
			viewComponent = SkillInfoLayer,
			data = {
				skillOnShip = arg_13_2,
				skillId = arg_13_1,
				onExit = arg_13_3
			}
		})))
	arg_1_0.bind(var_0_0.SET_TECHNOLOGY_VERSION, function(arg_14_0, arg_14_1)
		var_1_0.setVersion(arg_14_1))
	arg_1_0.bind(var_0_0.SIMULATION_BATTLE, function(arg_15_0, arg_15_1)
		arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
			system = SYSTEM_SIMULATION,
			stageId = arg_15_1
		}))
	arg_1_0.bind(var_0_0.QUICK_EXCHAGE_BLUEPRINT, function(arg_16_0, arg_16_1)
		arg_1_0.sendNotification(GAME.QUICK_EXCHANGE_BLUEPRINT, arg_16_1))

	local var_1_4 = var_1_0.getBluePrints()

	arg_1_0.viewComponent.setShipBluePrints(var_1_4)

	local var_1_5 = getProxy(BayProxy)

	arg_1_0.viewComponent.setShipVOs(var_1_5.getRawData())
	arg_1_0.viewComponent.setVersion(var_1_0.getVersion())
	arg_1_0.viewComponent.setTaskVOs(getProxy(TaskProxy).getTasksForBluePrint())

def var_0_0.listNotificationInterests(arg_17_0):
	return {
		GAME.BUILD_SHIP_BLUEPRINT_DONE,
		TechnologyProxy.BLUEPRINT_UPDATED,
		TaskProxy.TASK_ADDED,
		TaskProxy.TASK_UPDATED,
		TaskProxy.TASK_REMOVED,
		GAME.SUBMIT_TASK_DONE,
		GAME.FINISH_SHIP_BLUEPRINT_DONE,
		GAME.ITEM_LOCK_SHIP_BLUPRINT_DONE,
		GAME.STOP_BLUEPRINT_DONE,
		GAME.MOD_BLUEPRINT_DONE,
		BayProxy.SHIP_ADDED,
		BayProxy.SHIP_UPDATED,
		GAME.BEGIN_STAGE_DONE,
		GAME.MOD_BLUEPRINT_ANIM_LOCK,
		GAME.PURSUING_RESET_DONE,
		GAME.QUICK_EXCHANGE_BLUEPRINT_DONE
	}

def var_0_0.handleNotification(arg_18_0, arg_18_1):
	local var_18_0 = arg_18_1.getName()
	local var_18_1 = arg_18_1.getBody()

	if var_18_0 == TechnologyProxy.BLUEPRINT_UPDATED:
		arg_18_0.viewComponent.updateShipBluePrintVO(var_18_1)
	elif var_18_0 == GAME.EXCHANG_BLUEPRINT_DONE:
		arg_18_0.viewComponent.clearSelected()
		arg_18_0.viewComponent.updateExchangeItems()
		arg_18_0.viewComponent.updateBuildInfo()
	elif var_18_0 == TaskProxy.TASK_ADDED or TaskProxy.TASK_UPDATED == var_18_0 or TaskProxy.TASK_REMOVED == var_18_0:
		arg_18_0.viewComponent.setTaskVOs(getProxy(TaskProxy).getTasksForBluePrint())
		arg_18_0.viewComponent.updateTaskList()
		arg_18_0.viewComponent.updateTasksProgress()
	elif var_18_0 == GAME.SUBMIT_TASK_DONE:
		local var_18_2 = arg_18_0.contextData.shipBluePrintVO

		if var_18_2 and var_18_2.isDeving() and var_18_2.isFinishedAllTasks():
			local var_18_3 = getProxy(TechnologyProxy)
			local var_18_4 = var_18_3.getBluePrintById(var_18_2.id)

			var_18_4.finish()
			var_18_3.updateBluePrint(var_18_4)
	elif var_18_0 == GAME.FINISH_SHIP_BLUEPRINT_DONE or var_18_0 == GAME.ITEM_LOCK_SHIP_BLUPRINT_DONE:
		arg_18_0.addSubLayers(Context.New({
			mediator = NewShipMediator,
			viewComponent = NewShipLayer,
			data = {
				ship = var_18_1.ship,
				canSkipBatch = var_18_1.canSkipBatch
			},
			def onRemoved:()
				pg.NewStoryMgr.GetInstance().Play("FANGAN2")
		}))
	elif GAME.STOP_BLUEPRINT_DONE == var_18_0:
		arg_18_0.viewComponent.clearTimers(var_18_1.id)
	elif GAME.MOD_BLUEPRINT_DONE == var_18_0:
		arg_18_0.viewComponent.doModAnim(var_18_1.oldBluePrint, var_18_1.newBluePrint)
		arg_18_0.viewComponent.updateAllPursuingCostTip()
	elif var_18_0 == BayProxy.SHIP_ADDED or BayProxy.SHIP_UPDATED == var_18_0:
		local var_18_5 = getProxy(BayProxy)

		arg_18_0.viewComponent.setShipVOs(var_18_5.getRawData())
	elif GAME.BUILD_SHIP_BLUEPRINT_DONE == var_18_0:
		arg_18_0.viewComponent.buildStartAni("researchStartWindow")
	elif var_18_0 == GAME.BEGIN_STAGE_DONE:
		arg_18_0.sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_18_1)
	elif var_18_0 == GAME.MOD_BLUEPRINT_ANIM_LOCK:
		arg_18_0.viewComponent.noUpdateMod = True
	elif var_18_0 == GAME.PURSUING_RESET_DONE:
		-- block empty
	elif var_18_0 == GAME.QUICK_EXCHANGE_BLUEPRINT_DONE:
		arg_18_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_18_1, function()
			arg_18_0.viewComponent.updateShipBluePrintVO())

return var_0_0
