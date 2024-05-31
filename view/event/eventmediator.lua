EventConst = require("view/event/EventConst")

local var_0_0 = class("EventMediator", import("..base.ContextMediator"))

function var_0_0.register(arg_1_0)
	arg_1_0:bind(EventConst.EVEN_USE_PREV_FORMATION, function(arg_2_0, arg_2_1, arg_2_2)
		local var_2_0 = getProxy(EventProxy)
		local var_2_1 = getProxy(BayProxy)
		local var_2_2 = var_2_1:getData()
		local var_2_3 = {}
		local var_2_4 = false
		local var_2_5 = false

		local function var_2_6(arg_3_0)
			for iter_3_0, iter_3_1 in ipairs(arg_2_2) do
				local var_3_0 = arg_3_0[iter_3_1]

				if var_3_0 then
					local var_3_1, var_3_2 = ShipStatus.ShipStatusConflict("inEvent", var_3_0)

					if var_3_1 == ShipStatus.STATE_CHANGE_FAIL then
						var_2_4 = true
					elseif var_3_1 == ShipStatus.STATE_CHANGE_CHECK then
						var_2_5 = true
					else
						table.insert(var_2_3, iter_3_1)
					end
				end
			end

			if var_2_4 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("collect_tip"))
			end

			if var_2_5 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("collect_tip2"))
			end

			var_2_0.selectedEvent = arg_2_1
			var_2_0.selectedEvent.shipIds = var_2_3

			arg_1_0:updateEventList(true)

			var_2_0.selectedEvent = nil
		end

		local var_2_7 = var_2_1:getRawData()

		var_2_6(var_2_7)
	end)
	arg_1_0:bind(EventConst.EVENT_LIST_UPDATE, function(arg_4_0)
		arg_1_0:updateEventList(true)
	end)
	arg_1_0:bind(EventConst.EVENT_OPEN_DOCK, function(arg_5_0, arg_5_1)
		local var_5_0 = getProxy(BayProxy):getRawData()
		local var_5_1 = {}

		for iter_5_0, iter_5_1 in pairs(var_5_0) do
			if not table.contains(arg_5_1.template.ship_type, iter_5_1:getShipType()) or iter_5_1:isActivityNpc() then
				table.insert(var_5_1, iter_5_0)
			end
		end

		local var_5_2 = getProxy(EventProxy)

		var_5_2.selectedEvent = arg_5_1

		local var_5_3, var_5_4, var_5_5 = arg_1_0:getDockCallbackFuncs()

		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
			selectedMax = 6,
			useBlackBlock = true,
			selectedMin = 1,
			ignoredIds = var_5_1,
			selectedIds = var_5_2.selectedEvent and var_5_2.selectedEvent.shipIds or {},
			onShip = var_5_3,
			confirmSelect = var_5_4,
			onSelected = var_5_5,
			leftTopInfo = i18n("word_operation"),
			hideTagFlags = ShipStatus.TAG_HIDE_EVENT,
			blockTagFlags = ShipStatus.TAG_BLOCK_EVENT
		})
	end)
	arg_1_0:bind(EventConst.EVENT_FLUSH_NIGHT, function(arg_6_0)
		arg_1_0:sendNotification(GAME.EVENT_FLUSH_NIGHT)
	end)
	arg_1_0:bind(EventConst.EVENT_START, function(arg_7_0, arg_7_1)
		arg_1_0:sendNotification(GAME.EVENT_START, {
			id = arg_7_1.id,
			shipIds = arg_7_1.shipIds
		})
	end)
	arg_1_0:bind(EventConst.EVENT_GIVEUP, function(arg_8_0, arg_8_1)
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("event_confirm_giveup"),
			onYes = function()
				arg_1_0:sendNotification(GAME.EVENT_GIVEUP, {
					id = arg_8_1.id
				})
			end
		})
	end)
	arg_1_0:bind(EventConst.EVENT_FINISH, function(arg_10_0, arg_10_1)
		arg_1_0:sendNotification(GAME.EVENT_FINISH, {
			id = arg_10_1.id
		})
	end)
	arg_1_0:bind(EventConst.EVENT_RECOMMEND, function(arg_11_0, arg_11_1)
		local var_11_0 = getProxy(EventProxy)

		var_11_0.selectedEvent = arg_11_1

		getProxy(EventProxy):fillRecommendShip(arg_11_1)
		arg_1_0:updateEventList(true, true)

		var_11_0.selectedEvent = nil

		if not arg_11_1:reachNum() then
			pg.TipsMgr.GetInstance():ShowTips(i18n("event_recommend_fail"))
		end
	end)
	arg_1_0:bind(EventConst.EVENT_RECOMMEND_LEVEL1, function(arg_12_0, arg_12_1)
		local var_12_0 = getProxy(EventProxy)

		var_12_0.selectedEvent = arg_12_1

		getProxy(EventProxy):fillRecommendShipLV1(arg_12_1)
		arg_1_0:updateEventList(true, true)

		var_12_0.selectedEvent = nil

		if not arg_12_1:reachNum() then
			pg.TipsMgr.GetInstance():ShowTips(i18n("event_recommend_fail"))
		end
	end)
	arg_1_0:updateEventList(false)
end

function var_0_0.listNotificationInterests(arg_13_0)
	return {
		GAME.EVENT_LIST_UPDATE,
		GAME.EVENT_SHOW_AWARDS
	}
end

function var_0_0.handleNotification(arg_14_0, arg_14_1)
	local var_14_0 = arg_14_1:getName()
	local var_14_1 = arg_14_1:getBody()

	if var_14_0 == GAME.EVENT_LIST_UPDATE then
		arg_14_0:updateEventList(true)
	elseif var_14_0 == GAME.EVENT_SHOW_AWARDS then
		local var_14_2

		var_14_2 = coroutine.wrap(function()
			if #var_14_1.oldShips > 0 then
				arg_14_0.viewComponent:emit(BaseUI.ON_SHIP_EXP, {
					title = pg.collection_template[var_14_1.eventId].title,
					oldShips = var_14_1.oldShips,
					newShips = var_14_1.newShips,
					isCri = var_14_1.isCri
				}, var_14_2)
				coroutine.yield()
			end

			arg_14_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_14_1.awards)
		end)

		var_14_2()
	end
end

function var_0_0.updateEventList(arg_16_0, arg_16_1, arg_16_2)
	local var_16_0 = getProxy(BayProxy)
	local var_16_1 = getProxy(EventProxy)

	var_16_1.virgin = false

	local var_16_2 = var_16_1.eventList

	table.sort(var_16_2, function(arg_17_0, arg_17_1)
		if arg_17_0.state ~= arg_17_1.state then
			return arg_17_0.state > arg_17_1.state
		elseif arg_17_0.template.type ~= arg_17_1.template.type then
			return arg_17_0.template.type > arg_17_1.template.type
		elseif arg_17_0.template.lv ~= arg_17_1.template.lv then
			return arg_17_0.template.lv > arg_17_1.template.lv
		else
			return arg_17_0.id > arg_17_1.id
		end
	end)

	for iter_16_0, iter_16_1 in ipairs(var_16_2) do
		iter_16_1.ships = {}

		if iter_16_1.state == EventInfo.StateNone and iter_16_1 ~= var_16_1.selectedEvent then
			iter_16_1.shipIds = {}
		else
			for iter_16_2 = #iter_16_1.shipIds, 1, -1 do
				local var_16_3 = var_16_0:getShipById(iter_16_1.shipIds[iter_16_2])

				if var_16_3 then
					table.insert(iter_16_1.ships, 1, var_16_3)
				else
					table.remove(iter_16_1.shipIds, iter_16_2)
				end
			end
		end
	end

	var_16_1.busyFleetNums = var_16_1:countBusyFleetNums()

	arg_16_0.viewComponent:updateAll(var_16_1, arg_16_1, arg_16_2)

	if getProxy(SettingsProxy):ShouldShowEventActHelp() and _.any(var_16_2, function(arg_18_0)
		return arg_18_0:IsActivityType()
	end) then
		getProxy(SettingsProxy):MarkEventActHelpFlag()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_act_event.tip
		})
	end
end

function var_0_0.getDockCallbackFuncs(arg_19_0)
	local function var_19_0(arg_20_0, arg_20_1, arg_20_2)
		local var_20_0, var_20_1 = ShipStatus.ShipStatusCheck("inEvent", arg_20_0, arg_20_1)

		if not var_20_0 then
			return var_20_0, var_20_1
		end

		local var_20_2 = getProxy(BayProxy)

		for iter_20_0, iter_20_1 in ipairs(arg_20_2) do
			local var_20_3 = var_20_2:getShipById(iter_20_1)

			if arg_20_0:isSameKind(var_20_3) then
				return false, i18n("ship_formationMediator_changeNameError_sameShip")
			end
		end

		return true
	end

	local function var_19_1(arg_21_0, arg_21_1, arg_21_2)
		arg_21_1()
	end

	local function var_19_2(arg_22_0)
		getProxy(EventProxy).selectedEvent.shipIds = arg_22_0
	end

	return var_19_0, var_19_1, var_19_2
end

return var_0_0
