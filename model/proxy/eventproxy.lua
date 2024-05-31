local var_0_0 = class("EventProxy", import(".NetProxy"))

function var_0_0.register(arg_1_0)
	arg_1_0.eventList = {}

	arg_1_0:on(13002, function(arg_2_0)
		arg_1_0.maxFleetNums = arg_2_0.max_team

		arg_1_0:updateInfo(arg_2_0.collection_list)
	end)
	arg_1_0:on(13011, function(arg_3_0)
		for iter_3_0, iter_3_1 in ipairs(arg_3_0.collection) do
			local var_3_0 = EventInfo.New(iter_3_1)
			local var_3_1, var_3_2 = arg_1_0:findInfoById(iter_3_1.id)

			if var_3_2 == -1 then
				table.insert(arg_1_0.eventList, var_3_0)

				arg_1_0.eventForMsg = var_3_0
			else
				arg_1_0.eventList[var_3_2] = var_3_0
			end
		end

		arg_1_0.virgin = true

		pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inEvent")
		arg_1_0.facade:sendNotification(GAME.EVENT_LIST_UPDATE)
	end)

	arg_1_0.timer = Timer.New(function()
		arg_1_0:updateTime()
	end, 1, -1)

	arg_1_0.timer:Start()
end

function var_0_0.remove(arg_5_0)
	if arg_5_0.timer then
		arg_5_0.timer:Stop()

		arg_5_0.timer = nil
	end
end

function var_0_0.updateInfo(arg_6_0, arg_6_1)
	arg_6_0.eventList = {}

	for iter_6_0, iter_6_1 in ipairs(arg_6_1) do
		table.insert(arg_6_0.eventList, EventInfo.New(iter_6_1))
	end

	pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inEvent")
	arg_6_0.facade:sendNotification(GAME.EVENT_LIST_UPDATE)
end

function var_0_0.updateNightInfo(arg_7_0, arg_7_1)
	for iter_7_0, iter_7_1 in ipairs(arg_7_1) do
		table.insert(arg_7_0.eventList, EventInfo.New(iter_7_1))
	end

	pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inEvent")
	arg_7_0.facade:sendNotification(GAME.EVENT_LIST_UPDATE)
end

function var_0_0.getActiveShipIds(arg_8_0)
	local var_8_0 = {}

	for iter_8_0, iter_8_1 in ipairs(arg_8_0.eventList) do
		if iter_8_1.state ~= EventInfo.StateNone then
			for iter_8_2, iter_8_3 in ipairs(iter_8_1.shipIds) do
				table.insert(var_8_0, iter_8_3)
			end
		end
	end

	return var_8_0
end

function var_0_0.findInfoById(arg_9_0, arg_9_1)
	for iter_9_0, iter_9_1 in ipairs(arg_9_0.eventList) do
		if iter_9_1.id == arg_9_1 then
			return iter_9_1, iter_9_0
		end
	end

	return nil, -1
end

function var_0_0.countByState(arg_10_0, arg_10_1)
	local var_10_0 = 0

	for iter_10_0, iter_10_1 in ipairs(arg_10_0.eventList) do
		if iter_10_1.state == arg_10_1 then
			var_10_0 = var_10_0 + 1
		end
	end

	return var_10_0
end

function var_0_0.hasFinishState(arg_11_0)
	if arg_11_0:countByState(EventInfo.StateFinish) > 0 then
		return true
	end
end

function var_0_0.countBusyFleetNums(arg_12_0)
	local var_12_0 = 0

	for iter_12_0, iter_12_1 in ipairs(arg_12_0.eventList) do
		if not iter_12_1:IsActivityType() and iter_12_1.state ~= EventInfo.StateNone then
			var_12_0 = var_12_0 + 1
		end
	end

	return var_12_0
end

function var_0_0.updateTime(arg_13_0)
	local var_13_0 = false

	for iter_13_0, iter_13_1 in pairs(arg_13_0.eventList) do
		if iter_13_1:updateTime() then
			var_13_0 = true
		end
	end

	if var_13_0 then
		pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inEvent")
		arg_13_0:sendNotification(GAME.EVENT_LIST_UPDATE)
	end
end

function var_0_0.getEventList(arg_14_0)
	return Clone(arg_14_0.eventList)
end

function var_0_0.getActiveEvents(arg_15_0)
	local var_15_0 = {}

	for iter_15_0, iter_15_1 in ipairs(arg_15_0.eventList) do
		if iter_15_1.finishTime >= pg.TimeMgr.GetInstance():GetServerTime() then
			table.insert(var_15_0, iter_15_1)
		end
	end

	return var_15_0
end

function var_0_0.fillRecommendShip(arg_16_0, arg_16_1)
	local var_16_0 = getProxy(BayProxy):getDelegationRecommendShips(arg_16_1)

	for iter_16_0, iter_16_1 in ipairs(var_16_0) do
		table.insert(arg_16_1.shipIds, iter_16_1)
	end
end

function var_0_0.fillRecommendShipLV1(arg_17_0, arg_17_1)
	local var_17_0 = getProxy(BayProxy):getDelegationRecommendShipsLV1(arg_17_1)

	for iter_17_0, iter_17_1 in ipairs(var_17_0) do
		table.insert(arg_17_1.shipIds, iter_17_1)
	end
end

function var_0_0.checkNightEvent(arg_18_0)
	local var_18_0 = pg.TimeMgr.GetInstance():GetServerHour()

	return (var_18_0 >= pg.gameset.night_collection_begin.key_value and var_18_0 < 24 or var_18_0 >= 0 and var_18_0 < pg.gameset.night_collection_end.key_value) and not _.any(arg_18_0.eventList, function(arg_19_0)
		local var_19_0 = arg_19_0:GetCountDownTime()

		return arg_19_0.template.type == EventConst.EVENT_TYPE_NIGHT and (not var_19_0 or var_19_0 > 0)
	end)
end

function var_0_0.AddActivityEvents(arg_20_0, arg_20_1, arg_20_2)
	for iter_20_0 = #arg_20_0.eventList, 1, -1 do
		local var_20_0 = arg_20_0.eventList[iter_20_0]

		if var_20_0:IsActivityType() and var_20_0:BelongActivity(arg_20_2) then
			table.remove(arg_20_0.eventList, iter_20_0)
		end
	end

	for iter_20_1, iter_20_2 in ipairs(arg_20_1) do
		print("add collection-----------", iter_20_2.id)
		table.insert(arg_20_0.eventList, iter_20_2)
	end

	pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inEvent")
end

function var_0_0.AddActivityEvent(arg_21_0, arg_21_1)
	print("zero add collection-----------", arg_21_1.id)
	table.insert(arg_21_0.eventList, arg_21_1)
end

function var_0_0.CanJoinEvent(arg_22_0, arg_22_1)
	if not arg_22_1:reachNum() then
		return false, i18n("event_minimus_ship_numbers", arg_22_1.template.ship_num)
	end

	if not arg_22_1:reachLevel() then
		return false, i18n("event_level_unreached")
	end

	if not arg_22_1:reachTypes() then
		return false, i18n("event_type_unreached")
	end

	if not arg_22_1:IsActivityType() and arg_22_0.busyFleetNums >= arg_22_0.maxFleetNums then
		pg.TipsMgr.GetInstance():ShowTips(i18n("event_fleet_busy"))

		return
	end

	local var_22_0 = arg_22_1:GetCountDownTime()

	if var_22_0 and var_22_0 < 0 then
		return false, i18n("event_over_time_expired")
	end

	local var_22_1 = getProxy(PlayerProxy):getData()

	if arg_22_1:getOilConsume() > var_22_1.oil then
		local var_22_2

		if not ItemTipPanel.ShowOilBuyTip(arg_22_1:getOilConsume()) then
			var_22_2 = i18n("common_no_oil")
		end

		return false, var_22_2
	end

	local var_22_3 = pg.collection_template[arg_22_1.id]

	if var_22_3 then
		local var_22_4 = var_22_3.drop_oil_max or 0

		if var_22_1:OilMax(var_22_4) then
			return false, i18n("oil_max_tip_title") .. i18n("resource_max_tip_eventstart")
		end

		local var_22_5 = var_22_3.drop_gold_max or 0

		if var_22_1:GoldMax(var_22_5) then
			return false, i18n("gold_max_tip_title") .. i18n("resource_max_tip_eventstart")
		end
	end

	return true
end

function var_0_0.CanFinishEvent(arg_23_0, arg_23_1)
	local var_23_0 = arg_23_1.template

	if not var_23_0 then
		return false
	end

	local var_23_1 = getProxy(PlayerProxy):getData()
	local var_23_2 = var_23_0.drop_oil_max or 0

	if var_23_1:OilMax(var_23_2) then
		return false, i18n("oil_max_tip_title") .. i18n("resource_max_tip_event")
	end

	local var_23_3 = var_23_0.drop_gold_max or 0

	if var_23_1:GoldMax(var_23_3) then
		return false, i18n("gold_max_tip_title") .. i18n("resource_max_tip_event")
	end

	return true
end

function var_0_0.GetEventByActivityId(arg_24_0, arg_24_1)
	for iter_24_0, iter_24_1 in ipairs(arg_24_0.eventList) do
		if iter_24_1:BelongActivity(arg_24_1) then
			return iter_24_1, iter_24_0
		end
	end
end

function var_0_0.GetEventListForCommossionInfo(arg_25_0)
	local var_25_0 = arg_25_0:getEventList()
	local var_25_1 = 0
	local var_25_2 = 0
	local var_25_3 = 0
	local var_25_4 = 0
	local var_25_5 = 0
	local var_25_6 = 0
	local var_25_7 = {}

	_.each(var_25_0, function(arg_26_0)
		if arg_26_0:IsActivityType() then
			if arg_26_0.state == EventInfo.StateNone then
				var_25_6 = var_25_6 + 1
			elseif arg_26_0.state == EventInfo.StateActive then
				var_25_5 = var_25_5 + 1
			elseif arg_26_0.state == EventInfo.StateFinish then
				var_25_4 = var_25_4 + 1
			end
		elseif arg_26_0.state == EventInfo.StateNone then
			-- block empty
		elseif arg_26_0.state == EventInfo.StateActive then
			var_25_2 = var_25_2 + 1

			table.insert(var_25_7, arg_26_0)
		elseif arg_26_0.state == EventInfo.StateFinish then
			var_25_1 = var_25_1 + 1

			table.insert(var_25_7, arg_26_0)
		end
	end)

	local var_25_8 = var_25_1 + var_25_4
	local var_25_9 = var_25_2 + var_25_5
	local var_25_10 = arg_25_0.maxFleetNums - (var_25_1 + var_25_2) + var_25_6

	return var_25_7, var_25_8, var_25_9, var_25_10
end

return var_0_0
