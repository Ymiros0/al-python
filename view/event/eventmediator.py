EventConst = require("view/event/EventConst")

local var_0_0 = class("EventMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	arg_1_0.bind(EventConst.EVEN_USE_PREV_FORMATION, function(arg_2_0, arg_2_1, arg_2_2)
		local var_2_0 = getProxy(EventProxy)
		local var_2_1 = getProxy(BayProxy)
		local var_2_2 = var_2_1.getData()
		local var_2_3 = {}
		local var_2_4 = False
		local var_2_5 = False

		local function var_2_6(arg_3_0)
			for iter_3_0, iter_3_1 in ipairs(arg_2_2):
				local var_3_0 = arg_3_0[iter_3_1]

				if var_3_0:
					local var_3_1, var_3_2 = ShipStatus.ShipStatusConflict("inEvent", var_3_0)

					if var_3_1 == ShipStatus.STATE_CHANGE_FAIL:
						var_2_4 = True
					elif var_3_1 == ShipStatus.STATE_CHANGE_CHECK:
						var_2_5 = True
					else
						table.insert(var_2_3, iter_3_1)

			if var_2_4:
				pg.TipsMgr.GetInstance().ShowTips(i18n("collect_tip"))

			if var_2_5:
				pg.TipsMgr.GetInstance().ShowTips(i18n("collect_tip2"))

			var_2_0.selectedEvent = arg_2_1
			var_2_0.selectedEvent.shipIds = var_2_3

			arg_1_0.updateEventList(True)

			var_2_0.selectedEvent = None

		local var_2_7 = var_2_1.getRawData()

		var_2_6(var_2_7))
	arg_1_0.bind(EventConst.EVENT_LIST_UPDATE, function(arg_4_0)
		arg_1_0.updateEventList(True))
	arg_1_0.bind(EventConst.EVENT_OPEN_DOCK, function(arg_5_0, arg_5_1)
		local var_5_0 = getProxy(BayProxy).getRawData()
		local var_5_1 = {}

		for iter_5_0, iter_5_1 in pairs(var_5_0):
			if not table.contains(arg_5_1.template.ship_type, iter_5_1.getShipType()) or iter_5_1.isActivityNpc():
				table.insert(var_5_1, iter_5_0)

		local var_5_2 = getProxy(EventProxy)

		var_5_2.selectedEvent = arg_5_1

		local var_5_3, var_5_4, var_5_5 = arg_1_0.getDockCallbackFuncs()

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
			selectedMax = 6,
			useBlackBlock = True,
			selectedMin = 1,
			ignoredIds = var_5_1,
			selectedIds = var_5_2.selectedEvent and var_5_2.selectedEvent.shipIds or {},
			onShip = var_5_3,
			confirmSelect = var_5_4,
			onSelected = var_5_5,
			leftTopInfo = i18n("word_operation"),
			hideTagFlags = ShipStatus.TAG_HIDE_EVENT,
			blockTagFlags = ShipStatus.TAG_BLOCK_EVENT
		}))
	arg_1_0.bind(EventConst.EVENT_FLUSH_NIGHT, function(arg_6_0)
		arg_1_0.sendNotification(GAME.EVENT_FLUSH_NIGHT))
	arg_1_0.bind(EventConst.EVENT_START, function(arg_7_0, arg_7_1)
		arg_1_0.sendNotification(GAME.EVENT_START, {
			id = arg_7_1.id,
			shipIds = arg_7_1.shipIds
		}))
	arg_1_0.bind(EventConst.EVENT_GIVEUP, function(arg_8_0, arg_8_1)
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("event_confirm_giveup"),
			def onYes:()
				arg_1_0.sendNotification(GAME.EVENT_GIVEUP, {
					id = arg_8_1.id
				})
		}))
	arg_1_0.bind(EventConst.EVENT_FINISH, function(arg_10_0, arg_10_1)
		arg_1_0.sendNotification(GAME.EVENT_FINISH, {
			id = arg_10_1.id
		}))
	arg_1_0.bind(EventConst.EVENT_RECOMMEND, function(arg_11_0, arg_11_1)
		local var_11_0 = getProxy(EventProxy)

		var_11_0.selectedEvent = arg_11_1

		getProxy(EventProxy).fillRecommendShip(arg_11_1)
		arg_1_0.updateEventList(True, True)

		var_11_0.selectedEvent = None

		if not arg_11_1.reachNum():
			pg.TipsMgr.GetInstance().ShowTips(i18n("event_recommend_fail")))
	arg_1_0.bind(EventConst.EVENT_RECOMMEND_LEVEL1, function(arg_12_0, arg_12_1)
		local var_12_0 = getProxy(EventProxy)

		var_12_0.selectedEvent = arg_12_1

		getProxy(EventProxy).fillRecommendShipLV1(arg_12_1)
		arg_1_0.updateEventList(True, True)

		var_12_0.selectedEvent = None

		if not arg_12_1.reachNum():
			pg.TipsMgr.GetInstance().ShowTips(i18n("event_recommend_fail")))
	arg_1_0.updateEventList(False)

def var_0_0.listNotificationInterests(arg_13_0):
	return {
		GAME.EVENT_LIST_UPDATE,
		GAME.EVENT_SHOW_AWARDS
	}

def var_0_0.handleNotification(arg_14_0, arg_14_1):
	local var_14_0 = arg_14_1.getName()
	local var_14_1 = arg_14_1.getBody()

	if var_14_0 == GAME.EVENT_LIST_UPDATE:
		arg_14_0.updateEventList(True)
	elif var_14_0 == GAME.EVENT_SHOW_AWARDS:
		local var_14_2

		var_14_2 = coroutine.wrap(function()
			if #var_14_1.oldShips > 0:
				arg_14_0.viewComponent.emit(BaseUI.ON_SHIP_EXP, {
					title = pg.collection_template[var_14_1.eventId].title,
					oldShips = var_14_1.oldShips,
					newShips = var_14_1.newShips,
					isCri = var_14_1.isCri
				}, var_14_2)
				coroutine.yield()

			arg_14_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_14_1.awards))

		var_14_2()

def var_0_0.updateEventList(arg_16_0, arg_16_1, arg_16_2):
	local var_16_0 = getProxy(BayProxy)
	local var_16_1 = getProxy(EventProxy)

	var_16_1.virgin = False

	local var_16_2 = var_16_1.eventList

	table.sort(var_16_2, function(arg_17_0, arg_17_1)
		if arg_17_0.state != arg_17_1.state:
			return arg_17_0.state > arg_17_1.state
		elif arg_17_0.template.type != arg_17_1.template.type:
			return arg_17_0.template.type > arg_17_1.template.type
		elif arg_17_0.template.lv != arg_17_1.template.lv:
			return arg_17_0.template.lv > arg_17_1.template.lv
		else
			return arg_17_0.id > arg_17_1.id)

	for iter_16_0, iter_16_1 in ipairs(var_16_2):
		iter_16_1.ships = {}

		if iter_16_1.state == EventInfo.StateNone and iter_16_1 != var_16_1.selectedEvent:
			iter_16_1.shipIds = {}
		else
			for iter_16_2 = #iter_16_1.shipIds, 1, -1:
				local var_16_3 = var_16_0.getShipById(iter_16_1.shipIds[iter_16_2])

				if var_16_3:
					table.insert(iter_16_1.ships, 1, var_16_3)
				else
					table.remove(iter_16_1.shipIds, iter_16_2)

	var_16_1.busyFleetNums = var_16_1.countBusyFleetNums()

	arg_16_0.viewComponent.updateAll(var_16_1, arg_16_1, arg_16_2)

	if getProxy(SettingsProxy).ShouldShowEventActHelp() and _.any(var_16_2, function(arg_18_0)
		return arg_18_0.IsActivityType()):
		getProxy(SettingsProxy).MarkEventActHelpFlag()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_act_event.tip
		})

def var_0_0.getDockCallbackFuncs(arg_19_0):
	local function var_19_0(arg_20_0, arg_20_1, arg_20_2)
		local var_20_0, var_20_1 = ShipStatus.ShipStatusCheck("inEvent", arg_20_0, arg_20_1)

		if not var_20_0:
			return var_20_0, var_20_1

		local var_20_2 = getProxy(BayProxy)

		for iter_20_0, iter_20_1 in ipairs(arg_20_2):
			local var_20_3 = var_20_2.getShipById(iter_20_1)

			if arg_20_0.isSameKind(var_20_3):
				return False, i18n("ship_formationMediator_changeNameError_sameShip")

		return True

	local function var_19_1(arg_21_0, arg_21_1, arg_21_2)
		arg_21_1()

	local function var_19_2(arg_22_0)
		getProxy(EventProxy).selectedEvent.shipIds = arg_22_0

	return var_19_0, var_19_1, var_19_2

return var_0_0
