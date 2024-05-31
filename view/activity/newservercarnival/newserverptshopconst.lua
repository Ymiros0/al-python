﻿NewServerPTShopConst = {}

local var_0_0 = NewServerPTShopConst

var_0_0.ConfigTable = pg.newserver_shop_template

function var_0_0.GetActivity()
	local var_1_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_NEWSERVER_SHOP)

	if var_1_0 and not var_1_0:isEnd() then
		return var_1_0
	end
end

var_0_0.GoodStatu = {
	OnSell = 1,
	Locked = 2,
	SellOut = 3
}

function var_0_0.GetGoodStatu(arg_2_0, arg_2_1)
	arg_2_1 = arg_2_1 or var_0_0.GetActivity()

	if var_0_0.isGoodOnSell(arg_2_0, arg_2_1) then
		return var_0_0.GoodStatu.OnSell
	elseif var_0_0.isGoodSellOut(arg_2_0, arg_2_1) then
		return var_0_0.GoodStatu.SellOut
	elseif var_0_0.isGoodLocked(arg_2_0, arg_2_1) then
		return var_0_0.GoodStatu.Locked
	end
end

function var_0_0.isGoodOnSell(arg_3_0, arg_3_1)
	local var_3_0 = var_0_0.isGoodInTime(arg_3_0, arg_3_1)
	local var_3_1 = arg_3_0:isLeftCount()

	return var_3_0 and var_3_1
end

function var_0_0.isGoodSellOut(arg_4_0, arg_4_1)
	local var_4_0 = var_0_0.isGoodInTime(arg_4_0, arg_4_1)
	local var_4_1 = not arg_4_0:isLeftCount()

	return var_4_0 and var_4_1
end

function var_0_0.isGoodLocked(arg_5_0, arg_5_1)
	return not var_0_0.isGoodInTime(arg_5_0, arg_5_1)
end

function var_0_0.GetAllGoodVOList(arg_6_0)
	arg_6_0 = arg_6_0 or var_0_0.GetActivity()

	local var_6_0 = {}
	local var_6_1 = arg_6_0.data2KeyValueList

	for iter_6_0, iter_6_1 in pairs(var_6_1) do
		local var_6_2 = NewServerPTGood.New(iter_6_0)

		var_6_2:updateAllInfo(arg_6_0)
		table.insert(var_6_0, var_6_2)
	end

	return var_6_0
end

function var_0_0.GetGoodVOListByIndex(arg_7_0, arg_7_1, arg_7_2)
	arg_7_1 = arg_7_1 or var_0_0.GetActivity()
	arg_7_2 = arg_7_2 or var_0_0.GetAllGoodVOList()

	local var_7_0 = {}

	for iter_7_0, iter_7_1 in ipairs(arg_7_2) do
		if iter_7_1:getUnlockIndex() == arg_7_0 then
			table.insert(var_7_0, iter_7_1)
		end
	end

	return var_7_0
end

function var_0_0.SortGoodVOList(arg_8_0, arg_8_1)
	arg_8_1 = arg_8_1 or var_0_0.GetActivity()

	local function var_8_0(arg_9_0, arg_9_1)
		local var_9_0 = arg_9_0:getUnlockIndex()
		local var_9_1 = arg_9_1:getUnlockIndex()
		local var_9_2 = var_0_0.GetGoodStatu(arg_9_0, arg_8_1)
		local var_9_3 = var_0_0.GetGoodStatu(arg_9_1, arg_8_1)

		if var_9_0 < var_9_1 then
			return true
		elseif var_9_1 < var_9_0 then
			return false
		elseif var_9_0 == var_9_1 then
			if var_9_2 < var_9_3 then
				return true
			elseif var_9_3 < var_9_2 then
				return false
			elseif var_9_2 == var_9_3 then
				return arg_9_0.configID < arg_9_1.configID
			end
		end
	end

	table.sort(arg_8_0, var_8_0)

	return arg_8_0
end

function var_0_0.GetStartTime(arg_10_0)
	arg_10_0 = arg_10_0 or var_0_0.GetActivity()

	return arg_10_0.stopTime - 1814400
end

function var_0_0.GetSecSinceStart(arg_11_0)
	arg_11_0 = arg_11_0 or var_0_0.GetActivity()

	return pg.TimeMgr.GetInstance():GetServerTime() - var_0_0.GetStartTime(arg_11_0)
end

function var_0_0.isGoodInTime(arg_12_0, arg_12_1)
	arg_12_1 = arg_12_1 or var_0_0.GetActivity()

	return var_0_0.GetSecSinceStart(arg_12_1) >= arg_12_0:getConfig("unlock_time")
end

return var_0_0
