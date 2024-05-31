local var_0_0 = class("CourtYardMediator", import("..base.ContextMediator"))

var_0_0.SET_UP = "CourtYardMediator.SET_UP"
var_0_0.RENAME = "CourtYardMediator.RENAME"
var_0_0.FOLD = "CourtYardMediator.FOLD"
var_0_0.SWITCH = "CourtYardMediator.SWITCH"
var_0_0.GO_SHOP = "CourtYardMediator.GO_SHOP"
var_0_0.OPEN_DECORATION = "CourtYardMediator.OPEN_DECORATION"
var_0_0.SEL_TRAIN_SHIP = "CourtYardMediator.SEL_TRAIN_SHIP"
var_0_0.SEL_REST_SHIP = "CourtYardMediator.SEL_REST_SHIP"
var_0_0.GO_GRANARY = "CourtYardMediator.GO_GRANARY"
var_0_0.OPEN_ADD_EXP = "CourtYardMediator.OPEN_ADD_EXP"
var_0_0.CLOSE_ADD_EXP = "CourtYardMediator.CLOSE_ADD_EXP"
var_0_0.UN_LOCK_2FLOOR = "CourtYardMediator.UN_LOCK_2FLOOR"
var_0_0.GO_THEME_TEMPLATE = "CourtYardMediator.GO_THEME_TEMPLATE"
var_0_0.ON_ADD_VISITOR_SHIP = "CourtYardMediator.ON_ADD_VISITOR_SHIP"
var_0_0.ONE_KEY = "CourtYardMediator.ONE_KEY"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ONE_KEY, function(arg_2_0)
		arg_1_0.sendNotification(GAME.BACKYARD_ONE_KEY))
	arg_1_0.bind(var_0_0.ON_ADD_VISITOR_SHIP, function(arg_3_0)
		local function var_3_0(arg_4_0)
			if arg_4_0:
				_courtyard.GetController().AddVisitorShip(arg_4_0)

		local var_3_1 = getProxy(DormProxy)
		local var_3_2 = var_3_1.GetVisitorShip()

		if var_3_2:
			var_3_0(var_3_2)

			return

		arg_1_0.sendNotification(GAME.BACKYARD_GET_VISITOR_SHIP, {
			def callback:()
				var_3_0(var_3_1.GetVisitorShip())
		}))
	arg_1_0.bind(var_0_0.GO_THEME_TEMPLATE, function(arg_6_0)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.BACKYARD_THEME_TEMPLATE))
	arg_1_0.bind(var_0_0.UN_LOCK_2FLOOR, function(arg_7_0, arg_7_1, arg_7_2)
		arg_1_0.sendNotification(GAME.SHOPPING, {
			id = arg_7_1,
			count = arg_7_2
		}))
	arg_1_0.bind(var_0_0.GO_GRANARY, function()
		arg_1_0.addSubLayers(Context.New({
			mediator = BackyardFeedMediator,
			viewComponent = BackyardFeedLayer
		})))
	arg_1_0.bind(var_0_0.SEL_TRAIN_SHIP, function(arg_9_0)
		local var_9_0 = _courtyard.GetController().GetMaxCntForShip()

		arg_1_0.addSubLayers(Context.New({
			mediator = NewBackYardShipInfoMediator,
			viewComponent = NewBackYardShipInfoLayer,
			data = {
				type = Ship.STATE_TRAIN,
				MaxRsetPos = var_9_0
			}
		})))
	arg_1_0.bind(var_0_0.SEL_REST_SHIP, function(arg_10_0)
		local var_10_0 = _courtyard.GetController().GetMaxCntForShip()

		arg_1_0.addSubLayers(Context.New({
			mediator = NewBackYardShipInfoMediator,
			viewComponent = NewBackYardShipInfoLayer,
			data = {
				type = Ship.STATE_REST,
				MaxRsetPos = var_10_0
			}
		})))
	arg_1_0.bind(var_0_0.GO_SHOP, function(arg_11_0, arg_11_1)
		local var_11_0 = arg_11_1 and {
			def onDeattch:()
				arg_1_0.viewComponent.emit(var_0_0.OPEN_DECORATION)
		}

		arg_1_0.addSubLayers(Context.New({
			mediator = NewBackYardShopMediator,
			viewComponent = NewBackYardShopLayer,
			data = var_11_0
		})))
	arg_1_0.bind(var_0_0.OPEN_DECORATION, function(arg_13_0)
		_courtyard.GetController().EnterEditMode())
	arg_1_0.bind(var_0_0.SWITCH, function(arg_14_0, arg_14_1)
		if getProxy(DormProxy).floor == arg_14_1:
			return

		_courtyard.Dispose()

		_courtyard = None

		gcAll()
		arg_1_0.viewComponent.emit(var_0_0.SET_UP, arg_14_1)
		arg_1_0.viewComponent.SwitchFloorDone())
	arg_1_0.bind(var_0_0.FOLD, function(arg_15_0, arg_15_1)
		arg_1_0.viewComponent.FoldPanel(arg_15_1))
	arg_1_0.bind(var_0_0.RENAME, function(arg_16_0, arg_16_1)
		arg_1_0.sendNotification(GAME.BACKYARD_RENAME, arg_16_1))
	arg_1_0.bind(var_0_0.SET_UP, function(arg_17_0, arg_17_1)
		getProxy(DormProxy).floor = arg_17_1
		arg_1_0.contextData.floor = arg_17_1
		_courtyard = CourtYardBridge.New(arg_1_0.GenCourtYardData(arg_17_1)))

	local var_1_0 = arg_1_0.contextData.dorm or getProxy(DormProxy).getRawData()

	arg_1_0.viewComponent.SetDorm(var_1_0)

def var_0_0.listNotificationInterests(arg_18_0):
	return {
		DormProxy.DORM_UPDATEED,
		DormProxy.INIMACY_AND_MONEY_ADD,
		DormProxy.SHIPS_EXP_ADDED,
		GAME.EXTEND_BACKYARD_AREA_DONE,
		GAME.BACKYARD_ADD_MONEY_DONE,
		GAME.BACKYARD_ADD_INTIMACY_DONE,
		GAME.BACKYARD_ONE_KEY_DONE,
		GAME.BACKYARD_SHIP_EXP_ADDED,
		GAME.OPEN_BACKYARD_SHOP,
		GAME.EXIT_SHIP_DONE,
		GAME.ADD_SHIP_DONE,
		GAME.LOAD_LAYERS,
		GAME.REMOVE_LAYERS,
		GAME.ON_APPLICATION_PAUSE,
		GAME.BUY_FURNITURE_DONE,
		GAME.ON_RECONNECTION,
		CourtYardEvent._EXTEND,
		CourtYardEvent._QUIT,
		CourtYardEvent._ENTER_MODE,
		CourtYardEvent._EXIT_MODE,
		CourtYardEvent._INITED,
		CourtYardEvent._NO_POS_TO_ADD_SHIP,
		CourtYardEvent._DRAG_ITEM,
		CourtYardEvent._DRAG_ITEM_END,
		CourtYardEvent._TOUCH_SHIP,
		CourtYardEvent._ADD_ITEM_FAILED,
		BackYardDecorationMediator.START_TAKE_THEME_PHOTO,
		BackYardDecorationMediator.END_TAKE_THEME_PHOTO
	}

def var_0_0.handleNotification(arg_19_0, arg_19_1):
	local var_19_0 = arg_19_1.getName()
	local var_19_1 = arg_19_1.getBody()
	local var_19_2 = arg_19_1.getType()

	if var_19_0 == DormProxy.SHIPS_EXP_ADDED:
		if arg_19_0.contextData.OpenShop:
			return

		if not CourtYardMediator.firstTimeAddExp and not pg.NewGuideMgr.GetInstance().IsBusy():
			CourtYardMediator.firstTimeAddExp = True

			arg_19_0.SettleExp(var_19_1)
		elif not arg_19_0.isTipFood:
			arg_19_0.viewComponent.ShowAddFoodTip()

		arg_19_0.isTipFood = True
	elif var_19_0 == GAME.LOAD_LAYERS:
		CourtYardMediator.firstTimeAddExp = True
	elif var_19_0 == GAME.REMOVE_LAYERS:
		arg_19_0.viewComponent.OnRemoveLayer(var_19_1)
	elif var_19_0 == CourtYardEvent._NO_POS_TO_ADD_SHIP:
		arg_19_0.sendNotification(GAME.EXIT_SHIP, {
			shipId = var_19_1
		})
		pg.TipsMgr.GetInstance().ShowTips(i18n("backyard_notPosition_shipExit"))
		arg_19_0.viewComponent.UpdateDorm(getProxy(DormProxy).getRawData(), BackYardConst.DORM_UPDATE_TYPE_SHIP)
	elif var_19_0 == CourtYardEvent._ADD_ITEM_FAILED:
		getProxy(DormProxy).getRawData().GetTheme(getProxy(DormProxy).floor).DeleteFurniture(var_19_1)

	arg_19_0.handleCourtyardNotification(var_19_0, var_19_1, var_19_2)

def var_0_0.handleCourtyardNotification(arg_20_0, arg_20_1, arg_20_2, arg_20_3):
	if not _courtyard or not _courtyard.IsLoaed():
		return

	if arg_20_1 == CourtYardEvent._QUIT:
		arg_20_0.viewComponent.emit(BaseUI.ON_BACK)
	elif arg_20_1 == CourtYardEvent._INITED:
		arg_20_0.viewComponent.OnCourtYardLoaded()
	elif arg_20_1 == GAME.LOAD_LAYERS:
		local var_20_0 = arg_20_2.context.mediator == NewBackYardShipInfoMediator

		_courtyard.GetController().OnOpenLayerOrCloseLayer(True, var_20_0)
	elif arg_20_1 == GAME.REMOVE_LAYERS:
		local var_20_1 = arg_20_2.context.mediator == NewBackYardShipInfoMediator

		_courtyard.GetController().OnOpenLayerOrCloseLayer(False, var_20_1)
	elif arg_20_1 == GAME.ON_APPLICATION_PAUSE and arg_20_2:
		_courtyard.GetController().OnApplicationPaused()

	if arg_20_0.contextData.mode == CourtYardConst.SYSTEM_VISIT:
		return

	if arg_20_1 == GAME.BACKYARD_ADD_MONEY_DONE:
		_courtyard.GetController().ClearShipCoin(arg_20_2.id)
	elif arg_20_1 == GAME.EXIT_SHIP_DONE:
		_courtyard.GetController().ExitShip(arg_20_2.id)
	elif arg_20_1 == GAME.BUY_FURNITURE_DONE:
		arg_20_0.viewComponent.OnAddFurniture()
	elif arg_20_1 == GAME.ON_RECONNECTION:
		arg_20_0.viewComponent.OnReconnection()
	elif arg_20_1 == GAME.ADD_SHIP_DONE:
		local var_20_2 = getProxy(BayProxy).getShipById(arg_20_2.id)

		if ({
			Ship.STATE_TRAIN,
			Ship.STATE_REST
		})[getProxy(DormProxy).floor] == var_20_2.state:
			_courtyard.GetController().AddShip(var_20_2)
	elif arg_20_1 == GAME.BACKYARD_ADD_INTIMACY_DONE:
		_courtyard.GetController().ClearShipIntimacy(arg_20_2.id)
	elif arg_20_1 == GAME.BACKYARD_ONE_KEY_DONE:
		for iter_20_0, iter_20_1 in ipairs(arg_20_2.shipIds):
			_courtyard.GetController().ClearShipCoin(iter_20_1)
			_courtyard.GetController().ClearShipIntimacy(iter_20_1)
	elif arg_20_1 == GAME.EXTEND_BACKYARD_AREA_DONE:
		_courtyard.GetController().LevelUp()
	elif arg_20_1 == DormProxy.INIMACY_AND_MONEY_ADD:
		local var_20_3 = arg_20_2.id
		local var_20_4 = arg_20_2.money
		local var_20_5 = arg_20_2.intimacy

		_courtyard.GetController().UpdateShipCoinAndIntimacy(var_20_3, var_20_4, var_20_5)
	elif arg_20_1 == GAME.BACKYARD_SHIP_EXP_ADDED:
		_courtyard.GetController().AddShipExp(arg_20_2.id, arg_20_2.exp)
	elif arg_20_1 == DormProxy.DORM_UPDATEED:
		arg_20_0.viewComponent.UpdateDorm(getProxy(DormProxy).getRawData(), arg_20_3)
	elif arg_20_1 == CourtYardEvent._ENTER_MODE:
		arg_20_0.addSubLayers(Context.New({
			mediator = BackYardDecorationMediator,
			viewComponent = BackYardDecrationLayer
		}))
		arg_20_0.viewComponent.OnEnterOrExitEdit(True)
	elif arg_20_1 == CourtYardEvent._EXIT_MODE:
		arg_20_0.viewComponent.OnEnterOrExitEdit(False)
	elif arg_20_1 == GAME.OPEN_BACKYARD_SHOP:
		arg_20_0.viewComponent.emit(var_0_0.GO_SHOP, True)
	elif arg_20_1 == CourtYardEvent._EXTEND:
		arg_20_0.OnExtend()
	elif arg_20_1 == BackYardDecorationMediator.START_TAKE_THEME_PHOTO:
		GetOrAddComponent(arg_20_0.viewComponent.mainTF, typeof(CanvasGroup)).alpha = 0

		_courtyard.GetController().OnTakeThemePhoto()
	elif arg_20_1 == BackYardDecorationMediator.END_TAKE_THEME_PHOTO:
		GetOrAddComponent(arg_20_0.viewComponent.mainTF, typeof(CanvasGroup)).alpha = 1

		_courtyard.GetController().OnEndTakeThemePhoto()
	elif arg_20_1 == CourtYardEvent._DRAG_ITEM:
		arg_20_0.viewComponent.BlockEvents()
	elif arg_20_1 == CourtYardEvent._DRAG_ITEM_END:
		arg_20_0.viewComponent.UnBlockEvents()
	elif arg_20_1 == CourtYardEvent._TOUCH_SHIP:
		local var_20_6 = getProxy(TaskProxy).GetBackYardInterActionTaskList()

		if var_20_6 and #var_20_6 > 0:
			for iter_20_2, iter_20_3 in ipairs(var_20_6):
				pg.m02.sendNotification(GAME.UPDATE_TASK_PROGRESS, {
					taskId = iter_20_3.id
				})

def var_0_0.SettleExp(arg_21_0, arg_21_1):
	if arg_21_0.contextData.mode == CourtYardConst.SYSTEM_VISIT:
		return

	local var_21_0 = getProxy(DormProxy).getRawData()
	local var_21_1 = getProxy(BayProxy)
	local var_21_2 = 0

	for iter_21_0, iter_21_1 in ipairs(var_21_0.shipIds):
		local var_21_3 = var_21_1.RawGetShipById(iter_21_1)

		if var_21_3 and var_21_3.state == Ship.STATE_TRAIN:
			var_21_2 = var_21_2 + 1

	local var_21_4 = var_21_0.load_exp * var_21_2

	if var_21_2 != 0 and (var_21_4 != 0 or var_21_0.food != 0):
		onNextTick(function()
			arg_21_0.addSubLayers(Context.New({
				mediator = BackYardSettlementMediator,
				viewComponent = BackYardSettlementLayer,
				data = {
					oldShips = arg_21_1.oldShips,
					newShips = arg_21_1.newShips
				}
			})))

		arg_21_0.contextData.settleShipExp = True

def var_0_0.OnExtend(arg_23_0):
	if getProxy(BagProxy).getItemCountById(ITEM_BACKYARD_AREA_EXTEND) <= 0:
		local var_23_0 = getProxy(DormProxy).getRawData().GetExpandId()
		local var_23_1 = pg.shop_template[var_23_0]
		local var_23_2 = Drop.New({
			type = DROP_TYPE_RESOURCE,
			id = var_23_1.resource_type
		}).getName()

		_BackyardMsgBoxMgr.Show({
			content = i18n("backyard_buyExtendItem_question", var_23_1.resource_num .. var_23_2),
			def onYes:()
				arg_23_0.sendNotification(GAME.SHOPPING, {
					count = 1,
					id = var_23_0
				})
		})
	else
		arg_23_0.sendNotification(GAME.USE_ITEM, {
			count = 1,
			id = ITEM_BACKYARD_AREA_EXTEND
		})

def var_0_0.remove(arg_25_0):
	if _courtyard:
		_courtyard.Dispose()

		_courtyard = None

def var_0_0.GenCourtYardData(arg_26_0, arg_26_1):
	local var_26_0 = arg_26_0.contextData.mode or CourtYardConst.SYSTEM_DEFAULT
	local var_26_1
	local var_26_2

	if var_26_0 == CourtYardConst.SYSTEM_VISIT:
		var_26_1 = arg_26_0.contextData.dorm
		var_26_2 = CourtYardConst.STYLE_INNER
	elif var_26_0 == CourtYardConst.SYSTEM_DEFAULT:
		var_26_1 = getProxy(DormProxy).getRawData()
		var_26_2 = CourtYardConst.STYLE_INNER
	elif var_26_0 == CourtYardConst.SYSTEM_FEAST:
		var_26_1 = getProxy(FeastProxy).getRawData()
		var_26_2 = CourtYardConst.STYLE_FEAST
	elif var_26_0 == CourtYardConst.SYSTEM_OUTSIDE:
		assert(False)

		var_26_2 = CourtYardConst.STYLE_OUTSIDE
	elif var_26_0 == CourtYardConst.SYSTEM_EDIT_FEAST:
		var_26_1 = getProxy(DormProxy).getRawData()
		var_26_2 = CourtYardConst.STYLE_FEAST

	local var_26_3 = var_26_1.GetMapSize()

	if var_26_0 == CourtYardConst.SYSTEM_EDIT_FEAST:
		var_26_3 = getProxy(FeastProxy).getRawData().GetMapSize()

	local var_26_4 = {
		[arg_26_1] = {
			id = arg_26_1,
			level = var_26_1.level,
			furnitures = var_26_1.GetPutFurnitureList(arg_26_1),
			ships = var_26_1.GetPutShipList(arg_26_1)
		}
	}

	return {
		system = var_26_0,
		storeys = var_26_4,
		storeyId = arg_26_1,
		style = var_26_2,
		mapSize = var_26_3,
		name = arg_26_0.viewComponent.getUIName(),
		core = pg.m02
	}

return var_0_0
