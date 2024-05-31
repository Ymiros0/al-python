local var_0_0 = class("WorldFleetSelectMediator", import("..base.ContextMediator"))

var_0_0.OnSelectShip = "WorldFleetSelectMediator.OnSelectShip"
var_0_0.OnGO = "WorldFleetSelectMediator.OnGO"
var_0_0.OnShipDetail = "WorldFleetSelectMediator.OnShipDetail"
var_0_0.OnSelectEliteCommander = "WorldFleetSelectMediator.OnSelectEliteCommander"
var_0_0.OnCommanderFormationOp = "WorldFleetSelectMediator.OnCommanderFormationOp"
var_0_0.OnCommanderSkill = "WorldFleetSelectMediator.OnCommanderSkill"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.OnSelectShip, function(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
		local var_2_0 = tobool(arg_2_2[arg_2_3])
		local var_2_1 = {}

		for iter_2_0, iter_2_1 in pairs(arg_1_0.contextData.fleets):
			for iter_2_2, iter_2_3 in ipairs(iter_2_1):
				for iter_2_4 = 1, 3:
					if iter_2_3[arg_2_1][iter_2_4]:
						table.insert(var_2_1, iter_2_3[arg_2_1][iter_2_4])

		local var_2_2, var_2_3, var_2_4 = arg_1_0.GetDockCallbackFuncs(arg_2_2, arg_2_3, var_2_1)

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
			selectedMax = 1,
			useBlackBlock = True,
			selectedMin = 0,
			leastLimitMsg = i18n("ship_formationMediator_leastLimit"),
			quitTeam = var_2_0,
			teamFilter = arg_2_1,
			leftTopInfo = i18n("word_formation"),
			onShip = var_2_2,
			confirmSelect = var_2_3,
			onSelected = var_2_4,
			hideTagFlags = ShipStatus.TAG_HIDE_WORLD,
			otherSelectedIds = var_2_1
		}))
	arg_1_0.bind(var_0_0.OnGO, function(arg_3_0)
		local var_3_0 = nowWorld()
		local var_3_1 = arg_1_0.contextData.fleets

		if arg_1_0.contextData.mapId:
			arg_1_0.sendNotification(GAME.WORLD_ACTIVATE, {
				id = arg_1_0.contextData.mapId,
				enter_map_id = arg_1_0.contextData.entranceId,
				elite_fleet_list = var_3_0.FormationIds2NetIds(var_3_1),
				camp = var_3_0.GetRealm()
			})
		else
			local var_3_2 = {}

			if not var_3_0.CompareRedeploy(var_3_1):
				table.insert(var_3_2, function(arg_4_0)
					pg.MsgboxMgr.GetInstance().ShowMsgBox({
						content = i18n("world_redeploy_not_change"),
						onYes = arg_4_0
					}))

			table.insert(var_3_2, function(arg_5_0)
				local var_5_0 = var_3_0.CalcOrderCost(WorldConst.OpReqRedeploy)
				local var_5_1 = var_3_0.staminaMgr.GetTotalStamina()

				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("world_redeploy_cost_tip", setColorStr(var_5_0, COLOR_GREEN), setColorStr(var_5_1, var_5_0 <= var_5_1 and COLOR_GREEN or COLOR_RED)),
					def onYes:()
						if var_3_0.staminaMgr.GetTotalStamina() < var_5_0:
							var_3_0.staminaMgr.Show()
						else
							arg_5_0()
				}))
			seriesAsync(var_3_2, function()
				arg_1_0.sendNotification(GAME.WORLD_FLEET_REDEPLOY, {
					elite_fleet_list = var_3_0.FormationIds2NetIds(var_3_1)
				})))
	arg_1_0.bind(var_0_0.OnShipDetail, function(arg_8_0, arg_8_1)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
			shipId = arg_8_1.shipId,
			shipVOs = arg_8_1.shipVOs
		}))
	arg_1_0.bind(var_0_0.OnCommanderFormationOp, function(arg_9_0, arg_9_1)
		arg_1_0.sendNotification(GAME.COMMANDER_FORMATION_OP, {
			data = arg_9_1
		}))
	arg_1_0.bind(var_0_0.OnCommanderSkill, function(arg_10_0, arg_10_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = CommanderSkillMediator,
			viewComponent = CommanderSkillLayer,
			data = {
				isWorld = True,
				skill = arg_10_1
			}
		})))
	arg_1_0.bind(var_0_0.OnSelectEliteCommander, function(arg_11_0, arg_11_1, arg_11_2, arg_11_3)
		local var_11_0 = arg_1_0.contextData.fleets[arg_11_1][arg_11_2]
		local var_11_1 = Fleet.New({
			ship_list = {},
			commanders = var_11_0.commanders
		})
		local var_11_2 = var_11_1.getCommanders()

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.COMMANDERCAT, {
			maxCount = 1,
			mode = CommanderCatScene.MODE_SELECT,
			fleetType = CommanderCatScene.FLEET_TYPE_WORLD,
			fleets = arg_1_0.contextData.fleets,
			activeCommander = var_11_2[arg_11_3],
			ignoredIds = {},
			def onCommander:(arg_12_0)
				return True,
			def onSelected:(arg_13_0, arg_13_1)
				local var_13_0 = arg_13_0[1]
				local var_13_1 = getProxy(CommanderProxy).getCommanderById(var_13_0)

				for iter_13_0, iter_13_1 in pairs(arg_1_0.contextData.fleets):
					for iter_13_2, iter_13_3 in ipairs(iter_13_1):
						if iter_13_0 == arg_11_1 and iter_13_2 == arg_11_2:
							for iter_13_4, iter_13_5 in pairs(var_11_2):
								if iter_13_5.groupId == var_13_1.groupId and iter_13_4 != arg_11_3:
									pg.TipsMgr.GetInstance().ShowTips(i18n("commander_can_not_select_same_group"))

									return
						else
							for iter_13_6, iter_13_7 in pairs(iter_13_3.commanders):
								if var_13_0 == iter_13_7.id:
									pg.TipsMgr.GetInstance().ShowTips(i18n("commander_is_in_fleet_already"))

									return

				var_11_1.updateCommanderByPos(arg_11_3, var_13_1)

				var_11_0.commanders = var_11_1.outputCommanders()

				arg_13_1(),
			def onQuit:(arg_14_0)
				var_11_1.updateCommanderByPos(arg_11_3, None)

				var_11_0.commanders = var_11_1.outputCommanders()

				arg_14_0()
		})

		arg_1_0.contextData.editFleet = True)

	local var_1_0 = getProxy(CommanderProxy).getPrefabFleet()

	arg_1_0.viewComponent.setCommanderPrefabs(var_1_0)

def var_0_0.listNotificationInterests(arg_15_0):
	return {
		GAME.WORLD_ACTIVATE_DONE,
		GAME.WORLD_FLEET_REDEPLOY_DONE,
		CommanderProxy.PREFAB_FLEET_UPDATE,
		GAME.COMMANDER_WORLD_FORMATION_OP_DONE
	}

def var_0_0.handleNotification(arg_16_0, arg_16_1):
	local var_16_0 = arg_16_1.getName()
	local var_16_1 = arg_16_1.getBody()

	if var_16_0 == GAME.WORLD_ACTIVATE_DONE:
		local var_16_2 = nowWorld()
		local var_16_3 = {}

		if var_16_2.IsSystemOpen(WorldConst.SystemDailyTask):
			table.insert(var_16_3, function(arg_17_0)
				var_16_2.GetTaskProxy().checkDailyTask(arg_17_0))

		seriesAsync(var_16_3, function()
			arg_16_0.SetFleetSuccess())
	elif var_16_0 == GAME.WORLD_FLEET_REDEPLOY_DONE:
		arg_16_0.SetFleetSuccess()
	elif var_16_0 == CommanderProxy.PREFAB_FLEET_UPDATE:
		local var_16_4 = getProxy(CommanderProxy).getPrefabFleet()

		arg_16_0.viewComponent.setCommanderPrefabs(var_16_4)
		arg_16_0.viewComponent.updateCommanderPrefab()
	elif var_16_0 == GAME.COMMANDER_WORLD_FORMATION_OP_DONE:
		arg_16_0.viewComponent.UpdateFleets()
		arg_16_0.viewComponent.updateCommanderFleet(var_16_1.fleet)

def var_0_0.GetDockCallbackFuncs(arg_19_0, arg_19_1, arg_19_2, arg_19_3):
	local var_19_0 = getProxy(BayProxy)

	local function var_19_1(arg_20_0, arg_20_1)
		local var_20_0, var_20_1 = ShipStatus.ShipStatusCheck("inWorld", arg_20_0, arg_20_1)

		if not var_20_0:
			return var_20_0, var_20_1

		for iter_20_0, iter_20_1 in ipairs(arg_19_3):
			if arg_20_0.id != iter_20_1 and arg_20_0.isSameKind(var_19_0.getShipById(iter_20_1)):
				return False, i18n("event_same_type_not_allowed")

		return True

	local function var_19_2(arg_21_0, arg_21_1, arg_21_2)
		arg_21_1()

	local function var_19_3(arg_22_0)
		for iter_22_0, iter_22_1 in pairs(arg_19_0.contextData.fleets):
			for iter_22_2, iter_22_3 in ipairs(iter_22_1):
				for iter_22_4, iter_22_5 in pairs(iter_22_3):
					for iter_22_6 = 3, 1, -1:
						if arg_19_1 == iter_22_5 and iter_22_6 == arg_19_2:
							iter_22_5[iter_22_6] = arg_22_0[1]
						elif iter_22_5[iter_22_6] == arg_22_0[1]:
							iter_22_5[iter_22_6] = None

	return var_19_1, var_19_2, var_19_3

def var_0_0.SetFleetSuccess(arg_23_0):
	local var_23_0 = {
		inPort = True
	}

	if arg_23_0.contextData.mapId and nowWorld().IsReseted():
		var_23_0 = {
			inShop = True
		}

	local var_23_1 = getProxy(ContextProxy).getContextByMediator(WorldMediator)

	if var_23_1:
		var_23_1.extendData(var_23_0)
		arg_23_0.viewComponent.closeView()
	else
		arg_23_0.sendNotification(GAME.CHANGE_SCENE, SCENE.WORLD, var_23_0)

return var_0_0
