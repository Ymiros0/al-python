local var_0_0 = class("NewBackYardShipInfoMediator", import("...base.ContextMediator"))

var_0_0.EXTEND = "NewBackYardShipInfoMediator.EXTEND"
var_0_0.OPEN_CHUANWU = "NewBackYardShipInfoMediator.OPEN_CHUANWU"
var_0_0.UPDATE_SHIPS = "NewBackYardShipInfoMediator.UPDATE_SHIPS"
var_0_0.LOOG_PRESS_SHIP = "NewBackYardShipInfoMediator.LOOG_PRESS_SHIP"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.EXTEND, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.SHOPPING, {
			count = 1,
			id = arg_2_1
		}))
	arg_1_0.bind(var_0_0.LOOG_PRESS_SHIP, function(arg_3_0, arg_3_1, arg_3_2)
		arg_1_0.contextData.type = arg_3_1

		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
			shipId = arg_3_2.id
		}))
	arg_1_0.bind(var_0_0.OPEN_CHUANWU, function(arg_4_0, arg_4_1, arg_4_2)
		arg_1_0.contextData.type = arg_4_1

		arg_1_0.OnSelShips(arg_4_1, arg_4_2))

def var_0_0.OnSelShips(arg_5_0, arg_5_1, arg_5_2):
	local var_5_0 = getProxy(DormProxy).getRawData()
	local var_5_1, var_5_2, var_5_3 = arg_5_0.GetSelectedShips(var_5_0, arg_5_1, arg_5_2)
	local var_5_4 = {
		callbackQuit = True,
		selectedMax = arg_5_0.GetMaxSel(var_5_0, arg_5_1),
		quitTeam = arg_5_2 != None,
		ignoredIds = pg.ShipFlagMgr.GetInstance().FilterShips({
			isActivityNpc = True
		}),
		selectedIds = var_5_3,
		preView = arg_5_0.viewComponent.__cname,
		hideTagFlags = ShipStatus.TAG_HIDE_BACKYARD,
		blockTagFlags = ShipStatus.TAG_BLOCK_BACKYARD,
		def onShip:(arg_6_0, arg_6_1, arg_6_2)
			return arg_5_0.OnShip(var_5_2, arg_6_0, arg_6_1, arg_6_2),
		def onSelected:(arg_7_0, arg_7_1)
			arg_5_0.OnSelected(arg_5_1, arg_5_2, arg_7_0, function()
				arg_5_0.sendNotification(var_0_0.UPDATE_SHIPS)
				arg_7_1()),
		priorEquipUpShipIDList = {}
	}

	for iter_5_0, iter_5_1 in pairs(var_5_1):
		table.insert(var_5_4.priorEquipUpShipIDList, iter_5_1)

	for iter_5_2, iter_5_3 in pairs(var_5_2):
		table.insert(var_5_4.priorEquipUpShipIDList, iter_5_3)

	var_5_4.leftTopWithFrameInfo = i18n("backyard_longpress_ship_tip")
	var_5_4.isLayer = True
	var_5_4.energyDisplay = True

	arg_5_0.addSubLayers(Context.New({
		viewComponent = DockyardScene,
		mediator = DockyardMediator,
		data = var_5_4
	}))

def var_0_0.GetMaxSel(arg_9_0, arg_9_1, arg_9_2):
	local var_9_0 = 0

	if arg_9_2 == Ship.STATE_TRAIN:
		var_9_0 = arg_9_1.exp_pos
	elif arg_9_2 == Ship.STATE_REST:
		var_9_0 = arg_9_1.rest_pos

	return var_9_0

def var_0_0.GetSelectedShips(arg_10_0, arg_10_1, arg_10_2, arg_10_3):
	local var_10_0 = arg_10_3 and arg_10_3.id or -1
	local var_10_1 = {}
	local var_10_2 = {}
	local var_10_3 = {}

	for iter_10_0, iter_10_1 in ipairs(arg_10_1.shipIds):
		local var_10_4 = getProxy(BayProxy).RawGetShipById(iter_10_1)

		if var_10_4.state == arg_10_2:
			table.insert(var_10_1, var_10_4.id)

			if var_10_4.id != var_10_0:
				table.insert(var_10_3, var_10_4.id)
		else
			table.insert(var_10_2, var_10_4.id)

	return var_10_1, var_10_2, var_10_3

def var_0_0.OnShip(arg_11_0, arg_11_1, arg_11_2, arg_11_3, arg_11_4):
	if #arg_11_4 > arg_11_0.contextData.MaxRsetPos:
		return False, i18n("backyard_no_pos_for_ship")

	if table.contains(arg_11_1, arg_11_2.id):
		return False, i18n("backyard_backyardShipInfoMediator_shipState_rest")

	local var_11_0, var_11_1 = ShipStatus.ShipStatusCheck("inBackyard", arg_11_2, function(arg_12_0)
		arg_11_3())

	return var_11_0, var_11_1

def var_0_0.OnSelected(arg_13_0, arg_13_1, arg_13_2, arg_13_3, arg_13_4):
	local var_13_0 = getProxy(DormProxy).getRawData().GetStateShipsById(arg_13_1)

	pg.UIMgr.GetInstance().LoadingOn()

	if arg_13_3 == None or #arg_13_3 == 0:
		if arg_13_2:
			arg_13_0.sendNotification(GAME.EXIT_SHIP, {
				shipId = arg_13_2.id,
				callback = arg_13_4
			})
		else
			arg_13_4()

		pg.UIMgr.GetInstance().LoadingOff()

		return

	local var_13_1 = {}

	for iter_13_0, iter_13_1 in pairs(var_13_0):
		if not table.contains(arg_13_3, iter_13_0):
			table.insert(var_13_1, function(arg_14_0)
				arg_13_0.sendNotification(GAME.EXIT_SHIP, {
					shipId = iter_13_0,
					callback = arg_14_0
				}))

	arg_13_0.contextData.shipIdToAdd = {}

	for iter_13_2, iter_13_3 in ipairs(arg_13_3):
		if not var_13_0[iter_13_3]:
			local var_13_2 = arg_13_1 == Ship.STATE_TRAIN and 1 or 2

			table.insert(arg_13_0.contextData.shipIdToAdd, {
				iter_13_3,
				var_13_2
			})

	if arg_13_0.contextData.shipIdToAdd and #arg_13_0.contextData.shipIdToAdd > 0:
		for iter_13_4, iter_13_5 in ipairs(arg_13_0.contextData.shipIdToAdd):
			table.insert(var_13_1, function(arg_15_0)
				arg_13_0.sendNotification(GAME.ADD_SHIP, {
					id = iter_13_5[1],
					type = iter_13_5[2],
					callBack = arg_15_0
				}))

	if #var_13_1 > 0:
		seriesAsync(var_13_1, function()
			arg_13_0.contextData.shipIdToAdd = None

			pg.UIMgr.GetInstance().LoadingOff()
			arg_13_4())
	else
		pg.UIMgr.GetInstance().LoadingOff()
		arg_13_4()

def var_0_0.listNotificationInterests(arg_17_0):
	return {
		GAME.EXTEND_BACKYARD_DONE,
		var_0_0.UPDATE_SHIPS
	}

def var_0_0.handleNotification(arg_18_0, arg_18_1):
	local var_18_0 = arg_18_1.getName()
	local var_18_1 = arg_18_1.getBody()

	if var_18_0 == GAME.EXTEND_BACKYARD_DONE:
		pg.TipsMgr.GetInstance().ShowTips(i18n("backyard_backyardShipInfoMediator_ok_unlock"))
		arg_18_0.viewComponent.UpdateSlots()
	elif var_18_0 == var_0_0.UPDATE_SHIPS:
		arg_18_0.viewComponent.UpdateSlots()

return var_0_0
