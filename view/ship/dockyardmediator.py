local var_0_0 = class("DockyardMediator", import("..base.ContextMediator"))

var_0_0.ON_DESTROY_SHIPS = "DockyardMediator.ON_DESTROY_SHIPS"
var_0_0.ON_SHIP_DETAIL = "DockyardMediator.ON_SHIP_DETAIL"
var_0_0.ON_SHIP_REPAIR = "DockyardMediator.ON_SHIP_REPAIR"
var_0_0.OPEN_DOCKYARD_INDEX = "DockyardMediator.OPEN_DOCKYARD_INDEX"

def var_0_0.register(arg_1_0):
	if arg_1_0.contextData.selectFriend:
		local var_1_0 = getProxy(FriendProxy).getAllFriends()

		arg_1_0.viewComponent.setFriends(var_1_0)

	local var_1_1 = getProxy(BayProxy)

	if arg_1_0.contextData.shipVOs:
		arg_1_0.shipsById = {}

		for iter_1_0, iter_1_1 in ipairs(arg_1_0.contextData.shipVOs):
			arg_1_0.shipsById[iter_1_1.id] = iter_1_1
	elif arg_1_0.contextData.mode == DockyardScene.MODE_WORLD:
		arg_1_0.shipsById = {}

		for iter_1_2, iter_1_3 in ipairs(nowWorld().GetShipVOs()):
			arg_1_0.shipsById[iter_1_3.id] = iter_1_3
	else
		arg_1_0.shipsById = {}

		for iter_1_4, iter_1_5 in pairs(var_1_1.data):
			arg_1_0.shipsById[iter_1_4] = iter_1_5

	if arg_1_0.contextData.mode == DockyardScene.MODE_MOD:
		local var_1_2 = arg_1_0.contextData.ignoredIds[1]

		arg_1_0.viewComponent.setModShip(arg_1_0.shipsById[var_1_2].clone())

	arg_1_0.fleetProxy = getProxy(FleetProxy)
	arg_1_0.fleetShipIds = arg_1_0.fleetProxy.getAllShipIds()

	if arg_1_0.contextData.ignoredIds:
		for iter_1_6, iter_1_7 in ipairs(arg_1_0.contextData.ignoredIds):
			arg_1_0.shipsById[iter_1_7] = None

	arg_1_0.viewComponent.setShips(arg_1_0.shipsById)
	arg_1_0.viewComponent.setShipsCount(var_1_1.getShipCount())

	local var_1_3 = getProxy(PlayerProxy).getData()

	arg_1_0.viewComponent.setPlayer(var_1_3)
	arg_1_0.bind(var_0_0.ON_DESTROY_SHIPS, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0.sendNotification(GAME.DESTROY_SHIPS, {
			destroyEquipment = arg_2_2,
			shipIds = arg_2_1
		}))
	arg_1_0.bind(var_0_0.ON_SHIP_DETAIL, function(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
			shipId = arg_3_1.id,
			shipVOs = arg_3_2,
			selectContextData = arg_3_3
		}))
	arg_1_0.bind(var_0_0.ON_SHIP_REPAIR, function(arg_4_0, arg_4_1, arg_4_2)
		arg_1_0.sendNotification(GAME.WORLD_SHIP_REPAIR, {
			shipIds = arg_4_1,
			totalCost = arg_4_2
		}))
	arg_1_0.bind(var_0_0.OPEN_DOCKYARD_INDEX, function(arg_5_0, arg_5_1)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = CustomIndexLayer,
			mediator = CustomIndexMediator,
			data = arg_5_1
		})))

def var_0_0.listNotificationInterests(arg_6_0):
	return {
		GAME.DESTROY_SHIP_DONE,
		FleetProxy.FLEET_UPDATED,
		GAME.EXIT_SHIP_DONE,
		GAME.UPDATE_EXERCISE_FLEET_DONE,
		GAME.CANCEL_LEARN_TACTICS_DONE,
		PlayerProxy.UPDATED,
		GAME.WORLD_SHIP_REPAIR_DONE,
		GAME.UPDATE_LOCK_DONE,
		GAME.WORLD_FLEET_REDEPLOY_DONE
	}

def var_0_0.handleNotification(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_1.getName()
	local var_7_1 = arg_7_1.getBody()

	if var_7_0 == GAME.DESTROY_SHIP_DONE:
		if not pg.m02.hasMediator(ShipMainMediator.__cname):
			pg.TipsMgr.GetInstance().ShowTips(i18n("ship_dockyardMediator_destroy"))

		for iter_7_0, iter_7_1 in ipairs(var_7_1.destroiedShipIds):
			arg_7_0.viewComponent.removeShip(iter_7_1)

		arg_7_0.viewComponent.updateShipCount()
		arg_7_0.viewComponent.setShipsCount(getProxy(BayProxy).getShipCount())
		arg_7_0.viewComponent.updateBarInfo()
		arg_7_0.viewComponent.updateSelected()
		arg_7_0.viewComponent.updateDestroyRes()

		local function var_7_2()
			if table.getCount(var_7_1.equipments) > 0:
				local var_8_0 = {}

				for iter_8_0, iter_8_1 in pairs(var_7_1.equipments):
					table.insert(var_8_0, iter_8_1)

				arg_7_0.addSubLayers(Context.New({
					viewComponent = ResolveEquipmentLayer,
					mediator = ResolveEquipmentMediator,
					data = {
						Equipments = var_8_0
					}
				}))

		arg_7_0.viewComponent.emit(BaseUI.ON_AWARD, {
			items = var_7_1.bonus,
			title = AwardInfoLayer.TITLE.ITEM,
			removeFunc = var_7_2
		})
		arg_7_0.viewComponent.closeDestroyPanel()
	elif var_7_0 == FleetProxy.FLEET_UPDATED:
		local var_7_3 = arg_7_0.fleetShipIds

		arg_7_0.fleetShipIds = arg_7_0.fleetProxy.getAllShipIds()

		local var_7_4 = {}

		for iter_7_2, iter_7_3 in ipairs(var_7_3):
			var_7_4[iter_7_3] = 1

		for iter_7_4, iter_7_5 in ipairs(arg_7_0.fleetShipIds):
			if var_7_4[iter_7_5] == 1:
				var_7_4[iter_7_5] = 2
			else
				var_7_4[iter_7_5] = 3

		for iter_7_6, iter_7_7 in ipairs(var_7_3):
			if var_7_4[iter_7_7] == 1:
				var_7_4[iter_7_7] = 0

		for iter_7_8, iter_7_9 in pairs(var_7_4):
			if iter_7_9 == 0:
				arg_7_0.setShipFlag(iter_7_8, "inFleet", False)
			elif iter_7_9 == 3:
				arg_7_0.setShipFlag(iter_7_8, "inFleet", True)

			arg_7_0.viewComponent.updateShipStatusById(iter_7_8)
	elif var_7_0 == GAME.EXIT_SHIP_DONE:
		arg_7_0.setShipFlag(var_7_1.id, "inBackyard", False)
		arg_7_0.viewComponent.updateShipStatusById(var_7_1.id)
	elif var_7_0 == GAME.UPDATE_LOCK_DONE:
		arg_7_0.shipsById[var_7_1.id].lockState = var_7_1.lockState

		arg_7_0.viewComponent.updateShipStatusById(var_7_1.id)
	elif var_7_0 == GAME.CANCEL_LEARN_TACTICS_DONE:
		arg_7_0.setShipFlag(var_7_1.shipId, "inTactics", False)
		arg_7_0.viewComponent.updateShipStatusById(var_7_1.shipId)
	elif var_7_0 == GAME.UPDATE_EXERCISE_FLEET_DONE:
		local var_7_5 = var_7_1.oldFleet
		local var_7_6 = var_7_1.newFleet

		for iter_7_10, iter_7_11 in ipairs(var_7_5.ships):
			arg_7_0.setShipFlag(iter_7_11, "inExercise", False)
			arg_7_0.viewComponent.updateShipStatusById(iter_7_11)

		for iter_7_12, iter_7_13 in ipairs(var_7_6.ships):
			arg_7_0.setShipFlag(iter_7_13, "inExercise", True)
			arg_7_0.viewComponent.updateShipStatusById(iter_7_13)
	elif var_7_0 == PlayerProxy.UPDATED:
		arg_7_0.viewComponent.setPlayer(var_7_1)
	elif var_7_0 == GAME.WORLD_SHIP_REPAIR_DONE:
		_.each(var_7_1.shipIds, function(arg_9_0)
			arg_7_0.viewComponent.updateShipStatusById(arg_9_0))
	elif var_7_0 == GAME.WORLD_FLEET_REDEPLOY_DONE:
		arg_7_0.viewComponent.emit(BaseUI.ON_BACK)

def var_0_0.setShipFlag(arg_10_0, arg_10_1, arg_10_2, arg_10_3):
	local var_10_0 = arg_10_0.shipsById[arg_10_1]

	if var_10_0:
		var_10_0[arg_10_2] = arg_10_3

return var_0_0
