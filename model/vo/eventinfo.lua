local var_0_0 = class("EventInfo", import(".BaseVO"))

var_0_0.StateNone = 0
var_0_0.StateActive = 1
var_0_0.StateFinish = 2

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.id = arg_1_1.id
	arg_1_0.template = pg.collection_template[arg_1_0.id]

	assert(arg_1_0.template, "pg.collection_template>>>" .. arg_1_0.id)

	arg_1_0.finishTime = arg_1_1.finish_time
	arg_1_0.overTime = arg_1_1.over_time
	arg_1_0.shipIds = arg_1_1.ship_id_list or {}
	arg_1_0.ships = {}
	arg_1_0.state = var_0_0.StateNone
	arg_1_0.activityId = arg_1_1.activity_id or 0

	if arg_1_0.finishTime == 0 then
		arg_1_0.state = var_0_0.StateNone
	elseif arg_1_0.finishTime >= pg.TimeMgr.GetInstance():GetServerTime() then
		arg_1_0.state = var_0_0.StateActive
	else
		arg_1_0.state = var_0_0.StateFinish
	end
end

function var_0_0.IsActivityType(arg_2_0)
	return arg_2_0.activityId > 0
end

function var_0_0.IsStarting(arg_3_0)
	return arg_3_0.state ~= var_0_0.StateNone
end

function var_0_0.SetActivityId(arg_4_0, arg_4_1)
	arg_4_0.activityId = arg_4_1
end

function var_0_0.BelongActivity(arg_5_0, arg_5_1)
	return arg_5_0.activityId > 0 and arg_5_0.activityId == arg_5_1
end

function var_0_0.reachNum(arg_6_0)
	return arg_6_0.template.ship_num <= #arg_6_0.ships
end

function var_0_0.reachLevel(arg_7_0)
	return #arg_7_0.ships > 0 and _.any(arg_7_0.ships, function(arg_8_0)
		return arg_8_0.level >= arg_7_0.template.ship_lv
	end)
end

function var_0_0.reachTypes(arg_9_0)
	if table.getCount(arg_9_0.ships) == 0 then
		return false
	end

	local var_9_0 = true

	for iter_9_0, iter_9_1 in ipairs(arg_9_0.ships) do
		local var_9_1 = iter_9_1:getShipType()

		if not table.contains(arg_9_0.template.ship_type, var_9_1) then
			var_9_0 = false

			break
		end
	end

	return var_9_0
end

function var_0_0.getOilConsume(arg_10_0)
	return arg_10_0.template.oil or 0
end

function var_0_0.updateTime(arg_11_0)
	local var_11_0 = false

	if arg_11_0.state == var_0_0.StateActive and pg.TimeMgr.GetInstance():GetServerTime() > arg_11_0.finishTime then
		arg_11_0.state = var_0_0.StateFinish
		var_11_0 = true
	end

	return var_11_0
end

function var_0_0.getTypesStr(arg_12_0)
	local var_12_0 = pg.ship_data_by_type
	local var_12_1 = arg_12_0.template.ship_type
	local var_12_2 = false

	if #var_12_1 == #var_12_0.all then
		var_12_2 = true

		for iter_12_0, iter_12_1 in pairs(var_12_0.all) do
			if not table.contains(var_12_1, iter_12_1) then
				var_12_2 = false

				break
			end
		end
	end

	if var_12_2 then
		return i18n("event_type_unlimit")
	else
		local var_12_3 = ""

		for iter_12_2, iter_12_3 in ipairs(ShipType.FilterOverQuZhuType(var_12_1)) do
			local var_12_4 = iter_12_2 == #arg_12_0.template.ship_type and "" or ", "

			var_12_3 = var_12_3 .. var_12_0[iter_12_3].type_name .. var_12_4
		end

		return i18n("event_condition_ship_type", var_12_3)
	end
end

local var_0_1 = "EVENTINFO_FORMATION_KEY_"

function var_0_0.ExistPrevFormation(arg_13_0)
	local var_13_0 = getProxy(PlayerProxy):getRawData().id

	return PlayerPrefs.HasKey(var_0_1 .. var_13_0)
end

function var_0_0.GetPrevFormation(arg_14_0)
	local var_14_0 = getProxy(PlayerProxy):getRawData().id
	local var_14_1 = PlayerPrefs.GetString(var_0_1 .. var_14_0)
	local var_14_2 = string.split(var_14_1, "#")

	return _.map(var_14_2, function(arg_15_0)
		return tonumber(arg_15_0)
	end)
end

function var_0_0.SavePrevFormation(arg_16_0)
	if not arg_16_0:CanRecordPrevFormation() then
		return
	end

	local var_16_0 = _.map(arg_16_0.ships, function(arg_17_0)
		return arg_17_0.id
	end)

	if #var_16_0 == 0 then
		var_16_0 = arg_16_0.shipIds
	end

	local var_16_1 = table.concat(var_16_0, "#")
	local var_16_2 = getProxy(PlayerProxy):getRawData().id

	PlayerPrefs.SetString(var_0_1 .. var_16_2, var_16_1)
	PlayerPrefs.Save()
end

function var_0_0.CanRecordPrevFormation(arg_18_0)
	return arg_18_0.template.oil >= 800
end

function var_0_0.GetCountDownTime(arg_19_0)
	return arg_19_0.state == EventInfo.StateNone and arg_19_0.overTime > 0 and arg_19_0.overTime - pg.TimeMgr.GetInstance():GetServerTime()
end

return var_0_0
