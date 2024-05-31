local var_0_0 = class("Favorite", import(".BaseVO"))

var_0_0.STATE_AWARD = 1
var_0_0.STATE_WAIT = 2
var_0_0.STATE_LOCK = 3
var_0_0.STATE_FETCHED = 4

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.configId = arg_1_1.id
	arg_1_0.id = arg_1_0.configId
	arg_1_0.star = arg_1_1.star
end

function var_0_0.bindConfigTable(arg_2_0)
	return pg.storeup_data_template
end

function var_0_0.getStarCount(arg_3_0, arg_3_1)
	local var_3_0 = 0

	for iter_3_0, iter_3_1 in pairs(arg_3_0:getConfig("char_list")) do
		if arg_3_1[iter_3_1] then
			var_3_0 = var_3_0 + arg_3_1[iter_3_1].star
		end
	end

	return var_3_0
end

function var_0_0.getNextAwardIndex(arg_4_0, arg_4_1)
	local var_4_0 = 1

	if arg_4_1[arg_4_0.id] then
		var_4_0 = arg_4_1[arg_4_0.id] + 1
	end

	return var_4_0
end

function var_0_0.isFetchAll(arg_5_0, arg_5_1)
	return (arg_5_1[arg_5_0.id] or 0) >= #arg_5_0:getConfig("level")
end

function var_0_0.canGetRes(arg_6_0, arg_6_1, arg_6_2)
	local var_6_0 = arg_6_0:getNextAwardIndex(arg_6_2)
	local var_6_1 = arg_6_0:getConfig("award_display")
	local var_6_2 = arg_6_0:getStarCount(arg_6_1)
	local var_6_3 = false

	if var_6_0 <= #var_6_1 then
		var_6_3 = true

		if var_6_2 >= arg_6_0:getConfig("level")[var_6_0] then
			return true
		end
	end

	return false, var_6_3
end

function var_0_0.getState(arg_7_0, arg_7_1, arg_7_2)
	local var_7_0 = arg_7_2[arg_7_0.id]
	local var_7_1, var_7_2 = arg_7_0:canGetRes(arg_7_1, arg_7_2)
	local var_7_3 = arg_7_0:isFetchAll(arg_7_2)

	if var_7_1 then
		return var_0_0.STATE_AWARD
	elseif var_7_3 then
		return var_0_0.STATE_FETCHED
	else
		return var_7_2 and var_0_0.STATE_WAIT or var_0_0.STATE_LOCK
	end
end

function var_0_0.getAwardState(arg_8_0, arg_8_1, arg_8_2, arg_8_3)
	local var_8_0 = arg_8_2[arg_8_0.id] or 0
	local var_8_1 = arg_8_0:getConfig("level")
	local var_8_2 = arg_8_0:getConfig("award_display")

	if var_8_1[arg_8_3] <= arg_8_0:getStarCount(arg_8_1) then
		return var_8_0 < arg_8_3 and (var_8_2[arg_8_3] and var_0_0.STATE_AWARD or var_0_0.STATE_LOCK) or var_0_0.STATE_FETCHED
	else
		return var_8_2[arg_8_3] and var_0_0.STATE_WAIT or var_0_0.STATE_LOCK
	end
end

function var_0_0.containShipGroup(arg_9_0, arg_9_1)
	local var_9_0 = arg_9_0:getConfig("award_display")

	return _.any(var_9_0, function(arg_10_0)
		if arg_10_0[1] == DROP_TYPE_SHIP and Ship.New({
			configId = arg_10_0[2]
		}):getGroupId() == arg_9_1 then
			return true
		end

		return false
	end)
end

return var_0_0
