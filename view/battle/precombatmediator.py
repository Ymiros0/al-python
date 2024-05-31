local var_0_0 = class("PreCombatMediator", import("..base.ContextMediator"))

var_0_0.ON_START = "PreCombatMediator.ON_START"
var_0_0.ON_CHANGE_FLEET = "PreCombatMediator.ON_CHANGE_FLEET"
var_0_0.ON_COMMIT_EDIT = "PreCombatMediator.ON_COMMIT_EDIT"
var_0_0.ON_ABORT_EDIT = "PreCombatMediator.ON_ABORT_EDIT"
var_0_0.OPEN_SHIP_INFO = "PreCombatMediator.OPEN_SHIP_INFO"
var_0_0.REMOVE_SHIP = "PreCombatMediator.REMOVE_SHIP"
var_0_0.CHANGE_FLEET_SHIPS_ORDER = "PreCombatMediator.CHANGE_FLEET_SHIPS_ORDER"
var_0_0.CHANGE_FLEET_SHIP = "PreCombatMediator.CHANGE_FLEET_SHIP"
var_0_0.BEGIN_STAGE_PROXY = "PreCombatMediator.BEGIN_STAGE_PROXY"
var_0_0.SHOW_CONTINUOUS_OPERATION_WINDOW = "PreCombatMediator.SHOW_CONTINUOUS_OPERATION_WINDOW"
var_0_0.CONTINUOUS_OPERATION = "PreCombatMediator.CONTINUOUS_OPERATION"
var_0_0.ON_AUTO = "PreCombatMediator.ON_AUTO"
var_0_0.ON_SUB_AUTO = "PreCombatMediator.ON_SUB_AUTO"

def var_0_0.register(arg_1_0):
	arg_1_0.bindEvent()

	arg_1_0.ships = getProxy(BayProxy).getRawData()

	arg_1_0.viewComponent.SetShips(arg_1_0.ships)

	local var_1_0 = arg_1_0.contextData.system
	local var_1_1 = getProxy(FleetProxy)
	local var_1_2 = var_1_1.getData()

	if var_1_1.EdittingFleet != None:
		var_1_2[var_1_1.EdittingFleet.id] = var_1_1.EdittingFleet

	arg_1_0.fleets = var_1_2

	arg_1_0.viewComponent.SetFleets(var_1_2)

	local var_1_3 = getProxy(PlayerProxy)
	local var_1_4 = var_1_3.getData()

	arg_1_0.viewComponent.SetPlayerInfo(var_1_4)

	if var_1_0 == SYSTEM_DUEL:
		arg_1_0.viewComponent.SetCurrentFleet(FleetProxy.PVP_FLEET_ID)
	elif var_1_0 == SYSTEM_SUB_ROUTINE:
		arg_1_0.viewComponent.SetStageID(arg_1_0.contextData.stageId)
		arg_1_0.viewComponent.SetCurrentFleet(arg_1_0.contextData.subFleetId)
	else
		arg_1_0.viewComponent.SetStageID(arg_1_0.contextData.stageId)
		arg_1_0.viewComponent.SetCurrentFleet(var_1_3.combatFleetId)

def var_0_0.bindEvent(arg_2_0):
	local var_2_0 = arg_2_0.contextData.system

	arg_2_0.bind(var_0_0.ON_ABORT_EDIT, function(arg_3_0)
		local var_3_0 = getProxy(FleetProxy)

		var_3_0.abortEditting()
		var_3_0.syncFleet())
	arg_2_0.bind(var_0_0.ON_CHANGE_FLEET, function(arg_4_0, arg_4_1)
		arg_2_0.changeFleet(arg_4_1))
	arg_2_0.bind(var_0_0.ON_AUTO, function(arg_5_0, arg_5_1)
		arg_2_0.onAutoBtn(arg_5_1))
	arg_2_0.bind(var_0_0.ON_SUB_AUTO, function(arg_6_0, arg_6_1)
		arg_2_0.onAutoSubBtn(arg_6_1))
	arg_2_0.bind(var_0_0.CHANGE_FLEET_SHIPS_ORDER, function(arg_7_0, arg_7_1)
		arg_2_0.refreshEdit(arg_7_1))
	arg_2_0.bind(var_0_0.REMOVE_SHIP, function(arg_8_0, arg_8_1, arg_8_2)
		FormationMediator.removeShipFromFleet(arg_8_2, arg_8_1)
		arg_2_0.refreshEdit(arg_8_2))
	arg_2_0.bind(var_0_0.OPEN_SHIP_INFO, function(arg_9_0, arg_9_1, arg_9_2)
		arg_2_0.contextData.form = PreCombatLayer.FORM_EDIT

		local var_9_0 = {}

		for iter_9_0, iter_9_1 in ipairs(arg_9_2.getShipIds()):
			table.insert(var_9_0, arg_2_0.ships[iter_9_1])

		arg_2_0.sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
			shipId = arg_9_1,
			shipVOs = var_9_0
		}))
	arg_2_0.bind(var_0_0.CHANGE_FLEET_SHIP, function(arg_10_0, arg_10_1, arg_10_2, arg_10_3)
		assert(arg_10_2.id != FleetProxy.PVP_FLEET_ID, "fleet type error")

		arg_2_0.contextData.form = PreCombatLayer.FORM_EDIT

		FormationMediator.saveEdit()

		local var_10_0 = var_2_0 == SYSTEM_DUEL
		local var_10_1 = var_10_0 and ShipStatus.TAG_HIDE_PVP or ShipStatus.TAG_HIDE_NORMAL
		local var_10_2 = var_10_0 and ShipStatus.TAG_BLOCK_PVP or None
		local var_10_3, var_10_4, var_10_5 = FormationMediator.getDockCallbackFuncs(arg_2_0, arg_10_1, arg_10_2, arg_10_3)
		local var_10_6 = {}

		for iter_10_0, iter_10_1 in ipairs(arg_10_2.ships):
			if not arg_10_1 or iter_10_1 != arg_10_1.id:
				table.insert(var_10_6, iter_10_1)

		arg_2_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
			selectedMax = 1,
			useBlackBlock = True,
			selectedMin = 0,
			energyDisplay = True,
			leastLimitMsg = i18n("battle_preCombatMediator_leastLimit"),
			quitTeam = arg_10_1 != None,
			teamFilter = arg_10_3,
			onShip = var_10_3,
			confirmSelect = var_10_4,
			onSelected = var_10_5,
			hideTagFlags = var_10_1,
			blockTagFlags = var_10_2,
			otherSelectedIds = var_10_6
		}))
	arg_2_0.bind(var_0_0.ON_COMMIT_EDIT, function(arg_11_0, arg_11_1)
		arg_2_0.commitEdit(arg_11_1))
	arg_2_0.bind(var_0_0.ON_START, function(arg_12_0, arg_12_1, arg_12_2)
		seriesAsync({
			function(arg_13_0)
				if pg.battle_cost_template[var_2_0].enter_energy_cost == 0:
					arg_13_0()

					return

				local var_13_0
				local var_13_1
				local var_13_2 = getProxy(FleetProxy).getFleetById(arg_12_1)
				local var_13_3 = {}

				for iter_13_0, iter_13_1 in ipairs(var_13_2.ships):
					table.insert(var_13_3, getProxy(BayProxy).getShipById(iter_13_1))

				local var_13_4 = var_13_2.GetName()

				Fleet.EnergyCheck(var_13_3, var_13_4, function(arg_14_0)
					if arg_14_0:
						arg_13_0(), None, var_13_1),
			function(arg_15_0)
				if arg_2_0.contextData.OnConfirm:
					arg_2_0.contextData.OnConfirm(arg_15_0)
				else
					arg_15_0(),
			function()
				arg_2_0.viewComponent.emit(var_0_0.BEGIN_STAGE_PROXY, {
					curFleetId = arg_12_1,
					continuousBattleTimes = arg_12_2
				})
		}))

	local function var_2_1()
		local var_17_0 = 0

		for iter_17_0, iter_17_1 in ipairs(arg_2_0.contextData.fleets):
			local var_17_1 = iter_17_1.GetCostSum().oil
			local var_17_2 = iter_17_0 == 1
			local var_17_3 = arg_2_0.contextData.costLimit[var_17_2 and 1 or 2]

			if var_17_3 > 0:
				var_17_1 = math.min(var_17_1, var_17_3)

			var_17_0 = var_17_0 + var_17_1

		return var_17_0

	arg_2_0.bind(var_0_0.SHOW_CONTINUOUS_OPERATION_WINDOW, function(arg_18_0, arg_18_1)
		arg_2_0.addSubLayers(Context.New({
			mediator = ContinuousOperationWindowMediator,
			viewComponent = ContinuousOperationWindow,
			data = {
				mainFleetId = arg_18_1,
				stageId = arg_2_0.contextData.stageId,
				system = arg_2_0.contextData.system,
				oilCost = var_2_1()
			}
		})))
	arg_2_0.bind(var_0_0.BEGIN_STAGE_PROXY, function(arg_19_0, arg_19_1)
		local var_19_0

		if arg_2_0.contextData.rivalId:
			var_19_0 = arg_2_0.contextData.rivalId
		else
			var_19_0 = arg_2_0.contextData.stageId

		arg_2_0.sendNotification(GAME.BEGIN_STAGE, {
			stageId = var_19_0,
			mainFleetId = arg_19_1.curFleetId,
			system = arg_2_0.contextData.system,
			actId = arg_2_0.contextData.actId,
			rivalId = arg_2_0.contextData.rivalId,
			continuousBattleTimes = arg_19_1.continuousBattleTimes,
			totalBattleTimes = arg_19_1.continuousBattleTimes
		}))

def var_0_0.changeFleet(arg_20_0, arg_20_1):
	if arg_20_0.contextData.system == SYSTEM_SUB_ROUTINE:
		arg_20_0.contextData.subFleetId = arg_20_1
	else
		getProxy(PlayerProxy).combatFleetId = arg_20_1

	arg_20_0.viewComponent.SetCurrentFleet(arg_20_1)
	arg_20_0.viewComponent.UpdateFleetView(True)
	arg_20_0.viewComponent.SetFleetStepper()

def var_0_0.refreshEdit(arg_21_0, arg_21_1):
	local var_21_0 = getProxy(FleetProxy)

	var_21_0.EdittingFleet = arg_21_1

	if arg_21_0.contextData.system != SYSTEM_SUB_ROUTINE:
		local var_21_1 = var_21_0.getData()

		var_21_1[arg_21_1.id] = arg_21_1

		arg_21_0.viewComponent.SetFleets(var_21_1)

	arg_21_0.viewComponent.UpdateFleetView(False)

def var_0_0.commitEdit(arg_22_0, arg_22_1):
	local var_22_0 = getProxy(FleetProxy)
	local var_22_1 = var_22_0.EdittingFleet

	if var_22_1 == None or var_22_1.isFirstFleet() or var_22_1.isLegalToFight() == True:
		var_22_0.commitEdittingFleet(arg_22_1)
	elif #var_22_1.ships == 0:
		var_22_0.commitEdittingFleet(arg_22_1)

		if arg_22_0.contextData.system == SYSTEM_SUB_ROUTINE:
			-- block empty
		else
			arg_22_0.changeFleet(1)
	else
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("ship_formationMediaror_trash_warning", var_22_1.defaultName),
			def onYes:()
				local var_23_0 = getProxy(BayProxy).getRawData()
				local var_23_1 = var_22_1.ships

				for iter_23_0 = #var_23_1, 1, -1:
					var_22_1.removeShip(var_23_0[var_23_1[iter_23_0]])

				if var_22_1.id == FleetProxy.PVP_FLEET_ID:
					var_22_0.commitEdittingFleet()
					arg_22_0.changeFleet(FleetProxy.PVP_FLEET_ID)
				else
					var_22_0.commitEdittingFleet(arg_22_1)
					arg_22_0.changeFleet(1)
		})

def var_0_0.onAutoBtn(arg_24_0, arg_24_1):
	local var_24_0 = arg_24_1.isOn
	local var_24_1 = arg_24_1.toggle

	arg_24_0.sendNotification(GAME.AUTO_BOT, {
		isActiveBot = var_24_0,
		toggle = var_24_1
	})

def var_0_0.onAutoSubBtn(arg_25_0, arg_25_1):
	local var_25_0 = arg_25_1.isOn
	local var_25_1 = arg_25_1.toggle

	arg_25_0.sendNotification(GAME.AUTO_SUB, {
		isActiveSub = var_25_0,
		toggle = var_25_1
	})

def var_0_0.listNotificationInterests(arg_26_0):
	return {
		GAME.BEGIN_STAGE_DONE,
		PlayerProxy.UPDATED,
		GAME.BEGIN_STAGE_ERRO,
		PreCombatMediator.BEGIN_STAGE_PROXY,
		var_0_0.CONTINUOUS_OPERATION
	}

def var_0_0.handleNotification(arg_27_0, arg_27_1):
	local var_27_0 = arg_27_1.getName()
	local var_27_1 = arg_27_1.getBody()

	if var_27_0 == GAME.BEGIN_STAGE_DONE:
		arg_27_0.sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_27_1)
	elif var_27_0 == PlayerProxy.UPDATED:
		arg_27_0.viewComponent.SetPlayerInfo(getProxy(PlayerProxy).getData())
	elif var_27_0 == GAME.BEGIN_STAGE_ERRO:
		if var_27_1 == 3:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				hideNo = True,
				content = i18n("battle_preCombatMediator_timeout"),
				def onYes:()
					arg_27_0.viewComponent.emit(BaseUI.ON_CLOSE)
			})
	elif var_27_0 == PreCombatMediator.BEGIN_STAGE_PROXY:
		arg_27_0.viewComponent.emit(PreCombatMediator.BEGIN_STAGE_PROXY, var_27_1)
	elif var_27_0 == var_0_0.CONTINUOUS_OPERATION:
		arg_27_0.viewComponent.emit(PreCombatMediator.ON_START, var_27_1.mainFleetId, var_27_1.battleTimes)

return var_0_0
