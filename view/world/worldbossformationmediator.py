local var_0_0 = class("WorldBossFormationMediator", import("..base.ContextMediator"))

var_0_0.ON_START = "WorldBossFormationMediator.ON_START"
var_0_0.ON_COMMIT_EDIT = "WorldBossFormationMediator.ON_COMMIT_EDIT"
var_0_0.OPEN_SHIP_INFO = "WorldBossFormationMediator.OPEN_SHIP_INFO"
var_0_0.REMOVE_SHIP = "WorldBossFormationMediator.REMOVE_SHIP"
var_0_0.CHANGE_FLEET_SHIP = "WorldBossFormationMediator.CHANGE_FLEET_SHIPs"
var_0_0.ON_AUTO = "WorldBossFormationMediator.ON_AUTO"
var_0_0.CHANGE_FLEET_SHIPS_ORDER = "WorldBossFormationMediator.CHANGE_FLEET_SHIPS_ORDER"

def var_0_0.register(arg_1_0):
	local var_1_0 = getProxy(BayProxy)

	arg_1_0.ships = var_1_0.getRawData()

	arg_1_0.viewComponent.SetShips(arg_1_0.ships)

	local var_1_1 = nowWorld().GetBossProxy()
	local var_1_2 = arg_1_0.contextData.editingFleetVO or Clone(var_1_1.GetFleet(arg_1_0.contextData.bossId))

	arg_1_0.viewComponent.SetBossProxy(var_1_1, arg_1_0.contextData.bossId)
	var_1_1.LockCacheBoss(arg_1_0.contextData.bossId)
	arg_1_0.viewComponent.SetCurrentFleet(var_1_2)

	local var_1_3 = getProxy(PlayerProxy).getData()

	arg_1_0.viewComponent.SetPlayerInfo(var_1_3)
	arg_1_0.bind(var_0_0.REMOVE_SHIP, function(arg_2_0, arg_2_1, arg_2_2)
		if not arg_2_2.canRemove(arg_2_1):
			local var_2_0, var_2_1 = arg_2_2.getShipPos(arg_2_1)

			pg.TipsMgr.GetInstance().ShowTips(i18n("ship_formationUI_removeError_onlyShip", arg_2_1.getConfigTable().name, arg_2_2.name, Fleet.C_TEAM_NAME[var_2_1]))

			return

		arg_2_2.removeShip(arg_2_1)
		arg_1_0.viewComponent.UpdateFleetView(True))
	arg_1_0.bind(var_0_0.CHANGE_FLEET_SHIPS_ORDER, function(arg_3_0, arg_3_1)
		arg_1_0.viewComponent.UpdateFleetView())
	arg_1_0.bind(var_0_0.OPEN_SHIP_INFO, function(arg_4_0, arg_4_1, arg_4_2)
		arg_1_0.contextData.form = PreCombatLayer.FORM_EDIT

		local var_4_0 = arg_1_0.viewComponent._currentFleetVO
		local var_4_1 = {}

		for iter_4_0, iter_4_1 in ipairs(arg_4_2.ships):
			table.insert(var_4_1, arg_1_0.ships[iter_4_1])

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
			shipId = arg_4_1,
			shipVOs = var_4_1
		}))
	arg_1_0.bind(var_0_0.ON_COMMIT_EDIT, function(arg_5_0, arg_5_1)
		local var_5_0 = arg_1_0.viewComponent._currentFleetVO

		var_1_1.UpdateFleet(arg_1_0.contextData.bossId, var_5_0)
		var_1_1.SavaCacheShips(arg_1_0.contextData.bossId, var_5_0)
		arg_5_1())
	arg_1_0.bind(var_0_0.ON_AUTO, function(arg_6_0, arg_6_1)
		arg_1_0.onAutoBtn(arg_6_1))
	arg_1_0.bind(var_0_0.ON_START, function(arg_7_0)
		local var_7_0, var_7_1 = var_1_1.GetFleet(arg_1_0.contextData.bossId).isLegalToFight()

		if var_7_0 != True:
			pg.TipsMgr.GetInstance().ShowTips(i18n("elite_disable_no_fleet"))

			return

		local var_7_2 = nowWorld().GetBossProxy().GetBossById(arg_1_0.contextData.bossId)

		if not var_7_2:
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_joint_boss_not_found"))

			return

		if arg_1_0.contextData.isOther and var_1_1.GetPt() <= 0 and WorldBossConst._IsCurrBoss(var_7_2):
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_joint_count_no_enough"))

			return

		if arg_1_0.contextData.isOther:
			WorldBossScene.inOtherBossBattle = arg_1_0.contextData.bossId

		arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
			actId = 0,
			bossId = arg_1_0.contextData.bossId,
			system = SYSTEM_WORLD_BOSS
		}))
	arg_1_0.bind(var_0_0.CHANGE_FLEET_SHIP, function(arg_8_0, arg_8_1, arg_8_2, arg_8_3)
		arg_1_0.contextData.form = WorldBossFormationLayer.FORM_EDIT
		CurrentWorldBossDetailPage.formDock = True

		local var_8_0 = tobool(arg_8_1)
		local var_8_1 = arg_8_1 and arg_8_1.id or None
		local var_8_2 = arg_8_2.ships or {}

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
			selectedMin = 1,
			selectedMax = 1,
			ignoredIds = var_8_2,
			leastLimitMsg = i18n("ship_formationMediator_leastLimit"),
			quitTeam = var_8_0,
			teamFilter = arg_8_3,
			leftTopInfo = i18n("word_formation"),
			def onShip:(arg_9_0)
				if _.any(arg_8_2.ships, function(arg_10_0)
					return arg_9_0.isSameKind(var_1_0.getShipById(arg_10_0))):
					return False, i18n("event_same_type_not_allowed")

				return True,
			def onSelected:(arg_11_0)
				local var_11_0 = arg_11_0[1]
				local var_11_1 = getProxy(BayProxy).getShipById(var_11_0)

				if var_11_1 and var_1_2.containShip(var_11_1):
					return

				if var_8_1 == None:
					arg_8_2.insertShip(var_11_1, None, arg_8_3)
				else
					local var_11_2 = var_1_2.getShipPos(arg_8_1)

					arg_8_2.removeShipById(var_8_1)

					if var_11_1 and var_11_2:
						arg_8_2.insertShip(var_11_1, var_11_2, arg_8_3),
			preView = arg_1_0.viewComponent.__cname,
			hideTagFlags = ShipStatus.TAG_HIDE_ALL
		}))

def var_0_0.onAutoBtn(arg_12_0, arg_12_1):
	local var_12_0 = arg_12_1.isOn
	local var_12_1 = arg_12_1.toggle

	arg_12_0.sendNotification(GAME.AUTO_BOT, {
		isActiveBot = var_12_0,
		toggle = var_12_1,
		system = SYSTEM_WORLD
	})

def var_0_0.listNotificationInterests(arg_13_0):
	return {
		GAME.BEGIN_STAGE_DONE,
		GAME.WORLD_BOSS_START_BATTLE_FIALED,
		PlayerProxy.UPDATED,
		GAME.END_GUIDE
	}

def var_0_0.handleNotification(arg_14_0, arg_14_1):
	local var_14_0 = arg_14_1.getName()
	local var_14_1 = arg_14_1.getBody()

	if var_14_0 == GAME.BEGIN_STAGE_DONE:
		arg_14_0.sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_14_1)
	elif var_14_0 == GAME.WORLD_BOSS_START_BATTLE_FIALED:
		arg_14_0.viewComponent.emit(BaseUI.ON_CLOSE)
	elif var_14_0 == PlayerProxy.UPDATED:
		arg_14_0.viewComponent.SetPlayerInfo(getProxy(PlayerProxy).getData())
	elif var_14_0 == GAME.END_GUIDE:
		arg_14_0.viewComponent.TryPlayGuide()

return var_0_0
